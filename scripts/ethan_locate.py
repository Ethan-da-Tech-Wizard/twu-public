# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Read-only file locator for the Ethan CLI: typo-tolerant name search plus literal content search. Stdlib only, writes nothing.

  python3 scripts/ethan_locate.py "taxes fil"                 # top name matches (path, size, modified)
  python3 scripts/ethan_locate.py "kayaking" --content        # also files whose text contains the words, with the exact matching lines
  python3 scripts/ethan_locate.py "budget" --root Documents --k 5

Safety: roots must stay inside the workspace, /tmp or /mnt/GameDrive/twu_scratch (real paths; symlinks are not followed). Hidden entries,
private folders (profile, business, grants, apply, backups, .evidence, exports, ...), secret-looking names and binary/huge files are skipped
and never printed. Output is data: a path listed here exists; no match prints NOT FOUND, never a guess.
"""
from __future__ import annotations
import argparse
import difflib
import os
import re
import sys
import time
from pathlib import Path

def norm(s: str) -> list:
    raise NotImplementedError('TODO: implement')

def query_tokens(s: str) -> list:
    """Query words without filler (folder, file, rows, first ...); if nothing is left, keep them all."""
    raise NotImplementedError('TODO: implement')

def score(query: list, path: Path) -> float:
    """0..1: share of query tokens matched (exactly, by prefix/substring, or by close spelling) in the file name + parent folder names."""
    raise NotImplementedError('TODO: implement')

def allowed_root(p: Path) -> bool:
    raise NotImplementedError('TODO: implement')

def walk(root: Path):
    raise NotImplementedError('TODO: implement')

def content_hits(fp: Path, words: list, limit: int=3) -> list:
    raise NotImplementedError('TODO: implement')

def locate(query: str, root: Path, k: int=8, content: bool=False) -> dict:
    raise NotImplementedError('TODO: implement')

def fmt(res: dict) -> str:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
