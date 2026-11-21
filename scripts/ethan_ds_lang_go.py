# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Execution-verified Go rows for the Ethan CLI model (schema ethan-system-pair.v1, language=go, family = go:<kind>:<seed>).

Every row is a tool-use trajectory in the CLI's real tool frame (run_shell_command, read_file, replace, write_file; system prompt and tool
schemas reused from ethan_system_pairs.frame()/ext_frame()). The workspace is a virtual Go module (go.mod + Makefile pre-exist, because go.mod and
Makefile writes are ASK_USER and `go` itself is denied by the real policy; `make test` is allowed and runs go build/vet/test). The model reads files, edits with
`replace` (old_string copied from the earlier read), runs `make test` and reports honestly. Tool results are REAL outputs captured by running the
toolchain through scripts/ethan_lang_verify.py (bwrap example_host, /usr/bin/go, GOPROXY=off, std library only); durations are normalised.

Kinds: K1 stdlib API usage, K2 function from spec with HIDDEN table tests, K3 project generation (multi-file, build+vet+test, hidden pkg+main tests),
K4 bug-fix/refactor on seeded broken code, K5 compile-error repair loops (multi-turn, 1 or 2 stages). Hidden tests live in hidden_tests.json (never in
messages). Chosen final state must PASS the hidden tests; the rejected (DPO negative) final state must really FAIL compile or tests.
verified_by='execution' only when the example_host actually ran: UNAVAILABLE/ERROR aborts the build (never PASS).

  nice -n 19 python3 -B scripts/ethan_ds_lang_go.py [--out-dir DIR] [--seed N] [--target N]
  nice -n 19 python3 -B scripts/ethan_ds_lang_go.py --reverify [DIR]
"""
import argparse
import hashlib
import json
import os
import random
import re
import string
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
import ethan_lang_verify as lv
import ethan_system_pairs as P

class Unavailable(RuntimeError):
    """The example_host or Go toolchain could not really run: never treated as PASS."""

class DesignDrop(Exception):
    """A candidate row did not meet its own invariants (counted, not shipped)."""

class GoErr(Exception):
    """Raised by a Python reference when the Go function must return an error."""

def sha(x):
    raise NotImplementedError('TODO: implement')

def tabs(s):
    raise NotImplementedError('TODO: implement')

def G(text, **kw):
    """$name substitution (Go braces stay untouched) then 4-space -> tab indentation."""
    raise NotImplementedError('TODO: implement')

def gdiv(a, b):
    raise NotImplementedError('TODO: implement')

def lit(v, t):
    raise NotImplementedError('TODO: implement')

def zero_lit(t):
    raise NotImplementedError('TODO: implement')

def split_ret(ret):
    raise NotImplementedError('TODO: implement')

class Noun:

    def __init__(self, s):
        raise NotImplementedError('TODO: implement')

def rl(r, n, lo, hi):
    raise NotImplementedError('TODO: implement')

def rwords(r, n, pool=None):
    raise NotImplementedError('TODO: implement')

def rstr(r, alpha, lo, hi):
    raise NotImplementedError('TODO: implement')

def D(fn, args, ret, desc, body, bad, ref, gen, imports=..., notes=..., d=1, bug_note=..., bad_imports=None):
    raise NotImplementedError('TODO: implement')

def seed(group):
    raise NotImplementedError('TODO: implement')

def over_limit_sum(r, N):
    raise NotImplementedError('TODO: implement')

def clamp_all(r, N):
    raise NotImplementedError('TODO: implement')

def _dedupe_ref(ci):
    raise NotImplementedError('TODO: implement')

def dedupe_keep_order(r, N):
    raise NotImplementedError('TODO: implement')

def count_long_words(r, N):
    raise NotImplementedError('TODO: implement')

def is_balanced(r, N):
    raise NotImplementedError('TODO: implement')

def run_length_encode(r, N):
    raise NotImplementedError('TODO: implement')

def run_length_decode(r, N):
    raise NotImplementedError('TODO: implement')

def fizz_variant(r, N):
    raise NotImplementedError('TODO: implement')

def lcm_pair(r, N):
    raise NotImplementedError('TODO: implement')

def prime_count(r, N):
    raise NotImplementedError('TODO: implement')

def collatz_steps(r, N):
    raise NotImplementedError('TODO: implement')

def roman_numeral(r, N):
    raise NotImplementedError('TODO: implement')

def first_index_sorted(r, N):
    raise NotImplementedError('TODO: implement')

def count_pair_sums(r, N):
    raise NotImplementedError('TODO: implement')

def best_run_sum(r, N):
    raise NotImplementedError('TODO: implement')

def window_sums(r, N):
    raise NotImplementedError('TODO: implement')

def rotate_ints(r, N):
    raise NotImplementedError('TODO: implement')

def transpose_grid(r, N):
    raise NotImplementedError('TODO: implement')

def flatten_sorted(r, N):
    raise NotImplementedError('TODO: implement')

def anagram_groups(r, N):
    raise NotImplementedError('TODO: implement')

def shift_letters(r, N):
    raise NotImplementedError('TODO: implement')

def title_words(r, N):
    raise NotImplementedError('TODO: implement')

def snake_to_camel(r, N):
    raise NotImplementedError('TODO: implement')

def camel_to_snake(r, N):
    raise NotImplementedError('TODO: implement')

def is_palindrome_text(r, N):
    raise NotImplementedError('TODO: implement')

def common_prefix(r, N):
    raise NotImplementedError('TODO: implement')

def char_class_counts(r, N):
    raise NotImplementedError('TODO: implement')

def top_words(r, N):
    raise NotImplementedError('TODO: implement')

def parse_pairs(r, N):
    raise NotImplementedError('TODO: implement')

def merge_intervals(r, N):
    raise NotImplementedError('TODO: implement')

def prefix_sums(r, N):
    raise NotImplementedError('TODO: implement')

def diagonal_sum(r, N):
    raise NotImplementedError('TODO: implement')

def eval_rpn(r, N):
    raise NotImplementedError('TODO: implement')

def popcount_checked(r, N):
    raise NotImplementedError('TODO: implement')

def next_pow2(r, N):
    raise NotImplementedError('TODO: implement')

def digital_root(r, N):
    raise NotImplementedError('TODO: implement')

def to_base_text(r, N):
    raise NotImplementedError('TODO: implement')

def luhn_ok(r, N):
    raise NotImplementedError('TODO: implement')

def money_text(r, N):
    raise NotImplementedError('TODO: implement')

def hms_text(r, N):
    raise NotImplementedError('TODO: implement')

def day_of_year(r, N):
    raise NotImplementedError('TODO: implement')

def median_text(r, N):
    raise NotImplementedError('TODO: implement')

def percent_text(r, N):
    raise NotImplementedError('TODO: implement')

def bucket_floor(r, N):
    raise NotImplementedError('TODO: implement')

def sum_by_key(r, N):
    raise NotImplementedError('TODO: implement')

def invert_index(r, N):
    raise NotImplementedError('TODO: implement')

def sort_len_alpha(r, N):
    raise NotImplementedError('TODO: implement')

def chunk_list(r, N):
    raise NotImplementedError('TODO: implement')

def zip_add(r, N):
    raise NotImplementedError('TODO: implement')

def distinct_ci(r, N):
    raise NotImplementedError('TODO: implement')

def second_largest(r, N):
    raise NotImplementedError('TODO: implement')

def valid_ipv4(r, N):
    raise NotImplementedError('TODO: implement')

def mask_digits(r, N):
    raise NotImplementedError('TODO: implement')

def wrap_lines(r, N):
    raise NotImplementedError('TODO: implement')

def longest_streak(r, N):
    raise NotImplementedError('TODO: implement')

def longest_unique(r, N):
    raise NotImplementedError('TODO: implement')

def edit_distance(r, N):
    raise NotImplementedError('TODO: implement')

def pascal_row(r, N):
    raise NotImplementedError('TODO: implement')

def grid_paths(r, N):
    raise NotImplementedError('TODO: implement')

def strictly_increasing(r, N):
    raise NotImplementedError('TODO: implement')

def moving_max_streak(r, N):
    raise NotImplementedError('TODO: implement')

def balance_ledger(r, N):
    raise NotImplementedError('TODO: implement')

def api_normalize_tags(r, N):
    raise NotImplementedError('TODO: implement')

def api_parse_amounts(r, N):
    raise NotImplementedError('TODO: implement')

def api_top_n(r, N):
    raise NotImplementedError('TODO: implement')

def api_sorted_keys(r, N):
    raise NotImplementedError('TODO: implement')

def api_dedup_sorted(r, N):
    raise NotImplementedError('TODO: implement')

def api_classify_num(r, N):
    raise NotImplementedError('TODO: implement')

def api_longest_word(r, N):
    raise NotImplementedError('TODO: implement')

def api_expand_vars(r, N):
    raise NotImplementedError('TODO: implement')

def api_head_bytes(r, N):
    raise NotImplementedError('TODO: implement')

def api_total_price(r, N):
    raise NotImplementedError('TODO: implement')

def api_to_json(r, N):
    raise NotImplementedError('TODO: implement')

def api_days_between(r, N):
    raise NotImplementedError('TODO: implement')

def api_pretty_duration(r, N):
    raise NotImplementedError('TODO: implement')

def api_parallel_sum(r, N):
    raise NotImplementedError('TODO: implement')

def api_drain_ctx(r, N):
    raise NotImplementedError('TODO: implement')

def api_route(r, N):
    raise NotImplementedError('TODO: implement')

def api_render(r, N):
    raise NotImplementedError('TODO: implement')

def api_extract_ids(r, N):
    raise NotImplementedError('TODO: implement')

def api_acronym(r, N):
    raise NotImplementedError('TODO: implement')

def api_k_smallest(r, N):
    raise NotImplementedError('TODO: implement')

def api_truncate_runes(r, N):
    raise NotImplementedError('TODO: implement')

def api_sum_column(r, N):
    raise NotImplementedError('TODO: implement')

def api_sanitize(r, N):
    raise NotImplementedError('TODO: implement')

def api_group_ext(r, N):
    raise NotImplementedError('TODO: implement')

def api_format_row(r, N):
    raise NotImplementedError('TODO: implement')

def api_slugify(r, N):
    raise NotImplementedError('TODO: implement')

def sig_args(args):
    raise NotImplementedError('TODO: implement')

def go_src(pkg, inst, body, imports):
    raise NotImplementedError('TODO: implement')

def stub_body(inst):
    raise NotImplementedError('TODO: implement')

def test_src(pkg, inst, cases, suffix, call_name=None, name_const=None):
    raise NotImplementedError('TODO: implement')

def compute_cases(inst, rng, limit=14):
    raise NotImplementedError('TODO: implement')

def go_mod(mod):
    raise NotImplementedError('TODO: implement')

def thermal_wait():
    raise NotImplementedError('TODO: implement')

def norm_obs(text):
    raise NotImplementedError('TODO: implement')

def make_run(files, hidden=None, memo=None, project=False):
    """Run `make test` for a virtual workspace in the verifier example_host. Returns {'status','obs'}; raises Unavailable if it could not really run."""
    raise NotImplementedError('TODO: implement')

def read_call(path):
    raise NotImplementedError('TODO: implement')

def grep_obs(files, pat, root):
    raise NotImplementedError('TODO: implement')

def play(files0, calls, hidden=None, final_hidden=False, memo=None):
    """Execute tool calls on a virtual workspace. Returns (obs list, final files, last make result or None)."""
    raise NotImplementedError('TODO: implement')

def diff_edit(path, old_src, new_src):
    """Minimal unique replace edit turning old_src into new_src (line based, context added until old_string matches once)."""
    raise NotImplementedError('TODO: implement')

def rep(path, old, new):
    raise NotImplementedError('TODO: implement')

def wf(path, content):
    raise NotImplementedError('TODO: implement')

def ok_line(obs):
    raise NotImplementedError('TODO: implement')

def fail_summary(obs):
    raise NotImplementedError('TODO: implement')

def lc(s):
    raise NotImplementedError('TODO: implement')

def style_prompt(kind, pid, c):
    raise NotImplementedError('TODO: implement')

def entry_lit(es):
    raise NotImplementedError('TODO: implement')

def main_wrapper(mod, pkg, body_lines, extra_imports=...):
    raise NotImplementedError('TODO: implement')

def hidden_main_test(expected):
    raise NotImplementedError('TODO: implement')

def proj_tally(r, N, mod):
    raise NotImplementedError('TODO: implement')

def proj_rpn(r, N, mod):
    raise NotImplementedError('TODO: implement')

def proj_store(r, N, mod):
    raise NotImplementedError('TODO: implement')

def mutations(src, inst):
    raise NotImplementedError('TODO: implement')

def finals_pool(kind, side, rng, c):
    raise NotImplementedError('TODO: implement')

def base_files(mod, project=False):
    raise NotImplementedError('TODO: implement')

def paraphrase_of(seed_s, kind, sid, k):
    raise NotImplementedError('TODO: implement')

def instance(seed_s, kind, sid, k):
    raise NotImplementedError('TODO: implement')

def finish_row(kind, sid, k, c, task, files0, hidden, chosen, rejected, rfinal_fn, cfinal_fn, rng, diff, para, single_pkg, project=False):
    """Run both trajectories for real, check the invariants, and build the row."""
    raise NotImplementedError('TODO: implement')

def frame_cached():
    raise NotImplementedError('TODO: implement')

def mk_ctx(kind, inst, N, pkg, path, rng, extra=None):
    raise NotImplementedError('TODO: implement')

def code_files(inst, pkg, mod, rng, nvis, kind_vis=None):
    raise NotImplementedError('TODO: implement')

def fill_calls(inst, pkg, path, imports, body):
    raise NotImplementedError('TODO: implement')

def build_k12(kind, sid, k, seed_s, seed_int):
    raise NotImplementedError('TODO: implement')

def build_k4(kind, sid, k, seed_s, seed_int):
    raise NotImplementedError('TODO: implement')

def build_k5(kind, sid, k, seed_s, seed_int):
    raise NotImplementedError('TODO: implement')

def build_k4r(kind, sid, k, seed_s, seed_int):
    raise NotImplementedError('TODO: implement')

def build_k3(kind, sid, k, seed_s, seed_int):
    raise NotImplementedError('TODO: implement')

def norm_prompt(s):
    raise NotImplementedError('TODO: implement')

def shingles(s, n=8):
    raise NotImplementedError('TODO: implement')

def jaccard(a, b):
    raise NotImplementedError('TODO: implement')

def skeleton(src):
    raise NotImplementedError('TODO: implement')

def diversity(rows):
    raise NotImplementedError('TODO: implement')

def plan(seed_s, target):
    raise NotImplementedError('TODO: implement')

def build(seed_s=..., target=..., log=..., only_kinds=None, limit=None, per_kind=None, partial=None):
    raise NotImplementedError('TODO: implement')

def gate(div):
    raise NotImplementedError('TODO: implement')

def write_outputs(rows, hidden, info, out_dir, seed_s, runtime):
    raise NotImplementedError('TODO: implement')

def reverify(path, log=...):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
