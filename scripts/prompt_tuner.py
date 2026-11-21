# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Finds the system-prompt wording the local model answers best with, by measuring, not opinion (DSPy's idea, sized for 8 GB).

  1. EVAL SET    questions with checkable answers: the hand-written command recipes plus fixed instruction-following probes
  2. CANDIDATES  a few short wordings of the bridge's system prompt (data/prompt_tuning/candidates.json, or the built-ins)
  3. SCORE       every candidate answers every question through the local model (temperature 0); 1 point when the reply
                 contains the expected text; waits when the machine is hot
  4. ADOPT       the winner is written to data/prompt_tuning/best_prompt.txt ONLY if it beats the current wording by
                 ADOPT_MARGIN; the bridge reads that file, so the Ethan CLI uses the winner on its next request

  prompt_tuner.py --plan     show the eval set and candidates; no model calls
  prompt_tuner.py --run      do it (about 10 minutes of model time)
No network beyond localhost, no sudo, stdlib only.
"""
import argparse, json, re, subprocess, sys, time, urllib.request
from pathlib import Path

def recipe_evals(limit=10):
    """Questions built from the hand-written recipes; the expected text is the command's fixed head (no placeholders)."""
    raise NotImplementedError('TODO: implement')

def score_reply(reply, want):
    raise NotImplementedError('TODO: implement')

def ask(system_text, question, post=None, knowledge=None):
    """One answer from the local model, composed exactly as the bridge composes it (system prompt + matching recipes)."""
    raise NotImplementedError('TODO: implement')

def too_hot():
    """Unknown telemetry counts as hot: never run on a machine we cannot read (fail closed)."""
    raise NotImplementedError('TODO: implement')

def evaluate(candidates, evals, post=None, knowledge=None, wait=..., hot=...):
    """Mean score per candidate, in order. Waits out heat between questions instead of cooking the laptop."""
    raise NotImplementedError('TODO: implement')

def current_prompt():
    raise NotImplementedError('TODO: implement')

def adopt(candidates, scores, out=None):
    """Write the winner only when it clearly beats the current wording. Returns (winner_text, adopted?)."""
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
