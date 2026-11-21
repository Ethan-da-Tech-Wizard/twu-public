# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Ethan assumptions: the follow-up work Ethan would assume without being asked.

Given a task context (files changed, task kind, services, hosts, ...) this computes, deterministically,
the checklist a careful Ethan-aligned agent should finish, and DETECTS from repo/system state whether each
item is done.  No model calls, no network, read-only.  Every item cites its source rule (AGENTS.md rule or a
memory file), has a trigger over the context, and a detector that is a pure function of a state snapshot.

  python3 scripts/ethan_assumptions.py --check [paths...] [--json] [--kind code|capability|incident|doc]
         [--services unit,...] [--hosts h,...] [--security] [--message-file F]
  python3 scripts/ethan_assumptions.py --emit-pairs data/autoimprove/20261101/assumptions/pairs.jsonl

Statuses: DONE, MISSING (action needed), UNKNOWN (state not observable here).  Exit 1 if anything MISSING.
Design: data/autoimprove/20261101/assumptions/README.md.
"""
from __future__ import annotations
import argparse
import glob
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

def is_test(p):
    raise NotImplementedError('TODO: implement')

def is_script(p):
    raise NotImplementedError('TODO: implement')

def test_for(p):
    raise NotImplementedError('TODO: implement')

def noise(p):
    raise NotImplementedError('TODO: implement')

def rule(rid, source, why):
    raise NotImplementedError('TODO: implement')

def changed(ctx, pred=...):
    raise NotImplementedError('TODO: implement')

def live(ctx):
    raise NotImplementedError('TODO: implement')

def trig_test_exists(ctx):
    raise NotImplementedError('TODO: implement')

def det_test_exists(snap, p):
    raise NotImplementedError('TODO: implement')

def det_test_run(snap, p):
    raise NotImplementedError('TODO: implement')

def det_branch(snap, _):
    raise NotImplementedError('TODO: implement')

def trig_new_cap(ctx):
    raise NotImplementedError('TODO: implement')

def det_wiring(snap, p):
    raise NotImplementedError('TODO: implement')

def det_moving(snap, p):
    raise NotImplementedError('TODO: implement')

def trig_changelog(ctx):
    raise NotImplementedError('TODO: implement')

def det_changelog(snap, _):
    raise NotImplementedError('TODO: implement')

def trig_archive(ctx):
    raise NotImplementedError('TODO: implement')

def det_archive(snap, p):
    raise NotImplementedError('TODO: implement')

def trig_code_added(ctx):
    raise NotImplementedError('TODO: implement')

def det_abs(snap, p):
    raise NotImplementedError('TODO: implement')

def det_pkill(snap, p):
    raise NotImplementedError('TODO: implement')

def trig_check_all(ctx):
    raise NotImplementedError('TODO: implement')

def det_check_all(snap, _):
    raise NotImplementedError('TODO: implement')

def trig_units(ctx):
    raise NotImplementedError('TODO: implement')

def det_unit(snap, u):
    raise NotImplementedError('TODO: implement')

def det_hold(snap, u):
    raise NotImplementedError('TODO: implement')

def trig_security(ctx):
    raise NotImplementedError('TODO: implement')

def det_security(snap, _):
    raise NotImplementedError('TODO: implement')

def det_sync(snap, _):
    raise NotImplementedError('TODO: implement')

def det_short(snap, _):
    raise NotImplementedError('TODO: implement')

def trig_issues(ctx):
    raise NotImplementedError('TODO: implement')

def det_fixnow(snap, issue):
    raise NotImplementedError('TODO: implement')

def det_dep(snap, dep):
    raise NotImplementedError('TODO: implement')

def det_dl(snap, dl):
    raise NotImplementedError('TODO: implement')

def det_host(snap, h):
    raise NotImplementedError('TODO: implement')

def det_magi(snap, tid):
    raise NotImplementedError('TODO: implement')

def compute_checklist(ctx):
    raise NotImplementedError('TODO: implement')

def detect(ctx, snap):
    raise NotImplementedError('TODO: implement')

def _git(args, root, timeout=60):
    raise NotImplementedError('TODO: implement')

def parse_status(out):
    raise NotImplementedError('TODO: implement')

def systemd_state(units):
    raise NotImplementedError('TODO: implement')

def inflight(port=18190):
    raise NotImplementedError('TODO: implement')

def build_snapshot(ctx, root=...):
    raise NotImplementedError('TODO: implement')

def context_from_tree(root=..., paths=..., kind=None, **extra):
    raise NotImplementedError('TODO: implement')

def _f(*items):
    raise NotImplementedError('TODO: implement')

def emit_pairs(path):
    raise NotImplementedError('TODO: implement')

def render(res):
    raise NotImplementedError('TODO: implement')

def _hook_on():
    raise NotImplementedError('TODO: implement')

def _write_last(data, path=None):
    raise NotImplementedError('TODO: implement')

def changed_since(since, root=...):
    """Changed (non-noise) existing paths whose mtime is newer than ``since``: the work done this turn."""
    raise NotImplementedError('TODO: implement')

def after_agent(now=None, root=..., last_path=None, runner=None):
    """Cheap per-turn check. Returns the record written. Never raises, never blocks longer than HOOK_TIMEOUT."""
    raise NotImplementedError('TODO: implement')

def session_start_text(now=None, last_path=None):
    """One untrusted-data line for the NEXT session about MISSING items, or ''."""
    raise NotImplementedError('TODO: implement')

def context_notice(stream, client, workspace):
    """Read just the chat binding from a native hook packet and return fixed UI text after a trim."""
    raise NotImplementedError('TODO: implement')

def hook_main(args):
    """`--gemini-hook AfterAgent|SessionStart`. Always prints a JSON object and exits 0.

    AfterAgent sends its optional notice through the native UI systemMessage channel.
    SessionStart retains the existing assumptions reminder in additionalContext.
    """
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
