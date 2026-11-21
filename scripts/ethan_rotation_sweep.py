# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Discovery sweeper + nagger for credential rotation (example_host, example_host, Ethans-example_host).

ONE-SHOT (run by a timer). Finds accounts/logins/credentials that exist on THIS host and makes sure
Ethan registers each in the rotation tracker (scripts/ethan_rotation.py) or explicitly ignores it.

Metadata only. It never prints, stores or sends a secret: account names, key FINGERPRINTS (from
`ssh-keygen -lf` on .pub / authorized_keys, never private key files), registry HOSTNAMES, connection
NAMES, environment variable NAMES. Files that can hold secrets (.netrc, .env, rc files,
.git-credentials, docker config.json) are parsed with name/host-only patterns and the values are
dropped in the same expression.

Writes only (data/rotation/, one writer per host):
  discovered.<host>.json   {"checked", "items":[{key,kind,label,source,first_seen,status}]}
  nag_state.<host>.json    when each new item was last nagged
  sweep.log.jsonl          append-only one-line receipt per sweep
Reads decisions.<host>.json (owned by the tracker): {key: 'registered'|'ignored'} or {key:{status:..}}.
"""
from __future__ import annotations
import argparse
import json
import os
import re
import socket
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import urlparse
import stop_latch

def this_host() -> str:
    raise NotImplementedError('TODO: implement')

def rot_dir() -> Path:
    raise NotImplementedError('TODO: implement')

def default_run(cmd, timeout=15):
    """Run a command, return stdout text or None on any failure. No shell, no network side effects."""
    raise NotImplementedError('TODO: implement')

def host_of(url: str) -> str:
    """Hostname only from a URL / scp-style git remote; credentials in the userinfo are discarded."""
    raise NotImplementedError('TODO: implement')

def item(key, kind, label, source):
    raise NotImplementedError('TODO: implement')

def local_users(run, passwd=..., darwin=None):
    raise NotImplementedError('TODO: implement')

def fingerprints(run, path: Path):
    raise NotImplementedError('TODO: implement')

def ssh_keys(run, home: Path):
    raise NotImplementedError('TODO: implement')

def docker_hosts(home: Path):
    raise NotImplementedError('TODO: implement')

def netrc_hosts(home: Path):
    raise NotImplementedError('TODO: implement')

def git_cred_hosts(run, home: Path, repos):
    raise NotImplementedError('TODO: implement')

def known_repos(home: Path):
    raise NotImplementedError('TODO: implement')

def split_nmcli(line: str):
    raise NotImplementedError('TODO: implement')

def network_names(run, darwin=None):
    raise NotImplementedError('TODO: implement')

def names_in_file(path: Path):
    """Secret-looking variable NAMES only; each line's value is never kept."""
    raise NotImplementedError('TODO: implement')

def env_files(home: Path, repo: Path):
    raise NotImplementedError('TODO: implement')

def env_names(home: Path, repo: Path):
    raise NotImplementedError('TODO: implement')

def app_presence(home: Path):
    raise NotImplementedError('TODO: implement')

def parse_last(text: str):
    """`last` lines -> [(user, host)] for REMOTE logins only (IP/hostname). Local ones (tty, :0, tmux, pts) are skipped."""
    raise NotImplementedError('TODO: implement')

def logins(run):
    raise NotImplementedError('TODO: implement')

def discover(run=..., home: Path | None=None, repo: Path=..., passwd=..., darwin=None):
    raise NotImplementedError('TODO: implement')

def read_json(path: Path, default):
    raise NotImplementedError('TODO: implement')

def write_atomic(path: Path, obj):
    raise NotImplementedError('TODO: implement')

def decision_of(v):
    raise NotImplementedError('TODO: implement')

def merge(found, previous, decisions, now):
    raise NotImplementedError('TODO: implement')

def due_nags(items, nag, now):
    """Keys to nag now: never nagged, else daily, else every 4h once older than 3 days."""
    raise NotImplementedError('TODO: implement')

def notify(run, title, body, darwin=None):
    raise NotImplementedError('TODO: implement')

def sweep(d: Path, host: str, run=..., home=None, repo=..., passwd=..., darwin=None, now=None, send_notify=True):
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
