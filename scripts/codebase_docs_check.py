# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
from __future__ import annotations
import argparse
import ast
import hashlib
import json
import re
import sys
from pathlib import Path

def _strip_docstrings(tree: ast.AST) -> ast.AST:
    raise NotImplementedError('TODO: implement')

def fingerprint(text: str) -> str:
    """Hash of the syntax tree WITHOUT docstrings. Equal before and after an edit means only comments and docstrings changed."""
    raise NotImplementedError('TODO: implement')

def block_lines(text: str) -> list:
    """The lines of the HOW THIS WORKS block (empty list if there is none)."""
    raise NotImplementedError('TODO: implement')

def block_problems(text: str) -> list:
    raise NotImplementedError('TODO: implement')

def load(path: Path) -> dict:
    raise NotImplementedError('TODO: implement')

def save(path: Path, data: dict) -> None:
    raise NotImplementedError('TODO: implement')

class locked:
    """Exclusive lock around a read-modify-write of the shared baseline. Eight helpers snapshotting at once used to overwrite each other's
    entries (read, add mine, write: the last writer wins), which showed up as 'NO SNAPSHOT'."""

    def __init__(self, path: Path):
        raise NotImplementedError('TODO: implement')

    def __enter__(self):
        raise NotImplementedError('TODO: implement')

    def __exit__(self, *exc):
        raise NotImplementedError('TODO: implement')

def pinned_modules(root: Path=...) -> dict:
    """{relative path: why} for scripts whose RAW BYTES something else fingerprints, so even a comment edit would break an integrity check.
    Found 2026-11-20 the hard way: HOW THIS WORKS blocks in ethan_typo_normalizer.py (the decoder's saved corrections are pinned to its hash) and in
    four example_host scripts (canonical_pins.json) made those checks fail. Sources checked: canonical_pins.json (canonical and mirror paths) and the file list
    in ethan_decoder_learning.engine_signature()."""
    raise NotImplementedError('TODO: implement')

def exempt_modules(root: Path=...) -> dict:
    raise NotImplementedError('TODO: implement')

def missing_blocks(root: Path=...) -> list:
    """Key modules that should carry a HOW THIS WORKS block and do not (exempt, hash-pinned modules are not expected to), plus pinned modules
    that carry one anyway (that breaks an integrity check)."""
    raise NotImplementedError('TODO: implement')

def pick(root: Path=..., n: int=...) -> list:
    """The most central modules: imported by the most other scripts (ties: larger first). Python only, no tests, no conflict or backup copies."""
    raise NotImplementedError('TODO: implement')

def cmd_check(root: Path=...) -> int:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
