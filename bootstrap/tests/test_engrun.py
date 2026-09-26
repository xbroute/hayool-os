import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from bootstrap.engrun import REQUIRED_CHECKS, evaluate, risk_for_path


class EngineeringRunGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.target = "a" * 40
        self.base = "b" * 40
        report = {"base_sha": self.base, "target_sha": self.target, "workspace_clean": True, "checks": {name: "PASS" for name in REQUIRED_CHECKS}, "source": "github_actions", "conclusion": "success", "url": "https://github.com/xbroute/hayool-os/actions/runs/1"}
        self._write("baseline.json", report)
        for name in ("review-1.json", "review-2.json"):
            self._write(name, {"target_sha": self.target, "read_only": True, "verdict": "PASS"})
        self.run = {
            "schema_version": 1,
            "run_id": "ENG-RUN-test",
            "mode": "shadow",
            "repository": "xbroute/hayool-os",
            "branch": "codex/shadow-test",
            "base_sha": self.base,
            "target_sha": self.target,
            "policy_sha": self.base,
            "decided_at": "2026-09-26T18:30:00Z",
            "changed_paths": ["samples/shadow-proof.txt"],
            "risk": "R0",
            "writer": {
                "id": "writer", "branch": "codex/shadow-test", "read_only": False,
                "lease_issued_at": "2026-09-26T18:00:00Z", "lease_expires_at": "2026-09-26T19:00:00Z",
                "gateway": "test-gateway", "requested_provider": "test-provider", "effective_provider": "test-provider", "requested_model": "test-model", "effective_model": "test-model", "identity_verified": True,
            },
            "reviewers": [
                {"id": f"reviewer-{i}", "read_only": True, "target_sha": self.target, "verdict": "PASS",
                 "gateway": "test-gateway", "requested_provider": "test-provider", "effective_provider": "test-provider", "requested_model": "test-model", "effective_model": "test-model", "identity_verified": True,
                 "report_path": f"review-{i}.json", "report_sha256": self._hash(f"review-{i}.json")}
                for i in (1, 2)
            ],
            "hard_checks": [
                {"name": name, "status": "PASS", "target_sha": self.target,
                 "report_path": "baseline.json", "report_sha256": self._hash("baseline.json")}
                for name in sorted(REQUIRED_CHECKS)
            ],
            "limits": {"repair_iterations": 0, "elapsed_seconds": 180, "external_cost_usd": 0, "external_cost_cap_usd": 0},
            "kill_switch": {"engaged": False, "autonomous_writes_enabled": False, "merge_enabled": False,
                            "deploy_enabled": False, "external_calls_enabled": False},
            "merge_performed": False,
            "deployment_performed": False,
            "result": "PASS",
        }

    def _write(self, name, value):
        (self.root / name).write_text(json.dumps(value, sort_keys=True), encoding="utf-8")

    def _hash(self, name):
        return hashlib.sha256((self.root / name).read_bytes()).hexdigest()

    def test_valid_shadow_trace_passes(self):
        self.assertEqual(evaluate(self.run, self.root, self.target), [])

    def test_failure_injection_ai_votes_cannot_override_hard_failure(self):
        report = json.loads((self.root / "baseline.json").read_text())
        report["checks"]["secrets"] = "FAIL"
        self._write("baseline.json", report)
        for check in self.run["hard_checks"]:
            check["report_sha256"] = self._hash("baseline.json")
        errors = evaluate(self.run, self.root, self.target)
        self.assertTrue(any("hard check secrets conflicts" in error for error in errors), errors)

    def test_ci_failure_cannot_be_replaced_by_local_pass(self):
        report = json.loads((self.root / "baseline.json").read_text())
        report["checks"]["ci"] = "FAIL"
        report["conclusion"] = "failure"
        self._write("baseline.json", report)
        for check in self.run["hard_checks"]:
            check["report_sha256"] = self._hash("baseline.json")
        errors = evaluate(self.run, self.root, self.target)
        self.assertTrue(any("GitHub CI proof" in error for error in errors), errors)

    def test_stale_sha_blocks(self):
        self.assertTrue(any("stale" in e for e in evaluate(self.run, self.root, "c" * 40)))

    def test_budget_and_kill_switch_block(self):
        self.run["limits"]["repair_iterations"] = 4
        self.run["kill_switch"]["engaged"] = True
        errors = evaluate(self.run, self.root, self.target)
        self.assertTrue(any("repair cap" in e for e in errors))
        self.assertTrue(any("kill switch" in e for e in errors))

    def test_policy_paths_are_high_risk(self):
        self.assertEqual(risk_for_path("docs/adr/ADR_CATALOG.md"), "R3")
        self.assertEqual(risk_for_path("samples/shadow-proof.txt"), "R0")


if __name__ == "__main__":
    unittest.main()
