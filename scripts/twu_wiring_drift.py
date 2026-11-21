# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/twu_wiring_drift.py - detection-only wiring drift reporter for scripts/ tools.

Stdlib only; deterministic; no model, no network, never runs a proposed command. Compares scripts/*.py (and *.sh) tools with
data/enki_tools.json, data/tool_registry.json, data/command_registry.json, data/wiring_manifest.json and the smoke receipt
data/tool_trials/enki_tools/LATEST.json (via enki_tools.check/classify). Writes ONLY data/health/wiring_drift.<hostname>.json
(a snapshot of script sha256s), never the registries; --dry-run writes nothing.

  python3 scripts/twu_wiring_drift.py [--root PATH] [--json] [--dry-run] [--since-snapshot]

Drift kinds: unregistered, changed_since_smoke, no_smoke_receipt, smoke_failed, class_drift, missing_test,
registered_missing_script, unregistered_shell, changed_since_snapshot, new_since_snapshot, removed_since_snapshot
(the last three only with --since-snapshot). Exit 0 clean, 1 drift. proposed_commands are text for a human or Magi.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import socket
import sys
from pathlib import Path
import enki_tools
import tool_registry

def snapshot_path(root, host=None):
    raise NotImplementedError('TODO: implement')

def _load(path):
    raise NotImplementedError('TODO: implement')

def _sha(path):
    raise NotImplementedError('TODO: implement')

def discover(root, snapshot_names=..., manifest_names=...):
    """{name: {"path", "sha256", "kind": py|sh}} for scripts that look like tools."""
    raise NotImplementedError('TODO: implement')

def _command_entries(root):
    raise NotImplementedError('TODO: implement')

def _manifest_files(root):
    raise NotImplementedError('TODO: implement')

def scan(root, since_snapshot=False, host=None):
    raise NotImplementedError('TODO: implement')

def proposed(findings, tools):
    """Exact existing commands a human/Magi would run; this module never runs them."""
    raise NotImplementedError('TODO: implement')

def build_report(root, since_snapshot=False, host=None):
    raise NotImplementedError('TODO: implement')

def write_snapshot(root, tools, host=None):
    raise NotImplementedError('TODO: implement')

def summary(report, wrote):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
