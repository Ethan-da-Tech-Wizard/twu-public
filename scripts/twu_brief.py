# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""twu_brief: the one short page every AI session reads FIRST, so it knows what is going on instead of guessing.

  twu_brief.py print          print the brief (fresh)
  twu_brief.py write          write it to data/health/BRIEF.<host>.md (the catch-up runner does this every 15 minutes)
  twu_brief.py hook           what a Claude Code SessionStart hook runs: prints the brief (reuses the file if under 10 minutes old)
  twu_brief.py install-hook   add that SessionStart hook to ~/.claude/settings.json (backup first, keeps everything else, safe to repeat)
  twu_brief.py uninstall-hook remove only our hook

Why: the full rules are ~34,000 words (AGENTS.md + MOVING_PARTS.md); no model reads that reliably, docs go stale, and a session that is not told what is happening will state guesses as facts
(2026-11-08: 'WireGuard is not installed', reports addressed to a Magi who never joined, a Linux command given for a Mac, five documented background jobs that were never installed).
This page is under ~450 words and says: which machine you are on and what it is for, which connections are verified, reported or unknown, which files are claimed, what is broken, which facts were CHECKED just now, which docs are known to be wrong,
and a few standing rules. Every section degrades to 'unavailable: <why>' instead of failing. Deterministic: no model, no network. Receives nothing from the user; reads only workspace files and local commands.
"""
from __future__ import annotations
import calendar, glob, json, os, re, shutil, socket, subprocess, sys, tempfile, time
from pathlib import Path

def brief_path(root=..., host=None):
    """Per-machine generated file in data/health/ (NOT in MAGI_0: the instruction rules allow exactly one brief there, MASTER_HANDOFF.md)."""
    raise NotImplementedError('TODO: implement')

def _safe(fn, *a, **k):
    raise NotImplementedError('TODO: implement')

def _age(seconds):
    raise NotImplementedError('TODO: implement')

def where_am_i(root, host, now):
    raise NotImplementedError('TODO: implement')

def _machine_line(m, h, root, now):
    raise NotImplementedError('TODO: implement')

def _fmt_fact(name, v):
    raise NotImplementedError('TODO: implement')

def facts(root, host, now):
    raise NotImplementedError('TODO: implement')

def problems(root, host, now):
    raise NotImplementedError('TODO: implement')

def known_wrong_docs(root, host, now):
    raise NotImplementedError('TODO: implement')

def _connection_lines(report):
    """Render the common roster's evidence states without inventing attendance."""
    raise NotImplementedError('TODO: implement')

def people(root, host, now, run=...):
    raise NotImplementedError('TODO: implement')

def changed(root, host, now):
    raise NotImplementedError('TODO: implement')

def build(root=..., host=None, now=None, run=...):
    raise NotImplementedError('TODO: implement')

def write(root=..., host=None, now=None, run=..., path=None):
    raise NotImplementedError('TODO: implement')

def hook_text(root=..., now=None, run=..., path=None):
    """Brief for a SessionStart hook: reuse the file if fresh, else rebuild. Never raises (a broken hook must not block a session)."""
    raise NotImplementedError('TODO: implement')

def _our_hook(command):
    raise NotImplementedError('TODO: implement')

def install_hook(settings=None, root=..., uninstall=False):
    """Add (or remove) our SessionStart hook in the user's Claude Code settings. Backup first; keeps every other setting; refuses a settings file it cannot parse."""
    raise NotImplementedError('TODO: implement')

def main(a=None):
    raise NotImplementedError('TODO: implement')
