# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
from __future__ import annotations
import argparse
import glob
import json
import os
import platform
import shutil
import subprocess
import sys
import time
from pathlib import Path

def item(id_: str, status: str, detail: str, fix: str=...) -> dict:
    raise NotImplementedError('TODO: implement')

def walk_code(root: Path):
    raise NotImplementedError('TODO: implement')

def check_writable(root: Path, uid: int | None=None) -> dict:
    raise NotImplementedError('TODO: implement')

def check_immutable(root: Path) -> dict:
    raise NotImplementedError('TODO: implement')

def check_stop(root: Path) -> dict:
    raise NotImplementedError('TODO: implement')

def check_git(root: Path, now: float | None=None) -> list:
    raise NotImplementedError('TODO: implement')

def heal_stale_git_lock(root: Path, now: float | None=None, git_running=None, held=None) -> str:
    """The ONE automatic repair, only with --heal: remove an abandoned .git/index.lock. All of these must hold: the file is EMPTY, it is older
    than LOCK_AGE_S, no git process is running, and nothing has the file open. Anything else is left alone. Returns a one-line description."""
    raise NotImplementedError('TODO: implement')

def check_disk(root: Path, usage=None) -> dict:
    raise NotImplementedError('TODO: implement')

def check_conflicts(root: Path, now: float | None=None) -> dict:
    raise NotImplementedError('TODO: implement')

def check_claims(root: Path, now: float | None=None) -> dict:
    raise NotImplementedError('TODO: implement')

def check_key_file(home: Path | None=None) -> dict:
    raise NotImplementedError('TODO: implement')

def check_system_locks() -> dict:
    raise NotImplementedError('TODO: implement')

def run(root: Path=...) -> dict:
    raise NotImplementedError('TODO: implement')

def write_receipt(rec: dict, health: Path=...) -> None:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
