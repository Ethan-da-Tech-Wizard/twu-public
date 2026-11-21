# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""
PROGRAM:       fleet_briefing.py
PROGRAMMER:    Magi 10 (claude, example_host), MAGI_TODO 093098ee, at Ethan's request
LAST MODIFIED: 2026-11-20
PURPOSE:       One plain-language page for ETHAN (not for agents): is everything OK, and what do you need to do.

WHAT IT IS
  A read-only composer. It does not check hardware itself. It reads what the fleet's own watchers already wrote
  (alarm files, health snapshots, sync beacons, the stale sweep receipt, deploy logs, MAGI_TODO, owner command cards,
  CHANGELOG) and turns it into six short sections, top screen first:
    1. one verdict per computer (FINE / NEEDS A LOOK / BROKEN / UNKNOWN) with the reason in words and the data age
    2. Needs you      (MAGI_TODO tasks marked [Ethan] and open owner command cards: the one thing to do, and why)
    3. Changed        (CHANGELOG entries and dashboard deploys in the last N hours, one line each, grouped by area)
    4. Broken or at risk (alarms, failing units, what the sweep could not fix; plain meaning and the safe next step)
    5. Magi are working on (claimed MAGI_TODO tasks by seat)
    6. Good news      (things fixed, verified or finished)

RULES IT KEEPS (Ethan's rules for facts)
  * Every claim carries its source file and its age. Missing data stays the word "unknown"; it is never guessed.
  * If a computer's newest data is older than 30 minutes the verdict says so first and is UNKNOWN, never FINE.
  * No secrets: values that look like keys, tokens or passwords are replaced by [hidden].
  * Nothing is cut silently: when a list is shortened it says "and N more" and names the file that has all of them.
  * Read-only: it writes exactly one file, data/health/FLEET_BRIEFING.<this host>.md (a per-computer name, so
    Syncthing never sees two writers), and only when asked to (the default CLI run does; --no-write skips it).

USAGE
  python3 scripts/fleet_briefing.py [--since HOURS] [--json] [--no-write] [--root DIR]
  Import: build(root, now, since_hours) -> dict; render_markdown(b); render_html_snippet(b) -> str (escaped,
  safe to embed in a dashboard page); write_briefing(b, root) -> Path.

CHANGE HISTORY:
  2026-11-20  Magi 10  Created.
"""
from __future__ import annotations
import argparse
import datetime as dt
import html
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import time
from pathlib import Path

def _redact(text):
    """Replace the value after a secret-looking name with [hidden]."""
    raise NotImplementedError('TODO: implement')

def age_words(seconds):
    """Plain age: '45 s', '12 min', '3 h', '2 days'. None -> 'unknown age'."""
    raise NotImplementedError('TODO: implement')

def _read_json(path):
    """Read a JSON file; returns (data, mtime) or (None, None). Never raises."""
    raise NotImplementedError('TODO: implement')

def _last_jsonl(path, tail_bytes=65536):
    """Last parseable JSON object of a (possibly large) .jsonl file, reading only its tail. (obj, mtime) or (None, None)."""
    raise NotImplementedError('TODO: implement')

def _iso_to_ts(text):
    """ISO 8601 (with Z or +hhmm) -> epoch seconds, or None."""
    raise NotImplementedError('TODO: implement')

def _run(argv, root, timeout=60):
    """Run a read-only helper script; returns stdout text or None if it failed. Never raises."""
    raise NotImplementedError('TODO: implement')

def _first_sentence(text, limit=220):
    """First sentence of a text, flattened to one line. If it is longer than the limit it ends with ' ...'."""
    raise NotImplementedError('TODO: implement')

def _alarm_plain(key, text):
    """(meaning, next step) for an alarm key; falls back to the alarm's own text so nothing is invented."""
    raise NotImplementedError('TODO: implement')

def host_facts(root, host, now, local_host):
    """Everything the fleet files say about one computer, each fact with its source and age."""
    raise NotImplementedError('TODO: implement')

def verdict(f):
    """(word, reason in plain words). UNKNOWN beats everything when data is too old: never invent health."""
    raise NotImplementedError('TODO: implement')

def parse_task_lines(text):
    """Parse `magi_todo_board.py list` output into dicts. Lines that do not match are ignored."""
    raise NotImplementedError('TODO: implement')

def needs_you(root, now, run):
    """MAGI_TODO tasks marked [Ethan] plus open owner command cards. Each has the one thing to do and why."""
    raise NotImplementedError('TODO: implement')

def magi_working(root, run):
    """Claimed MAGI_TODO tasks grouped by seat -> {seat: [titles]}; plus a missing note if the board did not answer."""
    raise NotImplementedError('TODO: implement')

def done_recently(root, since_date, run):
    """Tasks finished (done with evidence and review) since a date: titles only."""
    raise NotImplementedError('TODO: implement')

def changelog_since(root, since_date):
    """CHANGELOG entries dated on/after since_date, as [{date, line_no, text}]. Entries are whole lines; see cite."""
    raise NotImplementedError('TODO: implement')

def area_of(text):
    raise NotImplementedError('TODO: implement')

def deploys_since(root, hosts, since_ts):
    """Dashboard installs in the window from data/relay_work/dashboard_deploys.<host>.jsonl."""
    raise NotImplementedError('TODO: implement')

def failing_units(root, local_host, run_cmd=None):
    """User systemd units that are failed on THIS computer (None if systemctl is not available, e.g. on macOS)."""
    raise NotImplementedError('TODO: implement')

def fleet_hosts(root):
    """Computer names from the sync beacons (one file per computer, written by that computer)."""
    raise NotImplementedError('TODO: implement')

def build(root=None, now=None, since_hours=12.0, runner=None, host=None, units=None):
    """Compose the briefing dict. `runner(argv, root)` returns a helper script's stdout or None (injectable for tests)."""
    raise NotImplementedError('TODO: implement')

def _more(total, shown, where):
    raise NotImplementedError('TODO: implement')

def render_markdown(b):
    """Markdown for Ethan. The first screen is: the short answer, one line per computer, then Needs you."""
    raise NotImplementedError('TODO: implement')

def render_html_snippet(b):
    """A small read-only HTML block other pages can embed. Everything is escaped; there is no script and no form."""
    raise NotImplementedError('TODO: implement')

def write_briefing(b, root=None):
    """Write data/health/FLEET_BRIEFING.<host>.md (one writer per file) atomically. Returns the path."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
