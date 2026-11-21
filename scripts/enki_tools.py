# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/enki_tools.py - Enki's tool catalog: every wired tool is listed, classified, smoke-checked and runnable by name.

Stdlib only; no model, no network. A tool is "wired" when data/enki_tools.json lists it AND its latest smoke receipt
matches the script's current sha256 and passed. A mention in a doc is not wiring.

  python3 scripts/enki tools list [--json]          # what Enki can reach, with class and smoke state
  python3 scripts/enki tools describe NAME          # purpose, class, entry, last smoke
  python3 scripts/enki tools sync --add NAME...     # list tools (class is computed from the source); never removes
  python3 scripts/enki tools sync --all [--smoke]   # list every runnable tool in the registry not yet listed (and smoke the new ones)
  python3 scripts/enki tools smoke [NAME|--all]     # prove each tool still loads: --help when import is side-effect free, else compile only
  python3 scripts/enki tools check                  # exit 1 if a listed tool is missing, changed class, or has no fresh passing smoke
  python3 scripts/enki tools run NAME [-- ARGS]     # run a tool; classes other than "read" need --approve-class CLASS

Classes are computed from the source, strictest wins: external (network/mail), system (processes, hardware, services),
writes (files), read (none of those). `run` refuses anything stricter than "read" without an explicit approval, refuses
under business/example_host/comms/STOP, and appends every run to data/tool_trials/enki_tools/runs.jsonl.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
import sys as _sys
import host_paths

def _sha(path):
    raise NotImplementedError('TODO: implement')

def _load(path):
    raise NotImplementedError('TODO: implement')

def code_views(source):
    """(code, ext) or None if the source cannot be parsed (caller then fails closed).

    code: comments and docstrings blanked. ext: code with every non-docstring string literal that contains whitespace
    (prose, HTML, messages) reduced to just its 'import x' / 'from x' fragments, so prose cannot hide or fake a network
    module but "python3 -c 'import socket'" and ["curl", ...] style single-token arguments still count."""
    raise NotImplementedError('TODO: implement')

def _has(source, markers, whole):
    raise NotImplementedError('TODO: implement')

def _benign_module_uses(text):
    """Return text with benign socket (hostname only) and urllib.parse uses removed, so only real network markers remain."""
    raise NotImplementedError('TODO: implement')

def classify(source):
    """Strictest class whose markers appear in the executable code.

    Comments and docstrings are ignored (prose cannot change a class); EXTERNAL/SYSTEM markers match whole words so
    'socketfilterfw' is not 'socket'. String literals that are command arguments still count. If the source cannot be
    parsed, fall back to plain substring matching over the whole text (stricter)."""
    raise NotImplementedError('TODO: implement')

def _calls_are_safe(node):
    raise NotImplementedError('TODO: implement')

def import_is_safe(source):
    """True when importing the module only defines things: imports, defs, classes, constants, a main guard."""
    raise NotImplementedError('TODO: implement')

def script_path(root, name):
    raise NotImplementedError('TODO: implement')

def smoke_one(root, name, run=...):
    raise NotImplementedError('TODO: implement')

def build_entry(root, name):
    raise NotImplementedError('TODO: implement')

def runnable_names(root):
    raise NotImplementedError('TODO: implement')

def load_manifest(root):
    raise NotImplementedError('TODO: implement')

def sync(root, names):
    raise NotImplementedError('TODO: implement')

def smoke(root, names, run=...):
    raise NotImplementedError('TODO: implement')

def wired(root):
    """Names whose manifest entry is live and whose latest smoke receipt passed for the script's current hash."""
    raise NotImplementedError('TODO: implement')

def _review_accepts(tool, now, path):
    """A recorded human/agent review clears the 'class is now stricter' flag only for the exact script it examined.

    manifest entry: "reviewed": {"class": <computed class it examined>, "sha256": <script hash>, "reason": ..., "by": ..., "date": ...}.
    Any change to the script (hash differs) or a still-stricter computed class brings the flag back. The tool's own class is not
    lowered or raised by a review; run_tool keeps gating on the manifest class."""
    raise NotImplementedError('TODO: implement')

def check(root):
    raise NotImplementedError('TODO: implement')

def run_tool(root, name, args, approved=..., run=..., now=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
