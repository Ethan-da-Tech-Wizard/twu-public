# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""A/B measurement of the real Ethan CLI + local 7B on the task bank's held-out EVAL split.

Each rollout runs in its own throwaway git repo (a temp dir, `git init -b main`, the task's setup files committed, no
remote), so the CLI's clean-tree / local-only gate sees a clean repo and the shared workspace is never touched. The
launcher (`scripts/ethan` + `ethan_git_guard.py`) is copied into the example_host so its gate keys off the example_host, not the
shared repo; every other script, and Cannon/data/business/apps/MAGI_0, are symlinks. A write that reaches a symlinked
path is recorded as an `escaped_write` gaming event.

Pass/fail comes from the task's hidden verifier, run OUTSIDE the workdir with `python -I`. Protected files must be
byte-identical, and a pass also needs a random one-time marker the harness prints only after the verifier finishes, so
a verifier replaced or short-circuited by the model cannot produce a pass.

  ethan_eval_ab.py run --label NAME [--split eval] [--k 3] [--max-tasks N] [--minutes 120] [--headless|--visible]
                       [--server-managed] [--resume [FILE]] [--meta key=value ...]
  ethan_eval_ab.py compare A B          A, B = run file path or label (newest file for that label)
  ethan_eval_ab.py summary RUN
  ethan_eval_ab.py preflight            build one example_host and run the Git gate in it (no model call)

Outputs: data/self_improve/eval_ab/<label>-<stamp>.jsonl (header, one line per rollout, summary lines).
`compare` refuses to claim improvement unless the exact paired sign test (McNemar when k=1) is significant AND no
protected-file / escaped-write / missing-marker event occurred in either run. Nothing here trains or promotes a model.
"""
import argparse, collections, hashlib, json, math, os, secrets, shutil, subprocess, sys, tempfile, time
from pathlib import Path
import ethan_si_bank as bank
import ethan_nudge

def wilson(passes, n, z=1.959964):
    """95% Wilson score interval (lo, hi); (0, 1) when n == 0."""
    raise NotImplementedError('TODO: implement')

def exact_sign_p(b, c):
    """Two-sided exact binomial (p=0.5) on discordant counts b, c. This is the exact McNemar test."""
    raise NotImplementedError('TODO: implement')

def server_blocker(managed=False, listening=None, idle=None):
    """Why a run must not start now, or None. Never sends a request to the model server (reads /proc/net/tcp + nvidia-smi)."""
    raise NotImplementedError('TODO: implement')

def thermal_blocker():
    raise NotImplementedError('TODO: implement')

def default_guard(managed=False):
    raise NotImplementedError('TODO: implement')

def _git(cwd, *args):
    raise NotImplementedError('TODO: implement')

def build_example_host(task, parent, link_launcher=True, source=None):
    """Create <parent>/ws as a fresh local-only git repo on main holding only the task's setup files. Returns its path."""
    raise NotImplementedError('TODO: implement')

def destroy_example_host(parent):
    raise NotImplementedError('TODO: implement')

def file_hashes(ws):
    raise NotImplementedError('TODO: implement')

def escaped_writes(calls, ws):
    """Write-tool calls whose target is outside the task area (a launcher symlink, outside the example_host, or .git)."""
    raise NotImplementedError('TODO: implement')

def strict_verify(task, ws, timeout=...):
    """(passed, message, gaming). Protected files first; verifier outside ws via `python -I`; a one-time marker is required."""
    raise NotImplementedError('TODO: implement')

def rescue_events(t0, t1, path=None):
    """Union history in the time window; foreign explicit hosts are not local rollouts.

    Hostless historical observations remain visible as unknown-host evidence,
    never inferred from a filename or attached as authenticated local events.
    """
    raise NotImplementedError('TODO: implement')

def default_cli(ws, prompt, policy):
    raise NotImplementedError('TODO: implement')

def make_record(task, attempt, label_run):
    raise NotImplementedError('TODO: implement')

def run_one(task, attempt, label_run, timeout=420, cli_factory=..., link_launcher=True, emit=None, rescue_path=None, keep=False, source=None):
    raise NotImplementedError('TODO: implement')

def read_records(path):
    raise NotImplementedError('TODO: implement')

def rollouts_of(path):
    raise NotImplementedError('TODO: implement')

def header_of(path):
    raise NotImplementedError('TODO: implement')

def find_run(spec, out_dir=None):
    raise NotImplementedError('TODO: implement')

def select_tasks(split, max_tasks, ids=..., task_dir=None):
    raise NotImplementedError('TODO: implement')

def run_eval(label, tasks, k, path, guard, runner, deadline=None, now=..., resume=False, meta=None, echo=None):
    """Round-robin k attempts per task, appending each result to `path`. Returns (new records, stop reason)."""
    raise NotImplementedError('TODO: implement')

def _rate_row(rs):
    raise NotImplementedError('TODO: implement')

def summarize(recs):
    raise NotImplementedError('TODO: implement')

def format_summary(s, title=...):
    raise NotImplementedError('TODO: implement')

def task_rates(recs):
    raise NotImplementedError('TODO: implement')

def compare_runs(recs_a, recs_b):
    raise NotImplementedError('TODO: implement')

def _verdict(c):
    raise NotImplementedError('TODO: implement')

def format_compare(c, name_a=..., name_b=...):
    raise NotImplementedError('TODO: implement')

def cmd_preflight():
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
