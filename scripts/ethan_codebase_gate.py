# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Fail-closed evidence gate for Ethan CLI complete-codebase claims.

This validates current files and execution receipts. It never runs project code.
A deterministic fixture may prove the gate and project journey, but its overall
status remains NOT_RUN because it is not evidence of a Gemini/model invocation.
"""
from __future__ import annotations
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import sys
from typing import Any

class GateError(ValueError):
    pass

def sha256_file(path: Path) -> str:
    raise NotImplementedError('TODO: implement')

def require_object(value: Any, label: str) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def require_sha(value: Any, label: str) -> str:
    raise NotImplementedError('TODO: implement')

def require_timestamp(value: Any, label: str) -> str:
    raise NotImplementedError('TODO: implement')

def resolve_beneath(root: Path, relative: Any, label: str) -> Path:
    raise NotImplementedError('TODO: implement')

def read_linked_json(workspace: Path, link: Any, label: str) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def verify_linked_file(workspace: Path, link: Any, label: str) -> Path:
    raise NotImplementedError('TODO: implement')

def artifact_set_hash(artifacts: list[dict[str, str]]) -> str:
    raise NotImplementedError('TODO: implement')

def verify_execution_receipt(workspace: Path, link: Any, *, kind: str, expected_artifact_set: str) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def verify_model_invocation(workspace: Path, link: Any, label: str) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def verify_reviewer_change(workspace: Path, project_root: Path, link: Any, label: str) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def evaluate_manifest(manifest_path: Path, workspace: Path=...) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def main() -> int:
    raise NotImplementedError('TODO: implement')
