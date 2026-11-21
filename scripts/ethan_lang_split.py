# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Deterministic family-disjoint train/dev splitter for ethan-system-pair.v1 rows.

Units are whole families (rows sharing a family name, an id, or an exact /
normalized prompt are merged into one unit, so leaks are impossible by
construction). Order is decided by sha256(seed|family). No model calls.
"""
import argparse, hashlib, json, os, re, sys
from collections import defaultdict

def sha_bytes(b):
    raise NotImplementedError('TODO: implement')

def sha_file(p):
    raise NotImplementedError('TODO: implement')

def norm_prompt(s):
    raise NotImplementedError('TODO: implement')

def prompt_of(r):
    raise NotImplementedError('TODO: implement')

def load_rows(paths):
    raise NotImplementedError('TODO: implement')

def split(rows, seed=..., frac=...):
    raise NotImplementedError('TODO: implement')

def leak_report(train, dev):
    raise NotImplementedError('TODO: implement')

def counts(rows):
    raise NotImplementedError('TODO: implement')

def per_lang(rows):
    raise NotImplementedError('TODO: implement')

def build(paths, seed):
    raise NotImplementedError('TODO: implement')

def dumps(o):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
