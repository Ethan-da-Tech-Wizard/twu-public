# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Deterministic, execution-verified tool-call DPO pairs v3 for the Ethan CLI (domain ethan_cli).

What v3 changes relative to v2 (see data/autoimprove/20261101/verify/TOOLUSE_V2_REPORT.md, all findings applied):
  * The REAL Gemini PolicyEngine (node + installed gemini-cli + scripts/ethan_gemini_policy.toml) is re-run over EVERY chosen
    call at generation time. Any denial FAILS THE BUILD (no stale verdicts); the policy file sha256 goes in the manifest/rows.
  * Prompt/tools/system/ChatML are built by the eval harness itself (ethan_exec_eval.build_request + HEADER + tool_defs), so
    train and eval frames are byte-identical; rows also carry the Qwen chat-template rendering (prompt_chatml/chosen_chatml).
  * Hard negatives come from CONFUSABLE SIBLING INTENTS (every command shape is the right answer for one intent and the
    wrong answer for another), so flags/tools are balanced between chosen and rejected; a greedy balancer plus a measured
    cross-validated bag-of-tokens classifier (see separability()) keep hard-negative separability near chance.
    Rejected calls that turn out CORRECT are never used (each candidate is executed and must fail the checker).
  * No constant-call families, no single-step hidden-information label (cut_column asks for the Nth column), no grep -w /
    grep -rl . near-duplicate-correct rejects, prose rejects capped (~10%) and never containing the correct command.
  * Paraphrase pools (lead + core + tail), several path styles, tool-choice ambiguity (read_file vs cat vs head), benign
    git log/diff/show, ls -l, pip list look-alikes, >=8 distinct refusal texts, refusals <=15%.
  * ZERO overlap with data/autoimprove/20261101/eval/ (prompts, tasks, file paths, file-name tokens, call arguments) - every
    candidate is filtered against the eval sets, constant-call families are not generated at all.
Every chosen call is (1) parsed by the REAL rescue_text_tool_calls, (2) ALLOWED by the real policy engine, (3) executed in a
throwaway example_host, (4) compared with an expected value computed from the fixture spec. `--reverify PATH` re-executes every
non-refusal row with a separate executor (bash -c, plain-python tools, expectations re-derived from disk).

  python3 scripts/ethan_verified_pairs.py [--out PATH] [--seed N] [--per-intent N]
  python3 scripts/ethan_verified_pairs.py --reverify data/autoimprove/20261101/tooluse/pairs_v3.jsonl
"""
import argparse, glob as _glob, hashlib, json, math, os, random, re, shlex, shutil, stat as _stat, subprocess, sys, tempfile, time
from collections import Counter
from pathlib import Path

def _ee():
    raise NotImplementedError('TODO: implement')

def eval_frame(task):
    """(prompt, messages, tools) exactly as ethan_exec_eval.build_request sends them (system from ensure_tool_system_prompt)."""
    raise NotImplementedError('TODO: implement')

class Renderer:
    """HF chat-template renderer (jinja2) for the Qwen3 tokenizer_config chat template: what tokenizer.apply_chat_template does."""

    def __init__(self, tok_dir):
        raise NotImplementedError('TODO: implement')

    def render(self, messages, tools=None, add_generation_prompt=False, **kw):
        raise NotImplementedError('TODO: implement')

def qwen_call(name, args):
    """Exactly what the Qwen chat template renders for an assistant tool call."""
    raise NotImplementedError('TODO: implement')

def rescue(text):
    raise NotImplementedError('TODO: implement')

def _gemini_entry():
    raise NotImplementedError('TODO: implement')

def policy_sha256():
    raise NotImplementedError('TODO: implement')

def _run_node(argv, limit=900, startup=45, tries=4):
    """Run the policy script; return stdout. node was seen to hang (0% CPU, nothing printed) at startup inside the example_host, and the result
    line is printed before node would exit - so: kill+retry our own child if it prints nothing within `startup` s, and stop it as soon as
    the result line is complete."""
    raise NotImplementedError('TODO: implement')

def real_policy(calls):
    """calls: [(name, args)] -> [{'decision': 'allow'|'deny'|..., 'message': denyMessage|None}] from the REAL Gemini PolicyEngine."""
    raise NotImplementedError('TODO: implement')

def execute(name, args, cwd):
    """Run a call for real inside cwd. Returns (output, rc, cost). Tool errors become output text + rc 1."""
    raise NotImplementedError('TODO: implement')

def _lsl(out):
    raise NotImplementedError('TODO: implement')

def compare(expect, out):
    raise NotImplementedError('TODO: implement')

def passes(expect, ok_rc, name, out, rcode):
    """Output checker AND (optional) tool-choice constraint that the prompt states explicitly."""
    raise NotImplementedError('TODO: implement')

def build_fixture(root, fx):
    raise NotImplementedError('TODO: implement')

def _snapshot(root):
    raise NotImplementedError('TODO: implement')

def pick(r, xs):
    raise NotImplementedError('TODO: implement')

def stem(r):
    raise NotImplementedError('TODO: implement')

def dpath(r, depth=None):
    raise NotImplementedError('TODO: implement')

def fpath(r, ext, d=None, nospace=False):
    raise NotImplementedError('TODO: implement')

def uniq_paths(r, k, exts, d, nospace=False, taken=...):
    raise NotImplementedError('TODO: implement')

def sentence(r):
    raise NotImplementedError('TODO: implement')

def text_lines(r, n):
    raise NotImplementedError('TODO: implement')

def log_lines(r, n):
    raise NotImplementedError('TODO: implement')

def body(lines):
    raise NotImplementedError('TODO: implement')

def q(s):
    raise NotImplementedError('TODO: implement')

def parent(p):
    raise NotImplementedError('TODO: implement')

def rc(cmd):
    raise NotImplementedError('TODO: implement')

def decoy(r, f, files):
    """A same-directory, same-extension look-alike file so wrong-file negatives really exist."""
    raise NotImplementedError('TODO: implement')

class Phrase:

    def __init__(self, r, cores):
        raise NotImplementedError('TODO: implement')

    def __call__(self, **kw):
        raise NotImplementedError('TODO: implement')

def I(name, cluster, *cores, category=...):
    raise NotImplementedError('TODO: implement')

def S(goal, files, call, expect, cands, **kw):
    raise NotImplementedError('TODO: implement')

def E(mode, value, tool=None):
    raise NotImplementedError('TODO: implement')

def rf(p):
    raise NotImplementedError('TODO: implement')

def file_fix(r, exts=None, nl=...):
    raise NotImplementedError('TODO: implement')

def file_sibs(f, o, k):
    raise NotImplementedError('TODO: implement')

def other(cands, call):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def grep_fix(r):
    raise NotImplementedError('TODO: implement')

def grep_sibs(f, w, o):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def sort_sibs(f):
    raise NotImplementedError('TODO: implement')

def words_fix(r):
    raise NotImplementedError('TODO: implement')

def nums_fix(r):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def dir_fix(r, hidden=False, dirs_inside=True):
    raise NotImplementedError('TODO: implement')

def dir_sibs(x):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def py_maker(r):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _commits(r, k):
    raise NotImplementedError('TODO: implement')

def git_fix(r):
    raise NotImplementedError('TODO: implement')

def git_sibs(x, k):
    raise NotImplementedError('TODO: implement')

def gspec(x, k, goal, call, expect, **kw):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def _(r, ph):
    raise NotImplementedError('TODO: implement')

def refusal_vars(r):
    raise NotImplementedError('TODO: implement')

def load_eval_index(eval_dir=...):
    raise NotImplementedError('TODO: implement')

def eval_clash(ev, spec):
    """Reason string if this spec (task, fixture, chosen or any candidate call) touches the eval sets, else None."""
    raise NotImplementedError('TODO: implement')

def call_cmd(name, args):
    raise NotImplementedError('TODO: implement')

def norm_call(name, args):
    raise NotImplementedError('TODO: implement')

def a_call(name, args):
    raise NotImplementedError('TODO: implement')

def a_text(t):
    raise NotImplementedError('TODO: implement')

def run_checked(spec):
    """Execute chosen + candidates in fresh example_hostes. Returns (ok, info); info['wrong_results'] holds ONLY candidates that FAIL the checker."""
    raise NotImplementedError('TODO: implement')

def _run_checked_fixture(spec, template):
    raise NotImplementedError('TODO: implement')

def toks(text):
    raise NotImplementedError('TODO: implement')

def balance_rejected(hard, rng, passes_=4):
    """hard: list of dict(chosen_text, cands=[(name,args,wrong_result_dict)]). Choose one candidate per row so the token multiset of
    the rejected side tracks the chosen side (flags/tools appear equally often as right and wrong answers). Coordinate descent."""
    raise NotImplementedError('TODO: implement')

def separability(pairs, folds=5, seed=7, kind=...):
    """Cross-validated pairwise (Bradley-Terry style) logistic classifier on response text only (prompt excluded).
    pairs: [(chosen_text, rejected_text)]. Returns held-out accuracy = P(score(chosen) > score(rejected)); 0.5 is chance."""
    raise NotImplementedError('TODO: implement')

def build_rows(seed=1101, per_intent=26, refusal_max=0.14, prose_max=0.1, over_refusal_frac=0.3, eval_dir=..., render=None, log=None):
    raise NotImplementedError('TODO: implement')

def make_row(x, seed, render):
    raise NotImplementedError('TODO: implement')

def add_render(row, render, tool_call, rejected_is_call):
    raise NotImplementedError('TODO: implement')

def refusal_text(rnd, msg, cmd, web):
    raise NotImplementedError('TODO: implement')

def build_refusals(seed, cap, ev, render, pool=None):
    """Refusal rows. The pool (candidates + REAL policy verdicts) is built once up front (see build_rows); here only the cap is applied."""
    raise NotImplementedError('TODO: implement')

def refusal_pool(seed, ev, render, per_fam=34):
    raise NotImplementedError('TODO: implement')

def _cap_refusals(rows, cap):
    raise NotImplementedError('TODO: implement')

def refusal_row(fam, task, name, args, pol, render):
    raise NotImplementedError('TODO: implement')

def _rx_glob(pattern):
    raise NotImplementedError('TODO: implement')

def execute_independent(name, args, root):
    """A different implementation from execute(): bash -c, os.walk/os.scandir, hand-written glob regex."""
    raise NotImplementedError('TODO: implement')

def recompute_from_disk(row, root):
    """Re-derive the expected output from files on disk for the chosen call (argv + file contents only; no spec lambdas).
    Returns (supported, expected_value_or_None) in the row's own comparison mode."""
    raise NotImplementedError('TODO: implement')

def reverify(path):
    raise NotImplementedError('TODO: implement')

def summarize(rows, stats, render=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
