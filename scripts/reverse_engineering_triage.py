# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Read-only, cross-platform first-pass triage for authorized files."""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path
import platform
import re
import shutil
import subprocess
from typing import Any
import zipfile

def sha256_file(path: Path) -> str:
    raise NotImplementedError('TODO: implement')

def command_output(argv: list[str]) -> str | None:
    raise NotImplementedError('TODO: implement')

def magic_kind(head: bytes, suffix: str) -> str:
    raise NotImplementedError('TODO: implement')

def printable_strings(sample: bytes, limit: int=40) -> list[str]:
    raise NotImplementedError('TODO: implement')

def python_summary(path: Path) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def zip_summary(path: Path) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def recommendations(kind: str, installed: dict[str, str]) -> list[str]:
    raise NotImplementedError('TODO: implement')

def triage(path: Path) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def main() -> int:
    raise NotImplementedError('TODO: implement')
