# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""queue_audit: no queue item may be 'waiting', 'deferred' or tied to a time of day. Stdlib only, offline.

Every list item (a line starting with '-', '*' or '1.') in the handoff file, outside code fences, resolves to exactly one of:
  closed                                    (already in the vocabulary, untouched)
  open: <what> recheck_at=<time>            (time-of-day / defer wording removed, a recheck added)
  blocked-external: owner=<who> check=<how> recheck_at=<when>
  unclosable-defer                          (wording kept; reported, because no owner can be named: nothing is invented)
Dry run by default. --apply rewrites FILE and requires --backup DIR (the original is copied there first).
Receipts are evidence and are never rewritten; --receipts DIR only REPORTS deferral wording in each receipt's README.md.

  queue_audit.py FILE [--apply --backup DIR] [--receipts DIR]
"""
from __future__ import annotations
import argparse
import re
import shutil
import sys
import time
from pathlib import Path

def _recheck(now):
    raise NotImplementedError('TODO: implement')

def rewrite_item(text, now=None):
    """-> {'kind', 'new', 'warning'} for the text of ONE item (no bullet)."""
    raise NotImplementedError('TODO: implement')

def audit_text(text, now=None):
    """-> {'new_text', 'counts', 'changes': [(lineno, old, new, kind, warning)], 'unclosable': [(lineno, text)]}"""
    raise NotImplementedError('TODO: implement')

def scan_receipts(root):
    """Report deferral wording in each receipt's README.md (the human-written note). Evidence copies are skipped. Never rewrites."""
    raise NotImplementedError('TODO: implement')

def run(path, apply=False, backup=None, now=None, out=...):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
