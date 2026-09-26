"""Fast contract checks for the isolated candidate-test runner."""

import ast
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from bootstrap import baseline


class TestRunnerContract(unittest.TestCase):
    def test_no_inline_candidate_test_execution(self):
        source = Path(baseline.__file__).read_text(encoding="utf-8")
        module = ast.parse(source)
        unit = next(node for node in module.body if isinstance(node, ast.FunctionDef) and node.name == "unit")
        calls = [node for node in ast.walk(unit) if isinstance(node, ast.Call)]
        names = {node.func.attr for node in calls if isinstance(node.func, ast.Attribute)}
        self.assertNotIn("discover", names)
        self.assertNotIn("TextTestRunner", names)
        self.assertIn("Popen", names)

    def test_container_boundary_and_limits_are_required(self):
        constants = {value for value in baseline.unit.__code__.co_consts if isinstance(value, str)}
        for required in (
            "--network=none", "--read-only", "--cap-drop=ALL",
            "--security-opt=no-new-privileges", "--pids-limit=64",
            "--memory=512m", "--memory-swap=512m", "--cpus=1",
            "--user=65534:65534", "--tmpfs=/tmp:rw,nosuid,nodev,noexec,size=64m",
        ):
            self.assertIn(required, constants)
        self.assertTrue(baseline.TEST_IMAGE.startswith("docker.io/library/python@sha256:"))
        self.assertLessEqual(baseline.TEST_TIMEOUT_SECONDS, 90)
        self.assertLessEqual(baseline.TEST_OUTPUT_LIMIT_BYTES, 1_048_576)


if __name__ == "__main__":
    unittest.main()
