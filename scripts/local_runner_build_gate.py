# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""One-shot, metadata-only preflight for the local llama-server build.

This is intentionally a gate, not a build daemon.  It refuses profiles that
could fetch a UI asset, checks fresh local capacity, and records a compact
receipt.  A caller must explicitly start the reviewed command after a PASS.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import socket
import sys
from typing import Any, Callable
import ethan_thermal_guard as thermal

def now_utc() -> str:
    raise NotImplementedError('TODO: implement')

def profile_hash(profile: dict[str, str]) -> str:
    raise NotImplementedError('TODO: implement')

def safe_dir(path: Path, *, may_not_exist: bool=False) -> bool:
    raise NotImplementedError('TODO: implement')

def validate_profile(profile: dict[str, str]) -> str | None:
    raise NotImplementedError('TODO: implement')

def fresh_measurements(reader: Callable[[], tuple[Any, Any, Any]] | None=None) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def preflight(source: Path, build: Path, profile: dict[str, str]=..., reader: Callable[[], tuple[Any, Any, Any]] | None=None) -> tuple[str, dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def planned_command(source: Path, build: Path, profile: dict[str, str]=...) -> list[str]:
    """The only command this gate will ever describe; it never executes it."""
    raise NotImplementedError('TODO: implement')

def make_receipt(host: str, state: str, reason: str, measurements: dict[str, Any], profile: dict[str, str]=...) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def write_receipt(receipt: dict[str, Any], directory: Path=...) -> Path:
    raise NotImplementedError('TODO: implement')

def receipt_state(path: Path) -> str:
    raise NotImplementedError('TODO: implement')

def main(argv: list[str] | None=None) -> int:
    raise NotImplementedError('TODO: implement')
