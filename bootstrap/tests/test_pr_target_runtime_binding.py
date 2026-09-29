"""Real-shaped pull_request_target provenance regressions run in isolated CI."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from bootstrap import trusted_gate as gate  # noqa: E402
from bootstrap.regression_tests.test_target_gate import (  # noqa: E402
    ARTIFACT_ID, BASE, HEAD, JOB_ID, REPO, TRUSTED_RUN_ID, target_client,
)


class PullRequestTargetRuntimeBindingTests(unittest.TestCase):
    def test_real_api_head_is_candidate_while_policy_is_base(self):
        client, event = target_client()
        client.get_artifact_zip = lambda path: client.archive
        result = gate.evaluate_pr_target(event, REPO, BASE, TRUSTED_RUN_ID, 1, client)
        self.assertEqual(result["decision"], "PASS")
        self.assertEqual(result["policy_sha"], BASE)
        self.assertEqual(result["head_sha"], HEAD)
        self.assertEqual(result["candidate_artifact_id"], ARTIFACT_ID)

    def test_base_sha_disguised_as_run_head_is_rejected(self):
        client, event = target_client()
        client.responses[f"repos/{REPO}/actions/runs/{TRUSTED_RUN_ID}"]["head_sha"] = BASE
        with self.assertRaisesRegex(gate.GateError, "not the protected-main workflow"):
            gate.evaluate_pr_target(event, REPO, BASE, TRUSTED_RUN_ID, 1, client)

    def test_wrong_linked_pr_or_workflow_is_rejected(self):
        for change in ("number", "base", "head", "workflow"):
            with self.subTest(change=change):
                client, event = target_client()
                run = client.responses[f"repos/{REPO}/actions/runs/{TRUSTED_RUN_ID}"]
                if change == "number":
                    run["pull_requests"][0]["number"] = 99
                elif change == "base":
                    run["pull_requests"][0]["base"]["sha"] = HEAD
                elif change == "head":
                    run["pull_requests"][0]["head"]["sha"] = BASE
                else:
                    run["workflow_id"] = 999
                with self.assertRaises(gate.GateError):
                    gate.evaluate_pr_target(event, REPO, BASE, TRUSTED_RUN_ID, 1, client)

    def test_wrong_job_check_or_artifact_origin_is_rejected(self):
        for change in ("job", "check", "artifact"):
            with self.subTest(change=change):
                client, event = target_client()
                if change == "job":
                    client.responses[f"repos/{REPO}/actions/runs/{TRUSTED_RUN_ID}/jobs?per_page=100"]["jobs"][0]["head_sha"] = BASE
                elif change == "check":
                    client.responses[f"repos/{REPO}/check-runs/{JOB_ID}"]["head_sha"] = BASE
                else:
                    client.responses[f"repos/{REPO}/actions/runs/{TRUSTED_RUN_ID}/artifacts?per_page=100"]["artifacts"][0]["workflow_run"]["head_sha"] = BASE
                with self.assertRaises(gate.GateError):
                    gate.evaluate_pr_target(event, REPO, BASE, TRUSTED_RUN_ID, 1, client)

    def test_pr_added_spoof_workflow_is_rejected(self):
        client, event = target_client()
        client.responses[f"repos/{REPO}/git/trees/{HEAD}?recursive=1"]["tree"].append({
            "path": ".github/workflows/spoof-trusted-status.yml",
            "mode": "100644", "type": "blob", "sha": "f" * 40,
        })
        with self.assertRaisesRegex(gate.GateError, "workflow tree differs"):
            gate.evaluate_pr_target(event, REPO, BASE, TRUSTED_RUN_ID, 1, client)


if __name__ == "__main__":
    unittest.main()
