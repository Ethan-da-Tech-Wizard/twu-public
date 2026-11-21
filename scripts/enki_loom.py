# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Enki Loom: source-reported outcomes and reflection gaps, never training or authority."""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime, timezone
import fcntl
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import socket
import tempfile

def host_name(value=None):
    raise NotImplementedError('TODO: implement')

def canonical(value):
    raise NotImplementedError('TODO: implement')

def digest(value):
    raise NotImplementedError('TODO: implement')

def safe_path(root, relative):
    raise NotImplementedError('TODO: implement')

def no_links(path):
    raise NotImplementedError('TODO: implement')

def json_bytes(raw):
    raise NotImplementedError('TODO: implement')

def read_json(path, limit=...):
    raise NotImplementedError('TODO: implement')

def timestamp(value):
    raise NotImplementedError('TODO: implement')

def candidate(value):
    raise NotImplementedError('TODO: implement')

def action(row):
    raise NotImplementedError('TODO: implement')

def make_item(kind, identity, source, record, state, host=..., reflection=False, evidence=...):
    raise NotImplementedError('TODO: implement')

def clean_item(row):
    raise NotImplementedError('TODO: implement')

def snapshot_read(path, host):
    raise NotImplementedError('TODO: implement')

class Scan:

    def __init__(self, root):
        raise NotImplementedError('TODO: implement')

    def issue(self, source, reason, line=None):
        raise NotImplementedError('TODO: implement')

    def add(self, row):
        raise NotImplementedError('TODO: implement')

    def lines(self, relative):
        raise NotImplementedError('TODO: implement')

    def evidence(self, refs):
        raise NotImplementedError('TODO: implement')

def _same_connection(work, outcome):
    """A seat number cannot transfer work to its next occupant; legacy records remain attributed."""
    raise NotImplementedError('TODO: implement')

def _collect(scan, host, state_dir):
    raise NotImplementedError('TODO: implement')

def _sync(root, host, state_dir, destination, recovering=False):
    raise NotImplementedError('TODO: implement')

def sync(root=..., host=None, state_dir=None, *, recover=False):
    raise NotImplementedError('TODO: implement')

def status(root=..., host=None):
    raise NotImplementedError('TODO: implement')

def actions(root=..., host=None, *, limit=20, offset=0, action_label=None, kind=None, since=None, record_id=None):
    """Bounded read-only slices of saved work and diagnostics; listing never acknowledges work."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
