"""Run with: python3 -m unittest -v test_save_lab.py"""

import os
import stat
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

    @unittest.skipUnless(os.name == "posix", "POSIX filename limits required")
    def test_max_length_filename_can_be_replaced(self):
        name_max = os.pathconf(self.root, "PC_NAME_MAX")
        if name_max < 1:
            self.skipTest("filesystem does not report a finite filename limit")
        target = self.root / ("x" * name_max)
        target.write_bytes(b"OLD")

        safe_save(target, b"NEW")

        self.assertEqual(target.read_bytes(), b"NEW")
        self.assertEqual(sorted(p.name for p in self.root.iterdir()), [target.name])

    def test_directory_target_is_preserved_and_staging_is_cleaned(self):
        directory = self.root / "collection"
        directory.mkdir()
        marker = directory / "keep.txt"
        marker.write_bytes(b"KEEP")

        with patch("save_lab.tempfile.NamedTemporaryFile") as staging:
            with self.assertRaisesRegex(IsADirectoryError, "Target is a directory"):
                safe_save(directory, b"NEW")

        staging.assert_not_called()
        self.assertTrue(directory.is_dir())
        self.assertEqual(marker.read_bytes(), b"KEEP")
        self.assertEqual(sorted(p.name for p in self.root.iterdir()), ["collection"])

    @unittest.skipUnless(
        os.name == "posix" and hasattr(os, "mkfifo"),
        "POSIX named pipes required",
    )
    def test_named_pipe_target_is_preserved_without_staging(self):
        os.mkfifo(self.target)

        with patch("save_lab.tempfile.NamedTemporaryFile") as staging:
            with self.assertRaisesRegex(OSError, "not a regular file"):
                safe_save(self.target, b"NEW")

        staging.assert_not_called()
        self.assertTrue(stat.S_ISFIFO(self.target.lstat().st_mode))
        self.assertEqual(sorted(p.name for p in self.root.iterdir()), ["document.txt"])

    @unittest.skipUnless(os.name == "posix", "POSIX permission bits required")
    def test_replacement_preserves_existing_permission_bits(self):
        self.target.write_bytes(b"OLD")
        self.target.chmod(0o640)

        safe_save(self.target, b"NEW")

        self.assertEqual(stat.S_IMODE(self.target.stat().st_mode), 0o640)

    @unittest.skipUnless(os.name == "posix", "POSIX permission bits required")
    def test_replacement_drops_special_permission_bits(self):
        self.target.write_bytes(b"OLD")
        self.target.chmod(0o6755)
        self.assertEqual(stat.S_IMODE(self.target.stat().st_mode), 0o6755)

        safe_save(self.target, b"NEW")

        self.assertEqual(self.target.read_bytes(), b"NEW")
        self.assertEqual(stat.S_IMODE(self.target.stat().st_mode), 0o755)

    @unittest.skipUnless(os.name == "posix", "POSIX symlink behavior required")
    def test_symlink_target_replaces_link_without_touching_referent(self):
        referent = self.root / "referent.txt"
        referent.write_bytes(b"KEEP")
        self.target.symlink_to(referent.name)

        with patch("save_lab.os.fchmod") as fchmod:
            safe_save(self.target, b"NEW")

        fchmod.assert_not_called()
        self.assertFalse(self.target.is_symlink())
        self.assertEqual(self.target.read_bytes(), b"NEW")
        self.assertEqual(referent.read_bytes(), b"KEEP")

    @unittest.skipUnless(os.name == "posix", "POSIX permission bits required")
    def test_permission_copy_failure_preserves_original_and_cleans_staging(self):
        self.target.write_bytes(b"KNOWN GOOD")
        with (
            patch("save_lab.os.fchmod", side_effect=PermissionError("mode copy blocked")),
            patch("save_lab.os.replace") as replace,
        ):
            with self.assertRaisesRegex(PermissionError, "mode copy blocked"):
                safe_save(self.target, b"NEW")
        replace.assert_not_called()
        self.assertEqual(self.target.read_bytes(), b"KNOWN GOOD")
        self.assertEqual(sorted(p.name for p in self.root.iterdir()), ["document.txt"])

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

    def test_cleanup_failure_preserves_primary_error(self):
        self.target.write_bytes(b"KNOWN GOOD")
        with patch("save_lab.Path.unlink", side_effect=OSError("cleanup blocked")):
            with self.assertRaises(SimulatedInterruption) as raised:
                safe_save(self.target, b"NEW", interrupt_before_swap=True)
        if hasattr(raised.exception, "__notes__"):
            self.assertEqual(raised.exception.__notes__, ["Staging cleanup also failed: cleanup blocked"])
        else:
            self.assertRegex(str(raised.exception.__context__), "cleanup blocked")
        self.assertEqual(self.target.read_bytes(), b"KNOWN GOOD")

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

    def test_directory_sync_open_failure_is_reported_without_close(self):
        with (
            patch("save_lab.os.name", "posix"),
            patch("save_lab.os.O_DIRECTORY", 65536, create=True),
            patch("save_lab.os.O_RDONLY", 0, create=True),
            patch("save_lab.os.open", side_effect=OSError("directory sync unsupported")) as open_fd,
            patch("save_lab.os.close") as close,
        ):
            self.assertFalse(sync_directory(self.root))
        open_fd.assert_called_once_with(self.root, 65536)
        close.assert_not_called()

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

    def test_directory_sync_close_failure_is_reported(self):
        with (
            patch("save_lab.os.name", "posix"),
            patch("save_lab.os.O_DIRECTORY", 65536, create=True),
            patch("save_lab.os.O_RDONLY", 0, create=True),
            patch("save_lab.os.open", return_value=41) as open_fd,
            patch("save_lab.os.fsync") as fsync,
            patch("save_lab.os.close", side_effect=OSError("close blocked")) as close,
        ):
            self.assertFalse(sync_directory(self.root))
        open_fd.assert_called_once_with(self.root, 65536)
        fsync.assert_called_once_with(41)
        close.assert_called_once_with(41)

    def test_non_posix_directory_sync_returns_false_without_open(self):
        with (
            patch("save_lab.os.name", "nt"),
            patch("save_lab.os.open") as open_fd,
        ):
            self.assertFalse(sync_directory(self.root))
        open_fd.assert_not_called()

    def test_non_bytes_payload_preserves_original_without_staging(self):
        self.target.write_bytes(b"KNOWN GOOD")
        with self.assertRaisesRegex(TypeError, "payload must be bytes"):
            safe_save(self.target, "NEW")
        self.assertEqual(self.target.read_bytes(), b"KNOWN GOOD")
        self.assertEqual(sorted(p.name for p in self.root.iterdir()), ["document.txt"])

    def test_non_bytes_payload_is_rejected_before_filesystem_probe(self):
        missing_target = self.root / "does-not-exist" / "document.txt"
        with patch(
            "save_lab.Path.is_dir",
            side_effect=AssertionError("filesystem should not be probed"),
        ):
            with self.assertRaisesRegex(TypeError, "payload must be bytes"):
                safe_save(missing_target, "NEW")

    def test_non_bool_interruption_flag_is_rejected_before_filesystem_probe(self):
        self.target.write_bytes(b"KNOWN GOOD")

        for invalid in (0, 1, "false", None):
            with (
                self.subTest(invalid=invalid),
                patch("save_lab.Path.is_dir") as parent_probe,
                patch("save_lab.tempfile.NamedTemporaryFile") as staging,
            ):
                with self.assertRaisesRegex(TypeError, "must be a bool"):
                    safe_save(self.target, b"NEW", interrupt_before_swap=invalid)
                parent_probe.assert_not_called()
                staging.assert_not_called()

        self.assertEqual(self.target.read_bytes(), b"KNOWN GOOD")

    def test_missing_parent_fails_closed(self):
        missing_target = self.root / "does-not-exist" / "document.txt"
        with self.assertRaises(FileNotFoundError):
            safe_save(missing_target, b"NEW")
        self.assertFalse(missing_target.exists())

    def test_non_directory_parent_fails_closed_without_staging(self):
        parent = self.root / "parent.txt"
        parent.write_bytes(b"KEEP")
        nested_target = parent / "document.txt"

        with patch("save_lab.tempfile.NamedTemporaryFile") as staging:
            with self.assertRaisesRegex(
                NotADirectoryError, "Parent path is not a directory"
            ):
                safe_save(nested_target, b"NEW")

        staging.assert_not_called()
        self.assertEqual(parent.read_bytes(), b"KEEP")
        self.assertEqual(
            sorted(path.name for path in self.root.iterdir()),
            ["parent.txt"],
        )


if __name__ == "__main__":
    unittest.main()
