# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Wiring gate: new work is wired into the system automatically, and locked-in capabilities stay working.

Ethan (2026-10-27): "whenever you implement something it automatically gets wired into the system and
it should never miss anything", and the Ron-derived capabilities must be "locked in". This gate is
deterministic (no model, service, network or Git mutation) and runs from check_all.py.

Automatic discovery, every run (untested and unreferenced tools are NOT repeated here: scripts/scavenger.py
owns S2 untested-tool and S11 floating-tool findings with its own shrink-only baseline, and
scripts/enki_tools.py owns catalog/smoke wiring; this gate covers what they do not):
  1. daemons_without_stop every long-running worker (managed inventory, a --daemon/--continuous/--watch/
                          --loop/--forever flag, or a *_daemon/_sentinel/_watcher name) honours STOP
                          through stop_latch.enforce() or an executable STOP check
  2. undocumented_stores  every SQLite store under data/ (outside backups) is named in MOVING_PARTS.md
  3. tools_without_test   every runnable scripts/*.py has scripts/test_<tool>.py (or a test file naming it)
  4. tools_without_changelog every runnable scripts/*.py is named in CHANGELOG.md
  5. units_undocumented   every systemd unit/timer/path (~/.config/systemd/user plus repo-tracked copies) is
                          named in MOVING_PARTS.md or data/wiring_manifest.json
  6. tests_not_swept      no test file hides from ethan_certify's scripts/test_*.py sweep (wrong name, tests/
                          subdir, or no test cases)
Known debt from before this gate lives in data/wiring_baseline.json. The baseline only shrinks:
`--prune` drops entries that are fixed; anything new fails until it is wired or explicitly accepted
with `--accept KIND:NAME --reason "..."` (the reason is recorded).

Locked-in capabilities (data/wiring_manifest.json): each listed file must exist, its regression
suites must pass, and its declared check commands must exit 0. Managed inventory STOP failures and
locked-in failures can never be baselined.

  python3 scripts/wiring_check.py            # report
  python3 scripts/wiring_check.py --check    # exit 1 on any new gap or locked-in failure (check_all)
  python3 scripts/wiring_check.py --json
"""
from __future__ import annotations
import argparse
import ast
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

def _parse(path: Path):
    raise NotImplementedError('TODO: implement')

def is_daemon_like(path: Path) -> bool:
    raise NotImplementedError('TODO: implement')

def daemons_without_stop(scripts: Path=...) -> list[str]:
    raise NotImplementedError('TODO: implement')

def managed_inventory_failures() -> list[str]:
    raise NotImplementedError('TODO: implement')

def undocumented_stores(repo: Path=...) -> list[str]:
    raise NotImplementedError('TODO: implement')

def _tool_stems(scripts: Path) -> list[str]:
    """Runnable tools: scripts/*.py with a __main__ entry, excluding tests."""
    raise NotImplementedError('TODO: implement')

def _word_in(text: str, word: str) -> bool:
    raise NotImplementedError('TODO: implement')

def tools_without_test(scripts: Path=...) -> list[str]:
    """A tool needs scripts/test_<tool>.py, or at least one test file that names it."""
    raise NotImplementedError('TODO: implement')

def tools_without_changelog(scripts: Path=..., repo: Path=...) -> list[str]:
    raise NotImplementedError('TODO: implement')

def unit_names(repo: Path=..., home: Path | None=None) -> list[str]:
    """Systemd unit files installed for the user plus repo-tracked copies (drop-in dirs ignored)."""
    raise NotImplementedError('TODO: implement')

def units_undocumented(repo: Path=..., home: Path | None=None) -> list[str]:
    """Every unit must be named in MOVING_PARTS.md or data/wiring_manifest.json (by full name or by base name)."""
    raise NotImplementedError('TODO: implement')

def tests_not_swept(scripts: Path=...) -> list[str]:
    """ethan_certify sweeps scripts/test_*.py. Flag test files that glob would miss, and swept files with no test."""
    raise NotImplementedError('TODO: implement')

def lessons_format(path: Path) -> list[str]:
    raise NotImplementedError('TODO: implement')

def load_json(path: Path, default):
    raise NotImplementedError('TODO: implement')

def available_gib() -> float:
    """MemAvailable in GiB, or infinity when unreadable (never block on a missing /proc)."""
    raise NotImplementedError('TODO: implement')

def journal(line: str) -> None:
    """Append and fsync BEFORE a step starts, so a crash or kill leaves the culprit as the last START line."""
    raise NotImplementedError('TODO: implement')

def example_host_wanted() -> bool:
    raise NotImplementedError('TODO: implement')

def _unshare_prefix() -> list[str]:
    raise NotImplementedError('TODO: implement')

def example_host_available() -> bool:
    """Probe once: unshare must exist AND really create a pid namespace (child sees itself as PID 1)."""
    raise NotImplementedError('TODO: implement')

def example_host_argv(argv: list[str], home: str=..., env: dict | None=None) -> list[str]:
    """Wrap argv in a user+pid+net+mount namespace with a scrubbed env, or return it unchanged when unavailable.
    Inside: the child is PID 1 of its own pid namespace (real pids, kill(-1), the user systemd bus, the Wayland
    socket and the network are unreachable). cwd is inherited, so scripts/x.py paths still resolve."""
    raise NotImplementedError('TODO: implement')

def run_step(label: str, argv: list[str], env: dict, timeout: int=..., cwd=..., self_example_hosted: bool=False) -> tuple[int, str]:
    """One child at a time, in its own session and (when available) its own namespaces. Returns (rc, output)."""
    raise NotImplementedError('TODO: implement')

def fleet_context(repo: Path) -> dict:
    """Resolve the actual machine through fleet_roles; environment aliases cannot exempt checks."""
    raise NotImplementedError('TODO: implement')

def locked_in(manifest: dict, run_suites: bool=True) -> list[dict]:
    """Strictly sequential: every suite and command is its own process, run to completion before the next starts."""
    raise NotImplementedError('TODO: implement')

def report(run_suites: bool=True) -> dict:
    raise NotImplementedError('TODO: implement')

def save_baseline(data: dict) -> None:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
