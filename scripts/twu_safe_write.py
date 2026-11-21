# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Guarded write for files that several Magi share through Syncthing.

Claims are advisory and Syncthing only reports a conflict after the fact, so a plain overwrite can silently destroy another
worker's change. This helper is the missing last step of the proposal flow (scripts/magi_proposal.py prepare/review/verify-review):
it writes only if the target is still exactly what the writer read.

  twu_safe_write.py hash PATH                         print the sha256 of PATH (record it when you read the file)
  twu_safe_write.py write PATH --from-file NEW --expected-sha256 HASH [--dry-run]
  twu_safe_write.py write PATH --from-file NEW --create          (only when PATH does not exist yet)

Refuses (exit 2, nothing written) when: the target's sha256 differs from --expected-sha256; a PATH.sync-conflict-* sibling exists;
the target is a symlink or outside the repo; NEW is empty; or the target is a protected file (AGENTS.md, CLAUDE.md, STOP latch).
Edits publish via os.replace. Creates publish via a no-replace hard link. Both use a sibling temporary file and append a receipt to
data/health/safe_write.<host>.jsonl (per-host name, so Syncthing never sees two writers). Deterministic; no model, no network.
It is point-in-time evidence, not proof of exclusivity: another host may still change the file after the check.
"""
import argparse, hashlib, json, os, secrets, socket, sys, tempfile
from contextlib import ExitStack
from datetime import datetime, timezone
from pathlib import Path

def sha256_file(p):
    raise NotImplementedError('TODO: implement')

def conflict_siblings(path):
    raise NotImplementedError('TODO: implement')

def receipt_path(repo):
    raise NotImplementedError('TODO: implement')

def publish_new(repo, relative, data):
    """Create a complete file without replacing a concurrent writer or traversing a directory symlink."""
    raise NotImplementedError('TODO: implement')

def safe_write(path, data, expected_sha256=None, create=False, repo=..., dry_run=False, who=None):
    """Return {"ok": bool, "reason": str, ...}. Never raises for a refusal."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
