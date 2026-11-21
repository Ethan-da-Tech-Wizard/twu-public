# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Reviewed decoder feedback with replay checks; no prompts, model calls or training.

Candidates cannot enter the active lexicon. An explicit accept/reject decision
provides ranking feedback; accepted pairs still need passing replay checks before
becoming reusable exact corrections. Context-specific feedback stays suggest-only.
"""
from __future__ import annotations
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
import tempfile

def _sha(value):
    raise NotImplementedError('TODO: implement')

def _stamp():
    raise NotImplementedError('TODO: implement')

def engine_signature():
    raise NotImplementedError('TODO: implement')

def _path(path=None):
    raise NotImplementedError('TODO: implement')

def _validate(row):
    raise NotImplementedError('TODO: implement')

def _read(path):
    raise NotImplementedError('TODO: implement')

@contextmanager
def _edit(path=None):
    raise NotImplementedError('TODO: implement')

def record_feedback(observed, proposed, *, source_sha256, decision=..., reviewer=..., reason=..., left=..., right=..., path=None):
    """Record only an explicitly supplied token pair and optional adjacent words."""
    raise NotImplementedError('TODO: implement')

def load_feedback(path=None):
    raise NotImplementedError('TODO: implement')

def load_pairs(path=None):
    raise NotImplementedError('TODO: implement')

def evaluate(ident, *, path=None):
    """Replay actual decoder behavior; activation requires prior explicit review."""
    raise NotImplementedError('TODO: implement')

def status(path=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
