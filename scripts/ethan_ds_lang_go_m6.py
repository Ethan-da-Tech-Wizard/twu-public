# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Go language rows for the Ethan CLI model (ethan-traj.v1, skill 36): execution-verified, policy-gated, honest about not compiling.

The CLI model cannot run `go` (the real gemini-cli policy denies it); it CAN run `make test` when a Makefile exists, read, grep, and
write/replace .go sources (go.mod and Makefile writes are ASK_USER). So every row teaches writing correct Go and reporting honestly.
At generation time this script really builds the final repo state with the REAL toolchain /usr/lib/go/bin/go (never the `go` on PATH),
std-only modules, GOTOOLCHAIN=local GOPROXY=off, `go build` + `go vet` + `go test` against a table-driven HIDDEN harness, captures
real `go build` diagnostics and real `make test` output for the tool results, replays every call on a fresh example_host (byte-identical),
and checks every call against the real PolicyEngine (Oracle from scripts/ethan_ds_policy_skills.py).

Reuses (never copies) example_host/Run/policy oracle from scripts/ethan_ds_trajectories.py.
Usage: ETHAN_CAP=3G scripts/ethan_capped_run.sh python3 -B scripts/ethan_ds_lang_go_m6.py --out data/autoimprove/20261116/lang/go_m6_s1116.jsonl --seed 1116 --per-family 48
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
import ethan_ds_trajectories as T

def tabs(s):
    raise NotImplementedError('TODO: implement')

def S(x):
    """Go string literal for an ASCII Python string (JSON escapes are valid Go escapes here)."""
    raise NotImplementedError('TODO: implement')

def tool_env():
    raise NotImplementedError('TODO: implement')

def gofmt(text):
    raise NotImplementedError('TODO: implement')

def fmt_src(src):
    """gofmt a declaration-only snippet (no package clause)."""
    raise NotImplementedError('TODO: implement')

def auto_imports(code):
    raise NotImplementedError('TODO: implement')

def import_block(paths):
    raise NotImplementedError('TODO: implement')

def split_top(s):
    raise NotImplementedError('TODO: implement')

def parse_sig(sig):
    raise NotImplementedError('TODO: implement')

def SP(name, sig, desc, src, cases=None, raw=None, rdr=..., ren=None, bug=None, inv=None, api=..., typ=False, tuses=...):
    """name: Go identifier; sig: shown signature; src: Go declarations (4-space indent); cases: [(arg exprs, want expr | None for error)]; raw: hand-written test funcs;
    rdr: names of io.Reader params tested through strings.NewReader; bug: (old, new) that compiles but fails the tests; inv: (old, new) invented API (compile error)."""
    raise NotImplementedError('TODO: implement')

def first_func_line(src):
    raise NotImplementedError('TODO: implement')

def mutate(sp, kind):
    """-> broken src text and extra imports for `kind`, or None when it does not apply."""
    raise NotImplementedError('TODO: implement')

def ce_entries():
    raise NotImplementedError('TODO: implement')

def module_text(pkg, specs, extra_imports=..., src_override=None):
    raise NotImplementedError('TODO: implement')

def zero_lit(rt):
    raise NotImplementedError('TODO: implement')

def vb(t):
    raise NotImplementedError('TODO: implement')

def table_func(sp, fname, cases, mod_pkg_main=False):
    raise NotImplementedError('TODO: implement')

def test_funcs(sp, prefix=..., ncases=None):
    raise NotImplementedError('TODO: implement')

def test_text(pkg, specs, prefix=..., ncases=None):
    raise NotImplementedError('TODO: implement')

def w(fx, rel, text):
    raise NotImplementedError('TODO: implement')

def rd(fx, rel):
    raise NotImplementedError('TODO: implement')

def make_fixture(fx, pkg, mods, makefile=True, readme=True, extra_files=None, nunit=2):
    """mods: [(modname, specs, unit)]"""
    raise NotImplementedError('TODO: implement')

def buggy_src(sp):
    raise NotImplementedError('TODO: implement')

def inv_src(sp):
    raise NotImplementedError('TODO: implement')

def wrong_sig_src(sp):
    raise NotImplementedError('TODO: implement')

def with_src(sp, src):
    raise NotImplementedError('TODO: implement')

def snap_key(files, extra):
    raise NotImplementedError('TODO: implement')

def norm_out(out, root=None):
    raise NotImplementedError('TODO: implement')

def disk_cache_path(key):
    raise NotImplementedError('TODO: implement')

def run_in_tree(files, argv, timeout=150):
    """Write `files` ({rel: bytes}) into a fresh temp dir, run argv there with the REAL toolchain. Cached by content (memory + disk). -> (rc, normalised output)."""
    raise NotImplementedError('TODO: implement')

def tree_files(d):
    raise NotImplementedError('TODO: implement')

def go_build_diag(files):
    raise NotImplementedError('TODO: implement')

def versions():
    raise NotImplementedError('TODO: implement')

def _go_version():
    raise NotImplementedError('TODO: implement')

def harness_argv():
    raise NotImplementedError('TODO: implement')

def harness(files, hidden, run_test=None):
    raise NotImplementedError('TODO: implement')

def selfcheck():
    """Catalogue self-test: every spec is gofmt-clean, builds, vets and passes; bug fails to pass but compiles; inv fails to compile; every CE breaks as stated."""
    raise NotImplementedError('TODO: implement')

def ce_broken(sp, ce, pkg):
    raise NotImplementedError('TODO: implement')

class Gexample_host(T.example_host):
    """Base example_host plus a real `make test` (the one build command the policy allows); output captured from the real toolchain, normalised."""

    def t_run_shell_command(self, command, **kw):
        raise NotImplementedError('TODO: implement')

class GRun(T.Run):

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

def gverify(sp, messages, fixture, work):
    """-> (ok, detail, asks). Replays all calls on a fresh example_host, then checks policy, final state, real build/harness and the honesty of the answer."""
    raise NotImplementedError('TODO: implement')

class Meter:

    def __init__(self, enabled=True):
        raise NotImplementedError('TODO: implement')

    def count(self, row):
        raise NotImplementedError('TODO: implement')

    def close(self):
        raise NotImplementedError('TODO: implement')

def edit_pair(before, after):
    """Smallest unique line-based (old, new) pair that turns `before` into `after` (both non-empty, with at least one context line for pure inserts/deletes)."""
    raise NotImplementedError('TODO: implement')

def first_line(text):
    raise NotImplementedError('TODO: implement')

def finish(run, rng, line1, mode=None, extra=None):
    raise NotImplementedError('TODO: implement')

def ls_first(run, rng, files=...):
    raise NotImplementedError('TODO: implement')

class Ctx:

    def __init__(self, seed, fname, idx, attempt, rng):
        raise NotImplementedError('TODO: implement')

    def pick(self, pool, tag=...):
        raise NotImplementedError('TODO: implement')

def names(rng, k):
    raise NotImplementedError('TODO: implement')

def short_others(rng, exclude, k, limit=300, need=...):
    raise NotImplementedError('TODO: implement')

def setup_new_file(ctx, fx, pool, prompts, family):
    raise NotImplementedError('TODO: implement')

def fam_new_file(ctx, fx):
    raise NotImplementedError('TODO: implement')

def fam_std_api(ctx, fx):
    raise NotImplementedError('TODO: implement')

def split_header(text):
    raise NotImplementedError('TODO: implement')

def fam_add_fn(ctx, fx):
    raise NotImplementedError('TODO: implement')

def fam_fix_compile(ctx, fx):
    raise NotImplementedError('TODO: implement')

def fam_fix_test(ctx, fx):
    raise NotImplementedError('TODO: implement')

def fam_scaffold(ctx, fx):
    raise NotImplementedError('TODO: implement')

def fam_rename(ctx, fx):
    raise NotImplementedError('TODO: implement')

def fam_add_test(ctx, fx):
    raise NotImplementedError('TODO: implement')

def line_no(text, pred):
    raise NotImplementedError('TODO: implement')

def fam_navigate(ctx, fx):
    raise NotImplementedError('TODO: implement')

def fam_honesty(ctx, fx):
    raise NotImplementedError('TODO: implement')

def rowseed(seed, fi, idx, attempt):
    raise NotImplementedError('TODO: implement')

def diverge_mark(chosen, bad):
    raise NotImplementedError('TODO: implement')

def generate_row(seed, fi, idx, attempt, scratch, meter):
    raise NotImplementedError('TODO: implement')

def norm_prompt(s):
    raise NotImplementedError('TODO: implement')

def build(seed, per_family, scratch, meter, progress=None):
    raise NotImplementedError('TODO: implement')

def _build(seed, per_family, scratch, meter, progress=None):
    raise NotImplementedError('TODO: implement')

def pctl(xs, p):
    raise NotImplementedError('TODO: implement')

def manifest(rows, dropped, args, path, meter):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
