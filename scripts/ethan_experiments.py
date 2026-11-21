# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Experiment queue: one-change-at-a-time A/B experiments, serially, only when the GPU is idle.

  ethan_experiments.py list | status | run [--max N] [--rounds 2] [--owner S] | needs-ethan

Experiments are JSON in data/self_improve/experiments/*.json:
  {id, hypothesis, baseline{name,request}, candidate{name,request}, apply[...], revert[...], requires_root}
`apply`/`revert` are lists of steps: an argv list, a shell-split string, or {"restart_server": {"env": {...}}}
(stop the idle model server, start it again through scripts/magi_autostart.py --start-one llama_server).
Root steps are NEVER executed: the exact consolidated line goes to data/self_improve/experiments/NEEDS_ETHAN.md and the
queue moves on. Measurement is scripts/ethan_cool_ab.py. Every outcome is appended to data/self_improve/experiments.jsonl.
Decision (workspace rule): KEEP only if tokens/s >= 97% of baseline AND joules/token or peak temp or pause count
improves AND output is identical; REVERT if tokens/s drops > 3% or something got worse with no gain; else INCONCLUSIVE.
A keep never changes the live server: apply is always reverted; adoption is a separate, recorded step.
"""
import argparse
import json
import os
import shlex
import signal
import subprocess
import sys
import time
from pathlib import Path
import ethan_cool_ab as ab

def load_experiments(exp_dir=None):
    raise NotImplementedError('TODO: implement')

def read_log(log=None):
    raise NotImplementedError('TODO: implement')

def append_log(rec, log=None):
    raise NotImplementedError('TODO: implement')

def step_argv(step):
    raise NotImplementedError('TODO: implement')

def is_root_step(step):
    raise NotImplementedError('TODO: implement')

def needs_root(exp):
    raise NotImplementedError('TODO: implement')

def shell_line(steps):
    raise NotImplementedError('TODO: implement')

def pending_root(exps, log_recs):
    raise NotImplementedError('TODO: implement')

def write_needs(exps, log_recs, needs=None):
    """One consolidated line per pending root experiment, with its revert and the marker that tells the queue to measure."""
    raise NotImplementedError('TODO: implement')

def mean(xs):
    raise NotImplementedError('TODO: implement')

def summarize_runs(runs):
    raise NotImplementedError('TODO: implement')

def decide(base, cand):
    """base/cand are summarize_runs dicts. Returns (decision, reasons)."""
    raise NotImplementedError('TODO: implement')

class Runner:
    """Real-world actions; tests replace it with a fake."""

    def run(self, argv, env=None):
        raise NotImplementedError('TODO: implement')

    def listener_pid(self):
        raise NotImplementedError('TODO: implement')

    def kill(self, pid):
        raise NotImplementedError('TODO: implement')

    def start_server(self, env):
        raise NotImplementedError('TODO: implement')

    def healthy(self):
        raise NotImplementedError('TODO: implement')

def restart_server(runner, cab_env, env, owner, sleep=..., wait_s=240):
    """Stop the idle server and start it again through the standard starter. Refuses unless the GPU is idle."""
    raise NotImplementedError('TODO: implement')

def do_steps(steps, runner, cab_env, owner, sleep):
    raise NotImplementedError('TODO: implement')

def cfg_of(d, fallback):
    raise NotImplementedError('TODO: implement')

def measure(cab_env, cfg, prompt, n, owner, sleep, gap):
    raise NotImplementedError('TODO: implement')

def strip(runs):
    raise NotImplementedError('TODO: implement')

def run_experiment(exp, runner, cab_env, rounds=2, owner=None, gap=5.0, sleep=..., log=None, prev_recs=None):
    """Measure one experiment. Request-level: ABBA via ethan_cool_ab. Server-level (has apply): baseline block, apply,
    candidate block, then revert ALWAYS runs and is recorded."""
    raise NotImplementedError('TODO: implement')

def next_experiments(exps, recs):
    """Queue order = file order. Done: keep/revert recorded, or MAX_TRIES inconclusive attempts. Root ones are never runnable
    until Ethan has applied them (marker file)."""
    raise NotImplementedError('TODO: implement')

def run_queue(runner=None, cab_env=None, exp_dir=None, log=None, needs=None, max_n=1, rounds=2, owner=None, gap=5.0, sleep=...):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
