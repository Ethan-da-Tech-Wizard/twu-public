# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Daily encrypted, deduplicated backup of TWU_LLC with restic, to every repository that is reachable (USB stick, Google Drive).

Safe by design:
  * restic encrypts everything on this machine before it leaves; the passphrase file never leaves it either;
  * SQLite databases are copied with SQLite's own backup call into a staging folder (suffix .dbcopy), and the live
    .db/.db-wal/.db-shm files are excluded, so a copy never catches a database mid-write (Rule 7: read only);
  * skips itself when the STOP latch exists or the machine is hot; uploads are rate limited; one run at a time;
  * a failed or missing repository is logged and skipped, never fatal to the others;
  * weekly (Sunday): keep 7 daily / 4 weekly / 12 monthly snapshots and verify repository structure.
Results go to data/backup/ledger-<machine>.jsonl and show up in `ethan board`.

  ethan_backup.py            run one backup now (what the timer runs)
  ethan_backup.py --status   last result per repository
Restore a database copy: restore the snapshot, then rename X.db.dbcopy to X.db.
"""
import argparse, fcntl, json, os, platform, sqlite3, subprocess, sys, tempfile, time
from datetime import datetime
from pathlib import Path

def load_config():
    raise NotImplementedError('TODO: implement')

def log(rec):
    raise NotImplementedError('TODO: implement')

def too_hot():
    """True only if the coolest of 3 readings is over the line (a single reading is noisy on this laptop)."""
    raise NotImplementedError('TODO: implement')

def stage_databases(root=..., staging=...):
    """Copy every SQLite database under root into staging/<relative path>.dbcopy using SQLite's online backup."""
    raise NotImplementedError('TODO: implement')

def repo_available(repo):
    """USB repos need their mount point present; remote (rclone) repos are tried and fail soft."""
    raise NotImplementedError('TODO: implement')

def restic(cfg, repo, *args, timeout=...):
    raise NotImplementedError('TODO: implement')

def parse_summary(stdout):
    """The last JSON line of `restic backup --json` with message_type == summary."""
    raise NotImplementedError('TODO: implement')

def maintenance_due(now=None):
    raise NotImplementedError('TODO: implement')

def backup_one(cfg, repo):
    raise NotImplementedError('TODO: implement')

def mirror_one(cfg, mirror, results):
    """Copy an already-encrypted local restic repository to a remote as plain files with rclone.
    restic's own Google Drive backend makes thousands of tiny requests and hits Google's per-minute quota
    (403 rateLimitExceeded); copying the ~150 pack files stays far below it."""
    raise NotImplementedError('TODO: implement')

def maintain_one(cfg, repo):
    raise NotImplementedError('TODO: implement')

def status():
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
