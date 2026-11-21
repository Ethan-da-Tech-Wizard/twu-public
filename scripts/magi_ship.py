# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""
================================================================================
MODULE:        scripts.magi_ship
ROLE:          One-command, beginner-safe "commit exactly my files" wrapper
AUTHOR:        Magi (TWU LLC); requested by Ethan on 2026-11-19
OWNER / LAST CHANGED: Magi 23, 2026-11-19
LICENSE:       Apache-2.0
================================================================================

PURPOSE:
    A Magi in the shared, dirty TWU_LLC tree must commit ONLY its own files.
    The sanctioned flow (scripts/ethan_git_guard.py: begin, stage, verify, finish)
    needs 4 to 5 commands with sharp edges. This script runs that exact flow for
    the exact paths you name and prints plain results.

ARCHITECTURE & SYSTEM ROLE:
    - Upstream Callers: a Magi seat at the terminal; `scripts/magi.py leave`
                        (which imports `leave_warning` to print a reminder).
    - Downstream Deps:  `scripts/ethan_git_guard.py` (the ONLY thing that stages,
                        verifies and commits), read-only `git status`/`rev-parse`,
                        `data/comms/claims.json` (read only).
    - Layer:            Thin convenience wrapper. It is NOT a second git
                        implementation: every write to git goes through the guard.

DATA FLOW:
    paths ──> checks (inside repo, not secret, STOP absent, has changes)
          ──> preview (will commit / will leave alone)
          ──> guard begin [--adopt-dirty] ──> guard stage ──> guard verify --staged
          ──> guard finish -m MESSAGE ──> plain result

KEY INVARIANTS:
    1. Never pushes, never adds or edits a remote, never runs checkout, reset,
       stash, clean, `add -A` or `commit -a`. The only git commands run directly
       are read-only (`status`, `rev-parse`, `ls-files`, `diff --name-only`).
    2. Only the named paths are committed; every other dirty file is untouched.
    3. If the STOP latch exists, nothing is done.
    4. A failed step stops the run and says which step and why; no retries.

SECURITY & FAILURE BOUNDARIES:
    - Refuses absolute paths, `..`, symlinks, and secret-looking names before
      the guard even starts (the guard then scans file CONTENT for credentials).
    - Honest limit: a file that others also edited is committed WHOLE, including
      their edits. Git cannot split a file by author here.

HOW TO TEST: cd scripts; ETHAN_HOST=1 python3 -m unittest test_magi_ship

USAGE SYNOPSIS:
    python3 scripts/magi_ship.py --seat 5 --status
    python3 scripts/magi_ship.py --seat 5 -m "Add X. Why: ... Tests: ..." scripts/x.py scripts/test_x.py
    python3 scripts/magi_ship.py --seat 5 --dry-run -m "..." scripts/x.py
================================================================================
"""
from __future__ import annotations
import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path

class ShipError(RuntimeError):
    """A deliberate refusal with a plain-language reason (not a crash)."""

def _git_readonly(root: Path, args: list[str]) -> str:
    """Run one READ-ONLY git command in `root` and return stdout ('' on failure)."""
    raise NotImplementedError('TODO: implement')

def _guard(root: Path, args: list[str]) -> tuple[int, str]:
    """
    Run ethan_git_guard.py with `args`. This is the single place any git change happens.
    Returns (exit_code, combined output). Raises ShipError if the guard file is missing.
    """
    raise NotImplementedError('TODO: implement')

def check_paths(root: Path, paths: list[str]) -> list[str]:
    """
    Turn user-typed paths into clean repo-relative paths, or raise ShipError.

    PRECONDITIONS: `paths` is non-empty. POSTCONDITIONS: unique, sorted, relative,
    inside `root`, regular files that exist (or are tracked and deleted), not secret-looking.
    """
    raise NotImplementedError('TODO: implement')

def dirty_files(root: Path) -> dict[str, str]:
    """Return {path: 'tracked'|'new'} for every uncommitted change in the whole tree (read only)."""
    raise NotImplementedError('TODO: implement')

def classify(root: Path, paths: list[str]) -> tuple[list[str], list[str], list[str]]:
    """
    Split requested paths into (tracked_dirty, new, unchanged).
    A path that exists but is not in any git listing (e.g. ignored by the scripts/ default-deny
    rule) counts as 'new' when it is not tracked: the guard force-adds exact paths.
    """
    raise NotImplementedError('TODO: implement')

def active_task(root: Path) -> dict:
    """Read the guard's single task record (.git/ethan-task.json); {} if none."""
    raise NotImplementedError('TODO: implement')

def current_branch(root: Path) -> str:
    """Name of the checked-out branch ('' if detached or git fails). Read-only."""
    raise NotImplementedError('TODO: implement')

def check_ready(root: Path, paths: list[str]) -> bool:
    """
    Decide whether we start fresh on main (False) or resume our own unfinished task (True).
    Raises ShipError when someone else's task blocks us (the guard allows ONE active task).
    """
    raise NotImplementedError('TODO: implement')

def read_claims(root: Path, seat: int) -> list[tuple[str, bool]]:
    """Return [(path, still_live)] for claims of `seat` in the claims registry (read only)."""
    raise NotImplementedError('TODO: implement')

def seat_uncommitted(root: Path, seat: int) -> list[str]:
    """Claimed paths of `seat` that are still uncommitted (sorted)."""
    raise NotImplementedError('TODO: implement')

def ship_command(seat: int, paths: list[str]) -> str:
    """The exact copy-paste command that commits `paths` (printed in warnings so a beginner never has to compose it)."""
    raise NotImplementedError('TODO: implement')

def leave_warning(root: Path, seat: int) -> str:
    """
    Text for `magi.py leave`: '' when nothing is pending, else a plain warning plus the exact
    command. A warning only; leaving is never blocked.
    """
    raise NotImplementedError('TODO: implement')

def status_report(root: Path, seat: int) -> str:
    """Plain --status text: this seat's claimed files vs git, plus how many other dirty files exist."""
    raise NotImplementedError('TODO: implement')

def ship(root: Path, seat: int, message: str, raw_paths: list[str], dry_run: bool=False, out=...) -> int:
    """
    Commit exactly `raw_paths` through the sanctioned guard flow. Returns a process exit code.

    EDGE CASES: nothing changed -> refuse; STOP present -> refuse; guard step fails -> stop and
    report the step (work stays safe on its task branch; fix and re-run the same command).
    """
    raise NotImplementedError('TODO: implement')

def build_parser() -> argparse.ArgumentParser:
    """Define the command line: --seat (required), -m, --status, --dry-run and the exact file paths. Returns the parser."""
    raise NotImplementedError('TODO: implement')

def main(argv: list[str] | None=None, root: Path | None=None) -> int:
    """CLI entry (`root` is injectable for tests). --status prints and exits 0; otherwise a message is required, else exit 2."""
    raise NotImplementedError('TODO: implement')
