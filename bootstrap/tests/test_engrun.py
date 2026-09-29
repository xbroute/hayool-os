import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from bootstrap.engrun import REQUIRED_CHECKS, evaluate, main, risk_for_path, verify_changed_paths, verify_github_ci, verify_reviewer_sessions, verify_writer_github, verify_writer_session


class EngineeringRunGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.target = "a" * 40
        self.base = "b" * 40
        baseline_checks = REQUIRED_CHECKS - {"ci"}
        report = {"schema_version": 1, "base_sha": self.base, "target_sha": self.target, "policy_source": "base", "workspace_clean": True, "checks": {name: "PASS" for name in baseline_checks}, "errors": {name: [] for name in baseline_checks}}
        self._write("baseline.json", report)
        self._write("ci.json", {"base_sha": self.base, "target_sha": self.target, "workspace_clean": True, "checks": {"ci": "PASS"}, "source": "github_actions", "conclusion": "success", "url": "https://github.com/xbroute/hayool-os/actions/runs/1"})
        self._write("trusted-gate.json", {
            "schema_version": 1, "decision": "PASS", "github_api_verified": True,
            "repository": "xbroute/hayool-os", "pr_number": 9,
            "base_sha": self.base, "head_sha": self.target, "policy_sha": self.base,
            "candidate_run_id": 1, "candidate_run_attempt": 1,
            "candidate_check_run_id": 11, "candidate_artifact_id": 12,
            "candidate_artifact_digest": "sha256:" + "d" * 64,
            "baseline_json_sha256": self._hash("baseline.json"),
            "workflow_sha256": "e" * 64, "baseline_policy_sha256": "f" * 64,
            "checks": {name: "PASS" for name in baseline_checks}, "errors": [],
        })
        for name in ("review-1.json", "review-2.json"):
            self._write(name, {"target_sha": self.target, "read_only": True, "verdict": "PASS", "findings": []})
        self.run = {
            "schema_version": 2,
            "run_id": "ENG-RUN-test",
            "pr_number": 9,
            "mode": "shadow",
            "ci_mode": "legacy_workflow_run",
            "repository": "xbroute/hayool-os",
            "branch": "codex/shadow-test",
            "base_sha": self.base,
            "target_sha": self.target,
            "policy_sha": self.base,
            "decided_at": "2026-09-26T18:30:00Z",
            "changed_paths": ["samples/shadow-proof.txt"],
            "risk": "R0",
            "writer": {
                "id": "/root", "branch": "codex/shadow-test", "read_only": False,
                "lease_issued_at": "2026-09-26T18:00:00Z", "lease_expires_at": "2026-09-26T19:00:00Z",
                "gateway": "test-gateway", "requested_provider": "test-provider", "effective_provider": "test-provider", "requested_model": "test-model", "effective_model": "test-model", "identity_verified": True,
                "session_id": "11111111-1111-4111-8111-111111111111", "github_login": "xbroute",
            },
            "reviewers": [
                {"id": f"/root/review_{i}", "read_only": True, "target_sha": self.target, "verdict": "PASS",
                 "findings": [],
                 "gateway": "test-gateway", "requested_provider": "test-provider", "effective_provider": "test-provider", "requested_model": "test-model", "effective_model": "test-model", "identity_verified": True,
                 "session_id": f"00000000-0000-4000-8000-{i:012d}",
                 "agent_path": f"/root/review_{i}", "response_item_id": f"msg_review_{i}",
                 "report_path": f"review-{i}.json", "report_sha256": self._hash(f"review-{i}.json")}
                for i in (1, 2)
            ],
            "hard_checks": [
                {"name": name, "status": "PASS", "target_sha": self.target,
                 "report_path": "ci.json" if name == "ci" else "baseline.json",
                 "report_sha256": self._hash("ci.json" if name == "ci" else "baseline.json")}
                for name in sorted(REQUIRED_CHECKS)
            ],
            "trusted_gate": {"run_id": 2, "run_attempt": 1, "artifact_id": 22,
                             "report_path": "trusted-gate.json", "report_sha256": self._hash("trusted-gate.json")},
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

    def test_structural_shadow_trace_passes_without_live_ci(self):
        self.assertEqual(evaluate(self.run, self.root, self.target), [])

    def test_writer_forged_review_files_cannot_make_cli_pass(self):
        # CI and structural checks are mocked green to isolate reviewer origin.
        # The two JSON files in setUp are writer-created, not agent session output.
        run_file = self.root / "run.json"
        run_file.write_text(json.dumps(self.run), encoding="utf-8")
        def checkout(command, **kwargs):
            if command[-2:] == ["rev-parse", "HEAD"]:
                return self.target + "\n"
            if command[-1] == "--show-current":
                return self.run["branch"] + "\n"
            if command[-1] == "--porcelain":
                return ""
            raise AssertionError(command)
        with patch("bootstrap.engrun.verify_changed_paths", return_value=[]), \
             patch("bootstrap.engrun.verify_github_ci", return_value=[]), \
             patch("bootstrap.engrun.verify_writer_session", return_value=[]), \
             patch("bootstrap.engrun.verify_writer_github", return_value=[]), \
             patch("bootstrap.engrun.subprocess.check_output", side_effect=checkout), \
             patch.object(sys, "argv", ["engrun.py", str(run_file), "--root", str(self.root), "--sha", self.target]):
            self.assertEqual(main(), 1)

    def test_writer_model_claim_cannot_make_cli_pass_without_session(self):
        # Isolate the writer boundary: assume separate reviewers and CI passed.
        # The fixture's writer provider/model are invented by its JSON author.
        run_file = self.root / "run.json"
        run_file.write_text(json.dumps(self.run), encoding="utf-8")
        def checkout(command, **kwargs):
            if command[-2:] == ["rev-parse", "HEAD"]:
                return self.target + "\n"
            if command[-1] == "--show-current":
                return self.run["branch"] + "\n"
            if command[-1] == "--porcelain":
                return ""
            raise AssertionError(command)
        with patch("bootstrap.engrun.verify_reviewer_sessions", return_value=[]), \
             patch("bootstrap.engrun.verify_changed_paths", return_value=[]), \
             patch("bootstrap.engrun.verify_github_ci", return_value=[]), \
             patch("bootstrap.engrun.verify_writer_github", return_value=[]), \
             patch("bootstrap.engrun.subprocess.check_output", side_effect=checkout), \
             patch.object(sys, "argv", ["engrun.py", str(run_file), "--root", str(self.root), "--sha", self.target]):
            self.assertEqual(main(), 1)

    def test_writer_model_and_github_login_require_external_observation(self):
        sessions = self.root / "writer-sessions"
        day = sessions / "2026" / "09" / "29"
        day.mkdir(parents=True)
        writer = self.run["writer"]
        writer["effective_provider"] = "openai"
        writer["effective_model"] = "gpt-6-sol"
        sid = writer["session_id"]
        path = day / f"rollout-2026-09-29T00-00-00-{sid}.jsonl"
        rows = [
            {"type": "session_meta", "payload": {"id": sid, "agent_path": None,
                "parent_thread_id": None, "model_provider": "openai"}},
            {"type": "turn_context", "payload": {"model": "gpt-6-sol"}},
        ]
        path.write_text("\n".join(json.dumps(row) for row in rows) + "\n", encoding="utf-8")
        self.assertEqual(verify_writer_session(self.run, sessions), [])
        writer["effective_model"] = "invented-model"
        self.assertTrue(verify_writer_session(self.run, sessions))
        writer["effective_model"] = "gpt-6-sol"
        live = {
            "pulls/9": {"number": 9, "state": "open", "user": {"login": "xbroute"},
                        "head": {"sha": self.target, "ref": self.run["branch"],
                                 "repo": {"full_name": "xbroute/hayool-os"}},
                        "base": {"sha": self.base}},
            f"commits/{self.target}": {"sha": self.target,
                "author": {"login": "xbroute"}, "committer": {"login": "xbroute"}},
        }
        with patch("bootstrap.engrun._github_json", side_effect=lambda key: live[key]):
            self.assertEqual(verify_writer_github(self.run, self.target), [])
            writer["github_login"] = "fake-writer"
            self.assertTrue(verify_writer_github(self.run, self.target))

    def test_external_final_answers_bind_review_bytes_and_identity(self):
        sessions = self.root / "external-codex-sessions"
        day = sessions / "2026" / "09" / "29"
        day.mkdir(parents=True)
        for i, review in enumerate(self.run["reviewers"], start=1):
            review["effective_provider"] = "openai"
            review["effective_model"] = "gpt-6-sol"
            report = {"target_sha": self.target, "read_only": True,
                      "verdict": "PASS", "findings": [],
                      "effective_provider": "openai", "effective_model": "gpt-6-sol"}
            self._write(f"review-{i}.json", report)
            review["report_sha256"] = self._hash(f"review-{i}.json")
            entries = [
                {"type": "session_meta", "payload": {"id": review["session_id"],
                    "agent_path": review["agent_path"],
                    "parent_thread_id": "11111111-1111-4111-8111-111111111111",
                    "model_provider": "openai"}},
                {"type": "turn_context", "payload": {"model": "gpt-6-sol"}},
                {"type": "response_item", "payload": {"id": review["response_item_id"],
                    "type": "message", "role": "assistant", "phase": "final_answer",
                    "content": [{"type": "output_text", "text":
                        (self.root / f"review-{i}.json").read_text(encoding="utf-8")}]}}
            ]
            path = day / f"rollout-2026-09-29T00-00-0{i}-{review['session_id']}.jsonl"
            path.write_text("\n".join(json.dumps(row) for row in entries) + "\n", encoding="utf-8")
            if i == 1:
                first_session = path
        self.assertEqual(verify_reviewer_sessions(self.run, self.root, self.target, sessions), [])
        # A writer can recalculate a local hash, but cannot make it equal the
        # independent final answer in the external session record.
        forged = {"target_sha": self.target, "read_only": True,
                  "verdict": "PASS", "findings": [],
                  "effective_provider": "openai", "effective_model": "gpt-6-sol",
                  "writer_added": "forged approval"}
        self._write("review-1.json", forged)
        self.run["reviewers"][0]["report_sha256"] = self._hash("review-1.json")
        self.assertTrue(verify_reviewer_sessions(self.run, self.root, self.target, sessions))
        self._write("review-1.json", {"target_sha": self.target, "read_only": True,
                                      "verdict": "PASS", "findings": [],
                                      "effective_provider": "openai", "effective_model": "gpt-6-sol"})
        self.run["reviewers"][0]["report_sha256"] = self._hash("review-1.json")
        correction = {"type": "response_item", "payload": {"id": "msg_later_correction",
            "type": "message", "role": "assistant", "phase": "final_answer",
            "content": [{"type": "output_text", "text": json.dumps({
                "target_sha": self.target, "read_only": True, "verdict": "FAIL",
                "findings": [{"id": "SEC-1", "severity": "P1", "status": "OPEN",
                              "target_sha": self.target, "summary": "later correction"}]})}]}}
        with first_session.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(correction) + "\n")
        self.assertTrue(verify_reviewer_sessions(self.run, self.root, self.target, sessions),
                        "a stale PASS cannot override the reviewer's later FAIL")

    def test_failure_injection_ai_votes_cannot_override_hard_failure(self):
        report = json.loads((self.root / "baseline.json").read_text())
        report["checks"]["secrets"] = "FAIL"
        self._write("baseline.json", report)
        for check in self.run["hard_checks"]:
            if check["name"] != "ci":
                check["report_sha256"] = self._hash("baseline.json")
        errors = evaluate(self.run, self.root, self.target)
        self.assertTrue(any("hard check secrets conflicts" in error for error in errors), errors)

    def test_ci_failure_cannot_be_replaced_by_local_pass(self):
        report = json.loads((self.root / "ci.json").read_text())
        report["checks"]["ci"] = "FAIL"
        report["conclusion"] = "failure"
        self._write("ci.json", report)
        for check in self.run["hard_checks"]:
            if check["name"] == "ci":
                check["report_sha256"] = self._hash("ci.json")
        errors = evaluate(self.run, self.root, self.target)
        self.assertTrue(any("GitHub CI proof" in error for error in errors), errors)

    def test_live_ci_verification_rejects_failed_run(self):
        with patch("bootstrap.engrun._github_json") as query:
            query.return_value = {"head_sha": self.target, "event": "pull_request", "status": "completed", "conclusion": "failure", "path": ".github/workflows/engineering-baseline.yml"}
            self.assertTrue(verify_github_ci(self.run, self.root, self.target))

    def test_live_ci_verification_accepts_exact_executed_run(self):
        responses = {
            "actions/runs/1": {"id": 1, "repository": {"full_name": "xbroute/hayool-os"}, "name": "engineering-candidate", "run_attempt": 1, "head_sha": self.target, "event": "pull_request", "status": "completed", "conclusion": "success", "path": ".github/workflows/engineering-baseline.yml", "pull_requests": [{"number": 9, "base": {"sha": self.base, "repo": {"name": "hayool-os"}}, "head": {"sha": self.target, "ref": "codex/shadow-test"}}]},
            "actions/runs/1/jobs": {"jobs": [{"id": 11, "name": "engineering-baseline", "head_sha": self.target, "conclusion": "success", "steps": [{"name": name, "conclusion": "success"} for name in ("Load policy from PR base", "Run deterministic M0 checks on PR head", "Preserve check evidence")]}]},
            "actions/runs/1/artifacts": {"artifacts": [{"id": 12, "name": "engineering-baseline-" + self.target, "expired": False, "digest": "sha256:" + "d" * 64}]},
            "actions/runs/2": {"id": 2, "repository": {"full_name": "xbroute/hayool-os"}, "event": "workflow_run", "head_branch": "main", "head_sha": self.base, "run_attempt": 1, "status": "completed", "conclusion": "success", "path": ".github/workflows/engineering-trusted-gate.yml"},
            "actions/runs/2/jobs": {"jobs": [{"name": "trusted-gate", "conclusion": "success", "steps": [{"name": name, "conclusion": "success"} for name in ("Verify exact candidate evidence with default-branch policy", "Preserve trusted-gate evidence")]}]},
            "actions/runs/2/artifacts": {"artifacts": [{"id": 22, "name": "engineering-trusted-gate-1", "expired": False, "workflow_run": {"id": 2}}]},
            "git/ref/heads/main": {"object": {"sha": self.base}},
        }
        artifact = json.loads((self.root / "baseline.json").read_text())
        trusted_bytes = (self.root / "trusted-gate.json").read_bytes()
        with patch("bootstrap.engrun._github_json", side_effect=lambda path: responses[path]), patch("bootstrap.engrun._download_baseline", return_value=artifact), patch("bootstrap.engrun._download_trusted", return_value=trusted_bytes):
            self.assertEqual(verify_github_ci(self.run, self.root, self.target), [])
            responses["actions/runs/2"]["conclusion"] = "failure"
            self.assertTrue(verify_github_ci(self.run, self.root, self.target))
            responses["actions/runs/2"]["conclusion"] = "success"
            responses["git/ref/heads/main"]["object"]["sha"] = "c" * 40
            self.assertTrue(verify_github_ci(self.run, self.root, self.target))
            responses["git/ref/heads/main"]["object"]["sha"] = self.base
            responses["actions/runs/1"]["pull_requests"][0]["base"]["sha"] = "c" * 40
            self.assertTrue(verify_github_ci(self.run, self.root, self.target))
            responses["actions/runs/1"]["pull_requests"][0]["base"]["sha"] = self.base
            artifact["checks"]["secrets"] = "FAIL"
            self.assertTrue(verify_github_ci(self.run, self.root, self.target))

    def test_failure_injection_ai_pass_votes_cannot_override_trusted_gate_failure(self):
        report = json.loads((self.root / "trusted-gate.json").read_text())
        report["decision"] = "FAIL"
        report["errors"] = ["candidate workflow differs from trusted policy bytes"]
        self._write("trusted-gate.json", report)
        self.run["trusted_gate"]["report_sha256"] = self._hash("trusted-gate.json")
        self.assertTrue(all(review["verdict"] == "PASS" for review in self.run["reviewers"]))
        errors = evaluate(self.run, self.root, self.target)
        self.assertTrue(any("trusted gate report failed" in error for error in errors), errors)

    def test_open_p1_finding_blocks_ai_pass_votes(self):
        finding = {"id": "SEC-1", "severity": "P1", "status": "OPEN",
                   "target_sha": self.target, "summary": "required check can be forged"}
        report = json.loads((self.root / "review-1.json").read_text())
        report["findings"] = [finding]
        self._write("review-1.json", report)
        self.run["reviewers"][0]["findings"] = [finding]
        self.run["reviewers"][0]["report_sha256"] = self._hash("review-1.json")
        self.assertTrue(all(review["verdict"] == "PASS" for review in self.run["reviewers"]))
        errors = evaluate(self.run, self.root, self.target)
        self.assertTrue(any("open P1" in error for error in errors), errors)

    def test_review_findings_must_be_present_and_match_hashed_report(self):
        del self.run["reviewers"][0]["findings"]
        errors = evaluate(self.run, self.root, self.target)
        self.assertTrue(any("findings differ" in error for error in errors), errors)

    def test_malformed_or_stale_finding_is_rejected(self):
        finding = {"id": "SEC-2", "severity": "P1", "status": "OPEN",
                   "target_sha": "c" * 40, "summary": "stale review"}
        self.run["reviewers"][0]["findings"] = [finding]
        self._write("review-1.json", {"target_sha": self.target, "read_only": True,
                                      "verdict": "PASS", "findings": [finding]})
        self.run["reviewers"][0]["report_sha256"] = self._hash("review-1.json")
        errors = evaluate(self.run, self.root, self.target)
        self.assertTrue(any("malformed, duplicate, or stale" in error for error in errors), errors)

    def test_open_p2_is_recorded_without_blocking(self):
        finding = {"id": "MAINT-2", "severity": "P2", "status": "OPEN",
                   "target_sha": self.target, "summary": "manual evidence entry"}
        self.run["reviewers"][0]["findings"] = [finding]
        self._write("review-1.json", {"target_sha": self.target, "read_only": True,
                                      "verdict": "PASS", "findings": [finding]})
        self.run["reviewers"][0]["report_sha256"] = self._hash("review-1.json")
        self.assertEqual(evaluate(self.run, self.root, self.target), [])

    def test_open_p0_blocks_and_closed_p1_needs_closure_evidence(self):
        findings = [
            {"id": "SEC-0", "severity": "P0", "status": "OPEN",
             "target_sha": self.target, "summary": "critical gate bypass"},
            {"id": "SEC-1", "severity": "P1", "status": "CLOSED",
             "target_sha": self.target, "summary": "fixed without evidence"},
        ]
        self.run["reviewers"][0]["findings"] = findings
        self._write("review-1.json", {"target_sha": self.target, "read_only": True,
                                      "verdict": "PASS", "findings": findings})
        self.run["reviewers"][0]["report_sha256"] = self._hash("review-1.json")
        errors = evaluate(self.run, self.root, self.target)
        self.assertTrue(any("open P0" in error for error in errors), errors)
        self.assertTrue(any("lacks closure evidence" in error for error in errors), errors)

    def test_protected_mode_does_not_accept_candidate_only_run(self):
        self.run["ci_mode"] = "protected_main_pr_target"
        del self.run["trusted_gate"]
        self.assertEqual(verify_github_ci(self.run, self.root, self.target),
                         ["protected-main trusted gate evidence is absent"])

    def test_regression_pr_controlled_workflow_cannot_self_attest(self):
        """A PR-controlled baseline workflow alone must never authorize ENG-RUN."""
        del self.run["trusted_gate"]
        responses = {
            "actions/runs/1": {"id": 1, "repository": {"full_name": "xbroute/hayool-os"}, "name": "engineering-candidate", "run_attempt": 1, "head_sha": self.target, "event": "pull_request", "status": "completed", "conclusion": "success", "path": ".github/workflows/engineering-baseline.yml@refs/pull/9/merge", "pull_requests": [{"number": 9, "base": {"sha": self.base, "repo": {"name": "hayool-os"}}, "head": {"sha": self.target, "ref": "codex/shadow-test"}}]},
            "actions/runs/1/jobs": {"jobs": [{"id": 11, "name": "engineering-baseline", "head_sha": self.target, "conclusion": "success", "steps": [{"name": name, "conclusion": "success"} for name in ("Load policy from PR base", "Run deterministic M0 checks on PR head", "Preserve check evidence")]}]},
            "actions/runs/1/artifacts": {"artifacts": [{"id": 12, "name": "engineering-baseline-" + self.target, "expired": False, "digest": "sha256:" + "d" * 64}]},
        }
        artifact = json.loads((self.root / "baseline.json").read_text())
        with patch("bootstrap.engrun._github_json", side_effect=lambda path: responses[path]), patch("bootstrap.engrun._download_baseline", return_value=artifact):
            self.assertEqual(verify_github_ci(self.run, self.root, self.target), ["candidate GitHub CI verified; trusted default-branch gate run is absent"])

    def test_changed_path_claim_must_equal_git_diff(self):
        with patch("bootstrap.engrun.subprocess.check_output", return_value="docs/adr/ADR_CATALOG.md\n"):
            self.assertTrue(verify_changed_paths(self.run, self.target))

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
