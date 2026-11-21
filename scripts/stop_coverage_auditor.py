# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Statically audit whether MAGI-managed Python workers check the STOP file."""
from __future__ import annotations
import argparse
import ast
import json
from pathlib import Path
from typing import Any, Iterable
from magi_autostart import REPO_ROOT, get_managed_daemons_inventory
from stop_latch import ENTRY_FUNCTIONS

def _mentions_stop(node: ast.AST) -> bool:
    """Return true when an expression resolves or refers to the canonical STOP path."""
    raise NotImplementedError('TODO: implement')

def _is_latch_entry_call(node: ast.Call, latch_names: set[str]) -> bool:
    """`stop_latch.enforce(...)` / `stop_latch.refuse_if_stopped(...)` or a name imported from it."""
    raise NotImplementedError('TODO: implement')

def source_honors_stop(path: Path) -> tuple[bool, str]:
    raise NotImplementedError('TODO: implement')

def python_entrypoint(command: Iterable[str], repo_root: Path=...) -> Path | None:
    raise NotImplementedError('TODO: implement')

def audit_configs(configs: Iterable[dict[str, Any]], repo_root: Path=...) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def main() -> int:
    raise NotImplementedError('TODO: implement')
