# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Validate the local observe → assess → action → verify chain.

This projection never collects data, starts a process, or changes a setting.
It records only host-scoped, hash-bound action candidates. Historical verified
labels remain claims: snapshot evaluates numeric comparisons and review bindings
separately. Comparable reviewed evidence does not authenticate execution or
authorize promotion. Execution remains subject to the candidate's authority.
"""
from __future__ import annotations
import argparse
from datetime import date
import hashlib
import json
import math
from pathlib import Path, PurePosixPath
import platform
import re
import sys

def host_name():
    raise NotImplementedError('TODO: implement')

def _text(value, name, maximum):
    raise NotImplementedError('TODO: implement')

def _path(value):
    raise NotImplementedError('TODO: implement')

def _reference(root, row, name):
    raise NotImplementedError('TODO: implement')

def _metric_reference(root, row, name):
    raise NotImplementedError('TODO: implement')

def validate(data, root=..., *, host=None):
    raise NotImplementedError('TODO: implement')

def path_for(root=..., host=None):
    raise NotImplementedError('TODO: implement')

def read(root=..., *, host=None):
    raise NotImplementedError('TODO: implement')

def evaluate_gain(row, root=...):
    """Check comparison evidence, never authenticate a reviewer or promote code.

    Metric receipts use measurement.metric.v1 with action_id, metric, value,
    unit, direction (lower/higher), subject/evaluator/cases/configuration references,
    enki_enabled and protections (references to PROTECTED_ENKI_PATHS).
    A measurement.review.v1 evidence receipt binds action_id, verifier,
    decision=accept and the exact before/after references. Every reference is
    {path, sha256}. Review names and hashes do not authenticate who ran a check.
    Legacy opaque receipts remain unknown, never upgraded in place.
    """
    raise NotImplementedError('TODO: implement')

def snapshot(root=..., *, host=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
