# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Safely dispatch completion-paced AFK work into one visible Codex terminal.

The sender fails closed unless Terminal is frontmost, the configured title and
TTY match, Codex is idle, its input line is empty, and the keyboard/mouse have
been quiet.  It never clears or overwrites input.  The next 420-second deadline
is measured only after the submitted Codex turn visibly returns to an idle,
empty prompt.
"""
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
import sys
import time
from typing import Any, Callable
import gemini_afk_scheduler as scheduler
import codex_thread_scheduler as project_scheduler

def run_osa(source: str, runner=...) -> str:
    raise NotImplementedError('TODO: implement')

def hid_idle_seconds(runner=...) -> float:
    raise NotImplementedError('TODO: implement')

def snapshot(*, window_id: int=..., osa=..., idle_probe=...) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def readiness(view: dict[str, Any], *, expected_title: str, expected_tty: str, min_idle_seconds: float) -> tuple[bool, str]:
    raise NotImplementedError('TODO: implement')

def view_fingerprint(view: dict[str, Any]) -> str:
    raise NotImplementedError('TODO: implement')

def staged_prompt_verified(contents: str, nonce: str) -> bool:
    """Prove the unique staged prompt reached Terminal before pressing Return."""
    raise NotImplementedError('TODO: implement')

def inject_prompt(prompt: str, *, expected_title: str, expected_tty: str, min_idle_seconds: float, required_nonce: str, window_id: int=..., snapshot_fn=..., runner=...) -> tuple[bool, str, dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def completed_after_dispatch(before_hash: str, *, expected_title: str, expected_tty: str, window_id: int=..., snapshot_fn=...) -> tuple[bool, str]:
    raise NotImplementedError('TODO: implement')

def append_event(path: Path, event: dict[str, Any]) -> None:
    raise NotImplementedError('TODO: implement')

def checklist_position(state: dict[str, Any], task_id: str) -> int:
    """Keep completed work complete when unrelated live evidence changes."""
    raise NotImplementedError('TODO: implement')

def main(argv: list[str] | None=None) -> int:
    raise NotImplementedError('TODO: implement')
