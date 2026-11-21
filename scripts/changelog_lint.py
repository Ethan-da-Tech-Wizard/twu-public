# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""changelog_lint: the CHANGELOG is the system's memory, so it must not duplicate itself.

  changelog_lint.py check [FILE]              exit 1 if there are NEW duplicate entry headers / long bullets beyond the baseline
  changelog_lint.py report [FILE]             list every duplicate (counts and line numbers, headers shortened)
  changelog_lint.py baseline [FILE] --yes     record today's duplicates as known (old ones are not rewritten; only NEW ones fail)
  changelog_lint.py upsert --header '## DATE - TITLE' --body-file F [--agent A] [--wait-s N] [--lock-root R] [--task-root R] [FILE]
                                              the ONLY write path: idempotent (same header = REPLACED, never appended twice), path-validated
                                              against --task-root (default the repo), one writer at a time via data/locks/<sha1>.lock;
                                              a lock held by a live process = BLOCKED-BY-LOCK, exit 75 (no retry; --wait-s N waits once, bounded)

Entry key = the full '## ' header line (date + title). Bullets only count when the whole stripped line is >= 100 chars
(short '- **`scripts/x.py`:**' prefixes legitimately repeat). Stdlib only, offline, deterministic.
"""
import hashlib
import json
import os
import re
import sys
from pathlib import Path

def _fp(s):
    raise NotImplementedError('TODO: implement')

def find_duplicates(text):
    """-> {"headers": {fp: [line numbers]}, "bullets": {fp: [line numbers]}} for keys that occur more than once."""
    raise NotImplementedError('TODO: implement')

def load_baseline(path=None):
    raise NotImplementedError('TODO: implement')

def new_duplicates(dups, base):
    """Duplicates whose COUNT exceeds what the baseline allowed (so an old known duplicate may not grow)."""
    raise NotImplementedError('TODO: implement')

class DuplicateWrite(Exception):
    """The write would leave a NEW duplicate (beyond the baseline); the file is left exactly as it was."""

def upsert(path, header, body, baseline=None):
    """Replace the entry whose header line equals `header` (trimmed), else insert it at the top. Idempotent.
    After writing, the result is checked against the baseline; a NEW duplicate rolls the write back and raises."""
    raise NotImplementedError('TODO: implement')

def upsert_locked(path, header, body, agent_id=..., session=None, lock_root=None, task_root=None, wait_s=0.0, ttl_s=30, baseline=None, _hook=None):
    """upsert() as the ONLY CHANGELOG write path: validate the path against the declared task root, hold the single-writer
    lock for the file (write_guard: data/locks/<sha1>.lock) across the whole read-modify-write, release in finally.
    A lock held by another live process is a hard stop: BlockedByLock, no retry. wait_s > 0 makes ONE bounded wait
    for a short-lived holder (a CHANGELOG write takes milliseconds) and then raises; the default is no waiting."""
    raise NotImplementedError('TODO: implement')

def _upsert(p, header, body):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
