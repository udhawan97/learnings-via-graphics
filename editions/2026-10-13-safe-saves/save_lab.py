"""Offline teaching lab: stage, sync, and replace a file in a trusted directory.

This example illustrates an interruption *before rename*. It cannot simulate a
real power cut, storage-device dishonesty, concurrent writers, or cloud sync.
Only use paths inside a directory you own and trust.
"""

from __future__ import annotations

import os
import stat
import sys
import tempfile
from pathlib import Path


class SimulatedInterruption(RuntimeError):
    """An intentional failure before the replacement step."""


def sync_directory(directory: Path) -> bool:
    """Try to fsync the parent on POSIX; return False when unsupported.

    Return value is observational, not a guarantee against power loss.
    """
    if os.name != "posix" or not hasattr(os, "O_DIRECTORY"):
        return False
    try:
        fd = os.open(directory, os.O_RDONLY | os.O_DIRECTORY)
    except OSError:
        return False
    synced = True
    try:
        try:
            os.fsync(fd)
        except OSError:
            synced = False
    finally:
        try:
            os.close(fd)
        except OSError:
            synced = False
    return synced


def safe_save(target: Path, payload: bytes, *, interrupt_before_swap: bool = False) -> bool:
    """Stage bytes beside target; sync temp; replace target; try dir sync.

    On POSIX, preserve an existing regular file's ordinary read/write/execute
    permission bits, but not set-user-ID, set-group-ID, or sticky bits. Ownership,
    ACLs, extended metadata, and new-file policy remain outside this lab.
    Assumes a trusted directory and a single writer. Returns whether the
    optional directory-sync attempt succeeded, *not* a durability guarantee.
    """
    target = Path(target)
    if not isinstance(payload, bytes):
        raise TypeError("payload must be bytes")
    if type(interrupt_before_swap) is not bool:
        raise TypeError("interrupt_before_swap must be a bool")
    parent = target.parent
    if not parent.is_dir():
        if parent.exists():
            raise NotADirectoryError(f"Parent path is not a directory: {parent}")
        raise FileNotFoundError(f"Parent directory does not exist: {parent}")

    existing_mode: int | None = None
    try:
        target_status = target.lstat()
    except FileNotFoundError:
        target_status = None
    if target_status is not None and stat.S_ISDIR(target_status.st_mode):
        raise IsADirectoryError(f"Target is a directory: {target}")
    if target_status is not None and not (
        stat.S_ISREG(target_status.st_mode) or stat.S_ISLNK(target_status.st_mode)
    ):
        raise OSError(f"Target is not a regular file or symbolic link: {target}")
    if (
        os.name == "posix"
        and target_status is not None
        and stat.S_ISREG(target_status.st_mode)
    ):
        existing_mode = stat.S_IMODE(target_status.st_mode) & 0o777

    scratch: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb", dir=parent, prefix=".safe-save-",
            suffix=".tmp", delete=False
        ) as file:
            scratch = Path(file.name)
            written = file.write(payload)
            if written != len(payload):
                raise OSError(
                    f"Staging write was incomplete: expected {len(payload)} bytes, "
                    f"wrote {written}"
                )
            file.flush()
            if existing_mode is not None:
                os.fchmod(file.fileno(), existing_mode)
            os.fsync(file.fileno())
        if interrupt_before_swap:
            raise SimulatedInterruption("Stop after temp sync, before replacement")
        os.replace(scratch, target)
        return sync_directory(parent)
    finally:
        primary_error = sys.exc_info()[1]
        if scratch is not None:
            try:
                scratch.unlink(missing_ok=True)
            except OSError as cleanup_error:
                if primary_error is None:
                    raise
                if hasattr(primary_error, "add_note"):
                    primary_error.add_note(f"Staging cleanup also failed: {cleanup_error}")
                else:
                    primary_error.__context__ = cleanup_error


def demo() -> None:
    with tempfile.TemporaryDirectory(prefix="safe-save-demo-") as root:
        document = Path(root) / "note.txt"
        document.write_bytes(b"Version A: old and complete\n")
        try:
            safe_save(document, b"Version B: new and complete\n", interrupt_before_swap=True)
        except SimulatedInterruption:
            print("Injected failure: old version preserved:", document.read_text().strip())
        parent_synced = safe_save(document, b"Version B: new and complete\n")
        print("Successful replace:", document.read_text().strip())
        print("Parent-directory fsync attempted successfully:", parent_synced)
        print("Actual power-loss / concurrency guarantees: NOT TESTED")


if __name__ == "__main__":
    demo()
