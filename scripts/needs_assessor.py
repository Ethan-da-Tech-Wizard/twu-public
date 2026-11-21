# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""needs_assessor.py — one-shot, zero-model, per-machine "what does this computer need?" report.

  python3 scripts/needs_assessor.py            # measure, write data/health/needs.<mac|linux>.{json,md}, exit
  python3 scripts/needs_assessor.py --checks   # also run check_all.py --no-build once and fold its result in (slower)
  python3 scripts/needs_assessor.py --resources --pid 123 --sample-seconds 2 --json  # selected read-only Linux CPU/RSS sample

Runs from a timer (launchd / systemd), does its work in about two seconds and exits, so nothing stays resident.
Reads only: disk, the footprint ledger, saved local hardware profile, sync-conflict files, scheduled-job failures, scripts that have no test, and
(optionally) the repo check. It also projects the existing machine-local immutable job queue so an approved plan stays
visible until validator evidence marks it passed, and the explicit research-outcome register so open research cannot be mistaken for a result. Ranks the needs by severity and records each as a tool request for a seat (or a model, on
demand) to pick up. Per-machine output, so Syncthing never sees two writers; the other machine's file is read-only here.
Stdlib only. The default mode writes its reports; --resources only reads /proc and prints, with no saved report,
model, service action, process arguments, environment, working directories, or application content.
"""
import argparse
import glob
import json
import math
import os
from pathlib import Path
import re
import shutil
import socket
import subprocess
import sys
import time
from datetime import datetime, timezone

def sample_seconds(value):
    raise NotImplementedError('TODO: implement')

def process_id(value):
    raise NotImplementedError('TODO: implement')

def read_metric(path, limit=65536):
    raise NotImplementedError('TODO: implement')

def parse_process_stat(text, pid):
    """Read only kernel accounting fields; comm can contain spaces and parentheses."""
    raise NotImplementedError('TODO: implement')

def process_snapshot(proc_root=...):
    raise NotImplementedError('TODO: implement')

def process_deltas(before, after, ticks_per_second, page_bytes):
    raise NotImplementedError('TODO: implement')

def system_resources(proc_root=...):
    raise NotImplementedError('TODO: implement')

def pressure_deltas(before, after):
    """System PSI totals over each file's read-start interval, not the process scan or avg10 window."""
    raise NotImplementedError('TODO: implement')

def resource_report(seconds=2, proc_root=..., pid=None):
    raise NotImplementedError('TODO: implement')

def resource_text(report):
    raise NotImplementedError('TODO: implement')

def untested_scripts(root):
    """Return scripts with no direct or explicitly grouped test reference.

    Some suites intentionally cover several tools (for example,
    ``test_universal_db_and_pdf_cannon.py`` covers
    ``accomplishments_ledger.py``).  A filename-only comparison treats those
    as gaps and creates duplicate work.  This remains a conservative coverage
    *hint*, not proof that a referenced test exercises every branch.
    """
    raise NotImplementedError('TODO: implement')

def conflicts(root):
    raise NotImplementedError('TODO: implement')

def failing_jobs():
    raise NotImplementedError('TODO: implement')

def check_all_summary(root):
    raise NotImplementedError('TODO: implement')

def hardware_needs(profile):
    """Turn a bounded, saved hardware profile into review requests, never changes.

    A one-shot temperature is a signal for a controlled baseline, not permission
    to alter firmware, governors, fan curves, or kernel policy.
    """
    raise NotImplementedError('TODO: implement')

def _profile_time(value):
    raise NotImplementedError('TODO: implement')

def needs_report_state(report, *, hostname, side, now=None, max_age_seconds=...):
    """Classify a synced needs report before another service relays its requests.

    A report belongs only to its named host and platform side. Missing, future,
    malformed, or old reports are diagnostic evidence, never current work input.
    """
    raise NotImplementedError('TODO: implement')

def load_local_hardware_profile(root, *, platform=None, hostname=None, now=None):
    """Return ``(profile, state)`` only for fresh evidence from this machine.

    Profiles sync between machines.  A foreign or old snapshot must never create
    a thermal, storage, or tuning suggestion on the receiving host.
    """
    raise NotImplementedError('TODO: implement')

def hardware_profile_need(state):
    raise NotImplementedError('TODO: implement')

def thermal_baseline_state(root=..., *, hostname=None, now=None):
    raise NotImplementedError('TODO: implement')

def thermal_baseline_need(summary):
    raise NotImplementedError('TODO: implement')

def plan_flag_summary(jobs):
    """Summarize immutable approved plans without exposing their specs or evidence."""
    raise NotImplementedError('TODO: implement')

def local_plan_flags(root=...):
    """Read, never create or recover, the existing per-host plan queue."""
    raise NotImplementedError('TODO: implement')

def plan_flag_needs(summary):
    raise NotImplementedError('TODO: implement')

def research_outcome_state(root=...):
    raise NotImplementedError('TODO: implement')

def research_outcome_needs(summary):
    raise NotImplementedError('TODO: implement')

def measurement_action_state(root=...):
    raise NotImplementedError('TODO: implement')

def measurement_action_needs(summary):
    raise NotImplementedError('TODO: implement')

def app_behavior_state(root=..., *, hostname=None, now=None):
    """Read a small host-local observation tail; malformed history never creates a tuning request."""
    raise NotImplementedError('TODO: implement')

def _number(value):
    raise NotImplementedError('TODO: implement')

def _family_rows(records):
    raise NotImplementedError('TODO: implement')

def app_behavior_needs(summary):
    raise NotImplementedError('TODO: implement')

def assess(f):
    """Pure function: facts -> ranked needs. Each need: severity, id, why, tool_request."""
    raise NotImplementedError('TODO: implement')

def atomic_write(path, content):
    """Publish a complete receipt in one replace, never a reader-visible partial file."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
