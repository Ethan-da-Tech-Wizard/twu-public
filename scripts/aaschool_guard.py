# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Change log for the shared AASchool tree. It never fails: sync is allowed to change anything.

`check` (default) compares the tree with the last baseline, rolls the baseline forward, and records every edit,
new file, removed file, emptied file and unsafe state (Syncthing conflict copy, symlink, runtime clutter, legacy
duplicate tree) in data/aaschool_guard/changes.jsonl, printing a one-line summary. It always exits 0.

  python3 scripts/aaschool_guard.py check      # default; log changes and roll the baseline forward
  python3 scripts/aaschool_guard.py snapshot   # force the baseline to the current tree
"""
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
import sys
import tempfile

def files():
    """Return ({relative path: sha256}, {relative path: size}, [unsafe-state errors])."""
    raise NotImplementedError('TODO: implement')

def write_manifest(rows, sizes):
    raise NotImplementedError('TODO: implement')

def snapshot():
    raise NotImplementedError('TODO: implement')

def check():
    """Never fails. Rolls the baseline forward and logs every change, delete, emptied file and unsafe state."""
    raise NotImplementedError('TODO: implement')
