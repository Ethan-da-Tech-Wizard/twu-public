# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Rust language rows for the Ethan CLI model (ethan-traj.v1, skill 33): execution-verified, policy-gated, honest about not compiling.

The CLI model cannot run cargo or rustc (the real gemini-cli policy denies them); it CAN run `make test` when a Makefile exists, read, grep,
and write/replace source files (Cargo.toml and Makefile writes are ASK_USER). So every row teaches writing correct Rust and reporting honestly.
At generation time this script really builds the final repo state with the std-only Rust toolchain (rustc/cargo, `--offline`, warnings as errors)
against a hidden harness, really captures `make test` output and real rustc diagnostics for the tool results, and replays every call on a
fresh example_host (byte-identical outputs). Every call is checked against the real PolicyEngine (Oracle from scripts/ethan_ds_policy_skills.py).

Reuses (never copies) example_host/Run/policy oracle from scripts/ethan_ds_trajectories.py.
Usage: python3 -B scripts/ethan_ds_lang_rust.py --out data/autoimprove/20261116/lang/rust_v1.jsonl --seed 1116 --per-family 48
"""
import argparse
import hashlib
import json
import os
import random
import re
import shutil
import subprocess
import sys
import textwrap
import ethan_ds_trajectories as T
import pwd

def SP(name, sig, desc, src, tests, uses=..., tuses=..., ren=None, bug=None, inv=None, api=...):
    raise NotImplementedError('TODO: implement')

def CE(name, code, ok, bad_from, bad_to, tests, uses=..., tuses=..., note=...):
    raise NotImplementedError('TODO: implement')

def tname(sp):
    raise NotImplementedError('TODO: implement')

def indent(text, n):
    raise NotImplementedError('TODO: implement')

def module_text(specs, unit=True, nunit=1):
    raise NotImplementedError('TODO: implement')

def test_file_text(crate, mod, specs, prefix=..., only=None):
    """Integration-style tests using the crate's public path (also the hidden harness)."""
    raise NotImplementedError('TODO: implement')

def cargo_toml(crate):
    raise NotImplementedError('TODO: implement')

def w(fx, rel, text):
    raise NotImplementedError('TODO: implement')

def lib_text(crate, mods, extra=...):
    raise NotImplementedError('TODO: implement')

def make_fixture(fx, crate, mods, makefile=True, readme=True, tests_dir=None, extra_lib=...):
    """mods: list of (modname, specs, unit_tests: bool). tests_dir: {modname: text} integration tests."""
    raise NotImplementedError('TODO: implement')

def broken_text(ce):
    raise NotImplementedError('TODO: implement')

def ce_spec(ce, ok=True):
    """A spec-shaped view of a compile-error entry (src is the good or the broken text)."""
    raise NotImplementedError('TODO: implement')

def buggy_src(sp):
    raise NotImplementedError('TODO: implement')

def inv_src(sp):
    raise NotImplementedError('TODO: implement')

def tool_env(target, deny_warnings=False):
    raise NotImplementedError('TODO: implement')

def norm_out(out, root=None):
    raise NotImplementedError('TODO: implement')

def snap_key(files, extra):
    raise NotImplementedError('TODO: implement')

def run_in_tree(files, argv, deny_warnings=False, timeout=120):
    """Write `files` ({rel: bytes}) into a fresh temp dir, run argv there with the real toolchain. Cached by content. -> (rc, normalised output)."""
    raise NotImplementedError('TODO: implement')

def tree_files(d):
    raise NotImplementedError('TODO: implement')

def rustc_diag(files):
    """Real rustc diagnostic for the (broken) crate: metadata-only build of src/lib.rs. -> (rc, text)."""
    raise NotImplementedError('TODO: implement')

def versions():
    raise NotImplementedError('TODO: implement')

def selfcheck():
    """Catalogue self-test: every spec compiles warning-free and passes; every bug fails; every inv fails to compile; every CE breaks as stated and its fix passes."""
    raise NotImplementedError('TODO: implement')

class Rexample_host(T.example_host):
    """Base example_host plus a real `make test` (the one build command the policy allows); output captured from the real toolchain, normalised."""

    def t_run_shell_command(self, command, **kw):
        raise NotImplementedError('TODO: implement')

class RRun(T.Run):

    def __init__(self, sb, prompt):
        raise NotImplementedError('TODO: implement')

    def call(self, name, args, train=True):
        raise NotImplementedError('TODO: implement')

def make_quote(out):
    raise NotImplementedError('TODO: implement')

def claims_success(text):
    raise NotImplementedError('TODO: implement')

def policy_check(calls):
    raise NotImplementedError('TODO: implement')

def harness(files, hidden, run_test=None):
    raise NotImplementedError('TODO: implement')

def rverify(sp, messages, fixture, work):
    """-> (ok, detail, asks). Replays all calls on a fresh example_host, then checks policy, final state, real build/harness and the honesty of the answer."""
    raise NotImplementedError('TODO: implement')

class Meter:

    def __init__(self, enabled=True):
        raise NotImplementedError('TODO: implement')

    def count(self, row):
        raise NotImplementedError('TODO: implement')

    def close(self):
        raise NotImplementedError('TODO: implement')

def rd(fx, rel):
    raise NotImplementedError('TODO: implement')

def wrong_sig_src(sp):
    raise NotImplementedError('TODO: implement')

def with_src(sp, src):
    raise NotImplementedError('TODO: implement')

def edit_pair(before, after):
    """Smallest unique line-based (old, new) pair turning `before` into `after`."""
    raise NotImplementedError('TODO: implement')

def first_line(text):
    raise NotImplementedError('TODO: implement')

def finish(run, rng, line1, mode=None, extra=None):
    raise NotImplementedError('TODO: implement')

def pick(rng, lst, idx):
    raise NotImplementedError('TODO: implement')

def distinct(rng, pool, k, avoid_names=...):
    raise NotImplementedError('TODO: implement')

def ls_first(run, rng, files=...):
    """A few ways a model starts: list/glob then read, or read directly."""
    raise NotImplementedError('TODO: implement')

def mk_names(rng, k):
    raise NotImplementedError('TODO: implement')

def setup_new_file(rng, fx, idx, pool, prompts):
    raise NotImplementedError('TODO: implement')

def fam_new_file(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def fam_std_api(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def fam_add_fn(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def diag_code(diag):
    raise NotImplementedError('TODO: implement')

def fam_fix_compile(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def fam_fix_test(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def fam_scaffold(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def fam_rename(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def fam_add_test(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def line_no(text, pred):
    raise NotImplementedError('TODO: implement')

def fam_navigate(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def fam_honesty(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def rowseed(seed, fi, idx, attempt):
    raise NotImplementedError('TODO: implement')

def diverge_mark(chosen, bad):
    raise NotImplementedError('TODO: implement')

def generate_row(seed, fi, idx, attempt, scratch, meter):
    raise NotImplementedError('TODO: implement')

def norm_prompt(s):
    raise NotImplementedError('TODO: implement')

def build(seed, per_family, scratch, meter):
    raise NotImplementedError('TODO: implement')

def _build(seed, per_family, scratch, meter):
    raise NotImplementedError('TODO: implement')

def manifest(rows, dropped, args, path, meter):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
