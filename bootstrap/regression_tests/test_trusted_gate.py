"""Trust-boundary regressions for the default-branch workflow_run verifier."""

import base64
import hashlib
import io
import json
import sys
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from bootstrap import trusted_gate as gate  # noqa: E402

REPO = "xbroute/hayool-os"
BASE = "a" * 40
HEAD = "b" * 40
RUN_ID = 1234
CHECK_ID = 5678
ARTIFACT_ID = 9012


def content(data: bytes) -> dict:
    return {
        "type": "file", "encoding": "base64", "size": len(data),
        "content": base64.b64encode(data).decode("ascii"),
        "sha": hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest(),
    }


def zipped(report: dict) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        archive.writestr("baseline.json", json.dumps(report, sort_keys=True))
    return buffer.getvalue()


class FakeClient:
    def __init__(self) -> None:
        self.status_posts = []
        workflow = b"name: engineering-candidate\non: pull_request\n"
        policy = b"# reviewed base policy\n"
        gate_code = b"# reviewed trusted gate\n"
        engrun_code = b"# reviewed ENG-RUN evaluator\n"
        engrun_schema = b"{}\n"
        workflow_blob = hashlib.sha1(f"blob {len(workflow)}\0".encode() + workflow).hexdigest()
        workflow_tree = [
            {"path": ".github/workflows", "mode": "040000", "type": "tree", "sha": "d" * 40},
            {"path": gate.WORKFLOW_PATH, "mode": "100644", "type": "blob", "sha": workflow_blob},
        ]
        self.event = {"action": "completed", "workflow_run": {"id": RUN_ID, "head_sha": HEAD, "conclusion": "success", "run_attempt": 1}}
        report = {
            "schema_version": 1, "policy_source": "base", "base_sha": BASE,
            "target_sha": HEAD, "workspace_clean": True,
            "checks": {name: "PASS" for name in gate.HARD_CHECKS},
            "errors": {name: [] for name in gate.HARD_CHECKS},
        }
        self.archive = zipped(report)
        self.responses = {
            f"repos/{REPO}/actions/runs/{RUN_ID}": {
                "id": RUN_ID, "repository": {"full_name": REPO}, "event": "pull_request",
                "name": gate.WORKFLOW_NAME, "path": gate.WORKFLOW_PATH,
                "status": "completed", "conclusion": "success", "head_sha": HEAD,
                "head_repository": {"full_name": REPO}, "run_attempt": 1,
                "check_suite_id": 999, "pull_requests": [{
                    "number": 7, "base": {"sha": BASE}, "head": {"sha": HEAD},
                }],
            },
            f"repos/{REPO}/pulls/7": {
                "number": 7, "state": "open", "base": {"ref": "main", "sha": BASE},
                "head": {"sha": HEAD},
            },
            f"repos/{REPO}/git/ref/heads/main": {"object": {"sha": BASE}},
            f"repos/{REPO}/git/trees/{BASE}?recursive=1": {"truncated": False, "tree": workflow_tree},
            f"repos/{REPO}/git/trees/{HEAD}?recursive=1": {"truncated": False, "tree": [dict(row) for row in workflow_tree]},
            f"repos/{REPO}/contents/{gate.WORKFLOW_PATH}?ref={BASE}": content(workflow),
            f"repos/{REPO}/contents/{gate.WORKFLOW_PATH}?ref={HEAD}": content(workflow),
            f"repos/{REPO}/contents/{gate.POLICY_PATH}?ref={BASE}": content(policy),
            f"repos/{REPO}/contents/{gate.POLICY_PATH}?ref={HEAD}": content(policy),
            f"repos/{REPO}/contents/{gate.GATE_PATH}?ref={BASE}": content(gate_code),
            f"repos/{REPO}/contents/{gate.GATE_PATH}?ref={HEAD}": content(gate_code),
            f"repos/{REPO}/contents/{gate.ENGRUN_PATH}?ref={BASE}": content(engrun_code),
            f"repos/{REPO}/contents/{gate.ENGRUN_PATH}?ref={HEAD}": content(engrun_code),
            f"repos/{REPO}/contents/{gate.ENGRUN_SCHEMA_PATH}?ref={BASE}": content(engrun_schema),
            f"repos/{REPO}/contents/{gate.ENGRUN_SCHEMA_PATH}?ref={HEAD}": content(engrun_schema),
            f"repos/{REPO}/actions/runs/{RUN_ID}/jobs?per_page=100": {
                "total_count": 1, "jobs": [{"id": CHECK_ID, "name": gate.JOB_NAME,
                                              "conclusion": "success", "head_sha": HEAD}],
            },
            f"repos/{REPO}/check-runs/{CHECK_ID}": {
                "id": CHECK_ID, "name": gate.JOB_NAME, "head_sha": HEAD,
                "conclusion": "success", "app": {"slug": "github-actions"},
                "check_suite": {"id": 999},
            },
            f"repos/{REPO}/actions/runs/{RUN_ID}/artifacts?per_page=100": {
                "total_count": 1, "artifacts": [{
                    "id": ARTIFACT_ID, "name": f"engineering-baseline-{HEAD}",
                    "expired": False, "size_in_bytes": len(self.archive),
                    "workflow_run": {"id": RUN_ID, "head_sha": HEAD},
                    "digest": "sha256:" + hashlib.sha256(self.archive).hexdigest(),
                }],
            },
        }

    def get_json(self, path: str) -> dict:
        return self.responses[path]

    def get_artifact_zip(self, path: str) -> bytes:
        if path != f"repos/{REPO}/actions/artifacts/{ARTIFACT_ID}/zip":
            raise AssertionError(path)
        return self.archive

    def post_json(self, path: str, body: dict) -> dict:
        self.status_posts.append((path, body))
        return {"state": body["state"]}

    def change_report(self, **changes: object) -> None:
        report = json.loads(zipfile.ZipFile(io.BytesIO(self.archive)).read("baseline.json"))
        report.update(changes)
        self.archive = zipped(report)
        artifact = self.responses[f"repos/{REPO}/actions/runs/{RUN_ID}/artifacts?per_page=100"]["artifacts"][0]
        artifact["size_in_bytes"] = len(self.archive)
        artifact["digest"] = "sha256:" + hashlib.sha256(self.archive).hexdigest()


class TrustedGateTests(unittest.TestCase):
    def test_valid_run_binds_exact_policy_workflow_and_artifact(self) -> None:
        client = FakeClient()
        result = gate.evaluate(client.event, REPO, BASE, client)
        self.assertEqual(result["decision"], "PASS")
        self.assertTrue(result["github_api_verified"])
        self.assertEqual(result["head_sha"], HEAD)
        self.assertEqual(result["policy_sha"], BASE)
        self.assertEqual(result["candidate_artifact_id"], ARTIFACT_ID)

    def test_pr_controlled_success_workflow_cannot_replace_policy(self) -> None:
        client = FakeClient()
        # The attacker preserves a successful run/check/artifact but changes the
        # candidate workflow into a trivial PASS. Exact byte comparison rejects it.
        attack = b"name: engineering-candidate\non: pull_request\nrun: true\n"
        client.responses[f"repos/{REPO}/contents/{gate.WORKFLOW_PATH}?ref={HEAD}"] = content(attack)
        client.responses[f"repos/{REPO}/git/trees/{HEAD}?recursive=1"]["tree"][1]["sha"] = content(attack)["sha"]
        with self.assertRaisesRegex(gate.GateError, "workflow tree differs"):
            gate.evaluate(client.event, REPO, BASE, client)

    def test_added_spoof_workflow_rejected_even_if_original_workflow_unchanged(self) -> None:
        client = FakeClient()
        client.responses[f"repos/{REPO}/git/trees/{HEAD}?recursive=1"]["tree"].append({
            "path": ".github/workflows/fake-pass.yml", "mode": "100644",
            "type": "blob", "sha": "f" * 40,
        })
        with self.assertRaisesRegex(gate.GateError, "workflow tree differs"):
            gate.evaluate(client.event, REPO, BASE, client)

    def test_truncated_tree_fails_closed(self) -> None:
        client = FakeClient()
        client.responses[f"repos/{REPO}/git/trees/{HEAD}?recursive=1"]["truncated"] = True
        with self.assertRaisesRegex(gate.GateError, "tree is truncated"):
            gate.evaluate(client.event, REPO, BASE, client)

    def test_changed_trusted_gate_code_rejected(self) -> None:
        client = FakeClient()
        client.responses[f"repos/{REPO}/contents/{gate.GATE_PATH}?ref={HEAD}"] = content(b"print('PASS')\n")
        with self.assertRaisesRegex(gate.GateError, "trusted gate differs"):
            gate.evaluate(client.event, REPO, BASE, client)

    def test_changed_engrun_evaluator_or_schema_rejected(self) -> None:
        for path, pattern in ((gate.ENGRUN_PATH, "ENG-RUN evaluator differs"),
                              (gate.ENGRUN_SCHEMA_PATH, "ENG-RUN schema differs")):
            with self.subTest(path=path):
                client = FakeClient()
                client.responses[f"repos/{REPO}/contents/{path}?ref={HEAD}"] = content(b"{\"result\":\"PASS\"}\n")
                with self.assertRaisesRegex(gate.GateError, pattern):
                    gate.evaluate(client.event, REPO, BASE, client)

    def test_workflow_path_ref_suffix_is_accepted(self) -> None:
        client = FakeClient()
        client.responses[f"repos/{REPO}/actions/runs/{RUN_ID}"]["path"] += "@refs/pull/7/merge"
        self.assertEqual(gate.evaluate(client.event, REPO, BASE, client)["decision"], "PASS")

    def test_stale_rerun_attempt_is_not_reused(self) -> None:
        client = FakeClient()
        client.responses[f"repos/{REPO}/actions/runs/{RUN_ID}"]["run_attempt"] = 2
        with self.assertRaisesRegex(gate.GateError, "stale run attempt"):
            gate.evaluate(client.event, REPO, BASE, client)

    def test_forged_pass_artifact_cannot_change_exact_sha(self) -> None:
        client = FakeClient()
        client.change_report(target_sha="c" * 40)
        with self.assertRaisesRegex(gate.GateError, "report SHA binding"):
            gate.evaluate(client.event, REPO, BASE, client)

    def test_artifact_bytes_must_match_github_digest(self) -> None:
        client = FakeClient()
        client.archive += b"tampered"
        with self.assertRaisesRegex(gate.GateError, "artifact digest mismatch"):
            gate.evaluate(client.event, REPO, BASE, client)

    def test_stale_pr_head_cannot_reuse_previous_success(self) -> None:
        client = FakeClient()
        client.responses[f"repos/{REPO}/pulls/7"]["head"]["sha"] = "c" * 40
        with self.assertRaisesRegex(gate.GateError, "PR head advanced"):
            gate.evaluate(client.event, REPO, BASE, client)

    def test_fake_ai_or_artifact_pass_cannot_override_failed_ci(self) -> None:
        client = FakeClient()
        client.responses[f"repos/{REPO}/actions/runs/{RUN_ID}"]["conclusion"] = "failure"
        client.event["workflow_run"]["conclusion"] = "failure"
        with self.assertRaisesRegex(gate.GateError, "workflow did not succeed"):
            gate.evaluate(client.event, REPO, BASE, client)

    def test_failure_overwrites_prior_success_status_on_same_live_head(self) -> None:
        client = FakeClient()
        result = {"decision": "FAIL", "errors": ["candidate workflow tree differs"]}
        gate.post_gate_status(client, client.event, REPO, result, state="pending")
        gate.post_gate_status(client, client.event, REPO, result)
        self.assertEqual([body["state"] for _, body in client.status_posts], ["pending", "failure"])
        self.assertEqual(client.status_posts[-1][0], f"repos/{REPO}/statuses/{HEAD}")

    def test_failure_status_cannot_target_stale_pr_head(self) -> None:
        client = FakeClient()
        client.responses[f"repos/{REPO}/pulls/7"]["head"]["sha"] = "c" * 40
        with self.assertRaisesRegex(gate.GateError, "PR is stale"):
            gate.post_gate_status(client, client.event, REPO, {"decision": "FAIL"})
        self.assertEqual(client.status_posts, [])


if __name__ == "__main__":
    unittest.main()
