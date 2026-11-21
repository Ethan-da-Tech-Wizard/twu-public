# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""C# (skill 34) language rows for the Ethan CLI model (ethan-traj.v1), execution-verified with the real dotnet SDK.

The CLI model cannot run dotnet (the real gemini-cli policy denies every compiler), so rows teach WRITING CORRECT C#:
new files, minimal replaces, fixes from a pasted REAL Roslyn diagnostic, fixes from a recorded failing test run, stdlib usage,
project scaffolds, renames and honest "not compiled here" answers. The GENERATOR compiles and runs the final repo state of every
kept row (Roslyn csc for speed, `dotnet build` / `make test` for diagnostics and scaffolds) against a hidden console harness.

No network, no model calls. Deterministic from --seed. Run heavy work through scripts/ethan_capped_run.sh.
  ETHAN_CAP=3G scripts/ethan_capped_run.sh /usr/bin/python3 -B scripts/ethan_ds_lang_csharp.py --out data/autoimprove/20261116/lang/csharp_v1.jsonl --seed 1116 --per-family 48
"""
import argparse
import collections
import difflib
import hashlib
import json
import os
import random
import re
import shutil
import subprocess
import sys
import ethan_ds_trajectories as T

def ind(text, n):
    raise NotImplementedError('TODO: implement')

def S(mod, sig, use, body, desc, ex, tests, bugs=..., hint=..., hre=..., nullmut=..., vis=3):
    raise NotImplementedError('TODO: implement')

def is_scalar(spec):
    raise NotImplementedError('TODO: implement')

def csproj(proj):
    raise NotImplementedError('TODO: implement')

def makefile(proj):
    raise NotImplementedError('TODO: implement')

def usings_for(specs):
    raise NotImplementedError('TODO: implement')

def method_text(spec, body=None):
    raise NotImplementedError('TODO: implement')

def class_file(proj, cls, specs, bodies=None, marker=True, usings=None):
    raise NotImplementedError('TODO: implement')

def sub_tests(spec, cls, name=None):
    raise NotImplementedError('TODO: implement')

def test_lines(spec, cls, name=None, lo=0, hi=None):
    raise NotImplementedError('TODO: implement')

def harness(proj, mod, items, extra_lines=..., wired=None):
    """Console Main harness. items = list of (spec, cls, name, lo, hi)."""
    raise NotImplementedError('TODO: implement')

def mini_harness(proj, cls, spec, n=3, name=None):
    """Compact scaffold harness (scalar specs only): what a model would write for a fresh project."""
    raise NotImplementedError('TODO: implement')

def dn_env():
    raise NotImplementedError('TODO: implement')

def sh(argv, cwd, timeout=240):
    raise NotImplementedError('TODO: implement')

def key_of(*parts):
    raise NotImplementedError('TODO: implement')

def cached(kind, key, fn):
    raise NotImplementedError('TODO: implement')

def write_tree(root, files):
    raise NotImplementedError('TODO: implement')

def csc_run(files, run=True):
    """Real Roslyn (csc.dll from the SDK) with nullable on and warnings as errors, then `dotnet out.dll`. Returns {compiled, compile_out, rc, out}."""
    raise NotImplementedError('TODO: implement')

def dotnet_build(files):
    """Real `dotnet build` (offline: NuGet sources cleared, ref pack from the SDK). Returns {rc, out} with paths mapped to DISPLAY_ROOT."""
    raise NotImplementedError('TODO: implement')

def make_test(files):
    """Real `make test` in a throwaway copy; returns (rc, stdout) with paths mapped to DISPLAY_ROOT."""
    raise NotImplementedError('TODO: implement')

def diag_lines(out, kinds=...):
    raise NotImplementedError('TODO: implement')

def tool_versions():
    raise NotImplementedError('TODO: implement')

def app_files(proj, rng, mod, makefile_on=True, readme_extra=...):
    raise NotImplementedError('TODO: implement')

def selftest(verbose=False):
    """Every spec: reference passes its full hidden harness; every bug compiles and FAILS the harness; null mutants raise CS86xx."""
    raise NotImplementedError('TODO: implement')

class CSBox(T.example_host):
    """The shared example_host plus a real `make test` (the policy allows it; the generator really runs dotnet in a throwaway copy)."""

    def t_run_shell_command(self, command, **kw):
        raise NotImplementedError('TODO: implement')

def lead(i):
    raise NotImplementedError('TODO: implement')

def hon(i):
    raise NotImplementedError('TODO: implement')

def final_claims(text):
    raise NotImplementedError('TODO: implement')

def split_params(params):
    raise NotImplementedError('TODO: implement')

def param_names(params):
    raise NotImplementedError('TODO: implement')

def lineno(text, sub):
    raise NotImplementedError('TODO: implement')

def two_part_diff(old, new):
    """Minimal (old_string, new_string) pair that turns `old` into `new` (single contiguous change plus one anchor line for pure inserts)."""
    raise NotImplementedError('TODO: implement')

def spec_variant(spec, body=None, sig=None):
    raise NotImplementedError('TODO: implement')

def bad_variant(spec, mode, rng):
    """Deliberately wrong implementations used by rejected sides (real compile errors / failing harness)."""
    raise NotImplementedError('TODO: implement')

def pick(rng, seq):
    raise NotImplementedError('TODO: implement')

def tpl(options, idx, **kw):
    raise NotImplementedError('TODO: implement')

def new_files_state(snap):
    raise NotImplementedError('TODO: implement')

def evidence_text(calls):
    raise NotImplementedError('TODO: implement')

def verify_row(sp, messages, files, tag, prompt=...):
    """Replay on a fresh example_host, check the final state against the spec, compile + run the hidden harness. -> (ok, detail)."""
    raise NotImplementedError('TODO: implement')

def hid(proj, mod, items, extra=...):
    raise NotImplementedError('TODO: implement')

def sig_range_call(run, path, text, sig, extra_lines=2):
    raise NotImplementedError('TODO: implement')

def case_new_file(rng, idx):
    raise NotImplementedError('TODO: implement')

def case_add_method(rng, idx):
    raise NotImplementedError('TODO: implement')

def compile_mutants(spec, rng):
    raise NotImplementedError('TODO: implement')

def case_fix_compile(rng, idx):
    raise NotImplementedError('TODO: implement')

def case_fix_test(rng, idx):
    raise NotImplementedError('TODO: implement')

def case_stdlib(rng, idx):
    raise NotImplementedError('TODO: implement')

def case_scaffold(rng, idx):
    raise NotImplementedError('TODO: implement')

def service_file(proj, cls, spec):
    raise NotImplementedError('TODO: implement')

def case_rename(rng, idx):
    raise NotImplementedError('TODO: implement')

def nav_files(rng, idx):
    raise NotImplementedError('TODO: implement')

def case_navigate(rng, idx):
    raise NotImplementedError('TODO: implement')

def case_honesty(rng, idx):
    raise NotImplementedError('TODO: implement')

def norm_call(c):
    raise NotImplementedError('TODO: implement')

def policy_report(calls):
    """-> (ok, ask_user_count, reason). Real gemini-cli PolicyEngine decisions; ask_user is acceptable only for build-config files."""
    raise NotImplementedError('TODO: implement')

def gen_row(seed, fam, idx, attempt, want_reject=None):
    raise NotImplementedError('TODO: implement')

def _fixture(files, tag):
    raise NotImplementedError('TODO: implement')

def est_tokens(row):
    raise NotImplementedError('TODO: implement')

def build(seed, per_family, families=None, log=..., skip=None):
    raise NotImplementedError('TODO: implement')

def token_counts_inproc(rows):
    raise NotImplementedError('TODO: implement')

def token_counts(rows):
    """Real tokenizer through the train312 venv (the system python has no transformers). Returns None when unavailable."""
    raise NotImplementedError('TODO: implement')

def build_checked(seed, per_family, families=None, log=...):
    """build() plus a real-tokenizer pass: rows above MAX_TOKENS are regenerated with the next attempt (never truncated)."""
    raise NotImplementedError('TODO: implement')

def opener(text):
    raise NotImplementedError('TODO: implement')

def manifest(rows, dropped, missing, toks, checked, args, path):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
