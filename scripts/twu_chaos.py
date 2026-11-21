# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""twu_chaos: declarative chaos experiments (Chaos Toolkit experiment format, Apache-2.0) against THROWAWAY targets only.

Each experiment: steady-state hypothesis -> inject fault -> verify recovery -> rollback. Targets are child processes
and temp files this script creates itself. It never touches the model server, Syncthing, systemd units or any
workspace data file; the one real component exercised is ethan_selfheal.load_state / failure_drill-style recovery
logic against a temp copy. Kills only PIDs it started (never by name).

  python3 scripts/twu_chaos.py list
  python3 scripts/twu_chaos.py run [--only NAME ...] [--engine builtin|chaostoolkit] [--no-receipt]
  python3 scripts/twu_chaos.py dump NAME          # print the chaostoolkit-format JSON for an experiment

Engines: builtin (stdlib only, default) interprets the experiment dicts itself. chaostoolkit re-runs the SAME
experiments through chaoslib (venv ~/.local/share/twu-chaos-venv; chaostoolkit 1.21.4 / chaostoolkit-lib 1.45.1,
Apache-2.0) with python providers pointing at this module. Receipt: data/tool_trials/example_host/.
"""
from __future__ import annotations
import argparse
import json
import os
import signal
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

def _alive(pid):
    raise NotImplementedError('TODO: implement')

def _wait(pred, timeout=8.0):
    raise NotImplementedError('TODO: implement')

def _worker_pid():
    raise NotImplementedError('TODO: implement')

def setup():
    raise NotImplementedError('TODO: implement')

def teardown():
    raise NotImplementedError('TODO: implement')

def start_supervisor():
    raise NotImplementedError('TODO: implement')

def worker_alive():
    raise NotImplementedError('TODO: implement')

def kill_worker():
    raise NotImplementedError('TODO: implement')

def worker_restarted():
    raise NotImplementedError('TODO: implement')

def stop_supervisor():
    raise NotImplementedError('TODO: implement')

def write_state():
    raise NotImplementedError('TODO: implement')

def corrupt_state():
    raise NotImplementedError('TODO: implement')

def loader_recovers():
    """Current ethan_selfheal contract (changed before this experiment was written down): a corrupt state file is
    NOT silently reset to an empty shape (that would destroy the evidence and re-arm the retry budget). load_state
    must raise StateReadError, heal() must DEFER instead of acting, and the corrupt file must be left byte-for-byte
    untouched for review. Recovery = the rollback step rewriting a valid file, after which loading works again.
    Before 2026-11-21 this probe demanded the old silent-reset behaviour, so the experiment reported 'failed'
    even though the loader was behaving as designed."""
    raise NotImplementedError('TODO: implement')

def quota_ok():
    raise NotImplementedError('TODO: implement')

def fill_quota():
    raise NotImplementedError('TODO: implement')

def rotate_quota():
    """Recovery under test: bounded-log trim (keep the newest cap bytes), as a log guard would."""
    raise NotImplementedError('TODO: implement')

def within_quota():
    raise NotImplementedError('TODO: implement')

def make_stale_lock():
    raise NotImplementedError('TODO: implement')

def acquire_lock():
    """Lock acquire that must break a lock whose owner pid is dead (and refuse one whose owner is alive)."""
    raise NotImplementedError('TODO: implement')

def lock_clean():
    raise NotImplementedError('TODO: implement')

def release_lock():
    raise NotImplementedError('TODO: implement')

def no_lock_held_by_dead_owner():
    raise NotImplementedError('TODO: implement')

def _py(fn, **kw):
    raise NotImplementedError('TODO: implement')

def _probe(name, fn, tolerance=True):
    raise NotImplementedError('TODO: implement')

def _call(item):
    raise NotImplementedError('TODO: implement')

def _hypothesis(exp):
    raise NotImplementedError('TODO: implement')

def run_builtin(name):
    raise NotImplementedError('TODO: implement')

def run_chaostoolkit(name):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
