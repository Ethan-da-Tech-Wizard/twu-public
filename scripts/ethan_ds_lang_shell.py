# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Bash / POSIX-sh dataset generator for the Ethan CLI LoRA (rows: schema ethan-system-pair.v1, language=shell). Execution-verified, no model calls.

Every row is a CLI trajectory built from the CLI's real tool set and system prompt (ethan_system_pairs.frame/ext_frame): the chosen shell commands
are ALLOWED by the real gemini-cli PolicyEngine (`make test`, grep/sed/awk/sort/... pipelines); script CONTENT arrives through write_file / replace
(edit-tool calls whose old_string was shown by an earlier tool result) and is verified by the example_host, not by the policy.

Modes (one per instance): write (script from spec + hidden harness), bugfix (seeded broken script flagged by shellcheck AND failing tests),
repair (multi-turn: masked flawed first draft -> REAL shellcheck + test output -> replace -> green), pipe (coreutils pipeline with exact expected output).
Verification: `make test` = shellcheck (all severities) + a hidden bash harness (tests/harness.sh over tests/cases/*), run inside bubblewrap
(--unshare-all, --die-with-parent, read-only /usr, only the temp dir writable, timeout, RLIMITs; flags and limits from scripts/ethan_lang_verify.py,
which has no bash language, so its bwrap_works/_limits are imported and the runner is written here). Expected outputs come from Python reference
code, never from the script under test. --reverify re-runs every chosen final state through a SECOND code path (per-case direct execution compared
in Python) and replays all tool calls byte-for-byte; rejected states must fail the tests or have a shellcheck error.

POSIX-sh limit: /usr/bin/dash is absent, so `sh` rows run under `bash --posix` plus `shellcheck -s sh`; dash-only incompatibilities are NOT caught.

  python3 -B scripts/ethan_ds_lang_shell.py [--out-dir DIR] [--seed N] [--per-seed N] [--allow-unexample_hosted]
  python3 -B scripts/ethan_ds_lang_shell.py --reverify [DIR_OR_JSONL]
  python3 -B scripts/ethan_ds_lang_shell.py --selfcheck
"""
import argparse
import hashlib
import itertools
import json
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile
import time
from collections import Counter
from pathlib import Path
import ethan_lang_verify as LV
import ethan_system_pairs as S
import ethan_ds_trajectories as T

class example_hostUnavailable(RuntimeError):
    pass

def example_host_ok():
    raise NotImplementedError('TODO: implement')

def toolchain_ok():
    raise NotImplementedError('TODO: implement')

def toolchain_versions():
    raise NotImplementedError('TODO: implement')

def _norm(text, work):
    raise NotImplementedError('TODO: implement')

def run_in(work, argv, timeout=25, ro=..., tmp=None, merge=True, mem_mb=1024):
    """Run argv with cwd=work inside bubblewrap (work is /work, rw). ro: [(host, dest)] read-only extra binds. tmp: host dir bound at /tmp.
    Returns (rc, output) merged stdout+stderr (rc 124 on timeout). Refuses to run unexample_hosted unless allow_unexample_hosted."""
    raise NotImplementedError('TODO: implement')

class Shexample_host(T.example_host):
    """Gemini-CLI-shaped tool results (read_file/replace/write_file from ethan_ds_trajectories) with run_shell_command executed in bubblewrap."""

    def exec(self, name, args):
        raise NotImplementedError('TODO: implement')

    def t_run_shell_command(self, command, **_):
        raise NotImplementedError('TODO: implement')

def write_tree(root, files):
    raise NotImplementedError('TODO: implement')

def exec_calls(files, calls):
    """Fresh temp dir from `files`, run calls with CLI-shaped tool semantics. Returns (obs, final_files)."""
    raise NotImplementedError('TODO: implement')

def makefile(dialect):
    raise NotImplementedError('TODO: implement')

def C(args=..., stdin=..., files=None, out=..., rc=0, expect=None, absent=..., tmp=False):
    raise NotImplementedError('TODO: implement')

def case_files(cases):
    raise NotImplementedError('TODO: implement')

def shebang(dialect):
    raise NotImplementedError('TODO: implement')

def scaffold(dialect, cases):
    raise NotImplementedError('TODO: implement')

def parse_make(out):
    raise NotImplementedError('TODO: implement')

def analyze(dialect, script, cases):
    """Run shellcheck (all severities and errors-only) and `make test` on a candidate solution.sh. Returns dict."""
    raise NotImplementedError('TODO: implement')

def py_check(dialect, script, cases):
    """Independent second path: run the script once per case in the example_host and compare in Python (no Makefile, no harness.sh). -> (ok, detail)."""
    raise NotImplementedError('TODO: implement')

def _run_case(work, tmp, argv, script_path, stdin_path):
    """One case through `bash -c 'exec "$@" <stdin'` so stdout alone is captured (stderr dropped like the harness)."""
    raise NotImplementedError('TODO: implement')

def K(name, dialect=..., kind=..., **params):
    raise NotImplementedError('TODO: implement')

def P(name, **params):
    raise NotImplementedError('TODO: implement')

def fill(text, p):
    raise NotImplementedError('TODO: implement')

def L_(*xs):
    raise NotImplementedError('TODO: implement')

def pick(r, seq, k):
    raise NotImplementedError('TODO: implement')

def s_slugify(p, r):
    raise NotImplementedError('TODO: implement')

def s_csv_col_sum(p, r):
    raise NotImplementedError('TODO: implement')

def s_word_freq(p, r):
    raise NotImplementedError('TODO: implement')

def s_dedupe(p, r):
    raise NotImplementedError('TODO: implement')

def s_getopts(p, r):
    raise NotImplementedError('TODO: implement')

def s_kv(p, r):
    raise NotImplementedError('TODO: implement')

def s_loglevels(p, r):
    raise NotImplementedError('TODO: implement')

def s_rotate(p, r):
    raise NotImplementedError('TODO: implement')

def s_tmptrap(p, r):
    raise NotImplementedError('TODO: implement')

def s_heredoc(p, r):
    raise NotImplementedError('TODO: implement')

def s_join(p, r):
    raise NotImplementedError('TODO: implement')

def s_param(p, r):
    raise NotImplementedError('TODO: implement')

def s_countargs(p, r):
    raise NotImplementedError('TODO: implement')

def s_grepcount(p, r):
    raise NotImplementedError('TODO: implement')

def s_subsum(p, r):
    raise NotImplementedError('TODO: implement')

def s_nullfind(p, r):
    raise NotImplementedError('TODO: implement')

def s_rename(p, r):
    raise NotImplementedError('TODO: implement')

def s_ext(p, r):
    raise NotImplementedError('TODO: implement')

def s_atomic(p, r):
    raise NotImplementedError('TODO: implement')

def s_number(p, r):
    raise NotImplementedError('TODO: implement')

def s_fizz(p, r):
    raise NotImplementedError('TODO: implement')

def s_trim(p, r):
    raise NotImplementedError('TODO: implement')

def s_minmax(p, r):
    raise NotImplementedError('TODO: implement')

def s_csvrec(p, r):
    raise NotImplementedError('TODO: implement')

def s_greet(p, r):
    raise NotImplementedError('TODO: implement')

def s_case(p, r):
    raise NotImplementedError('TODO: implement')

def s_deps(p, r):
    raise NotImplementedError('TODO: implement')

def s_retry(p, r):
    raise NotImplementedError('TODO: implement')

def s_split(p, r):
    raise NotImplementedError('TODO: implement')

def s_tsv(p, r):
    raise NotImplementedError('TODO: implement')

def s_strip(p, r):
    raise NotImplementedError('TODO: implement')

def s_checksum(p, r):
    raise NotImplementedError('TODO: implement')

def s_ini(p, r):
    raise NotImplementedError('TODO: implement')

def s_base(p, r):
    raise NotImplementedError('TODO: implement')

def s_port(p, r):
    raise NotImplementedError('TODO: implement')

def s_csvfilter(p, r):
    raise NotImplementedError('TODO: implement')

def s_longest(p, r):
    raise NotImplementedError('TODO: implement')

def s_uniqci(p, r):
    raise NotImplementedError('TODO: implement')

def s_tpl(p, r):
    raise NotImplementedError('TODO: implement')

def s_assoc(p, r):
    raise NotImplementedError('TODO: implement')

def s_traprc(p, r):
    raise NotImplementedError('TODO: implement')

def s_table(p, r):
    raise NotImplementedError('TODO: implement')

def s_leap(p, r):
    raise NotImplementedError('TODO: implement')

def s_gcd(p, r):
    raise NotImplementedError('TODO: implement')

def s_revwords(p, r):
    raise NotImplementedError('TODO: implement')

def s_sumargs(p, r):
    raise NotImplementedError('TODO: implement')

def s_newest(p, r):
    raise NotImplementedError('TODO: implement')

def s_optslong(p, r):
    raise NotImplementedError('TODO: implement')

def s_chars(p, r):
    raise NotImplementedError('TODO: implement')

def s_pairjoin(p, r):
    raise NotImplementedError('TODO: implement')

def s_wcb(p, r):
    raise NotImplementedError('TODO: implement')

def uc(items):
    """uniq -c rendering: 7-wide counts."""
    raise NotImplementedError('TODO: implement')

def p_count_level(p, r):
    raise NotImplementedError('TODO: implement')

def p_top_words(p, r):
    raise NotImplementedError('TODO: implement')

def p_sum_column(p, r):
    raise NotImplementedError('TODO: implement')

def p_dedupe(p, r):
    raise NotImplementedError('TODO: implement')

def p_dups(p, r):
    raise NotImplementedError('TODO: implement')

def p_cut(p, r):
    raise NotImplementedError('TODO: implement')

def p_find(p, r):
    raise NotImplementedError('TODO: implement')

def p_xargs(p, r):
    raise NotImplementedError('TODO: implement')

def p_squeeze(p, r):
    raise NotImplementedError('TODO: implement')

def p_sedrange(p, r):
    raise NotImplementedError('TODO: implement')

def p_group(p, r):
    raise NotImplementedError('TODO: implement')

def p_sedsubst(p, r):
    raise NotImplementedError('TODO: implement')

def p_strip(p, r):
    raise NotImplementedError('TODO: implement')

def p_sortnum(p, r):
    raise NotImplementedError('TODO: implement')

def p_headtail(p, r):
    raise NotImplementedError('TODO: implement')

def p_topips(p, r):
    raise NotImplementedError('TODO: implement')

def p_vsort(p, r):
    raise NotImplementedError('TODO: implement')

def p_cuniq(p, r):
    raise NotImplementedError('TODO: implement')

def p_matchlines(p, r):
    raise NotImplementedError('TODO: implement')

def lc_first(s):
    raise NotImplementedError('TODO: implement')

def make_task(rng, mode, inst, i):
    raise NotImplementedError('TODO: implement')

def apply_muts(body, muts):
    """Return [(old,new,bad_body)] for each mutation that applies exactly once."""
    raise NotImplementedError('TODO: implement')

def diff_edit(bad, good):
    """Smallest contiguous (old, new) such that bad.replace(old, new, 1) == good and old occurs exactly once in bad."""
    raise NotImplementedError('TODO: implement')

def rd(path):
    raise NotImplementedError('TODO: implement')

def instances(seed, per_seed, rseed):
    raise NotImplementedError('TODO: implement')

def plan_instance(seed, p, idx, rseed):
    """Build one plan (no example_host yet) or raise."""
    raise NotImplementedError('TODO: implement')

def choose_mode(inst, idx, bad_info):
    raise NotImplementedError('TODO: implement')

def survey_bad(inst):
    """Try each mutation; keep those that fail the tests (and note which are also flagged by shellcheck)."""
    raise NotImplementedError('TODO: implement')

def finalize_text_ok(rng, inst, n):
    raise NotImplementedError('TODO: implement')

def build_script_row(inst, mode, idx, rseed, bad_info):
    raise NotImplementedError('TODO: implement')

def build_pipe_row(inst, idx, rseed):
    raise NotImplementedError('TODO: implement')

def pipe_final(rng, cmd, out):
    raise NotImplementedError('TODO: implement')

def plan_calls_for_policy(plans):
    raise NotImplementedError('TODO: implement')

def trajectory(calls, obs, final, masked):
    raise NotImplementedError('TODO: implement')

def policy_for(calls):
    raise NotImplementedError('TODO: implement')

def verify_chosen(pl, obs, final_files, inst, final_text):
    """Chosen must satisfy its checker. Returns (ok, detail)."""
    raise NotImplementedError('TODO: implement')

def verify_rejected(pl, robs, rfiles, inst):
    """Rejected must really fail. Returns (ok, kind)."""
    raise NotImplementedError('TODO: implement')

def row_from(inst, pl, mode_idx, seed, task, tpl, obs, robs, final, rfinal, rkind, dec, split_unused=None):
    raise NotImplementedError('TODO: implement')

def ngrams8(text, n=8):
    raise NotImplementedError('TODO: implement')

def near_dup_report(tasks, thr=0.85):
    raise NotImplementedError('TODO: implement')

def build_rows(seed=..., per_seed=5, only=None, log=...):
    raise NotImplementedError('TODO: implement')

def write_outputs(rows, info, out_dir, seed, per_seed):
    raise NotImplementedError('TODO: implement')

def reverify(path):
    raise NotImplementedError('TODO: implement')

def cases_from_files(files):
    """Rebuild the case list from a stored fixture (tests/cases/NN/...)."""
    raise NotImplementedError('TODO: implement')

def selfcheck(only=None, per_seed=5, seed=...):
    """Every instance: good passes (shellcheck clean + tests) and has >=1 failing mutation; pipe good output equals the Python reference."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
