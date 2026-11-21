# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Model-candidate experiment: is another local model better AND cooler for the Ethan CLI? Answered by measurement.

  ethan_model_ab.py plan    [--baseline M] [--candidate M] [--tasks N] [--k 2]   what would run and what blocks it (no GPU)
  ethan_model_ab.py run     --baseline M --candidate M [--tasks N] [--k 2] [--owner NAME]
  ethan_model_ab.py compare [RESULT.json]                                         recompute the verdict from a saved result

M is a GGUF path or a registry alias (qwen7b, qwen3-4b, gpt-oss-20b: the three on disk, no download needed).
`run` starts the model server ITSELF through the standard starter (scripts/magi_autostart.py --start-one llama_server with
ETHAN_CHAT_MODEL=<path>; gpt-oss also ETHAN_TUNE_N_CPU_MOE=12), ONLY when the GPU is idle and no server is up. A server it did
not start (not recorded in data/self_improve/model_ab/server.json with a live matching pid) is never touched: the run refuses.
Blocks follow ABBA over attempts (k=2: base, cand, cand, base); each block runs the same N bank tasks (eval split first, id order)
through ethan_eval_ab.run_one. While a block runs: GPU power/temperature are sampled (nvidia-smi, RAPL), guard pauses are counted
and tokens come from the server's /metrics counters when it exposes them (the starter does not pass --metrics, so tok/s and
J/token are usually None and the verdict then uses temperature only; it says so).
Safeguards (autopilot style): GPU_WINDOW lease owned 'model_ab', STOP/MODEL_STANDBY latches, thermal start_blocker, no live human
CLI session (ethan_cli_session), quiet hours from data/self_improve/autopilot.json. The server it started is always stopped at
the end (also on error); defaults are never changed or promoted. Needs the bridge (18195) already up; it never starts it.
Output: data/self_improve/model_ab/<stamp>.json. Verdict 'candidate better and cooler' needs: no gaming, valid runs, pass rate
not worse (paired exact sign test not significantly worse AND point estimate not lower) AND cooler (mean temp lower by 0.5 C)
or lower J/token (1%). Otherwise 'worse' (significant regression) or 'inconclusive'.
"""
from __future__ import annotations
import argparse
import json
import os
import signal
import subprocess
import sys
import threading
import time
import urllib.request
from datetime import datetime
from pathlib import Path
import ethan_eval_ab as ea
import ethan_cool_ab as cab

class Refused(RuntimeError):
    pass

def resolve_model(spec):
    """(name, path, extra_env). Alias or a GGUF path; a path that matches a registry entry keeps that entry's env."""
    raise NotImplementedError('TODO: implement')

def block_order(k):
    """Model label per block: ABBA over attempts. k=2 -> base, cand, cand, base (the first attempt of each model
    comes from a fresh block order that alternates who goes first). Returns [(attempt_of_model, 'base'|'cand')] * 2k."""
    raise NotImplementedError('TODO: implement')

def select_n(n, task_dir=None):
    """Eval split first (id order), then train split to fill; deterministic."""
    raise NotImplementedError('TODO: implement')

def lease_state(path, alive=None, now_ts=None):
    raise NotImplementedError('TODO: implement')

def acquire_lease(path, purpose, alive=None, now_ts=None):
    raise NotImplementedError('TODO: implement')

def release_lease(path):
    raise NotImplementedError('TODO: implement')

class Env:

    def __init__(self):
        raise NotImplementedError('TODO: implement')

    def now(self):
        raise NotImplementedError('TODO: implement')

    def sleep(self, s):
        raise NotImplementedError('TODO: implement')

    def stopped(self):
        raise NotImplementedError('TODO: implement')

    def standby(self):
        raise NotImplementedError('TODO: implement')

    def thermal_blocker(self):
        raise NotImplementedError('TODO: implement')

    def quiet_cfg(self):
        raise NotImplementedError('TODO: implement')

    def human_session(self):
        raise NotImplementedError('TODO: implement')

    def gpu_idle(self):
        raise NotImplementedError('TODO: implement')

    def listening(self, port):
        raise NotImplementedError('TODO: implement')

    def connections(self):
        raise NotImplementedError('TODO: implement')

    def listener_pid(self):
        raise NotImplementedError('TODO: implement')

    def path_exists(self, path):
        raise NotImplementedError('TODO: implement')

    def pid_alive(self, pid):
        raise NotImplementedError('TODO: implement')

    def start_server(self, path, extra_env):
        raise NotImplementedError('TODO: implement')

    def healthy(self):
        raise NotImplementedError('TODO: implement')

    def kill(self, pid):
        raise NotImplementedError('TODO: implement')

    def metrics(self):
        """(tokens_predicted_total, tokens_predicted_seconds_total) from /metrics, or None when the server does not expose it."""
        raise NotImplementedError('TODO: implement')

    def gpu_sample(self):
        raise NotImplementedError('TODO: implement')

    def rapl_uj(self):
        raise NotImplementedError('TODO: implement')

    def guard_pauses(self):
        raise NotImplementedError('TODO: implement')

    def runner(self, label, timeout=420):
        raise NotImplementedError('TODO: implement')

def in_quiet_hours(cfg, now):
    raise NotImplementedError('TODO: implement')

def preflight(env, need_idle=True):
    """Reason the run must not start, else None. Order: latches, quiet hours, human CLI, thermal, bridge, servers, idle."""
    raise NotImplementedError('TODO: implement')

def read_state(path):
    raise NotImplementedError('TODO: implement')

def harness_server(env):
    """None = no server up; 'ours' = a leftover server this harness started (pid recorded, alive, same listener); 'foreign'."""
    raise NotImplementedError('TODO: implement')

class ServerSlot:
    """Starts/stops ONLY the server it started. Context manager: always stops on exit."""

    def __init__(self, env, log=...):
        raise NotImplementedError('TODO: implement')

    def stop(self):
        raise NotImplementedError('TODO: implement')

    def ensure(self, name, path, extra_env):
        raise NotImplementedError('TODO: implement')

    def __enter__(self):
        raise NotImplementedError('TODO: implement')

    def __exit__(self, *exc):
        raise NotImplementedError('TODO: implement')

def run_block(env, label, tasks, attempt, runner, guard, interval=...):
    """Run each task once (attempt index `attempt`) while sampling; returns (rollouts, metrics, stop_reason)."""
    raise NotImplementedError('TODO: implement')

def aggregate(blocks):
    """Merge a model's block metrics: tokens/s = total tokens / total decode seconds, J/token = total joules / total tokens."""
    raise NotImplementedError('TODO: implement')

def compact(r):
    raise NotImplementedError('TODO: implement')

def verdict(base_recs, cand_recs, base_m, cand_m):
    """Pure. 'candidate better and cooler' only when pass rate is not worse AND (cooler OR lower J/token)."""
    raise NotImplementedError('TODO: implement')

def build_result(meta, base_recs, cand_recs, base_blocks, cand_blocks):
    raise NotImplementedError('TODO: implement')

def run_ab(env, baseline, candidate, n_tasks=6, k=2, owner=None, out_dir=None, tasks=None, log=..., task_dir=None):
    raise NotImplementedError('TODO: implement')

def plan_text(env, baseline, candidate, n_tasks, k):
    raise NotImplementedError('TODO: implement')

def latest_result(out_dir=None):
    raise NotImplementedError('TODO: implement')

def recompute(path):
    raise NotImplementedError('TODO: implement')

def main(argv=None, env=None):
    raise NotImplementedError('TODO: implement')
