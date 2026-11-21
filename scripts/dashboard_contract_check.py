# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""
PROGRAM:       dashboard_contract_check.py
PROGRAMMER:    Magi 10 (claude, example_host), MAGI_TODO 00eae68c
LAST MODIFIED: 2026-11-20
PURPOSE:       Measure how many dashboard panels already conform to the JSON panel contract
               (docs/codebase/migration/schemas/panel.v1.schema.json = what exists today,
                panel.v2.schema.json = the target a new UI would rely on).  Read-only and offline:
               it imports the panel modules, calls each panel's build(ctx) once with a normal
               context, and validates the returned dict.  It never starts the dashboard, never
               runs an action, never writes, and NEVER raises: a broken panel is a row in the
               report, not a crash.  It runs at low priority (os.nice) so it does not slow the
               dashboard or heat the laptop.

WHY: a UI migration (docs/codebase/MIGRATION_GUIDE.md) is only safe if every panel's data shape is
     known and checked.  This tool is that check, and it is the parity test a new UI is built against.

COMMANDS
  python3 scripts/dashboard_contract_check.py check [--json] [--panel NAME] [--no-build]
      check      build every panel once and validate raw output against v1 and v2
      --no-build only validate the schema files themselves (fast self-test)
  Exit status is always 0 (informational): use the counts, not the exit code.

VALIDATOR: a small stdlib JSON-Schema subset (type, required, properties, enum, const, pattern,
           minLength, maxLength, maxItems, items, $ref, allOf).  No third-party package is needed
           (jsonschema is not installed), which also keeps the 20-year dependency list short.

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
from typing import Any, Dict, List, Optional, Tuple

def _type_ok(value: Any, want: Any) -> bool:
    """True when value matches a JSON-Schema type name or a list of names (bool is not a number)."""
    raise NotImplementedError('TODO: implement')

def load_schema(name: str, schema_dir: Path=...) -> Dict[str, Any]:
    """Load one schema file by file name; returns {} if it is missing or unreadable (never raises)."""
    raise NotImplementedError('TODO: implement')

def validate(value: Any, schema: Dict[str, Any], root_schema: Optional[Dict[str, Any]]=None, schema_dir: Path=..., path: str=...) -> List[str]:
    """Return a list of 'path: problem' strings (empty list = valid).  Implements the schema subset documented above."""
    raise NotImplementedError('TODO: implement')

def _panel_modules() -> Tuple[Dict[str, Any], Dict[str, str]]:
    """Discover panel modules the same way the dashboard does; returns ({name: module}, {name: why_not_loaded})."""
    raise NotImplementedError('TODO: implement')

def check_panels(only: Optional[str]=None, build: bool=True) -> Dict[str, Any]:
    """Build each panel once and validate against v1 and v2.  Returns a report dict (never raises)."""
    raise NotImplementedError('TODO: implement')

def main(argv: Optional[List[str]]=None) -> int:
    raise NotImplementedError('TODO: implement')
