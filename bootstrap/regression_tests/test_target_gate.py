"""PR-target trust boundary tests. Run this file only in the isolated test container."""

import hashlib
import io
import json
import sys
import tempfile
import unittest
import zipfile
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
    pr["head"]["ref"] = "codex/shadow-test"
    pr["head"]["repo"] = {"full_name": REPO, "id": 42}
    pr["base"]["repo"] = {"full_name": REPO, "id": 42}
    event = {"action": "synchronize", "pull_request": {
        "number": 7, "base": {"sha": BASE, "ref": "main"},
        "head": {"sha": HEAD, "ref": "codex/shadow-test"},
    }}
    client.responses[f"repos/{REPO}/actions/runs/{TRUSTED_RUN_ID}"] = {
        "id": TRUSTED_RUN_ID, "run_attempt": 1,
        "repository": {"full_name": REPO, "id": 42},
        "head_repository": {"full_name": REPO, "id": 42},
        "event": "pull_request_target",
        "head_sha": HEAD, "head_branch": "codex/shadow-test", "status": "in_progress",
        "path": gate.TRUSTED_WORKFLOW_PATH, "workflow_id": 111,
        "check_suite_id": 777,
        "pull_requests": [{
            "number": 7,
            "base": {"ref": "main", "sha": BASE, "repo": {"id": 42}},
            "head": {"ref": "codex/shadow-test", "sha": HEAD, "repo": {"id": 42}},
        }],
    }
    client.responses[f"repos/{REPO}/actions/workflows/{gate.TRUSTED_WORKFLOW_PATH}"] = {
        "id": 111, "path": gate.TRUSTED_WORKFLOW_PATH, "state": "active",
    }
    client.responses[f"repos/{REPO}/actions/runs/{TRUSTED_RUN_ID}/jobs?per_page=100"] = {
        "total_count": 2, "jobs": [
            {"id": JOB_ID, "name": "candidate-check", "conclusion": "success",
             "head_sha": HEAD},
            {"id": JOB_ID + 1, "name": "trusted-gate", "conclusion": None},
        ],
    }
    client.responses[f"repos/{REPO}/check-runs/{JOB_ID}"] = {
        "id": JOB_ID, "name": "candidate-check", "conclusion": "success",
        "head_sha": HEAD,
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
            "workflow_run": {"id": TRUSTED_RUN_ID, "head_sha": HEAD,
                             "head_branch": "codex/shadow-test",
                             "repository_id": 42, "head_repository_id": 42},
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

    def test_live_run_candidate_sha_cannot_be_replaced_by_policy_sha(self):
        client, event = target_client()
        client.responses[f"repos/{REPO}/actions/runs/{TRUSTED_RUN_ID}"]["head_sha"] = BASE
        with self.assertRaisesRegex(gate.GateError, "not the protected-main workflow"):
            gate.evaluate_pr_target(event, REPO, BASE, TRUSTED_RUN_ID, 1, client)

    def test_linked_pr_must_bind_number_base_head_and_repository(self):
        for field, value in (("number", 8), ("base_sha", "c" * 40),
                             ("head_sha", "c" * 40), ("repo_id", 999)):
            with self.subTest(field=field):
                client, event = target_client()
                linked = client.responses[f"repos/{REPO}/actions/runs/{TRUSTED_RUN_ID}"]["pull_requests"][0]
                if field == "number":
                    linked["number"] = value
                elif field == "base_sha":
                    linked["base"]["sha"] = value
                elif field == "head_sha":
                    linked["head"]["sha"] = value
                else:
                    linked["head"]["repo"]["id"] = value
                with self.assertRaisesRegex(gate.GateError, "run PR base/head binding mismatch"):
                    gate.evaluate_pr_target(event, REPO, BASE, TRUSTED_RUN_ID, 1, client)

    def test_wrong_workflow_id_or_artifact_origin_fails_closed(self):
        client, event = target_client()
        client.responses[f"repos/{REPO}/actions/runs/{TRUSTED_RUN_ID}"]["workflow_id"] = 222
        with self.assertRaisesRegex(gate.GateError, "workflow identity is not active"):
            gate.evaluate_pr_target(event, REPO, BASE, TRUSTED_RUN_ID, 1, client)
        client, event = target_client()
        client.responses[f"repos/{REPO}/actions/runs/{TRUSTED_RUN_ID}/artifacts?per_page=100"]["artifacts"][0]["workflow_run"]["head_sha"] = BASE
        with self.assertRaisesRegex(gate.GateError, "artifact origin mismatch"):
            gate.evaluate_pr_target(event, REPO, BASE, TRUSTED_RUN_ID, 1, client)

    def test_candidate_job_and_check_must_bind_exact_candidate_sha(self):
        client, event = target_client()
        client.responses[f"repos/{REPO}/actions/runs/{TRUSTED_RUN_ID}/jobs?per_page=100"]["jobs"][0]["head_sha"] = BASE
        with self.assertRaisesRegex(gate.GateError, "candidate job missing or failed"):
            gate.evaluate_pr_target(event, REPO, BASE, TRUSTED_RUN_ID, 1, client)
        client, event = target_client()
        client.responses[f"repos/{REPO}/check-runs/{JOB_ID}"]["head_sha"] = BASE
        with self.assertRaisesRegex(gate.GateError, "candidate check provenance mismatch"):
            gate.evaluate_pr_target(event, REPO, BASE, TRUSTED_RUN_ID, 1, client)

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

    def test_real_shaped_trusted_artifact_allows_publication_only_with_exact_origin(self):
        client, event = target_client()
        baseline_zip = client.archive
        client.get_artifact_zip = lambda path: baseline_zip
        result = gate.evaluate_pr_target(event, REPO, BASE, TRUSTED_RUN_ID, 1, client)
        output = io.BytesIO()
        with zipfile.ZipFile(output, "w") as bundle:
            bundle.writestr("trusted-gate.json", json.dumps(result))
        trusted_zip = output.getvalue()
        listing = client.responses[f"repos/{REPO}/actions/runs/{TRUSTED_RUN_ID}/artifacts?per_page=100"]
        listing["artifacts"].append({
            "id": ARTIFACT_ID + 1,
            "name": f"engineering-trusted-gate-{TRUSTED_RUN_ID}",
            "expired": False, "size_in_bytes": len(trusted_zip),
            "digest": "sha256:" + hashlib.sha256(trusted_zip).hexdigest(),
            "workflow_run": {"id": TRUSTED_RUN_ID, "head_sha": HEAD,
                             "head_branch": "codex/shadow-test",
                             "repository_id": 42, "head_repository_id": 42},
        })
        listing["total_count"] = 2
        client.get_artifact_zip = lambda path: (trusted_zip if path.endswith(
            f"/{ARTIFACT_ID + 1}/zip") else baseline_zip)
        with tempfile.TemporaryDirectory() as directory:
            report_path = Path(directory) / "trusted-gate.json"
            report_path.write_text(json.dumps(result), encoding="utf-8")
            gate.require_trusted_artifact(client, REPO, TRUSTED_RUN_ID, BASE,
                                          result, report_path)
            listing["artifacts"][1]["workflow_run"]["head_sha"] = BASE
            with self.assertRaisesRegex(gate.GateError, "trusted artifact origin invalid"):
                gate.require_trusted_artifact(client, REPO, TRUSTED_RUN_ID, BASE,
                                              result, report_path)


if __name__ == "__main__":
    unittest.main()
