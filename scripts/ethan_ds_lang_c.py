# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Deterministic, execution-verified C trajectories for the Ethan CLI (ethan-traj.v1, skill 31).

The CLI model cannot run gcc or any binary (the real gemini-cli policy denies them); it can read, edit .c/.h files, and run
`make test` (allowed; the Makefile write itself is ASK_USER). So every row teaches WRITING correct C. The GENERATOR does the proving:
each kept row's final repo state is compiled with `gcc -std=c17 -Wall -Wextra -Werror -O0` and run against a hidden harness (plus the
fixture's own `make test`, and AddressSanitizer/UBSan/LeakSanitizer for the memory-safety family). Compile diagnostics pasted into
prompts and `make test` outputs shown to the model are REAL (produced here, with LC_ALL=C, relative paths). Final answers never
claim a build or test pass that no tool result showed. Every shell/replace/write call is checked against the real PolicyEngine
(Oracle in scripts/ethan_ds_policy_skills.py, one batch): allow, or ask_user for a Makefile write (counted), never deny.

  python3 -B scripts/ethan_ds_lang_c.py --out data/autoimprove/20261116/lang/c_v1.jsonl --seed 1116 --per-family 50
  ETHAN_CAP=3G scripts/ethan_capped_run.sh /usr/bin/python3 -B scripts/ethan_ds_lang_c.py ...   (CPU/RAM capped, sequential)

Families: new_module, add_function, fix_compile_error, fix_failing_test, stub_impl_stdlib, scaffold_project, rename_refactor,
navigation, honesty_build, memory_safety. About 1/3 of rows carry a `rejected` side (claims a build, rewrites a file, edits the test,
invents an API, wrong signature, partial fix, fabricated quote, direct gcc call) that is verified to FAIL its checker.
"""
import argparse
import collections
import difflib
import glob as globmod
import hashlib
import json
import os
import random
import re
import resource
import shlex
import shutil
import subprocess
import sys
import tempfile
import ethan_ds_trajectories as T

def _lines(s):
    raise NotImplementedError('TODO: implement')

def hdr_block(e):
    raise NotImplementedError('TODO: implement')

def header_text(p, present=...):
    raise NotImplementedError('TODO: implement')

def util_text(p):
    raise NotImplementedError('TODO: implement')

def module_text(p, e, code=None):
    raise NotImplementedError('TODO: implement')

def tests_text(p, tests):
    raise NotImplementedError('TODO: implement')

def makefile_text(p):
    raise NotImplementedError('TODO: implement')

def readme_text(p):
    raise NotImplementedError('TODO: implement')

def base_files(p, present=..., module_override=None, extra=None, tests=True):
    """present = entries already implemented (header decl + src/<mod>.c + visible tests)."""
    raise NotImplementedError('TODO: implement')

def write_tree(root, files):
    raise NotImplementedError('TODO: implement')

def run_cmd(argv, cwd, timeout=90, tmpdir=None, extra_env=None):
    raise NotImplementedError('TODO: implement')

def run_make(root):
    raise NotImplementedError('TODO: implement')

def harness_text(p, tests, extra_inc=...):
    raise NotImplementedError('TODO: implement')

def scrub(out, root, hd):
    raise NotImplementedError('TODO: implement')

def run_harness(root, p, tests, asan=False):
    raise NotImplementedError('TODO: implement')

def trim_diag(out):
    """First diagnostic block of a failed `make test` plus the trailing gcc/make summary lines; real text, paths already relative."""
    raise NotImplementedError('TODO: implement')

class Cexample_host(T.example_host):
    """T.example_host plus `make test` run for real in the example_host directory (what the real policy allows the CLI model to do)."""

    def snapshot(self):
        raise NotImplementedError('TODO: implement')

    def t_run_shell_command(self, command, **kw):
        raise NotImplementedError('TODO: implement')

def play(files, prompt, steps, tag):
    raise NotImplementedError('TODO: implement')

def cleanup(sb):
    raise NotImplementedError('TODO: implement')

def C(name, **args):
    raise NotImplementedError('TODO: implement')

def RP(path, instr, old, new, multi=False):
    raise NotImplementedError('TODO: implement')

def minimal_edits(mut, orig):
    """List of (old, new) replaces that turn `mut` into `orig`; each `old` occurs exactly once in the text it is applied to."""
    raise NotImplementedError('TODO: implement')

def apply_edits(text, edits):
    raise NotImplementedError('TODO: implement')

def mutate_module(p, e, kind):
    raise NotImplementedError('TODO: implement')

def kinds_for(e):
    raise NotImplementedError('TODO: implement')

def diag_for(p, e, kind, work_tag):
    """Really build the mutated project and return (mutated module text, trimmed real diagnostic) or None when gcc does not give the expected error."""
    raise NotImplementedError('TODO: implement')

def break_logic(p, e):
    raise NotImplementedError('TODO: implement')

def cap1(s):
    raise NotImplementedError('TODO: implement')

def honest_tail(rng, hint=True):
    raise NotImplementedError('TODO: implement')

def pick(rng, seq, i):
    raise NotImplementedError('TODO: implement')

def final_shape(text):
    raise NotImplementedError('TODO: implement')

def tool_calls(msgs):
    raise NotImplementedError('TODO: implement')

def last_make_ok(msgs):
    """True when a `make test` ran successfully after the last successful edit (or there was no edit and one ran)."""
    raise NotImplementedError('TODO: implement')

def verify_final(sb, msgs, files, spec, rejected=False):
    """Universal checker. Chosen rows must pass; every `rejected` side must fail it."""
    raise NotImplementedError('TODO: implement')

def common_prefix(a, b):
    raise NotImplementedError('TODO: implement')

def make_row(fam, tag, plan):
    """plan: prompt, files, steps, spec, rej (optional dict steps/reason). Returns (row, why) with row None when verification fails."""
    raise NotImplementedError('TODO: implement')

def lead(i, pool):
    raise NotImplementedError('TODO: implement')

def ctx_names(p, e):
    raise NotImplementedError('TODO: implement')

def claim_line(i):
    raise NotImplementedError('TODO: implement')

def proto_of(e):
    raise NotImplementedError('TODO: implement')

def bad_sig(e):
    raise NotImplementedError('TODO: implement')

def stub_text(p, e):
    raise NotImplementedError('TODO: implement')

def edit_summary(old, new):
    """(old_line, new_line) of the first differing line pair (either may be None)."""
    raise NotImplementedError('TODO: implement')

def hdr_replace(p, e, bad=False):
    raise NotImplementedError('TODO: implement')

def b_new_module(i, c, p, e, rej_mode, rng):
    raise NotImplementedError('TODO: implement')

def host_text(p, a):
    raise NotImplementedError('TODO: implement')

def b_add_function(i, c, p, e, rej_mode, rng, hosts):
    raise NotImplementedError('TODO: implement')

def b_compile_fix(i, c, p, e, rej_mode, rng):
    raise NotImplementedError('TODO: implement')

def mk_failing(p, e):
    raise NotImplementedError('TODO: implement')

def b_failing_test(i, c, p, e, rej_mode, rng):
    raise NotImplementedError('TODO: implement')

def b_stub_impl(i, c, p, e, rej_mode, rng):
    raise NotImplementedError('TODO: implement')

def scaffold_files(p, e):
    raise NotImplementedError('TODO: implement')

def b_scaffold(i, c, p, e, rej_mode, rng):
    raise NotImplementedError('TODO: implement')

def b_rename(i, c, p, e, rej_mode, rng):
    raise NotImplementedError('TODO: implement')

def typedef_name(e):
    raise NotImplementedError('TODO: implement')

def b_navigation(i, c, p, e, rej_mode, rng, others):
    raise NotImplementedError('TODO: implement')

def first_fail_line(out):
    raise NotImplementedError('TODO: implement')

def b_honesty(i, c, p, e, rej_mode, rng):
    raise NotImplementedError('TODO: implement')

def b_memory(i, c, p, m, rej_mode, rng):
    raise NotImplementedError('TODO: implement')

def small(e, n):
    raise NotImplementedError('TODO: implement')

def pools(rng):
    raise NotImplementedError('TODO: implement')

def build_plan(fam, i, c, p, e, rej_mode, rng, pool):
    raise NotImplementedError('TODO: implement')

def policy_filter(rows, stats):
    raise NotImplementedError('TODO: implement')

def public(r):
    raise NotImplementedError('TODO: implement')

def token_filter(rows, stats, enabled=True):
    raise NotImplementedError('TODO: implement')

def tokenize_child(inp, outp):
    raise NotImplementedError('TODO: implement')

def gen_family(fam, seed, per_family, stats, seen, tokens=True):
    raise NotImplementedError('TODO: implement')

def toolchain():
    raise NotImplementedError('TODO: implement')

def build(seed, per_family, families, tokens=True):
    raise NotImplementedError('TODO: implement')

def write_outputs(rows, stats, tc, out, seed, per_family):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
