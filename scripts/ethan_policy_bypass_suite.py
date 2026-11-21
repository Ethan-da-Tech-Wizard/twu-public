# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Bypass + regression suite for scripts/ethan_gemini_policy.toml, run through the REAL gemini-cli PolicyEngine.

  * VERIFIER_145: the independent verifier's 145 attempts (data/autoimprove/20261101/verify/tooluse_v3_bypass.py), with the
    expected decision of the allowlist policy (two deliberate differences are annotated).
  * MINE: 120+ further attempts across obfuscation, wrappers, shells, interpreters, python -c, git, network, destructive
    commands, secret/glob/quote-split paths, protected-file writes, redirections, file tools and argument smuggling.
  * BENIGN_EXTRA: ordinary read-only / workspace commands that must stay allowed.
Engine modes:  "user"  = the toml loaded as the user tier (what scripts/test_ethan_gemini_policy.py always did);
               "launcher" = what `ethan chat` really does: the deny rules are copied into an admin-tier snapshot, the
               whole file is loaded as the user tier, and both are given to one PolicyEngine (yolo approval mode).
Run:  python3 scripts/ethan_policy_bypass_suite.py [--mode user|launcher|both] [--json out.json]
Exit status 1 when any attempt gets an unexpected decision (an unexpected ALLOW of an attack is the dangerous one).
Heavy batches wait while data/health/GPU_WINDOW exists (poll 60 s, up to 40 min) unless ETHAN_POLICY_SUITE_NO_WAIT=1.
"""
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

def sh(cmd, exp=..., note=...):
    raise NotImplementedError('TODO: implement')

def wait_for_gpu_window():
    raise NotImplementedError('TODO: implement')

def gemini_entry():
    raise NotImplementedError('TODO: implement')

def decide(calls, mode=..., policy=..., chunk=250, timeout=45, retries=2, extra_policy=None):
    """calls: [(tool, args[, server])] -> [{'decision','message'}] from the REAL PolicyEngine.  A hung node is killed after
    `timeout` seconds and the chunk retried (Popen + communicate so only our own child is ever killed)."""
    raise NotImplementedError('TODO: implement')

def run(mode=..., verbose=True, extra_policy=None):
    """Returns dict with unexpected allows (dangerous), unexpected denies (usability) and counts."""
    raise NotImplementedError('TODO: implement')
