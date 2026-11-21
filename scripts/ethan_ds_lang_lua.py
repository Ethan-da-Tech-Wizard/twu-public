# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Lua language rows for the Ethan CLI model (ethan-traj.v1, skill 37): execution-verified, policy-gated, honest about not running lua.

The CLI model cannot run lua or luajit (the real gemini-cli policy denies them); it CAN run `make test` when a Makefile exists, read, grep, and
write/replace .lua files (a Makefile write is ASK_USER). So every row teaches writing correct Lua and reporting honestly. At generation time this
script really runs the final repo state with the real interpreters (Lua 5.5.1 and LuaJIT, in a bubblewrap example_host with timeouts, no network)
against a hidden plain-assert harness (exit codes, no test framework), really captures `make test` output and the real `lua: x.lua:N: ...` error
messages with stack tracebacks for the tool results and prompts, and replays every call on a fresh example_host (byte-identical outputs). Every call is
checked against the real PolicyEngine (Oracle from scripts/ethan_ds_policy_skills.py).

Reuses (never copies) example_host/Run/policy oracle from scripts/ethan_ds_trajectories.py.
Usage: python3 -B scripts/ethan_ds_lang_lua.py --out data/autoimprove/20261116/lang/lua_v1.jsonl --seed 1116 --per-family 50
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
import tempfile
from collections import Counter
import ethan_ds_trajectories as T
import ethan_lang_verify as LV

def S(name, desc, src, tests, bug, rt=..., inv=None, ren=None, api=...):
    raise NotImplementedError('TODO: implement')

def _ck(s):
    raise NotImplementedError('TODO: implement')

def CS(name, desc, bad, good, tests, fails_on, api, err_kind):
    raise NotImplementedError('TODO: implement')

def tid(spec):
    raise NotImplementedError('TODO: implement')

def sig_of(spec):
    raise NotImplementedError('TODO: implement')

def module_text(specs):
    raise NotImplementedError('TODO: implement')

def sub_m(expr, mod):
    raise NotImplementedError('TODO: implement')

def check_lines(tests, mod):
    raise NotImplementedError('TODO: implement')

def block_text(mod, specs):
    raise NotImplementedError('TODO: implement')

def tests_text(mods):
    """mods: [(mod, [specs])] -> the project's own tests.lua (plain asserts, exit code, no framework)."""
    raise NotImplementedError('TODO: implement')

def hidden_text(mod, specs):
    raise NotImplementedError('TODO: implement')

def init_text(names):
    raise NotImplementedError('TODO: implement')

def readme_text(proj, names):
    raise NotImplementedError('TODO: implement')

def demo_expr(spec, mod):
    raise NotImplementedError('TODO: implement')

def app_text(mod, spec):
    raise NotImplementedError('TODO: implement')

def apply_mut(src, old, new):
    raise NotImplementedError('TODO: implement')

def bug_spec(spec):
    raise NotImplementedError('TODO: implement')

def inv_spec(spec):
    raise NotImplementedError('TODO: implement')

def syn_break(src, kind):
    raise NotImplementedError('TODO: implement')

def snap_key(files, extra):
    raise NotImplementedError('TODO: implement')

def norm_out(out):
    raise NotImplementedError('TODO: implement')

def run_in_tree(files, argv, timeout=20):
    """Write files ({rel: bytes}) into a fresh temp dir and run argv there inside bubblewrap (read-only /usr, no network, only the dir writable,
    rlimits, timeout). Cached by content. -> (rc, normalised merged output)."""
    raise NotImplementedError('TODO: implement')

def tree_files(d):
    raise NotImplementedError('TODO: implement')

def versions():
    raise NotImplementedError('TODO: implement')

def lua_paths(files):
    raise NotImplementedError('TODO: implement')

def harness(files, hidden, both=False):
    """Real check of a final repo state: luac -p on every .lua file, the project's own tests.lua, then the hidden plain-assert script (exit code). -> (rc, output)."""
    raise NotImplementedError('TODO: implement')

def first_err(out):
    raise NotImplementedError('TODO: implement')

def selfcheck():
    """Catalogue self-test with the real interpreters: every spec passes (warning-free luac -p), every bug fails its test, every runtime-error mutation raises the stated error,
    every invented-API variant fails, every syntax mutation is a syntax error, every compat entry passes on both interpreters and its bad version fails where stated."""
    raise NotImplementedError('TODO: implement')

class Lexample_host(T.example_host):
    """Base example_host plus a real `make test` (the one build command the policy allows); output captured from the real interpreters, normalised."""

    def t_run_shell_command(self, command, **kw):
        raise NotImplementedError('TODO: implement')

class LRun(T.Run):

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

def lverify(sp, messages, fixture, work):
    """-> (ok, detail, asks). Replays all calls on a fresh example_host, then checks policy, final state, the real interpreters and the honesty of the answer."""
    raise NotImplementedError('TODO: implement')

class Meter:

    def __init__(self, enabled=True):
        raise NotImplementedError('TODO: implement')

    def count(self, row):
        raise NotImplementedError('TODO: implement')

    def close(self):
        raise NotImplementedError('TODO: implement')

def pick_spec(rng, pool, avoid=...):
    raise NotImplementedError('TODO: implement')

def make_fixture(fx, proj, mods, makefile=True, both=False, app=None, broken=None, readme=True):
    raise NotImplementedError('TODO: implement')

def rd(fx, rel):
    raise NotImplementedError('TODO: implement')

def edit_pair(before, after):
    """Smallest unique line-based (old, new) pair turning `before` into `after`."""
    raise NotImplementedError('TODO: implement')

def first_line(text):
    raise NotImplementedError('TODO: implement')

def finish(run, rng, line1, mode=None, extra=None):
    raise NotImplementedError('TODO: implement')

def ls_first(run, rng, files=...):
    raise NotImplementedError('TODO: implement')

def with_src(spec, src):
    raise NotImplementedError('TODO: implement')

def rename_spec(spec, old, new):
    raise NotImplementedError('TODO: implement')

def mk_names(rng, k):
    raise NotImplementedError('TODO: implement')

def bgs(rng, k, avoid):
    raise NotImplementedError('TODO: implement')

def jit_safe(spec):
    """True when the spec's module and checks also pass under LuaJIT (decided by really running luajit), so it can be a background module in a compat fixture."""
    raise NotImplementedError('TODO: implement')

def sigtxt(spec):
    raise NotImplementedError('TODO: implement')

def setup_new_file(rng, fx, idx, pool, prompts):
    raise NotImplementedError('TODO: implement')

def fam_new_file(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def fam_std_api(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def fam_add_fn(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def real_error(fx):
    raise NotImplementedError('TODO: implement')

def fam_fix_runtime(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def fam_fix_assert(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def fam_scaffold(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def fam_rename(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def line_no(text, pred):
    raise NotImplementedError('TODO: implement')

def fam_navigate(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def fam_honesty(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def fam_compat(rng, fx, idx):
    raise NotImplementedError('TODO: implement')

def rowseed(seed, fi, idx, attempt):
    raise NotImplementedError('TODO: implement')

def diverge_mark(chosen, bad):
    raise NotImplementedError('TODO: implement')

def generate_row(seed, fi, idx, attempt, scratch, meter):
    raise NotImplementedError('TODO: implement')

def norm_prompt(s):
    raise NotImplementedError('TODO: implement')

def build(seed, per_family, scratch, meter, log=None):
    raise NotImplementedError('TODO: implement')

def _build(seed, per_family, scratch, meter, log=None):
    raise NotImplementedError('TODO: implement')

def pct(vals, q):
    raise NotImplementedError('TODO: implement')

def manifest(rows, dropped, args, path, meter):
    raise NotImplementedError('TODO: implement')

def write_rows(path, rows):
    raise NotImplementedError('TODO: implement')

def archive_if_different(path, new_bytes):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
