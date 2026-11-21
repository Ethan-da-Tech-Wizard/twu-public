# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""relay_sync - build the paste-ready SYNC PROMPT for a fresh DeepSeek window. Stdlib only, offline, read-only.

DeepSeek starts with no memory every time, so the operator pastes this first. It carries: what the operator wants
(blanks to fill), the decisions waiting (section B of the handoff), this host's open alarms (scope-tagged), who is
connected, and the short core rules. It is scrubbed with relay_scrub.scrub_outbound (fail closed) and capped in bytes.

  python3 scripts/relay_sync.py [--max-bytes N]      prints the prompt; exit 1 and no output if the scrubber refuses
"""
from __future__ import annotations
import argparse
import json
import os
import platform
import re
import subprocess
import sys
from pathlib import Path

class SyncRefused(RuntimeError):
    """The scrubber is missing or blocked the text; nothing is emitted (fail closed)."""

def _scrubber():
    raise NotImplementedError('TODO: implement')

def _decisions(handoff):
    raise NotImplementedError('TODO: implement')

def _alarms(root, host):
    raise NotImplementedError('TODO: implement')

def _who(root):
    raise NotImplementedError('TODO: implement')

def _seats_summary(who):
    """One short line per seat: seat, CLI, status word. No hostnames or timestamps (the scrubber blocks them)."""
    raise NotImplementedError('TODO: implement')

def _fit(text, limit, label):
    raise NotImplementedError('TODO: implement')

def build_sync_prompt(root=..., host=None, handoff=None, who_text=None, max_bytes=...):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
