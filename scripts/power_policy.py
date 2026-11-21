# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""
PROGRAM:       power_policy.py
PROGRAMMER:    Magi 10 (claude, example_host), for Ethan
LAST MODIFIED: 2026-11-19
PURPOSE:       ONE reader for data/power/policy.json, shared by the root applier
               (twu_power_apply.py) and the user-level checker (twu_power_heal.py), so the two
               can never disagree about a power or fan target again.

WHY: on 2026-11-19 the root applier set EPP=balance_power on battery while the heal script demanded
     EPP=power, so the heal unit reported drift forever. Both now read this file.

SAFETY: values are CLAMPED to the "limits" block (and to hard-coded fallback limits if that block is
     missing or edited), because the root applier acts on whatever this file says. An invalid or
     missing file falls back to the built-in defaults below, never to "no limits".

CHANGE HISTORY:
  2026-11-19  Magi 10  Created.
"""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict

def _clamp(v: Any, lo: int, hi: int, fallback: int) -> int:
    """Return int(v) clamped to [lo, hi]; fallback when v is not a number."""
    raise NotImplementedError('TODO: implement')

def load(path: Path | None=None) -> Dict[str, Any]:
    """Read and sanitise the policy. Returns {"bat": {...}, "ac": {...}} of plain values (no 'why')."""
    raise NotImplementedError('TODO: implement')

def target(mode: str, path: Path | None=None) -> Dict[str, Any]:
    """Targets for one mode ('bat' or 'ac'); anything else is treated as 'ac'."""
    raise NotImplementedError('TODO: implement')
