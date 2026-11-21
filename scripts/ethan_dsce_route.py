# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Decide whether DSCE can safely improve a real project revision."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import tempfile
from typing import Any

def sha256_bytes(value: bytes) -> str:
    raise NotImplementedError('TODO: implement')

def canonical(value: Any) -> bytes:
    raise NotImplementedError('TODO: implement')

def source_manifest(project: Path) -> list[dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def tree_sha256(files: list[dict[str, Any]]) -> str:
    raise NotImplementedError('TODO: implement')

def assess(project: Path, request: Path) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def atomic_json(path: Path, value: dict[str, Any]) -> None:
    raise NotImplementedError('TODO: implement')

def main() -> int:
    raise NotImplementedError('TODO: implement')
