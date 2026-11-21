# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""catchup_runner: every scheduled job that was missed while the Mac was off or asleep runs when you come back, and you can see what ran.

  catchup_runner.py run            run whatever is due now (the LaunchAgent does this at login and every 15 minutes); exit 1 if any job is failing/stuck
  catchup_runner.py report         one table: every job, how often, last success, what is due, what was missed
  catchup_runner.py run --dry-run  say what WOULD run, run nothing

Why: launchd skips a timer that fires while the Mac sleeps and never runs a timer while it is off, and on 2026-11-08 it turned out the nightly jobs the docs describe
(contact-tracker rebuild "at 12:01 AM", grants to-do, tracker, 15-minute deadline alerts) were not scheduled on this Mac at all. This runner is the one scheduler + catch-up:
it reads data/scheduled_jobs.json (plain data, edit it to add a job) and, for this machine, runs each enabled job that is due.
  kind "run"      : run a command. cadence "daily" (once per calendar day, after the given time) or "every" N seconds. A job missed N times runs ONCE (not N times).
  kind "launchd" : an existing LaunchAgent whose evidence file is overdue is started with `launchctl kickstart` (it keeps its own settings).
Safety: nothing runs while the STOP latch is set; each command has a timeout and runs at low priority; no overlapping runs (lock file); a job that fails 3 times in a row is an alarm
(`catchup:failing:<id>`), never a silent skip; unreadable state means "never ran" (runs again), never "fine". Deterministic: no model, no network of its own. Receipt:
data/netguard/CATCHUP.<host>.json. State: data/netguard/catchup_state.<host>.json.
"""
from __future__ import annotations
import json, os, platform, socket, subprocess, sys, time
from pathlib import Path

def load_manifest(path=...):
    raise NotImplementedError('TODO: implement')

def _state_path(d):
    raise NotImplementedError('TODO: implement')

def load_state(d):
    raise NotImplementedError('TODO: implement')

def save_state(d, st):
    raise NotImplementedError('TODO: implement')

def local_day(ts):
    raise NotImplementedError('TODO: implement')

def minutes_into_day(ts):
    raise NotImplementedError('TODO: implement')

def is_due(job, js, now):
    """(due, why). js = this job's saved state."""
    raise NotImplementedError('TODO: implement')

def missed(job, js, now):
    """How many scheduled runs were skipped while away (information only; the job still runs once)."""
    raise NotImplementedError('TODO: implement')

def _expand(s):
    raise NotImplementedError('TODO: implement')

def evidence_age(job, root, now):
    raise NotImplementedError('TODO: implement')

def boot_age(now=None):
    """Seconds since the Mac booted (None if it cannot be read)."""
    raise NotImplementedError('TODO: implement')

def process_running(pattern):
    raise NotImplementedError('TODO: implement')

def run_job(job, root, run=..., now=None):
    """Run one 'run' job. Returns (ok, detail). ok_codes lists the exit codes that mean 'it ran' (check_all exits 1 when it FINDS problems; that is not a crash)."""
    raise NotImplementedError('TODO: implement')

def kickstart(label, run=...):
    raise NotImplementedError('TODO: implement')

def stop_set(stop_path=None):
    raise NotImplementedError('TODO: implement')

def acquire(d):
    raise NotImplementedError('TODO: implement')

def run_due(root=..., d=None, jobs=None, now=None, run=..., system=None, dry=False, stop_path=None, kick=None, uptime=None, is_running=None):
    raise NotImplementedError('TODO: implement')

def report(root=..., d=None, jobs=None, now=None):
    raise NotImplementedError('TODO: implement')

def alarm_problems(now=None, d=None):
    raise NotImplementedError('TODO: implement')

def main(a=None):
    raise NotImplementedError('TODO: implement')
