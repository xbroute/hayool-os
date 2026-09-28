"""Small, fail-closed evaluator for a shadow Engineering Run.

The CLI reads GitHub CI state and Git history; it never writes the repository,
calls a model, merges, or deploys. Pure evaluate() checks evidence structure.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

SHA = re.compile(r"^[0-9a-f]{40}$")
REQUIRED_CHECKS = frozenset(
    {"source_integrity", "unit", "security", "dependencies", "licenses", "secrets", "test_integrity", "traceability", "ci"}
)
RISK_ORDER = {"R0": 0, "R1": 1, "R2": 2, "R3": 3, "R4": 4}


def risk_for_path(path: str) -> str:
    p = path.lower().replace("\\", "/")
    if p.startswith(("deploy/production/", "infra/production/")):
        return "R4"
    if p in {"agents.md", "claude.md", "project_state.md", "next_actions.md"}:
        return "R3"
    if p.startswith((".github/", "bootstrap/", "docs/adr/", "docs/requirements/", "docs/security/", "docs/finance/", "docs/engineering/", "docs/owner_", "docs/evidence/")):
        return "R3"
    if p.startswith("archive/") or p in {"package_manifest.json", "source_manifest.json"}:
        return "R3"
    if p.endswith((".py", ".ts", ".tsx", ".js", ".sql", ".tf")):
        return "R2"
    if p.startswith("tests/"):
        return "R2"
    if p.startswith(("samples/", "notes/")) or p in {"readme.md", "readme_fa.md"}:
        return "R0"
    return "R3"  # Unknown content never defaults to low risk.


def _time(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("timestamp must have a timezone")
    return parsed.astimezone(timezone.utc)


def _evidence(root: Path, relative: str, expected: str) -> bool:
    candidate = (root / relative).resolve()
    if not candidate.is_relative_to(root.resolve()) or not candidate.is_file():
        return False
    return hashlib.sha256(candidate.read_bytes()).hexdigest() == expected


def _review_findings(findings: object, expected_sha: str, index: int) -> list[str]:
    """Treat reviewer findings as gate inputs, never as optional prose."""
    if not isinstance(findings, list):
        return [f"reviewer {index} findings missing or invalid"]
    errors: list[str] = []
    seen: set[str] = set()
    for item in findings:
        if not isinstance(item, dict):
            errors.append(f"reviewer {index} finding is not an object")
            continue
        finding_id = item.get("id")
        severity = item.get("severity")
        status = item.get("status")
        if (set(item) - {"id", "severity", "status", "target_sha", "summary", "closure_evidence"}
                or not isinstance(finding_id, str) or not finding_id.strip()
                or finding_id in seen
                or severity not in {"P0", "P1", "P2", "P3"}
                or status not in {"OPEN", "CLOSED"}
                or item.get("target_sha") != expected_sha
                or not isinstance(item.get("summary"), str) or not item["summary"].strip()):
            errors.append(f"reviewer {index} finding malformed, duplicate, or stale")
            continue
        seen.add(finding_id)
        if status == "OPEN" and severity in {"P0", "P1"}:
            errors.append(f"reviewer {index} open {severity} finding: {finding_id}")
        if status == "CLOSED" and severity in {"P0", "P1"} and not (
            isinstance(item.get("closure_evidence"), str) and item["closure_evidence"].strip()
        ):
            errors.append(f"reviewer {index} closed {severity} finding lacks closure evidence: {finding_id}")
    return errors


def evaluate(run: dict, root: Path, expected_sha: str) -> list[str]:
    errors: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    require(run.get("schema_version") == 2, "unsupported schema_version")
    require(bool(re.fullmatch(r"ENG-RUN-[A-Za-z0-9_-]+", str(run.get("run_id", "")))), "invalid run_id")
    require(run.get("mode") == "shadow", "M0 runner permits shadow mode only")
    require(run.get("ci_mode") in {"legacy_workflow_run", "protected_main_pr_target"}, "CI trust mode missing or invalid")
    require(run.get("repository") == "xbroute/hayool-os", "repository mismatch")
    for field in ("base_sha", "target_sha", "policy_sha"):
        require(bool(SHA.fullmatch(str(run.get(field, "")))), f"invalid {field}")
    require(run.get("target_sha") == expected_sha, "stale or wrong target SHA")
    require(run.get("policy_sha") == run.get("base_sha"), "policy must bind to approved base SHA")
    paths = run.get("changed_paths")
    require(isinstance(paths, list) and bool(paths) and all(isinstance(p, str) and p and not p.startswith("/") and ".." not in Path(p).parts for p in paths or []), "invalid changed_paths")
    if isinstance(paths, list) and paths:
        computed = max((risk_for_path(p) for p in paths), key=lambda r: RISK_ORDER[r])
        require(run.get("risk") in RISK_ORDER and RISK_ORDER.get(run.get("risk"), -1) >= RISK_ORDER[computed], f"risk below deterministic {computed}")

    writer = run.get("writer") or {}
    reviewers = run.get("reviewers") or []
    require(isinstance(writer, dict) and bool(writer.get("id")), "one named writer required")
    require(writer.get("branch") == run.get("branch") and str(run.get("branch", "")).startswith("codex/"), "writer branch mismatch")
    require(writer.get("read_only") is False, "writer role invalid")
    require(all(writer.get(k) for k in ("gateway", "requested_provider", "effective_provider", "requested_model", "effective_model")) and writer.get("identity_verified") is True, "writer provider/model identity disclosure missing")
    try:
        decided = _time(run["decided_at"])
        issued = _time(writer["lease_issued_at"])
        expires = _time(writer["lease_expires_at"])
        require(issued <= decided <= expires and (expires - issued).total_seconds() <= 3600, "writer lease expired or unbounded")
    except (KeyError, TypeError, ValueError):
        errors.append("invalid writer lease time")
    require(isinstance(reviewers, list) and len(reviewers) >= 2, "two independent reviewers required")
    ids = [writer.get("id")] + [r.get("id") for r in reviewers if isinstance(r, dict)]
    require(len(ids) == len(set(ids)) and all(ids), "writer/reviewer identities overlap")
    for index, review in enumerate(reviewers):
        if not isinstance(review, dict):
            errors.append(f"reviewer {index} invalid")
            continue
        require(review.get("read_only") is True and review.get("verdict") == "PASS", f"reviewer {index} did not pass read-only")
        require(review.get("target_sha") == expected_sha, f"reviewer {index} stale SHA")
        require(all(review.get(k) for k in ("gateway", "requested_provider", "effective_provider", "requested_model", "effective_model")) and review.get("identity_verified") is True, f"reviewer {index} identity disclosure missing")
        require(_evidence(root, str(review.get("report_path", "")), str(review.get("report_sha256", ""))), f"reviewer {index} report missing or changed")
        try:
            review_path = (root / str(review.get("report_path", ""))).resolve()
            if not review_path.is_relative_to(root.resolve()):
                raise ValueError("review path escaped evidence root")
            review_report = json.loads(review_path.read_text(encoding="utf-8"))
            require(review_report.get("target_sha") == expected_sha and review_report.get("read_only") is True and review_report.get("verdict") == "PASS", f"reviewer {index} report conflicts with attestation")
            require(review_report.get("findings") == review.get("findings"), f"reviewer {index} findings differ from hashed report")
            errors.extend(_review_findings(review_report.get("findings"), expected_sha, index))
        except (OSError, ValueError, AttributeError):
            errors.append(f"reviewer {index} report unreadable")

    checks = run.get("hard_checks") or []
    names = {c.get("name") for c in checks if isinstance(c, dict)}
    require(REQUIRED_CHECKS <= names and len(names) == len(checks), "missing or duplicate hard check")
    for check in checks:
        if not isinstance(check, dict):
            errors.append("invalid hard check")
            continue
        name = check.get("name")
        require(check.get("status") == "PASS" and check.get("target_sha") == expected_sha, f"hard check {name} failed or stale")
        path, digest = str(check.get("report_path", "")), str(check.get("report_sha256", ""))
        require(_evidence(root, path, digest), f"hard check {name} report missing or changed")
        try:
            report = json.loads((root / path).read_text(encoding="utf-8"))
            require(report.get("target_sha") == expected_sha and report.get("base_sha") == run.get("base_sha") and report.get("workspace_clean") is True and report.get("checks", {}).get(name) == "PASS", f"hard check {name} conflicts with report")
            if name == "ci":
                require(report.get("source") == "github_actions" and report.get("conclusion") == "success" and str(report.get("url", "")).startswith("https://github.com/xbroute/hayool-os/actions/runs/"), "GitHub CI proof missing or failed")
        except (OSError, ValueError, AttributeError):
            errors.append(f"hard check {name} report unreadable")

    gate = run.get("trusted_gate")
    require(isinstance(gate, dict), "trusted gate evidence missing")
    if isinstance(gate, dict):
        require(all(type(gate.get(key)) is int and gate[key] > 0 for key in ("run_id", "run_attempt", "artifact_id")), "trusted gate run or artifact identity invalid")
        gate_path = str(gate.get("report_path", ""))
        require(_evidence(root, gate_path, str(gate.get("report_sha256", ""))), "trusted gate report missing or changed")
        try:
            report_path = (root / gate_path).resolve()
            if not report_path.is_relative_to(root.resolve()):
                raise ValueError("trusted gate report escaped evidence root")
            gate_report = json.loads(report_path.read_text(encoding="utf-8"))
            protected = run.get("ci_mode") == "protected_main_pr_target"
            require(
                gate_report.get("schema_version") == (2 if protected else 1)
                and gate_report.get("decision") == "PASS"
                and gate_report.get("github_api_verified") is True
                and (not protected or gate_report.get("source") == "protected_main_pr_target")
                and gate_report.get("repository") == run.get("repository")
                and gate_report.get("base_sha") == run.get("base_sha")
                and gate_report.get("head_sha") == expected_sha
                and gate_report.get("policy_sha") == run.get("policy_sha")
                and (not protected or (gate_report.get("trusted_run_id") == gate.get("run_id")
                                       and gate_report.get("trusted_run_attempt") == gate.get("run_attempt")))
                and gate_report.get("errors") == []
                and isinstance(gate_report.get("checks"), dict)
                and set(gate_report["checks"]) == REQUIRED_CHECKS - {"ci"}
                and all(status == "PASS" for status in gate_report["checks"].values()),
                "trusted gate report failed or has conflicting exact-SHA evidence",
            )
        except (OSError, ValueError, AttributeError, TypeError):
            errors.append("trusted gate report unreadable")

    limits = run.get("limits") or {}
    require(isinstance(limits.get("repair_iterations"), int) and 0 <= limits["repair_iterations"] <= 3, "repair cap exceeded")
    require(isinstance(limits.get("elapsed_seconds"), (int, float)) and 0 <= limits["elapsed_seconds"] <= 3600, "time cap exceeded")
    require(limits.get("external_cost_usd") == 0 and limits.get("external_cost_cap_usd") == 0, "unapproved external cost")
    kill = run.get("kill_switch") or {}
    configured_kill = json.loads((Path(__file__).parent / "kill_switch.json").read_text(encoding="utf-8"))
    require(kill == configured_kill, "kill switch state does not match trusted configuration")
    require(kill.get("engaged") is False, "kill switch engaged")
    require(all(kill.get(k) is False for k in ("autonomous_writes_enabled", "merge_enabled", "deploy_enabled", "external_calls_enabled")), "shadow mode acquired active authority")
    require(run.get("merge_performed") is False and run.get("deployment_performed") is False, "shadow run performed merge/deploy")
    require(run.get("result") == "PASS", "run does not declare PASS")
    return errors


def _github_json(path: str) -> dict:
    raw = subprocess.check_output(
        ["gh", "api", f"repos/xbroute/hayool-os/{path}"], text=True, timeout=30
    )
    value = json.loads(raw)
    if not isinstance(value, dict):
        raise ValueError("GitHub response is not an object")
    return value


def _download_baseline(run_id: str, artifact_name: str) -> dict:
    with tempfile.TemporaryDirectory(prefix="hayool-m0-artifact-") as directory:
        subprocess.run(
            ["gh", "run", "download", run_id, "--repo", "xbroute/hayool-os",
             "--name", artifact_name, "--dir", directory],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, timeout=30,
        )
        return json.loads((Path(directory) / "baseline.json").read_text(encoding="utf-8"))


def _download_trusted(run_id: str, artifact_name: str) -> bytes:
    with tempfile.TemporaryDirectory(prefix="hayool-m0-trusted-") as directory:
        subprocess.run(
            ["gh", "run", "download", run_id, "--repo", "xbroute/hayool-os",
             "--name", artifact_name, "--dir", directory],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, timeout=30,
        )
        return (Path(directory) / "trusted-gate.json").read_bytes()


def _artifact_zip(artifact_id: int) -> bytes:
    """Download exact ZIP bytes so the GitHub artifact digest can be checked."""
    from bootstrap.trusted_gate import GitHubClient

    token = subprocess.check_output(["gh", "auth", "token"], text=True, timeout=10).strip()
    return GitHubClient(token).get_artifact_zip(
        f"repos/xbroute/hayool-os/actions/artifacts/{artifact_id}/zip"
    )


def verify_protected_ci(run: dict, root: Path, expected_sha: str) -> list[str]:
    """Authenticate the completed default-main PR-target run and server policy."""
    try:
        gate = run.get("trusted_gate")
        if not isinstance(gate, dict):
            return ["protected-main trusted gate evidence is absent"]
        run_id = gate["run_id"]
        if type(run_id) is not int or run_id <= 0:
            return ["protected-main run ID is invalid"]
        report_path = (root / str(gate["report_path"])).resolve()
        if not report_path.is_relative_to(root.resolve()):
            return ["trusted gate report escaped evidence root"]
        report_bytes = report_path.read_bytes()
        if hashlib.sha256(report_bytes).hexdigest() != gate.get("report_sha256"):
            return ["protected-main report digest mismatch"]
        report = json.loads(report_bytes)
        pr_number = report.get("pr_number")
        if type(pr_number) is not int or pr_number <= 0:
            return ["protected-main PR number missing"]
        live_pr = _github_json(f"pulls/{pr_number}")
        main_ref = _github_json("git/ref/heads/main")
        if not (
            live_pr.get("state") == "open"
            and live_pr.get("head", {}).get("sha") == expected_sha
            and live_pr.get("head", {}).get("ref") == run.get("branch")
            and live_pr.get("head", {}).get("repo", {}).get("full_name") == run.get("repository")
            and live_pr.get("base", {}).get("ref") == "main"
            and live_pr.get("base", {}).get("sha") == run.get("base_sha")
            and main_ref.get("object", {}).get("sha") == run.get("policy_sha")
        ):
            return ["protected-main PR/head/base/policy is stale or inconsistent"]
        observed = _github_json(f"actions/runs/{run_id}")
        if not (
            observed.get("id") == run_id
            and observed.get("repository", {}).get("full_name") == run.get("repository")
            and observed.get("event") == "pull_request_target"
            and observed.get("head_sha") == run.get("policy_sha")
            and observed.get("head_branch") == "main"
            and observed.get("run_attempt") == gate.get("run_attempt")
            and observed.get("status") == "completed"
            and observed.get("conclusion") == "success"
            and str(observed.get("path", "")).split("@", 1)[0]
                == ".github/workflows/engineering-trusted-gate.yml"
        ):
            return ["protected-main GitHub run is not completed success from exact policy SHA"]
        jobs = _github_json(f"actions/runs/{run_id}/jobs?per_page=100")
        rows = jobs.get("jobs")
        if not isinstance(rows, list) or jobs.get("total_count") != len(rows):
            return ["protected-main job list incomplete"]
        candidate = [j for j in rows if j.get("name") == "candidate-check" and j.get("conclusion") == "success"]
        trusted = [j for j in rows if j.get("name") == "trusted-gate" and j.get("conclusion") == "success"]
        if len(candidate) != 1 or len(trusted) != 1 or candidate[0].get("id") != report.get("candidate_job_id"):
            return ["protected-main isolated or status job failed"]
        artifacts = _github_json(f"actions/runs/{run_id}/artifacts?per_page=100")
        listed = artifacts.get("artifacts")
        if not isinstance(listed, list) or artifacts.get("total_count") != len(listed):
            return ["protected-main artifact list incomplete"]
        names = {
            "baseline": f"engineering-protected-baseline-{expected_sha}",
            "gate": f"engineering-trusted-gate-{run_id}",
        }
        selected = {}
        for kind, name in names.items():
            matches = [a for a in listed if a.get("name") == name]
            if len(matches) != 1:
                return [f"protected-main {kind} artifact missing or duplicated"]
            artifact = matches[0]
            if not (type(artifact.get("id")) is int and artifact["id"] > 0
                    and artifact.get("expired") is False
                    and re.fullmatch(r"sha256:[0-9a-f]{64}", str(artifact.get("digest", "")))
                    and artifact.get("workflow_run", {}).get("id") == run_id
                    and artifact.get("workflow_run", {}).get("head_sha") == run.get("policy_sha")):
                return [f"protected-main {kind} artifact origin/digest invalid"]
            selected[kind] = artifact
        if selected["gate"]["id"] != gate.get("artifact_id"):
            return ["protected-main trusted artifact ID mismatch"]
        from bootstrap.trusted_gate import artifact_report
        baseline_zip = _artifact_zip(selected["baseline"]["id"])
        gate_zip = _artifact_zip(selected["gate"]["id"])
        if (hashlib.sha256(baseline_zip).hexdigest() != selected["baseline"]["digest"][7:]
                or hashlib.sha256(gate_zip).hexdigest() != selected["gate"]["digest"][7:]):
            return ["protected-main artifact ZIP digest mismatch"]
        baseline, baseline_sha = artifact_report(baseline_zip)
        import io
        import zipfile
        with zipfile.ZipFile(io.BytesIO(gate_zip)) as bundle:
            if bundle.namelist() != ["trusted-gate.json"]:
                return ["protected-main trusted artifact members invalid"]
            downloaded_gate = bundle.read("trusted-gate.json")
        if downloaded_gate != report_bytes:
            return ["protected-main trusted artifact differs from retained report"]
        check = next((c for c in run.get("hard_checks", []) if c.get("name") == "source_integrity"), None)
        ci_check = next((c for c in run.get("hard_checks", []) if c.get("name") == "ci"), None)
        if not check or not ci_check:
            return ["protected-main hard-check evidence missing"]
        baseline_path = (root / str(check["report_path"])).resolve()
        ci_path = (root / str(ci_check["report_path"])).resolve()
        if not baseline_path.is_relative_to(root.resolve()) or not ci_path.is_relative_to(root.resolve()):
            return ["protected-main hard-check report escaped evidence root"]
        baseline_bytes = baseline_path.read_bytes()
        ci_report = json.loads(ci_path.read_text(encoding="utf-8"))
        expected_checks = REQUIRED_CHECKS - {"ci"}
        if not (
            baseline == json.loads(baseline_bytes)
            and baseline_sha == hashlib.sha256(baseline_bytes).hexdigest()
            and baseline.get("base_sha") == run.get("base_sha")
            and baseline.get("target_sha") == expected_sha
            and baseline.get("policy_source") == "base"
            and baseline.get("workspace_clean") is True
            and set(baseline.get("checks", {})) == expected_checks
            and all(baseline["checks"][name] == "PASS" for name in expected_checks)
            and report.get("candidate_artifact_id") == selected["baseline"]["id"]
            and report.get("candidate_artifact_digest") == selected["baseline"]["digest"]
            and report.get("baseline_json_sha256") == baseline_sha
            and report.get("trusted_run_id") == run_id
            and report.get("trusted_run_attempt") == observed.get("run_attempt")
            and report.get("head_sha") == expected_sha
            and report.get("policy_sha") == run.get("policy_sha")
            and report.get("decision") == "PASS"
            and report.get("errors") == []
            and ci_report.get("url") == f"https://github.com/xbroute/hayool-os/actions/runs/{run_id}"
            and ci_report.get("conclusion") == "success"
        ):
            return ["protected-main report does not bind exact run, artifact and hard checks"]
        policy = _github_json("actions/policies/5892")
        if not (policy.get("enforcement") == "active"
                and policy.get("conditions", {}).get("workflow_path", {}).get("include") == ["~ALL"]
                and policy.get("conditions", {}).get("workflow_path", {}).get("exclude") == []
                and policy.get("rules") == [{"type": "restrict_action_events", "parameters": {
                    "allowed_events": ["pull_request_target"]}}]):
            return ["server-side Actions event policy is not active and exact"]
        protection = _github_json("branches/main/protection")
        required = protection.get("required_status_checks", {}).get("checks", [])
        if not any(c.get("context") == "engineering-trusted-gate-status" and c.get("app_id") == 15368
                   for c in required) or protection.get("required_status_checks", {}).get("strict") is not True:
            return ["protected main does not require the trusted exact-head status from Actions"]
        statuses = _github_json(f"commits/{expected_sha}/status").get("statuses", [])
        matching = [s for s in statuses if s.get("context") == "engineering-trusted-gate-status"]
        if not matching or not (
            matching[0].get("state") == "success"
            and matching[0].get("target_url") == f"https://github.com/xbroute/hayool-os/actions/runs/{run_id}"
            and matching[0].get("creator", {}).get("login") == "github-actions[bot]"
        ):
            return ["protected-main exact-head status is absent, stale or failed"]
        return []
    except (OSError, KeyError, ValueError, TypeError, AttributeError, IndexError,
            subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return ["protected-main GitHub evidence could not be independently verified"]


def verify_github_ci(run: dict, root: Path, expected_sha: str) -> list[str]:
    """Require both candidate CI and a default-branch trusted verifier run.

    The PR-owned workflow/artifact cannot attest its own policy. The trusted
    workflow must be a separate successful ``workflow_run`` from exact main.
    """
    if run.get("ci_mode") == "protected_main_pr_target":
        return verify_protected_ci(run, root, expected_sha)
    check = next((c for c in run.get("hard_checks", []) if isinstance(c, dict) and c.get("name") == "ci"), None)
    if not check:
        return ["GitHub CI check is absent"]
    try:
        report = json.loads((root / str(check["report_path"])).read_text(encoding="utf-8"))
        url = str(report.get("url", ""))
        match = re.fullmatch(r"https://github\.com/xbroute/hayool-os/actions/runs/([0-9]+)", url)
        if not match:
            return ["GitHub CI run URL is invalid"]
        run_id = match.group(1)
        observed = _github_json(f"actions/runs/{run_id}")
        jobs = _github_json(f"actions/runs/{run_id}/jobs").get("jobs", [])
        artifacts = _github_json(f"actions/runs/{run_id}/artifacts").get("artifacts", [])
        matching_prs = [
            pr for pr in observed.get("pull_requests", [])
            if pr.get("base", {}).get("sha") == run.get("base_sha")
            and pr.get("head", {}).get("sha") == expected_sha
            and pr.get("head", {}).get("ref") == run.get("branch")
            and pr.get("base", {}).get("repo", {}).get("name") == "hayool-os"
        ]
        if not (
            matching_prs
            and observed.get("id") == int(run_id)
            and observed.get("repository", {}).get("full_name") == run.get("repository")
            and observed.get("head_sha") == expected_sha
            and observed.get("event") == "pull_request"
            and observed.get("name") == "engineering-candidate"
            and observed.get("status") == "completed"
            and observed.get("conclusion") == "success"
            and str(observed.get("path", "")).split("@", 1)[0] == ".github/workflows/engineering-baseline.yml"
            and type(observed.get("run_attempt")) is int
        ):
            return ["GitHub Actions run is not successful for exact SHA and baseline workflow"]
        good_jobs = [
            job for job in jobs
            if job.get("name") == "engineering-baseline"
            and job.get("head_sha", expected_sha) == expected_sha
            and job.get("conclusion") == "success"
            and job.get("steps")
            and all(step.get("conclusion") == "success" for step in job["steps"])
            and {"Load policy from PR base", "Run deterministic M0 checks on PR head", "Preserve check evidence"}
                <= {step.get("name") for step in job["steps"] if step.get("conclusion") == "success"}
        ]
        if len(good_jobs) != 1 or type(good_jobs[0].get("id")) is not int:
            return ["GitHub Actions baseline job did not execute successfully"]
        artifact_name = f"engineering-baseline-{expected_sha}"
        selected = [artifact for artifact in artifacts if artifact.get("name") == artifact_name and artifact.get("expired") is False]
        if len(selected) != 1 or type(selected[0].get("id")) is not int or not re.fullmatch(r"sha256:[0-9a-f]{64}", str(selected[0].get("digest", ""))):
            return ["GitHub Actions exact-SHA baseline artifact missing"]
        candidate_artifact = selected[0]
        observed_baseline = _download_baseline(run_id, artifact_name)
        local_check = next(c for c in run["hard_checks"] if c.get("name") == "source_integrity")
        local_baseline_path = (root / local_check["report_path"]).resolve()
        if not local_baseline_path.is_relative_to(root.resolve()):
            return ["baseline report escaped evidence root"]
        local_baseline_bytes = local_baseline_path.read_bytes()
        local_baseline = json.loads(local_baseline_bytes)
        expected_checks = REQUIRED_CHECKS - {"ci"}
        if not (
            observed_baseline.get("base_sha") == run.get("base_sha")
            and observed_baseline.get("target_sha") == expected_sha
            and observed_baseline.get("policy_source") == "base"
            and observed_baseline.get("workspace_clean") is True
            and all(observed_baseline.get("checks", {}).get(name) == "PASS" for name in expected_checks)
            and observed_baseline == local_baseline
        ):
            return ["GitHub Actions baseline artifact conflicts with exact local report"]

        gate = run.get("trusted_gate")
        if not isinstance(gate, dict) or not all(type(gate.get(k)) is int and gate[k] > 0 for k in ("run_id", "run_attempt", "artifact_id")):
            return ["candidate GitHub CI verified; trusted default-branch gate run is absent"]
        gate_path = (root / str(gate["report_path"])).resolve()
        if not gate_path.is_relative_to(root.resolve()):
            return ["trusted gate report escaped evidence root"]
        gate_bytes = gate_path.read_bytes()
        if hashlib.sha256(gate_bytes).hexdigest() != gate.get("report_sha256"):
            return ["trusted gate local report digest mismatch"]
        trusted_report = json.loads(gate_bytes)

        trusted_id = str(gate["run_id"])
        trusted_run = _github_json(f"actions/runs/{trusted_id}")
        trusted_jobs = _github_json(f"actions/runs/{trusted_id}/jobs").get("jobs", [])
        trusted_artifacts = _github_json(f"actions/runs/{trusted_id}/artifacts").get("artifacts", [])
        main_ref = _github_json("git/ref/heads/main")
        if not (
            trusted_run.get("id") == gate["run_id"]
            and trusted_run.get("repository", {}).get("full_name") == run.get("repository")
            and trusted_run.get("event") == "workflow_run"
            and trusted_run.get("head_branch") == "main"
            and trusted_run.get("head_sha") == run.get("policy_sha")
            and trusted_run.get("run_attempt") == gate["run_attempt"]
            and trusted_run.get("status") == "completed"
            and trusted_run.get("conclusion") == "success"
            and str(trusted_run.get("path", "")).split("@", 1)[0] == ".github/workflows/engineering-trusted-gate.yml"
            and main_ref.get("object", {}).get("sha") == run.get("policy_sha")
        ):
            return ["trusted gate was not a successful exact-policy default-branch workflow run"]
        gate_jobs = [
            job for job in trusted_jobs
            if job.get("name") == "trusted-gate"
            and job.get("conclusion") == "success"
            and {"Verify exact candidate evidence with default-branch policy", "Preserve trusted-gate evidence"}
                <= {step.get("name") for step in job.get("steps", []) if step.get("conclusion") == "success"}
        ]
        if len(gate_jobs) != 1:
            return ["trusted gate job did not execute and pass"]
        trusted_artifact_name = f"engineering-trusted-gate-{run_id}"
        selected_gate_artifacts = [
            artifact for artifact in trusted_artifacts
            if artifact.get("name") == trusted_artifact_name
            and artifact.get("id") == gate["artifact_id"]
            and artifact.get("expired") is False
            and artifact.get("workflow_run", {}).get("id") == gate["run_id"]
        ]
        if len(selected_gate_artifacts) != 1:
            return ["trusted gate artifact is missing or has wrong origin"]
        downloaded_gate_bytes = _download_trusted(trusted_id, trusted_artifact_name)
        if downloaded_gate_bytes != gate_bytes:
            return ["trusted gate artifact differs from retained exact report"]
        if not (
            trusted_report.get("schema_version") == 1
            and trusted_report.get("decision") == "PASS"
            and trusted_report.get("github_api_verified") is True
            and trusted_report.get("repository") == run.get("repository")
            and trusted_report.get("pr_number") == matching_prs[0].get("number")
            and trusted_report.get("base_sha") == run.get("base_sha")
            and trusted_report.get("head_sha") == expected_sha
            and trusted_report.get("policy_sha") == run.get("policy_sha")
            and trusted_report.get("candidate_run_id") == int(run_id)
            and trusted_report.get("candidate_run_attempt") == observed.get("run_attempt")
            and trusted_report.get("candidate_check_run_id") == good_jobs[0]["id"]
            and trusted_report.get("candidate_artifact_id") == candidate_artifact["id"]
            and trusted_report.get("candidate_artifact_digest") == candidate_artifact["digest"]
            and trusted_report.get("baseline_json_sha256") == hashlib.sha256(local_baseline_bytes).hexdigest()
            and trusted_report.get("checks") == {name: "PASS" for name in expected_checks}
            and trusted_report.get("errors") == []
        ):
            return ["trusted gate artifact does not bind exact candidate run, policy and hard checks"]
        return []
    except (OSError, KeyError, ValueError, TypeError, AttributeError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return ["GitHub CI could not be verified through the Actions API"]


def verify_changed_paths(run: dict, expected_sha: str) -> list[str]:
    try:
        actual = subprocess.check_output(
            ["git", "diff", "--name-only", run["base_sha"], expected_sha], text=True
        ).splitlines()
        if sorted(set(actual)) != sorted(run.get("changed_paths", [])):
            return ["changed_paths differs from exact base-to-head Git diff"]
        return []
    except (KeyError, OSError, subprocess.CalledProcessError):
        return ["exact base-to-head Git diff unavailable"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_file", type=Path)
    parser.add_argument("--root", type=Path, required=True, help="directory containing immutable evidence files")
    parser.add_argument("--sha", required=True, help="exact commit SHA being decided")
    args = parser.parse_args()
    if not SHA.fullmatch(args.sha):
        parser.error("--sha must be a 40-character lowercase commit SHA")
    run = json.loads(args.run_file.read_text(encoding="utf-8"))
    errors = evaluate(run, args.root, args.sha)
    errors.extend(verify_changed_paths(run, args.sha))
    errors.extend(verify_github_ci(run, args.root, args.sha))
    try:
        head = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
        branch = subprocess.check_output(["git", "branch", "--show-current"], text=True).strip()
        dirty = subprocess.check_output(["git", "status", "--porcelain"], text=True).strip()
        if head != args.sha or branch != run.get("branch") or dirty:
            errors.append("CLI checkout is dirty, wrong branch, or not the target SHA")
    except subprocess.CalledProcessError:
        errors.append("CLI must run in a Git checkout")
    print(json.dumps({"run_id": run.get("run_id"), "target_sha": args.sha, "decision": "FAIL" if errors else "PASS", "errors": errors}, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
