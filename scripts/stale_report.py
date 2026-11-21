# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/stale_report.py - one read-only answer to "is anything outdated right now?".

Aggregates the existing freshness signals (no model, no network, no writes, no service changes):
instruction fingerprint, knowledge index, Graphify navigation, tool registry, scavenger scan,
freshness-sentinel receipt, check_all result, workspace inventory.  Each item is PASS or STALE with
the exact fix command.  Exit 0 = nothing stale, 1 = something stale.

  python3 scripts/stale_report.py          # human list
  python3 scripts/stale_report.py --json   # machine-readable
  python3 scripts/stale_report.py --heal   # run the cheap, zero-model, local refreshes, then re-report

--heal only runs SAFE_HEALS (knowledge index and tool registry rebuilds, both local and capped) and writes
data/health/stale_report.json, which ethan_alarm reads. Everything else (check_all runs from its own daily
timer, scavenger errors need a person) is reported, never run.  twu-stale-heal.timer runs --heal every 2h.
"""
from __future__ import annotations
import argparse
import json
import socket
import subprocess
import sys
import time
from pathlib import Path

def lynis_item(report=..., root=..., now=None):
    """Independent root-run Lynis audit: report must exist, be <=9 days old, and be ingested."""
    raise NotImplementedError('TODO: implement')

def lynis_needs_ingest(report=..., root=...):
    raise NotImplementedError('TODO: implement')

def heal(items, run=None, root=...):
    """Run the safe refresh for each stale item that has one; return [(item, returncode)]."""
    raise NotImplementedError('TODO: implement')

def write_receipt(items, healed, root=..., now=None):
    raise NotImplementedError('TODO: implement')

def _run(cmd, timeout=120):
    raise NotImplementedError('TODO: implement')

def age_item(label, rel, max_h, fix, root=..., now=None):
    raise NotImplementedError('TODO: implement')

def collect(run=..., root=..., now=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
