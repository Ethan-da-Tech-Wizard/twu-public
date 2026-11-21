# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Completion-paced AFK prompts for one already-open Linux Codex window."""
from __future__ import annotations
import argparse
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import time
from typing import Any

def stall_note() -> str:
    """Extra prompt text when the last turns kept repeating the same fix with live evidence still NOT_RUN (see afk_trajectory.py)."""
    raise NotImplementedError('TODO: implement')

def client(address: str) -> dict[str, Any] | None:
    raise NotImplementedError('TODO: implement')

def descendant_of(pid: int, ancestor: int) -> bool:
    raise NotImplementedError('TODO: implement')

def empty_placeholder_visible(ocr: str) -> bool:
    """Accept the measured Tesseract A/[/I ambiguity, but only on a prompt line."""
    raise NotImplementedError('TODO: implement')

def active_marker_visible(view: dict[str, Any], ocr: str) -> bool:
    raise NotImplementedError('TODO: implement')

def window_ocr(view: dict[str, Any]) -> str:
    raise NotImplementedError('TODO: implement')

def readiness(view: dict[str, Any] | None, ocr: str, *, kitty_pid: int, codex_pid: int) -> tuple[bool, str]:
    raise NotImplementedError('TODO: implement')

def snapshot(address: str, kitty_pid: int, codex_pid: int) -> tuple[dict[str, Any], str, str]:
    raise NotImplementedError('TODO: implement')

def send_visible(prompt: str, address: str) -> tuple[bool, str]:
    raise NotImplementedError('TODO: implement')

def append(path: Path, event: dict[str, Any]) -> None:
    raise NotImplementedError('TODO: implement')

def next_sequence() -> int:
    raise NotImplementedError('TODO: implement')

def mark_unproven_timeout(state: dict[str, Any], *, sequence: int, nonce: str, interval: int, monotonic_now: float, wall_now: float, completed_at: str) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def main(argv: list[str] | None=None) -> int:
    raise NotImplementedError('TODO: implement')
