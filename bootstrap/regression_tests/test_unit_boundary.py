"""End-to-end regression for the PR-test/trusted-checker process boundary."""

import os
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from bootstrap import baseline


POISON_TEST = textwrap.dedent("""\
    import os
    import socket
    import sys
    import unittest

    def forged_security():
        return []

    # This replaces the actual hard check under the old in-process loader.
    trusted = sys.modules['__main__']
    if hasattr(trusted, 'security'):
        trusted.security.__code__ = forged_security.__code__

    class PoisonTest(unittest.TestCase):
        def test_container_has_no_secret_or_host_write(self):
            if not hasattr(trusted, 'security'):
                self.assertNotIn('GITHUB_TOKEN', os.environ)
                self.assertTrue(os.statvfs('/candidate').f_flag & os.ST_RDONLY)
                with self.assertRaises(OSError):
                    open('/candidate/probe', 'w').close()
                sock = socket.socket()
                try:
                    self.assertNotEqual(sock.connect_ex(('1.1.1.1', 53)), 0)
                finally:
                    sock.close()
""")


class CandidateTestBoundary(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="hayool-unit-boundary-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        os.chmod(self.root, 0o755)  # The container's non-root user can traverse it.
        test_dir = self.root / "bootstrap" / "tests"
        test_dir.mkdir(parents=True)
        (test_dir / "test_poison.py").write_text(POISON_TEST, encoding="utf-8")

    def test_old_inline_loader_is_exploitable(self):
        # A disposable old-style loader demonstrates the pre-fix failure; it
        # cannot mutate this host process or the repository.
        vulnerable = textwrap.dedent("""\
            import sys, unittest
            from pathlib import Path
            def security():
                return ['HARD FAILURE']
            suite = unittest.defaultTestLoader.discover(sys.argv[1], pattern='test_*.py')
            result = unittest.TextTestRunner().run(suite)
            assert result.wasSuccessful()
            assert security() == [], 'old loader did not reproduce the exploit'
            print('OLD_INLINE_GATE_BYPASSED')
        """)
        result = subprocess.run(
            [sys.executable, "-c", vulnerable, str(self.root / "bootstrap" / "tests")],
            capture_output=True, text=True, timeout=15, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("OLD_INLINE_GATE_BYPASSED", result.stdout)

    def test_isolated_runner_keeps_trusted_state_and_secrets_out(self):
        original_security_code = baseline.security.__code__
        original_patterns = dict(baseline.SECRET_PATTERNS)
        with patch.object(baseline, "ROOT", self.root), patch.dict(os.environ, {"GITHUB_TOKEN": "SENTINEL-NOT-FOR-TESTS"}):
            self.assertEqual(baseline.unit(), [])
        self.assertIs(baseline.security.__code__, original_security_code)
        self.assertEqual(baseline.SECRET_PATTERNS, original_patterns)


if __name__ == "__main__":
    unittest.main()
