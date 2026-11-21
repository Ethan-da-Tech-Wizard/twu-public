# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""twu_linkmap.py - offline link map of the TWU_LLC workspace.

Finds every reference between files (markdown links, backticked paths, code
path literals, JSON path strings, unit names, MOVING_PARTS rows, wiring
manifest entries, test pairs, data file names) so a rename can be done safely.

Commands:
  build                 write data/dashboard/linkmap.json and docs/SYSTEM_LINKS.md
                        (incremental via data/dashboard/linkmap_cache.json)
  check                 list broken references; exit 0 none, 1 broken found,
                        2 tool error. archive/ targets on another host are
                        reported separately as UNAVAILABLE_HERE, not broken
  labels                list dead paths in data/workspace_labels.json
                        (path, label key); read-only
  who-uses PATH         every file:line that references PATH
  rename OLD NEW        dry-run list of edits; --apply archives then rewrites
                        references only (it never moves the file itself)

Standard library only. No network, no model calls, no daemons.
"""
import argparse
import json
import os
import re
import shutil
import sys
import tempfile
import datetime
from collections import Counter, defaultdict
from pathlib import Path

def rel_posix(root, p):
    raise NotImplementedError('TODO: implement')

def is_generated_path(rel):
    raise NotImplementedError('TODO: implement')

def protected_reason(rel, text_head=...):
    """Why a file must never be rewritten, or '' if it may be."""
    raise NotImplementedError('TODO: implement')

def list_files(root):
    """Scannable text files plus the basename index. Never follows symlinks."""
    raise NotImplementedError('TODO: implement')

def read_text(path):
    raise NotImplementedError('TODO: implement')

class Resolver:

    def __init__(self, root, files):
        raise NotImplementedError('TODO: implement')

    def exists(self, rel):
        raise NotImplementedError('TODO: implement')

    def isdir(self, rel):
        raise NotImplementedError('TODO: implement')

    @staticmethod
    def norm(rel):
        raise NotImplementedError('TODO: implement')

    def resolve(self, token, src, kind_hint):
        """-> (target, how, state). state: ok | broken | unresolved."""
        raise NotImplementedError('TODO: implement')

def classify(line, start, end, src_ext):
    raise NotImplementedError('TODO: implement')

def final_kind(src, ctx, target, literal, line):
    raise NotImplementedError('TODO: implement')

def extract_file(rel, text):
    """Resolution-independent extraction for one file -> (gen, items).

    items are ["r", line, col, token, ctx, pipe_line] or ["s", line, col, stem]
    in scan order. Nothing here looks at other files, so it is safe to cache
    keyed on this file's (size, mtime_ns) alone."""
    raise NotImplementedError('TODO: implement')

def resolve_items(rel, gen, items, rs):
    """Resolve extracted items against the current tree (never cached)."""
    raise NotImplementedError('TODO: implement')

def scan_file(rel, text, rs):
    """Yield reference dicts found in one file."""
    raise NotImplementedError('TODO: implement')

def test_pairs(files, rs):
    raise NotImplementedError('TODO: implement')

def cache_version():
    raise NotImplementedError('TODO: implement')

def load_cache(root):
    """Previous cache entries, or {} if absent, corrupt, symlinked or stale."""
    raise NotImplementedError('TODO: implement')

def save_cache(root, entries):
    raise NotImplementedError('TODO: implement')

def scan(root, use_cache=False, write_cache=False):
    """Scan the tree. use_cache reads linkmap_cache.json; write_cache saves it.

    A file is re-extracted when it has no entry or its (size, mtime_ns)
    differ; files no longer present are dropped from the saved cache."""
    raise NotImplementedError('TODO: implement')

def is_noise_source(r):
    """Sources whose dangling paths are expected (history, fixtures, tests)."""
    raise NotImplementedError('TODO: implement')

def broken_refs(refs):
    raise NotImplementedError('TODO: implement')

def short_host(h):
    raise NotImplementedError('TODO: implement')

def load_labels(root):
    """Parsed workspace_labels.json, or None if absent. Never follows symlinks."""
    raise NotImplementedError('TODO: implement')

def archive_host_of(labels):
    """instructions.archive_host as scripts/magi.py instruction_state reads it."""
    raise NotImplementedError('TODO: implement')

def is_storage_host(host, archive_host):
    """Same rule as magi.py: no recorded host means history is expected here."""
    raise NotImplementedError('TODO: implement')

def local_host_name():
    raise NotImplementedError('TODO: implement')

def under_archive(target):
    raise NotImplementedError('TODO: implement')

def split_broken(refs, archive_host, host):
    """-> (broken, unavailable_here). archive/ targets are unavailable_here
    only when this host is not the recorded storage host."""
    raise NotImplementedError('TODO: implement')

def dead_labels(root, archive_host, host):
    """-> (dead [(path, label_key)], unavailable_here count). Read-only."""
    raise NotImplementedError('TODO: implement')

def atomic_write(path, data, mode=None):
    raise NotImplementedError('TODO: implement')

def summarize(result):
    raise NotImplementedError('TODO: implement')

def build(root, host=None):
    raise NotImplementedError('TODO: implement')

def norm_arg(root, p):
    raise NotImplementedError('TODO: implement')

def matches(target, path):
    raise NotImplementedError('TODO: implement')

def find_uses(result, path):
    raise NotImplementedError('TODO: implement')

def new_literal(ref, old, new):
    raise NotImplementedError('TODO: implement')

def plan_rename(root, old, new):
    raise NotImplementedError('TODO: implement')

def archive_target(root, rel, stamp):
    raise NotImplementedError('TODO: implement')

def apply_rename(root, plan, today=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None, root=None, out=None, host=None):
    raise NotImplementedError('TODO: implement')

def run_command(a, root, pr, host):
    raise NotImplementedError('TODO: implement')
