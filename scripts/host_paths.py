# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""
PROGRAM:       host_paths.py
PROGRAMMER:    Magi 10 (claude, example_host)
LAST MODIFIED: 2026-11-19
PURPOSE:       One place that gives every writer a PER-HOST file name, so two computers never write the
               same synced file (Syncthing then makes a *.sync-conflict-* copy on every cycle).

THE PATTERN (same idea as data/knowledge/hosts/<host>/index.db):
  data/tool_trials/scavenger/LATEST.json  ->  data/tool_trials/scavenger/LATEST.<host>.json
  per_host("a/b/name.ext")                ->  "a/b/name.<host>.ext"
  Writers call per_host(); readers call resolve(), which returns the per-host file if it exists and
  otherwise the legacy shared file (read-only fallback, so nothing breaks before the first new write).

HOST NAME: env TWU_HOST if set (tests and overrides), else the short hostname, lower-cased
  ("example_host", "example_host", "example_host").  Never empty.

CHANGE HISTORY:
  2026-11-19  Magi 10  Created for MAGI_TODO b82aae54 (sync naming collisions).
"""
from __future__ import annotations
import os
import socket
from pathlib import Path

def host_name() -> str:
    """Short, lower-case name of this computer; TWU_HOST overrides (used by tests)."""
    raise NotImplementedError('TODO: implement')

def per_host(rel, host: str | None=None) -> Path:
    """Insert the host name before the final suffix: a/LATEST.json -> a/LATEST.<host>.json."""
    raise NotImplementedError('TODO: implement')

def resolve(root, rel, host: str | None=None) -> Path:
    """Path to READ: this host's file if present, else the legacy shared file (read-only fallback)."""
    raise NotImplementedError('TODO: implement')
