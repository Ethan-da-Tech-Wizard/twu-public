# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Create an unverified, deterministic Python project-candidate bundle.

This generator DOES NOT execute candidate code, run the reference tests, verify
answers, train a model, or stage rows for training. Reference tests are emitted
separately from candidate rows so they are not accidentally included in prompts.
The directory must be new; nothing existing is replaced.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path

def canonical(value):
    raise NotImplementedError('TODO: implement')

def rows():
    """Return deterministic candidate and separate check records, without execution."""
    raise NotImplementedError('TODO: implement')

def build(out_dir):
    """Write a new candidate directory. No existing path may be replaced."""
    raise NotImplementedError('TODO: implement')

def cli_target(value, root=...):
    """Accept an existing real parent under the local autoimprove directory."""
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
