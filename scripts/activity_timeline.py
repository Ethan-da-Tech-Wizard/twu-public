# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""activity_timeline: know what was done, day by day, and never let a progress tracker go quietly stale.

  activity_timeline.py check            repair what can be repaired, then alarm on every progress source that is still stale (exit 1 if any)
  activity_timeline.py timeline [--since YYYY-MM-DD]   rebuild data/ACTIVITY_TIMELINE.md (default: last 45 days) and print the blind-spot days
  activity_timeline.py status           what is stale right now (from the last check)

Why: on 2026-11-07 the conversation scraper turned out to have been dark since 2026-10-22, so `direction.md` ("where the work went") was 16 days old and no
tool had said so. This keeps one table of every progress/journey source with the longest age it may have, repairs the ones a deterministic command can refresh
(session_archive.py, --direction), and writes a day-by-day timeline from FOUR independent sources (archived conversations, CHANGELOG, the Magi message bus, git),
so a day that shows work in one source but no conversation capture is named as a BLIND SPOT (another machine, an autonomous job, or a scraper gap).
Stdlib only, no model, no network. Reads titles/counts only, never prompt text. Receipt: data/netguard/PROGRESSFRESH.<host>.json.
"""
from __future__ import annotations
import collections, gzip, json, os, re, socket, subprocess, sys, time
from pathlib import Path
import command_ledger as cl

def _day(ts):
    raise NotImplementedError('TODO: implement')

def arch_rel(root):
    """This host's archive folder, relative to root (OWNER host: data/session_archive; any other host: data/session_archive/hosts/<host>)."""
    raise NotImplementedError('TODO: implement')

def conversations(root):
    """{day: {tool: user_prompt_count}} from every host's scrubbed archive (a session file is counted once)."""
    raise NotImplementedError('TODO: implement')

def changelog_days(root):
    raise NotImplementedError('TODO: implement')

def bus_days(root):
    raise NotImplementedError('TODO: implement')

def git_days(root):
    raise NotImplementedError('TODO: implement')

def direction_rows(root):
    """{day: (turns, code_edited, tests_pass)} parsed from direction.md."""
    raise NotImplementedError('TODO: implement')

def timeline(root=..., since=None, now=None):
    raise NotImplementedError('TODO: implement')

def devices(root=..., now=None):
    """[(host, archive_dir, session_files, newest_mtime)] for every device the fleet knows (one data/health/ALARMS.<host>.json each, seen in the last 30 days)."""
    raise NotImplementedError('TODO: implement')

def device_problems(root=..., now=None):
    raise NotImplementedError('TODO: implement')

def freshness(root=..., now=None):
    """{key: problem text} for every progress source that is missing or older than its limit."""
    raise NotImplementedError('TODO: implement')

def run_repair(key, root=...):
    raise NotImplementedError('TODO: implement')

def check(root=..., d=None, repair=..., now=None):
    raise NotImplementedError('TODO: implement')

def alarm_problems(now=None, d=None):
    raise NotImplementedError('TODO: implement')

def main(a=None):
    raise NotImplementedError('TODO: implement')
