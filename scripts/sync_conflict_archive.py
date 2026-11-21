# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Safe handling of Syncthing *.sync-conflict-* files. NEVER deletes.

scan  : read-only classification (identical / differing / held).
apply : MOVE (never delete) conflict copies that are byte-identical (sha256 + cmp)
        to their current base into archive/<date>/syncthing-conflicts-identical/,
        preserving the relative path, with manifest.jsonl; re-verifies afterwards.
        Differing conflicts are never touched; held ones are only listed.
Held: data/comms/**, anything claimed in data/comms/claims.json (read-only),
      scripts/** whose base changed in the last 30 minutes, missing base.
"""
from __future__ import annotations
import argparse
import filecmp
import hashlib
import json
import os
import re
import shutil
import sys
import time
from pathlib import Path

def sha256(p: Path) -> str:
    raise NotImplementedError('TODO: implement')

def base_of(c: Path) -> Path:
    raise NotImplementedError('TODO: implement')

def find_conflicts(root: Path) -> list[Path]:
    """Locate all Syncthing conflict files across repo excluding build/cache artifacts."""
    raise NotImplementedError('TODO: implement')

def load_claims(root: Path) -> dict:
    raise NotImplementedError('TODO: implement')

def classify(root: Path, c: Path, claims: dict, now: float) -> dict:
    raise NotImplementedError('TODO: implement')

def scan(root: Path, now: float | None=None) -> list[dict]:
    raise NotImplementedError('TODO: implement')

def apply(root: Path, date: str, now: float | None=None) -> dict:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
