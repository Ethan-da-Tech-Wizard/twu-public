# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Cheaper-but-equal preference pairs and a first-try scorecard from existing run evidence.

A pair is emitted ONLY when two runs of the same task family ran against the same verifier id, BOTH passed that
verifier, and the chosen run is cheaper (no cost metric worse beyond tolerance, at least one better beyond a
margin). No model ever labels anything. Runs that did not pass, runs with unknown verifier, and evidence with no
checker (e.g. raw throughput benchmarks) never produce pairs; they are counted as impossible in the report.

  python3 scripts/ethan_efficiency_pairs.py build [--out DIR]
  python3 scripts/ethan_efficiency_pairs.py measure --family F --task T --verifier-id V [--attempt N] -- CMD...
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import resource
import subprocess
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

def _sha(text: str | bytes) -> str:
    raise NotImplementedError('TODO: implement')

def _jsonl(path: Path):
    raise NotImplementedError('TODO: implement')

def _rel(p: Path, root: Path) -> str:
    raise NotImplementedError('TODO: implement')

def load_witness(root: Path) -> list[dict]:
    """data/task_lab/witness: fixed CLI task, independent tests, one receipt per run."""
    raise NotImplementedError('TODO: implement')

def load_self_improve(root: Path) -> list[dict]:
    raise NotImplementedError('TODO: implement')

def load_repair_trials(root: Path) -> list[dict]:
    raise NotImplementedError('TODO: implement')

def load_reasoning(root: Path) -> list[dict]:
    raise NotImplementedError('TODO: implement')

def load_run_metrics(path: Path) -> list[dict]:
    """The ledger written by `measure` (future-proof source)."""
    raise NotImplementedError('TODO: implement')

def count_unverifiable(root: Path) -> dict:
    raise NotImplementedError('TODO: implement')

def _cost(run: dict) -> dict:
    raise NotImplementedError('TODO: implement')

def compare(chosen: dict, rejected: dict):
    """Return (better_metrics, worse_metrics, compared_metrics) for chosen vs rejected."""
    raise NotImplementedError('TODO: implement')

def build_pairs(runs: list[dict]) -> list[dict]:
    raise NotImplementedError('TODO: implement')

def scorecard(runs: list[dict]) -> list[dict]:
    raise NotImplementedError('TODO: implement')

def _gpu_used_mb() -> float | None:
    raise NotImplementedError('TODO: implement')

def measure(family, task, verifier_id, attempt, cmd, ledger: Path, sample_gpu=True) -> int:
    """Run cmd; record wall, peak RSS (children high-water mark), peak GPU memory, output bytes, retries, outcome.
    Outcome is the command's own exit code (0 == pass); it is never judged by a model."""
    raise NotImplementedError('TODO: implement')

def load_all(root: Path, ledger: Path | None=None) -> list[dict]:
    raise NotImplementedError('TODO: implement')

def build(root: Path, out: Path) -> dict:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
