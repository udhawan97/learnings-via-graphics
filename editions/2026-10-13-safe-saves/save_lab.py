"""Offline teaching lab: stage, sync, and replace a file in a trusted directory.

This example illustrates an interruption *before rename*. It cannot simulate a
real power cut, storage-device dishonesty, concurrent writers, or cloud sync.
Only use paths inside a directory you own and trust.
"""

from __future__ import annotations

import os
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
    try:
        try:
            os.fsync(fd)
        except OSError:
            return False
        return True
    finally:
        os.close(fd)


def safe_save(target: Path, payload: bytes, *, interrupt_before_swap: bool = False) -> bool:
    """Stage bytes beside target; sync temp; replace target; try dir sync.

    Assumes a trusted directory and a single writer. Returns whether the
    optional directory-sync attempt succeeded, *not* a durability guarantee.
    """
    target = Path(target)
    if not target.parent.is_dir():
        raise FileNotFoundError(f"Parent directory does not exist: {target.parent}")
    if not isinstance(payload, bytes):
        raise TypeError("payload must be bytes")

    scratch: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb", dir=target.parent, prefix=f".{target.name}.",
            suffix=".tmp", delete=False
        ) as file:
            scratch = Path(file.name)
            file.write(payload)
            file.flush()
            os.fsync(file.fileno())
        if interrupt_before_swap:
            raise SimulatedInterruption("Stop after temp sync, before replacement")
        os.replace(scratch, target)
        return sync_directory(target.parent)
    finally:
        if scratch is not None:
            scratch.unlink(missing_ok=True)


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
