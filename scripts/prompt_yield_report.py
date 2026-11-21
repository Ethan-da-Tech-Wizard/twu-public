# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Yield report: of the prompts sent to our CLIs, how many produced real, verified work, by origin, day, machine and tool.

Builds on the existing all-prompt ledger (scripts/all_prompt_ledger.py) and changes nothing in it. Read-only on every
transcript. No model, no network, stdlib only. For every prompt it assigns:

  ORIGIN (deterministic, strongest evidence first; harness text is never counted as human or autonomous):
    harness            AGENTS.md context, session context, task notifications, system messages
    autonomous_marked  carries the daemon marker (ground truth)
    autonomous_daemon  matches a dispatch our prompter daemon logged (ground truth for the past)
    autonomous_likely  the keyword heuristic says autonomous, no hard evidence (a guess)
    human              everything else

  OUTCOME (weak, rule-based labels from the reply summary and tool calls; checked by a human sample, see --review):
    verified_work      tools ran AND the reply shows passing evidence (PASS, N/N, tests pass, verified) and no failure
    failed             failure evidence and no passing evidence
    blocked            reply says it could not proceed (blocked, quota, not allowed, NOT_RUN)
    idle               no tools and the reply says nothing to do / standing by / resting
    worked_unverified  tools ran, no verification evidence
    talk_only          no tools, a substantive reply
    no_reply           the reply is empty or only a placeholder ("Recorded in ..."): nothing to judge, so no outcome is claimed

No classifier is trained here on purpose: origin is known exactly from the marker and the daemon log, and an outcome
model should only be trained after humans have labelled the sample in data/prompt_yield/review_queue.md.

  prompt_yield_report.py              scrape, label, write data/prompt_yield/report.md
  prompt_yield_report.py --review     also write a 20-prompt sample for a human to label
  prompt_yield_report.py --score      compare the rules with the human labels in data/prompt_yield/human_labels.jsonl
"""
import argparse, json, random, re, sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

def is_afk_stamped(text):
    raise NotImplementedError('TODO: implement')

def origin_of(marker, daemon_match, heuristic_autonomous, harness):
    raise NotImplementedError('TODO: implement')

def _last(rx, text):
    raise NotImplementedError('TODO: implement')

def outcome_of(response, tool_count):
    """The LAST verdict in the reply wins: "failed earlier, now 40/40 PASS" is a verified repair, not a failure."""
    raise NotImplementedError('TODO: implement')

def pct(a, b):
    raise NotImplementedError('TODO: implement')

def aggregate(rows):
    """rows: dicts with day, box_tool, origin, outcome. Returns the markdown report body."""
    raise NotImplementedError('TODO: implement')

def find_storms(items, window_s=30, min_run=5):
    """Retry storms: the SAME prompt sent again and again with gaps of at most window_s seconds.
    items: [(epoch, text, status_text)] -> [{start, end, count, status, sample}] largest first."""
    raise NotImplementedError('TODO: implement')

def storm_section(storms):
    raise NotImplementedError('TODO: implement')

def build_rows():
    raise NotImplementedError('TODO: implement')

def write_report(rows, storms=...):
    raise NotImplementedError('TODO: implement')

def write_review(rows, details, n=20):
    raise NotImplementedError('TODO: implement')

def score():
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
