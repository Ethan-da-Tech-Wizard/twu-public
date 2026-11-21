# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""
PROGRAM:       command_library_eval.py
PROGRAMMER:    Magi 10 (claude, example_host)
LAST MODIFIED: 2026-11-20
PURPOSE:       Measure how well Command Library search answers plain-language questions ("find files modified in
               the last day" must put `find` first). Read-only: it opens the library database read-only and never
               writes to it.

WHAT IT DOES
  * Loads data/commands/eval_questions.json (hand written task questions, each with the acceptable commands, and
    optional per-OS expectations for example_host, Arch and macOS).
  * Runs a ranker over every question and scores it: recall@1, recall@5, recall@10 and MRR (mean reciprocal rank,
    the average of 1/rank of the first correct command), overall and per category.
  * Prints every failure (question, what was expected, what came back first) so nothing is hidden.
  * Questions whose acceptable commands do not exist on this computer's OS are "unanswerable here": they are
    listed and NOT counted (a missing tool is not a ranking failure).

SPLIT (honesty rule)
  Each question has a fixed split, dev or heldout, derived from a hash of its text. Tune the ranker on dev ONLY;
  report heldout numbers as the honest result. `--split heldout` never prints expectations that would invite tuning
  unless `--failures` is given.

RANKERS
  baseline : scripts/command_library.py search() exactly as it is (the starting point).
  layer    : scripts/command_library_query.py rank() (intents, field boosts, OS-aware ranking).

USAGE (from the repo root)
  python3 scripts/command_library_eval.py --ranker baseline --split all
  python3 scripts/command_library_eval.py --ranker layer --split heldout --failures
  python3 scripts/command_library_eval.py --ranker layer --os macos     (uses the macOS expectations; needs a macOS DB)
  COMMAND_LIBRARY_DB=/path/to/snapshot.sqlite3 python3 scripts/command_library_eval.py ...   (repeatable run on a frozen copy)
  splits: dev (tune here), heldout, all, fresh (informal, used to guide GENERAL fixes), fresh2 (informal, untouched until the final report), fresh3 (single-purpose tools, 2026-11-20)

CHANGE HISTORY:
  2026-11-20  Magi 10  Created (MAGI_TODO cca40004).
"""
from __future__ import annotations
import argparse
import json
import sqlite3
import sys
from collections import OrderedDict, defaultdict
from pathlib import Path

def load_questions(path=..., fresh=False, fresh2=False, fresh3=False):
    """Read the question file; returns the list of question dicts."""
    raise NotImplementedError('TODO: implement')

def expected_for(q, os_id):
    """Acceptable commands for this OS: the per-OS list if present, else the general list."""
    raise NotImplementedError('TODO: implement')

def open_db(root):
    """Open this computer's library read-only WITHOUT importing command_library.py (another agent is editing it and its
    import can break mid-rewrite; the eval must stay runnable). Same path rule: data/commands/hosts/<host>/."""
    raise NotImplementedError('TODO: implement')

def known_commands(root, os_id):
    """Set of command names present in the library for this OS (read-only). Used to skip unanswerable questions."""
    raise NotImplementedError('TODO: implement')

def _fts_query(text, any_term=False):
    raise NotImplementedError('TODO: implement')

def baseline_ranker(root, text, os_id=None, limit=50):
    """Frozen old search: AND query then OR fallback on docs_fts (bm25 6/4/1), exact command name, example hits."""
    raise NotImplementedError('TODO: implement')

def layer_ranker(root, text, os_id=None, limit=50):
    """The new query layer (scripts/command_library_query.py)."""
    raise NotImplementedError('TODO: implement')

def score(ranked, expected):
    """1-based rank of the first expected command in the ranked list, or None."""
    raise NotImplementedError('TODO: implement')

def run(root, ranker_name, split, os_id, verbose_failures):
    raise NotImplementedError('TODO: implement')

def fmt(b):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
