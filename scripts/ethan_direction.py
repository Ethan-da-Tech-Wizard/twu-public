# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Local direction board; no model or network calls.

  ethan_direction.py --refresh       project bounded saved summaries and the current brief (also the default)
  ethan_direction.py --quick         print the saved board, labeled as not refreshed; no writes
  ethan_direction.py --live          redraw the bounded projection every 20 s (Ctrl+C to stop)
  ethan_direction.py --full-refresh  explicitly requested maintenance: harvest, analyze, verify, then rebuild all details

Only full maintenance reads session archives/journals, walks the workspace and updates daily history.
STOP blocks every mode and is checked between full-maintenance stages.
"""
import argparse, glob, json, os, re, subprocess, sys, time
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

class Stopped(RuntimeError):
    pass

def check_stop():
    raise NotImplementedError('TODO: implement')

def saved_text(path, limit=..., tail=False):
    """Read a fixed byte budget; timestamps describe saved evidence, not current verification."""
    raise NotImplementedError('TODO: implement')

def saved_json(path, limit=...):
    raise NotImplementedError('TODO: implement')

def decoded_direction(limit=5, max_chars=280):
    """Ethan's newest own words from the local transcript mirror, with their safe typo-decoded reading.

    Harness-authored rows mislabeled HUMAN_INTERACTIVE are filtered by shape.
    Exact edits and review-only predictions are shown beside the original.
    Unavailable mirrors or decoder yield an honest note.
    """
    raise NotImplementedError('TODO: implement')

def build():
    """Refresh evidence freshness without doing the maintenance it describes."""
    raise NotImplementedError('TODO: implement')

def iso_ago(hours):
    raise NotImplementedError('TODO: implement')

def edited_files(turn):
    """Code files a turn changed, for any CLI: Codex patches and the file_path of Claude/Gemini edit tools."""
    raise NotImplementedError('TODO: implement')

def tagged_turns():
    raise NotImplementedError('TODO: implement')

def activity(turns, since_iso):
    raise NotImplementedError('TODO: implement')

def magi_pulse(now=None):
    """Per Magi seat: messages in the last 24 h, newest message, and the newest few room messages overall."""
    raise NotImplementedError('TODO: implement')

def gaps(archive_index, turns):
    """Plain-language list of what is missing or stale, from files that already exist."""
    raise NotImplementedError('TODO: implement')

def suggestions(stall, evo, gap_list):
    raise NotImplementedError('TODO: implement')

def sync_health(root=None, now=None):
    """What would break or mislead across machines: real sync-conflict files (Syncthing's own .stversions history and archive/
    are not conflicts), empty .db files, and how old each Magi seat's newest message is (a stale seat = a stale copy of its records)."""
    raise NotImplementedError('TODO: implement')

def build_full():
    raise NotImplementedError('TODO: implement')

def refresh_sources():
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
