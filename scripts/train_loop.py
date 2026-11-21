# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""One full training loop on certified data, ending in ONE number. Serves the single goal (Magi 2, A2-ONE-GOAL-2026-10-22).

  1. GATE    sovereign_dataset_hub.py train-file rebuilds train_clean.jsonl and refuses unless certification passes
  2. SAMPLE  a fixed, seeded slice of its DPO pairs (small, so one run is about an hour on the 8 GB card)
  3. TRAIN   private/example_host/distill/train_dpo.py (QLoRA, capped VRAM), nice 19
  4. SCORE   scripts/heldout_preference_score.py on the immutable held-out set: a different tool from the trainer
  5. RECORD  data/train_loop/<run>/result.json and RESULT.md: base accuracy, tuned accuracy, uplift

  train_loop.py                plan only: prints what would run and what blocks it (touches nothing, no GPU)
  train_loop.py --run NAME     do it for real (refuses if the GPU is busy or hot; it never stops your model itself)

The GPU rule: the local model server holds most of the 8 GB card, so a real run needs it stopped first. That is your call,
so this tool only checks and tells you. No network, no sudo, stdlib only (the venv python does the heavy work).
"""
import argparse, hashlib, json, math, os, random, re, signal, subprocess, sys, tempfile, time
from pathlib import Path
import ethan_thermal_guard as _tg

def sample_pairs(path, n, seed=146, quality=None, domain=None):
    """Seeded distinct DPO pairs; quality is a claimed label, not semantic proof."""
    raise NotImplementedError('TODO: implement')

def blockers(gpu, base_exists=True, venv_exists=True, cpu_c=None):
    """gpu: {'free_mib': int, 'temp_c': int} or None. Returns a list of plain reasons the run cannot start now."""
    raise NotImplementedError('TODO: implement')

def heat_action(temp_c, paused, cpu_c=None):
    """What to do with the training process given the GPU (and CPU) temperature: 'pause', 'resume', 'abort' or '' (carry on)."""
    raise NotImplementedError('TODO: implement')

def known_temperature(value):
    raise NotImplementedError('TODO: implement')

def hold_reason():
    raise NotImplementedError('TODO: implement')

def read_cpu_temp():
    raise NotImplementedError('TODO: implement')

def signal_group(proc, sig):
    """Signal only a real child's own group. killpg(1, s) is kill(-1, s): every process of the user (a MagicMock pid
    converts to 1; this killed Ethan's desktop session 3 times on 2026-10-31)."""
    raise NotImplementedError('TODO: implement')

def cleanup_group(proc):
    """Resume a paused group so TERM can work, then reap the direct child."""
    raise NotImplementedError('TODO: implement')

def run_guarded(cmd, cwd, read_temp=None, poll=5.0, log=..., read_cpu=None, max_seconds=3600, output=None, observe=None):
    """Guard training or scoring, including cooling pauses, within one wall deadline."""
    raise NotImplementedError('TODO: implement')

def read_gpu():
    raise NotImplementedError('TODO: implement')

def summarize(score):
    """The one number is uplift = tuned - base preference accuracy on the held-out pairs."""
    raise NotImplementedError('TODO: implement')

def _json_tail(text):
    raise NotImplementedError('TODO: implement')

def atomic_json(path, value):
    """Publish a whole receipt, including failed/interrupted phases."""
    raise NotImplementedError('TODO: implement')

def training_artifacts(run):
    raise NotImplementedError('TODO: implement')

def wait_for_cooldown(deadline, publish):
    """Wait only for known hot telemetry, never for unknown telemetry or occupied VRAM."""
    raise NotImplementedError('TODO: implement')

def run_cycles(a, deadline):
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
