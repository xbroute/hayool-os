"""PR-target trust boundary tests. Run this file only in the isolated test container."""

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from bootstrap import trusted_gate as gate  # noqa: E402
from bootstrap.regression_tests.test_trusted_gate import (  # noqa: E402
    FakeClient, REPO, BASE, HEAD, content,
)

TRUSTED_RUN_ID = 4321
JOB_ID = 8765
ARTIFACT_ID = 2109


def target_client():
    client = FakeClient()
    workflow = b"name: engineering-trusted-gate\non: pull_request_target\n"
    blob = content(workflow)
    for revision in (BASE, HEAD):
        client.responses[f"repos/{REPO}/git/trees/{revision}?recursive=1"]["tree"].append({
            "path": gate.TRUSTED_WORKFLOW_PATH, "mode": "100644", "type": "blob",
            "sha": blob["sha"],
        })
        client.responses[f"repos/{REPO}/contents/{gate.TRUSTED_WORKFLOW_PATH}?ref={revision}"] = blob
    pr = client.responses[f"repos/{REPO}/pulls/7"]
    pr["head"]["repo"] = {"full_name": REPO}
    event = {"action": "synchronize", "pull_request": {
        "number": 7, "base": {"sha": BASE}, "head": {"sha": HEAD},
    }}
    client.responses[f"repos/{REPO}/actions/runs/{TRUSTED_RUN_ID}"] = {
        "id": TRUSTED_RUN_ID, "run_attempt": 1,
        "repository": {"full_name": REPO}, "event": "pull_request_target",
        "head_sha": BASE, "head_branch": "main", "status": "in_progress",
        "path": gate.TRUSTED_WORKFLOW_PATH, "check_suite_id": 777,
    }
    client.responses[f"repos/{REPO}/actions/runs/{TRUSTED_RUN_ID}/jobs?per_page=100"] = {
        "total_count": 2, "jobs": [
            {"id": JOB_ID, "name": "candidate-check", "conclusion": "success"},
            {"id": JOB_ID + 1, "name": "trusted-gate", "conclusion": None},
        ],
    }
    client.responses[f"repos/{REPO}/check-runs/{JOB_ID}"] = {
        "id": JOB_ID, "name": "candidate-check", "conclusion": "success",
        "app": {"slug": "github-actions"}, "check_suite": {"id": 777},
    }
    report = json.loads(__import__("zipfile").ZipFile(__import__("io").BytesIO(client.archive)).read("baseline.json"))
    report["policy_source"] = "base"
    report["traceability_source"] = "head_commit_message"
    from bootstrap.regression_tests.test_trusted_gate import zipped
    client.archive = zipped(report)
    client.responses[f"repos/{REPO}/actions/runs/{TRUSTED_RUN_ID}/artifacts?per_page=100"] = {
        "total_count": 1, "artifacts": [{
            "id": ARTIFACT_ID, "name": f"engineering-protected-baseline-{HEAD}",
            "expired": False, "size_in_bytes": len(client.archive),
            "workflow_run": {"id": TRUSTED_RUN_ID, "head_sha": BASE},
            "digest": "sha256:" + hashlib.sha256(client.archive).hexdigest(),
        }],
    }
    return client, event


class TargetGateTests(unittest.TestCase):
    def test_valid_protected_run_binds_exact_shas_and_artifact(self):
        client, event = target_client()
        client.get_artifact_zip = lambda path: client.archive
        result = gate.evaluate_pr_target(event, REPO, BASE, TRUSTED_RUN_ID, 1, client)
        self.assertEqual(result["decision"], "PASS")
        self.assertEqual(result["head_sha"], HEAD)
        self.assertEqual(result["policy_sha"], BASE)

    def test_pr_added_spoof_workflow_is_rejected_even_with_pass_artifact(self):
        client, event = target_client()
        client.get_artifact_zip = lambda path: client.archive
        client.responses[f"repos/{REPO}/git/trees/{HEAD}?recursive=1"]["tree"].append({
            "path": ".github/workflows/fake-pass.yml", "mode": "100644",
            "type": "blob", "sha": "f" * 40,
        })
        with self.assertRaisesRegex(gate.GateError, "workflow tree differs"):
            gate.evaluate_pr_target(event, REPO, BASE, TRUSTED_RUN_ID, 1, client)

    def test_failed_isolated_job_cannot_be_overridden_by_ai_pass(self):
        client, event = target_client()
        client.responses[f"repos/{REPO}/actions/runs/{TRUSTED_RUN_ID}/jobs?per_page=100"]["jobs"][0]["conclusion"] = "failure"
        with self.assertRaisesRegex(gate.GateError, "isolated candidate job missing or failed"):
            gate.evaluate_pr_target(event, REPO, BASE, TRUSTED_RUN_ID, 1, client)

    def test_stale_head_cannot_receive_status(self):
        client, event = target_client()
        client.responses[f"repos/{REPO}/pulls/7"]["head"]["sha"] = "c" * 40
        with self.assertRaisesRegex(gate.GateError, "PR event differs"):
            gate.post_target_status(client, event, REPO, BASE, TRUSTED_RUN_ID,
                                    {"decision": "FAIL"})
        self.assertEqual(client.status_posts, [])

    def test_pass_cannot_publish_before_trusted_artifact_upload(self):
        client, event = target_client()
        client.get_artifact_zip = lambda path: client.archive
        result = gate.evaluate_pr_target(event, REPO, BASE, TRUSTED_RUN_ID, 1, client)
        with tempfile.TemporaryDirectory() as directory:
            report_path = Path(directory) / "trusted-gate.json"
            report_path.write_text(json.dumps(result), encoding="utf-8")
            with self.assertRaisesRegex(gate.GateError, "trusted artifact missing"):
                gate.require_trusted_artifact(client, REPO, TRUSTED_RUN_ID, BASE,
                                              result, report_path)
        self.assertEqual(client.status_posts, [])


if __name__ == "__main__":
    unittest.main()
