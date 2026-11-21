# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Locate->read->report evaluation for the Ethan CLI. Builds a fake home tree (~100 files, similar names, nested dirs, near-duplicates,
secrets) and asks differently worded, typo'd questions. Deterministic checkers only: right file found, values literally correct, no
invented path, honest 'not found', secrets/private never echoed. Never trains. Scratch lives under /mnt/GameDrive/twu_scratch/.

  python3 scripts/ethan_locate_eval.py list
  python3 scripts/ethan_locate_eval.py gold                 # self-check: every checker accepts its gold answer and rejects a wrong one (no model)
  python3 scripts/ethan_locate_eval.py run --label before --really-run [--tasks id,id]   # real CLI via bridge (needs the 7B up)
  python3 scripts/ethan_locate_eval.py summary --label before
  python3 scripts/ethan_locate_eval.py pairs --label before # failures -> verified pairs (data/dogfood/locate_pairs.jsonl)
"""
from __future__ import annotations
import argparse
import json
import os
import re
import shutil
import sys
import tempfile
import time
from pathlib import Path

def tree() -> dict:
    raise NotImplementedError('TODO: implement')

def add_guidance(root: Path, locate: bool=False):
    """Create a labeled synthetic benchmark context, not a production-policy copy.

    GEMINI.md is the fixture's default CLI context entry point. No host-local
    settings/guide or full workspace instructions are copied into the tiny task.
    """
    raise NotImplementedError('TODO: implement')

def build(root: Path) -> set:
    raise NotImplementedError('TODO: implement')

def money(*vals):
    raise NotImplementedError('TODO: implement')

def T(id, prompt, any_of=..., all_of=..., none_of=..., kind=..., verb=...):
    raise NotImplementedError('TODO: implement')

def check(task: dict, final: str, calls: list, names: set):
    """(ok, detail). Deterministic; looks only at final text and tool calls."""
    raise NotImplementedError('TODO: implement')

def gold_answer(t):
    raise NotImplementedError('TODO: implement')

def cmd_gold(a):
    raise NotImplementedError('TODO: implement')

class Runner:

    def __init__(self, locate=False):
        raise NotImplementedError('TODO: implement')

    def run(self, t, root: Path):
        raise NotImplementedError('TODO: implement')

def cmd_run(a):
    raise NotImplementedError('TODO: implement')

def cmd_tools(a):
    """Model-free ceiling: does the locate helper surface the right file/line for each task's own words, and NOT FOUND / nothing private otherwise?"""
    raise NotImplementedError('TODO: implement')

def cmd_gold_pairs(a):
    """Execution-verified locate->read->report pairs (slim prompt), no model: every step is run in a fresh fixture, the answer must pass check()."""
    raise NotImplementedError('TODO: implement')

def load(label):
    raise NotImplementedError('TODO: implement')

def rescore(r):
    """Recompute ok/check from the stored final text and calls with the CURRENT checkers (so checker fixes apply to every label equally)."""
    raise NotImplementedError('TODO: implement')

def cmd_summary(a):
    raise NotImplementedError('TODO: implement')

def cmd_pairs(a):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
