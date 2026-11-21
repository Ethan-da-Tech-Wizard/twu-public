# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Deterministic, compiler-verified C++ tool trajectories for the Ethan CLI model (ethan-traj.v1, skill 32).

The CLI model cannot run g++/cmake/binaries (the real gemini-cli policy denies them); it can write/replace sources, run `make test`
when a Makefile exists, and read. So every row teaches WRITING CORRECT C++ and honest reporting, and THIS generator proves each row at
generation time with the real toolchain (g++ -std=c++20 -Wall -Wextra -Werror -O0, cmake + make + ctest), outside the model's tool path:
  * the FINAL repo state of every kept row compiles and passes a hidden harness (or the project's own `make test` / ctest);
  * broken diagnostics pasted into prompts are produced by the real compiler on the real broken file;
  * `make test` results shown to the model are the real make output of the fixture (run on a throwaway copy);
  * every tool call is checked by the REAL gemini-cli PolicyEngine (Oracle of ethan_ds_policy_skills): allow, or ask_user only for
    build-config files (Makefile, CMakeLists.txt), which are counted;
  * about 30% of rows carry a `rejected` side from a deterministic wrong policy that FAILS the same verifier.
No network, no model, no GPU. Usage:
  ETHAN_CAP=3G scripts/ethan_capped_run.sh /usr/bin/python3 -B scripts/ethan_ds_lang_cpp.py --out data/autoimprove/20261116/lang/cpp_v1.jsonl --seed 1116 --per-family 48
"""
import argparse
import difflib
import hashlib
import json
import os
import random
import re
import resource
import shutil
import subprocess
import sys
import ethan_ds_trajectories as T

def includes_for(*texts, extra=...):
    raise NotImplementedError('TODO: implement')

def fn_decl(e, n):
    raise NotImplementedError('TODO: implement')

def fn_impl(e, n):
    raise NotImplementedError('TODO: implement')

def buggy_body(e):
    raise NotImplementedError('TODO: implement')

def fn_impl_bug(e, n):
    raise NotImplementedError('TODO: implement')

def mod_header(proj, decls, hdr_inc):
    raise NotImplementedError('TODO: implement')

def mod_source(proj, mod, impls, cpp_inc):
    raise NotImplementedError('TODO: implement')

def test_source(hdr, proj, items, std=..., path=...):
    """items: list of C++ statements (already complete lines). Plain bool expressions are wrapped by callers via check()."""
    raise NotImplementedError('TODO: implement')

def fn_checks(e, n, k=None):
    raise NotImplementedError('TODO: implement')

def type_checks(e, t, k=None):
    raise NotImplementedError('TODO: implement')

def makefile_one(mod, srcs=True):
    raise NotImplementedError('TODO: implement')

def cmake_text(proj, mod):
    raise NotImplementedError('TODO: implement')

def _limits():
    raise NotImplementedError('TODO: implement')

def _run(argv, cwd, timeout=120):
    raise NotImplementedError('TODO: implement')

def tree_files(root):
    raise NotImplementedError('TODO: implement')

def tree_key(files, *extra):
    raise NotImplementedError('TODO: implement')

def _tmpdir(tag):
    raise NotImplementedError('TODO: implement')

def run_make(root):
    """`make test` on a throwaway copy of root (never pollutes the example_host). Returns (output with example_host paths hidden, rc)."""
    raise NotImplementedError('TODO: implement')

def run_cmake(root):
    """Real `cmake -S . -B build`, `cmake --build build`, `ctest` on a copy. Returns (ok, detail)."""
    raise NotImplementedError('TODO: implement')

def run_harness(root, srcs, harness_text, inc_dirs=..., tag=...):
    """Compile harness_text (a main) with srcs from root under the strict flags and run it. Returns (ok, detail)."""
    raise NotImplementedError('TODO: implement')

class Cppexample_host(T.example_host):
    """The shared example_host plus a real `make test` (the one build command the policy allows); compilers and binaries stay denied."""

    def t_run_shell_command(self, command, **_):
        raise NotImplementedError('TODO: implement')

def build_cfg_path(args):
    raise NotImplementedError('TODO: implement')

def policy_check(calls, counter):
    """Real PolicyEngine decisions. allow passes; ask_user passes only for build-config write/replace (counted). In the collect pass everything passes."""
    raise NotImplementedError('TODO: implement')

def verify_cpp(sp, messages, fixture, work, counter=None):
    """Replay on a fresh example_host, then check policy, minimal diff, protected files, compile+hidden harness and honest wording."""
    raise NotImplementedError('TODO: implement')

def wr(fx, rel, text):
    raise NotImplementedError('TODO: implement')

def rd(fx, rel):
    raise NotImplementedError('TODO: implement')

def balanced_call(test, name_marker=...):
    """The `@N(...)` call text of a test expression, e.g. '@N({1, 2}, 3)'."""
    raise NotImplementedError('TODO: implement')

def first_diff(old, new):
    """First differing line pair (stripped) of an old->new edit, for 'Changed `a` to `b`' style answers."""
    raise NotImplementedError('TODO: implement')

def change_line(o, n):
    raise NotImplementedError('TODO: implement')

def last_line(out):
    raise NotImplementedError('TODO: implement')

def cap(s, n=190):
    raise NotImplementedError('TODO: implement')

def names(rng):
    raise NotImplementedError('TODO: implement')

def pick_fn(rng, key=None, with_bug=False, n_names=2):
    raise NotImplementedError('TODO: implement')

def module_project(fx, proj, mod, items, vis=2, app=None, readme=False, sloppy_inc=True, wild=False):
    """items: [(entry, name, buggy)]. Writes Makefile, src/mod.hpp/.cpp, tests/test_mod.cpp (+ src/main.cpp when app=(entry, name, call))."""
    raise NotImplementedError('TODO: implement')

def harness_for(hdr, proj, items, std=...):
    raise NotImplementedError('TODO: implement')

def check_make(root):
    raise NotImplementedError('TODO: implement')

def phrase(rng, templates, idx, **kw):
    raise NotImplementedError('TODO: implement')

def honest_line(rng):
    raise NotImplementedError('TODO: implement')

def s_newmod(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def p_newmod(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s_addfn(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def p_addfn(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def err_files(fx, proj, mod, sc, n):
    raise NotImplementedError('TODO: implement')

def s_fixerr(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def p_fixerr(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s_failtest(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def p_failtest(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def std_header(proj, e, name, body=None):
    raise NotImplementedError('TODO: implement')

def std_sig(e, name):
    raise NotImplementedError('TODO: implement')

def std_checks(e, name, k=None):
    raise NotImplementedError('TODO: implement')

def s_stdapi(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def p_stdapi(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s_scaffold(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def p_scaffold(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s_rename(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def p_rename(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s_locate(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def p_locate(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s_honest(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def p_honest(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s_apierr(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def p_apierr(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def load_cache():
    raise NotImplementedError('TODO: implement')

def save_cache():
    raise NotImplementedError('TODO: implement')

def bank_ids():
    raise NotImplementedError('TODO: implement')

def toolchain():
    raise NotImplementedError('TODO: implement')

def token_len(messages):
    """Length under the Qwen3.5 chat template (system prompt included); None when the tokenizer is unavailable."""
    raise NotImplementedError('TODO: implement')

def rowseed(seed, fi, idx, attempt):
    raise NotImplementedError('TODO: implement')

def generate_row(seed, fi, idx, attempt, scratch, counter, want_reject=None):
    raise NotImplementedError('TODO: implement')

def _build(seed, per_family, scratch, counter):
    raise NotImplementedError('TODO: implement')

def build(seed, per_family, scratch):
    """Pass 1 collects every tool call and asks the real policy engine once in a batch; pass 2 rebuilds with the real decisions."""
    raise NotImplementedError('TODO: implement')

def manifest(rows, dropped, counter, args, path):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
