"""Adversarial checks for SHA-bound traceability and immutable M0 tests."""

import json
import os
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from bootstrap import baseline  # noqa: E402


TRACE = "REQ: REQ-GOV-004\nADR: ADR-033\nRisk: R3\nTests: gate regressions\nEvidence: exact-SHA CI\nMigration: none\n"


class GateRegressions(unittest.TestCase):
    def test_pr_body_edit_cannot_change_sha_bound_traceability(self):
        with tempfile.TemporaryDirectory() as directory:
            event = Path(directory) / "event.json"
            with patch.object(baseline, "git", return_value=TRACE), patch.dict(
                os.environ, {"GITHUB_EVENT_PATH": str(event)}
            ):
                event.write_text(json.dumps({"pull_request": {"body": "invalid"}}))
                self.assertEqual(baseline.traceability(), [])
                event.write_text(json.dumps({"pull_request": {"body": TRACE}}))
                self.assertEqual(baseline.traceability(), [])
            with patch.object(baseline, "git", return_value="No trace\n"), patch.dict(
                os.environ, {"GITHUB_EVENT_PATH": str(event)}
            ):
                self.assertTrue(baseline.traceability())

    def test_new_poison_test_cannot_mask_existing_test_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            tests = Path(directory)
            (tests / "test_000_poison.py").write_text(textwrap.dedent("""\
                import unittest
                def skip_real_test(self, result=None):
                    return unittest.TestResult()
                unittest.TestCase.run = skip_real_test
                class Poison(unittest.TestCase):
                    def test_present(self):
                        pass
            """))
            (tests / "test_100_existing.py").write_text(textwrap.dedent("""\
                import unittest
                class Existing(unittest.TestCase):
                    def test_must_fail(self):
                        self.fail('existing hard failure')
            """))
            vulnerable = textwrap.dedent("""\
                import sys, unittest
                suite = unittest.defaultTestLoader.discover(sys.argv[1], pattern='test_*.py')
                count = suite.countTestCases()
                result = unittest.TextTestRunner().run(suite)
                assert count > 0 and result.wasSuccessful()
                print('OLD_SUITE_FAILURE_MASKED')
            """)
            old = subprocess.run([sys.executable, "-I", "-c", vulnerable, directory],
                                 capture_output=True, text=True, timeout=15, check=False)
            self.assertEqual(old.returncode, 0, old.stderr)
            self.assertIn("OLD_SUITE_FAILURE_MASKED", old.stdout)
        with patch.object(baseline.subprocess, "run", return_value=SimpleNamespace(returncode=0)), \
             patch.object(baseline, "git", return_value="A\tbootstrap/tests/test_000_poison.py"):
            errors = baseline.test_integrity("a" * 40, "b" * 40)
        self.assertTrue(any("candidate changed test" in error for error in errors), errors)

    def test_new_package_or_import_shadow_cannot_poison_fixed_suite(self):
        for path in ("bootstrap/__init__.py", "datetime.py"):
            with self.subTest(path=path), \
                 patch.object(baseline.subprocess, "run", return_value=SimpleNamespace(returncode=0)), \
                 patch.object(baseline, "git", return_value="A\t" + path):
                errors = baseline.test_integrity("a" * 40, "b" * 40)
                self.assertTrue(any("protected M0 path" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
