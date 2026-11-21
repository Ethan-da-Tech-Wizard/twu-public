# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Real-CLI-prompt tool-use data (pairs_v4) and the 'cli_real' eval set.

Why: a Qwen3-1.7B model that scored 194/228 on the lean exec-eval prompt passed only 4/9 real CLI acceptance tasks because the
real CLI sends a ~10.5k-token request (the Gemini CLI system prompt + a text copy of the tool list + 5 native tools + a session
context with the directory tree and GEMINI.md) and the model then ignored tool results. This module renders every example with
that captured request shape (optional guidance is now a labeled synthetic fixture, not a claim of current production context; template captured from the bridge: data/autoimprove/20261102/cli_real/template.json), including
multi-turn rows where the assistant must answer FROM the tool result.

Everything is verified by execution: each scenario builds a real fixture directory, the gold calls are executed by the same
read-only executor the eval uses (formats copied from real CLI tool results captured through the bridge), and the training answer
is accepted only if every expected value is (a) independently computed from the files on disk and (b) literally present in the
tool output the model saw. No model labels anything. Local only; nothing is sent anywhere.

Hold-out: the real acceptance fixtures (scripts/ethan_cli_acceptance.py make_fixture/build_tasks) are never trained on; file
names, paths, key names and values used by those tasks are excluded from the vocabularies and checked by leak_report().

  python3 scripts/ethan_cli_real.py build --out-dir DIR [--seed 4101] [--scenarios 650]
  python3 scripts/ethan_cli_real.py show  --split eval --index 0
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import random
import re
import shlex
import subprocess
import sys
import tempfile
from pathlib import Path

def benchmark_guidance():
    """Reproducible bounded eval input; never read unsynced host-local policy."""
    raise NotImplementedError('TODO: implement')

def guidance_provenance(text):
    raise NotImplementedError('TODO: implement')

def template():
    raise NotImplementedError('TODO: implement')

def bucket(word, n=5):
    raise NotImplementedError('TODO: implement')

def pool(words, split):
    raise NotImplementedError('TODO: implement')

def tree_text(root, files, empty_dirs):
    """Directory structure as the CLI prints it inside <session_context>."""
    raise NotImplementedError('TODO: implement')

def fmt_list_directory(dir_abs, entries):
    """entries: [(name, is_dir, size)] -> the CLI's listing (directories first)."""
    raise NotImplementedError('TODO: implement')

def fmt_glob(pattern, dir_abs, paths):
    raise NotImplementedError('TODO: implement')

def fmt_grep(pattern, path_abs, hits, context):
    """hits: [(relname, [(lineno, text, is_match)])]; a match is 'L<n>: text', context 'L<n>- text'."""
    raise NotImplementedError('TODO: implement')

def fmt_shell(stdout, pgid=215):
    raise NotImplementedError('TODO: implement')

class example_host:
    """A real directory for a scenario, addressed in prompts by a virtual absolute root."""

    def __init__(self, scn):
        raise NotImplementedError('TODO: implement')

    def snapshot(self):
        raise NotImplementedError('TODO: implement')

    def unchanged(self):
        raise NotImplementedError('TODO: implement')

    def real(self, virtual):
        raise NotImplementedError('TODO: implement')

    def virt(self, p):
        raise NotImplementedError('TODO: implement')

    def close(self):
        raise NotImplementedError('TODO: implement')

    def run(self, name, args):
        """-> (status, text). status 'success' or 'error' (error text is the CLI's JSON error object)."""
        raise NotImplementedError('TODO: implement')

    def _err(self, msg):
        raise NotImplementedError('TODO: implement')

    def _read_file(self, a):
        raise NotImplementedError('TODO: implement')

    def _list_directory(self, a):
        raise NotImplementedError('TODO: implement')

    def _glob(self, a):
        raise NotImplementedError('TODO: implement')

    def _grep_search(self, a):
        raise NotImplementedError('TODO: implement')

    def _run_shell_command(self, a):
        raise NotImplementedError('TODO: implement')

def session_context(scn, guidance=False, rng=None):
    raise NotImplementedError('TODO: implement')

def user_message(scn):
    raise NotImplementedError('TODO: implement')

def gold_calls(scn):
    raise NotImplementedError('TODO: implement')

def episode_messages(scn, results, upto):
    """OpenAI messages the bridge would send before the model turn `upto` (0 = first). results[k] = tool text of step k."""
    raise NotImplementedError('TODO: implement')

def to_wire(msgs):
    """Messages as the bridge puts them on the wire (tool-call arguments are JSON strings)."""
    raise NotImplementedError('TODO: implement')

def chat_request(msgs, sampling=..., seed=1234, max_tokens=256):
    raise NotImplementedError('TODO: implement')

def tool_call_text(name, args):
    raise NotImplementedError('TODO: implement')

def _names(rng, split, n, exts=None, taken=...):
    raise NotImplementedError('TODO: implement')

def _word(rng, split):
    raise NotImplementedError('TODO: implement')

def _lines(rng, n):
    raise NotImplementedError('TODO: implement')

def _root(rng, split):
    raise NotImplementedError('TODO: implement')

def _decoys(rng, split, files, dirs, n=None):
    """Extra files/dirs so the tree is not just the files the task needs."""
    raise NotImplementedError('TODO: implement')

class Task:
    """One scenario builder result (filled by the family functions below)."""

def _finish(scn, split, rng, steps, task, expect, answer, kind=..., family=..., forbid=...):
    raise NotImplementedError('TODO: implement')

def _base(rng, split):
    raise NotImplementedError('TODO: implement')

def _p(scn, rel):
    raise NotImplementedError('TODO: implement')

def pick_tpl(family, split, rng):
    raise NotImplementedError('TODO: implement')

def fam_json_key(rng, split):
    raise NotImplementedError('TODO: implement')

def fam_py_const(rng, split):
    raise NotImplementedError('TODO: implement')

def fam_label_line(rng, split):
    raise NotImplementedError('TODO: implement')

def fam_nth_line(rng, split):
    raise NotImplementedError('TODO: implement')

def fam_list_names(rng, split):
    raise NotImplementedError('TODO: implement')

def fam_list_has(rng, split):
    raise NotImplementedError('TODO: implement')

def fam_two_files(rng, split):
    raise NotImplementedError('TODO: implement')

def fam_glob_ext(rng, split):
    raise NotImplementedError('TODO: implement')

def fam_grep_count(rng, split):
    raise NotImplementedError('TODO: implement')

def fam_grep_which(rng, split):
    raise NotImplementedError('TODO: implement')

def fam_sh_wc(rng, split):
    raise NotImplementedError('TODO: implement')

def fam_sh_head(rng, split):
    raise NotImplementedError('TODO: implement')

def fam_sh_ls(rng, split):
    raise NotImplementedError('TODO: implement')

def fam_csv_cols(rng, split):
    raise NotImplementedError('TODO: implement')

def fam_missing_file(rng, split):
    raise NotImplementedError('TODO: implement')

def fam_unsafe(rng, split):
    raise NotImplementedError('TODO: implement')

def _contains(answer, needle):
    raise NotImplementedError('TODO: implement')

def run_episode_gold(scn):
    """Execute the gold calls in a real example_host -> (tool texts, statuses). Asserts nothing was mutated."""
    raise NotImplementedError('TODO: implement')

def independent_check(scn, outs):
    """Recompute the answer-bearing facts from the files and require them in the tool output the model saw. Raises on any mismatch."""
    raise NotImplementedError('TODO: implement')

def episode_rows(scn, outs, split, idx):
    """Training rows (v3-compatible: prompt/chosen/messages/tools/family): one per model turn."""
    raise NotImplementedError('TODO: implement')

def build_scenarios(split, seed, n):
    raise NotImplementedError('TODO: implement')

def acceptance_tasks():
    raise NotImplementedError('TODO: implement')

def leak_report(train_scns, eval_scns):
    raise NotImplementedError('TODO: implement')

def extract_turn(resp):
    """-> (calls, text) using the bridge's own response translation (what the CLI would act on)."""
    raise NotImplementedError('TODO: implement')

def run_item(scn, post, sampling=..., seed=1234, max_turns=4):
    """End-to-end episode, like the CLI: model -> execute its call in a real example_host with real-format results -> model ... until text.
    Pass = a final text answer containing every expected value after at least one executed successful tool call (refusal items: no
    allowed call executed and the example_host unchanged). Also returns the teacher-forced answer-turn result ('gold_answer_ok')."""
    raise NotImplementedError('TODO: implement')

def summarize(recs):
    raise NotImplementedError('TODO: implement')

def write_jsonl(path, rows):
    raise NotImplementedError('TODO: implement')

def cmd_build(a):
    raise NotImplementedError('TODO: implement')

def cmd_show(a):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
