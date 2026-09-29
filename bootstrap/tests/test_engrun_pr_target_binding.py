"""ENG-RUN must authenticate real-shaped protected-main GitHub metadata."""

import hashlib
import io
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from bootstrap import engrun as engrun_module  # noqa: E402
from bootstrap.engrun import REQUIRED_CHECKS, verify_protected_ci  # noqa: E402


REPO = "xbroute/hayool-os"
BASE = "a" * 40
HEAD = "b" * 40
BRANCH = "codex/shadow-test"
RUN_ID = 4321
REPO_ID = 42


def zipped(name: str, data: bytes) -> bytes:
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w") as archive:
        archive.writestr(name, data)
    return output.getvalue()


class ProtectedRunBindingTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        names = REQUIRED_CHECKS - {"ci"}
        baseline = {
            "schema_version": 1, "policy_source": "base",
            "traceability_source": "head_commit_message", "base_sha": BASE,
            "target_sha": HEAD, "workspace_clean": True,
            "checks": {name: "PASS" for name in names},
            "errors": {name: [] for name in names},
        }
        baseline_bytes = json.dumps(baseline, sort_keys=True).encode()
        (self.root / "baseline.json").write_bytes(baseline_bytes)
        (self.root / "ci.json").write_text(json.dumps({
            "url": f"https://github.com/{REPO}/actions/runs/{RUN_ID}",
            "conclusion": "success",
        }))
        baseline_zip = zipped("baseline.json", baseline_bytes)
        baseline_digest = "sha256:" + hashlib.sha256(baseline_zip).hexdigest()
        report = {
            "schema_version": 2, "decision": "PASS", "github_api_verified": True,
            "source": "protected_main_pr_target", "repository": REPO,
            "pr_number": 7, "base_sha": BASE, "head_sha": HEAD,
            "head_branch": BRANCH, "repository_id": REPO_ID,
            "policy_sha": BASE, "trusted_run_id": RUN_ID,
            "trusted_run_attempt": 1, "candidate_job_id": 123,
            "candidate_artifact_id": 901, "candidate_artifact_digest": baseline_digest,
            "baseline_json_sha256": hashlib.sha256(baseline_bytes).hexdigest(),
            "checks": {name: "PASS" for name in names}, "errors": [],
        }
        report_bytes = json.dumps(report, sort_keys=True).encode()
        (self.root / "trusted-gate.json").write_bytes(report_bytes)
        gate_zip = zipped("trusted-gate.json", report_bytes)
        gate_digest = "sha256:" + hashlib.sha256(gate_zip).hexdigest()
        self.run = {
            "repository": REPO, "branch": BRANCH, "pr_number": 7,
            "base_sha": BASE, "target_sha": HEAD, "policy_sha": BASE,
            "trusted_gate": {
                "run_id": RUN_ID, "run_attempt": 1, "artifact_id": 902,
                "report_path": "trusted-gate.json",
                "report_sha256": hashlib.sha256(report_bytes).hexdigest(),
            },
            "hard_checks": [
                {"name": "source_integrity", "report_path": "baseline.json"},
                {"name": "ci", "report_path": "ci.json"},
            ],
        }
        origin = {
            "id": RUN_ID, "head_sha": HEAD, "head_branch": BRANCH,
            "repository_id": REPO_ID, "head_repository_id": REPO_ID,
        }
        self.responses = {
            "pulls/7": {
                "number": 7, "state": "open",
                "head": {"sha": HEAD, "ref": BRANCH,
                         "repo": {"full_name": REPO, "id": REPO_ID}},
                "base": {"sha": BASE, "ref": "main",
                         "repo": {"full_name": REPO, "id": REPO_ID}},
            },
            "git/ref/heads/main": {"object": {"sha": BASE}},
            "actions/workflows/engineering-trusted-gate.yml": {
                "id": 111, "state": "active",
                "path": ".github/workflows/engineering-trusted-gate.yml",
            },
            f"actions/runs/{RUN_ID}": {
                "id": RUN_ID, "repository": {"full_name": REPO, "id": REPO_ID},
                "head_repository": {"full_name": REPO, "id": REPO_ID},
                "event": "pull_request_target", "head_sha": HEAD,
                "head_branch": BRANCH, "run_attempt": 1,
                "status": "completed", "conclusion": "success",
                "path": ".github/workflows/engineering-trusted-gate.yml",
                "workflow_id": 111,
                "pull_requests": [{
                    "number": 7,
                    "base": {"ref": "main", "sha": BASE, "repo": {"id": REPO_ID}},
                    "head": {"ref": BRANCH, "sha": HEAD, "repo": {"id": REPO_ID}},
                }],
            },
            f"actions/runs/{RUN_ID}/jobs?per_page=100": {
                "total_count": 2, "jobs": [
                    {"id": 123, "name": "candidate-check", "conclusion": "success",
                     "head_sha": HEAD},
                    {"id": 124, "name": "trusted-gate", "conclusion": "success",
                     "head_sha": HEAD},
                ],
            },
            f"actions/runs/{RUN_ID}/artifacts?per_page=100": {
                "total_count": 2, "artifacts": [
                    {"id": 901, "name": f"engineering-protected-baseline-{HEAD}",
                     "expired": False, "digest": baseline_digest,
                     "workflow_run": dict(origin)},
                    {"id": 902, "name": f"engineering-trusted-gate-{RUN_ID}",
                     "expired": False, "digest": gate_digest,
                     "workflow_run": dict(origin)},
                ],
            },
            "actions/policies/5892": {
                "enforcement": "active",
                "conditions": {"workflow_path": {"include": ["~ALL"], "exclude": []}},
                "rules": [{"type": "restrict_action_events", "parameters": {
                    "allowed_events": ["pull_request_target"]}}],
            },
            "branches/main/protection": {
                "required_status_checks": {"strict": True, "checks": [{
                    "context": "engineering-trusted-gate-status", "app_id": 15368,
                }]},
            },
            f"statuses/{HEAD}": [{
                "context": "engineering-trusted-gate-status", "state": "success",
                "creator": {"login": "github-actions[bot]"},
                "target_url": f"https://github.com/{REPO}/actions/runs/{RUN_ID}",
            }],
        }
        self.zips = {901: baseline_zip, 902: gate_zip}

    def verify(self):
        production_json = engrun_module._github_json

        def objects_or_production_status(path):
            if path.startswith("statuses/"):
                return production_json(path)
            return self.responses[path]

        with patch("bootstrap.engrun._github_json",
                   side_effect=objects_or_production_status), \
             patch("bootstrap.engrun.subprocess.check_output",
                   return_value=json.dumps(self.responses[f"statuses/{HEAD}"])), \
             patch("bootstrap.engrun._artifact_zip",
                   side_effect=lambda artifact_id: self.zips[artifact_id]):
            return verify_protected_ci(self.run, self.root, HEAD)

    def test_real_shaped_run_and_direct_status_source_pass(self):
        self.assertEqual(self.verify(), [])

    def test_wrong_candidate_or_linked_base_cannot_pass(self):
        self.responses[f"actions/runs/{RUN_ID}"]["head_sha"] = BASE
        self.assertTrue(self.verify())
        self.responses[f"actions/runs/{RUN_ID}"]["head_sha"] = HEAD
        self.responses[f"actions/runs/{RUN_ID}"]["pull_requests"][0]["base"]["sha"] = HEAD
        self.assertTrue(self.verify())

    def test_wrong_artifact_origin_or_status_source_cannot_pass(self):
        artifact = self.responses[f"actions/runs/{RUN_ID}/artifacts?per_page=100"]["artifacts"][0]
        artifact["workflow_run"]["head_sha"] = BASE
        self.assertTrue(self.verify())
        artifact["workflow_run"]["head_sha"] = HEAD
        self.responses[f"statuses/{HEAD}"][0]["creator"] = {"login": "xbroute"}
        self.assertTrue(self.verify())


if __name__ == "__main__":
    unittest.main()
