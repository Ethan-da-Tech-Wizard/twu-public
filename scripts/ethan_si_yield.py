# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Deterministic selection math: which verified runs become SFT/DPO training data.

Pure functions only; the `report` CLI reads a run file and prints, with no side effects.
"""
import argparse
import hashlib
import itertools
import json
import sys
from pathlib import Path
import ethan_si_math

def shingles(text, k=3):
    raise NotImplementedError('TODO: implement')

def jaccard(a, b):
    raise NotImplementedError('TODO: implement')

def dedupe_near(traces, threshold):
    raise NotImplementedError('TODO: implement')

def _hash(r):
    raise NotImplementedError('TODO: implement')

def _key(r):
    raise NotImplementedError('TODO: implement')

def _usable(records, f, passing):
    raise NotImplementedError('TODO: implement')

def _by_task(rs):
    raise NotImplementedError('TODO: implement')

def select_sft(records, f):
    raise NotImplementedError('TODO: implement')

def select_dpo(records, f):
    raise NotImplementedError('TODO: implement')

def diversity_report(selected):
    raise NotImplementedError('TODO: implement')

def _with_share(rep, all_tasks):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
