# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Isolated, hash-bound file proposals for cooperating Magi on one host.

prepare snapshots one existing file into a unique local proposal directory.
Workers edit only its candidate file. review performs a three-way merge of the
snapshot, current shared file, and candidate, retaining conflicts for inspection.
The tool never writes the shared file; a clean result is a review candidate.

Syncthing has no cross-host atomic compare-and-swap, and direct editors need not
cooperate. A clean merge and hash match are not proof that a change is correct.
The recorded current hash describes a snapshot and may be stale immediately.
Re-read and re-review before integrating. No Git metadata is touched; no models run.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import stat
import subprocess
import sys
import tempfile
from pathlib import Path, PurePosixPath

class ProposalError(Exception):
    pass

def digest(data):
    raise NotImplementedError('TODO: implement')

def read_fd(fd):
    raise NotImplementedError('TODO: implement')

def read_regular(path):
    raise NotImplementedError('TODO: implement')

def read_target(root, relative):
    raise NotImplementedError('TODO: implement')

def write_new(path, data):
    raise NotImplementedError('TODO: implement')

def put_json(path, value):
    raise NotImplementedError('TODO: implement')

def load_json(path):
    raise NotImplementedError('TODO: implement')

def prepare(root, relative, store=...):
    raise NotImplementedError('TODO: implement')

def review(proposal):
    raise NotImplementedError('TODO: implement')

def verify_review(review_path):
    """Check a review's local snapshots; this is not a publication lock or approval."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
