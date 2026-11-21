# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Read-only report of Syncthing *.sync-conflict-* files. Never modifies, moves or deletes anything.

Exit code 1 if any conflict exists, 0 if none, 2 on usage error.
"""
from __future__ import annotations
import argparse
import difflib
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

def sha256(path: Path) -> str | None:
    raise NotImplementedError('TODO: implement')

def find_conflicts(root: Path) -> list[Path]:
    raise NotImplementedError('TODO: implement')

def base_of(conflict: Path) -> Path:
    raise NotImplementedError('TODO: implement')

def load_claims(root: Path) -> dict:
    raise NotImplementedError('TODO: implement')

def claim_info(claims: dict, rel: str, now: float) -> dict | None:
    raise NotImplementedError('TODO: implement')

def git_tracked(root: Path, rel: str) -> bool | None:
    raise NotImplementedError('TODO: implement')

def read_lines(path: Path) -> list[str] | None:
    raise NotImplementedError('TODO: implement')

def describe(path: Path) -> dict:
    raise NotImplementedError('TODO: implement')

def analyze(root: Path, conflict: Path, claims: dict, now: float, diff_lines: int, check_git: bool=True) -> dict:
    raise NotImplementedError('TODO: implement')

def build_report(root: Path, diff_lines: int=0, check_git: bool=True) -> dict:
    raise NotImplementedError('TODO: implement')

def render(rep: dict) -> str:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
