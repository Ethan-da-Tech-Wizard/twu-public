# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Light, deterministic host telemetry checked against the shared unsafe-things catalog.

One short run per interval (systemd user timer on Linux, LaunchAgent on macOS). No model calls,
no network, no payloads. It records METADATA ONLY: names, paths, hashes, fingerprints. It never
stores key/token/password/cookie/history contents.

Collects: running processes (name, exe path, user, parent), listening ports and established
outbound connections with their owning process, persistence points (systemd, cron/at, autostart,
shell rc files, ~/.local/bin, ssh authorized_keys fingerprints, sudoers.d, ld.so.preload, pacman
hooks; macOS LaunchAgents/Daemons, login-item database hash, profiles, quarantine-stripped
downloads), setuid/setgid files in common dirs, browser extension ids/names/permissions, kernel
modules, executables dropped in Downloads/tmp.

Evaluation reuses private/example_host/safety/unsafe_catalog.py (scope "host", rules UC-1xx in
data/safety/unsafe_catalog.json). The first run writes data/telemetry/<host>/baseline.json and
reports only absolute-rule hits; later runs also report items NEW or CHANGED since baseline.
`--accept` rolls the baseline forward after a human/Magi has reviewed the new items.

Outputs (host-owned, so Syncthing never conflicts): data/telemetry/<host>/{baseline.json,
runs.jsonl (bounded), latest.json, state.json}. Shared, human-edited policy:
data/telemetry/allowlist.json (documented benign items; they stay listed as ALLOWED, not hidden).

  python3 scripts/host_telemetry.py [--accept] [--no-notify] [--json] [--strict]
"""
from __future__ import annotations
import argparse
import base64
import hashlib
import json
import os
import platform
import plistlib
import re
import shutil
import stat
import subprocess
import sys
import time
from pathlib import Path
import unsafe_catalog as uc

def redact(text, limit=200):
    raise NotImplementedError('TODO: implement')

def sha256_file(path, cap=...):
    raise NotImplementedError('TODO: implement')

def read_text(path, limit=262144):
    raise NotImplementedError('TODO: implement')

class Ctx:
    """Where to look. Tests point root/home at temp fixtures and set live=False (no subprocess)."""

    def __init__(self, root=..., home=None, system=None, live=True, uid=None):
        raise NotImplementedError('TODO: implement')

    def R(self, p):
        raise NotImplementedError('TODO: implement')

    def short(self, p):
        raise NotImplementedError('TODO: implement')

    def item(self, cat, key, h=..., label=None, track=True):
        raise NotImplementedError('TODO: implement')

    def hit(self, rule_id, cat, key, evidence, **extra):
        raise NotImplementedError('TODO: implement')

    def scan(self, text, cat, key, only=None):
        """Run startup text through the shared catalog (scope host); comment lines are skipped by it."""
        raise NotImplementedError('TODO: implement')

    def listdir(self, d):
        raise NotImplementedError('TODO: implement')

    def run(self, argv, timeout=10):
        raise NotImplementedError('TODO: implement')

def collect_processes(ctx):
    raise NotImplementedError('TODO: implement')

def process_findings(ctx, procs):
    raise NotImplementedError('TODO: implement')

def split_addr(a):
    raise NotImplementedError('TODO: implement')

def is_loopback(h):
    raise NotImplementedError('TODO: implement')

def is_private(h):
    raise NotImplementedError('TODO: implement')

def collect_net(ctx):
    raise NotImplementedError('TODO: implement')

def net_findings(ctx, listen, estab):
    raise NotImplementedError('TODO: implement')

def file_item(ctx, cat, path, scan=True, only=None, track=True, label=None):
    raise NotImplementedError('TODO: implement')

def collect_systemd(ctx):
    raise NotImplementedError('TODO: implement')

def collect_cron(ctx):
    raise NotImplementedError('TODO: implement')

def collect_autostart(ctx):
    raise NotImplementedError('TODO: implement')

def collect_rc(ctx):
    raise NotImplementedError('TODO: implement')

def collect_local_bin(ctx):
    raise NotImplementedError('TODO: implement')

def collect_ssh_keys(ctx):
    raise NotImplementedError('TODO: implement')

def collect_sudoers(ctx):
    raise NotImplementedError('TODO: implement')

def collect_system_files(ctx):
    raise NotImplementedError('TODO: implement')

def collect_setuid(ctx):
    raise NotImplementedError('TODO: implement')

def collect_exec_drops(ctx):
    """Executable-looking regular files in Downloads/tmp (depth<=2). Hashes compared to the known-bad list."""
    raise NotImplementedError('TODO: implement')

def collect_browser_ext(ctx):
    raise NotImplementedError('TODO: implement')

def _add_ext(ctx, browser, eid, name, version, perms):
    raise NotImplementedError('TODO: implement')

def collect_kmods(ctx):
    raise NotImplementedError('TODO: implement')

def expected_users(ctx):
    raise NotImplementedError('TODO: implement')

def collect_accounts(ctx):
    """Users, UID 0, shells, privileged-group membership, /etc/shadow metadata (never contents)."""
    raise NotImplementedError('TODO: implement')

def _recent(ts_text, days=7):
    raise NotImplementedError('TODO: implement')

def parse_last(ctx, text, expected):
    raise NotImplementedError('TODO: implement')

def parse_journal(ctx, text, expected):
    raise NotImplementedError('TODO: implement')

def check_log_tamper(ctx):
    """A login/audit log that shrank since the last run is a tamper sign (rotation also does this; REVIEW)."""
    raise NotImplementedError('TODO: implement')

def collect_logins(ctx):
    raise NotImplementedError('TODO: implement')

def load_json(path, default):
    raise NotImplementedError('TODO: implement')

def write_json(path, obj):
    raise NotImplementedError('TODO: implement')

def inventory_map(items):
    raise NotImplementedError('TODO: implement')

def allow_match(entry, f):
    raise NotImplementedError('TODO: implement')

def evaluate(raw_hits, ctx, baseline, allow):
    """Turn absolute hits + new/changed-vs-baseline into findings with PASS/REVIEW/FAIL severity."""
    raise NotImplementedError('TODO: implement')

def verdict_of(findings):
    raise NotImplementedError('TODO: implement')

def host_name():
    raise NotImplementedError('TODO: implement')

def data_dir():
    raise NotImplementedError('TODO: implement')

def notify(title, body, urgent):
    raise NotImplementedError('TODO: implement')

def compose_notice(fresh, host):
    raise NotImplementedError('TODO: implement')

def _canon(rec):
    raise NotImplementedError('TODO: implement')

def chain_append(path, rec):
    """Append rec with prev = sha256 of the previous line's exact text. Append-only by construction."""
    raise NotImplementedError('TODO: implement')

def verify_chain(path):
    """(ok, records, problem). Detects edited or deleted-in-the-middle records; a deleted TAIL needs a peer copy."""
    raise NotImplementedError('TODO: implement')

def compare_peer(local_path, peer_path):
    """Compare the peer's copy of this host's chain with ours. Returns (ok, message)."""
    raise NotImplementedError('TODO: implement')

def rotate_runs(path):
    raise NotImplementedError('TODO: implement')

def collect_all(ctx):
    raise NotImplementedError('TODO: implement')

def run(ctx, out_dir, host, accept=False, notify_on=True, now=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
