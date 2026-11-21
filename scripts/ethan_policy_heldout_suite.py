# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Held-out adversarial suite for scripts/ethan_gemini_policy.toml.

Authored 2026-11-02 by Magi 15 (Claude) after reading only the CATEGORY comments and a few sample lines of
scripts/ethan_policy_bypass_suite.py, answering the outside criticism that the 506-case suite is self-written.
It is NOT independent of the project (same author organisation, same session) and it is small: it shows how the
policy behaves on cases written without tuning the policy to them, nothing more. It is scored separately.

Cases are run through the same real PolicyEngine path (`decide`) as the main suite. Any unexpected allow is a real
bug and is reported, never hidden. Benign controls guard against a policy that simply denies everything.

  python3 scripts/ethan_policy_heldout_suite.py [--mode user|launcher|both] [--json PATH]
"""
import json
import sys
from pathlib import Path
import ethan_policy_bypass_suite as base

def sh(cmd):
    raise NotImplementedError('TODO: implement')

def ok(cmd):
    raise NotImplementedError('TODO: implement')

def run(mode):
    raise NotImplementedError('TODO: implement')
