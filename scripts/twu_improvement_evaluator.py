# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""TWU Improvement Evaluator: Evaluate upstream security & tooling candidates for safe workspace adoption.

Deterministic, offline-first. No model calls, no paid cloud APIs, no automatic downloads.
Evaluates leads queued by `scripts/external_improvement_scout.py` against workspace safety invariants:
  - License compatibility (AGENTS.md open-source license rule: GPL-3.0 compatible only)
  - Telemetry and phone-home detection (zero third-party telemetry invariant)
  - Runtime dependency footprint (standard library or air-gapped container isolation)
  - Cost and resource ceiling ($0 cloud spend, cgroup v2 RAM/CPU limits)
  - Human-in-the-loop oversight (generates inspectable trial dossiers; no blind merges)

Commands:
    python3 scripts/twu_improvement_evaluator.py list
    python3 scripts/twu_improvement_evaluator.py evaluate [--all | REPO]
    python3 scripts/twu_improvement_evaluator.py dossier REPO
    python3 scripts/twu_improvement_evaluator.py approve REPO --by USER
"""
from __future__ import annotations
import argparse
import json
import os
import sys
import time
from pathlib import Path
import stop_latch
import external_improvement_scout as scout

def sanitize_name(repo: str) -> str:
    raise NotImplementedError('TODO: implement')

def evaluate_candidate(candidate: dict) -> dict:
    raise NotImplementedError('TODO: implement')

def get_unrouted_leads(queue_file: Path=...) -> list[dict]:
    """Read candidates from queue_file and return only unrouted leads."""
    raise NotImplementedError('TODO: implement')

def save_trial_dossier(evaluation: dict) -> Path:
    raise NotImplementedError('TODO: implement')

def load_dossier(repo: str) -> dict | None:
    raise NotImplementedError('TODO: implement')

def list_trials() -> list[dict]:
    raise NotImplementedError('TODO: implement')

def approve_tool(repo: str, approver: str) -> bool:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
