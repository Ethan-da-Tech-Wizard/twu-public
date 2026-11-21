# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""publish_public: the ONLY way anything from this system may reach GitHub. DRY-RUN BY DEFAULT. Never run by agents.

  publish_public.py [--staging DIR] [--repo NAME]                       dry run: check every gate, print file count, change nothing
  publish_public.py --execute [--staging DIR] [--repo NAME]             create PRIVATE repo + push staging only, leak-watch once, write receipt
  publish_public.py --execute --public --confirm "PHRASE" ...           additionally flip to public (separate step, needs the phrase)

Gates (all must hold): audit receipt data/health/PUBLIC_AUDIT_RECEIPT.json verdict PASS, tree_hash == current staging tree hash,
younger than 30 min; staging is its own git repo (toplevel == staging) whose tracked files == the staged tree, no remotes yet other than the target;
gh login == pinned owner (github_leak_watch.OWNER, env TWU_GITHUB_OWNER); the private workspace is never the cwd of a push.
Uses existing gh auth; no token is read or printed. Receipt: data/health/PUBLIC_PUBLISH_RECEIPT.json (counts and hashes only).
"""
from __future__ import annotations
import argparse, hashlib, json, subprocess, sys, time
from pathlib import Path

class Refuse(Exception):
    pass

def run(cmd, cwd=None, timeout=120):
    raise NotImplementedError('TODO: implement')

def tree_hash(d: Path):
    """sha256 over sorted (relative path, file sha256), skipping .git. Returns (hash, file_count)."""
    raise NotImplementedError('TODO: implement')

def pinned_owner():
    raise NotImplementedError('TODO: implement')

def check_audit(staging: Path, now=None, audit=None):
    raise NotImplementedError('TODO: implement')

def check_staging(staging: Path):
    raise NotImplementedError('TODO: implement')

def check_owner(login_fn=None):
    raise NotImplementedError('TODO: implement')

def gates(staging: Path, login_fn=None):
    raise NotImplementedError('TODO: implement')

def execute(staging: Path, repo: str, owner: str, th: str, n: int, public: bool, confirm: str):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
