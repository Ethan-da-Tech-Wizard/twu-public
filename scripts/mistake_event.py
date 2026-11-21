# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/mistake_event.py - local-only logger for correction / frustration / repeated-ask prompts.

Records one JSON line per flagged prompt to data/mistakes/<host>.jsonl (per-host shard,
append-only, flock). Never stores the full prompt: only a 200-char redacted excerpt plus
a sha256. Hook mode (`hook`) reads hook JSON on stdin, never writes stdout, always exits 0.

  mistake_event.py hook [--cli claude]
  mistake_event.py scan-transcripts --file PATH [--cli claude] [--write]
  mistake_event.py calibrate --file PATH   (counts only, no text, no writes)
  mistake_event.py summary [--json]
Near-duplicate detection is default-off (set MISTAKE_EVENT_NEARDUP=1).
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import platform
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

def _now():
    raise NotImplementedError('TODO: implement')

def normalize(text):
    raise NotImplementedError('TODO: implement')

def redact(text, limit=...):
    raise NotImplementedError('TODO: implement')

def simhash(text):
    """64-bit SimHash of the prompt's words. Non-invertible: only the sketch is kept."""
    raise NotImplementedError('TODO: implement')

def clean_text(text):
    raise NotImplementedError('TODO: implement')

def is_human(prompt):
    raise NotImplementedError('TODO: implement')

def neardup_enabled():
    raise NotImplementedError('TODO: implement')

def analyze(prompt):
    """Return (pattern_ids, weight, strong) from regex only, on cleaned text."""
    raise NotImplementedError('TODO: implement')

def is_flagged(ids, weight, strong):
    """Strong pattern, or weight>=2 from something other than just punctuation+again."""
    raise NotImplementedError('TODO: implement')

def _locked_append(path, line):
    raise NotImplementedError('TODO: implement')

def _state_path(dir, host):
    raise NotImplementedError('TODO: implement')

def _load_state(dir, host):
    raise NotImplementedError('TODO: implement')

def _save_state(dir, host, state):
    raise NotImplementedError('TODO: implement')

def check_duplicate(state, session_id, prompt):
    """Update state in place; True if prompt is a near-duplicate of one of the last 5.

    State holds only a 64-bit SimHash (hex) per recent prompt, never words or word hashes.
    """
    raise NotImplementedError('TODO: implement')

def build_record(prompt, cli, session_id, ids, weight, ts=None):
    raise NotImplementedError('TODO: implement')

def record_prompt(prompt, dir, cli=..., session_id=..., host=None, state=None, write=True):
    """Analyze one prompt; append a record if flagged. Returns the record or None."""
    raise NotImplementedError('TODO: implement')

def hook_run(raw, dir, cli=..., host=None):
    """Process hook stdin text. Never raises."""
    raise NotImplementedError('TODO: implement')

def _user_texts(obj):
    raise NotImplementedError('TODO: implement')

def scan_transcripts(path, dir, cli=..., write=False, host=None):
    """Retro-scan a transcript JSONL. Returns {'prompts': n, 'flagged': n, 'patterns': {...}}."""
    raise NotImplementedError('TODO: implement')

def summary(dir):
    raise NotImplementedError('TODO: implement')

def main(argv=None, stdin=None, dir=None):
    raise NotImplementedError('TODO: implement')
