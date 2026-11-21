# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Failure drill: prove the alarm, self-heal and stale systems really respond, against the real systemd user session.

Every scenario breaks something on purpose, runs our own tool, then asks an INDEPENDENT oracle (systemd itself,
the file system, `find`) whether the repair happened. A tool's own report is never the verdict.

  python3 scripts/failure_drill.py --list
  python3 scripts/failure_drill.py [--only N ...] [--json]      exit 0 only if every selected scenario passes

Safety: the only things ever created are `systemd-run --user` transient units named `twu-drill-*`; every start/stop/
reset-failed is refused (and the scenario fails) for any other unit; real units get read-only status calls only. The
self-heal state file and the STOP latch are redirected to a temp directory, so data/health/selfheal_state.json and the
real STOP file are never touched. No models, no kill-by-name. A present real STOP latch makes the drill refuse to run.
Cleanup always stops and reset-faileds every twu-drill-* unit and verifies `list-units 'twu-drill-*'` is empty.
"""
from __future__ import annotations
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from types import SimpleNamespace

def parse_timespan(text):
    """systemd timespan like '9h 48min 49.699204s' -> seconds, or None."""
    raise NotImplementedError('TODO: implement')

class Refused(RuntimeError):
    """The drill tried something outside its example_host."""

def real_runner(argv, timeout=30):
    raise NotImplementedError('TODO: implement')

def guard(argv):
    """Raise Refused unless argv is one of the few commands the drill is allowed to run."""
    raise NotImplementedError('TODO: implement')

class Drill:

    def __init__(self, runner=..., sleep=..., tmp=None, transient_dir=None, wait=12.0):
        raise NotImplementedError('TODO: implement')

    def run(self, argv, timeout=30):
        raise NotImplementedError('TODO: implement')

    def ctl(self, *args, timeout=30):
        raise NotImplementedError('TODO: implement')

    def state(self, verb, unit):
        raise NotImplementedError('TODO: implement')

    def poll(self, pred):
        raise NotImplementedError('TODO: implement')

    def make_failed(self, unit, timer=False):
        raise NotImplementedError('TODO: implement')

    def heal_run(self, synthetic_timers=...):
        """subprocess.run lookalike for ethan_selfheal: real systemctl, but it can only see (and so only touch) twu-drill-*."""
        raise NotImplementedError('TODO: implement')

    def avoid_real_selfheal(self, need=30.0):
        """The real ethan-alarm.service runs self-heal every 2 minutes and would also heal our twu-drill-* failures.
        Read-only: wait until that timer is not about to fire (and the service is idle) so the fixtures stay ours."""
        raise NotImplementedError('TODO: implement')

    def cleanup(self):
        raise NotImplementedError('TODO: implement')

def s1_selfheal_clears_failed(d):
    raise NotImplementedError('TODO: implement')

def s2_stopped_timer_restarted(d):
    raise NotImplementedError('TODO: implement')

def s3_crash_loop_breaker(d):
    raise NotImplementedError('TODO: implement')

def s4_stop_latch_blocks_heal(d):
    raise NotImplementedError('TODO: implement')

def s5_stale_detected(d, rel=..., limit=3.0):
    raise NotImplementedError('TODO: implement')

def _snapshot(paths):
    raise NotImplementedError('TODO: implement')

def build_mode_watch_paths():
    raise NotImplementedError('TODO: implement')

def s6_build_mode_dry_run_writes_nothing(d, watch=None):
    raise NotImplementedError('TODO: implement')

def run_drill(only=None, drill=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
