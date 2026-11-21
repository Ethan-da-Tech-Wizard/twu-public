# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Run one bounded Ethan codebase worker and write an honest invocation receipt."""
from __future__ import annotations
import argparse
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from typing import Any
import uuid

class WorkerError(ValueError):
    pass

def now() -> str:
    raise NotImplementedError('TODO: implement')

def default_availability_path() -> Path:
    raise NotImplementedError('TODO: implement')

def default_pending_path() -> Path:
    raise NotImplementedError('TODO: implement')

def pending_lock_path(path: Path) -> Path:
    raise NotImplementedError('TODO: implement')

@contextmanager
def pending_state_claim(path: Path):
    """Keep one process responsible for pending selection through final commit."""
    raise NotImplementedError('TODO: implement')

def _write_private_json(path: Path, value: dict[str, Any]) -> None:
    raise NotImplementedError('TODO: implement')

def read_pending(path: Path) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def quota_reset_seconds(text: str) -> int:
    raise NotImplementedError('TODO: implement')

def read_availability(path: Path, at: datetime | None=None) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def write_unavailable(path: Path, provider: str, reason: str, retry_seconds: int | None, *, observed_at: datetime | None=None, source_receipt: dict[str, str] | None=None) -> None:
    raise NotImplementedError('TODO: implement')

def clear_unavailable(path: Path, provider: str) -> None:
    raise NotImplementedError('TODO: implement')

def sha256_file(path: Path) -> str:
    raise NotImplementedError('TODO: implement')

def resolve_workspace_path(value: Path, *, must_be_file: bool=False, must_be_dir: bool=False) -> Path:
    raise NotImplementedError('TODO: implement')

def snapshot_project(project: Path) -> dict[str, str]:
    raise NotImplementedError('TODO: implement')

def project_symlinks(project: Path) -> set[str]:
    raise NotImplementedError('TODO: implement')

def project_directories(project: Path) -> set[str]:
    raise NotImplementedError('TODO: implement')

def backup_project(project: Path, before: dict[str, str], backup: Path) -> None:
    raise NotImplementedError('TODO: implement')

def restore_failed_attempt(project: Path, backup: Path, before: dict[str, str], changed: dict[str, Any], new_symlinks: set[str], new_directories: set[str]) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def begin_source_transaction(project: Path) -> dict[str, Any]:
    """Hold an exact source snapshot across provider execution and qualification."""
    raise NotImplementedError('TODO: implement')

def rollback_source_transaction(project: Path, transaction: dict[str, Any]) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def qualify_transactionally(project: Path, result: dict[str, Any], receipt: Path, base_manifest: Path | None, transaction: dict[str, Any] | None, *, bootstrap_new_project: bool=False) -> dict[str, Any]:
    """Commit provider source only when its complete-codebase qualification passes."""
    raise NotImplementedError('TODO: implement')

def classify(exit_code: int, stderr: str, response: str, changed: dict[str, Any], provider: str=...) -> tuple[str, str]:
    raise NotImplementedError('TODO: implement')

def file_link(path: Path) -> dict[str, str]:
    raise NotImplementedError('TODO: implement')

def has_project_changes(receipt: dict[str, Any]) -> bool:
    raise NotImplementedError('TODO: implement')

def load_acceptance_contract(path: Path) -> list[dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def validate_bootstrap_acceptance(checks: list[dict[str, Any]]) -> None:
    """Fail closed on generated checks that install, network, shell, or escape the project."""
    raise NotImplementedError('TODO: implement')

def run_acceptance_checks(project: Path, checks: list[dict[str, Any]], evidence: Path, env: dict[str, str]) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def run_worker(project: Path, request_file: Path, *, gemini_bin: Path | None=None, timeout: int=300, provider: str=..., acceptance_file: Path | None=None, availability_file: Path | None=None, bootstrap_new_project: bool=False) -> tuple[dict[str, Any], Path]:
    raise NotImplementedError('TODO: implement')

def run_provider_route(project: Path, request_file: Path, *, timeout: int=300, gemini_bin: Path | None=None, antigravity_bin: Path | None=None, acceptance_file: Path | None=None, availability_file: Path | None=None, bootstrap_new_project: bool=False) -> tuple[dict[str, Any], Path]:
    """Attempt Gemini first and continue only after a clean, zero-edit NOT_RUN."""
    raise NotImplementedError('TODO: implement')

def _linked_path(link: dict[str, str]) -> Path:
    raise NotImplementedError('TODO: implement')

def _queue_pending_claimed(path: Path, result: dict[str, Any], receipt_path: Path, *, provider: str, timeout: int, base_manifest: Path | None=None, bootstrap_new_project: bool=False) -> dict[str, Any]:
    """Preserve an exact NOT_RUN request so the user never has to relay it again."""
    raise NotImplementedError('TODO: implement')

def queue_pending(path: Path, result: dict[str, Any], receipt_path: Path, *, provider: str, timeout: int, base_manifest: Path | None=None, bootstrap_new_project: bool=False) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def _resume_pending_claimed(path: Path, availability_file: Path, *, job_id: str | None=None, gemini_bin: Path | None=None, antigravity_bin: Path | None=None) -> tuple[dict[str, Any], Path | None, str]:
    raise NotImplementedError('TODO: implement')

def resume_pending(path: Path, availability_file: Path, *, job_id: str | None=None, gemini_bin: Path | None=None, antigravity_bin: Path | None=None) -> tuple[dict[str, Any], Path | None, str]:
    raise NotImplementedError('TODO: implement')

def main() -> int:
    raise NotImplementedError('TODO: implement')
