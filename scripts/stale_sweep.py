# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""stale_sweep: nothing goes stale unseen. Repairs what is safely mechanical, and raises an alarm for what needs a human decision.

  stale_sweep.py check     repair, re-verify, write receipt; exit 1 if anything still needs a human
  stale_sweep.py status    print what is still open from the last receipt

Mechanical repairs (deterministic, no model, no network, no spending):
  * an Enki tool whose script changed after its smoke receipt  -> `enki_tools.py smoke NAME` (proves it still loads, on the new hash)
  * data/command_registry.json out of step with its generator  -> `command_registry.py --build`
  * data/tool_registry.json out of step with scripts/            -> `tool_registry.py` (rebuild; the scavenger's only error-level finding)
  * Syncthing conflict copies of data/health telemetry logs      -> MOVED (never deleted) to archive/sync_conflicts/ with a sha256 manifest
                                                                   (only data/health; a conflicted document anywhere else stays a person's decision)
  * the conversation scraper + command ledger                    -> `command_ledger.py scan` (refreshes session_archive, rebuilds data/command_ledger.json
                                                                   and data/COMMAND_LEDGER.md; its own problems are passed through as alarms)
  * every progress/journey tracker (direction.md, archive, ledger)  -> `activity_timeline.py check` (refreshes what a command can refresh; alarms on
                                                                   the rest) and writes data/ACTIVITY_TIMELINE.md, the day-by-day record with blind-spot days
  * the knowledge index behind `ethan_know.py` out of date      -> `ethan_know.py build` (incremental), then `verify` (no secrets indexed)
NOT repaired automatically (a judgment, so it stays an alarm until a person reviews it): a tool whose computed safety class changed,
a missing/removed tool, any failing smoke, any failed rebuild. Receipt: data/netguard/STALESWEEP.<host>.json (names only).
Scheduled by MAGI_0/com.twu.stale-sweep.plist (Mac) or twu-stale-sweep.timer (Linux); a silent sweeper is itself an alarm.
"""
from __future__ import annotations
import hashlib, json, os, re, shutil, socket, subprocess, sys, time
from pathlib import Path

def _run(args, timeout=600):
    raise NotImplementedError('TODO: implement')

def enki_problems(run=...):
    """Problem strings from `enki_tools.py check`, or None if the check itself could not run."""
    raise NotImplementedError('TODO: implement')

def registry_ok(run=...):
    raise NotImplementedError('TODO: implement')

def _sha(path):
    raise NotImplementedError('TODO: implement')

def archive_health_conflicts(root=..., now=None):
    """Move data/health/*.sync-conflict-* into archive/sync_conflicts/, record sha256 + how many lines the base file lacks. Returns (moved, errors)."""
    raise NotImplementedError('TODO: implement')

def tool_registry_ok(run=...):
    raise NotImplementedError('TODO: implement')

def index_current(run=...):
    raise NotImplementedError('TODO: implement')

def sweep(run=..., d=None, now=None, root=None):
    raise NotImplementedError('TODO: implement')

def alarm_problems(now=None, d=None):
    raise NotImplementedError('TODO: implement')

def main(a=None):
    raise NotImplementedError('TODO: implement')
