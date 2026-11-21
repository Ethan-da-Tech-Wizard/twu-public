# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Big-task probe: does the local 7B DO a large multi-step build ask (typo'd, vaguely worded) instead of refusing?

Replays the real CLI turn shape (slim system prompt, native tools incl. write_file/replace, an explicit synthetic guidance fixture in the first user message,
CLI sampling with the bridge's tool-turn cap) straight against the model server, runs every tool call for real inside a bwrap example_host
(network off, only the scratch task dir writable), and scores with deterministic file checks: outputs exist and are non-empty.
Nothing is model-judged. Generated output lives under /mnt/GameDrive/twu_scratch/bigtask, never in the repo.

  python3 scripts/ethan_bigtask_probe.py list
  python3 scripts/ethan_bigtask_probe.py run --label before --guidance base [--refusal] [--asks id,id] [--turns 24]
  python3 scripts/ethan_bigtask_probe.py pairs [--out FILE]     # executed-verified gold chains -> training pairs (slim format)

--guidance base|big : reproducible synthetic task fixtures, not current production CLI policy; big adds scoped artifact/verification directives. --refusal turns on the bridge
refusal rescue (ETHAN_BRIDGE_REASK_REFUSAL) in-process. Needs the model on 18190; run one at a time (single slot).
"""
from __future__ import annotations
import argparse
import copy
from datetime import datetime, timezone
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.request
from pathlib import Path
import ethan_cli_real as cr
import ethan_cli_real_slim as crs
import gemini_broker_bridge as gb

def _n(d, pat):
    raise NotImplementedError('TODO: implement')

def _deck(d):
    raise NotImplementedError('TODO: implement')

def _has(d, pat):
    raise NotImplementedError('TODO: implement')

def guidance_text(mode):
    raise NotImplementedError('TODO: implement')

def system_and_tools():
    raise NotImplementedError('TODO: implement')

def first_user(ask, cwd, guidance):
    raise NotImplementedError('TODO: implement')

def safe_delete_file(file_path: str | Path, cwd: Path, receipt_dir: Path | None=None) -> tuple[bool, str]:
    """Safely delete a file with example_host boundary check, refusal for critical system files,
    and audit logging to data/receipts/file_deletion_receipts.jsonl."""
    raise NotImplementedError('TODO: implement')

def run_tool(name, args, cwd):
    raise NotImplementedError('TODO: implement')

def post_model(req):
    raise NotImplementedError('TODO: implement')

def model_request(msgs, tools):
    raise NotImplementedError('TODO: implement')

def episode(ask, cwd, guidance, refusal, max_turns=24, post=...):
    """Drive one ask to the end. Returns (transcript, final_text, calls, refused_first)."""
    raise NotImplementedError('TODO: implement')

def claims_done(final):
    raise NotImplementedError('TODO: implement')

def cmd_run(a):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
