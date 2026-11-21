# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
from __future__ import annotations
import argparse
import json
import os
import sys
import time
from pathlib import Path

def code_files(root: Path=...):
    raise NotImplementedError('TODO: implement')

def count_code_lines(data: bytes) -> int:
    """Physical lines, NOT counting a CLOSED '# >>> HOW THIS WORKS' ... '# <<< HOW THIS WORKS' explanation block: explaining a giant file must never
    make it count as having grown (scripts/codebase_docs_check.py proves such a block is comment-only). A block that is never closed is NOT
    exempt (otherwise one stray marker would hide the whole rest of a file from the ratchet)."""
    raise NotImplementedError('TODO: implement')

def sizes(root: Path=...) -> dict:
    raise NotImplementedError('TODO: implement')

def load(path: Path=...) -> dict:
    raise NotImplementedError('TODO: implement')

def save(data: dict, path: Path=...) -> None:
    raise NotImplementedError('TODO: implement')

def check(root: Path=..., baseline: Path=..., now_sizes: dict | None=None) -> list:
    """Returns a list of plain problems (empty = fine)."""
    raise NotImplementedError('TODO: implement')

def ratchet(root: Path=..., baseline: Path=..., now_sizes: dict | None=None) -> list:
    """Lower baseline numbers for files that shrank; drop entries that now fit the budget. Never raises a number. Returns what changed."""
    raise NotImplementedError('TODO: implement')

def init(root: Path=..., baseline: Path=...) -> dict:
    raise NotImplementedError('TODO: implement')

def allow(rel: str, number: int, why: str, baseline: Path=...) -> None:
    """The one deliberate way to raise a limit: it must be explicit, have a reason, and is written to the baseline's own log."""
    raise NotImplementedError('TODO: implement')

def report(root: Path=..., baseline: Path=..., top: int=15) -> str:
    raise NotImplementedError('TODO: implement')

def importer_counts(root: Path=...) -> dict:
    """module name -> how many OTHER python files import it (a regex scan of import lines; cheap and good enough to rank risk)."""
    raise NotImplementedError('TODO: implement')

def risk_rows(root: Path=..., baseline: Path=..., top: int=25) -> list:
    """The biggest code files with what makes each one risky to leave alone: no test file, no purpose header, imported by nothing."""
    raise NotImplementedError('TODO: implement')

def risk_md(root: Path=..., baseline: Path=..., top: int=25) -> str:
    raise NotImplementedError('TODO: implement')

def write_receipt(problems: list, root: Path=...) -> None:
    """data/health/SIZE_RATCHET.<host>.json: the last result, so a dashboard card can show it without re-scanning 2000 files."""
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
