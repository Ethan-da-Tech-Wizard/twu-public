# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Offline dashboard catalog and link checks using bounded local metadata.

No content browsing, downloads, database queries, source writes, network or execution.
The dashboard control router owns file and database access. Catalog references are
navigation and observations, never permission to modify or execute their targets.
"""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat

def _relative(value, *, empty=False):
    raise NotImplementedError('TODO: implement')

def _open(root, relative, *, directory=False):
    """Walk pinned directory descriptors, refusing symlinks at every component."""
    raise NotImplementedError('TODO: implement')

def _read(root, relative, limit):
    raise NotImplementedError('TODO: implement')

def _json(root, relative, limit=...):
    raise NotImplementedError('TODO: implement')

def _reference(root, relative):
    raise NotImplementedError('TODO: implement')

def catalog(root=...):
    raise NotImplementedError('TODO: implement')

def check_links(root=...):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
