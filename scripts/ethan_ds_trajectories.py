# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Deterministic, execution-verified multi-turn tool trajectories for the Gemini-CLI tool set (ethan-traj.v1).

Pipeline per row: build a small REAL fixture repo (fixtures/<row>/), copy it to a example_host, let a scripted oracle policy call the
real example_hosted tools (glob, grep_search, read_file, list_directory, replace, write_file, run_shell_command), record the real tool
outputs, then VERIFY by replaying every call on a fresh copy (outputs must be byte-identical) and checking the final repo state
(tests pass / exact answer / minimal diff). Rows that fail verification are dropped. About 30% of rows also carry a `rejected`
alternative produced by a deterministic wrong policy whose verifier FAILED (DPO negative).

No network, no model calls. Shell tool is a cwd-confined allowlist (python3/ls/cat/wc/head/tail, no shell operators).
Usage: python3 -B scripts/ethan_ds_trajectories.py --out data/autoimprove/20261116/trajectories/traj_v1.jsonl --seed 1116 --per-skill 180
"""
import argparse
import difflib
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

def _E(cat, name, params, correct, buggy, inputs):
    raise NotImplementedError('TODO: implement')

def fn_source(e, buggy):
    raise NotImplementedError('TODO: implement')

def entry_ns(e, buggy=False):
    raise NotImplementedError('TODO: implement')

def call_text(name, args):
    raise NotImplementedError('TODO: implement')

def camel(s):
    raise NotImplementedError('TODO: implement')

def _w(fx, rel, text):
    raise NotImplementedError('TODO: implement')

def find_line(fx, rel, sub):
    raise NotImplementedError('TODO: implement')

def make_project(rng, fx, bug_entries=..., n_mods=None, dup_value=False, js_timeout=False, todos=0, typo_word=None):
    raise NotImplementedError('TODO: implement')

def jerr(msg):
    """Gemini CLI tool errors reach the model as functionResponse {"error": msg}; the bridge renders that with json.dumps."""
    raise NotImplementedError('TODO: implement')

def is_err(out):
    raise NotImplementedError('TODO: implement')

def diff_snippet(old, new, ctx=5):
    """Port of getDiffContextSnippet (gemini-cli 0.65.0 chunk-DKZARV6U.js)."""
    raise NotImplementedError('TODO: implement')

def read_text(path):
    raise NotImplementedError('TODO: implement')

class example_host:
    """cwd-confined executor whose tool-result strings follow Gemini CLI 0.65.0 (see FIDELITY). Paths are shown as DISPLAY_ROOT/..."""

    def __init__(self, fixture, work):
        raise NotImplementedError('TODO: implement')

    def cleanup(self):
        raise NotImplementedError('TODO: implement')

    def disp(self, full):
        raise NotImplementedError('TODO: implement')

    def rel(self, full):
        raise NotImplementedError('TODO: implement')

    def _path(self, p):
        raise NotImplementedError('TODO: implement')

    def _touch(self, full):
        raise NotImplementedError('TODO: implement')

    def snapshot(self):
        raise NotImplementedError('TODO: implement')

    def exec(self, name, args):
        raise NotImplementedError('TODO: implement')

    def t_read_file(self, file_path, start_line=None, end_line=None, **_):
        raise NotImplementedError('TODO: implement')

    def t_list_directory(self, dir_path, **_):
        raise NotImplementedError('TODO: implement')

    def _files(self, base):
        raise NotImplementedError('TODO: implement')

    def t_glob(self, pattern, dir_path=..., **_):
        raise NotImplementedError('TODO: implement')

    def t_grep_search(self, pattern, dir_path=None, **_):
        raise NotImplementedError('TODO: implement')

    def t_replace(self, file_path, old_string, new_string, instruction=..., allow_multiple=False, **_):
        raise NotImplementedError('TODO: implement')

    def _create(self, full, content):
        raise NotImplementedError('TODO: implement')

    def t_write_file(self, file_path, content, **_):
        raise NotImplementedError('TODO: implement')

    def t_run_shell_command(self, command, **_):
        raise NotImplementedError('TODO: implement')

def shell_rc(out):
    raise NotImplementedError('TODO: implement')

class Run:

    def __init__(self, sb, prompt):
        raise NotImplementedError('TODO: implement')

    def call(self, name, args, train=True):
        raise NotImplementedError('TODO: implement')

    def say(self, text):
        raise NotImplementedError('TODO: implement')

def vary_lines(rng, vk, lines, cyc=None):
    raise NotImplementedError('TODO: implement')

def fin(run, *lines):
    raise NotImplementedError('TODO: implement')

def parse_calls(messages):
    raise NotImplementedError('TODO: implement')

def changed_files(before, after):
    raise NotImplementedError('TODO: implement')

def oracle():
    """The REAL gemini-cli PolicyEngine (launcher mode), through the same helper scripts/ethan_ds_policy_skills.py uses."""
    raise NotImplementedError('TODO: implement')

def policy_denials(calls):
    raise NotImplementedError('TODO: implement')

def verify(sp, messages, fixture, work):
    raise NotImplementedError('TODO: implement')

def _verify(sp, messages, fixture, work):
    """Replay all calls on a fresh example_host copy, then check final state against the spec. Returns (passed, detail)."""
    raise NotImplementedError('TODO: implement')

def _lc(t):
    raise NotImplementedError('TODO: implement')

def lowerish(s):
    raise NotImplementedError('TODO: implement')

def typo(rng, text, n=2):
    raise NotImplementedError('TODO: implement')

def is_imperative(text):
    raise NotImplementedError('TODO: implement')

def style_prompt(rng, cores, k):
    """13 styles; polite prefixes ('pls', 'can you') are used only before imperatives, never before questions or fragments."""
    raise NotImplementedError('TODO: implement')

def read(fx, rel):
    raise NotImplementedError('TODO: implement')

def fix_span(fx, m):
    raise NotImplementedError('TODO: implement')

def sline(fx, name):
    raise NotImplementedError('TODO: implement')

def ran_n(out):
    raise NotImplementedError('TODO: implement')

def mk_fix(rng, fx, cat=None, cores=None):
    raise NotImplementedError('TODO: implement')

def pol_fix(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def a_pol(tools):
    raise NotImplementedError('TODO: implement')

def s1_base(rng, fx):
    raise NotImplementedError('TODO: implement')

def s1_where(rng, fx):
    raise NotImplementedError('TODO: implement')

def t_where(sp, run, rng):
    raise NotImplementedError('TODO: implement')

def s1_config(rng, fx):
    raise NotImplementedError('TODO: implement')

def t_config(sp, run, rng):
    raise NotImplementedError('TODO: implement')

def s1_readme(rng, fx):
    raise NotImplementedError('TODO: implement')

def t_readme(sp, run, rng):
    raise NotImplementedError('TODO: implement')

def s1_cli(rng, fx):
    raise NotImplementedError('TODO: implement')

def t_cli(sp, run, rng):
    raise NotImplementedError('TODO: implement')

def s1_tests(rng, fx):
    raise NotImplementedError('TODO: implement')

def t_tests(sp, run, rng):
    raise NotImplementedError('TODO: implement')

def s1_callers(rng, fx):
    raise NotImplementedError('TODO: implement')

def t_callers(sp, run, rng):
    raise NotImplementedError('TODO: implement')

def s1_js(rng, fx):
    raise NotImplementedError('TODO: implement')

def t_js(sp, run, rng):
    raise NotImplementedError('TODO: implement')

def s1_shell(rng, fx):
    raise NotImplementedError('TODO: implement')

def t_shell(sp, run, rng):
    raise NotImplementedError('TODO: implement')

def s1_version(rng, fx):
    raise NotImplementedError('TODO: implement')

def t_version(sp, run, rng):
    raise NotImplementedError('TODO: implement')

def s1_changelog(rng, fx):
    raise NotImplementedError('TODO: implement')

def t_changelog(sp, run, rng):
    raise NotImplementedError('TODO: implement')

def edit_spec(fx, info, path, old, new, cores, gpat, vpat, wrong, ans, vk=..., **kw):
    raise NotImplementedError('TODO: implement')

def s2_const(rng, fx, vague=False):
    raise NotImplementedError('TODO: implement')

def s2_version(rng, fx):
    raise NotImplementedError('TODO: implement')

def s2_typo(rng, fx):
    raise NotImplementedError('TODO: implement')

def s2_js(rng, fx, vague=False):
    raise NotImplementedError('TODO: implement')

def s2_sh(rng, fx):
    raise NotImplementedError('TODO: implement')

def s2_cli(rng, fx):
    raise NotImplementedError('TODO: implement')

def pol_edit(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def mk_fix_cat(cat):
    raise NotImplementedError('TODO: implement')

def s4_wrongpath(rng, fx):
    raise NotImplementedError('TODO: implement')

def p4_wrongpath(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s4_nonunique(rng, fx):
    raise NotImplementedError('TODO: implement')

def p4_nonunique(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s4_missingdir(rng, fx):
    raise NotImplementedError('TODO: implement')

def p4_missingdir(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s4_malformed(rng, fx):
    raise NotImplementedError('TODO: implement')

def p4_malformed(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s4_notfound(rng, fx):
    raise NotImplementedError('TODO: implement')

def p4_notfound(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s4_wrongmod(rng, fx):
    raise NotImplementedError('TODO: implement')

def p4_wrongmod(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s5_ambig(rng, fx):
    raise NotImplementedError('TODO: implement')

def p5_ambig(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s5_missing(rng, fx):
    raise NotImplementedError('TODO: implement')

def p5_missing(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s5_zero(rng, fx):
    raise NotImplementedError('TODO: implement')

def p5_zero(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s5_green(rng, fx):
    raise NotImplementedError('TODO: implement')

def p5_green(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def act_wrap(setup, **kw):
    raise NotImplementedError('TODO: implement')

def s5_actfix(rng, fx):
    raise NotImplementedError('TODO: implement')

def p5_actfix(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s6_addfunc(rng, fx):
    raise NotImplementedError('TODO: implement')

def p6_addfunc(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s6_twobugs(rng, fx):
    raise NotImplementedError('TODO: implement')

def p6_twobugs(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s6_port(rng, fx):
    raise NotImplementedError('TODO: implement')

def p6_port(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s6_inventory(rng, fx):
    raise NotImplementedError('TODO: implement')

def p6_inventory(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s6_newtest(rng, fx):
    raise NotImplementedError('TODO: implement')

def p6_newtest(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s6_version(rng, fx):
    raise NotImplementedError('TODO: implement')

def p6_version(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def _regress_args(e):
    raise NotImplementedError('TODO: implement')

def s6_regress(rng, fx):
    raise NotImplementedError('TODO: implement')

def p6_regress(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s6_rename(rng, fx):
    raise NotImplementedError('TODO: implement')

def p6_rename(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s6_create(rng, fx):
    raise NotImplementedError('TODO: implement')

def p6_create(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s6_renameall(rng, fx):
    raise NotImplementedError('TODO: implement')

def p6_renameall(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s2_replall(rng, fx):
    raise NotImplementedError('TODO: implement')

def p2_replall(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s1_log(rng, fx):
    raise NotImplementedError('TODO: implement')

def t_log(sp, run, rng):
    raise NotImplementedError('TODO: implement')

def s6_listact(rng, fx):
    raise NotImplementedError('TODO: implement')

def p6_listact(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def s4_replrec(rng, fx):
    raise NotImplementedError('TODO: implement')

def p4_replrec(sp, run, mode, rng):
    raise NotImplementedError('TODO: implement')

def rowseed(seed, skill, idx, attempt):
    raise NotImplementedError('TODO: implement')

def norm_prompt(s):
    raise NotImplementedError('TODO: implement')

def task_tokens(sp):
    """Fixture-specific names (package, modules, target function) that make a prompt unique to its repo."""
    raise NotImplementedError('TODO: implement')

def tag_prompt(prompt, sp, idx):
    """Prompts that name no repo token get the package (and sometimes a module) woven into the sentence; a parenthetical only on ~4% of rows."""
    raise NotImplementedError('TODO: implement')

def generate_row(seed, skill, idx, attempt, scratch, want_reject=None, table=None, force_mode=None):
    raise NotImplementedError('TODO: implement')

def build(seed, per_skill, scratch, extra_js=0, extra_each=0):
    """Pass 1 collects every tool call, one batch asks the real policy engine, pass 2 builds with real decisions (rows with a denied/ask_user call are dropped)."""
    raise NotImplementedError('TODO: implement')

def _build(seed, per_skill, scratch, extra_js=0, extra_each=0):
    raise NotImplementedError('TODO: implement')

def manifest(rows, dropped, args, path):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
