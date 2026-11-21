# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
from __future__ import annotations
import argparse
import json
import os
import platform
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import time
from pathlib import Path

def run(args, timeout=30):
    """Run an argument list (never a shell). Returns (rc, stdout, stderr). rc 127 = not installed, 124 = timed out."""
    raise NotImplementedError('TODO: implement')

def host_name():
    raise NotImplementedError('TODO: implement')

def detect_os(os_release=..., system=None):
    """'example_host', 'arch', 'macos' or None. Exact ID match only (Manjaro or Ubuntu are NOT arch or example_host)."""
    raise NotImplementedError('TODO: implement')

def load_playbooks(path=None):
    raise NotImplementedError('TODO: implement')

def item(value, state, detail, how):
    """One status fact: value, state ok|warn|unknown, a plain sentence, and the command or file it came from."""
    raise NotImplementedError('TODO: implement')

def _unknown(detail, how):
    raise NotImplementedError('TODO: implement')

def check_disk(disk_usage=...):
    raise NotImplementedError('TODO: implement')

def _count_lines(text):
    raise NotImplementedError('TODO: implement')

def check_failed_units_linux(runner=...):
    raise NotImplementedError('TODO: implement')

def check_failed_units_macos(runner=...):
    raise NotImplementedError('TODO: implement')

def _pk_updates(runner, refresh):
    """Updates via PackageKit (pkcon), which a normal user may ask read-only (dnf5 cannot read its system state without root).
    Without --refresh it uses PackageKit's cached lists (fast, no network of its own, may be hours old); with --refresh it asks
    PackageKit to refresh first. Returns an item or None when pkcon is unavailable."""
    raise NotImplementedError('TODO: implement')

def example_host_updates(runner=..., refresh=False):
    """dnf5 as a normal user fails reading its system state, so PackageKit is the read-only way to count updates here."""
    raise NotImplementedError('TODO: implement')

def arch_updates(runner=..., refresh=False):
    raise NotImplementedError('TODO: implement')

def macos_updates(runner=..., refresh=False):
    raise NotImplementedError('TODO: implement')

def example_host_reboot(runner=...):
    raise NotImplementedError('TODO: implement')

def arch_reboot(runner=..., isdir=...):
    raise NotImplementedError('TODO: implement')

def macos_reboot(runner=...):
    raise NotImplementedError('TODO: implement')

def example_host_last_update(runner=...):
    raise NotImplementedError('TODO: implement')

def arch_last_update(read=None, log=...):
    raise NotImplementedError('TODO: implement')

def macos_last_update(runner=...):
    raise NotImplementedError('TODO: implement')

def snapshots_linux(listdir=...):
    raise NotImplementedError('TODO: implement')

def snapshots_macos(runner=...):
    raise NotImplementedError('TODO: implement')

def collect_status(os_id, runner=..., refresh=False, now=None, host=None, disk_usage=...):
    """Gather every fact for THIS computer. Never raises; a fact that cannot be read is 'unknown' with the reason."""
    raise NotImplementedError('TODO: implement')

def write_status(status, directory=None):
    """Atomic write of status.<host>.json (one file per computer)."""
    raise NotImplementedError('TODO: implement')

def os_for_host(host, playbooks):
    raise NotImplementedError('TODO: implement')

def job_steps(playbooks, os_id, job):
    raise NotImplementedError('TODO: implement')

def is_sudo(cmd):
    raise NotImplementedError('TODO: implement')

def card_groups(steps):
    """Split a job into cards: consecutive command steps with the same sudo-ness share a card (the card linter refuses a card
    that mixes sudo and non-sudo). Notes (command null) ride with the first card. Returns [{'steps': [...], 'sudo': bool}]."""
    raise NotImplementedError('TODO: implement')

def build_cards(playbooks, os_id, job, host):
    """The card specs (label, on, runs, why, undo, verify, notes, done_check) for one job on one computer."""
    raise NotImplementedError('TODO: implement')

def open_labels(lister=None):
    """Labels of owner cards that are still open, so a re-run does not post the same card twice."""
    raise NotImplementedError('TODO: implement')

def post_card(card, poster=None):
    """Post one card with owner_command.py add. Returns (ok, output)."""
    raise NotImplementedError('TODO: implement')

def lint_playbooks(playbooks):
    """Every command in the playbook through the owner-card linter. Returns a list of 'os/job/step: problem' strings."""
    raise NotImplementedError('TODO: implement')

def render_doc(playbooks):
    raise NotImplementedError('TODO: implement')

def main(argv=None, runner=...):
    raise NotImplementedError('TODO: implement')
