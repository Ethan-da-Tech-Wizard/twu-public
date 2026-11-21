# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Emit a portable fleet-needs.v1 coverage receipt for THIS host, then self-validate it.

The Fleet Needs Contract requires every host to state what it measured, what is unknown, and how
fresh that statement is, so no planner or Fleet Console treats a missing measurement as health.
`fleet_needs.py` validates that schema but nothing produced a conforming receipt; this is the missing
producer. It derives coverage only from receipts this host already writes (pair diagnostics, the needs
report, and the metadata-only app-behavior sample). A category is "measured" only when a fresh source
backs it, "stale" when the source exists but is old, and "unknown" when this host has no evidence for
it (for example TWOS boot/journey/performance, which are the Linux node's lane). It writes nothing but
its own receipt and never reads app content, credentials, or vault state.

  python3 scripts/fleet_needs_emit.py            # write data/health/fleet_needs.<host>.json, validate, print
  python3 scripts/fleet_needs_emit.py --stdout    # also print the receipt JSON
"""
from __future__ import annotations
import argparse
from datetime import datetime, timedelta, timezone
import json
import platform
import subprocess
import sys
from pathlib import Path
import fleet_needs

def host_slug():
    raise NotImplementedError('TODO: implement')

def parse_ts(value):
    raise NotImplementedError('TODO: implement')

def mac_backup_status():
    """Measure this Mac's OS backup coverage via tmutil (no sudo). None off macOS or if unavailable."""
    raise NotImplementedError('TODO: implement')

def read_json(path):
    raise NotImplementedError('TODO: implement')

def last_jsonl(path):
    raise NotImplementedError('TODO: implement')

def fresh_state(ts, now, window=...):
    """measured if the source timestamp is recent, stale if old, error if absent/unparseable."""
    raise NotImplementedError('TODO: implement')

def build(now=None):
    raise NotImplementedError('TODO: implement')

def write_receipt(now=None):
    """Build, validate, and persist this host's receipt. Returns (receipt, errors, path)."""
    raise NotImplementedError('TODO: implement')

def receipt_risks(receipt):
    """Actionable risks hidden inside measured metrics, so coverage is not just a completeness count.

    A category can be 'measured' and still carry bad news (no backup, CPU throttling, low disk). This
    pulls those out so the rollup shows what actually needs attention, not only where data is missing.
    """
    raise NotImplementedError('TODO: implement')

def summarize(now=None):
    """Read every host's emitted receipt into one concise coverage rollup.

    This is the reader that makes the receipts worth writing: it tells Ethan/Enki where the fleet
    has fresh measured coverage, where it is flying blind (unknown/stale), and which measured metrics
    carry an actual risk. On-demand only; it starts no daemon.
    """
    raise NotImplementedError('TODO: implement')

def summary_cmd(now=None, refresh=True):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
