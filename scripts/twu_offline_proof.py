# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Offline PROOF (Python 3.9, stdlib only; no network, no model, no daemon).

  twu_offline_proof.py run [--json]   run the listed read-only commands inside a network-deny
                                      example_host, write data/dashboard/offline_proof.<host>.json
  twu_offline_proof.py show           print the last written file as a table

Never runs a command unexample_hosted.  Before trusting the example_host a CANARY runs inside it
(loopback connect to a parent-owned listener, DNS lookup, UDP send to TEST-NET); every probe must
FAIL there.  Statuses: NOT-AVAILABLE, UNPROVEN, FAILED-LEAKY, VERIFIED-ISOLATED (plus TOOLS-FAILED
when isolation is proven but a command failed or tried the network).  NETWORK-ATTEMPT means the
tool tried a network call and the example_host denied it (text match on its output: a heuristic).

Per command (or per file default) `network_mode`: `none` (default, deny all) or `loopback_only` (127.0.0.1 reachable,
everything else denied).  loopback_only has its own canary (loopback connect must SUCCEED; DNS, TEST-NET TCP and
TEST-NET UDP must FAIL); if it does not pass, no command in that mode runs.  In that mode NETWORK-ATTEMPT means an
attempt at a non-loopback address.
"""
from __future__ import annotations
import json
import os
import platform
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import time
from pathlib import Path

def real_runner(argv, cwd, timeout):
    raise NotImplementedError('TODO: implement')

def detect_mechanism(runner=..., system=None, which=..., mode=...):
    """Return (name, argv_prefix) or (None, reason).  A mechanism must run `true` successfully.
    mode `none` denies all network; `loopback_only` leaves 127.0.0.1 reachable (Linux: needs unshare + ip)."""
    raise NotImplementedError('TODO: implement')

def run_canary(prefix, runner=...):
    """Run the canary inside the example_host.  Returns dict with status in
    VERIFIED-ISOLATED | FAILED-LEAKY | UNPROVEN and per-probe results."""
    raise NotImplementedError('TODO: implement')

def run_loopback_canary(prefix, runner=...):
    """Canary for loopback_only.  VERIFIED-ISOLATED here means: the parent-owned loopback listener WAS reached, and
    DNS (example.invalid), TCP to 192.0.2.1:80 and UDP to 192.0.2.1 all failed.  The TEST-NET probes must fail with
    PermissionError (a example_host denial); a timeout is not proof of denial and gives UNPROVEN.
    Loopback not reachable -> UNPROVEN; any non-loopback probe succeeded -> FAILED-LEAKY."""
    raise NotImplementedError('TODO: implement')

def run_canary_for(mode, prefix, runner=...):
    raise NotImplementedError('TODO: implement')

def validate_entry(e):
    """Return list of error strings (empty if valid)."""
    raise NotImplementedError('TODO: implement')

def load_commands(list_dir=...):
    """Return (commands, errors).  Invalid entries are dropped and reported."""
    raise NotImplementedError('TODO: implement')

def run_command(entry, prefix, runner=...):
    raise NotImplementedError('TODO: implement')

def overall_status(isolation, rows, list_errors=...):
    raise NotImplementedError('TODO: implement')

def build_report(runner=..., list_dir=..., system=None, which=...):
    raise NotImplementedError('TODO: implement')

def write_atomic(path, data):
    raise NotImplementedError('TODO: implement')

def format_table(rep):
    raise NotImplementedError('TODO: implement')

def out_path():
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
