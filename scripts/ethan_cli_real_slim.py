# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""pairs_v5_slim: the pairs_v4 scenarios (same seed, same 650 verified episodes) rendered with the bridge's SLIM prompt.

The system prompt and tool prose are produced by gemini_broker_bridge.apply_slim_prompt() itself (never copied), so the training
format cannot drift from what the CLI sends when ETHAN_BRIDGE_SLIM_PROMPT=<level>. Re-run this script if the bridge's slim
function changes; the manifest records the slim sha so a stale file is detectable (`check`).

Differences from v4 beyond the prompt: refusal answers name the refused command (no canned boilerplate); every non-refusal answer
is re-verified to contain the expected values AND those values must be in the tool output (already enforced by build_scenarios).

  python3 scripts/ethan_cli_real_slim.py build [--level 2] [--out-dir DIR]
  python3 scripts/ethan_cli_real_slim.py check [--out-dir DIR]   # leak/hold-out + staleness + tail checks, no model
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import sys
from pathlib import Path
import ethan_cli_real as cr
import gemini_broker_bridge as gb

def slim_template(level):
    raise NotImplementedError('TODO: implement')

def refusal_answer(scn):
    raise NotImplementedError('TODO: implement')

def render(scn, tpl, outs):
    raise NotImplementedError('TODO: implement')

def build_all(seed, n, n_eval, level):
    raise NotImplementedError('TODO: implement')

def check_rows(rows, train, ev):
    raise NotImplementedError('TODO: implement')

def cmd_build(a):
    raise NotImplementedError('TODO: implement')

def cmd_check(a):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
