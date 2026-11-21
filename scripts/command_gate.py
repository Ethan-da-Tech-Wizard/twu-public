# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""command_gate.py — checks a shell command BEFORE it runs.

  python3 scripts/command_gate.py check "<command>"            # verdict only (exit 0 allow, 3 review, 4 block)
  python3 scripts/command_gate.py run "<command>"              # runs only if verdict is allow
  python3 scripts/command_gate.py run --approve <who> "<cmd>"  # review-level: snapshots files first, then runs
  python3 scripts/command_gate.py log [-n 20]                  # recent decisions

Verdicts: block (never runs) / review (needs --approve, files snapshotted first) / allow (read-only allowlist).
Anything unrecognised is "review". This catches bad commands and makes them undoable; it cannot prove a command is perfect.
Log: data/example_host/command_gate/log.jsonl. Snapshots: archive/<date>/command_gate/<time>/. Stdlib only.
"""
import argparse
import datetime
import json
import os
import re
import shlex
import shutil
import subprocess
import sys

def segments(cmd):
    """Split on ; && || | & and newlines (outside quotes) into token lists."""
    raise NotImplementedError('TODO: implement')

def resolve(p):
    raise NotImplementedError('TODO: implement')

def in_repo(path):
    raise NotImplementedError('TODO: implement')

def is_repository_root_operand(operand):
    """Recognize this synced repository root on either computer.

    The absolute prefix differs between macOS and Linux, so compare the
    resolved local root and fail closed for an absolute path with the same
    repository basename.
    """
    raise NotImplementedError('TODO: implement')

def classify(cmd):
    raise NotImplementedError('TODO: implement')

def bash_syntax(cmd):
    raise NotImplementedError('TODO: implement')

def snapshot(paths):
    raise NotImplementedError('TODO: implement')

def log(entry):
    raise NotImplementedError('TODO: implement')

def run_gated(cmd, approve=None, timeout=120):
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
