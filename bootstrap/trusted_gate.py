"""Verify exact PR evidence from a protected default-branch workflow.

This status-writing process reads GitHub API responses and artifact bytes only.
It never checks out, imports, or executes code from the pull request. Its own
workflow must be loaded from protected main. A repository Actions policy must
allow only pull_request_target before its status can be trusted against spoofing.
"""

from __future__ import annotations

import argparse
import base64
import binascii
import hashlib
import io
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import zipfile
import zlib
from pathlib import Path

WORKFLOW_PATH = ".github/workflows/engineering-baseline.yml"
TRUSTED_WORKFLOW_PATH = ".github/workflows/engineering-trusted-gate.yml"
POLICY_PATH = "bootstrap/baseline.py"
GATE_PATH = "bootstrap/trusted_gate.py"
ENGRUN_PATH = "bootstrap/engrun.py"
ENGRUN_SCHEMA_PATH = "bootstrap/engrun.schema.json"
WORKFLOW_NAME = "engineering-candidate"
JOB_NAME = "engineering-baseline"
HARD_CHECKS = frozenset({
    "source_integrity", "unit", "security", "dependencies", "licenses",
    "secrets", "test_integrity", "traceability",
})
MAX_API_BYTES = 2 * 1024 * 1024
MAX_ARTIFACT_BYTES = 2 * 1024 * 1024
MAX_REPORT_BYTES = 1024 * 1024
SHA_RE = re.compile(r"[0-9a-f]{40}\Z")
SHA256_RE = re.compile(r"sha256:([0-9a-f]{64})\Z")
REPO_RE = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z")


class GateError(Exception):
    """A missing, stale, or inconsistent trust-boundary fact."""


def demand(condition: bool, reason: str) -> None:
    if not condition:
        raise GateError(reason)


def sha(value: object, label: str) -> str:
    demand(isinstance(value, str) and SHA_RE.fullmatch(value) is not None, f"invalid {label}")
    return value


def bounded_read(response: object, limit: int) -> bytes:
    data = response.read(limit + 1)  # type: ignore[attr-defined]
    demand(len(data) <= limit, "GitHub response exceeds size limit")
    return data


class GitHubClient:
    """A minimal read-only API client; the artifact CDN never receives the token."""

    def __init__(self, token: str) -> None:
        demand(bool(token), "GITHUB_TOKEN missing")
        self.token = token

    def _request(self, path: str, *, body: dict[str, object] | None = None) -> urllib.request.Request:
        demand(path.startswith("repos/"), "unexpected GitHub API path")
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer " + self.token,
            "User-Agent": "hayool-trusted-gate/1",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        data = None if body is None else json.dumps(body, sort_keys=True).encode("utf-8")
        if data is not None:
            headers["Content-Type"] = "application/json"
        return urllib.request.Request("https://api.github.com/" + path, data=data, headers=headers)

    def get_json(self, path: str) -> dict[str, object]:
        with urllib.request.urlopen(self._request(path), timeout=20) as response:
            value = json.loads(bounded_read(response, MAX_API_BYTES))
        demand(isinstance(value, dict), "GitHub API returned a non-object")
        return value

    def post_json(self, path: str, body: dict[str, object]) -> dict[str, object]:
        with urllib.request.urlopen(self._request(path, body=body), timeout=20) as response:
            value = json.loads(bounded_read(response, MAX_API_BYTES))
        demand(isinstance(value, dict), "GitHub API status response invalid")
        return value

    def get_artifact_zip(self, path: str) -> bytes:
        class NoRedirect(urllib.request.HTTPRedirectHandler):
            def redirect_request(self, request, fp, code, msg, headers, newurl):
                return None

        opener = urllib.request.build_opener(NoRedirect())
        try:
            with opener.open(self._request(path), timeout=20) as response:
                # GitHub normally returns 302, but a direct ZIP response is safe.
                return bounded_read(response, MAX_ARTIFACT_BYTES)
        except urllib.error.HTTPError as error:
            if error.code not in {301, 302, 303, 307, 308}:
                raise
            location = error.headers.get("Location", "")
        parsed = urllib.parse.urlsplit(location)
        demand(parsed.scheme == "https" and bool(parsed.hostname), "unsafe artifact download redirect")
        # The signed download URL is issued by GitHub. Never forward our API token.
        request = urllib.request.Request(location, headers={"User-Agent": "hayool-trusted-gate/1"})
        with urllib.request.urlopen(request, timeout=20) as response:
            return bounded_read(response, MAX_ARTIFACT_BYTES)


def api_content(client: GitHubClient, repo: str, path: str, revision: str) -> bytes:
    encoded = urllib.parse.quote(path, safe="/")
    response = client.get_json(f"repos/{repo}/contents/{encoded}?ref={revision}")
    demand(response.get("type") == "file" and response.get("encoding") == "base64", f"missing GitHub file: {path}")
    content = response.get("content")
    demand(isinstance(content, str), f"invalid GitHub file: {path}")
    data = base64.b64decode(content, validate=False)
    demand(len(data) <= MAX_API_BYTES and response.get("size") == len(data), f"GitHub file size mismatch: {path}")
    git_blob = hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()
    demand(response.get("sha") == git_blob, f"GitHub file blob mismatch: {path}")
    return data


def workflow_tree(client: GitHubClient, repo: str, revision: str) -> list[tuple[str, str, str, str]]:
    """Bind every workflow file, including newly added spoof workflows."""
    response = client.get_json(f"repos/{repo}/git/trees/{revision}?recursive=1")
    demand(response.get("truncated") is False, "GitHub workflow tree is truncated")
    entries = response.get("tree")
    demand(isinstance(entries, list), "GitHub workflow tree missing")
    selected: list[tuple[str, str, str, str]] = []
    for item in entries:
        demand(isinstance(item, dict), "GitHub workflow tree entry invalid")
        path = item.get("path")
        if path == ".github/workflows" or (isinstance(path, str) and path.startswith(".github/workflows/")):
            fields = (path, item.get("mode"), item.get("type"), item.get("sha"))
            demand(all(isinstance(value, str) for value in fields), "GitHub workflow tree metadata invalid")
            selected.append(fields)
    demand(any(item[0] == WORKFLOW_PATH and item[2] == "blob" for item in selected), "approved candidate workflow missing from tree")
    return sorted(selected)


def artifact_report(archive: bytes) -> tuple[dict[str, object], str]:
    try:
        with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
            names = bundle.namelist()
            demand(names == ["baseline.json"], "candidate artifact has unexpected members")
            entry = bundle.getinfo("baseline.json")
            demand(entry.file_size <= MAX_REPORT_BYTES, "candidate report exceeds size limit")
            data = bundle.read(entry)
            demand(len(data) <= MAX_REPORT_BYTES, "candidate report exceeds size limit")
    except (zipfile.BadZipFile, RuntimeError, zlib.error) as exc:
        raise GateError("candidate artifact is not a valid ZIP") from exc
    try:
        report = json.loads(data)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise GateError("candidate report is not valid JSON") from exc
    demand(isinstance(report, dict), "candidate report is not an object")
    return report, hashlib.sha256(data).hexdigest()


def evaluate(event: dict[str, object], repo: str, policy_sha: str, client: GitHubClient) -> dict[str, object]:
    """Return a PASS report only when every live API and artifact binding agrees."""
    demand(REPO_RE.fullmatch(repo) is not None, "invalid repository")
    sha(policy_sha, "policy SHA")
    demand(event.get("action") == "completed", "workflow_run event is not completed")
    event_run = event.get("workflow_run")
    demand(isinstance(event_run, dict), "workflow_run payload missing")
    run_id = event_run.get("id")
    demand(isinstance(run_id, int) and run_id > 0, "workflow run ID missing")
    run = client.get_json(f"repos/{repo}/actions/runs/{run_id}")
    demand(run.get("id") == run_id, "workflow run ID mismatch")
    demand(run.get("repository", {}).get("full_name") == repo, "workflow repository mismatch")
    demand(run.get("event") == "pull_request", "candidate run has wrong event")
    run_path = run.get("path")
    demand(run.get("name") == WORKFLOW_NAME and isinstance(run_path, str) and run_path.split("@", 1)[0] == WORKFLOW_PATH, "candidate workflow identity mismatch")
    demand(run.get("status") == "completed" and run.get("conclusion") == "success", "candidate workflow did not succeed")
    demand(event_run.get("head_sha") == run.get("head_sha") and event_run.get("conclusion") == run.get("conclusion"), "workflow event differs from live API")
    head_sha = sha(run.get("head_sha"), "head SHA")
    demand(run.get("head_repository", {}).get("full_name") == repo, "forked candidate is outside M0 scope")
    attempt = run.get("run_attempt")
    demand(isinstance(attempt, int) and attempt >= 1, "run attempt missing")
    demand(event_run.get("run_attempt") == attempt, "workflow event is from a stale run attempt")
    linked = run.get("pull_requests")
    demand(isinstance(linked, list) and len(linked) == 1, "candidate run must bind one PR")
    pr_number = linked[0].get("number") if isinstance(linked[0], dict) else None
    demand(isinstance(pr_number, int) and pr_number > 0, "PR number missing")
    pr = client.get_json(f"repos/{repo}/pulls/{pr_number}")
    demand(pr.get("number") == pr_number and pr.get("state") == "open", "linked PR is not open")
    demand(pr.get("head", {}).get("sha") == head_sha, "PR head advanced after candidate run")
    demand(pr.get("base", {}).get("ref") == "main" and pr.get("base", {}).get("sha") == policy_sha, "PR base/policy SHA mismatch")
    demand(linked[0].get("base", {}).get("sha") == policy_sha and linked[0].get("head", {}).get("sha") == head_sha, "run PR base/head binding mismatch")
    branch = client.get_json(f"repos/{repo}/git/ref/heads/main")
    demand(branch.get("object", {}).get("sha") == policy_sha, "policy SHA is no longer current main")

    trusted_tree = workflow_tree(client, repo, policy_sha)
    candidate_tree = workflow_tree(client, repo, head_sha)
    demand(candidate_tree == trusted_tree, "candidate workflow tree differs from trusted policy")
    workflow = api_content(client, repo, WORKFLOW_PATH, policy_sha)
    candidate_workflow = api_content(client, repo, WORKFLOW_PATH, head_sha)
    demand(candidate_workflow == workflow, "candidate workflow differs from trusted policy bytes")
    policy = api_content(client, repo, POLICY_PATH, policy_sha)
    candidate_policy = api_content(client, repo, POLICY_PATH, head_sha)
    demand(candidate_policy == policy, "candidate baseline policy differs from trusted policy bytes")
    gate_code = api_content(client, repo, GATE_PATH, policy_sha)
    candidate_gate_code = api_content(client, repo, GATE_PATH, head_sha)
    demand(candidate_gate_code == gate_code, "candidate trusted gate differs from trusted policy bytes")
    engrun_code = api_content(client, repo, ENGRUN_PATH, policy_sha)
    candidate_engrun_code = api_content(client, repo, ENGRUN_PATH, head_sha)
    demand(candidate_engrun_code == engrun_code, "candidate ENG-RUN evaluator differs from trusted policy bytes")
    engrun_schema = api_content(client, repo, ENGRUN_SCHEMA_PATH, policy_sha)
    candidate_engrun_schema = api_content(client, repo, ENGRUN_SCHEMA_PATH, head_sha)
    demand(candidate_engrun_schema == engrun_schema, "candidate ENG-RUN schema differs from trusted policy bytes")

    jobs = client.get_json(f"repos/{repo}/actions/runs/{run_id}/jobs?per_page=100")
    rows = jobs.get("jobs")
    demand(isinstance(rows, list) and jobs.get("total_count") == len(rows), "candidate job list incomplete")
    selected = [row for row in rows if isinstance(row, dict) and row.get("name") == JOB_NAME]
    demand(len(selected) == 1 and selected[0].get("conclusion") == "success", "candidate hard-check job missing or failed")
    job = selected[0]
    demand(job.get("head_sha") == head_sha, "candidate job SHA mismatch")
    check_id = job.get("id")
    demand(isinstance(check_id, int) and check_id > 0, "candidate check ID missing")
    check = client.get_json(f"repos/{repo}/check-runs/{check_id}")
    demand(check.get("id") == check_id and check.get("name") == JOB_NAME, "candidate check identity mismatch")
    demand(check.get("head_sha") == head_sha and check.get("conclusion") == "success", "candidate check SHA/conclusion mismatch")
    demand(check.get("app", {}).get("slug") == "github-actions", "candidate check is not from GitHub Actions")
    demand(check.get("check_suite", {}).get("id") == run.get("check_suite_id"), "candidate check suite mismatch")

    listing = client.get_json(f"repos/{repo}/actions/runs/{run_id}/artifacts?per_page=100")
    artifacts = listing.get("artifacts")
    demand(isinstance(artifacts, list) and listing.get("total_count") == len(artifacts), "candidate artifact list incomplete")
    expected_name = f"engineering-baseline-{head_sha}"
    selected_artifacts = [row for row in artifacts if isinstance(row, dict) and row.get("name") == expected_name]
    demand(len(selected_artifacts) == 1, "candidate evidence artifact missing or duplicated")
    artifact = selected_artifacts[0]
    artifact_id = artifact.get("id")
    demand(isinstance(artifact_id, int) and artifact_id > 0 and artifact.get("expired") is False, "candidate artifact expired or invalid")
    demand(isinstance(artifact.get("size_in_bytes"), int) and artifact["size_in_bytes"] <= MAX_ARTIFACT_BYTES, "candidate artifact exceeds size limit")
    origin = artifact.get("workflow_run")
    demand(isinstance(origin, dict) and origin.get("id") == run_id and origin.get("head_sha") == head_sha, "candidate artifact origin mismatch")
    digest = artifact.get("digest")
    demand(isinstance(digest, str) and SHA256_RE.fullmatch(digest) is not None, "candidate artifact digest missing")
    archive = client.get_artifact_zip(f"repos/{repo}/actions/artifacts/{artifact_id}/zip")
    demand(hashlib.sha256(archive).hexdigest() == digest[7:], "candidate artifact digest mismatch")
    baseline, baseline_digest = artifact_report(archive)
    demand(baseline.get("schema_version") == 1 and baseline.get("policy_source") == "base", "candidate report used untrusted policy")
    demand(baseline.get("base_sha") == policy_sha and baseline.get("target_sha") == head_sha, "candidate report SHA binding mismatch")
    demand(baseline.get("workspace_clean") is True, "candidate checkout was not clean")
    checks = baseline.get("checks")
    errors = baseline.get("errors")
    demand(isinstance(checks, dict) and set(checks) == HARD_CHECKS and all(v == "PASS" for v in checks.values()), "candidate hard checks incomplete or failed")
    demand(isinstance(errors, dict) and set(errors) == HARD_CHECKS and all(v == [] for v in errors.values()), "candidate hard-check errors conflict with PASS")

    return {
        "schema_version": 1,
        "decision": "PASS",
        "github_api_verified": True,
        "repository": repo,
        "pr_number": pr_number,
        "base_sha": policy_sha,
        "head_sha": head_sha,
        "policy_sha": policy_sha,
        "candidate_run_id": run_id,
        "candidate_run_attempt": attempt,
        "candidate_check_run_id": check_id,
        "candidate_artifact_id": artifact_id,
        "candidate_artifact_digest": digest,
        "baseline_json_sha256": baseline_digest,
        "workflow_sha256": hashlib.sha256(workflow).hexdigest(),
        "workflow_tree_sha256": hashlib.sha256(json.dumps(trusted_tree, separators=(",", ":")).encode("utf-8")).hexdigest(),
        "baseline_policy_sha256": hashlib.sha256(policy).hexdigest(),
        "trusted_gate_sha256": hashlib.sha256(gate_code).hexdigest(),
        "engrun_policy_sha256": hashlib.sha256(engrun_code).hexdigest(),
        "engrun_schema_sha256": hashlib.sha256(engrun_schema).hexdigest(),
        "checks": {name: "PASS" for name in sorted(HARD_CHECKS)},
        "errors": [],
    }


def target_identity(event: dict[str, object], repo: str, policy_sha: str,
                    client: GitHubClient) -> tuple[int, str]:
    """Resolve the live current PR head, never trusting event text alone."""
    demand(REPO_RE.fullmatch(repo) is not None, "invalid repository")
    sha(policy_sha, "policy SHA")
    event_pr = event.get("pull_request")
    demand(isinstance(event_pr, dict), "PR event missing")
    number = event_pr.get("number")
    demand(isinstance(number, int) and number > 0, "PR number missing")
    pr = client.get_json(f"repos/{repo}/pulls/{number}")
    demand(pr.get("number") == number and pr.get("state") == "open", "PR is not open")
    head = pr.get("head")
    base = pr.get("base")
    demand(isinstance(head, dict) and isinstance(base, dict), "PR head/base missing")
    head_sha = sha(head.get("sha"), "head SHA")
    demand(head.get("repo", {}).get("full_name") == repo, "forked PR is outside M0 scope")
    demand(base.get("ref") == "main" and base.get("sha") == policy_sha, "PR base/policy SHA mismatch")
    demand(event_pr.get("head", {}).get("sha") == head_sha
           and event_pr.get("base", {}).get("sha") == policy_sha,
           "PR event differs from live head/base")
    main_ref = client.get_json(f"repos/{repo}/git/ref/heads/main")
    demand(main_ref.get("object", {}).get("sha") == policy_sha, "policy is no longer current main")
    return number, head_sha


def evaluate_pr_target(event: dict[str, object], repo: str, policy_sha: str,
                       run_id: int, run_attempt: int, client: GitHubClient) -> dict[str, object]:
    """Bind a default-main PR-target run, isolated job, and exact artifact."""
    number, head_sha = target_identity(event, repo, policy_sha, client)
    run = client.get_json(f"repos/{repo}/actions/runs/{run_id}")
    demand(run.get("id") == run_id and run.get("run_attempt") == run_attempt,
           "trusted run ID/attempt mismatch")
    demand(run.get("repository", {}).get("full_name") == repo
           and run.get("event") == "pull_request_target"
           and run.get("head_sha") == policy_sha
           and run.get("head_branch") == "main"
           and str(run.get("path", "")).split("@", 1)[0] == TRUSTED_WORKFLOW_PATH,
           "trusted run is not the protected-main workflow")
    demand(run.get("status") in {"queued", "in_progress", "completed"}, "trusted run status invalid")

    trusted_tree = workflow_tree(client, repo, policy_sha)
    candidate_tree = workflow_tree(client, repo, head_sha)
    demand(candidate_tree == trusted_tree, "candidate workflow tree differs from trusted policy")
    policy_hashes: dict[str, str] = {}
    for path in (WORKFLOW_PATH, TRUSTED_WORKFLOW_PATH, POLICY_PATH, GATE_PATH,
                 ENGRUN_PATH, ENGRUN_SCHEMA_PATH):
        trusted_bytes = api_content(client, repo, path, policy_sha)
        demand(api_content(client, repo, path, head_sha) == trusted_bytes,
               "candidate changed trusted policy bytes: " + path)
        policy_hashes[path] = hashlib.sha256(trusted_bytes).hexdigest()

    jobs = client.get_json(f"repos/{repo}/actions/runs/{run_id}/jobs?per_page=100")
    rows = jobs.get("jobs")
    demand(isinstance(rows, list) and jobs.get("total_count") == len(rows), "trusted job list incomplete")
    candidates = [row for row in rows if isinstance(row, dict) and row.get("name") == "candidate-check"]
    demand(len(candidates) == 1 and candidates[0].get("conclusion") == "success",
           "isolated candidate job missing or failed")
    candidate_job = candidates[0]
    candidate_job_id = candidate_job.get("id")
    demand(isinstance(candidate_job_id, int) and candidate_job_id > 0,
           "candidate job ID missing")
    check = client.get_json(f"repos/{repo}/check-runs/{candidate_job_id}")
    demand(check.get("id") == candidate_job_id and check.get("name") == "candidate-check"
           and check.get("conclusion") == "success"
           and check.get("app", {}).get("slug") == "github-actions"
           and check.get("check_suite", {}).get("id") == run.get("check_suite_id"),
           "isolated candidate check provenance mismatch")

    listing = client.get_json(f"repos/{repo}/actions/runs/{run_id}/artifacts?per_page=100")
    artifacts = listing.get("artifacts")
    demand(isinstance(artifacts, list) and listing.get("total_count") == len(artifacts),
           "trusted artifact list incomplete")
    expected_name = f"engineering-protected-baseline-{head_sha}"
    matching = [row for row in artifacts if isinstance(row, dict) and row.get("name") == expected_name]
    demand(len(matching) == 1, "protected baseline artifact missing or duplicated")
    artifact = matching[0]
    artifact_id = artifact.get("id")
    digest = artifact.get("digest")
    demand(isinstance(artifact_id, int) and artifact_id > 0
           and artifact.get("expired") is False
           and isinstance(artifact.get("size_in_bytes"), int)
           and artifact["size_in_bytes"] <= MAX_ARTIFACT_BYTES
           and isinstance(digest, str) and SHA256_RE.fullmatch(digest) is not None,
           "protected baseline artifact metadata invalid")
    origin = artifact.get("workflow_run")
    demand(isinstance(origin, dict) and origin.get("id") == run_id
           and origin.get("head_sha") == policy_sha,
           "protected baseline artifact origin mismatch")
    archive = client.get_artifact_zip(f"repos/{repo}/actions/artifacts/{artifact_id}/zip")
    demand(hashlib.sha256(archive).hexdigest() == digest[7:], "protected artifact digest mismatch")
    baseline, baseline_sha256 = artifact_report(archive)
    demand(baseline.get("schema_version") == 1 and baseline.get("policy_source") == "base"
           and baseline.get("traceability_source") == "head_commit_message"
           and baseline.get("base_sha") == policy_sha
           and baseline.get("target_sha") == head_sha
           and baseline.get("workspace_clean") is True,
           "protected baseline report SHA/policy mismatch")
    checks = baseline.get("checks")
    errors = baseline.get("errors")
    demand(isinstance(checks, dict) and set(checks) == HARD_CHECKS
           and all(value == "PASS" for value in checks.values())
           and isinstance(errors, dict) and set(errors) == HARD_CHECKS
           and all(value == [] for value in errors.values()),
           "protected baseline hard checks failed or incomplete")
    return {
        "schema_version": 2, "decision": "PASS", "github_api_verified": True,
        "source": "protected_main_pr_target", "repository": repo, "pr_number": number,
        "base_sha": policy_sha, "head_sha": head_sha, "policy_sha": policy_sha,
        "trusted_run_id": run_id, "trusted_run_attempt": run_attempt,
        "candidate_job_id": candidate_job_id, "candidate_artifact_id": artifact_id,
        "candidate_artifact_digest": digest, "baseline_json_sha256": baseline_sha256,
        "workflow_tree_sha256": hashlib.sha256(json.dumps(trusted_tree, separators=(",", ":")).encode()).hexdigest(),
        "policy_hashes": policy_hashes,
        "checks": {name: "PASS" for name in sorted(HARD_CHECKS)}, "errors": [],
    }


def post_target_status(client: GitHubClient, event: dict[str, object], repo: str,
                       policy_sha: str, run_id: int, result: dict[str, object],
                       state: str | None = None) -> None:
    number, head_sha = target_identity(event, repo, policy_sha, client)
    if result.get("decision") == "PASS":
        demand(result.get("pr_number") == number and result.get("head_sha") == head_sha
               and result.get("trusted_run_id") == run_id, "PASS report is not current PR")
    state = state or ("success" if result.get("decision") == "PASS" else "failure")
    demand(state in {"pending", "success", "failure"}, "invalid target status state")
    client.post_json(f"repos/{repo}/statuses/{head_sha}", {
        "state": state, "context": "engineering-trusted-gate-status",
        "description": {"pending": "Protected-main verification in progress",
                        "success": "Protected-main exact-SHA checks verified",
                        "failure": "Protected-main hard gate failed"}[state],
        "target_url": f"https://github.com/{repo}/actions/runs/{run_id}",
    })
    result["head_sha"] = head_sha
    result["trusted_run_id"] = run_id


def require_trusted_artifact(client: GitHubClient, repo: str, run_id: int,
                             policy_sha: str, expected: dict[str, object],
                             first_report: Path) -> None:
    """A PASS cannot be published before the trusted report is preserved."""
    prior = json.loads(first_report.read_text(encoding="utf-8"))
    demand(prior == expected and prior.get("decision") == "PASS",
           "pre-upload and final trusted reports disagree")
    listing = client.get_json(f"repos/{repo}/actions/runs/{run_id}/artifacts?per_page=100")
    rows = listing.get("artifacts")
    demand(isinstance(rows, list) and listing.get("total_count") == len(rows),
           "trusted artifact listing incomplete")
    matches = [row for row in rows if isinstance(row, dict)
               and row.get("name") == f"engineering-trusted-gate-{run_id}"]
    demand(len(matches) == 1, "trusted artifact missing or duplicated")
    artifact = matches[0]
    artifact_id = artifact.get("id")
    digest = artifact.get("digest")
    demand(isinstance(artifact_id, int) and artifact_id > 0
           and artifact.get("expired") is False
           and isinstance(digest, str) and SHA256_RE.fullmatch(digest) is not None
           and artifact.get("workflow_run", {}).get("id") == run_id
           and artifact.get("workflow_run", {}).get("head_sha") == policy_sha,
           "trusted artifact origin invalid")
    archive = client.get_artifact_zip(f"repos/{repo}/actions/artifacts/{artifact_id}/zip")
    demand(hashlib.sha256(archive).hexdigest() == digest[7:],
           "trusted artifact ZIP digest mismatch")
    try:
        with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
            demand(bundle.namelist() == ["trusted-gate.json"],
                   "trusted artifact members invalid")
            data = bundle.read("trusted-gate.json")
    except (zipfile.BadZipFile, RuntimeError, zlib.error) as exc:
        raise GateError("trusted artifact ZIP invalid") from exc
    demand(len(data) <= MAX_REPORT_BYTES and json.loads(data) == expected,
           "trusted artifact content differs from gate decision")


def linked_head_for_failure(event: dict[str, object], repo: str, client: GitHubClient) -> tuple[str, int]:
    """Return a live, current PR head only; never post to a head from event data alone."""
    event_run = event.get("workflow_run")
    demand(isinstance(event_run, dict), "workflow_run payload missing")
    run_id = event_run.get("id")
    demand(isinstance(run_id, int) and run_id > 0, "workflow run ID missing")
    run = client.get_json(f"repos/{repo}/actions/runs/{run_id}")
    head_sha = sha(run.get("head_sha"), "head SHA")
    demand(run.get("id") == run_id and run.get("event") == "pull_request", "failure status run identity mismatch")
    demand(run.get("repository", {}).get("full_name") == repo and event_run.get("head_sha") == head_sha, "failure status repository/head mismatch")
    linked = run.get("pull_requests")
    demand(isinstance(linked, list) and len(linked) == 1 and isinstance(linked[0], dict), "failure status PR link missing")
    pr_number = linked[0].get("number")
    demand(isinstance(pr_number, int) and pr_number > 0, "failure status PR number missing")
    pr = client.get_json(f"repos/{repo}/pulls/{pr_number}")
    demand(pr.get("state") == "open" and pr.get("head", {}).get("sha") == head_sha and pr.get("base", {}).get("ref") == "main", "failure status PR is stale")
    return head_sha, run_id


def post_gate_status(client: GitHubClient, event: dict[str, object], repo: str,
                     result: dict[str, object], state: str | None = None) -> None:
    """Publish pending/success/failure only to a live PR head verified by API."""
    demand(REPO_RE.fullmatch(repo) is not None, "invalid repository for status")
    head_sha, run_id = linked_head_for_failure(event, repo, client)
    if result.get("decision") == "PASS":
        demand(result.get("head_sha") == head_sha and result.get("candidate_run_id") == run_id,
               "PASS report differs from live PR head")
    state = state or ("success" if result.get("decision") == "PASS" else "failure")
    demand(state in {"pending", "success", "failure"}, "invalid gate status state")
    client.post_json(
        f"repos/{repo}/statuses/{head_sha}",
        {"state": state, "context": "engineering-trusted-gate-status",
         "description": {"pending": "Trusted evidence verification in progress",
                         "success": "Trusted workflow_run evidence verified",
                         "failure": "Trusted workflow_run evidence failed"}[state],
         "target_url": f"https://github.com/{repo}/actions/runs/{run_id}"},
    )
    result["head_sha"] = head_sha
    result["candidate_run_id"] = run_id


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    events = parser.add_mutually_exclusive_group(required=True)
    events.add_argument("--event", type=Path, help="legacy workflow_run evidence only")
    events.add_argument("--pr-target-event", type=Path, help="protected-main pull_request_target event")
    parser.add_argument("--repo", required=True)
    parser.add_argument("--policy-sha", required=True)
    parser.add_argument("--run-id", type=int)
    parser.add_argument("--run-attempt", type=int)
    parser.add_argument("--require-trusted-artifact", type=Path,
                        help="pre-upload report; require its uploaded artifact before PASS")
    parser.add_argument("--verify-outcome")
    parser.add_argument("--upload-outcome")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--post-status", action="store_true", help="requires server-side event policy before status is trusted")
    args = parser.parse_args()
    client = None
    event = None
    try:
        event_path = args.pr_target_event or args.event
        assert event_path is not None
        event = json.loads(event_path.read_text(encoding="utf-8"))
        demand(isinstance(event, dict), "workflow event is not an object")
        client = GitHubClient(os.environ.get("GITHUB_TOKEN", ""))
        if args.pr_target_event is not None:
            demand(isinstance(args.run_id, int) and args.run_id > 0
                   and isinstance(args.run_attempt, int) and args.run_attempt > 0,
                   "trusted run ID/attempt missing")
            if args.post_status:
                post_target_status(client, event, args.repo, args.policy_sha, args.run_id,
                                   {"decision": "FAIL"}, state="pending")
            result = evaluate_pr_target(event, args.repo, args.policy_sha,
                                        args.run_id, args.run_attempt, client)
            if args.require_trusted_artifact is not None:
                demand(args.verify_outcome == "success" and args.upload_outcome == "success",
                       "pre-upload verification or artifact upload failed")
                require_trusted_artifact(client, args.repo, args.run_id,
                                         args.policy_sha, result, args.require_trusted_artifact)
        else:
            demand(args.require_trusted_artifact is None, "artifact mode requires PR-target event")
            if args.post_status:
                post_gate_status(client, event, args.repo, {"decision": "FAIL"}, state="pending")
            result = evaluate(event, args.repo, args.policy_sha, client)
    except (GateError, OSError, ValueError, KeyError, AttributeError, TypeError,
            IndexError, binascii.Error, zlib.error, urllib.error.URLError) as exc:
        result = {
            "schema_version": 1, "decision": "FAIL", "github_api_verified": False,
            "repository": args.repo, "policy_sha": args.policy_sha,
            "errors": [str(exc)[:300]],
        }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if args.post_status and client is not None:
        try:
            demand(isinstance(event, dict), "event unavailable for final status")
            if args.pr_target_event is not None:
                demand(isinstance(args.run_id, int), "trusted run ID unavailable")
                post_target_status(client, event, args.repo, args.policy_sha, args.run_id, result)
            else:
                post_gate_status(client, event, args.repo, result)
        except (GateError, OSError, ValueError, AttributeError, TypeError,
                IndexError, urllib.error.URLError) as exc:
            result["decision"] = "FAIL"
            result.setdefault("errors", []).append("GitHub status publication failed: " + str(exc)[:200])
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"decision": result["decision"], "errors": result["errors"]}, sort_keys=True))
    return 0 if result["decision"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
