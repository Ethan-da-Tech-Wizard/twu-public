# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""
================================================================================
MODULE:        scripts/reboot_ready.py
ROLE:          Read-only "is this Mac safe to reboot / did it come back" checker
AUTHOR:        Ethan (TWU LLC)
================================================================================

PURPOSE:
    Answers two questions on this example_host Air with one PASS/WARN/FAIL line per
    item and the exact fix command for every WARN/FAIL: (1) before a reboot,
    will everything come back and is any work stranded; (2) after login, did
    it actually come back (tunnel, listeners, dashboard, sync).

ARCHITECTURE & SYSTEM ROLE:
    - Upstream callers: Ethan at a terminal; the future `ethan wrap` command
      (exit codes below are its contract).
    - Downstream: only the allowlisted external commands in ALLOWED_RULES,
      funnelled through ONE helper, run_cmd().
    - Design source: data/tool_trials/magitodo_prep/2026-11-19/
      reboot_readiness_mac.md (section 13) and one_command_design.md.

DATA FLOW & LIFECYCLE:
    argv -> STOP latch check -> lock file -> checks (each returns Items)
         -> optional single apply action -> receipt (JSON + text) -> stdout.

MODES:
    --check   (default) read-only before-reboot checks.
    --verify  check mode plus post-login liveness checks.
    --apply   check mode plus ONE reversible user-level action: if the
              twu-mesh tunnel is down, run `scutil --nc start twu-mesh`
              (reverse: `scutil --nc stop twu-mesh`) and re-check.
    --json    machine-readable output on stdout.
    --allow-warn  WARN results do not change the exit code.

EXIT CODES:
    0 all PASS (or WARN with --allow-warn)   1 any FAIL (or WARN without flag)
    2 usage error   3 STOP latch present   4 another run holds the lock

KEY INVARIANTS:
    - Every external command passes the static argv allowlist; anything else
      raises Refused before a process is created.
    - Each command has a timeout (default 10 s); the whole run has a 120 s
      budget; when the budget is spent remaining commands are skipped.
    - Check mode never reaches the apply path; the apply path can only run
      one exact argv.
    - Receipts live under ~/.local/state/twu/reboot_ready/<host>/ (dir 0700,
      files 0600), never in the synced workspace, never with secret values.

SECURITY & BOUNDARIES:
    Secret-bearing files are only stat()ed (mode and name); contents are never
    read or printed. No privilege escalation, no service control, no deletes,
    no git writes, no network except the optional `git ls-remote` per clone.

SYNOPSIS / USAGE:
    python3 scripts/reboot_ready.py              # before a reboot
    python3 scripts/reboot_ready.py --verify     # after login
    python3 scripts/reboot_ready.py --apply      # start twu-mesh if it is down
================================================================================
"""
from __future__ import annotations
import argparse
import fcntl
import hashlib
import json
import os
import re
import socket
import stat
import subprocess
import sys
import time
import plistlib
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, NamedTuple, Optional, Sequence

class Item(NamedTuple):
    """One line of the report: id, PASS/WARN/FAIL, what was seen, how to fix."""

class Result(NamedTuple):
    """Outcome of one external command (rc None means it did not run/finish)."""

class Refused(Exception):
    """Raised when an argv is not on the allowlist (nothing was executed)."""

def _git_root_ok(path: str) -> bool:
    """True when `path` is the workspace or sits under the two clone folders.

    Why: `git -C` on an arbitrary path could read any repository; the named
    roots keep the allowlist narrow.
    """
    raise NotImplementedError('TODO: implement')

def is_allowed(argv: Sequence[str], allow_apply: bool=False) -> bool:
    """Static allowlist: True only for the exact command shapes we permit.

    Why a function of argv (not a regex on a joined string): joining hides
    argument boundaries, which is how injection slips through.
    """
    raise NotImplementedError('TODO: implement')

class Budget:
    """Wall-clock budget shared by every command in one run."""

    def __init__(self, total: float=...):
        raise NotImplementedError('TODO: implement')

    def left(self) -> float:
        raise NotImplementedError('TODO: implement')

def _exec(argv: Sequence[str], timeout: float) -> Result:
    """The one place a process is created (tests replace this function)."""
    raise NotImplementedError('TODO: implement')

def run_cmd(argv: Sequence[str], timeout: float=..., allow_apply: bool=False) -> Result:
    """Run `argv` only if allowlisted, within its timeout and the run budget.

    Raises Refused for anything off-list. Returns skipped=True when the global
    budget is spent so a slow machine degrades to WARNs instead of hanging.
    """
    raise NotImplementedError('TODO: implement')

def state_root() -> str:
    """~/.local/state/twu/reboot_ready (local, not Syncthing-synced)."""
    raise NotImplementedError('TODO: implement')

def hostname() -> str:
    """Short host name used as the per-host receipt folder."""
    raise NotImplementedError('TODO: implement')

def _ensure_private_dir(path: str) -> None:
    """Create `path` (and parents) and force mode 0700 on it."""
    raise NotImplementedError('TODO: implement')

def parse_launchctl_list(text: str) -> Dict[str, Dict[str, str]]:
    """Map label -> {pid, status} from `launchctl list` (pid is '-' if idle)."""
    raise NotImplementedError('TODO: implement')

def parse_lsof_listen(text: str) -> List[Dict[str, object]]:
    """Parse `lsof -nP -iTCP -sTCP:LISTEN` into command/pid/host/port rows."""
    raise NotImplementedError('TODO: implement')

def _listeners() -> Optional[List[Dict[str, object]]]:
    """Current TCP listeners, or None when lsof failed or was skipped."""
    raise NotImplementedError('TODO: implement')

def _is_loopback(host: str) -> bool:
    raise NotImplementedError('TODO: implement')

def _is_wildcard(host: str) -> bool:
    raise NotImplementedError('TODO: implement')

def _skipped(item_id: str, title: str, r: Result) -> Item:
    """Uniform WARN when a command could not run (timeout/budget/missing)."""
    raise NotImplementedError('TODO: implement')

def check_launch_agents() -> List[Item]:
    """List com.twu.* / org.twu.* user agents with RunAtLoad and loaded state.

    Why: user LaunchAgents only start at GUI login; an agent that is not
    loaded now is one that will quietly not be running after the reboot too.
    The on-demand `scan-*` jobs are intentionally idle and exempt.
    """
    raise NotImplementedError('TODO: implement')

def check_filevault() -> Item:
    """FileVault status; informational WARN because nothing starts before login.

    Why: with FileVault on, a reboot waits at the disk password screen, so the
    mesh, sync and fleet access are all down until Ethan logs in.
    """
    raise NotImplementedError('TODO: implement')

def check_mesh_on_demand() -> Item:
    """twu-mesh On-Demand flag; FALSE means it needs a manual connect each login."""
    raise NotImplementedError('TODO: implement')

def check_fleet_access_perms() -> Item:
    """Fleet-access runtime dir must be 0700 and its key files 0600 (names only).

    Why: these hold SSH keys; a group/world-readable mode is a real exposure.
    Only stat() is used, file contents are never opened.
    """
    raise NotImplementedError('TODO: implement')

def check_mobile_hub_secret() -> Item:
    """Is the private mobile-hub secret file present (existence only)?

    Why: without it the hub falls back to a token inside the synced
    apps/mobile_hub/config.json, which is the weaker setup. Handles
    potential example_host or filesystem permission errors gracefully.
    """
    raise NotImplementedError('TODO: implement')

def _clone_dirs() -> List[Path]:
    """Git clones directly under ~/github_fleet and ~/github_fleet_work."""
    raise NotImplementedError('TODO: implement')

def _inspect_clone(path: Path, offline: bool) -> Dict[str, object]:
    """Dirty count and local-HEAD vs remote-main comparison for one clone.

    Why ls-remote and not origin/main: the local tracking ref goes stale
    after a disk-full fetch error and would hide unsent commits.
    """
    raise NotImplementedError('TODO: implement')

def check_clones(offline: bool=False) -> List[Item]:
    """Report clones with dirty files or commits not on the remote main."""
    raise NotImplementedError('TODO: implement')

def check_workspace_tree() -> Item:
    """Count of changed paths in the TWU_LLC working tree (count only, no names)."""
    raise NotImplementedError('TODO: implement')

def check_orphan_listeners() -> Item:
    """Long-running python/node processes outside launchd bound beyond loopback.

    Why: a process started by hand (parent is not launchd) dies at reboot, and
    one bound to a non-loopback address is also reachable from the network.
    """
    raise NotImplementedError('TODO: implement')

def check_disk() -> Item:
    """Free space on /; under 10 GB a sync or git write can fail midway."""
    raise NotImplementedError('TODO: implement')

def check_claims(now: Optional[float]=None) -> Item:
    """Seat claims in data/comms/claims.json that are live or expire soon (read-only)."""
    raise NotImplementedError('TODO: implement')

def check_conflicts(limit_s: float=20.0) -> Item:
    """Count Syncthing *sync-conflict* files under the workspace (informational)."""
    raise NotImplementedError('TODO: implement')

def check_mesh_up() -> Item:
    """twu-mesh tunnel connected and example_host answering one ping."""
    raise NotImplementedError('TODO: implement')

def _http_code(port: int) -> Optional[str]:
    raise NotImplementedError('TODO: implement')

def check_http_endpoints() -> List[Item]:
    """Dashboard answers on 8777; hub answers 401 (auth required) on 8780."""
    raise NotImplementedError('TODO: implement')

def check_listeners() -> List[Item]:
    """Fleet-access and phone-peer listeners on the mesh IP; no stray wildcard binds."""
    raise NotImplementedError('TODO: implement')

def check_syncthing() -> Item:
    """Syncthing has a peer connection and its log shows no recent errors.

    Why not the REST API: it needs the API key, and this tool never reads
    secrets. A peer socket on 22000 plus a clean log tail is the secret-free
    proxy for "connected and idle"; the real folder state is on :8384.
    """
    raise NotImplementedError('TODO: implement')

def check_steam() -> Item:
    """Steam app installed (it is a login item that should reopen)."""
    raise NotImplementedError('TODO: implement')

def collect(verify: bool, offline: bool) -> List[Item]:
    """Run all checks for the chosen mode and flatten the results."""
    raise NotImplementedError('TODO: implement')

def apply_mesh_start() -> Dict[str, object]:
    """If twu-mesh is down, run `scutil --nc start twu-mesh` once and re-check.

    Why this one: it is user-level, idempotent, and reversible with
    `scutil --nc stop twu-mesh`. Nothing else is ever applied.
    """
    raise NotImplementedError('TODO: implement')

def summarize(items: Sequence[Item]) -> Dict[str, int]:
    raise NotImplementedError('TODO: implement')

def exit_code_for(items: Sequence[Item], allow_warn: bool) -> int:
    """1 on any FAIL; WARN counts as failure unless --allow-warn; else 0."""
    raise NotImplementedError('TODO: implement')

def format_text(mode: str, items: Sequence[Item], actions: Sequence[dict]) -> str:
    """Human summary: alarms (FAIL) first, then WARN, then PASS; fix on its own line."""
    raise NotImplementedError('TODO: implement')

def write_receipt(doc: dict, text: str) -> Dict[str, str]:
    """Write <UTC>.json and <UTC>.txt (0600) in the 0700 per-host state dir."""
    raise NotImplementedError('TODO: implement')

def acquire_lock():
    """Take the single-instance lock; return the open file or None if held.

    flock is released by the OS if the process dies, so no stale lock files.
    """
    raise NotImplementedError('TODO: implement')

def build_parser() -> argparse.ArgumentParser:
    raise NotImplementedError('TODO: implement')

def main(argv: Optional[Sequence[str]]=None) -> int:
    """Entry point; returns the exit code (see module header)."""
    raise NotImplementedError('TODO: implement')
