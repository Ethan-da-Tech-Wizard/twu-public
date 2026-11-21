# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Read-only Git health check for the Ethan CLI gate (Python 3.9, stdlib only).

Commands: status | why | write | --json.  No network, no model, no daemon.
It never changes Git state: every git call goes through safe_run(), which refuses
anything that is not on a small read-only allowlist.  The only file it writes is
data/dashboard/githealth.<host>.json (atomically) and only for `write`.
The gate verdict re-implements the plain `begin` checks of scripts/ethan_git_guard.py
(the launcher runs `ethan_git_guard.py begin || exit 43`; stderr shows
"Git safety gate: <reason>").  When a check cannot be completed the verdict is UNKNOWN.
"""
import argparse
import json
import os
import re
import socket
import subprocess
import sys
import tempfile
import time
from collections import Counter
from pathlib import Path

class MutationRefused(RuntimeError):
    pass

def _is_read_only(args):
    raise NotImplementedError('TODO: implement')

def safe_run(runner, args, timeout=...):
    raise NotImplementedError('TODO: implement')

def real_runner(root):
    raise NotImplementedError('TODO: implement')

def host_tag():
    raise NotImplementedError('TODO: implement')

def _parse_porcelain(text):
    raise NotImplementedError('TODO: implement')

def _manifest(root):
    raise NotImplementedError('TODO: implement')

def _gate(f):
    """Mirror ethan_git_guard.begin() (no --paths). Returns (verdict, code, reason)."""
    raise NotImplementedError('TODO: implement')

def _steps(code, f):
    raise NotImplementedError('TODO: implement')

def is_safe_step(step):
    raise NotImplementedError('TODO: implement')

def collect(root, runner, now=None):
    raise NotImplementedError('TODO: implement')

def status_table(r):
    raise NotImplementedError('TODO: implement')

def why(r):
    raise NotImplementedError('TODO: implement')

def write_report(root, runner, report=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
