# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/gap_task_picker.py — turn the certifier's coverage gaps into the next CLI task.

ethan_certify.py deterministically finds scripts with no test. This picker turns
that gap list into the next bounded task for the local model through Ethan's
interactive CLI: it selects the smallest untested scripts (small enough for the
20B to handle well), and emits a ready-to-stage prompt in the proven pattern
(no search tools, absolute paths, read the source first, one write_file per
test, a one-sentence reply).

The loop this closes: certify finds the gap -> picker stages the task -> the
local model writes the test in Ethan's session -> a frontier Magi verifies it
independently (frontier_verification.py) -> the win becomes a verified training
pair and a journal entry. Deterministic gap finding, frontier verification.

This tool only reads the workspace and writes a prompt file; it never touches
Enki, the CLI, the bridge, or a running session.
"""
from __future__ import annotations
import argparse
import py_compile
import sys
import time
from pathlib import Path
from typing import List, Optional, Sequence, Tuple

def _is_referenced(name: str, scripts_dir: Path, extra_dirs: Optional[Sequence[Path]]=None) -> bool:
    """True when another file mentions this script: someone still points at it."""
    raise NotImplementedError('TODO: implement')

def freshness(path: Path, scripts_dir: Path, extra_dirs: Optional[Sequence[Path]]=None, now: Optional[float]=None) -> Tuple[bool, str]:
    """(current, reason). Deterministic staleness gate: a broken or abandoned
    script must never be recommended — writing tests for dead code wastes the
    model's run and pollutes the suite."""
    raise NotImplementedError('TODO: implement')

def untested_candidates(scripts_dir: Optional[Path]=None, min_size: int=..., max_size: int=..., check_fresh: bool=True, extra_ref_dirs: Optional[Sequence[Path]]=None, skipped: Optional[List[Tuple[str, str]]]=None) -> List[Tuple[int, str]]:
    """Smallest-first (size, name) list of current, untested scripts.

    Stale or broken scripts are excluded (and reported through `skipped` when a
    list is passed) so the picker never recommends outdated tools."""
    raise NotImplementedError('TODO: implement')

def build_prompt(names: Sequence[str], scripts_dir: Optional[Path]=None) -> str:
    """A staged CLI prompt in the proven pattern for 1..N small test-writing tasks."""
    raise NotImplementedError('TODO: implement')

def main(argv: Optional[Sequence[str]]=None) -> int:
    raise NotImplementedError('TODO: implement')
