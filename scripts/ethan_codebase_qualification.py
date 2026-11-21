# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Turn one accepted provider change into a strict complete-codebase gate bundle."""
from __future__ import annotations
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from typing import Any
import uuid
from scripts import ethan_codebase_gate as gate

class QualificationError(ValueError):
    pass

def now() -> str:
    raise NotImplementedError('TODO: implement')

def sha256_file(path: Path) -> str:
    raise NotImplementedError('TODO: implement')

def link(path: Path) -> dict[str, str]:
    raise NotImplementedError('TODO: implement')

def snapshot_linked_file(source_link: dict[str, Any], destination: Path, label: str) -> dict[str, str]:
    """Copy hash-current evidence into an immutable qualification-owned path."""
    raise NotImplementedError('TODO: implement')

def read_json(path: Path, label: str) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def resolve_workspace(path: Path, *, file: bool=True) -> Path:
    raise NotImplementedError('TODO: implement')

def _acceptance_check(invocation: dict[str, Any], kind: str) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def package_qualification(project: Path, invocation_path: Path, base_manifest_path: Path | None=None) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')
