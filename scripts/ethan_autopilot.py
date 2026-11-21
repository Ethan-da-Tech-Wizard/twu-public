# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Autopilot: keep the local 7B improving between human sessions by running the task bank against the live CLI.

  ethan_autopilot.py status | once | run --loop [--interval 900] [--max-ticks N]

One tick = at most ONE task, run through scripts/ethan_conductor.py (ladder mode, small budget) when ALL hold:
  config enabled; no STOP / MODEL_STANDBY latch; not inside quiet hours; today's compute budget not spent; no human CLI
  session (ethan_tree_keeper.active_cli_session or a /proc scan for 'ethan chat' / 'ETHAN CLI' / bin/gemini); data/health/
  GPU_WINDOW free (the experiment queue and other seats hold the same file) and the GPU idle; no thermal start_blocker.
It then takes the GPU lease (GPU_WINDOW = JSON {owner, pid, expiry, ...}; created O_EXCL, released only if still ours; a lease whose
pid is dead or whose expiry passed is stale and may be replaced). The conductor does its own git checkpoint/ff-merge, so the
autopilot never starts while a human session is alive. Nothing here sends a request to the model server, trains or promotes.

Priority: (1) tasks never attempted; (2) tasks with the highest recent failure rate (at most max_attempts_per_task_per_day a day);
(3) eval-split tasks round-robin (least recently run first) for a stable benchmark.
Task dirs: data/self_improve/tasks and data/self_improve/tasks_mined (if present).
Each run is appended to data/self_improve/autopilot.jsonl: task, config label (bridge flags + serving profile read from /proc),
state, full_pass, partial_credit, minutes, classifications. A crash is recorded (state CRASH) and the next tick carries on.
Settings: data/self_improve/autopilot.json (created with defaults on first `status`).
Exit codes: 0 normal (ran or skipped), 2 STOP latch.
"""
from __future__ import annotations
import argparse
import json
import os
import re
import signal
import subprocess
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
import stop_latch

def read_jsonl(path):
    raise NotImplementedError('TODO: implement')

def append_jsonl(path, rec):
    raise NotImplementedError('TODO: implement')

def load_config(path=None):
    raise NotImplementedError('TODO: implement')

def in_quiet_hours(cfg, now):
    raise NotImplementedError('TODO: implement')

def pid_alive(pid):
    raise NotImplementedError('TODO: implement')

def lease_state(path, now_ts=None, alive=...):
    """('free'|'ours'|'held'|'stale', text). Unreadable or non-JSON content is 'held' (fail closed)."""
    raise NotImplementedError('TODO: implement')

def acquire_lease(path, minutes, purpose, now_ts=None, alive=...):
    """Create the lease atomically. Returns (True, '') or (False, reason)."""
    raise NotImplementedError('TODO: implement')

def release_lease(path):
    """Remove the lease only when it is still ours."""
    raise NotImplementedError('TODO: implement')

def list_tasks(dirs=...):
    """[{id, dir, split}] from the task dirs; the first dir wins on a duplicate id."""
    raise NotImplementedError('TODO: implement')

def pick_next(tasks, recs, today, cfg):
    """(task, reason) or (None, why). Pure: depends only on its arguments."""
    raise NotImplementedError('TODO: implement')

class Env:
    """Real-world access; tests replace it with a fake."""

    def now(self):
        raise NotImplementedError('TODO: implement')

    def stopped(self):
        raise NotImplementedError('TODO: implement')

    def standby(self):
        raise NotImplementedError('TODO: implement')

    def blocker(self):
        raise NotImplementedError('TODO: implement')

    def human_session(self):
        """Description of a live human CLI session, else None."""
        raise NotImplementedError('TODO: implement')

    def gpu_idle(self):
        raise NotImplementedError('TODO: implement')

    def config_label(self):
        raise NotImplementedError('TODO: implement')

    def headless_supported(self):
        raise NotImplementedError('TODO: implement')

    def run_task(self, task, minutes, headless):
        """Run the conductor as a child process. Returns {rc, timed_out}. Only the child WE start is ever signalled."""
        raise NotImplementedError('TODO: implement')

def _util_low():
    raise NotImplementedError('TODO: implement')

def _listener_pid(port):
    raise NotImplementedError('TODO: implement')

def config_label():
    """Bridge flags (ETHAN_BRIDGE_* env of the 18195 listener) + serving profile (llama-server argv of the 18190 listener)."""
    raise NotImplementedError('TODO: implement')

def conductor_result(task_id, started_ts, log_size_before, log_dir=None):
    """(summary or None, classifications) for a run that began at started_ts."""
    raise NotImplementedError('TODO: implement')

def minutes_today(recs, today):
    raise NotImplementedError('TODO: implement')

def tick(env=None, cfg=None, log=None, lease=None, tasks_fn=None, state_path=None, log_dir=None):
    """Returns {'status': 'ran'|'skipped'|'stop', 'reason': ..., 'record': ..., 'backoff': bool}."""
    raise NotImplementedError('TODO: implement')

def status(env=None, cfg=None, log=None, lease=None, tasks_fn=None):
    raise NotImplementedError('TODO: implement')

def run_loop(env=None, cfg=None, max_ticks=None, sleep=..., **kw):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
