# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Read whole Codex AFK sessions and show where the autonomous loop is going: is it progressing or repeating itself?

Read-only on ~/.codex/sessions (the complete conversations the CLI already saves). Stdlib only, no model, no network.
For every turn (one AFK prompt and the reply) it records: sequence number, files edited, tests passed, whether live
evidence is still NOT_RUN, and how similar the reply is to the previous turn. It then marks STALLS: a run of turns on the
same milestone that keep editing the same files while the evidence the milestone needs stays NOT_RUN.

  afk_trajectory.py            analyse every AFK session, write data/afk_trajectory/{turns.jsonl,report.md,stall.json}
  afk_trajectory.py --stall    print only the verdict (exit 3 when the loop is stalled) so a loop can check itself
"""
import argparse, glob, json, os, re, sys
from datetime import datetime, timezone
from pathlib import Path

def similarity(a, b):
    """Share of distinct words two replies have in common (0..1); high means the reply repeats the last one."""
    raise NotImplementedError('TODO: implement')

def is_code_file(path):
    """Handoff notes and progress receipts are edited every turn, so they say nothing about whether the work moved."""
    raise NotImplementedError('TODO: implement')

def steer_milestone(text):
    """Milestones group by their safe typo-decoded reading, so a misspelled restatement of the same
    milestone cannot fragment a run and hide a stall from the steering verdict. Exact-pair corrections
    only (same guarantees as `ethan typo`); unknown words pass through unchanged."""
    raise NotImplementedError('TODO: implement')

def analyse_turn(user_text, reply, edited_files):
    raise NotImplementedError('TODO: implement')

def find_stalls(turns, min_run=3, same_files=0.5, same_words=0.5):
    """Runs of consecutive turns with the same milestone, overlapping edited files and similar replies while live evidence is NOT_RUN."""
    raise NotImplementedError('TODO: implement')

def stall_note(root=None):
    """Prompt text for a stalled loop, else ''. Recomputes from the saved sessions (about 3 s)."""
    raise NotImplementedError('TODO: implement')

def progress_note(turns, window=10):
    """One short paragraph that makes the next prompt different from the last: what the previous turn did and which code is
    absorbing the edits. '' when there is nothing real to say."""
    raise NotImplementedError('TODO: implement')

def evolve_note(root=None):
    """What the Linux AFK loop appends to every prompt: the progress note (always) plus the loop check (when stalled)."""
    raise NotImplementedError('TODO: implement')

def read_session(path):
    """Yield one dict per AFK turn from a Codex rollout file (streamed; files can be 80 MB)."""
    raise NotImplementedError('TODO: implement')

def build(paths):
    raise NotImplementedError('TODO: implement')

def report(turns, stalls):
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')

def _saved_verdict_current(paths):
    """True when stall.json is complete and newer than every session file, so --stall need not rescan gigabytes."""
    raise NotImplementedError('TODO: implement')

def _has_afk(path):
    raise NotImplementedError('TODO: implement')
