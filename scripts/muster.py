# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Muster (was: cannon volley): fire every Squire's (was: cannon's) real tests at the lowest priority and keep score. No model, no tokens, no network.

Each volley runs the registry check plus the cannon test files, one at a time, under `nice 19` with a timeout, and
appends one line per shot (HIT/MISS, seconds) to data/cannon_volley/ledger-<machine>.jsonl. One ledger file per machine
means Syncthing never has to merge two writers. Compares to the previous volley and writes data/cannon_volley/latest.md
listing regressions (HIT -> MISS) and slowdowns (> 1.5x and > 2 s) as repair tasks. Skips itself when the machine is hot,
the STOP latch exists, or another volley is running.

  muster.py            run one muster
  muster.py --report   print the latest report
"""
import argparse, fcntl, json, os, platform, subprocess, sys, time
from pathlib import Path

def warm():
    """True only if the machine is hot for real: the coolest of 3 readings 1 s apart is over the line.
    (A single reading is noisy: any one-second burst spikes this laptop's CPU into the 90s.)"""
    raise NotImplementedError('TODO: implement')

def safe_skip(message):
    """Record a deliberate safety/serialization hold without masking real failures."""
    raise NotImplementedError('TODO: implement')

def fire(cmd, timeout=120):
    raise NotImplementedError('TODO: implement')

def last_volley(path):
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
