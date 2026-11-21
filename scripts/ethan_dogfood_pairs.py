# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""dogfood v2 pairs: execution-verified, slim-format tool-use pairs for the split tool chain (scripts/ethan_split.py).

Why: the 7B CLI passed 5/20 dogfood sub-tasks (ignored tool results, answers from memory, calls printed as text, hallucinated paths).
These pairs teach the exact chain the dogfood tasks use: ONE call per step, answer QUOTING the tool result, follow `NEXT:` lines,
recover from errors ("Path not in workspace", "File not found", denied absolute path, unknown tool, unknown subcommand), refuse
delete/move/wipe requests, and never invent tool names.

Every scenario builds a fresh randomized project (directory names, file sets, wording, typos in the style of the personal lexicon),
EXECUTES the gold chain for real in a fresh example_host (the real ethan_split.py / ethan_split_plan.py, work folder outside the project)
and is accepted only if deterministic checks pass: expected values come from how the fixture was built (intended class of each file)
and are re-derived from the files on disk, are literally present in the tool output the model saw, and are quoted by the answer; the
project tree is byte-identical afterwards; copies equal the intended sets byte for byte. No model labels anything. Wrong first steps
used in recovery scenarios are history only: they get no training row.

Hold-out: 20% of scenarios (dogfood_eval) use a vocabulary-disjoint world (file stems, directory names, roots, lead-ins, phrasings,
tails) and are checked for zero overlap with the train scenarios and the real acceptance suite. Local only; secrets scrubbed.

  python3 scripts/ethan_dogfood_pairs.py build [--scenarios 190] [--seed 5202] [--out-dir data/dogfood]
  python3 scripts/ethan_dogfood_pairs.py mix   [--dogfood-weight 2]     # data/autoimprove/20261102/cli_real/TRAIN_MIX.json + train_mix_v6.jsonl
  python3 scripts/ethan_dogfood_pairs.py check                          # re-derive and compare with what is on disk
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import random
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path
import ethan_cli_real as cr
import ethan_cli_real_slim as slim
import ethan_split_plan as sp

def load_typos():
    raise NotImplementedError('TODO: implement')

def typoize(rng, text, protected, p=0.5):
    """Replace plain words with a lexicon typo (or one adjacent swap) with probability p per eligible word; protected tokens are untouched."""
    raise NotImplementedError('TODO: implement')

def fake_key(rng):
    raise NotImplementedError('TODO: implement')

def code_text(rng, ext):
    raise NotImplementedError('TODO: implement')

def build_world(rng, split):
    """-> (files {rel: text}, intended {rel: class}, dirs, meta). Names come only from this split's vocabulary pools."""
    raise NotImplementedError('TODO: implement')

class Run:
    """A scenario's real example_host plus a work folder OUTSIDE it. Every step is executed for real and recorded."""

    def __init__(self, scn):
        raise NotImplementedError('TODO: implement')

    def close(self):
        raise NotImplementedError('TODO: implement')

    def _split(self, rest):
        raise NotImplementedError('TODO: implement')

    def execute(self, name, args):
        raise NotImplementedError('TODO: implement')

    def do(self, name, args, record=True):
        raise NotImplementedError('TODO: implement')

    def sh(self, sub, record=True):
        raise NotImplementedError('TODO: implement')

    def silent_state(self, k):
        """Bring the work folder to state k (0 none, 1 classified, 2 +copy-code, 3 +copy-vault, 4 +verify, 5 +report) without recording."""
        raise NotImplementedError('TODO: implement')

    def workfiles(self, sub):
        raise NotImplementedError('TODO: implement')

def body(text):
    raise NotImplementedError('TODO: implement')

def counts_of(text):
    raise NotImplementedError('TODO: implement')

def next_cmd(text):
    raise NotImplementedError('TODO: implement')

def intended_counts(intended, exclude=...):
    raise NotImplementedError('TODO: implement')

def pick(rng, seq):
    raise NotImplementedError('TODO: implement')

def fam_status(rng, split, run, intended, meta):
    raise NotImplementedError('TODO: implement')

def fam_classify_one(rng, split, run, intended, meta):
    raise NotImplementedError('TODO: implement')

def fam_plan(rng, split, run, intended, meta):
    raise NotImplementedError('TODO: implement')

def _copy_fam(rng, split, run, intended, meta, kind, sub, dest):
    raise NotImplementedError('TODO: implement')

def fam_copy_code(rng, split, run, intended, meta):
    raise NotImplementedError('TODO: implement')

def fam_copy_vault(rng, split, run, intended, meta):
    raise NotImplementedError('TODO: implement')

def fam_verify(rng, split, run, intended, meta):
    raise NotImplementedError('TODO: implement')

def fam_report(rng, split, run, intended, meta):
    raise NotImplementedError('TODO: implement')

def fam_follow_next(rng, split, run, intended, meta):
    raise NotImplementedError('TODO: implement')

def fam_list_folder(rng, split, run, intended, meta):
    raise NotImplementedError('TODO: implement')

def fam_recover_tool(rng, split, run, intended, meta):
    raise NotImplementedError('TODO: implement')

def fam_recover_sub(rng, split, run, intended, meta):
    raise NotImplementedError('TODO: implement')

def fam_read_recover(rng, split, run, intended, meta):
    raise NotImplementedError('TODO: implement')

def fam_refuse(rng, split, run, intended, meta):
    raise NotImplementedError('TODO: implement')

def compose(rng, split, key, slots, typos):
    raise NotImplementedError('TODO: implement')

def expect_ok(answer, expect, forbid, outs):
    raise NotImplementedError('TODO: implement')

def make_scenario(rng, split, idx, fam):
    raise NotImplementedError('TODO: implement')

def scrub_ok(rows):
    raise NotImplementedError('TODO: implement')

def render(scn, outs, drop, tpl):
    raise NotImplementedError('TODO: implement')

def build(seed, n_total, eval_frac=0.2):
    raise NotImplementedError('TODO: implement')

def vocab_report(meta_all, scns):
    raise NotImplementedError('TODO: implement')

def write_jsonl(path, rows):
    raise NotImplementedError('TODO: implement')

def sha(path):
    raise NotImplementedError('TODO: implement')

def cmd_build(a):
    raise NotImplementedError('TODO: implement')

def cmd_check(a):
    raise NotImplementedError('TODO: implement')

def cmd_mix(a):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
