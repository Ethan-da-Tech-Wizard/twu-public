# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""One-page status board for the Ethan ecosystem -> data/ops_board.md (reads existing logs only; no model, no network).

Pulls the latest health snapshot, thermal-guard activity, cannon volley score and repair tasks, tuner result, and which
background timers are active, so there is one place to see where things stand and what to work on next.
"""
import platform
import json, subprocess, sys, time
from pathlib import Path
from health_snapshot_store import latest_local_snapshot, normalize_host, snapshot_path
from host_paths import resolve as _hp_resolve

def last_json(path, n=1):
    raise NotImplementedError('TODO: implement')

def load_tasks(path=None, repo=None):
    """Read historical, unverified board claims unchanged; artifact existence is not completion evidence."""
    raise NotImplementedError('TODO: implement')

def task_section(items, seats=...):
    """Render saved claims, never current assignments or attendance inferred from seats."""
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')

def refresh_guide():
    """Keep the plain-words System Guide (SYSTEM_GUIDE.html) and its live status fresh on this existing schedule."""
    raise NotImplementedError('TODO: implement')
