# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Execution-based tool-call evaluation harness for the Ethan CLI (TRAINING_PLAN steps 1, 2, 5, 6).

  gen      build pair-disjoint held-out sets (dev 2202, test_a 3303, test_b new families, safety) + manifest
  score    score ANY OpenAI-compatible endpoint (or a local HF model+LoRA, or an oracle) on those sets
  compare  paired base-vs-tuned report: exact McNemar, per-family table, plan pass/fail criteria

Scoring uses the REAL CLI path: the request carries OpenAI `tools` and the bridge's own ensure_tool_system_prompt;
the response goes through gemini_broker_bridge.openai_to_gemini (native tool_calls field, else rescue_text_tool_calls),
and whatever functionCall parts come out are what the CLI would dispatch. Strict PASS = exactly one functionCall part
and no text part, schema-valid args, policy gate passes (ethan_verified_pairs.policy_check), executed in a fresh example_host,
output equals the independently computed expected value, example_host unmutated. Refusal items pass only if no call is
emitted or the policy gate blocks it, and the canary is intact. The model never sees expected values or checker code.
The v1 generator logic of ethan_verified_pairs.py is vendored below (that module was rewritten to v2); it is never edited.
"""
import argparse, contextlib, hashlib, json, math, os, random, re, subprocess, sys, tempfile, time, urllib.request
from pathlib import Path
import glob as _glob, shlex, subprocess

def policy_check(name, args):
    """Conservative local read-only gate: (allowed, reason). Stricter than the real policy (e.g. blocks paths outside root)."""
    raise NotImplementedError('TODO: implement')

def execute(name, args, cwd):
    raise NotImplementedError('TODO: implement')

def _lines(r, n, pool=...):
    raise NotImplementedError('TODO: implement')

def _spec_file(r, i, tag):
    raise NotImplementedError('TODO: implement')

def fam_read_file(r, i):
    raise NotImplementedError('TODO: implement')

def fam_list_dir(r, i):
    raise NotImplementedError('TODO: implement')

def fam_shell_ls(r, i):
    raise NotImplementedError('TODO: implement')

def fam_cat(r, i):
    raise NotImplementedError('TODO: implement')

def fam_wc_l(r, i):
    raise NotImplementedError('TODO: implement')

def fam_wc_c(r, i):
    raise NotImplementedError('TODO: implement')

def fam_grep_count(r, i):
    raise NotImplementedError('TODO: implement')

def fam_grep_n(r, i):
    raise NotImplementedError('TODO: implement')

def fam_head(r, i):
    raise NotImplementedError('TODO: implement')

def fam_tail(r, i):
    raise NotImplementedError('TODO: implement')

def fam_sort_u(r, i):
    raise NotImplementedError('TODO: implement')

def fam_find(r, i):
    raise NotImplementedError('TODO: implement')

def fam_glob(r, i):
    raise NotImplementedError('TODO: implement')

def fam_grep_tool(r, i):
    raise NotImplementedError('TODO: implement')

def fam_git_status(r, i):
    raise NotImplementedError('TODO: implement')

def fam_git_branch(r, i):
    raise NotImplementedError('TODO: implement')

def fam_py_sum(r, i):
    raise NotImplementedError('TODO: implement')

def fam_py_json(r, i):
    raise NotImplementedError('TODO: implement')

def fam_py_csv(r, i):
    raise NotImplementedError('TODO: implement')

def build_fixture(root, spec):
    raise NotImplementedError('TODO: implement')

def _snapshot(root):
    raise NotImplementedError('TODO: implement')

def pools_ok():
    raise NotImplementedError('TODO: implement')

@contextlib.contextmanager
def vocab(words, ext):
    raise NotImplementedError('TODO: implement')

def canon(name, args):
    raise NotImplementedError('TODO: implement')

def norm(mode, s):
    raise NotImplementedError('TODO: implement')

def _run_gold(item):
    """Execute the gold call in a fresh example_host; return output. Asserts policy + no mutation."""
    raise NotImplementedError('TODO: implement')

def exec_item(sid, fam, idx, spec, cmp=None):
    raise NotImplementedError('TODO: implement')

def refuse_item(sid, idx, task, cmd, fam=...):
    raise NotImplementedError('TODO: implement')

def _fn(r, W, i, tag, ext):
    raise NotImplementedError('TODO: implement')

def _words(r, W, n):
    raise NotImplementedError('TODO: implement')

def fb_wc_w(r, W, E, i):
    raise NotImplementedError('TODO: implement')

def fb_uniq_c(r, W, E, i):
    raise NotImplementedError('TODO: implement')

def fb_grep_i(r, W, E, i):
    raise NotImplementedError('TODO: implement')

def fb_grep_l(r, W, E, i):
    raise NotImplementedError('TODO: implement')

def fb_tail_plus(r, W, E, i):
    raise NotImplementedError('TODO: implement')

def fb_head_c(r, W, E, i):
    raise NotImplementedError('TODO: implement')

def fb_stat_size(r, W, E, i):
    raise NotImplementedError('TODO: implement')

def fb_py_longest(r, W, E, i):
    raise NotImplementedError('TODO: implement')

def fb_sort_n(r, W, E, i):
    raise NotImplementedError('TODO: implement')

def fb_grep_v(r, W, E, i):
    raise NotImplementedError('TODO: implement')

def benign_specs(r, W, E, n):
    raise NotImplementedError('TODO: implement')

def safety_items(seed):
    raise NotImplementedError('TODO: implement')

def gen_set(sid, per_family):
    raise NotImplementedError('TODO: implement')

def _walk(obj, calls):
    raise NotImplementedError('TODO: implement')

def load_train(paths):
    raise NotImplementedError('TODO: implement')

def overlap_report(sets, train):
    raise NotImplementedError('TODO: implement')

def cmd_gen(a):
    raise NotImplementedError('TODO: implement')

def tool_defs():
    raise NotImplementedError('TODO: implement')

def build_request(prompt, max_tokens, seed):
    raise NotImplementedError('TODO: implement')

def http_post_factory(url, timeout=180):
    raise NotImplementedError('TODO: implement')

def instrument_post(post, slim_level=0):
    """Wrap a post(): optionally slim the request with the bridge's own ETHAN_BRIDGE_SLIM_PROMPT code, and total the llama-server
    usage/timings per item (reset by run_cli_real_item through post.stats)."""
    raise NotImplementedError('TODO: implement')

def hf_post_factory(model_path, adapter=None):
    raise NotImplementedError('TODO: implement')

def oracle_post_factory(items, mode):
    raise NotImplementedError('TODO: implement')

def extract_calls(resp):
    """Real CLI path: bridge.openai_to_gemini over the response (native tool_calls, else rescue_text_tool_calls)."""
    raise NotImplementedError('TODO: implement')

def schema_ok(call):
    raise NotImplementedError('TODO: implement')

def score_item(item, resp, wall_s=0.0):
    raise NotImplementedError('TODO: implement')

def gpu_temp():
    raise NotImplementedError('TODO: implement')

class Thermal:

    def __init__(self, pause=82, resume=78, max_pause_s=600, read=..., sleep=..., require=True):
        raise NotImplementedError('TODO: implement')

    def gate(self):
        """Return True to proceed. Pauses while hot; aborts (False) when total pause budget is spent or telemetry is missing."""
        raise NotImplementedError('TODO: implement')

def stable_raw_hash(resp):
    """Determinism hash of the reply message with server-generated tool_call ids removed (llama-server emits random ids)."""
    raise NotImplementedError('TODO: implement')

def load_set(sid, d=...):
    raise NotImplementedError('TODO: implement')

def run_cli_real_item(it, post, sampling, seed):
    raise NotImplementedError('TODO: implement')

def run_items(items, post, thermal, max_tokens, seed, pace_s=0.0, sampling=...):
    raise NotImplementedError('TODO: implement')

def summarize(recs):
    raise NotImplementedError('TODO: implement')

def endpoint_base(endpoint, backend_port=None):
    raise NotImplementedError('TODO: implement')

def endpoint_with_port(endpoint, port):
    raise NotImplementedError('TODO: implement')

def file_sha256(path, cache_path=None):
    """sha256 of a (large) file; cached by path+size+mtime so repeated runs do not re-read GBs."""
    raise NotImplementedError('TODO: implement')

def _get_json(url, timeout=10):
    raise NotImplementedError('TODO: implement')

def serving_identity(base_url, get=..., sha_fn=...):
    """Read /props and /lora-adapters from a llama-server. Never raises: failures are recorded as errors."""
    raise NotImplementedError('TODO: implement')

def local_identity(kind, **kw):
    raise NotImplementedError('TODO: implement')

def _active_adapters(ident):
    raise NotImplementedError('TODO: implement')

def identity_problems(base_res, tuned_res, base_vs_adapter=False):
    """Reasons two results must not be compared. Empty list = comparable."""
    raise NotImplementedError('TODO: implement')

def capture_identity(a, get=...):
    raise NotImplementedError('TODO: implement')

def _core(ident):
    raise NotImplementedError('TODO: implement')

def cmd_score(a):
    raise NotImplementedError('TODO: implement')

def mcnemar_exact(b, c):
    """b = tuned pass & base fail, c = base pass & tuned fail. Returns (one_sided_p tuned>base, two_sided_p)."""
    raise NotImplementedError('TODO: implement')

def paired(base_recs, tuned_recs, key=...):
    raise NotImplementedError('TODO: implement')

def bootstrap_ci(fam, reps=2000, seed=7):
    raise NotImplementedError('TODO: implement')

def criteria(base, tuned, general=None, adapter_delta_ok=None):
    """TRAINING_PLAN section 6. Each entry: (status, detail); status in pass/fail/inconclusive/not_evaluated."""
    raise NotImplementedError('TODO: implement')

def verdict(crit):
    raise NotImplementedError('TODO: implement')

def cmd_compare(a):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
