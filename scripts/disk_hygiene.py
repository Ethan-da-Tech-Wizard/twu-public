# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""
PROGRAM:       disk_hygiene.py
PROGRAMMER:    Magi 10 (claude, example_host), at Ethan's request
LAST MODIFIED: 2026-11-19
PURPOSE:       Stop stale Syncthing conflict copies from filling the disk.

WHY THIS EXISTS
  scripts/sync_conflict_archive.py MOVES conflict copies into archive/ and never
  deletes them, so a large file that conflicts repeatedly (data/knowledge/index.db,
  about 130 MB each) piles up forever: on 2026-11-19 archive/ held about 1.2 GB of
  index.sync-conflict-*.db copies (200 files under archive/2026-11-18 and
  archive/sync_conflicts).  This script adds the missing retention step.

WHAT IT DOES
  report (default): read-only. Lists conflict copies under archive/ and .stversions/
                    with sizes and ages, and what `prune` WOULD remove.
  prune --apply:    deletes ONLY files whose name contains `.sync-conflict-`, that sit
                    under archive/, are older than --days (default 3), and are not the
                    newest copy for their base name (the newest of each is always kept).
                    Without --apply it is a dry run.
  Never touches live (non-archive) conflict files, anything outside the workspace,
  symlinks, or files without the `.sync-conflict-` marker.  Live conflicts belong to
  sync_conflict_archive.py / magi.py, which decide which side wins.

UNDO: deleted copies are not recoverable.  They were already archived duplicates of
  files whose base copy is still live; the dry run prints every path first.

CHANGE HISTORY:
  2026-11-19  Magi 10  Created.
  2026-11-20  Magi 10  Seventh .stignore block: per-host home page cache (data/dashboard/home_cache.<host>.html).
  2026-11-19  Magi 10  prune --apply also (a) deletes old archive/*/evolve-* rollback folders
                       (ethan_evolve.py wrote ~233,000 files / 4 GB of them into the synced tree, 58% of
                       everything Syncthing tracked, the main cause of slow sync) keeping the 5 newest and
                       anything younger than 2 days, and (b) makes sure this host's .stignore carries the
                       sync-speed block so Syncthing stops scanning them. Undo (b): delete the marked block.
"""
from __future__ import annotations
import argparse
import re
import shutil
import sys
import time
from pathlib import Path

def human(n: float) -> str:
    """Format a byte count as a short human string (GB/MB/KB)."""
    raise NotImplementedError('TODO: implement')

def conflict_files(top: Path):
    """Yield (path, size, mtime) for regular conflict-marked files under top."""
    raise NotImplementedError('TODO: implement')

def plan_prune(days: float):
    """Return (to_delete, kept) lists of (path, size) for archive/ conflict copies."""
    raise NotImplementedError('TODO: implement')

def ensure_ignores(apply: bool) -> str:
    """Append each missing ignore block to ROOT/.stignore (once). Returns a one-line status."""
    raise NotImplementedError('TODO: implement')

def prune_evolve(apply: bool, keep: int=5, days: float=2.0):
    """Delete old archive/*/evolve-* folders (keep the newest `keep` and anything younger than `days`)."""
    raise NotImplementedError('TODO: implement')

def main() -> int:
    raise NotImplementedError('TODO: implement')
