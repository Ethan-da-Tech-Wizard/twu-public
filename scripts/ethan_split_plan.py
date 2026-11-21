# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Split planner: PRIVATE data side (stays local forever) versus CODE side (fit to publish under GPL-3).

Deterministic, standard library only, read-only on the workspace. Nothing here moves or deletes an original; the copy step
only COPIES, and refuses to write anywhere except under the scratch split_work directory.

  python3 scripts/ethan_split_plan.py classify            # walk the repo, write data/split/MANIFEST.json + SUMMARY.md
  python3 scripts/ethan_split_plan.py copy [--apply]       # dry-run by default; --apply copies into split_work/{code_repo,private_vault}
  python3 scripts/ethan_split_plan.py verify [--code DIR] [--vault DIR]   # proofs + license table (data/split/LICENSES.json/.md)

Classes
  PRIVATE  never leaves this machine (chat/transcripts, personal data, secrets, business, backups, weights, generated data)
  CODE     scripts, tests, tooling and docs that scanned clean and are fit to publish
  REVIEW   a human must decide (possible secret or personal data, large, binary, commercial, or instruction docs); copied nowhere

Note on .gitignore: this repo's .gitignore itself ignores scripts/ and data/, so it cannot be used as the classifier. Rules below are explicit.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

def personal_terms() -> re.Pattern:
    raise NotImplementedError('TODO: implement')

def is_binary(head: bytes) -> bool:
    raise NotImplementedError('TODO: implement')

def scan_text(text: str, terms: re.Pattern) -> dict:
    """Return {'hard': [...], 'pii': [...], 'soft': [...]} naming each pattern kind found (no matched text: safe to log)."""
    raise NotImplementedError('TODO: implement')

def scan_file(path: Path, terms: re.Pattern) -> dict | None:
    raise NotImplementedError('TODO: implement')

def _stable_small_file(path: Path, limit: int=...) -> tuple[bytes | None, str | None]:
    """Read and hash a small regular file through O_NOFOLLOW; detect replacement during the read."""
    raise NotImplementedError('TODO: implement')

def classify_path(rel: str, path: Path, terms: re.Pattern, *, raw: bytes | None=None) -> tuple[str, list[str], dict]:
    """Return (class, reasons, scan). Pure function of the path and file content."""
    raise NotImplementedError('TODO: implement')

def walk_files(root: Path):
    raise NotImplementedError('TODO: implement')

def classify(root: Path=...) -> dict:
    raise NotImplementedError('TODO: implement')

def summarize(m: dict) -> dict:
    raise NotImplementedError('TODO: implement')

def human(n: int) -> str:
    raise NotImplementedError('TODO: implement')

def write_summary(m: dict, s: dict, path: Path) -> None:
    raise NotImplementedError('TODO: implement')

def cmd_classify(a) -> int:
    raise NotImplementedError('TODO: implement')

def validate_manifest(manifest: dict, *, allowed_root: Path | None=None) -> dict:
    raise NotImplementedError('TODO: implement')

def read_manifest(path: Path, *, allowed_root: Path | None=None) -> dict:
    raise NotImplementedError('TODO: implement')

def write_private_text(path: Path, content: str) -> None:
    raise NotImplementedError('TODO: implement')

def write_manifest(path: Path, manifest: dict) -> None:
    raise NotImplementedError('TODO: implement')

def load_manifest() -> dict:
    raise NotImplementedError('TODO: implement')

def under_scratch(p: Path) -> Path:
    raise NotImplementedError('TODO: implement')

def plan_copy(m: dict) -> dict:
    raise NotImplementedError('TODO: implement')

def _safe_workspace_file(root: Path, rel: str) -> Path | None:
    raise NotImplementedError('TODO: implement')

def _safe_destination(dest: Path, target: Path) -> None:
    raise NotImplementedError('TODO: implement')

def secure_private_tree(root: Path) -> None:
    """Restrict an existing private vault and its history before any private copy work."""
    raise NotImplementedError('TODO: implement')

def copy_files(src_root: Path, rels: list[str], dest: Path, apply: bool, *, manifest: dict, expected_class: str) -> int:
    raise NotImplementedError('TODO: implement')

def cmd_copy(a) -> int:
    raise NotImplementedError('TODO: implement')

def sha256(path: Path) -> str:
    raise NotImplementedError('TODO: implement')

def detect_license(text: str, spdx: list, is_license_file: bool) -> str:
    """Strictest-first detection on the header (or a whole license file). Source files that merely mention a license in code are
    not caught because only the first 3000 characters are read and a license-ish word must be present."""
    raise NotImplementedError('TODO: implement')

def license_scan(tree: Path, rels: list[str] | None=None) -> dict:
    raise NotImplementedError('TODO: implement')

def spdx_header(rel: str) -> str | None:
    raise NotImplementedError('TODO: implement')

def write_license_table(res: dict, path: Path) -> None:
    raise NotImplementedError('TODO: implement')

def verify(m: dict, code: Path, vault: Path, src: Path, check_vault: bool=True, hash_private: bool=False) -> dict:
    raise NotImplementedError('TODO: implement')

def cmd_verify(a) -> int:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
