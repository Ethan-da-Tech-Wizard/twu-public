# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Read-only sync doctor (Magi 8): finds the ways files and Magi messages silently fail to cross boxes.
Checks: live beacon age per box, stale beacon files, sync-conflict files outside archive/, files the .stignore would
silently drop for a cross-box path list. No root, no network, changes nothing. `python3 scripts/sync_doctor.py [--json]`."""
import fnmatch, json, sys, time
from pathlib import Path

def ignore_patterns(root=...):
    raise NotImplementedError('TODO: implement')

def ignored(rel, pats):
    """First matching pattern wins; '!' negates. Syncthing semantics, simplified (glob on path or any segment)."""
    raise NotImplementedError('TODO: implement')

def report(root=..., now=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
