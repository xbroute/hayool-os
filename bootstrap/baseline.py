"""Deterministic M0 checks; runs without third-party Python packages or secrets."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import unittest
import zipfile
from pathlib import Path

ROOT = Path(os.environ.get("HAYOOL_CANDIDATE_ROOT") or Path(__file__).resolve().parents[1]).resolve()
ORIGINAL_ZIP = ROOT / "archive/V7.2/Hayool-OS-V7.2-Final-Source-of-Truth.zip"
ORIGINAL_ZIP_SHA256 = "35054ad417242eda797d81816d81ae10a2bcc44b4a10fcc8784005c7d1d5d700"
PREFIX = "hayool-os-v7.2-final/"
SECRET_PATTERNS = {
    "private_key": re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "github_token": re.compile(rb"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{36}\b"),
    "aws_access_key": re.compile(rb"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
}
ALLOWED_LICENSES = {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC", "PostgreSQL", "MPL-2.0", "CC-BY-4.0", "MIXED", "INTERNAL"}


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def source_integrity() -> list[str]:
    errors: list[str] = []
    if hashlib.sha256(ORIGINAL_ZIP.read_bytes()).hexdigest() != ORIGINAL_ZIP_SHA256:
        return ["original V7.2 ZIP hash mismatch"]
    with zipfile.ZipFile(ORIGINAL_ZIP) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)) or any(not n.startswith(PREFIX) or ".." in Path(n).parts for n in names):
            return ["unsafe or duplicate source ZIP path"]
        manifest = json.loads(archive.read(PREFIX + "PACKAGE_MANIFEST.json"))
        expected = {row["path"] for row in manifest["files"]}
        observed = {n[len(PREFIX):] for n in names if n != PREFIX + "PACKAGE_MANIFEST.json"}
        if expected != observed:
            errors.append("package manifest membership mismatch")
        for row in manifest["files"]:
            data = archive.read(PREFIX + row["path"])
            if len(data) != row["bytes"] or hashlib.sha256(data).hexdigest() != row["sha256"]:
                errors.append("source package hash mismatch: " + row["path"])
        design_digest = hashlib.sha256()
        for row in sorted(manifest["files"], key=lambda item: item["path"]):
            path = row["path"]
            if path.startswith(("archive/", "docs/evidence/")):
                continue
            design_digest.update(path.encode("utf-8") + b"\0" + hashlib.sha256(archive.read(PREFIX + path)).digest())
        if design_digest.hexdigest() != manifest["design_review_digest"]:
            errors.append("V7.2 design review digest mismatch")
        source = json.loads(archive.read(PREFIX + "SOURCE_MANIFEST.json"))
        if len(source["files"]) != manifest["source_files"] or manifest["source_files"] != 61:
            errors.append("source count mismatch")
        for row in source["files"]:
            relative = "archive/sources/" + row["path"]
            data = (ROOT / relative).read_bytes()
            if len(data) != row["local_bytes"] or hashlib.sha256(data).hexdigest() != row["sha256"]:
                errors.append("imported source hash mismatch: " + relative)
        predecessor = (ROOT / "archive/V7.1/Hayool-OS-V7.1-Source-of-Truth.zip").read_bytes()
        if hashlib.sha256(predecessor).hexdigest() != manifest["predecessor_v71_sha256"]:
            errors.append("V7.1 predecessor hash mismatch")
    return errors


def security() -> list[str]:
    errors: list[str] = []
    kill = json.loads((ROOT / "bootstrap/kill_switch.json").read_text(encoding="utf-8"))
    if kill != {"engaged": False, "autonomous_writes_enabled": False, "merge_enabled": False, "deploy_enabled": False, "external_calls_enabled": False}:
        errors.append("M0 shadow kill switch policy changed")
    workflows = sorted((ROOT / ".github/workflows").glob("*.yml"))
    if not workflows:
        return ["no CI workflow"]
    for workflow in workflows:
        text = workflow.read_text(encoding="utf-8")
        for forbidden in ("pull_request_target", "workflow_run:", "write-all", "secrets."):
            if forbidden in text:
                errors.append(f"unsafe workflow token in {workflow.name}: {forbidden}")
        if re.search(r"(?im)\b[A-Za-z_-]+:\s*write\b|permissions:\s*write-all\b", text):
            errors.append(f"workflow {workflow.name} requests write permission")
        for action in re.findall(r"^\s*-?\s*uses:\s*([^\s#]+)", text, re.MULTILINE):
            if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+@[0-9a-f]{40}", action):
                errors.append(f"unpinned action in {workflow.name}")
        if "contents: read" not in text:
            errors.append(f"workflow {workflow.name} lacks explicit read-only contents permission")
    return errors


def dependencies() -> list[str]:
    # M0 has no installed application runtime. A package manifest requires a new review.
    discovered = [p for name in ("package.json", "pnpm-lock.yaml", "package-lock.json", "yarn.lock", "requirements.txt", "poetry.lock", "Dockerfile") if (p := ROOT / name).exists()]
    return ["unreviewed installed dependency manifest: " + p.name for p in discovered]


def licenses() -> list[str]:
    path = ROOT / "bootstrap/dependency_baseline.json"
    if not path.is_file():
        return ["dependency baseline missing"]
    rows = json.loads(path.read_text(encoding="utf-8"))
    errors: list[str] = []
    if not isinstance(rows, list) or not rows:
        return ["dependency baseline empty"]
    for row in rows:
        name = row.get("name", "<unknown>")
        if not re.fullmatch(r"\d+\.\d+(?:\.\d+)?(?:[A-Za-z0-9.+_-]*)", str(row.get("version", ""))):
            errors.append(f"{name}: version is not exact")
        if row.get("license") not in ALLOWED_LICENSES:
            errors.append(f"{name}: license not in reviewed M0 allowlist")
        if row.get("license") in {"MIXED", "INTERNAL"} and not row.get("license_review"):
            errors.append(f"{name}: license follow-up missing")
        if row.get("status") != "planned" or row.get("installed") is not False:
            errors.append(f"{name}: inventory claims an unverified installation")
        if not str(row.get("source", "")).startswith("https://"):
            errors.append(f"{name}: source URL missing")
    return errors


def secrets() -> list[str]:
    errors: list[str] = []
    tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).split(b"\0")
    for raw in tracked:
        if not raw:
            continue
        relative = os.fsdecode(raw)
        path = ROOT / relative
        if path.is_symlink():
            errors.append(f"tracked symlink requires review: {relative}")
            continue
        if not path.is_file():
            errors.append(f"tracked file missing: {relative}")
            continue
        data = path.read_bytes()
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(data):
                errors.append(f"possible {label} in {relative}")
    return errors


def test_integrity(base_sha: str, target_sha: str) -> list[str]:
    errors: list[str] = []
    for line in git("diff", "--name-status", base_sha, target_sha).splitlines():
        columns = line.split("\t")
        status, path = columns[0], columns[-1]
        protected = (
            path.startswith(("bootstrap/tests/", "tests/", ".github/workflows/"))
            or path == "bootstrap/baseline.py"
        )
        if protected and not status.startswith("A"):
            errors.append("existing test or gate policy changed or removed: " + path)
    return errors


def traceability() -> list[str]:
    event_path = Path(os.environ.get("GITHUB_EVENT_PATH", ""))
    if not event_path.is_file():
        return ["GitHub PR event missing"]
    body = (json.loads(event_path.read_text(encoding="utf-8")).get("pull_request") or {}).get("body") or ""
    required = {
        "REQ": r"REQ-[A-Z]+-[0-9]+",
        "ADR": r"ADR-[0-9]+",
        "Risk": r"R[0-4]",
        "Tests": r"\S+",
        "Evidence": r"\S+",
        "Migration": r"\S+",
    }
    return ["PR body missing " + label for label, pattern in required.items() if not re.search(r"(?im)^" + label + r":\s*" + pattern, body)]


def unit() -> list[str]:
    suite = unittest.defaultTestLoader.discover(str(ROOT / "bootstrap/tests"), pattern="test_*.py")
    result = unittest.TextTestRunner(stream=sys.stderr, verbosity=1).run(suite)
    return [] if result.wasSuccessful() and result.testsRun > 0 else ["unit suite failed or empty"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-sha", required=True)
    parser.add_argument("--target-sha", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--allow-dirty", action="store_true", help="development only; evidence is not admissible")
    args = parser.parse_args()
    target_sha = git("rev-parse", "HEAD")
    if target_sha != args.target_sha:
        parser.error("checkout does not match the requested exact PR head SHA")
    clean = not bool(git("status", "--porcelain"))
    if not clean and not args.allow_dirty:
        parser.error("worktree is dirty; exact-SHA evidence requires a clean checkout")
    functions = {
        "source_integrity": source_integrity,
        "unit": unit,
        "security": security,
        "dependencies": dependencies,
        "licenses": licenses,
        "secrets": secrets,
        "test_integrity": lambda: test_integrity(args.base_sha, target_sha),
        "traceability": traceability,
    }
    details = {name: function() for name, function in functions.items()}
    checks = {name: "PASS" if not errors else "FAIL" for name, errors in details.items()}
    report = {"schema_version": 1, "policy_source": os.environ.get("HAYOOL_POLICY_SOURCE", "local-unverified"), "base_sha": args.base_sha, "target_sha": target_sha, "workspace_clean": clean, "checks": checks, "errors": details}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"target_sha": target_sha, "workspace_clean": clean, "checks": checks}, sort_keys=True))
    return 0 if clean and all(value == "PASS" for value in checks.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
