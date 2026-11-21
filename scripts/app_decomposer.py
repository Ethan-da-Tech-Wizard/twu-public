# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/app_decomposer.py — turn a high-level app goal into small verified steps.

Why this exists (2026-10-25): the offline app-builder had every layer except the
decomposition one. The local gpt-oss-20b reliably executes a single bounded
"write exactly this one file" prompt (proven via resilient_task_runner), but it
cannot hold a whole app in its head. Until now a frontier Magi decomposed each
goal into those bounded steps by hand. This tool automates that role: the LOCAL
model proposes the plan, and this code — never the model — enforces every safety
rule (path containment inside the project dir, a verify-type whitelist, a step
cap, unique ids, fail-closed strict-JSON parsing). Each step is then executed by
resilient_task_runner with a self-contained prompt that inlines previously
written files, and only counts as done when its file exists AND its verify
command exits 0.

Subcommands:
  plan  --goal TEXT --project-dir REL_PATH [--out DIR] [--max-steps N]
  run   --plan FILE [--max-attempts-per-step N]

Exit codes: 0 success, 1 failure (FAIL receipt written), 2 STOP latch raised.

Stdlib only. Externals (model_call, runner_invoke) are module-level injectable
functions so tests run with no model, no runner, and no network.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import shlex
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

def _now_iso() -> str:
    raise NotImplementedError('TODO: implement')

def stop_path() -> Path:
    raise NotImplementedError('TODO: implement')

def model_call(messages: List[Dict[str, str]]) -> str:
    """POST to the local model's OpenAI-style chat endpoint; return the reply text."""
    raise NotImplementedError('TODO: implement')

def runner_invoke(prompt_path: Path, expect_path: Path, verify_cmd: Optional[str], max_attempts: int) -> Dict[str, Any]:
    """Run one step through resilient_task_runner as a subprocess.

    Returns {"rc": int, "receipt_path": str|None, "stdout_tail": str}. The
    runner itself enforces that the expect file exists and the verify command
    exits 0 before it reports success (rc 0)."""
    raise NotImplementedError('TODO: implement')

def _resolve_project_dir(project_dir: str) -> Tuple[Optional[Path], Optional[str]]:
    raise NotImplementedError('TODO: implement')

def _resolve_step_path(project_root: Path, rel: Any) -> Tuple[Optional[Path], Optional[str]]:
    raise NotImplementedError('TODO: implement')

def build_planning_messages(goal: str, project_dir: str, max_steps: int) -> List[Dict[str, str]]:
    raise NotImplementedError('TODO: implement')

def _strip_fences(text: str) -> str:
    raise NotImplementedError('TODO: implement')

def parse_plan_reply(raw: str, project_root: Path, max_steps: int) -> Tuple[Optional[List[Dict[str, Any]]], List[str]]:
    """Fail-closed strict parse + validation. Returns (steps, errors)."""
    raise NotImplementedError('TODO: implement')

def _atomic_write_json(path: Path, obj: Dict[str, Any]) -> Path:
    raise NotImplementedError('TODO: implement')

def _sha256(path: Path) -> Optional[str]:
    raise NotImplementedError('TODO: implement')

def _journal(success: bool, summary: str, receipt_path: Path) -> None:
    """Best-effort rolling-journal entry; a journal failure never fails a run."""
    raise NotImplementedError('TODO: implement')

def cmd_plan(args: argparse.Namespace) -> int:
    raise NotImplementedError('TODO: implement')

def _verify_cmd_for(vtype: str, abs_path: Path) -> Optional[str]:
    raise NotImplementedError('TODO: implement')

def build_step_prompt(target: Path, spec: str, written: Sequence[Tuple[Path, str]]) -> str:
    raise NotImplementedError('TODO: implement')

def _attempts_from_receipt(receipt_path: Optional[str]) -> Optional[int]:
    raise NotImplementedError('TODO: implement')

def cmd_run(args: argparse.Namespace) -> int:
    raise NotImplementedError('TODO: implement')

def parse_args(argv: Optional[Sequence[str]]=None) -> argparse.Namespace:
    raise NotImplementedError('TODO: implement')

def main(argv: Optional[Sequence[str]]=None) -> int:
    raise NotImplementedError('TODO: implement')
