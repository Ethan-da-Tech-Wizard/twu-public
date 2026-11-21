# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Tree keeper: keep the shared workspace git tree clean enough for the Ethan task gate.

  check        list dirty files, classified as runtime (machine-written) or work
  checkpoint   when no dirty file changed in the last N seconds, commit everything locally
  return-main  on an ethan/* branch whose tracked tree is clean, ff-merge it into main and check out main

Local only: never pushes, never stashes/resets/cleans, refuses during merge/rebase/cherry-pick/revert.
"""
from __future__ import annotations
import argparse
import fnmatch
import json
import os
import re
import stat
import subprocess
import sys
import time
from pathlib import Path

def safe_work_path(root: Path, path: str) -> bool:
    """A work file may be checkpointed locally if it is a small regular file with no private prefix or secret."""
    raise NotImplementedError('TODO: implement')

def is_checkpointable(path: str) -> bool:
    raise NotImplementedError('TODO: implement')

def active_cli_session(ledger: Path | None=None, tail: int=400) -> int | None:
    """PID of a live Ethan CLI session, else None (shared helper ethan_cli_session; moving the repo off the CLI's ethan/*
    task branch mid-session broke visible local-model runs on 2026-11-05, so the keeper does nothing while one is alive)."""
    raise NotImplementedError('TODO: implement')

def _any_live_git_process(proc_root: Path=...) -> bool:
    """Return True if any live git process exists, or if process liveness cannot be verified (fail-closed)."""
    raise NotImplementedError('TODO: implement')

def reap_stale_index_lock(gitdir: Path, max_age_s: int=...) -> bool:
    """Remove an orphaned .git/index.lock only when regular, owned by us, >= max_age_s old, and no git process is alive."""
    raise NotImplementedError('TODO: implement')

def git(root: Path, *args: str, check: bool=False) -> subprocess.CompletedProcess:
    raise NotImplementedError('TODO: implement')

def classify(path: str) -> str:
    raise NotImplementedError('TODO: implement')

def dirty(root: Path) -> list[tuple[str, str]]:
    raise NotImplementedError('TODO: implement')

def in_progress(root: Path) -> str | None:
    raise NotImplementedError('TODO: implement')

def task_blocker(root: Path) -> str | None:
    """A disconnected CLI still owns its unfinished task; process absence is insufficient."""
    raise NotImplementedError('TODO: implement')

def newest_mtime(root: Path, items: list[tuple[str, str]]) -> float:
    raise NotImplementedError('TODO: implement')

def cmd_check(root: Path, _a) -> int:
    raise NotImplementedError('TODO: implement')

def cmd_checkpoint(root: Path, args) -> int:
    raise NotImplementedError('TODO: implement')

def cmd_return_main(root: Path, _a) -> int:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
