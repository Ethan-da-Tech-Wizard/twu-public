# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""twu_forever: can Ethan rebuild and run the system with no cloud AI and no internet?  (Python 3.9, stdlib only;
no network, no model, no daemon.)

  twu_forever.py check [--json] [--root DIR] [--no-hash]
      verify the FOREVER KIT, print a table, write data/health/forever.<host>.json atomically.
      Exit 1 when any check is 'fail', else 0.

  twu_forever.py hash [--root DIR] [--dir DIR]
      stream-hash every .gguf in ~/.cache/local_models (read only, nice'd, progress per GiB, resumable: unchanged
      size+mtime is skipped) into data/health/model_weights_manifest.json (atomic write).
  twu_forever.py verify-copy SRC DEST
      sha256 both; equal => record a verified copy in the manifest.  Refuses DEST under ~/.cache/local_models.
  twu_forever.py record-copy NAME --where TEXT --size N --method TEXT
      record a copy verified another way (size only = weaker evidence).

Checks (each reports only what it measured; anything it cannot measure is 'unknown', never 'ok'):
  models    every .gguf named in the repo's model registry/identity files: exists, size, sha256 vs the hash the
            repo recorded (if the repo recorded none: 'no recorded hash', which is NOT ok)
  cli       scripts/ethan exists and `scripts/ethan --help` (metadata only path) runs within 20 s; same for scripts/enki
  imports   static scan (ast) of critical scripts for TOP-LEVEL imports of cloud-AI SDKs, or of network libraries
            together with non-loopback URL literals.  Loopback-only is allowed.
  backups   `ethan_backup.py --status` (read-only) + restore-drill / repository-check records in data/backup
  library   offline library, Arch wiki and ethan_know index exist; `ethan_know.py freshness`
  runbook   docs/FOREVER_RUNBOOK.md present, not stale, every script path in its fenced blocks exists
  limits    what this program can NOT prove from one box

Runbook staleness rule: STALE when the newest script the runbook cites is more than 30 days newer than the runbook.

Result shape (same vocabulary as twu_integrity.py): {id, title, status, detail, evidence, rows?} with status in
ok / unknown / warn / fail; overall = worst check.
"""
import argparse
import ast
import datetime
import hashlib
import json
import os
import platform
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

def res(cid, title, status, detail, evidence=..., rows=None):
    raise NotImplementedError('TODO: implement')

def worst(statuses):
    raise NotImplementedError('TODO: implement')

def run(argv, timeout, cwd=None, env=None):
    """(rc, stdout, stderr); rc None when the command could not run or timed out."""
    raise NotImplementedError('TODO: implement')

def fmt_age(sec):
    raise NotImplementedError('TODO: implement')

def fmt_size(n):
    raise NotImplementedError('TODO: implement')

def read_text(p):
    raise NotImplementedError('TODO: implement')

def sha256_file(path):
    raise NotImplementedError('TODO: implement')

def _walk_json(node, names, hashes):
    """Collect .gguf names and recorded sha256 values (keyed by basename) from any JSON structure."""
    raise NotImplementedError('TODO: implement')

def _scan_file(path, names, hashes):
    raise NotImplementedError('TODO: implement')

def local_search_roots():
    raise NotImplementedError('TODO: implement')

def looks_other_box(p):
    """An absolute path that belongs to a different machine or user than this one."""
    raise NotImplementedError('TODO: implement')

def discover_models(root, extra_roots=None):
    raise NotImplementedError('TODO: implement')

def resolve_model(name, roots):
    """-> (path or None, scope) with scope in local / other-box / missing."""
    raise NotImplementedError('TODO: implement')

def check_models(root, hash_files=True, extra_roots=None):
    raise NotImplementedError('TODO: implement')

def check_cli(root, timeout=...):
    raise NotImplementedError('TODO: implement')

def _module_names(node):
    """Dotted module names an Import / ImportFrom statement brings in."""
    raise NotImplementedError('TODO: implement')

def _toplevel_stmts(body):
    raise NotImplementedError('TODO: implement')

def _match(mod, family):
    raise NotImplementedError('TODO: implement')

def _docstring_ids(tree):
    raise NotImplementedError('TODO: implement')

def _is_loopback(host):
    raise NotImplementedError('TODO: implement')

def scan_source(src):
    """-> dict(cloud=[modules], net=[modules], remote_hosts=[hosts]) for one source text; raises SyntaxError."""
    raise NotImplementedError('TODO: implement')

def check_imports(root):
    raise NotImplementedError('TODO: implement')

def _parse_ts(ts):
    raise NotImplementedError('TODO: implement')

def _jsonl(path):
    raise NotImplementedError('TODO: implement')

def check_backups(root, now=None):
    raise NotImplementedError('TODO: implement')

def check_library(root):
    raise NotImplementedError('TODO: implement')

def runbook_cited_paths(text):
    raise NotImplementedError('TODO: implement')

def check_runbook(root, now=None):
    raise NotImplementedError('TODO: implement')

def now_iso():
    raise NotImplementedError('TODO: implement')

def manifest_path(root):
    raise NotImplementedError('TODO: implement')

def load_manifest(root):
    raise NotImplementedError('TODO: implement')

def save_manifest(root, m):
    raise NotImplementedError('TODO: implement')

def sha256_progress(path, say=..., label=None):
    """Streaming sha256, read-only; prints a line every 1 GiB."""
    raise NotImplementedError('TODO: implement')

def find_source(root, digest):
    """Download URL the repo recorded for this sha256, else None."""
    raise NotImplementedError('TODO: implement')

def recorded_hashes(root):
    raise NotImplementedError('TODO: implement')

def hash_weights(root, models_dir=None, say=...):
    """Hash each .gguf in models_dir into the manifest. Resumable by (size, mtime). Returns the manifest."""
    raise NotImplementedError('TODO: implement')

def under(path, parent):
    raise NotImplementedError('TODO: implement')

def verify_copy(root, src, dest, where=None, say=...):
    """-> (rc, message). 0 recorded, 1 not verified, 2 refused."""
    raise NotImplementedError('TODO: implement')

def record_copy(root, name, where, size, method):
    """Record a copy checked another way. Only a byte-size match is accepted; labelled as weaker evidence."""
    raise NotImplementedError('TODO: implement')

def check_limits():
    raise NotImplementedError('TODO: implement')

def write_atomic(path, doc):
    raise NotImplementedError('TODO: implement')

def run_all(root=..., host=..., hash_files=True, now=None, extra_roots=None):
    raise NotImplementedError('TODO: implement')

def render(doc):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
