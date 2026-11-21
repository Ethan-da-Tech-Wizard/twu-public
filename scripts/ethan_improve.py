# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""One-page status for the auto-improve work (2026-11-01).

  ethan_improve.py status [--json] [--html]   short plain-English dashboard
  ethan_improve.py next                       only the next step
  ethan_improve.py decisions [list]           open questions for Ethan
  ethan_improve.py decisions answer ID yes|no|later

Cheap and read-only: small JSON files, two short local GETs, one nvidia-smi call.
No model requests. Missing source => 'unknown'. Only `decisions answer` and `--html` write files.
"""
from __future__ import annotations
import argparse
import calendar
import glob
import hashlib
import html
import json
import os
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

def _thermal_log_path(root):
    """Path of THIS computer's thermal guard log: data/thermal_guard.<host>.jsonl, else the legacy shared
    data/thermal_guard.jsonl (read-only fallback). Per-host since 2026-11-19 (Magi 10) so two computers
    never append to one synced file (a Syncthing conflict copy every few minutes)."""
    raise NotImplementedError('TODO: implement')

def jload(path):
    raise NotImplementedError('TODO: implement')

def get(url, timeout=1.5):
    raise NotImplementedError('TODO: implement')

def sha(path):
    raise NotImplementedError('TODO: implement')

def cpu_temp(root=...):
    raise NotImplementedError('TODO: implement')

def gpu_temp():
    raise NotImplementedError('TODO: implement')

def tail_lines(path, nbytes=65536):
    raise NotImplementedError('TODO: implement')

def collect(ai=..., repo=..., live=True, now=None):
    raise NotImplementedError('TODO: implement')

def next_step(r):
    raise NotImplementedError('TODO: implement')

def tf(v, unit=...):
    raise NotImplementedError('TODO: implement')

def lines(r):
    raise NotImplementedError('TODO: implement')

def render_html(r):
    raise NotImplementedError('TODO: implement')

def write_atomic(path, text):
    raise NotImplementedError('TODO: implement')

def answer(did, ans, path=...):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
