# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Self-improvement loop driver: rollout -> harvest -> score -> gate, on tasks from ethan_si_bank.

Every stage is finite. The loop is "unbounded" only in that you may run cycle after cycle; each rollout checks the STOP
latch, open chats and heat before every attempt. The pass/fail label is the task's hidden verifier plus the lab's
violation detector (ground truth, not a claimed quality). Eval-split tasks are never harvested for training.

  ethan_si_loop.py plan                       what would run and what blocks it (no model call)
  ethan_si_loop.py rollout --name N [--k 3] [--split train|eval|all] [--minutes 30] [ID ...]
  ethan_si_loop.py harvest --name N           send clean train-split passes (SFT) and pass/fail pairs (DPO) to the hub
  ethan_si_loop.py report  --name N           pass rates per task and split
  ethan_si_loop.py gate --baseline N --candidate M   promote only on a gain beyond noise with no regression

Nothing here trains or promotes a model: it makes verified data and a go/no-go decision.
"""
import argparse, collections, hashlib, json, os, queue, signal, subprocess, sys, threading, time
from pathlib import Path
import ethan_si_bank as bank
import ethan_si_math as simath

def run_path(name):
    raise NotImplementedError('TODO: implement')

def lab_task(task):
    """Adapt a bank task to the shape ethan_task_lab.run_task expects."""
    raise NotImplementedError('TODO: implement')

def short(value, n=160):
    raise NotImplementedError('TODO: implement')

def event_text(ev, state):
    """One stream-json event -> a plain, high-contrast line (or None). `state` accumulates assistant text and tool calls."""
    raise NotImplementedError('TODO: implement')

def run_streaming(argv, cwd, env, task_id, emit, timeout=420, heartbeat=..., clock=...):
    """Run the CLI, showing each event as it happens. Returns (returncode|None, timed_out, state, tail).
    The reader thread only queues lines; this thread prints, so output never interleaves."""
    raise NotImplementedError('TODO: implement')

def infrastructure_reason(returncode, timed_out, n_calls, tail):
    """Why this run says nothing about the model, or None. A refusal/crash/timeout with zero tool calls is not the model failing."""
    raise NotImplementedError('TODO: implement')

def live_emitter(task_id):
    raise NotImplementedError('TODO: implement')

def real_runner(task, emit=None, timeout=420):
    """Run one task through the canonical `scripts/ethan chat -p` (the Enki hooks admit the turn). The prompt carries the
    autonomous-prompt marker and ETHAN_PROMPT_ORIGIN=harness so provenance says machine-composed. Nothing is bypassed."""
    raise NotImplementedError('TODO: implement')

def runner_is_cli_only(runner):
    """True only for real_runner (-> ethan_task_lab.run_task -> `ethan chat`), or any runner while ALLOW_MOCK_RUNNER is set."""
    raise NotImplementedError('TODO: implement')

def real_guard():
    """Reason to stop now, or None. Checked before every single attempt."""
    raise NotImplementedError('TODO: implement')

def rollout(tasks, k, runner, guard, sink, deadline=None, now=..., formulas=None):
    """K attempts per task, round-robin so a time limit still leaves every task sampled. Returns (records, stop reason)."""
    raise NotImplementedError('TODO: implement')

def load(name):
    raise NotImplementedError('TODO: implement')

def harvest(records, seen, contribute, formulas=None):
    """Train-split only. PASS -> SFT; PASS + FAIL on the same task -> DPO. Returns counts; mutates `seen`."""
    raise NotImplementedError('TODO: implement')

def score_line(records):
    raise NotImplementedError('TODO: implement')

def rates(records):
    """{split: (passes, attempts)} and {task: (passes, attempts)}."""
    raise NotImplementedError('TODO: implement')

def wilson_bounds(passes, n, z=None):
    raise NotImplementedError('TODO: implement')

def gate(baseline, candidate, formulas=None):
    """Delegates to ethan_si_math.gate_decision with the current (or given) formulas."""
    raise NotImplementedError('TODO: implement')

def hub_contribute(kind, **fields):
    raise NotImplementedError('TODO: implement')

def select(ids, split, task_dir=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
