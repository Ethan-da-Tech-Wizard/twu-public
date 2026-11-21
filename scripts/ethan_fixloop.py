# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Fix loop: when a gate fails, diagnose WHY, apply the next untried cheap fix to a CANDIDATE stack, re-test only the failed items, then the full set; repeat.

  python3 scripts/ethan_fixloop.py run   RUN_DIR [--live ...]               # RUN_DIR = saved acceptance result (dir, results.jsonl, or dogfood failures.jsonl); default = offline replay
  python3 scripts/ethan_fixloop.py diagnose RUN_DIR                         # classify failures only, change nothing
  python3 scripts/ethan_fixloop.py watch [--once] [--interval 300]          # WATCH only: writes data/health/FIXLOOP_NEXT.txt, starts/changes nothing

Rules (workspace safety): every attempt is one new fix (key stored in state.json, never repeated, also across restarts); fixes touch only
a candidate config + a separate-port bridge (live) or saved-reply replay (offline). Never production ports 18190/18195 as a bridge, never
the promotion flow (ethan_promote / ethan_approve): the output is candidate_config.json + receipt.json for a human-approved promotion.
Stops: all pass | max attempts | max minutes | 3 attempts without improvement | catalog exhausted | HALT | unsafe task allowed (recommends HALT,
never "fixes" it). No model labeling: classification is rules on the saved transcript. Standard library only.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

def classify(rec: dict) -> str:
    """Cause class for one failed episode (normalized record: id, kind, answer, tool_calls, tool_statuses, why, ...). Deterministic rules."""
    raise NotImplementedError('TODO: implement')

def _jsonl(p: Path) -> list:
    raise NotImplementedError('TODO: implement')

def load_run(path) -> dict:
    """Normalize a saved gate result into {dir, episodes:{id: record}}. Accepts a stamp dir (summary.json / results.jsonl), an acceptance
    dir holding stamp dirs (latest taken), a results.jsonl, or a dogfood failures.jsonl (every row is a failed episode)."""
    raise NotImplementedError('TODO: implement')

def _raw_reply(transcript: Path) -> str:
    raise NotImplementedError('TODO: implement')

def failures_of(episodes: dict, passed: dict | None=None) -> dict:
    raise NotImplementedError('TODO: implement')

def diagnose(episodes: dict, passed: dict | None=None) -> dict:
    raise NotImplementedError('TODO: implement')

def bridge_flag_names() -> set:
    raise NotImplementedError('TODO: implement')

def _f(name, kind, addresses, env=None, replayable=False, needs=None, note=...):
    raise NotImplementedError('TODO: implement')

def catalog(available_flags: set | None=None) -> list:
    raise NotImplementedError('TODO: implement')

def next_fix(failure_classes: dict, state: dict, avail: set | None=None):
    """First untried fix (catalog order) that addresses at least one current failure class and whose prerequisite is applied."""
    raise NotImplementedError('TODO: implement')

class ReplayExecutor:
    """Offline: re-scores saved failures with no model call. A fix is replayable only when it acts on a saved raw reply (rescue_*):
    then 'pass' means the bridge would turn the saved reply into a valid declared-tool call (not that the answer is then right).
    Fixes that change what the model says cannot be judged offline and leave the episode failing (honest: needs --live)."""

    def __init__(self, episodes: dict):
        raise NotImplementedError('TODO: implement')

    def run(self, ids, config_env: dict) -> dict:
        raise NotImplementedError('TODO: implement')

    def start(self, config_env):
        raise NotImplementedError('TODO: implement')

    def stop(self):
        raise NotImplementedError('TODO: implement')

class LiveExecutor:
    """Runs scripts/ethan_cli_acceptance.py against a SEPARATE-port bridge started by this loop with the candidate flags. The bridge PID is
    saved and only that PID is ever signalled. Refuses production ports for the bridge. (Not exercised in unit tests: needs the GPU.)"""

    def __init__(self, episodes, out_dir: Path, model_port: int, bridge_port: int, share_live_model=False):
        raise NotImplementedError('TODO: implement')

    def start(self, config_env):
        raise NotImplementedError('TODO: implement')

    def stop(self):
        raise NotImplementedError('TODO: implement')

    def run(self, ids, config_env: dict) -> dict:
        raise NotImplementedError('TODO: implement')

def _halt_reason():
    raise NotImplementedError('TODO: implement')

def load_state(path: Path) -> dict:
    raise NotImplementedError('TODO: implement')

def save_state(path: Path, state: dict):
    raise NotImplementedError('TODO: implement')

def queue_pairs(eps: dict, classes: dict, queue: Path) -> int:
    """Failure -> pending training pair spec (prompt + failure class + what the model did). verified=false: the gold tool call and answer
    must still be produced and execution-verified (scripts/ethan_cli_real.py / ethan_dogfood_pairs.py) before any training."""
    raise NotImplementedError('TODO: implement')

def fix_loop(run: dict, executor, out_dir: Path, max_attempts=12, max_minutes=60.0, patience=3, halt_fn=..., queue_file: Path | None=None, now=...) -> dict:
    raise NotImplementedError('TODO: implement')

def write_receipt(run, eps, baseline_fail, baseline_score, passed, config, state, status, reason, out_dir, mode, start, end) -> dict:
    raise NotImplementedError('TODO: implement')

def newest_gate_run(root: Path):
    raise NotImplementedError('TODO: implement')

def watch_line(alarms_path: Path | None=None, root: Path | None=None, state_root: Path | None=None) -> str:
    raise NotImplementedError('TODO: implement')

def write_next(line: str, path: Path=...):
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
