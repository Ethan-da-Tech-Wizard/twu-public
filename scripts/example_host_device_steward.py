# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Emit the example_host example_host's Enki device-steward receipt (schema enki.device-steward.v1).

Producer only, same receipt shape as scripts/enki_device_steward.py (the Mac producer). It reads this
host's existing mbp-watch / mbp-guard heartbeats and snapshot plus /proc/meminfo, statvfs of the home
directory and /sys/class/thermal, and writes only its own receipt, atomically. No model, network,
service, sudo or install.

Privacy: every check note is a fixed, bounded phrase chosen from a table. No path, user name, process
name, package name, UUID, MAC or IP is ever emitted. A missing, unreadable or old input yields
unknown or stale, never measured.

  python3 scripts/example_host_device_steward.py                  # write data/example_host/enki/stewards/example_host.json
  python3 scripts/example_host_device_steward.py --stdout          # also print the receipt
  python3 scripts/example_host_device_steward.py --out DIR --host H   # test without touching the real folder
"""
from __future__ import annotations
import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

def _json(path):
    raise NotImplementedError('TODO: implement')

def _num(value):
    raise NotImplementedError('TODO: implement')

def heartbeat_age(path, now_ts):
    """(age_seconds, interval) from a heartbeat file, or (None, None) if missing or malformed."""
    raise NotImplementedError('TODO: implement')

def read_snapshot(snapshot_file=None, state_file=None, command=None):
    """Return (health_dict name->bool, ts, source) from the watcher snapshot; falls back to state.json.

    Only booleans are used; check names are never emitted.
    """
    raise NotImplementedError('TODO: implement')

def read_update_age_bucket(events_file, now_ts):
    """Bucket the age of the newest package or kernel change event: week, month, older, none; None if unreadable."""
    raise NotImplementedError('TODO: implement')

def read_meminfo_gb(path=...):
    raise NotImplementedError('TODO: implement')

def read_disk_free_gb(path):
    raise NotImplementedError('TODO: implement')

def read_cpu_temp_c(thermal_dir=...):
    """Package temperature in C: prefer the x86 package zone, else the hottest non-battery zone."""
    raise NotImplementedError('TODO: implement')

def _check(cid, state, note):
    raise NotImplementedError('TODO: implement')

def collect(home=None, now=None, snapshot_file=None, snapshot_cmd=None, thermal_dir=..., meminfo=..., disk_free_fn=None):
    """Gather bounded facts only (numbers and booleans), never strings from the inputs."""
    raise NotImplementedError('TODO: implement')

def _fresh(age, limit):
    raise NotImplementedError('TODO: implement')

def build(facts, host=..., now=None):
    raise NotImplementedError('TODO: implement')

def write_receipt(receipt, out_dir):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
