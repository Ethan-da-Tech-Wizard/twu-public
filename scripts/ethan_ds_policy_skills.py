# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Deterministic generator + verifier for the Ethan CLI "how this system works" policy dataset (policy_v1).

Stdlib only; no network, no model, no GPU. Ground truth comes from the repo itself:
  * data/enki_tools.json + data/tool_trials/enki_tools/LATEST.json + scripts/enki_tools.py (real run_tool gate, real argparse)
  * scripts/ethan_cda_judge.py (real select_jev_tier / evaluate_tool_gate / evaluate_code_gate, real argparse)
  * scripts/magi.py and scripts/ethan_git_guard.py (real argparse), data/workspace_labels.json, AGENTS.md
  * scripts/ethan_gemini_policy.toml evaluated by the REAL gemini-cli PolicyEngine through scripts/ethan_policy_bypass_suite.py
    (launcher mode = what `ethan chat` runs); data/autoimprove/20261101/verify/tooluse_v3_bypass.json for the bypass cases.
Skills 21..28 = the eight areas of the task list (enki, jev, magi, git, refusals, honest status, short replies, heat/RAM).

  python3 -B scripts/ethan_ds_policy_skills.py --out data/autoimprove/20261116/policy/policy_v1.jsonl --seed 20261116
  python3 -B scripts/ethan_ds_policy_skills.py --check FILE.jsonl      # re-verify an existing file

Run heavy invocations through scripts/ethan_capped_run.sh. Every row is re-checked by check_rows() before it is written;
rows that fail are dropped and counted in the manifest (the run exits 1 when any failed).
"""
from __future__ import annotations
import argparse
import collections
import contextlib
import copy
import functools
import hashlib
import io
import json
import os
import random
import re
import shlex
import shutil
import sys
import tempfile
from pathlib import Path

def bad_email(text):
    raise NotImplementedError('TODO: implement')

def private_call_arg(name, a):
    """True when a tool call's PATH-like arguments point into a private folder."""
    raise NotImplementedError('TODO: implement')

def read_live(rel):
    raise NotImplementedError('TODO: implement')

def read(rel):
    """Repo text as first seen in this process: other agents edit files while we generate, so generation reads a stable view."""
    raise NotImplementedError('TODO: implement')

def sha256_file(rel):
    raise NotImplementedError('TODO: implement')

class Oracle:
    """Cache of REAL gemini-cli PolicyEngine decisions (launcher mode). Pass 1 collects keys, then one batch resolves them."""

    def __init__(self):
        raise NotImplementedError('TODO: implement')

    @staticmethod
    def key(tool, args):
        raise NotImplementedError('TODO: implement')

    def ask(self, tool, args):
        raise NotImplementedError('TODO: implement')

    def resolve(self, calls):
        raise NotImplementedError('TODO: implement')

    def allowed(self, tool, args):
        raise NotImplementedError('TODO: implement')

    def message(self, tool, args):
        raise NotImplementedError('TODO: implement')

class _Parsed(Exception):

    def __init__(self, ns):
        raise NotImplementedError('TODO: implement')

def parse_cli(script, argv):
    """Run the module's own main() with parse_args patched to stop right after parsing. Returns (ok, namespace|error)."""
    raise NotImplementedError('TODO: implement')

class Repo:

    def __init__(self):
        raise NotImplementedError('TODO: implement')

    def reserved(self):
        raise NotImplementedError('TODO: implement')

    def docstring(self, name):
        raise NotImplementedError('TODO: implement')

def fake_root(repo=None, stop=False, bad_sha=...):
    """A throwaway root whose scripts/ and manifest are the real ones, so enki_tools.run_tool runs its REAL gate logic."""
    raise NotImplementedError('TODO: implement')

def gate_result(repo, name, approved=..., stop=False, bad=False):
    raise NotImplementedError('TODO: implement')

def enki_cli(repo, argv):
    raise NotImplementedError('TODO: implement')

def real_cmd(cmd):
    """Run a harmless read-only measurement for a tool result (wc/grep -c only)."""
    raise NotImplementedError('TODO: implement')

def lc(t):
    raise NotImplementedError('TODO: implement')

def _typo(t, r):
    raise NotImplementedError('TODO: implement')

def text_kind(base):
    raise NotImplementedError('TODO: implement')

def A(text=..., calls=None):
    raise NotImplementedError('TODO: implement')

def T(name, content):
    raise NotImplementedError('TODO: implement')

def SH(cmd):
    raise NotImplementedError('TODO: implement')

def fact_txt(path, has):
    raise NotImplementedError('TODO: implement')

def task_id(row):
    """Stable id of the underlying scenario (family + the calls/facts it is about), independent of the phrasing style."""
    raise NotImplementedError('TODO: implement')

class Gen:

    def __init__(self, seed, oracle, repo):
        raise NotImplementedError('TODO: implement')

    def refuse(self, reason_txt, alt=...):
        """A varied, <=3 line refusal that always carries the policy rationale."""
        raise NotImplementedError('TODO: implement')

    def rng(self, tag):
        raise NotImplementedError('TODO: implement')

    def style(self, skill, base, tag):
        raise NotImplementedError('TODO: implement')

    def add(self, skill, family, base, rest, facts=..., evidence=..., rejected=None, kind=..., deny=None, must=None, first_msgs=None, tools=None, verbatim=None):
        raise NotImplementedError('TODO: implement')

def rej(tail, why):
    raise NotImplementedError('TODO: implement')

def clip(s, n):
    """Shorten at a word boundary (never mid-word); a cut is marked with '...'."""
    raise NotImplementedError('TODO: implement')

def pl(n, word, plural=None):
    raise NotImplementedError('TODO: implement')

def reason(msg):
    raise NotImplementedError('TODO: implement')

def cat21(g):
    raise NotImplementedError('TODO: implement')

def cda():
    raise NotImplementedError('TODO: implement')

def tier_reason(j, res):
    raise NotImplementedError('TODO: implement')

def cat22(g):
    raise NotImplementedError('TODO: implement')

def who_table(r, R, me=None, force=None):
    """Synthetic `magi.py who` in the real line format. Returns (text, states{n:(state,cli,host)})."""
    raise NotImplementedError('TODO: implement')

def tok(r):
    raise NotImplementedError('TODO: implement')

def cat23(g):
    raise NotImplementedError('TODO: implement')

def cat24(g):
    raise NotImplementedError('TODO: implement')

def bypass_alt(tool, args):
    raise NotImplementedError('TODO: implement')

def cat25(g):
    raise NotImplementedError('TODO: implement')

def cat25b(g):
    raise NotImplementedError('TODO: implement')

def cat25c(g):
    """More benign lookalikes: scary words inside safe, allowed, really executed read-only commands. Different shapes from cat25b."""
    raise NotImplementedError('TODO: implement')

def cat29(g):
    raise NotImplementedError('TODO: implement')

def cat26(g):
    raise NotImplementedError('TODO: implement')

def cat27(g):
    raise NotImplementedError('TODO: implement')

def cat27b(g):
    raise NotImplementedError('TODO: implement')

def heat_decision(gpu, cpu, state):
    """AGENTS.md Linux limits: START at GPU<=96; PAUSE at GPU>=97 or CPU>=100; RESUME at GPU<=94 and CPU<=99; ABORT at GPU>=100."""
    raise NotImplementedError('TODO: implement')

def cat28(g):
    raise NotImplementedError('TODO: implement')

class Checker:

    def __init__(self, repo, oracle):
        raise NotImplementedError('TODO: implement')

    def fact(self, f):
        raise NotImplementedError('TODO: implement')

    def shell(self, cmd, ctx):
        raise NotImplementedError('TODO: implement')

    def sem_enki_tools(self, ns, args, ctx):
        raise NotImplementedError('TODO: implement')

    def sem_magi(self, ns, args, ctx):
        raise NotImplementedError('TODO: implement')

    def sem_ethan_git_guard(self, ns, args, ctx):
        raise NotImplementedError('TODO: implement')

    def sem_ethan_cda_judge(self, ns, args, ctx):
        raise NotImplementedError('TODO: implement')

    def sem_enki_tools_dummy(self):
        raise NotImplementedError('TODO: implement')

    def call(self, name, args, ctx):
        raise NotImplementedError('TODO: implement')

def extra_rules(c, tool_text, kind=...):
    """Conversation-level rules for one assistant call. Returns an error string or None."""
    raise NotImplementedError('TODO: implement')

def who_states(text):
    raise NotImplementedError('TODO: implement')

def final_text(msgs):
    raise NotImplementedError('TODO: implement')

def check_rows(rows, repo, oracle, strict_oracle=True):
    """Deterministic verification of every row. Returns (failures: {id: [reasons]}, stats)."""
    raise NotImplementedError('TODO: implement')

def prompt_ratios(rows):
    raise NotImplementedError('TODO: implement')

def task_stats(rows):
    raise NotImplementedError('TODO: implement')

def opener(text):
    raise NotImplementedError('TODO: implement')

def phrasing_report(rows):
    raise NotImplementedError('TODO: implement')

def build(seed, oracle, repo):
    raise NotImplementedError('TODO: implement')

def generate(seed):
    raise NotImplementedError('TODO: implement')

def summarize(rows):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
