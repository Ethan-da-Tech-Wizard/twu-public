# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Execution-verified web/scripting language rows for the Ethan CLI LoRA (JavaScript/Node, Lua, SQL/sqlite3, TypeScript, plus structural HTML/CSS).

Output rows follow `ethan-system-pair.v1` (messages / tools / chosen_messages / rejected_messages / loss_mask / family_hash / split / verified_by) with the
language-spec additions (language, task_kind, seed_id, difficulty, paraphrase_id, toolchain, verifier dict). No model, service, network or npm install is used.

Verification (every candidate is really run, twice, in a bubblewrap example_host via scripts/ethan_lang_verify._exec: --unshare-all, --die-with-parent, read-only /usr, one
writable /work, wall-clock timeout, RLIMITs):
  * JavaScript   node --test on a HIDDEN test file (fixed cases + fixed-seed random cases)           -> verified_by "execution"
  * Lua          lua5.5 (and luajit when portable) on a HIDDEN harness                               -> "execution"
  * SQL          sqlite3 on a visible AND a hidden dataset, result sets compared to a Python oracle  -> "execution"
  * TypeScript   types are stripped by node's built-in type stripping, then run on hidden tests      -> "execution" (types are NOT checked: no tsc; recorded as type_checked=false)
  * HTML / CSS   stdlib html.parser / small CSS parser structural checks                              -> "structural" (never "execution")
Every rejected (DPO) answer is run by the same verifier and must FAIL. Tool-framed rows replay the calls the real Ethan CLI policy allows (read_file, write_file,
replace, `npm test`, `make test`) in a fresh example_host; tool outputs in the rows are the real captured outputs (timings masked).

Usage:
  nice -n 19 python3 scripts/ethan_ds_lang_web.py [--out-dir DIR] [--seed N] [--langs js,lua,sql,ts,html,css] [--per-seed K]
  nice -n 19 python3 scripts/ethan_ds_lang_web.py --reverify [DIR_OR_JSONL]
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import random
import re
import shutil
import sys
import tempfile
import time
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path
import ethan_lang_verify as LV
import ethan_system_pairs as SP

class Unavailable(RuntimeError):
    """example_host or toolchain missing. Never converted into a PASS."""

def sha(s):
    raise NotImplementedError('TODO: implement')

def tool_versions():
    raise NotImplementedError('TODO: implement')

def require(*names):
    raise NotImplementedError('TODO: implement')

def mask(text, work_dir=None):
    raise NotImplementedError('TODO: implement')

class Work:
    """A throwaway example_host working directory (mounted at /work)."""

    def __init__(self, files):
        raise NotImplementedError('TODO: implement')

    def run(self, cmd, timeout=30):
        """Run a shell command; returns (rc|None, text, timed_out). One retry when node hangs at startup with no output."""
        raise NotImplementedError('TODO: implement')

    def snapshot(self):
        raise NotImplementedError('TODO: implement')

    def write(self, rel, text):
        raise NotImplementedError('TODO: implement')

    def close(self):
        raise NotImplementedError('TODO: implement')

    def __enter__(self):
        raise NotImplementedError('TODO: implement')

    def __exit__(self, *a):
        raise NotImplementedError('TODO: implement')

def run_files(files, cmd, timeout=30):
    raise NotImplementedError('TODO: implement')

def node_counts(text):
    raise NotImplementedError('TODO: implement')

def verdict_node(rc, text, expect_n):
    raise NotImplementedError('TODO: implement')

def verdict_lua(rc, text, expect_n):
    raise NotImplementedError('TODO: implement')

def first_failure(text):
    raise NotImplementedError('TODO: implement')

def js_lit(v):
    raise NotImplementedError('TODO: implement')

def lua_lit(v):
    raise NotImplementedError('TODO: implement')

def paraphrase(rng, pid, lang, task, extra=..., tail_ok=True):
    """Seven distinct phrasing frames (pid 0..6); vocabulary differs, not just filler."""
    raise NotImplementedError('TODO: implement')

def norm_prompt(s):
    raise NotImplementedError('TODO: implement')

def skeleton(code):
    """Solution skeleton: identifiers and literals masked, hashed."""
    raise NotImplementedError('TODO: implement')

def family_name(lang, kind, seed_id):
    raise NotImplementedError('TODO: implement')

def msg_a(text):
    raise NotImplementedError('TODO: implement')

def fence(lang, code):
    raise NotImplementedError('TODO: implement')

class Prob:

    def __init__(self, id, kind, desc, gen, oracle, js=..., lua=..., ts=None, edge=..., names_js=None, names_lua=None, jbody=None, lbody=None, uses=..., tuses=..., luajit=True, tsnative=None, hard=1, hint=...):
        raise NotImplementedError('TODO: implement')

def snake(s):
    raise NotImplementedError('TODO: implement')

def reg(**kw):
    raise NotImplementedError('TODO: implement')

def ints(r, n, lo=..., hi=9):
    raise NotImplementedError('TODO: implement')

def words(r, n, pool=...):
    raise NotImplementedError('TODO: implement')

def _rle(s):
    raise NotImplementedError('TODO: implement')

def _flat(xs):
    raise NotImplementedError('TODO: implement')

def _topw(text, k):
    raise NotImplementedError('TODO: implement')

def _rot(xs, k):
    raise NotImplementedError('TODO: implement')

def _two(nums, t):
    raise NotImplementedError('TODO: implement')

def _bal(s):
    raise NotImplementedError('TODO: implement')

def _toroman(n):
    raise NotImplementedError('TODO: implement')

def _fromroman(s):
    raise NotImplementedError('TODO: implement')

def _merge(iv):
    raise NotImplementedError('TODO: implement')

def _gen_iv(r):
    raise NotImplementedError('TODO: implement')
from math import gcd as _g

def _lcm(xs):
    raise NotImplementedError('TODO: implement')

def _ana(a, b):
    raise NotImplementedError('TODO: implement')

def _gen_ana(r):
    raise NotImplementedError('TODO: implement')

def _kv(text):
    raise NotImplementedError('TODO: implement')

def _gen_kv(r):
    raise NotImplementedError('TODO: implement')

def _ws(xs, k):
    raise NotImplementedError('TODO: implement')
import bisect as _bis

def _title(s):
    raise NotImplementedError('TODO: implement')
import os as _os

def _fib(n):
    raise NotImplementedError('TODO: implement')

def _col(n):
    raise NotImplementedError('TODO: implement')

def _pas(n):
    raise NotImplementedError('TODO: implement')

def _gbi(ws):
    raise NotImplementedError('TODO: implement')

def _luhn(s):
    raise NotImplementedError('TODO: implement')

def _gen_luhn(r):
    raise NotImplementedError('TODO: implement')

def _tobase(n, b):
    raise NotImplementedError('TODO: implement')

def _coins(cs, amt):
    raise NotImplementedError('TODO: implement')

def _lis(xs):
    raise NotImplementedError('TODO: implement')

def _spiral(m):
    raise NotImplementedError('TODO: implement')

def _tag(r):
    raise NotImplementedError('TODO: implement')

def _gen_ext(r):
    raise NotImplementedError('TODO: implement')

def _ext_or(p):
    raise NotImplementedError('TODO: implement')

def _gen_rel(r):
    raise NotImplementedError('TODO: implement')

def _relp(a, b):
    raise NotImplementedError('TODO: implement')

def _gen_qs(r):
    raise NotImplementedError('TODO: implement')

def _qs(u):
    raise NotImplementedError('TODO: implement')

def _gen_sp(r):
    raise NotImplementedError('TODO: implement')

def _setp(u, k, v):
    raise NotImplementedError('TODO: implement')

def _gen_tally(r):
    raise NotImplementedError('TODO: implement')

def _tally(evs):
    raise NotImplementedError('TODO: implement')

def _gen_fsw(r):
    raise NotImplementedError('TODO: implement')

def _gen_fsl(r):
    raise NotImplementedError('TODO: implement')

def _gen_chunks(r):
    raise NotImplementedError('TODO: implement')

def _gen_lines(r):
    raise NotImplementedError('TODO: implement')

def _gen_json(r):
    raise NotImplementedError('TODO: implement')

def _json_or(t, fb):
    raise NotImplementedError('TODO: implement')

def _retry_or(fails, val, att):
    raise NotImplementedError('TODO: implement')
import base64 as _b64
import hashlib as _hl
import datetime as _dt

def _gen_days(r):
    raise NotImplementedError('TODO: implement')

def _agen(s, m, n):
    raise NotImplementedError('TODO: implement')

def _gen_nums(r):
    raise NotImplementedError('TODO: implement')

def _gen_tpl(r):
    raise NotImplementedError('TODO: implement')

def _tplf(tpl, vs):
    raise NotImplementedError('TODO: implement')

def _gen_ver(r):
    raise NotImplementedError('TODO: implement')

def _ver(s):
    raise NotImplementedError('TODO: implement')

def _gen_split(r):
    raise NotImplementedError('TODO: implement')

def _gen_word(r):
    raise NotImplementedError('TODO: implement')

def _gfib(a, b, n):
    raise NotImplementedError('TODO: implement')

def _sched(a, an, b, bn, c, cn):
    raise NotImplementedError('TODO: implement')

def _gen_recs(r):
    raise NotImplementedError('TODO: implement')

def _gen_rl(r):
    raise NotImplementedError('TODO: implement')

def _rl(t, tag):
    raise NotImplementedError('TODO: implement')

def _caesar(s, k):
    raise NotImplementedError('TODO: implement')

def _gen_rm(r):
    raise NotImplementedError('TODO: implement')

def regts(**kw):
    raise NotImplementedError('TODO: implement')

def _area(s):
    raise NotImplementedError('TODO: implement')

def _gen_shape(r):
    raise NotImplementedError('TODO: implement')

def _by_len(ws):
    raise NotImplementedError('TODO: implement')

def _port(s):
    raise NotImplementedError('TODO: implement')

def _zip(a, b):
    raise NotImplementedError('TODO: implement')

def _tally_ts(ws):
    raise NotImplementedError('TODO: implement')

def _stackops(ops):
    raise NotImplementedError('TODO: implement')

def _nm(u):
    raise NotImplementedError('TODO: implement')
import copy

def render_desc(p, noun):
    raise NotImplementedError('TODO: implement')

def make_cases(p, rng, n_rand=8):
    raise NotImplementedError('TODO: implement')

def oracle_of(p, args):
    raise NotImplementedError('TODO: implement')

def fill_body(body, name, args, lang):
    raise NotImplementedError('TODO: implement')

def js_uses_text(uses, style):
    raise NotImplementedError('TODO: implement')

def js_solution(p, name, si, style):
    raise NotImplementedError('TODO: implement')

def js_stub(p, name, si, style):
    raise NotImplementedError('TODO: implement')

def ts_header(p, name):
    raise NotImplementedError('TODO: implement')

def ts_solution(p, name, si=0):
    raise NotImplementedError('TODO: implement')

def ts_stub(p, name):
    raise NotImplementedError('TODO: implement')

def lua_solution(p, name, si):
    raise NotImplementedError('TODO: implement')

def lua_stub(p, name, si):
    raise NotImplementedError('TODO: implement')

def test_js(p, name, cases, style, mod, idxs=None, ts=False):
    raise NotImplementedError('TODO: implement')

def test_lua(p, name, cases, idxs=None):
    raise NotImplementedError('TODO: implement')

def fixture_files(lang, p, name, si, style, cases, vis_idx, ptype=...):
    """The scaffold the CLI starts from: stub solution + visible tests + the runner (package.json / Makefile, which the CLI may not write)."""
    raise NotImplementedError('TODO: implement')

def hidden_spec(lang, p, name, cases, style, rec_seed):
    """Hidden test files + command + expected count. Content never enters the row (only its sha256)."""
    raise NotImplementedError('TODO: implement')

def run_hidden(spec, files, timeout=...):
    """Run a hidden spec against solution files. Returns verdict dict (status PASS/FAIL, failing case numbers)."""
    raise NotImplementedError('TODO: implement')

def _failing(text):
    raise NotImplementedError('TODO: implement')

def hidden_pass_twice(spec, files):
    raise NotImplementedError('TODO: implement')

def mutants(code, lang, rng, limit=40):
    """Yield (mutated_text, old_line, new_line) for single-line mutations whose mutated line is unique in the mutated file."""
    raise NotImplementedError('TODO: implement')

def sol_files(lang, style, text):
    raise NotImplementedError('TODO: implement')

def find_mutants(lang, p, name, si, cases, style, want=2, seed=0, max_try=14):
    """Return list of dicts {text, old, new, failing(sorted case numbers)} for mutants that FAIL hidden tests at assertion level (no syntax errors/timeouts)."""
    raise NotImplementedError('TODO: implement')

def syntax_break(sol, lang, avoid_line):
    """Replace one `return ` keyword with a typo (a real syntax error in JS/Lua/TS); returns (broken_text, old_line, new_line) or None."""
    raise NotImplementedError('TODO: implement')

def cap(text):
    raise NotImplementedError('TODO: implement')

def tool_text(text, rc):
    raise NotImplementedError('TODO: implement')

def exec_calls(files, calls, timeout=60):
    """Replay calls in a fresh example_host. Returns (observations, final_files). Shell calls really run (bwrap); edit tools use the real semantics."""
    raise NotImplementedError('TODO: implement')

def counts_from(obs, lang):
    raise NotImplementedError('TODO: implement')

def examples_text(p, name, cases, lang):
    raise NotImplementedError('TODO: implement')

def export_text(lang, name, style):
    raise NotImplementedError('TODO: implement')

def fn_core(p, lang, name, style, noun, cases, rng, code):
    raise NotImplementedError('TODO: implement')

def tool_prompt(pid, lang, name, core, noun):
    raise NotImplementedError('TODO: implement')

def bug_prompt(pid, lang, name, p, noun):
    raise NotImplementedError('TODO: implement')

def repair_prompt(pid, lang, name, p, noun):
    raise NotImplementedError('TODO: implement')

def fix_counts_text(obs, lang):
    raise NotImplementedError('TODO: implement')

class Dropped(Exception):
    pass

def make_candidate(**kw):
    raise NotImplementedError('TODO: implement')

def sha_files(d):
    raise NotImplementedError('TODO: implement')

def fn_rows(lang, p, seed, plan=...):
    """Build candidate rows (dicts) for one problem and language. Raises Dropped(reason) when the seed cannot be verified."""
    raise NotImplementedError('TODO: implement')

class Data:

    def __init__(self, A, B, P):
        raise NotImplementedError('TODO: implement')

def gen_data(rng, dom, hidden=False):
    raise NotImplementedError('TODO: implement')

def mapping(dom, P):
    raise NotImplementedError('TODO: implement')

def csv_cell(v):
    raise NotImplementedError('TODO: implement')

def csv_text(header, rows):
    raise NotImplementedError('TODO: implement')

def lit_sql(v):
    raise NotImplementedError('TODO: implement')

def schema_sql(dom, extra=...):
    raise NotImplementedError('TODO: implement')

def seed_sql(dom, D):
    raise NotImplementedError('TODO: implement')

class QS:

    def __init__(self, id, kind, desc, sql, header, oracle, prep=None, extra_schema=..., check=None, err_ok=False, hard=2):
        raise NotImplementedError('TODO: implement')

def q(*a, **k):
    raise NotImplementedError('TODO: implement')

def sk(rows, *keys):
    raise NotImplementedError('TODO: implement')

def _tree(D, root):
    raise NotImplementedError('TODO: implement')

def _bucket(D):
    raise NotImplementedError('TODO: implement')

def _daily(D):
    raise NotImplementedError('TODO: implement')

def _hv(D):
    raise NotImplementedError('TODO: implement')

def _nt(D):
    raise NotImplementedError('TODO: implement')

def _upsert(D, P):
    raise NotImplementedError('TODO: implement')

def _check_cols(D, A):
    raise NotImplementedError('TODO: implement')

def stateful(id, desc, sql, check, oracle_text, extra_schema=..., hard=3, err_ok=False, prep=None):
    raise NotImplementedError('TODO: implement')

def _dups(D, rng):
    raise NotImplementedError('TODO: implement')

def _dedup_rows(D):
    raise NotImplementedError('TODO: implement')

def _audit(D, P):
    raise NotImplementedError('TODO: implement')

def _mig(D, P):
    raise NotImplementedError('TODO: implement')

def _notes(D, P):
    raise NotImplementedError('TODO: implement')

def _sp(D, P):
    raise NotImplementedError('TODO: implement')

def _arch(D, P):
    raise NotImplementedError('TODO: implement')

def sql_mutants(sql, rng, limit=30):
    raise NotImplementedError('TODO: implement')

def sql_run(files, order, timeout=20):
    """Run sqlite3 (batch, csv, header) over the .read files in order. Returns (rc, stdout, stderr, timed_out)."""
    raise NotImplementedError('TODO: implement')

def expected_text(qs, dom, D):
    raise NotImplementedError('TODO: implement')

class SqlSpec:
    """Everything needed to check a candidate query.sql: visible and hidden datasets (deterministic from the seed string)."""

    def __init__(self, qs, dom, seed):
        raise NotImplementedError('TODO: implement')

    def check(self, query_text, which, runs=1):
        raise NotImplementedError('TODO: implement')

    def check_both_twice(self, query_text):
        raise NotImplementedError('TODO: implement')

    def makefile(self):
        raise NotImplementedError('TODO: implement')

    def fixture(self, query_text):
        raise NotImplementedError('TODO: implement')

def sql_core(spec, noun=None):
    raise NotImplementedError('TODO: implement')

def sql_tool_prompt(pid, spec):
    raise NotImplementedError('TODO: implement')

def sql_bug_prompt(pid, spec, repair=False):
    raise NotImplementedError('TODO: implement')

def sql_rows(qs, dom, seed, modes=...):
    raise NotImplementedError('TODO: implement')

def sql_project_rows(dom, seed, n_variants=2):
    """K3: a schema + migration + seed + query-set project given in one answer; run end to end and compared with oracle result sets."""
    raise NotImplementedError('TODO: implement')

def files_answer(files, fence_lang):
    raise NotImplementedError('TODO: implement')

def parse_files_answer(text):
    raise NotImplementedError('TODO: implement')

class HtmlScan(HTMLParser):

    def __init__(self):
        raise NotImplementedError('TODO: implement')

    def handle_decl(self, decl):
        raise NotImplementedError('TODO: implement')

    def handle_starttag(self, tag, attrs):
        raise NotImplementedError('TODO: implement')

    def handle_startendtag(self, tag, attrs):
        raise NotImplementedError('TODO: implement')

    def handle_endtag(self, tag):
        raise NotImplementedError('TODO: implement')

    def handle_data(self, data):
        raise NotImplementedError('TODO: implement')

    def close(self):
        raise NotImplementedError('TODO: implement')

def html_failures(text, rules):
    raise NotImplementedError('TODO: implement')

def page(title, body, lang=..., extra_head=...):
    raise NotImplementedError('TODO: implement')

def h_form(rng, noun):
    raise NotImplementedError('TODO: implement')

def h_article(rng, noun):
    raise NotImplementedError('TODO: implement')

def h_table(rng, noun):
    raise NotImplementedError('TODO: implement')

def h_gallery(rng, noun):
    raise NotImplementedError('TODO: implement')

def h_nav(rng, noun):
    raise NotImplementedError('TODO: implement')

def h_login(rng, noun):
    raise NotImplementedError('TODO: implement')

def h_faq(rng, noun):
    raise NotImplementedError('TODO: implement')

def h_dialog(rng, noun):
    raise NotImplementedError('TODO: implement')

def h_glossary(rng, noun):
    raise NotImplementedError('TODO: implement')

def h_radio(rng, noun):
    raise NotImplementedError('TODO: implement')

def h_landing(rng, noun):
    raise NotImplementedError('TODO: implement')

def h_progress(rng, noun):
    raise NotImplementedError('TODO: implement')

def h_video(rng, noun):
    raise NotImplementedError('TODO: implement')

def h_search(rng, noun):
    raise NotImplementedError('TODO: implement')

def h_list(rng, noun):
    raise NotImplementedError('TODO: implement')

def h_card(rng, noun):
    raise NotImplementedError('TODO: implement')

def color_rgb(v):
    raise NotImplementedError('TODO: implement')

def lum(rgb):
    raise NotImplementedError('TODO: implement')

def contrast(a, b):
    raise NotImplementedError('TODO: implement')

def parse_css(text):
    """Tiny CSS parser: returns (rules, errors). rules = [{ctx, sel, decls:{prop:value}}] where ctx is the enclosing @-rule prelude or ''."""
    raise NotImplementedError('TODO: implement')

def css_failures(text, rules_req):
    raise NotImplementedError('TODO: implement')

def cwrap(css):
    raise NotImplementedError('TODO: implement')

def c_center(rng, w):
    raise NotImplementedError('TODO: implement')

def c_grid(rng, w):
    raise NotImplementedError('TODO: implement')

def c_dark(rng, w):
    raise NotImplementedError('TODO: implement')

def c_sticky(rng, w):
    raise NotImplementedError('TODO: implement')

def c_focus(rng, w):
    raise NotImplementedError('TODO: implement')

def c_ellipsis(rng, w):
    raise NotImplementedError('TODO: implement')

def c_hidden(rng, w):
    raise NotImplementedError('TODO: implement')

def c_aspect(rng, w):
    raise NotImplementedError('TODO: implement')

def c_button(rng, w):
    raise NotImplementedError('TODO: implement')

def c_motion(rng, w):
    raise NotImplementedError('TODO: implement')

def c_zebra(rng, w):
    raise NotImplementedError('TODO: implement')

def c_holy(rng, w):
    raise NotImplementedError('TODO: implement')

def c_clamp(rng, w):
    raise NotImplementedError('TODO: implement')

def c_print(rng, w):
    raise NotImplementedError('TODO: implement')

def c_spec(rng, w):
    raise NotImplementedError('TODO: implement')

def c_space(rng, w):
    raise NotImplementedError('TODO: implement')

def structural_check(kind, text, rules):
    raise NotImplementedError('TODO: implement')

def web_rows(kind, seed_id, fn, seed, per=4):
    """Structural rows (HTML or CSS). Each chosen answer passes every check; each rejected answer violates at least one (verified)."""
    raise NotImplementedError('TODO: implement')

def lua_run_lines(p, name, cases, idxs, prefix):
    raise NotImplementedError('TODO: implement')

def lua_proj_harness(parts, modname=...):
    raise NotImplementedError('TODO: implement')

def proj_build(lang, pa, pb, na, nb, ca, cb, style):
    """Return (project_files, hidden_spec)."""
    raise NotImplementedError('TODO: implement')

def proj_rows(lang, seed, n):
    raise NotImplementedError('TODO: implement')

def toolchain_str(lang):
    raise NotImplementedError('TODO: implement')

def is_edit(c):
    raise NotImplementedError('TODO: implement')

def sol_answer(lang, style):
    raise NotImplementedError('TODO: implement')

def sql_hidden(spec):
    raise NotImplementedError('TODO: implement')

def hidden_sha(h):
    """sha256 the generator records as verifier.hidden_tests_sha256, recomputed from the receipt's own hidden block."""
    raise NotImplementedError('TODO: implement')

def build_replay(c):
    raise NotImplementedError('TODO: implement')

def _answer_files(ans, text):
    raise NotImplementedError('TODO: implement')

def _sqlite_status(h, files, which):
    raise NotImplementedError('TODO: implement')

def replay_verify(x):
    """Re-run a row from x['replay'] only (plus the row's own answer text): rebuild the workspace, run the commands, run the hidden check on both sides."""
    raise NotImplementedError('TODO: implement')

def build_row(c, seed, frame, ext, dec):
    raise NotImplementedError('TODO: implement')

def policy_decisions(cands):
    raise NotImplementedError('TODO: implement')

def shingles(text, n=8):
    raise NotImplementedError('TODO: implement')

def near_dups(rows, thr=0.85):
    """Return the set of row indexes that have an earlier row with 8-gram Jaccard >= thr (on the user task text)."""
    raise NotImplementedError('TODO: implement')

def metrics(rows):
    raise NotImplementedError('TODO: implement')

def hard_minimums(m):
    raise NotImplementedError('TODO: implement')

def build(seed=..., langs=..., log=..., limit=None):
    raise NotImplementedError('TODO: implement')

def write_outputs(rows, info, out_dir, seed):
    raise NotImplementedError('TODO: implement')

def first_fence(text):
    raise NotImplementedError('TODO: implement')

def catalog():
    raise NotImplementedError('TODO: implement')

def verify_row(x, cat):
    raise NotImplementedError('TODO: implement')

def _verify_row_regen(x, cat):
    raise NotImplementedError('TODO: implement')

def reverify(path, limit=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
