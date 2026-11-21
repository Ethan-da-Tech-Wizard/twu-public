# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""guarded_write: optimistic locking for shared files (compare-and-swap on the file's SHA-256). Stdlib only, local only.

Magi file claims are advisory: nothing stops another writer. This is the enforcement a writer can opt into:

  guarded_write.py hash PATH                      print the SHA-256 of PATH (record it when you READ the file)
  guarded_write.py write PATH --expect SHA        replace PATH with stdin, but ONLY if PATH still hashes to SHA
  guarded_write.py write PATH --expect-missing    create PATH, but ONLY if it does not exist

Exit 0 written | 3 CONCURRENT MODIFICATION (file changed since you read it; nothing written; re-read, re-apply, retry) | 2 bad use.
The compare and the replace happen under one per-file exclusive lock, and the replace is atomic (temp file + os.replace), so of two
writers holding the same expected hash exactly one succeeds. Limit, stated plainly: it only protects writers that call it. An
editor or script that writes the file directly is not stopped; that needs an OS permission or an editor hook.
"""
from __future__ import annotations
import fcntl
import hashlib
import os
import sys
import tempfile
from pathlib import Path

class ConcurrentModification(Exception):
    """The file's content is no longer the content the writer read."""

def sha256_of(path) -> str | None:
    raise NotImplementedError('TODO: implement')

def _lock_path(path: Path) -> Path:
    raise NotImplementedError('TODO: implement')

def write_if_unchanged(path, data: bytes, expected_sha256: str | None) -> str:
    """Write `data` to `path` iff it still hashes to `expected_sha256` (None = must not exist). Returns the new SHA-256."""
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
