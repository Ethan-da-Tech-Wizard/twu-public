# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""
PROGRAM:       dashboard_migration_inventory.py
PROGRAMMER:    Magi 10 (claude, example_host), MAGI_TODO 00eae68c
LAST MODIFIED: 2026-11-20
PURPOSE:       Generate docs/codebase/migration/INVENTORY.md: every dashboard route, API endpoint, static asset,
               panel, owner action and control, with what each reads and how hard it would be to expose as a JSON
               API.  It is GENERATED from the real code (regex over source text, imports of the panel modules, the
               offline control inventory) so it never goes stale: re-run it any time.

SAFETY:        read-only.  It never starts the dashboard, never runs an action, never executes a script it
               describes.  It parses source text with regular expressions and imports ONLY the panel modules and the
               control inventory (both are pure builders).  The route-security column is a HEURISTIC (keyword search
               in each route's branch of twu_dashboard.py) and says so.

USAGE:         python3 scripts/dashboard_migration_inventory.py [--out PATH] [--no-build]
               --no-build skips building panels (uses only static text; fast).

CHANGE HISTORY:
  2026-11-20  Magi 10  Created.
"""
from __future__ import annotations
import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any, Dict, List

def _read(p: Path) -> str:
    raise NotImplementedError('TODO: implement')

def routes_from_server(src: str) -> List[Dict[str, Any]]:
    """One row per route string found in `route ==`, `route in (...)`, `route.startswith(...)` and `path ==` tests."""
    raise NotImplementedError('TODO: implement')

def post_paths(src: str) -> List[str]:
    raise NotImplementedError('TODO: implement')

def panel_sources() -> Dict[str, str]:
    raise NotImplementedError('TODO: implement')

def data_reads(text: str) -> Dict[str, Any]:
    """What a panel module reads: workspace files named in read_json/age_hours/exists/Path calls, plus flags."""
    raise NotImplementedError('TODO: implement')

def api_difficulty(info: Dict[str, Any], row: Dict[str, Any]) -> str:
    """easy: data already shaped as rows; medium: subprocess/sqlite reads or many actions; hard: writes, network or live terminals."""
    raise NotImplementedError('TODO: implement')

def build_panel_rows(build: bool) -> List[Dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def action_ids() -> List[str]:
    raise NotImplementedError('TODO: implement')

def control_counts() -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def registry_counts() -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def render(build: bool=True) -> str:
    raise NotImplementedError('TODO: implement')

def main(argv: List[str] | None=None) -> int:
    raise NotImplementedError('TODO: implement')
