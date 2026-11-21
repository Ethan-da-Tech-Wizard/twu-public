# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Deterministic, execution-verified GIT and GITHUB trajectories for the Ethan CLI model (skill 41, schema ethan-traj.v1).

Every fixture is a REAL git repository built with the real git binary at generation time (fixed example identities and dates, a temp dir under
the scratch root, never the workspace). Tool results come from the shared example_host of scripts/ethan_ds_trajectories.py extended by composition:
read-only git commands and the real scripts/ethan_git_guard.py (copied into the fixture) run for real; timestamps and commit ids that the guard
creates are replaced by deterministic stand-ins. Every call is checked against the real gemini-cli PolicyEngine (Oracle of
scripts/ethan_ds_policy_skills.py). Rows are replayed byte-identically and checked on final repo state; ~30% carry a verified-failing `rejected`.
No network, no model calls. Usage: python3 -B scripts/ethan_ds_git.py --out data/autoimprove/20261116/git/git_v1.jsonl --seed 1116 --per-family 48
"""
import argparse
import collections
import contextlib
import hashlib
import io
import json
import os
import random
import re
import shlex
import shutil
import subprocess
import sys
import ethan_ds_trajectories as T
from ethan_ds_trajectories import example_host, Run, parse_calls, jerr, is_err, DISPLAY_ROOT, TOOLS, BUGS, fn_source, entry_ns, call_text, camel, norm_prompt

def sh_env(root):
    raise NotImplementedError('TODO: implement')

def build_env(root, when=..., who=...):
    raise NotImplementedError('TODO: implement')

def git_run(fx, args, when=..., who=..., ok=...):
    raise NotImplementedError('TODO: implement')

def wfile(fx, rel, text):
    raise NotImplementedError('TODO: implement')

def rfile(fx, rel):
    raise NotImplementedError('TODO: implement')

def clean_bug(e):
    """The buggy variant fails by wrong value (an assertion), never by an exception, and differs on at least one input."""
    raise NotImplementedError('TODO: implement')

class St:
    """Logical module state; render() gives module and test text."""

    def __init__(self, mod, cat):
        raise NotImplementedError('TODO: implement')

    def module(self):
        raise NotImplementedError('TODO: implement')

    def test(self, extra_asserts=...):
        raise NotImplementedError('TODO: implement')

    def readme(self):
        raise NotImplementedError('TODO: implement')

def build_fixture(rng, fx, *, guard=False, buggy_head=False, wt=None, branch=None, detach=False, no_git=False, ncommits=None, consts_n=None, extra_files=None):
    """Real git repo. Returns info dict (mod, paths, commits with real hashes, consts, funcs, extras)."""
    raise NotImplementedError('TODO: implement')

def build_conflict(rng, fx):
    """Real merge conflict: main and feature both change X (and sometimes Y); K is untouched so the hunks stay separate."""
    raise NotImplementedError('TODO: implement')

class Gexample_host(example_host):
    """example_host + real read-only git + the real guard. Output ids that depend on the wall clock are replaced by stable stand-ins."""

    def __init__(self, fixture, work, tag=...):
        raise NotImplementedError('TODO: implement')

    def _run(self, argv, env=None, timeout=60):
        raise NotImplementedError('TODO: implement')

    def _revs(self):
        raise NotImplementedError('TODO: implement')

    def branch(self):
        raise NotImplementedError('TODO: implement')

    def state(self):
        raise NotImplementedError('TODO: implement')

    def _fake(self, kind, real):
        """Stand-in keyed on the stable tail of the id (the timestamp part is wall-clock and must not matter)."""
        raise NotImplementedError('TODO: implement')

    def norm(self, out):
        raise NotImplementedError('TODO: implement')

    def _sync_vol(self):
        raise NotImplementedError('TODO: implement')

    def _done(self, out, rc):
        raise NotImplementedError('TODO: implement')

    def t_replace(self, file_path, *a, **k):
        raise NotImplementedError('TODO: implement')

    def t_write_file(self, file_path, content, **k):
        raise NotImplementedError('TODO: implement')

    def t_run_shell_command(self, command, **kw):
        raise NotImplementedError('TODO: implement')

    def _git(self, argv, pipe):
        raise NotImplementedError('TODO: implement')

    def _guard(self, argv):
        raise NotImplementedError('TODO: implement')

def body(out):
    raise NotImplementedError('TODO: implement')

def rcode(out):
    raise NotImplementedError('TODO: implement')

def blines(out):
    raise NotImplementedError('TODO: implement')

class GRun(Run):

    def denied(self, name, args):
        """A call the policy engine denies: recorded without a tool result (as in the policy rows' rejected side)."""
        raise NotImplementedError('TODO: implement')

    def sh(self, cmd, train=True):
        raise NotImplementedError('TODO: implement')

def oracle():
    raise NotImplementedError('TODO: implement')

def claim_problems(final, outs):
    raise NotImplementedError('TODO: implement')

def snippets(final):
    raise NotImplementedError('TODO: implement')

def guard_cli_problem(cmd):
    """Hand-off commands for the guard must parse under the real argparse of scripts/ethan_git_guard.py."""
    raise NotImplementedError('TODO: implement')

def verify(sp, messages, fixture, work, tag):
    raise NotImplementedError('TODO: implement')

def _verify(sp, messages, fixture, work, tag):
    raise NotImplementedError('TODO: implement')

def changed_files(a, b):
    raise NotImplementedError('TODO: implement')

def pick(rng, items):
    raise NotImplementedError('TODO: implement')

def pl(n, w):
    raise NotImplementedError('TODO: implement')

def gcmds(info):
    raise NotImplementedError('TODO: implement')

def sub_line(h, s):
    raise NotImplementedError('TODO: implement')

def commit_lines(info):
    """Expected `git log --oneline` lines, newest first."""
    raise NotImplementedError('TODO: implement')

def lead(rng, kind):
    raise NotImplementedError('TODO: implement')

def first_diff_lines(out, name):
    raise NotImplementedError('TODO: implement')

def base_sp(rng, fx, **kw):
    raise NotImplementedError('TODO: implement')

def fmt(rng, pool, **slots):
    raise NotImplementedError('TODO: implement')

def terse(rng, text):
    raise NotImplementedError('TODO: implement')

def s_log(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def g_log(sp, run, rng, mode=None):
    raise NotImplementedError('TODO: implement')

def s_show(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def g_show(sp, run, rng, mode=None):
    raise NotImplementedError('TODO: implement')

def s_pick(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def g_pick(sp, run, rng, mode=None):
    raise NotImplementedError('TODO: implement')

def s_branch(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def g_branch(sp, run, rng, mode=None):
    raise NotImplementedError('TODO: implement')

def min_edit(e, text):
    """old/new strings for replacing the buggy body of entry e inside module text (minimal differing lines)."""
    raise NotImplementedError('TODO: implement')

def s_flow(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def flow_check(sp):
    raise NotImplementedError('TODO: implement')

def g_flow(sp, run, rng, mode=None):
    raise NotImplementedError('TODO: implement')

def s_draft(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def g_draft(sp, run, rng, mode=None):
    raise NotImplementedError('TODO: implement')

def s_conflict(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def conflict_check(sp):
    raise NotImplementedError('TODO: implement')

def g_conflict(sp, run, rng, mode=None):
    raise NotImplementedError('TODO: implement')

def s_ignore(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def check_ignored(ignore_text, pos, neg):
    raise NotImplementedError('TODO: implement')

def ignore_check(sp):
    raise NotImplementedError('TODO: implement')

def g_ignore(sp, run, rng, mode=None):
    raise NotImplementedError('TODO: implement')

def hook_text(rules, info, rng=None):
    raise NotImplementedError('TODO: implement')

def hook_scenario(rule, info, h):
    """(violating setup, clean setup) on a scratch repo; returns exit codes of the hook for both."""
    raise NotImplementedError('TODO: implement')

def s_hook(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def hook_check(sp):
    raise NotImplementedError('TODO: implement')

def g_hook(sp, run, rng, mode=None):
    raise NotImplementedError('TODO: implement')

def wf_build(mod, test, *, name=..., trig=..., branch=..., py=..., cron=..., lint=False, perms=True, risks=..., job=..., tag=...):
    raise NotImplementedError('TODO: implement')

def wf_problems(text, need_py=..., need_on=..., need_cron=None):
    raise NotImplementedError('TODO: implement')

def s_wfwrite(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def wfwrite_check(sp):
    raise NotImplementedError('TODO: implement')

def g_wfwrite(sp, run, rng, mode=None):
    raise NotImplementedError('TODO: implement')

def s_wfreview(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def wfreview_check(sp):
    raise NotImplementedError('TODO: implement')

def g_wfreview(sp, run, rng, mode=None):
    raise NotImplementedError('TODO: implement')

def s_prdraft(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def prdraft_check(sp):
    raise NotImplementedError('TODO: implement')

def g_prdraft(sp, run, rng, mode=None):
    raise NotImplementedError('TODO: implement')

def deny_reason(cmd):
    raise NotImplementedError('TODO: implement')

def refusal_text(rng, i, reason, extra, alt):
    raise NotImplementedError('TODO: implement')

def s_gh(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def g_gh(sp, rng, i):
    raise NotImplementedError('TODO: implement')

def fake_gh_answer(sp):
    raise NotImplementedError('TODO: implement')

def s_secret(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def g_secret(sp, rng, i):
    raise NotImplementedError('TODO: implement')

def s_rewrite(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def g_rewrite(sp, rng, i):
    raise NotImplementedError('TODO: implement')

def s_main(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def g_main(sp, rng, i):
    raise NotImplementedError('TODO: implement')

def s_err(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def g_err(sp, run, rng, mode=None):
    raise NotImplementedError('TODO: implement')

def s_gerr(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def g_gerr(sp, run, rng, mode=None):
    raise NotImplementedError('TODO: implement')

def valid_modes(fam, sp):
    raise NotImplementedError('TODO: implement')

def mutate(final, rng):
    """A believable but unsupported rewrite of the quoted facts: hashes and numbers inside backticks change."""
    raise NotImplementedError('TODO: implement')

def task_id_of(fam, sp):
    raise NotImplementedError('TODO: implement')

def rowseed(seed, fam, idx, attempt):
    raise NotImplementedError('TODO: implement')

def verify_prose(sp, final):
    raise NotImplementedError('TODO: implement')

def prose_rejected(sp, mode, rng):
    raise NotImplementedError('TODO: implement')

def gen_prose(seed, fam, idx, attempt, want_reject):
    raise NotImplementedError('TODO: implement')

def gen_row(seed, fam, idx, attempt, scratch, want_reject, collect=False):
    raise NotImplementedError('TODO: implement')

def est_tokens(row):
    raise NotImplementedError('TODO: implement')

def want_reject(i):
    raise NotImplementedError('TODO: implement')

def build(seed, per_family, scratch, families=None):
    """Pass 1 collects every tool call, one batch asks the real policy engine, pass 2 builds and verifies with the real verdicts."""
    raise NotImplementedError('TODO: implement')

def token_counts(rows):
    """Real Qwen3.5 tokenizer, CPU, local files only (separate venv). Counts the chosen conversation and the longest rejected variant."""
    raise NotImplementedError('TODO: implement')

def versions():
    raise NotImplementedError('TODO: implement')

def manifest(rows, dropped, args, path, toks=None, tok_dropped=0):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
