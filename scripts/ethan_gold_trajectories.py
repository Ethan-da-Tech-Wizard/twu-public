# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Gold agent trajectories from the self-improvement bank, proven by replay. Prepares data only: no training, no model call.

For every sound bank task (data/self_improve/tasks/*.json) build the conversation the Ethan CLI / bridge shows the local
model (OpenAI chat format: system, user, assistant tool_calls, tool results, short final reply), using the reference solution
as the assistant's edits. Each trajectory is REPLAYED in a fresh example_host (read_file / write_file / replace executed for real,
tool results taken from that execution) and kept only if the task's hidden verifier passes (ethan_si_bank.verify).
Ladder rungs (ethan_ladder.derive_rungs) give one-requirement examples: rung prompt -> the correct write; kept only if that
rung's verifier and every earlier rung pass after the replay. Intermediate ladder states do not exist, so a rung example's
pre-state is the task's setup files and its edit is the full reference file (recorded as ladder_prestate=setup).

Split: ethan_si_bank.split_of (hash of the id). Eval tasks (and their rungs) go ONLY to eval.jsonl, never train.jsonl.
Data is synthetic and ours (bank tasks are authored locally); no private/personal data is read.

  ethan_gold_trajectories.py build [--out-dir data/training/gold_trajectories] [--stamp S] [--tasks ID ...]
  ethan_gold_trajectories.py check DIR        re-hash files, confirm eval ids are absent from train

Row shape (train.jsonl / eval.jsonl), TRL prompt-completion with tools, like private/example_host/distill/train_sft.py:
  {"prompt": [system, user, ...up to this step], "completion": [assistant message], "tools": "<json OpenAI tools>",
   "kind": "task"|"ladder_rung", "task": id, "split": "train"|"eval", "trajectory": id, "step": n}
One row per assistant turn, so loss falls only on the assistant. trajectories.jsonl holds the full message lists.
"""
import argparse, hashlib, json, sys, tempfile, time
from pathlib import Path
import ethan_si_bank as bank
import ethan_ladder as ladder

def _tool(name, desc, props, required):
    raise NotImplementedError('TODO: implement')

def extra_tools():
    """read_file/list_directory/... schemas as the CLI declares them (from saved dogfood rows) plus write_file and replace
    (Gemini CLI signatures; the saved rows never declared the two edit tools)."""
    raise NotImplementedError('TODO: implement')

def system_prompt():
    raise NotImplementedError('TODO: implement')

def make_prompt(task):
    raise NotImplementedError('TODO: implement')

def session_context(workdir, files, prompt):
    raise NotImplementedError('TODO: implement')

class example_host:
    """Executes the three file tools for real inside a temp dir; paths under the pretend workdir map into it."""

    def __init__(self, root, workdir):
        raise NotImplementedError('TODO: implement')

    def _path(self, p):
        raise NotImplementedError('TODO: implement')

    def run(self, name, args):
        raise NotImplementedError('TODO: implement')

def _call(i, name, args):
    raise NotImplementedError('TODO: implement')

def _edit_call(workdir, name, old, new):
    """replace when ONE contiguous region differs and its old text is unique, else write_file with the full content."""
    raise NotImplementedError('TODO: implement')

def final_reply(task, changed):
    raise NotImplementedError('TODO: implement')

def task_messages(task, workdir, tools_sys):
    """Message list (system, user, assistant/tool turns) for the whole task, or None when it cannot be expressed."""
    raise NotImplementedError('TODO: implement')

def rung_messages(task, rungs, idx, workdir, tools_sys):
    raise NotImplementedError('TODO: implement')

def rows_from(msgs, tools_json, meta):
    raise NotImplementedError('TODO: implement')

def sha(path):
    raise NotImplementedError('TODO: implement')

def build(out_dir=..., stamp=None, ids=None, task_dir=None):
    raise NotImplementedError('TODO: implement')

def check(d):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
