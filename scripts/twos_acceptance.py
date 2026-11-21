# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Validate the five separately evidenced TWOS release journeys."""
from __future__ import annotations
import argparse
from datetime import date
import hashlib
import json
from pathlib import Path, PurePosixPath
import platform
import re
import sys

def _text(value, name, maximum=240):
    raise NotImplementedError('TODO: implement')

def _reference(root, value):
    raise NotImplementedError('TODO: implement')

def validate(data, root=..., *, host=None):
    raise NotImplementedError('TODO: implement')

def snapshot(path=..., *, root=..., host=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
