# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""
PROGRAM:       source_hash_manifest.py
PROGRAMMER:    Magi 10 (claude, example_host)
LAST MODIFIED: 2026-11-19
PURPOSE:       Prove, per computer, that the SOURCE files are byte-identical across the fleet
               (MAGI_TODO task 73fa6e8d: "intended source hashes match on each box").

WHY: Syncthing reports "in sync" by its own index; nobody compared real file hashes between
  computers. Each computer writes ONE small manifest (sha256 of scripts/*.py, scripts/*.sh and
  the top-level *.md/*.json instruction files) and `compare` reads every host's manifest and
  names each file whose hash differs, is missing on a host, or whose manifest is older than
  the files it describes.

COMMANDS (read-only except `write`, which writes only data/health/SOURCE_HASHES.<host>.json):
  write     hash this computer's source set and write its manifest
  compare   read all manifests under data/health and report differences (exit 1 if any)

NEVER: runs nothing it reads, follows symlinks, hashes *.sync-conflict-* copies (those are
  preserved conflict copies, reported only as a count) or touches files outside the workspace.

CHANGE HISTORY:
  2026-11-19  Magi 10  Created for task 73fa6e8d.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import socket
import sys
import time
from pathlib import Path

def source_files():
    """Yield the workspace-relative source files that must match on every computer."""
    raise NotImplementedError('TODO: implement')

def sha256(path: Path) -> str:
    """sha256 of one file, read in 1 MiB blocks."""
    raise NotImplementedError('TODO: implement')

def write_manifest() -> Path:
    """Hash this computer's source set and write data/health/SOURCE_HASHES.<host>.json atomically."""
    raise NotImplementedError('TODO: implement')

def compare() -> int:
    """Compare every host manifest; print differences; return 1 when any exist."""
    raise NotImplementedError('TODO: implement')

def main() -> int:
    raise NotImplementedError('TODO: implement')
