# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Bounded overseer: one existing-model call may select one fixed maintenance action.

  observe -> the model picks one action from a fixed list -> code checks it is allowed -> run it -> observe again -> score
  The observed fault score before/after is stored per action. It is not a CPU/RAM/energy benchmark or proof of causation.

STOP, MODEL_STANDBY and unsafe/unknown heat hold the cycle. Recheck these and unit eligibility after the model decision.
Only enabled/enabled-runtime units reporting failed are recoverable; inactive alone may be an intentional stop.
Model/bridge absence is informational, never startup authority. If no model is up, use deterministic permitted
maintenance only. Tuning, volleys and certification require separate current approval, not this autonomous loop.
Ideas are proposal-only fields in the existing JSONL log. Old Markdown receipts are history, never action sources.

  overseer.py            one cycle (what the timer runs)
  overseer.py --plan     read observations and show the rule pick; no model call or action
"""
import fcntl
import os
import platform
import argparse, json, re, subprocess, sys, time, urllib.request
from pathlib import Path

def sh(cmd, timeout=20):
    raise NotImplementedError('TODO: implement')

def restart_eligible(state):
    """Enabled alone cannot distinguish an intentional stop from a failed workload."""
    raise NotImplementedError('TODO: implement')

def action_blocker(action, o):
    raise NotImplementedError('TODO: implement')

def observe():
    """A small dict of facts about the whole system; nothing here changes anything."""
    raise NotImplementedError('TODO: implement')

def score(o):
    """Observed unit/test issues, not resource efficiency; model availability is informational."""
    raise NotImplementedError('TODO: implement')

def rule_pick(o, allowed=None):
    """The fixed fallback: used when the model is down or its answer is not allowed. Also what the model is compared with."""
    raise NotImplementedError('TODO: implement')

def action_helped(record):
    """A failed/unmeasured action cannot take credit for an unrelated score drop."""
    raise NotImplementedError('TODO: implement')

def run_action(command, timeout):
    """Unlike observation sh(), execution must retain errors and return codes."""
    raise NotImplementedError('TODO: implement')

def history_stats(path=None):
    """Per action: how often it was tried and how often it lowered the score. Fed back into the prompt."""
    raise NotImplementedError('TODO: implement')

def struck_out(action, path=None, strikes=3):
    """True when the action's last `strikes` tries in a row all failed to lower the score: stop repeating it (found in the
    self-healing literature: restarting a thing that is failing for another reason fixes nothing; a human must look)."""
    raise NotImplementedError('TODO: implement')

def eligible_actions(o, history_path=None):
    raise NotImplementedError('TODO: implement')

def build_prompt(o, stats, allowed=None):
    raise NotImplementedError('TODO: implement')

def ask_model(prompt, post=None):
    """Returns the parsed JSON dict or None. Short timeout: the model may be busy with Ethan."""
    raise NotImplementedError('TODO: implement')

def choose(o, stats, ask=..., history_path=None):
    """Ask only when a permitted action remains within its repair budget."""
    raise NotImplementedError('TODO: implement')

def gate(o):
    """Reason not to run this cycle, or ''. Unknown telemetry is a reason: it must never authorize a cycle."""
    raise NotImplementedError('TODO: implement')

def cycle(plan_only=False, ask=..., observe_fn=..., run=None, out=None):
    raise NotImplementedError('TODO: implement')

def summary(path=None):
    """One plain paragraph for the status screen: cycles, how many acted, how many helped, model vs rule."""
    raise NotImplementedError('TODO: implement')

def cycle_lock_path():
    """Reuse the per-workspace host-local state location, never the synced OUT tree."""
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
