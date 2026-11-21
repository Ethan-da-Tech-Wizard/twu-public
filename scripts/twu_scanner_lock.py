# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Alignment lock for the two TWU scanner venvs (offline; no network, no install).

  twu_scanner_lock.py verify   compare each venv's installed distributions (name+version) with the lock
  twu_scanner_lock.py status   print package counts per venv

Lock: data/external_scout/scanner_wheel_locks.json (PyPI sha256-verified wheels).
"""
import json
import re
import subprocess
import sys
from pathlib import Path

def norm(name):
    raise NotImplementedError('TODO: implement')

def load_lock(path=...):
    raise NotImplementedError('TODO: implement')

def installed(venv_dir):
    raise NotImplementedError('TODO: implement')

def compare(locked, have):
    """locked: {name: {version}}; have: {name: version}. Returns list of problem strings."""
    raise NotImplementedError('TODO: implement')

def verify(lock_path=..., base=...):
    raise NotImplementedError('TODO: implement')

def status(lock_path=...):
    raise NotImplementedError('TODO: implement')

def main(argv):
    raise NotImplementedError('TODO: implement')
