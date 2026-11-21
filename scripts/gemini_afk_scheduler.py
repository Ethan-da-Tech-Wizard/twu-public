# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Narrow, headless Gemini work scheduler for one explicitly assigned task.

This deliberately does not import any terminal injector or fleet supervisor.  It
starts at most one direct Gemini child, waits for it, and measures the next
420-second deadline from that child's completion.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import signal
import subprocess
import sys
import time
from typing import Any

def utc_now() -> str:
    raise NotImplementedError('TODO: implement')

def local_state_dir(host_kind: str=...) -> Path:
    raise NotImplementedError('TODO: implement')

def read_json(path: Path) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def atomic_json(path: Path, value: dict[str, Any]) -> None:
    raise NotImplementedError('TODO: implement')

def authorization(seat: int, host_kind: str=...) -> tuple[bool, str]:
    raise NotImplementedError('TODO: implement')

def task_path(seat: int) -> Path:
    raise NotImplementedError('TODO: implement')

def load_task(seat: int) -> dict[str, Any] | None:
    raise NotImplementedError('TODO: implement')

def prompt_hash(task: dict[str, Any]) -> str:
    raise NotImplementedError('TODO: implement')

def get_newest_packet(seat: int, comms_dir: Path=...) -> dict[str, Any] | None:
    raise NotImplementedError('TODO: implement')

def extract_evidence(task: dict[str, Any], packet: dict[str, Any] | None) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def compute_evidence_sha256(evidence: dict[str, Any]) -> str:
    raise NotImplementedError('TODO: implement')

def compute_tea_hash(task_id: str, evidence_sha256: str, action: str) -> str:
    raise NotImplementedError('TODO: implement')

def resolve_checklist(task: dict[str, Any]) -> list[str]:
    raise NotImplementedError('TODO: implement')

def build_envelope(*, task_id: str, sequence: int, action: str, evidence_sha256: str, packet: dict[str, Any] | None, now_fn=...) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def attach_envelope_to_prompt(base_prompt: str, envelope: dict[str, Any]) -> str:
    raise NotImplementedError('TODO: implement')

def make_idle_receipt(task: dict[str, Any], envelope: dict[str, Any], cli_kind: str, *, receipt_path: Path, reason: str=...) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def publish_visible_prompt(seat: int, envelope: dict[str, Any], runner=...) -> None:
    """Publish the steering envelope to the shared room before model work."""
    raise NotImplementedError('TODO: implement')

def admission_ok(max_load: float, min_available_mb: int) -> tuple[bool, str]:
    raise NotImplementedError('TODO: implement')

def build_argv(cli_path: str, cli_kind: str, task: dict[str, Any], timeout: float) -> list[str]:
    raise NotImplementedError('TODO: implement')

def append_receipt(path: Path, receipt: dict[str, Any]) -> None:
    raise NotImplementedError('TODO: implement')

def run_task(task: dict[str, Any], *, cli_path: str, cli_kind: str, timeout: float, receipt_path: Path, envelope: dict[str, Any] | None=None, popen=..., monotonic=...) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def evaluate_and_dispatch(task: dict[str, Any], *, seat: int, cli_path: str, cli_kind: str, timeout: float, interval: int, state: dict[str, Any], state_path: Path, receipt_path: Path, comms_dir: Path=..., popen=..., monotonic=..., publish_runner=...) -> tuple[dict[str, Any], int]:
    raise NotImplementedError('TODO: implement')

def due(state: dict[str, Any], now: float, interval: int) -> bool:
    raise NotImplementedError('TODO: implement')

def mark_stopped(state: dict[str, Any], pid: int, stopped_at: str) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def main(argv: list[str] | None=None) -> int:
    raise NotImplementedError('TODO: implement')
