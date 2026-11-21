# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Java (skill 35) language rows for the Ethan CLI model (ethan-traj.v1), execution-verified with the real JDK and Maven.

The CLI model cannot run javac, java or mvn (the real gemini-cli policy denies every compiler and build tool), so rows teach WRITING
CORRECT JAVA: new files with package wiring, minimal replaces, fixes from a pasted REAL javac diagnostic, fixes from a recorded failing
test run, standard-library tasks, Maven scaffolds, renames, navigation and honest "not compiled here" answers. The GENERATOR compiles
and runs the final repo state of every kept row (javac -Xlint:all -Werror --release 21 plus a hidden assertion harness with a main and
exit codes; scaffold rows additionally run `mvn -o test` against a COPY of the offline Maven cache).

Underlying tasks: every row carries task_id = "java:<module>:<method>" (the bank entry); rows of one task share it (max 8 per task).
No network, no model calls. Deterministic from --seed. Run heavy work through scripts/ethan_capped_run.sh (default slot gate):
  ETHAN_CAP=3G scripts/ethan_capped_run.sh /usr/bin/python3 -B scripts/ethan_ds_lang_java.py --out data/autoimprove/20261116/lang/java_v1.jsonl --seed 1116 --per-family 48
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

def S(mod, sig, use, body, desc, ex, tests, bugs=..., hint=..., hre=..., vis=3):
    raise NotImplementedError('TODO: implement')

def is_scalar(spec):
    raise NotImplementedError('TODO: implement')

def pkg_of(proj):
    raise NotImplementedError('TODO: implement')

def pkgdir(proj):
    raise NotImplementedError('TODO: implement')

def src_path(proj, cls):
    raise NotImplementedError('TODO: implement')

def test_path(proj):
    raise NotImplementedError('TODO: implement')

def junit_path(proj, cls):
    raise NotImplementedError('TODO: implement')

def makefile(proj):
    raise NotImplementedError('TODO: implement')

def pom(proj):
    raise NotImplementedError('TODO: implement')

def imports_for(specs):
    raise NotImplementedError('TODO: implement')

def method_text(spec, body=None):
    raise NotImplementedError('TODO: implement')

def class_file(proj, cls, specs, bodies=None, marker=True, imports=None):
    raise NotImplementedError('TODO: implement')

def sub_tests(spec, cls, name=None):
    raise NotImplementedError('TODO: implement')

def test_lines(spec, cls, name=None, lo=0, hi=None):
    raise NotImplementedError('TODO: implement')

def harness(proj, mod, items, extra_lines=...):
    """Assertion harness with a main and an exit code. items = list of (spec, cls, name, lo, hi)."""
    raise NotImplementedError('TODO: implement')

def mini_harness(proj, cls, spec, n=3, name=None):
    """Compact scaffold harness (scalar specs only): what a model would write for a fresh Makefile project."""
    raise NotImplementedError('TODO: implement')

def junit_test(proj, cls, spec, n=3):
    raise NotImplementedError('TODO: implement')

def jenv():
    raise NotImplementedError('TODO: implement')

def sh(argv, cwd, timeout=240):
    raise NotImplementedError('TODO: implement')

def key_of(*parts):
    raise NotImplementedError('TODO: implement')

def cached(kind, key, fn):
    raise NotImplementedError('TODO: implement')

def write_tree(root, files):
    raise NotImplementedError('TODO: implement')

def javac_run(files, run=True, mains_only=True):
    """Real javac (-Xlint:all -Werror --release 21) of src/main plus the hidden Checks, then `java` on Checks. -> {compiled, compile_out, rc, out}.
    JUnit test sources (not compilable without the Maven classpath) are skipped here; scaffold rows get a real `mvn -o test` as well."""
    raise NotImplementedError('TODO: implement')

def ensure_m2():
    raise NotImplementedError('TODO: implement')

def mvn_test(files):
    """Real `mvn -o -q test` against the COPY of the offline cache, in a throwaway dir. -> {rc, out}."""
    raise NotImplementedError('TODO: implement')

def make_test(files):
    """Real `make test` in a throwaway copy; returns (rc, stdout)."""
    raise NotImplementedError('TODO: implement')

def tool_versions():
    raise NotImplementedError('TODO: implement')

def app_files(proj, rng, mod, makefile_on=True, readme_extra=...):
    raise NotImplementedError('TODO: implement')

def selftest(verbose=False):
    """Every spec: reference passes its full hidden harness; every bug compiles and FAILS the harness."""
    raise NotImplementedError('TODO: implement')

class JBox(T.example_host):
    """The shared example_host plus a real `make test` (the policy allows it; the generator really runs javac+java in a throwaway copy)."""

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
    """Deliberately wrong implementations used by rejected sides (real compile errors)."""
    raise NotImplementedError('TODO: implement')

def pick_spec(rng, pool):
    """Least-used task first (ties broken by the row rng), so no task exceeds MAX_PER_TASK and the bank is used evenly."""
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

def paths(proj, cls):
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

def nav_files(rng, idx, focus):
    raise NotImplementedError('TODO: implement')

def case_navigate(rng, idx):
    raise NotImplementedError('TODO: implement')

def case_honesty(rng, idx):
    raise NotImplementedError('TODO: implement')

def norm_call(c):
    raise NotImplementedError('TODO: implement')

def policy_report(calls):
    """-> (ok, ask_user_count, reason). Real gemini-cli PolicyEngine decisions; ask_user is acceptable only for build-config files (pom.xml, Makefile)."""
    raise NotImplementedError('TODO: implement')

def _fixture(files, tag):
    raise NotImplementedError('TODO: implement')

def gen_row(seed, fam, idx, attempt, want_reject=None):
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

def pct(vals, q):
    raise NotImplementedError('TODO: implement')

def manifest(rows, dropped, missing, toks, checked, args, path):
    raise NotImplementedError('TODO: implement')

def archive_existing(out):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
