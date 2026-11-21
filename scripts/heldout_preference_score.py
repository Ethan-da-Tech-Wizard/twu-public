# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Held-out preference score: does a tuned model prefer `chosen` over `rejected` on pairs it never trained on?

Why: training logs only record train loss. This script gives the missing test score on
private/example_host/training/gold/gold_holdout.jsonl, for the BASE model and for a TUNED LoRA run.

Metrics (all on the held-out pairs, higher is better):
  base_pref_acc       share of pairs where the base model gives `chosen` the higher mean token log-prob
  tuned_pref_acc      same, with the tuned adapter applied
  implicit_reward_acc share where beta * (logp_tuned - logp_base) is higher for `chosen` than `rejected`
                      (the same "accuracy" the DPO trainer logs, so it is comparable to training telemetry)
  uplift              tuned_pref_acc - base_pref_acc

Safety: refuses to run while a DPO training process is using the GPU (one GPU job at a time) unless --force.
`--dry-run` validates inputs and prints the plan without importing torch.

Usage (after the run finishes; uses the train312 venv):
  /mnt/GameDrive/example_host/venvs/train312/bin/python scripts/heldout_preference_score.py       --base /mnt/GameDrive/example_host/models/Qwen/Qwen3-1.7B/70d244cc86cc       --adapter /mnt/GameDrive/example_host/distill/runs/dpo_gold_v4/adapter

"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import shlex
import subprocess
import sys
from typing import Any, Dict, List, Sequence

def load_pairs(path: Path, limit: int=0) -> List[Dict[str, str]]:
    """Loads valid (prompt, chosen, rejected) rows from a JSONL file."""
    raise NotImplementedError('TODO: implement')

def compute_metrics(scored: Sequence[Dict[str, float]], beta: float=0.1) -> Dict[str, Any]:
    """Pure metric math. Each row needs mean/sum log-probs of chosen/rejected for the base model
    (`base_c`, `base_r`) and optionally the tuned model (`tuned_c`, `tuned_r`)."""
    raise NotImplementedError('TODO: implement')

def _direct_dpo_invocation(command: str) -> bool:
    """Recognize the script operand, never text inside a launcher or Python -c.

    shortcut: ps is a non-atomic textual snapshot, not general GPU isolation;
    use a shared GPU lease if competing launchers need atomic admission.
    """
    raise NotImplementedError('TODO: implement')

def gpu_training_in_progress() -> bool:
    """Block direct DPO trainers and unavailable process inspection."""
    raise NotImplementedError('TODO: implement')

def _mean_logprob(model: Any, tok: Any, prompt: str, answer: str, max_length: int, device: str) -> float:
    raise NotImplementedError('TODO: implement')

def run_scoring(args: argparse.Namespace, pairs: List[Dict[str, str]]) -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def main() -> int:
    raise NotImplementedError('TODO: implement')
