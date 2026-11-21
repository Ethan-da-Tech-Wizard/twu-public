# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Retired handoff relay; only the pure quota comparison remains supported.

Legacy entry points refuse without saving state, staging files or starting work.
Current instructions and routing live in AGENTS.md, not generated handoff notes.
"""
from __future__ import annotations
from pathlib import Path
import sys

def check_quota(used_percent: float, threshold_percent: float=90.0) -> bool:
    """Return True if token/quota usage reaches threshold (e.g. 10% remaining)."""
    raise NotImplementedError('TODO: implement')

def create_handoff(task_name: str, completed: list[str], active_state: str, blockers: list[str], next_action: str, model_id: str=...) -> Path:
    """Refuse the retired writer; supplied task state is not saved."""
    raise NotImplementedError('TODO: implement')

def sync_notebooklm() -> bool:
    """Refuse the retired staging entry point without starting a process."""
    raise NotImplementedError('TODO: implement')

def build_next_prompt(handoff_path: Path, next_target: str=...) -> str:
    """Refuse to turn historical handoff contents into current instructions."""
    raise NotImplementedError('TODO: implement')

def main() -> int:
    """Fail every legacy CLI invocation, including implicit quota triggers."""
    raise NotImplementedError('TODO: implement')
