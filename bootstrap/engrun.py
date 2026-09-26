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


def evaluate(run: dict, root: Path, expected_sha: str) -> list[str]:
    errors: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    require(run.get("schema_version") == 1, "unsupported schema_version")
    require(bool(re.fullmatch(r"ENG-RUN-[A-Za-z0-9_-]+", str(run.get("run_id", "")))), "invalid run_id")
    require(run.get("mode") == "shadow", "M0 runner permits shadow mode only")
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
            review_report = json.loads((root / str(review.get("report_path", ""))).read_text(encoding="utf-8"))
            require(review_report.get("target_sha") == expected_sha and review_report.get("read_only") is True and review_report.get("verdict") == "PASS", f"reviewer {index} report conflicts with attestation")
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


def verify_github_ci(run: dict, root: Path, expected_sha: str) -> list[str]:
    """Authenticate a claimed CI result against the repository's live Actions API."""
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
        if not (
            observed.get("head_sha") == expected_sha
            and observed.get("event") == "pull_request"
            and observed.get("status") == "completed"
            and observed.get("conclusion") == "success"
            and str(observed.get("path", "")).split("@", 1)[0].endswith(".github/workflows/engineering-baseline.yml")
        ):
            return ["GitHub Actions run is not successful for exact SHA and baseline workflow"]
        good_jobs = [
            job for job in jobs
            if job.get("name") == "engineering-baseline"
            and job.get("head_sha", expected_sha) == expected_sha
            and job.get("conclusion") == "success"
            and job.get("steps")
            and all(step.get("conclusion") == "success" for step in job["steps"])
        ]
        if not good_jobs:
            return ["GitHub Actions baseline job did not execute successfully"]
        if not any(
            artifact.get("name") == f"engineering-baseline-{expected_sha}"
            and artifact.get("expired") is False
            for artifact in artifacts
        ):
            return ["GitHub Actions exact-SHA baseline artifact missing"]
        return []
    except (OSError, KeyError, ValueError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
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
