# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""One rolling typo-flow batch: verify the decoder first, then refresh capture, corpus and a measured receipt.

Ethan's standing request (2026-10-25): the typo system runs in batches across machines, every batch is
verified EARLY, failures are fixed and amended honestly, and the decoder keeps improving from real usage.

Deterministic and fail-closed: no model, no network. Stage order per batch:
  1. STOP latch check (business/example_host/comms/STOP aborts silently with a SKIPPED receipt).
  2. Early verification: the three decoder test suites run first; any red suite writes a FAIL receipt
     and stops the batch - a broken decoder must never shape flow or mine new promotions.
  3. Bounded capture refresh: cli_harvester --scrape (the existing tool; prompts AND responses).
  4. Corpus rebuild: ethan_typo_corpus.py (mined promotion candidates grow with real usage).
  5. Measurement: decode the newest human-interactive prompts from this box's mirror and record the
     suggestion rates. Rates measure coverage, not interpretation accuracy.
Receipts: data/tool_trials/typo_flow/<shorthost>/<utc>.json plus LATEST.json (one writer per host).

  typo_flow_batch.py            run one batch
  typo_flow_batch.py --dry-run  run stages 1-2 only (verification without refresh)
"""
import argparse, json, math, os, platform, re, signal, subprocess, sys, tempfile, threading, time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import ethan_thermal_guard as thermal_guard
import stop_latch

class BatchStopped(RuntimeError):
    pass

class BatchDeadline(RuntimeError):
    pass

class BatchThermalAbort(RuntimeError):
    pass

@dataclass
class CommandResult:
    pass

def thermal_readings():
    raise NotImplementedError('TODO: implement')

def start_blocker():
    raise NotImplementedError('TODO: implement')

def start_blocker_for(gpu, cpu, ram):
    raise NotImplementedError('TODO: implement')

def thermal_action(gpu, cpu, ram, *, stopped):
    raise NotImplementedError('TODO: implement')

def thermal_checkpoint(*, deadline=None, on_event=None, stage=...):
    """Keep parent-process scans/measurement inside the same thermal and STOP policy."""
    raise NotImplementedError('TODO: implement')

def _tail(stream, limit=3000):
    raise NotImplementedError('TODO: implement')

def _signal_group(proc, sig):
    raise NotImplementedError('TODO: implement')

def _group_exists(pgid):
    raise NotImplementedError('TODO: implement')

def _stop_group(proc, *, paused=False):
    raise NotImplementedError('TODO: implement')

def run_monitored(cmd, *, timeout, deadline, cwd=...):
    """Run a child in an owned process group under shared thermal/STOP limits."""
    raise NotImplementedError('TODO: implement')

def short_host():
    raise NotImplementedError('TODO: implement')

def run_suite(name, timeout=300, *, deadline=None, runner=None):
    raise NotImplementedError('TODO: implement')

def human_prompts(box, limit=..., *, deadline=None, on_thermal_event=None):
    raise NotImplementedError('TODO: implement')

def measure(rows, *, deadline=None, on_thermal_event=None):
    raise NotImplementedError('TODO: implement')

def save(receipt):
    raise NotImplementedError('TODO: implement')

def batch(dry_run=False, runner=None, *, deadline=None, save_progress=True):
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
