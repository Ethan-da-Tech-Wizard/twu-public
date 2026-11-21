# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Training Set Curator: turns the raw DPO pile into a deduplicated "gold" set plus a held-out test split.

Why: the raw role datasets hold ~38k lines, but many files contain only a handful of distinct answers
(templated pairs that differ only by ids/numbers). Training on duplicates teaches the template, not the skill.

What it does (read-only on raw data; writes only under private/example_host/training/gold/):
  1. Reads every private/example_host/training/roles_data/*.jsonl (skips *.sync-conflict-* files).
  2. Normalizes each pair's `chosen` text (strips hex ids and digits) into a "template key".
  3. Keeps at most --cap pairs per template key and drops repeated (prompt, answer) combinations.
  4. Drops unusable pairs (empty, chosen == rejected, chosen shorter than 40 chars).
  5. Splits by template key (never by row) so the held-out set measures generalization, not memorization.
  6. Writes gold_train.jsonl, gold_holdout.jsonl and gold_report.json (per-file raw vs distinct counts).

"""
from __future__ import annotations
import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
import re
from typing import Any, Dict, List, Tuple

def template_key(text: str) -> str:
    """Normalizes text so pairs that differ only by ids/numbers collapse to one key."""
    raise NotImplementedError('TODO: implement')

def _bucket(key: str, buckets: int=10) -> int:
    raise NotImplementedError('TODO: implement')

def curate(cap: int=3, holdout_buckets: int=1, write: bool=True) -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def main() -> int:
    raise NotImplementedError('TODO: implement')
