# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Ethan dataset builder: shell scripting in bash (skill 39), schema ethan-traj.v1.

The CLI model cannot run scripts here (the real gemini-cli PolicyEngine DENIES `bash x.sh`, `./x.sh`, `sh x.sh`, `bash -n`, `shellcheck`;
it ALLOWS write_file/replace on .sh files, read-only inspection and `chmod +x`). So rows teach WRITING and FIXING correct bash with honest
"not run here" answers, while THIS GENERATOR verifies every kept row with the real toolchain:

  * the model's final script (from the example_host snapshot) is run by the real bash 5.3 in a throwaway cwd-confined directory (bubblewrap:
    read-only root, no network, fresh /dev and /proc, scrubbed environment, 10 s timeout) against fixture and hidden inputs; stdout,
    exit code, created/changed/deleted files, directories, modes and leftover temp files are compared with expected values computed
    in Python, independently of the script;
  * `bash -n` and `shellcheck` (JSON) are run on it: error and warning findings FAIL the row; info/style findings are allowed only for the
    codes listed in ALLOWED_STYLE (recorded in the manifest);
  * pasted diagnostics in prompts are REAL: the broken script is run by real bash / real shellcheck and its stderr / findings are pasted
    (temp paths replaced by the relative script path);
  * every model tool call is classified by the real PolicyEngine (Oracle in ethan_ds_policy_skills.py), one batch at the end;
  * destructive-script requests are answered with a guarded script (the harness feeds it dangerous arguments inside the read-only example_host) or a
    one-line refusal; the unsafe rejected side is never executed (static check only).

  ETHAN_CAP=3G scripts/ethan_capped_run.sh python3 -B scripts/ethan_ds_shell.py --out data/autoimprove/20261116/shell/shell_v1.jsonl --seed 1116 --per-family 46
"""
from __future__ import annotations
import argparse
import collections
import datetime
import hashlib
import json
import os
import random
import re
import shlex
import shutil
import subprocess
import sys
import time
from pathlib import Path
import ethan_ds_trajectories as T

def pick(rng, xs):
    raise NotImplementedError('TODO: implement')

def norm_prompt(s):
    raise NotImplementedError('TODO: implement')

class Shexample_host(T.example_host):
    """Gemini-CLI-shaped example_host plus `chmod +x FILE` (allowed by the real policy). Everything else keeps the base allowlist."""

    def t_run_shell_command(self, command, **_):
        raise NotImplementedError('TODO: implement')

def bwrap_ok():
    raise NotImplementedError('TODO: implement')

def _walk(work):
    raise NotImplementedError('TODO: implement')

def run_script(files, dirs, script_rel, case, shell=..., timeout=10):
    """Run `shell script_rel args...` in a fresh confined directory. Returns a result dict."""
    raise NotImplementedError('TODO: implement')

def _b(x):
    raise NotImplementedError('TODO: implement')

def check_case(res, case):
    """-> (ok, why). Everything not listed in writes/deletes/dirs must be unchanged."""
    raise NotImplementedError('TODO: implement')

def run_cases(files, dirs, script_rel, cases, shell=...):
    raise NotImplementedError('TODO: implement')

def bash_n(script_rel, text):
    raise NotImplementedError('TODO: implement')

def shellcheck(script_rel, text, fmt=..., dialect=...):
    raise NotImplementedError('TODO: implement')

def lint_ok(script_rel, text, dialect=..., strict=False):
    """bash -n clean and shellcheck without error/warning findings (info/style only for ALLOWED_STYLE; strict: nothing at all)."""
    raise NotImplementedError('TODO: implement')

def real_error(files, dirs, script_rel, case, shell=...):
    """Run a (broken) script and return its combined output as a user would paste it, with the confined work path removed."""
    raise NotImplementedError('TODO: implement')

def C(args=..., out=..., rc=0, **kw):
    raise NotImplementedError('TODO: implement')

def lines_of(rng, n, lo=1, hi=4, pool=...):
    raise NotImplementedError('TODO: implement')

def task(key, name, script, fixture, cases, spec, short, dirs=..., theme=..., ro=None):
    raise NotImplementedError('TODO: implement')

def t_wcopt(rng):
    raise NotImplementedError('TODO: implement')

def t_greet(rng):
    raise NotImplementedError('TODO: implement')

def t_padnum(rng):
    raise NotImplementedError('TODO: implement')

def t_sizefilter(rng):
    raise NotImplementedError('TODO: implement')

def t_repeat(rng):
    raise NotImplementedError('TODO: implement')

def t_kvget(rng):
    raise NotImplementedError('TODO: implement')

def t_rmtmp(rng):
    raise NotImplementedError('TODO: implement')

def t_levelcount(rng):
    raise NotImplementedError('TODO: implement')

def gen_log(rng, n):
    raise NotImplementedError('TODO: implement')

def t_topips(rng):
    raise NotImplementedError('TODO: implement')

def t_statushist(rng):
    raise NotImplementedError('TODO: implement')

def t_colsum(rng):
    raise NotImplementedError('TODO: implement')

def t_dedupe(rng):
    raise NotImplementedError('TODO: implement')

def t_joinowner(rng):
    raise NotImplementedError('TODO: implement')

def t_wordfreq(rng):
    raise NotImplementedError('TODO: implement')

def t_shellusers(rng):
    raise NotImplementedError('TODO: implement')

def t_colorfix(rng):
    raise NotImplementedError('TODO: implement')

def t_bigfiles(rng):
    raise NotImplementedError('TODO: implement')

def t_renamejpeg(rng):
    raise NotImplementedError('TODO: implement')

def t_numbered(rng):
    raise NotImplementedError('TODO: implement')

def t_wordtally(rng):
    raise NotImplementedError('TODO: implement')

def t_revargs(rng):
    raise NotImplementedError('TODO: implement')

def t_emptydirs(rng):
    raise NotImplementedError('TODO: implement')

def t_longest(rng):
    raise NotImplementedError('TODO: implement')

def t_totallines(rng):
    raise NotImplementedError('TODO: implement')

def t_stripext(rng):
    raise NotImplementedError('TODO: implement')

def t_mkconfig(rng):
    raise NotImplementedError('TODO: implement')

def t_semver(rng):
    raise NotImplementedError('TODO: implement')

def t_padtable(rng):
    raise NotImplementedError('TODO: implement')

def t_epoch(rng):
    raise NotImplementedError('TODO: implement')

def t_caseconv(rng):
    raise NotImplementedError('TODO: implement')

def t_describe(rng):
    raise NotImplementedError('TODO: implement')

def t_pathparts(rng):
    raise NotImplementedError('TODO: implement')

def t_tmpsort(rng):
    raise NotImplementedError('TODO: implement')

def t_grepcount(rng):
    raise NotImplementedError('TODO: implement')

def t_onlyin(rng):
    raise NotImplementedError('TODO: implement')

def t_lockrun(rng):
    raise NotImplementedError('TODO: implement')

def t_retry(rng):
    raise NotImplementedError('TODO: implement')

def t_evenodd(rng):
    raise NotImplementedError('TODO: implement')

def t_validate(rng):
    raise NotImplementedError('TODO: implement')

def t_revcopy(rng):
    raise NotImplementedError('TODO: implement')

def fixtask(key, name, script, good, bad, cases, run_args, kind, what, fixture=None, short=..., err_case=0):
    """`script` is the CORRECT script. The broken one replaces `good` (unique in script) by `bad`; the fix is bad -> good."""
    raise NotImplementedError('TODO: implement')

def b_unbound(rng):
    raise NotImplementedError('TODO: implement')

def b_then(rng):
    raise NotImplementedError('TODO: implement')

def b_done(rng):
    raise NotImplementedError('TODO: implement')

def b_typo(rng):
    raise NotImplementedError('TODO: implement')

def b_assign(rng):
    raise NotImplementedError('TODO: implement')

def b_int(rng):
    raise NotImplementedError('TODO: implement')

def b_subst(rng):
    raise NotImplementedError('TODO: implement')

def b_bracket(rng):
    raise NotImplementedError('TODO: implement')

def b_readonly(rng):
    raise NotImplementedError('TODO: implement')

def b_div(rng):
    raise NotImplementedError('TODO: implement')

def b_redirect(rng):
    raise NotImplementedError('TODO: implement')

def sctask(key, name, script, good, bad, code, cases, what, fixture=None, dirs=...):
    raise NotImplementedError('TODO: implement')

def c_rm_list(rng):
    raise NotImplementedError('TODO: implement')

def c_cmdsub(rng):
    raise NotImplementedError('TODO: implement')

def c_read(rng):
    raise NotImplementedError('TODO: implement')

def c_local(rng):
    raise NotImplementedError('TODO: implement')

def c_cd(rng):
    raise NotImplementedError('TODO: implement')

def c_backtick(rng):
    raise NotImplementedError('TODO: implement')

def c_args(rng):
    raise NotImplementedError('TODO: implement')

def c_status(rng):
    raise NotImplementedError('TODO: implement')

def c_array(rng):
    raise NotImplementedError('TODO: implement')

def c_ls(rng):
    raise NotImplementedError('TODO: implement')

def audit_lines(text):
    raise NotImplementedError('TODO: implement')

def p_audit1(rng):
    raise NotImplementedError('TODO: implement')

def p_audit2(rng):
    raise NotImplementedError('TODO: implement')

def p_audit3(rng):
    raise NotImplementedError('TODO: implement')

def p_port1(rng):
    raise NotImplementedError('TODO: implement')

def p_port2(rng):
    raise NotImplementedError('TODO: implement')

def p_port3(rng):
    raise NotImplementedError('TODO: implement')

def gnu_lines(text):
    raise NotImplementedError('TODO: implement')

def p_gnu1(rng):
    raise NotImplementedError('TODO: implement')

def p_gnu2(rng):
    raise NotImplementedError('TODO: implement')

def build_proj(rng):
    """A tiny multi-file bash project (lib + two scripts + README) whose identifiers are renamed by the refactor tasks."""
    raise NotImplementedError('TODO: implement')

def proj_expected(P, old, new, rng):
    """Differential oracle: run the ORIGINAL project with real bash and record outputs; renamed output = original with visible text replaced."""
    raise NotImplementedError('TODO: implement')

def s_clean(rng):
    raise NotImplementedError('TODO: implement')

def s_mkimage(rng):
    raise NotImplementedError('TODO: implement')

def s_purge(rng):
    raise NotImplementedError('TODO: implement')

def s_fixperms(rng):
    raise NotImplementedError('TODO: implement')

def s_prune(rng):
    raise NotImplementedError('TODO: implement')

def rowseed(seed, fam, idx, attempt):
    raise NotImplementedError('TODO: implement')

def base_files(proj, extra):
    raise NotImplementedError('TODO: implement')

def sh_cmd(path, args):
    raise NotImplementedError('TODO: implement')

def clip(s, n=200):
    raise NotImplementedError('TODO: implement')

def cmd_of(case, path):
    raise NotImplementedError('TODO: implement')

def short_files(files):
    raise NotImplementedError('TODO: implement')

def setup_write(theme):
    raise NotImplementedError('TODO: implement')

def final_write(sp, run, rng, mode):
    raise NotImplementedError('TODO: implement')

def pol_write(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def setup_fix(rng, idx):
    raise NotImplementedError('TODO: implement')

def final_fix(sp, run, rng, mode):
    raise NotImplementedError('TODO: implement')

def pol_fix(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def setup_sc(rng, idx):
    raise NotImplementedError('TODO: implement')

def final_sc(sp, run, rng, mode):
    raise NotImplementedError('TODO: implement')

def pol_sc(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def line_edits(orig, new):
    raise NotImplementedError('TODO: implement')

def setup_port(rng, idx):
    raise NotImplementedError('TODO: implement')

def fmt_hits(truth, gnu=None):
    raise NotImplementedError('TODO: implement')

def advice(gnu):
    raise NotImplementedError('TODO: implement')

def pol_audit(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def pol_port(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def setup_rename(rng, idx):
    raise NotImplementedError('TODO: implement')

def pol_rename(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def nav_items(script, typ):
    raise NotImplementedError('TODO: implement')

def nav_answer(script, typ):
    raise NotImplementedError('TODO: implement')

def setup_nav(rng, idx, nfix=11, nscript=33):
    raise NotImplementedError('TODO: implement')

def pol_nav(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def write_all():
    raise NotImplementedError('TODO: implement')

def setup_honest(rng, idx):
    raise NotImplementedError('TODO: implement')

def pol_honest(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def setup_safe(rng, idx, nsafe=25):
    raise NotImplementedError('TODO: implement')

def pol_safe(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def bad_modes(sp):
    raise NotImplementedError('TODO: implement')

def write_fixture(files, dirs, fx):
    raise NotImplementedError('TODO: implement')

def diff_lines(old, new):
    raise NotImplementedError('TODO: implement')

def judge(sp, msgs, fx, work):
    """-> (ok, detail). Replays every call on a fresh example_host (outputs must be byte-identical), then checks the final state with the real toolchain."""
    raise NotImplementedError('TODO: implement')

def gen_one(seed, fam, slot, attempt, scratch, want_rej):
    raise NotImplementedError('TODO: implement')

def build_rows(seed, per_family, scratch, only=None):
    raise NotImplementedError('TODO: implement')

def oracle_pass(rows):
    """One batch through the REAL PolicyEngine. Chosen calls must all be allowed; a rejected `bash x.sh` must be denied (its tool message becomes the engine's own text)."""
    raise NotImplementedError('TODO: implement')

def finalize(rows):
    raise NotImplementedError('TODO: implement')

def token_lengths(path, scratch):
    raise NotImplementedError('TODO: implement')

def versions():
    raise NotImplementedError('TODO: implement')

def bank_ids():
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
