# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Execution-verified BIG-TASK training pairs: typo'd, vaguely worded build asks -> write_file -> run -> verify -> truthful answer.

Every chain is EXECUTED for real in a scratch dir (bwrap, no network) through ethan_bigtask_probe.run_tool; a scenario is kept only if
all outputs exist, are non-empty, and every name/size in the final answer appears in the tool output. Nothing is model-labeled. The
prompt is the bridge's slim prompt plus a versioned synthetic BIG TASKS fixture. This does not claim parity with production CLI context.
Domains here are disjoint from the probe's held-out domains (office, hr, sales, budget, inventory, coffee, clinic, school, finance).

  python3 scripts/ethan_bigtask_pairs.py build [--out data/autoimprove/20261102/cli_real/pairs_bigtask.jsonl]
"""
from __future__ import annotations
import argparse
import hashlib
import json
import random
import shutil
import sys
from pathlib import Path
import ethan_bigtask_probe as bp
import ethan_cli_real as cr

def gen_script(domain, spec, seed):
    raise NotImplementedError('TODO: implement')

def deck_script(domain):
    raise NotImplementedError('TODO: implement')

def app_script(kind, stem):
    raise NotImplementedError('TODO: implement')

def execute(steps, root):
    raise NotImplementedError('TODO: implement')

def shell(out):
    raise NotImplementedError('TODO: implement')

def build_scenarios():
    raise NotImplementedError('TODO: implement')

def run_scenario(scn, idx):
    raise NotImplementedError('TODO: implement')

def render(ep, system, tools, guidance):
    raise NotImplementedError('TODO: implement')

def cmd_build(a):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
