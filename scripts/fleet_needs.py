# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Validate portable, privacy-bounded fleet-needs receipts.

This is a schema/coverage gate, not a collector or updater. It makes a host say
what it measured, what remains unknown, and how fresh that statement is before
any dashboard or planner treats coverage as healthy.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
import math
from pathlib import Path

def parse_time(value):
    raise NotImplementedError('TODO: implement')

def validate(receipt, *, now=None):
    """Return a list of precise errors. Empty means safe to consume as evidence."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
