# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""`ethan proof`: shows the things that run in the background as real output, so nothing has to be taken on trust.

  0. RESULTS              the newest CHANGELOG entries with the proof each one gives, plus the independent re-check
  1. CONVERSATION LOGGER  per CLI: the newest real prompt and reply saved, and the independent verifier's verdict
  2. LABELS               the sample of labelled prompts with a second, independent check; says how many labels look wrong
  3. LEARNED AFK PROMPT   the exact note the AFK loop would append to its next prompt, right now
  4. TRAINING             the last training-loop result, if any
Read-only. No model, no network, stdlib only. The AFK note re-reads the Codex sessions (about 3 s); the rest reads small files.
"""
import platform
import json, re, sys
from datetime import datetime, timezone
from pathlib import Path

def parse_review(text):
    """review_queue.md -> [{id, where, origin, outcome, prompt, reply}]"""
    raise NotImplementedError('TODO: implement')

def second_opinion(item):
    """An independent check of one rule label, using only what the sample shows. Returns a reason it looks wrong, or ''."""
    raise NotImplementedError('TODO: implement')

def _scan_archive(root):
    """Per CLI: your prompts saved, newest session time, and the last thing you typed with the start of the reply."""
    raise NotImplementedError('TODO: implement')

def _one_line(text, n=90):
    raise NotImplementedError('TODO: implement')

def logger_section():
    raise NotImplementedError('TODO: implement')

def changelog_entries(text, n=8):
    """Top n CHANGELOG entries: (heading, what the entry says was verified)."""
    raise NotImplementedError('TODO: implement')

def results_section():
    raise NotImplementedError('TODO: implement')

def labels_section():
    raise NotImplementedError('TODO: implement')

def afk_section():
    raise NotImplementedError('TODO: implement')

def training_section():
    raise NotImplementedError('TODO: implement')

def build():
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
