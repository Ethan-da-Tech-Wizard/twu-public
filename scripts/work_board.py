# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""work_board: one page that says what can be started NOW, what is blocked on what, and which claims look stale.

Magi 6, 2026-11-13. Read-only on the repo; the only file it writes is its own output
(default data/lucy_kit/WORK_BOARD.md). Stdlib only, no network, no model calls, py3.9+.

Sources (all cheap to parse; each is optional and a missing one is reported, never invented):
  data/lucy_kit/NEEDS_REGISTER_FULL.md   need rows: id, status, owner, blocking dependency
  data/lucy_kit/PROBLEMS_REGISTER.md     problem rows (open ones only)
  data/lucy_kit/KANTO_PLAYTEST_PLAN.md   task list (tables or "- [ ]" checkboxes), if present
  data/rules/decisions/*.jsonl, acks/    decision ledger: unacked count per seat
  data/rules/decisions/OPEN_QUESTIONS*.md, CONFLICTS-*.md   questions for Ethan with "My pick"/"Recommend" defaults
  business/example_host/comms/agent*/outbox.jsonl   active claims (fast tail scan) and seat activity
  python3 scripts/magi.py inbox --seat N --digest   pending-message summary (digest never acknowledges)

Classes: READY (no unmet dependency), BLOCKED (names what it waits on), WAITING-ON-ETHAN.
  work_board.py [--out PATH] [--stdout] [--json] [--root DIR] [--seat N] [--stale-hours H]
                [--claim-hours H] [--claims-tool] [--no-inbox]
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

def read_text(path):
    raise NotImplementedError('TODO: implement')

def parse_tables(text):
    """Yield (section_heading, header_cols_lowercase, [row cells]) for each markdown table row."""
    raise NotImplementedError('TODO: implement')

def col(header, cells, *names):
    raise NotImplementedError('TODO: implement')

def status_word(status):
    raise NotImplementedError('TODO: implement')

def owners_of(owner):
    raise NotImplementedError('TODO: implement')

def snippet(s, n=110):
    raise NotImplementedError('TODO: implement')

def load_needs(text):
    raise NotImplementedError('TODO: implement')

def find_default(*texts):
    raise NotImplementedError('TODO: implement')

def classify_need(n, needs):
    """Return (klass, waits_on, action, default)."""
    raise NotImplementedError('TODO: implement')

def priority_key(item, order):
    raise NotImplementedError('TODO: implement')

def build_items(needs, problems_text, plan_text):
    raise NotImplementedError('TODO: implement')

def read_jsonl(path):
    raise NotImplementedError('TODO: implement')

def ledger_state(root):
    raise NotImplementedError('TODO: implement')

def parse_questions(root):
    raise NotImplementedError('TODO: implement')

def tail_lines(path, nbytes):
    raise NotImplementedError('TODO: implement')

def parse_ts(s):
    raise NotImplementedError('TODO: implement')

def extract_paths(text, root):
    raise NotImplementedError('TODO: implement')

def scan_claims(root, now, lookback_h=48.0, nbytes=600000):
    """Fast outbox scan. A claim is kind==claim or status==running with a repo path; closed by a later
    completed/blocked/reviewed packet with the same packet_id. Returns (claims, seat_last_activity_hours)."""
    raise NotImplementedError('TODO: implement')

def parse_claims_output(text):
    """Parse `twu_claims.py list` text: 'seat N  path  packet  age X.Xh  [STATE]' then a quoted snippet line."""
    raise NotImplementedError('TODO: implement')

def claims_from_tool(root, timeout=20, hours=48):
    raise NotImplementedError('TODO: implement')

def merge_claims(claims):
    """One row per (seat, packet): all its paths."""
    raise NotImplementedError('TODO: implement')

def mark_stale(claims, last_activity, stale_hours):
    raise NotImplementedError('TODO: implement')

def inbox_digest(root, seat, timeout=15):
    raise NotImplementedError('TODO: implement')

def render(board):
    raise NotImplementedError('TODO: implement')

def build_board(root=None, now=None, seat=6, stale_hours=6.0, claim_hours=48.0, use_claims_tool=False, inbox=True):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
