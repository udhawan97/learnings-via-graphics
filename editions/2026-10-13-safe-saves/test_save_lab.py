"""Run with: python3 -m unittest -v test_save_lab.py"""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from save_lab import SimulatedInterruption, safe_save, sync_directory


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

    def test_successful_first_save_creates_target_and_cleans_staging(self):
        safe_save(self.target, b"FIRST")
        self.assertEqual(self.target.read_bytes(), b"FIRST")
        self.assertEqual(sorted(p.name for p in self.root.iterdir()), ["document.txt"])

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

    def test_directory_sync_failure_is_reported_after_replacement(self):
        self.target.write_bytes(b"OLD")
        with patch("save_lab.sync_directory", return_value=False) as sync:
            parent_synced = safe_save(self.target, b"NEW")
        self.assertFalse(parent_synced)
        sync.assert_called_once_with(self.root)
        self.assertEqual(self.target.read_bytes(), b"NEW")
        self.assertEqual(sorted(p.name for p in self.root.iterdir()), ["document.txt"])

    def test_directory_sync_closes_descriptor_after_sync_failure(self):
        with (
            patch("save_lab.os.name", "posix"),
            patch("save_lab.os.O_DIRECTORY", 65536, create=True),
            patch("save_lab.os.O_RDONLY", 0, create=True),
            patch("save_lab.os.open", return_value=41) as open_fd,
            patch("save_lab.os.fsync", side_effect=OSError("sync blocked")),
            patch("save_lab.os.close") as close,
        ):
            self.assertFalse(sync_directory(self.root))
        open_fd.assert_called_once_with(self.root, 65536)
        close.assert_called_once_with(41)

    def test_directory_sync_closes_descriptor_after_success(self):
        with (
            patch("save_lab.os.name", "posix"),
            patch("save_lab.os.O_DIRECTORY", 65536, create=True),
            patch("save_lab.os.O_RDONLY", 0, create=True),
            patch("save_lab.os.open", return_value=41) as open_fd,
            patch("save_lab.os.fsync") as fsync,
            patch("save_lab.os.close") as close,
        ):
            self.assertTrue(sync_directory(self.root))
        open_fd.assert_called_once_with(self.root, 65536)
        fsync.assert_called_once_with(41)
        close.assert_called_once_with(41)

    def test_non_bytes_payload_preserves_original_without_staging(self):
        self.target.write_bytes(b"KNOWN GOOD")
        with self.assertRaisesRegex(TypeError, "payload must be bytes"):
            safe_save(self.target, "NEW")
        self.assertEqual(self.target.read_bytes(), b"KNOWN GOOD")
        self.assertEqual(sorted(p.name for p in self.root.iterdir()), ["document.txt"])

    def test_missing_parent_fails_closed(self):
        missing_target = self.root / "does-not-exist" / "document.txt"
        with self.assertRaises(FileNotFoundError):
            safe_save(missing_target, b"NEW")
        self.assertFalse(missing_target.exists())


if __name__ == "__main__":
    unittest.main()
