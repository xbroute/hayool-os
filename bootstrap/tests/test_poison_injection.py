"""Controlled M0 attack fixture; this draft PR must never be merged."""

import os
import socket
import sys
import unittest


def forged_security():
    return []


trusted = sys.modules["__main__"]
if hasattr(trusted, "security"):
    # The former inline test loader let this replace the later hard check.
    trusted.security.__code__ = forged_security.__code__


class PoisonInjection(unittest.TestCase):
    def test_candidate_cannot_mutate_host_checker_or_access_secrets(self):
        if not hasattr(trusted, "security"):
            self.assertNotIn("GITHUB_TOKEN", os.environ)
            self.assertTrue(os.statvfs("/candidate").f_flag & os.ST_RDONLY)
            with self.assertRaises(OSError):
                open("/candidate/probe", "w").close()
            connection = socket.socket()
            try:
                self.assertNotEqual(connection.connect_ex(("1.1.1.1", 53)), 0)
            finally:
                connection.close()
