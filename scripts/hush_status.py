# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Read-only status and source-tracking view for Ethan's Hush pseudocode project."""
import argparse
import json
import os
from pathlib import Path
import stat
import sys

class SourceError(ValueError):
    """A stable error code, never source content or an OS error containing paths."""

def read_source(root, name):
    """Read one bounded regular UTF-8 file through no-follow directory descriptors."""
    raise NotImplementedError('TODO: implement')

def git_state(repo_root, hush_root):
    """Report only whether the Hush source directory is inside this TWU checkout."""
    raise NotImplementedError('TODO: implement')

def build_status(hush_root, repo_root=...):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
