# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Validate hash-only, host-scoped TWOS desktop fidelity sources.

The manifest records no configuration contents. It detects whether the real
Hypr/Plasma sources used to define a TWOS flavor changed after review, and
whether the required visual reference has actually been supplied.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import platform
import re
import sys

def hostname():
    raise NotImplementedError('TODO: implement')

def text(value, name, maximum=200):
    raise NotImplementedError('TODO: implement')

def home_path(value):
    raise NotImplementedError('TODO: implement')

def validate(data, *, host=None):
    raise NotImplementedError('TODO: implement')

def read(path=..., *, host=None):
    raise NotImplementedError('TODO: implement')

def digest(path):
    raise NotImplementedError('TODO: implement')

def check(path=..., *, home=None, host=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
