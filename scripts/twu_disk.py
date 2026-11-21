# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""twu_disk: read-only disk usage and duplicate report.

`usage [path]` runs gdu (MIT) if installed, else a stdlib os.scandir total.
`dupes [path]` runs fclones (MIT) if installed, else size + sha256 grouping.
Never deletes or modifies anything; symlinks are skipped; work is capped;
paths outside $HOME or the workspace are refused.
"""
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

def allowed_roots():
    raise NotImplementedError('TODO: implement')

def check_path(p):
    """Resolve p and return it only if inside $HOME or the workspace."""
    raise NotImplementedError('TODO: implement')

def walk_files(root, max_entries=...):
    """Yield (path, size) for regular files, skipping symlinks. Returns truncated flag via list."""
    raise NotImplementedError('TODO: implement')

def usage_fallback(root, max_entries=...):
    raise NotImplementedError('TODO: implement')

def sha256_file(path):
    raise NotImplementedError('TODO: implement')

def dupes_fallback(root, max_entries=..., max_hash_bytes=..., min_size=1):
    raise NotImplementedError('TODO: implement')

def run_gdu(root, binary):
    raise NotImplementedError('TODO: implement')

def run_fclones(root, binary):
    raise NotImplementedError('TODO: implement')

def usage(path, force_fallback=False):
    raise NotImplementedError('TODO: implement')

def dupes(path, force_fallback=False):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
