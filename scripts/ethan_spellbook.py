# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Spellbook: ledger of improvement 'spells', screened TOGETHER, then confirmed once on the real CLI.

Ethan's rule (corrected 2026-11-02): fast and together, not one by one. Stage 1 SCREEN: many spells at once in a small
designed experiment on cheap proxies (scripts/ethan_doe.py: on/off flags -> design rows -> main effect per spell); losers are
dropped early. Stage 2 CONFIRM: the winners combined, real CLI, one shot (safety gate stays). Stage 3 LIVE.
  add | status | next | evidence | gate | stage | set | page | design-input | screen-result | confirm-record
Ledger: data/autoimprove/spellbook/LEDGER.json
"""
import argparse
import json
import os
import sys
import tempfile
import time
from pathlib import Path
import ethan_safety as safety

def halted():
    """(rc, msg) when the global HALT latch is present, else None. Every ledger mutation checks this first."""
    raise NotImplementedError('TODO: implement')

def evidence_path(path, repo=...):
    raise NotImplementedError('TODO: implement')

def parse_paired(path, repo=...):
    """Read baseline, candidate, n from the evidence file itself. Accepts {"baseline","candidate","n"} at top level or under
    "paired_acceptance"; baseline/candidate are pass counts or rates on the same scale. Returns (b, c, n) or None."""
    raise NotImplementedError('TODO: implement')

def now():
    raise NotImplementedError('TODO: implement')

def load(path=None):
    raise NotImplementedError('TODO: implement')

def save(d, path=None):
    raise NotImplementedError('TODO: implement')

def find(d, sid):
    raise NotImplementedError('TODO: implement')

def mk(sid, category, change, flag, revert, status=..., stage=1, evidence=None, passed=..., note=..., prio=5):
    raise NotImplementedError('TODO: implement')

def add(d, **k):
    raise NotImplementedError('TODO: implement')

def set_gate(d, sid, gate, path, ok=True, baseline=None, candidate=None, n=None):
    """Record a gate. Numbers are NEVER taken from the caller (baseline/candidate/n are ignored): paired_acceptance is parsed
    from the evidence file, and the file's sha256 is pinned so a later edit fails the gate."""
    raise NotImplementedError('TODO: implement')

def check(d, s, repo=..., stage=None):
    """Return list of problems (empty = stage gates pass). Re-verifies the pinned checkers and every evidence file hash."""
    raise NotImplementedError('TODO: implement')

def gate(d, sid, advance=False, repo=...):
    raise NotImplementedError('TODO: implement')

def set_stage(d, sid, stage):
    raise NotImplementedError('TODO: implement')

def set_status(d, sid, status, note=None):
    raise NotImplementedError('TODO: implement')

def screen_pool(d):
    raise NotImplementedError('TODO: implement')

def screened(d):
    """Winners waiting for the single combined real-CLI confirmation."""
    raise NotImplementedError('TODO: implement')

def next_spell(d):
    raise NotImplementedError('TODO: implement')

def counts(d):
    raise NotImplementedError('TODO: implement')

def summary_lines(d=None):
    raise NotImplementedError('TODO: implement')

def status_lines(d):
    raise NotImplementedError('TODO: implement')

def design_input(d):
    """Hook OUT to ethan_doe.py: spells waiting to be screened, each with its on/off flag."""
    raise NotImplementedError('TODO: implement')

def screen_result(d, doc):
    raise NotImplementedError('TODO: implement')

def confirm_record(d, path, ok=True):
    """One combined real-CLI run covers every spell now at confirm: record the shared evidence file and gates.
    baseline/candidate/n are read from that file, not passed in."""
    raise NotImplementedError('TODO: implement')

def page(d):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
