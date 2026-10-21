"""Run with: python3 -m unittest -v test_save_lab.py"""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from save_lab import SimulatedInterruption, safe_save


class SafeSaveLabTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="safe-save-tests-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.target = self.root / "document.txt"

    def test_successful_replacement_writes_exact_new_bytes(self):
        self.target.write_bytes(b"OLD")
        safe_save(self.target, b"NEW")
        self.assertEqual(self.target.read_bytes(), b"NEW")

    def test_interruption_before_replace_keeps_original(self):
        self.target.write_bytes(b"KNOWN GOOD")
        with self.assertRaises(SimulatedInterruption):
            safe_save(self.target, b"INCOMPLETE", interrupt_before_swap=True)
        self.assertEqual(self.target.read_bytes(), b"KNOWN GOOD")

    def test_failed_first_write_creates_no_target(self):
        with self.assertRaises(SimulatedInterruption):
            safe_save(self.target, b"FIRST", interrupt_before_swap=True)
        self.assertFalse(self.target.exists())

    def test_staging_is_cleaned_after_failure(self):
        self.target.write_bytes(b"OLD")
        with self.assertRaises(SimulatedInterruption):
            safe_save(self.target, b"NEW", interrupt_before_swap=True)
        self.assertEqual(sorted(p.name for p in self.root.iterdir()), ["document.txt"])

    def test_replace_failure_preserves_original_and_cleans_staging(self):
        self.target.write_bytes(b"KNOWN GOOD")
        with patch("save_lab.os.replace", side_effect=PermissionError("replace blocked")):
            with self.assertRaisesRegex(PermissionError, "replace blocked"):
                safe_save(self.target, b"NEW")
        self.assertEqual(self.target.read_bytes(), b"KNOWN GOOD")
        self.assertEqual(sorted(p.name for p in self.root.iterdir()), ["document.txt"])

    def test_file_sync_failure_preserves_original_and_cleans_staging(self):
        self.target.write_bytes(b"KNOWN GOOD")
        with (
            patch("save_lab.os.fsync", side_effect=OSError("sync failed")),
            patch("save_lab.os.replace") as replace,
        ):
            with self.assertRaisesRegex(OSError, "sync failed"):
                safe_save(self.target, b"NEW")
        replace.assert_not_called()
        self.assertEqual(self.target.read_bytes(), b"KNOWN GOOD")
        self.assertEqual(sorted(p.name for p in self.root.iterdir()), ["document.txt"])

    def test_missing_parent_fails_closed(self):
        missing_target = self.root / "does-not-exist" / "document.txt"
        with self.assertRaises(FileNotFoundError):
            safe_save(missing_target, b"NEW")
        self.assertFalse(missing_target.exists())


if __name__ == "__main__":
    unittest.main()
