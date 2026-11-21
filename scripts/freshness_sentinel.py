# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/freshness_sentinel.py — re-run scheduled jobs whose evidence went stale.

A systemd timer with Persistent=true proves a job was TRIGGERED, not that it
FINISHED: if the box powers off mid-run (Ethan's "on for two minutes" case),
systemd records the trigger and will not retry until the next scheduled slot,
silently losing up to a day. This sentinel checks each job's actual output
artifact instead of its schedule: evidence older than the job's maximum age
and no run in progress means the job is started again, now.

Only jobs that deterministically produce an artifact on every run are enforced;
jobs that may legitimately skip (backups gated on a plugged drive, the tuner
gated on no open chat) are left to their own schedules.
"""
from __future__ import annotations
import json
import os
import platform
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

def evidence_ok(path: Path, spec) -> bool:
    raise NotImplementedError('TODO: implement')

def artifact_age_hours(path: Path, now: Optional[float]=None) -> Optional[float]:
    """Age of the artifact (newest file inside, for a directory). None = missing."""
    raise NotImplementedError('TODO: implement')

def unit_active(unit: str, run=...) -> bool:
    raise NotImplementedError('TODO: implement')

def start_unit(unit: str, run=...) -> bool:
    raise NotImplementedError('TODO: implement')

def _journal(kind: str, summary: str, refs) -> None:
    raise NotImplementedError('TODO: implement')

def _notify(title: str, body: str, run=...) -> None:
    raise NotImplementedError('TODO: implement')

def _load_state() -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def _save_state(state: Dict[str, Any]) -> None:
    raise NotImplementedError('TODO: implement')

def certify_problems(path: Optional[Path]=None) -> tuple:
    """(stamp, [plain-words problems]) from the newest COMPLETE nightly certification, else (None, [])."""
    raise NotImplementedError('TODO: implement')

def raise_certify_flag(state: Dict[str, Any], path: Optional[Path]=None) -> List[str]:
    """Broken things must raise flags (Ethan, 2026-10-25): journal ONE incident per certification receipt so the
    activity beacon puts it on screen. Returns the problems found (empty when healthy or already flagged)."""
    raise NotImplementedError('TODO: implement')

def _watcher_timer_state(name: str, home: Path, run) -> str:
    """'missing' (no unit file here), 'enabled', 'disabled' (file present, systemd says it is off) or 'unknown' (could not ask)."""
    raise NotImplementedError('TODO: implement')

def _watcher_timer_installed(name: str, home: Path, run) -> bool:
    raise NotImplementedError('TODO: implement')

def _role_units(repo: Path) -> List[str]:
    """The units this machine's ROLE allows (data/fleet_roles.json). The GitHub leak watch keeps full copies of every private repo, so an outside machine never gets it."""
    raise NotImplementedError('TODO: implement')

def ensure_outside_profile(system: Optional[str]=None, repo: Optional[Path]=None, host: Optional[str]=None, stop_path: Optional[Path]=None) -> Optional[Dict[str, Any]]:
    """On a machine whose role is OUTSIDE (data/fleet_roles.json), write the managed ignore block into its own .stignore so Syncthing stops bringing the sensitive
    folders onto it. Additive only: it never deletes a file (removing what is already there is the explicit `fleet_roles.py purge-outside`). None = nothing to do or report."""
    raise NotImplementedError('TODO: implement')

def ensure_watchers_installed(state: Dict[str, Any], run=..., system: Optional[str]=None, have_systemctl: Optional[bool]=None, home: Optional[Path]=None, repo: Optional[Path]=None, stop_path: Optional[Path]=None) -> Optional[Dict[str, Any]]:
    """Make this Linux box enable the leak-watch and stale-sweep timers by itself, ONCE per run.
    Returns None when there is nothing to report (not Linux/systemd, STOP set, already installed)."""
    raise NotImplementedError('TODO: implement')

def check_once(now: Optional[float]=None, run=...) -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def single_instance() -> Optional[int]:
    """Exclusive non-blocking lock so two runs (the timer plus a manual run, say) can never both read the state
    before either saves it and report the same problem twice (seen 2026-10-25: a duplicate flag). None = busy."""
    raise NotImplementedError('TODO: implement')

def main() -> int:
    raise NotImplementedError('TODO: implement')
