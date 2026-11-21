# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Ethan dataset builder: Arch Linux system administration (skill 40), schema ethan-traj.v1.

Teaches the CLI model (which can only run what the real gemini-cli PolicyEngine allows) to do sysadmin work safely:
read-only diagnosis from files and from the few allowed live commands, writing and reviewing PKGBUILDs, writing and fixing bash
scripts, authoring and fixing systemd units/timers and cron lines, reading efibootmgr output, and the HUMAN-RUN hand-off for every
command the policy denies (sudo, pacman, systemctl, journalctl, efibootmgr, fwupdmgr, partitioning). Nothing here flashes firmware,
writes boot variables or needs root.

Ground truth, all offline:
  * tool results of machine commands (uname, df, free, uptime, cat /etc/os-release, which ...) and every pasted/saved output
    (pacman -Q*, systemctl status, journalctl, efibootmgr, lsblk, ip) are REAL outputs captured on this machine by `--recapture`
    (data/autoimprove/20261116/sysadmin/sysadmin_v1_captures.json) and SCRUBBED (hostname, user, MAC, UUID, IP, serial, email, home paths);
  * failing-service scenarios are real: user units are linked, started and read back through real systemd;
  * PKGBUILDs are really built offline with makepkg from a local tarball; scripts are `bash -n` checked and run against fixtures;
    units are checked with `systemd-analyze verify --root=...`; cron lines with a field parser; efibootmgr math with a parser;
  * every human-run command printed in an answer is checked: read-only ones are really executed, privileged ones are shape-checked;
  * every model tool call is classified by the real PolicyEngine (Oracle in ethan_ds_policy_skills.py); refusal rows carry the denied
    call as `rejected`, with the engine's own message.

  python3 -B scripts/ethan_ds_sysadmin.py --out data/autoimprove/20261116/sysadmin/sysadmin_v1.jsonl --seed 1116 --per-family 48
  python3 -B scripts/ethan_ds_sysadmin.py --recapture     # refresh the scrubbed machine captures (needs this machine)
"""
from __future__ import annotations
import argparse
import collections
import gzip
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
import tarfile
import time
from pathlib import Path
import ethan_ds_trajectories as T

class Scrubber:
    """Deterministic scrubber. One instance per text keeps UUID/IP maps consistent inside that text."""

    def __init__(self):
        raise NotImplementedError('TODO: implement')

    @staticmethod
    def _map(table, key, fmt):
        raise NotImplementedError('TODO: implement')

    def __call__(self, text):
        raise NotImplementedError('TODO: implement')

def scrub(text):
    raise NotImplementedError('TODO: implement')

def leaks(text):
    """Residual identifying strings after scrub (empty list = clean). Used by tests and by the final row check."""
    raise NotImplementedError('TODO: implement')

def sh(cmd, timeout=25, cwd=None, env=None):
    raise NotImplementedError('TODO: implement')

def svc_name(si, k):
    raise NotImplementedError('TODO: implement')

def unit_text(name, sc, exe_dir):
    raise NotImplementedError('TODO: implement')

def user_unit_dir():
    raise NotImplementedError('TODO: implement')

def real_service_run(name, sc):
    """Really link + start a user unit, read back status/journal, then remove every trace."""
    raise NotImplementedError('TODO: implement')

def capture_all():
    raise NotImplementedError('TODO: implement')

def recapture():
    raise NotImplementedError('TODO: implement')

def caps():
    raise NotImplementedError('TODO: implement')

def user_host_only(s):
    raise NotImplementedError('TODO: implement')

class Sysexample_host(T.example_host):

    def __init__(self, fixture, work):
        raise NotImplementedError('TODO: implement')

    def _machine(self, argv):
        raise NotImplementedError('TODO: implement')

    def _segment(self, argv, stdin):
        raise NotImplementedError('TODO: implement')

    def t_run_shell_command(self, command, **_):
        raise NotImplementedError('TODO: implement')

def validate_human(cmd):
    """(ok, why). Read-only commands are really executed; privileged ones are shape-checked and never run."""
    raise NotImplementedError('TODO: implement')

def tool_text(msgs):
    raise NotImplementedError('TODO: implement')

def call_text(msgs):
    raise NotImplementedError('TODO: implement')

def final_text(msgs):
    raise NotImplementedError('TODO: implement')

def check_answer(sp, msgs):
    """Generic honesty/fact/format checks on a finished chosen or rejected message list. Returns (ok, detail)."""
    raise NotImplementedError('TODO: implement')

def res(cond, good, bad):
    raise NotImplementedError('TODO: implement')

def parse_calls(msgs):
    raise NotImplementedError('TODO: implement')

def write_fixture(files, path):
    raise NotImplementedError('TODO: implement')

def rowseed(seed, fam, idx, attempt):
    raise NotImplementedError('TODO: implement')

def norm_prompt(s):
    raise NotImplementedError('TODO: implement')

def pick(rng, xs):
    raise NotImplementedError('TODO: implement')

def ask_oracle_message(cmd_args):
    raise NotImplementedError('TODO: implement')

def oracle():
    raise NotImplementedError('TODO: implement')

def replay_identical(msgs, fx, work):
    raise NotImplementedError('TODO: implement')

def gen_one(seed, fam, idx, attempt, scratch, want_reject):
    raise NotImplementedError('TODO: implement')

def say(run, text):
    raise NotImplementedError('TODO: implement')

def shell(run, cmd, train=True):
    raise NotImplementedError('TODO: implement')

def last_assistant_call_tail(msgs):
    raise NotImplementedError('TODO: implement')

def tail_has_changed(snap, rel):
    raise NotImplementedError('TODO: implement')

def lines_quote(text, rx):
    raise NotImplementedError('TODO: implement')

def clip_lines(text, n):
    raise NotImplementedError('TODO: implement')

def sc_count_ext(rng):
    raise NotImplementedError('TODO: implement')

def sc_thresh(rng):
    raise NotImplementedError('TODO: implement')

def sc_keep_newest(rng):
    raise NotImplementedError('TODO: implement')

def sc_pkgdiff(rng):
    raise NotImplementedError('TODO: implement')

def sc_needcmds(rng):
    raise NotImplementedError('TODO: implement')

def sc_colsum(rng):
    raise NotImplementedError('TODO: implement')

def sc_dedupe(rng):
    raise NotImplementedError('TODO: implement')

def sc_ini(rng):
    raise NotImplementedError('TODO: implement')

def sc_retry(rng):
    raise NotImplementedError('TODO: implement')

def sc_tag(rng):
    raise NotImplementedError('TODO: implement')

def sc_errtail(rng):
    raise NotImplementedError('TODO: implement')

def sc_sumcheck(rng):
    raise NotImplementedError('TODO: implement')

def run_script(script_text, files, args, env=None, name=..., workdir=None):
    """Really run a script against its fixture in a throwaway dir. Returns (rc, combined output)."""
    raise NotImplementedError('TODO: implement')

def bash_n(script_text):
    raise NotImplementedError('TODO: implement')

def shellcheck_ok(script_text):
    raise NotImplementedError('TODO: implement')

def det_tar(path, files):
    raise NotImplementedError('TODO: implement')

def proj_files(name, ver, kind):
    raise NotImplementedError('TODO: implement')

def pkgbuild_text(name, ver, desc, lic, deps, kind, tar_name, sha, url_source, inst, backup, mode=None):
    raise NotImplementedError('TODO: implement')

def build_pkg(files, startdir_name=...):
    """Really run makepkg offline in a throwaway copy. Returns (ok, detail, listing, srcinfo)."""
    raise NotImplementedError('TODO: implement')

def s_pkg_write(rng, i):
    raise NotImplementedError('TODO: implement')

def p_pkg_write(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def v_pkg_write(sp, msgs, snap, fx, work):
    raise NotImplementedError('TODO: implement')

def risky_pkgbuild(rng, name, risks):
    raise NotImplementedError('TODO: implement')

def risk_lines(text, risks):
    raise NotImplementedError('TODO: implement')

def s_pkg_review(rng, i):
    raise NotImplementedError('TODO: implement')

def p_pkg_review(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def v_pkg_review(sp, msgs, snap, fx, work):
    raise NotImplementedError('TODO: implement')

def named(script, name):
    raise NotImplementedError('TODO: implement')

def sc_name(i):
    raise NotImplementedError('TODO: implement')

def first_data(files):
    raise NotImplementedError('TODO: implement')

def s_bash_write(rng, i):
    raise NotImplementedError('TODO: implement')

def p_bash_write(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def v_bash_write(sp, msgs, snap, fx, work):
    raise NotImplementedError('TODO: implement')

def s_bash_fix(rng, i):
    raise NotImplementedError('TODO: implement')

def p_bash_fix(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def v_bash_fix(sp, msgs, snap, fx, work):
    raise NotImplementedError('TODO: implement')

def calendar_ok(spec):
    raise NotImplementedError('TODO: implement')

def verify_units(files, timer_names, service_names, name):
    """files: {abs path inside fake root: text}. Really runs systemd-analyze verify --root=. Returns (rc, output with the root prefix removed)."""
    raise NotImplementedError('TODO: implement')

def unit_pair(job, desc, sched, user=False, hard=False):
    raise NotImplementedError('TODO: implement')

def s_unit_author(rng, i):
    raise NotImplementedError('TODO: implement')

def p_unit_author(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def v_unit_author(sp, msgs, snap, fx, work):
    raise NotImplementedError('TODO: implement')

def s_unit_fix(rng, i):
    raise NotImplementedError('TODO: implement')

def p_unit_fix(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def v_unit_fix(sp, msgs, snap, fx, work):
    raise NotImplementedError('TODO: implement')

def s_cron(rng, i):
    raise NotImplementedError('TODO: implement')

def p_cron(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def v_cron(sp, msgs, snap, fx, work):
    raise NotImplementedError('TODO: implement')

def scen_keys():
    raise NotImplementedError('TODO: implement')

def s_diag_service(rng, i):
    raise NotImplementedError('TODO: implement')

def diag_answer(sp, ev):
    raise NotImplementedError('TODO: implement')

def p_diag_service(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def v_diag_service(sp, msgs, snap, fx, work):
    raise NotImplementedError('TODO: implement')

def s_diag_sshd(rng, i):
    raise NotImplementedError('TODO: implement')

def p_diag_sshd(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def v_diag_sshd(sp, msgs, snap, fx, work):
    raise NotImplementedError('TODO: implement')

def s_disk_full(rng, i):
    raise NotImplementedError('TODO: implement')

def p_disk_full(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def v_disk_full(sp, msgs, snap, fx, work):
    raise NotImplementedError('TODO: implement')

def human_text(rng, tool, cmd, why, look, i):
    raise NotImplementedError('TODO: implement')

def s_pkg_human(rng, i):
    raise NotImplementedError('TODO: implement')

def p_human(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def v_human(sp, msgs, snap, fx, work):
    raise NotImplementedError('TODO: implement')

def s_pkg_paste(rng, i):
    raise NotImplementedError('TODO: implement')

def p_pkg_paste(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def v_pkg_paste(sp, msgs, snap, fx, work):
    raise NotImplementedError('TODO: implement')

def s_pkg_orphans(rng, i):
    raise NotImplementedError('TODO: implement')

def p_pkg_orphans(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def v_pkg_orphans(sp, msgs, snap, fx, work):
    raise NotImplementedError('TODO: implement')

def parse_efi(text):
    raise NotImplementedError('TODO: implement')

def efi_variant(rng, i):
    raise NotImplementedError('TODO: implement')

def s_efi_read(rng, i):
    raise NotImplementedError('TODO: implement')

def efi_facts(sp):
    raise NotImplementedError('TODO: implement')

def p_efi_read(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def v_efi_read(sp, msgs, snap, fx, work):
    raise NotImplementedError('TODO: implement')

def s_efi_chain(rng, i):
    raise NotImplementedError('TODO: implement')

def p_efi_chain(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def v_efi_chain(sp, msgs, snap, fx, work):
    raise NotImplementedError('TODO: implement')

def s_fw(rng, i):
    raise NotImplementedError('TODO: implement')

def p_fw(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def v_fw(sp, msgs, snap, fx, work):
    raise NotImplementedError('TODO: implement')

def s_refuse(rng, i):
    raise NotImplementedError('TODO: implement')

def p_refuse(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def v_refuse(sp, msgs, snap, fx, work):
    raise NotImplementedError('TODO: implement')

def s_inspect(rng, i):
    raise NotImplementedError('TODO: implement')

def s_live(rng, i):
    raise NotImplementedError('TODO: implement')

def p_live(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def v_live(sp, msgs, snap, fx, work):
    raise NotImplementedError('TODO: implement')

def s_aur(rng, i):
    raise NotImplementedError('TODO: implement')

def p_aur(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def v_aur(sp, msgs, snap, fx, work):
    raise NotImplementedError('TODO: implement')

def common_prefix_len(a, b):
    raise NotImplementedError('TODO: implement')

def deny_targets(row_sp):
    raise NotImplementedError('TODO: implement')

def build_rows(seed, per_family, scratch, only=None):
    raise NotImplementedError('TODO: implement')

def reword(row, fam, idx, seen_p, seed):
    """Deterministic fallback for a duplicate prompt: add a neutral opener and/or closing sentence (counted in the manifest)."""
    raise NotImplementedError('TODO: implement')

def oracle_pass(rows):
    """Classify every model call with the REAL PolicyEngine; non-refusal calls must be allow, denied calls must be deny/ask."""
    raise NotImplementedError('TODO: implement')

def finalize(rows):
    raise NotImplementedError('TODO: implement')

def _h(*parts):
    raise NotImplementedError('TODO: implement')

def task_id_for(r):
    raise NotImplementedError('TODO: implement')

def add_task_ids(path, manifest_path=None, token_max=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')

def tool_versions():
    raise NotImplementedError('TODO: implement')

def write_manifest(rows, dropped, a):
    raise NotImplementedError('TODO: implement')
