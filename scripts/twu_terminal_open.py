# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Open an allow-listed, hash-pinned .command file in a real Terminal.app window.

  twu_terminal_open.py open NAME [--yes-test]   look NAME up in the registry, confirm on the Mac, open
  twu_terminal_open.py list                     print the registry
  twu_terminal_open.py verify                   check every sha256 against the registry
  twu_terminal_open.py pin [--yes]              show hash diff; with --yes rewrite hashes

NAME is only ever a dictionary key. No command is built from it. Registry changes only by editing
data/dashboard/terminal_cmds/registry.json by hand and running `pin`. Non-interactive test mode
(skips the dialog) needs BOTH the flag --yes-test and env TWU_TERMINAL_NONINTERACTIVE=1.
Every request and decision is appended to data/health/terminal_open.ledger.jsonl.
Standard library only; no network.
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

def sha256_file(path):
    raise NotImplementedError('TODO: implement')

def load_registry(root):
    raise NotImplementedError('TODO: implement')

def _who():
    raise NotImplementedError('TODO: implement')

def log(root, name, decision, detail=..., who=None):
    raise NotImplementedError('TODO: implement')

def _as_quote(s):
    raise NotImplementedError('TODO: implement')

def dialog(entry, name, runner):
    """True only when the user clicks Open. Cancel, timeout, error: False."""
    raise NotImplementedError('TODO: implement')

def open_cmd(name, root=..., runner=..., interactive=True, who=None):
    """Returns (ok, message). Never raises for policy refusals."""
    raise NotImplementedError('TODO: implement')

def verify(root=...):
    raise NotImplementedError('TODO: implement')

def pin(root=..., yes=False, out=...):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
