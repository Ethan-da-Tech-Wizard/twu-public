# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Enki's explicit, hash-bound release path for quarantined downloads.

Nothing in this tool executes a held file. Release requires a named owner and
re-hashes the exact quarantined object immediately before moving it.
"""
from __future__ import annotations
import argparse
import datetime as dt
import hashlib
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, Tuple

def digest(path: Path) -> str:
    raise NotImplementedError('TODO: implement')

def regular_child(path: Path, root: Path) -> Path:
    """Return one regular, non-symlinked file directly below *root*."""
    raise NotImplementedError('TODO: implement')

def load(sha: str) -> Tuple[Dict[str, Any], Path, Path]:
    raise NotImplementedError('TODO: implement')

def release(sha: str, owner: str) -> Path:
    raise NotImplementedError('TODO: implement')

def resolve_held_target(target: str) -> str:
    """Resolve a target which may be 'latest', a filename, or a sha256 to a held sha256."""
    raise NotImplementedError('TODO: implement')

def main() -> None:
    raise NotImplementedError('TODO: implement')
