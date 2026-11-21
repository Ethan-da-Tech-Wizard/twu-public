# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""self_improve.py — one light round of "measure, rank, log". Runs and exits; nothing stays resident.

  python3 scripts/self_improve.py            # one round (skips itself if busy, hot, on battery, or already running)
  python3 scripts/self_improve.py --force    # ignore the busy/battery guards

Each round: take cheap measurements, compare with the last round, write one line to data/improvements.jsonl,
and put anything that needs Ethan into data/health/decisions.json (once per finding). It changes no records and
deletes nothing. The only file it rewrites is the TODAY page. Budget: 20 seconds, then it stops.
"""
import argparse
import glob
import json
import os
import subprocess
import sys
import time

def run(cmd, timeout=5):
    raise NotImplementedError('TODO: implement')

def busy_reason():
    """Return why we should not run now, or '' if fine."""
    raise NotImplementedError('TODO: implement')

def conflicts():
    raise NotImplementedError('TODO: implement')

def failing_jobs():
    raise NotImplementedError('TODO: implement')

def free_gb():
    raise NotImplementedError('TODO: implement')

def waste_gb():
    """Reclaimable space the footprint tool already knows how to find (report only; nothing is deleted here)."""
    raise NotImplementedError('TODO: implement')

def dsce_latency_ms():
    raise NotImplementedError('TODO: implement')

def dsce_selfheal_status():
    raise NotImplementedError('TODO: implement')

def measure():
    raise NotImplementedError('TODO: implement')

def last_round():
    raise NotImplementedError('TODO: implement')

def findings(m, prev):
    raise NotImplementedError('TODO: implement')

def add_decisions(items):
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
