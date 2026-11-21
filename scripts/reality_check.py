# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""reality_check: find places where the docs disagree with reality, so no AI (or person) is misled by them.

  reality_check.py check                  scan; write data/netguard/REALITY.<host>.json; exit 1 if unaccepted findings
  reality_check.py report                 print findings grouped by file
  reality_check.py accept ID --reason T   record a finding as accepted (reason required)
  reality_check.py status                 one-line state of the last receipt

Kinds: file-missing (backticked repo path does not exist), service-missing (com.twu.* / twu-*.service|timer documented but no
template in MAGI_0/ and not installed), service-not-installed (informational, macOS only: template exists, not installed here),
retired-name (host from data/retired_hosts.json named in a live doc). Stdlib only, no network, reads only the workspace
plus the NAMES in ~/Library/LaunchAgents.
"""
from __future__ import annotations
import argparse, hashlib, json, os, platform, re, socket, sys, time
from pathlib import Path

def doc_files(root=...):
    raise NotImplementedError('TODO: implement')

def _fid(kind, file, subject):
    raise NotImplementedError('TODO: implement')

def _retired_names(root):
    raise NotImplementedError('TODO: implement')

def _installed(home):
    raise NotImplementedError('TODO: implement')

def findings(root=..., home=None, system=None):
    raise NotImplementedError('TODO: implement')

def _accepted(d):
    raise NotImplementedError('TODO: implement')

def check(root=..., d=None, home=None, system=None):
    raise NotImplementedError('TODO: implement')

def _unaccepted(r, d):
    raise NotImplementedError('TODO: implement')

def accept(fid, reason, d=None, r=None):
    raise NotImplementedError('TODO: implement')

def alarm_problems(now=None, d=None):
    raise NotImplementedError('TODO: implement')

def _load(d):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
