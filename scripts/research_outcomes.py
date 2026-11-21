# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Validate the explicit bridge from research to an operational outcome.

This is a projection, not a research collector and not an execution queue.
It never infers an outcome from prose.  A manager registers only research that
is intended to drive work, then records exactly one disposition: implemented,
measured_rejected, decision, or open.  Approved implementation remains in the
existing machine-local immutable job queue.
"""
from __future__ import annotations
import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys
from example_host import local_reference
from example_host_activity import artifact_reference

def _require(condition, message):
    raise NotImplementedError('TODO: implement')

def _text(value, name, maximum):
    raise NotImplementedError('TODO: implement')

def _reference(root, value, name):
    raise NotImplementedError('TODO: implement')

def validate(data, root=...):
    raise NotImplementedError('TODO: implement')

def read(root=...):
    raise NotImplementedError('TODO: implement')

def snapshot(root=...):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
