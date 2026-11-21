# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""twu_autonomy: what may run by itself (AUTO), what must ask (PROPOSE), what never happens (NEVER).

  twu_autonomy.py check ACTION     exit 0 AUTO, 3 PROPOSE, 4 NEVER, 2 error; prints the matching rule + source
  twu_autonomy.py list             every rule, expired ones marked
  twu_autonomy.py explain ACTION   why ACTION is classed as it is (all matching rules)
  twu_autonomy.py log [N]          last N decisions (default 20)
  twu_autonomy.py validate         check data/health/autonomy_policy.json

Policy file: data/health/autonomy_policy.json (Ethan edits it).  Rules: {id, class, match, reason, source, expires?}.
Several rules may match one action; NEVER beats PROPOSE beats AUTO.  No match = PROPOSE.
A missing policy uses the built-in seed; a malformed one FAILS CLOSED (everything PROPOSE).
A seeded NEVER rule cannot be removed or loosened unless the edited rule carries "explicit_widen": true AND an
"expires" date; without both, the built-in NEVER rule stays in force and validate reports it.
Expiry: an expired AUTO or PROPOSE rule is ignored (falls back to PROPOSE). An expired NEVER widening stops
applying, so the seeded NEVER returns. No network, no model calls; stdlib only.
"""
from __future__ import annotations
import fnmatch
import json
import os
import platform
import re
import sys
import time
from pathlib import Path

def _r(rid, cls, match, reason, source):
    raise NotImplementedError('TODO: implement')

def policy_path(root=...):
    raise NotImplementedError('TODO: implement')

def log_path(root=..., host=...):
    raise NotImplementedError('TODO: implement')

def _parse_expiry(v):
    """-> epoch seconds or raises ValueError. Accepts YYYY-MM-DD (end of that day UTC) or ISO date-time."""
    raise NotImplementedError('TODO: implement')

def load_policy(root=...):
    """-> (rules, problems, state). state: seed | file | failed_closed. Never raises."""
    raise NotImplementedError('TODO: implement')

def _active(rule, now):
    raise NotImplementedError('TODO: implement')

def classify(action, rules, state=..., now=None):
    """-> (class, rule|None, matches). NEVER > PROPOSE > AUTO; unknown or failed-closed = PROPOSE."""
    raise NotImplementedError('TODO: implement')

def _append_log(path, line, cap=None):
    raise NotImplementedError('TODO: implement')

def decide(action, root=..., host=..., now=None, log=True):
    """Classify ACTION, append the decision to the log, return 'AUTO' | 'PROPOSE' | 'NEVER'. Never raises."""
    raise NotImplementedError('TODO: implement')

def _show(rule):
    raise NotImplementedError('TODO: implement')

def main(argv=None, root=...):
    raise NotImplementedError('TODO: implement')
