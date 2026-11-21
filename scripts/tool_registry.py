# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Auto-discover every tool in scripts/ so none is ever lost and Enki can see them all.

The Fleet Tool Cheatsheet is hand-curated, so a newly built tool is invisible to the system until
someone remembers to list it. This scans scripts/ deterministically and builds one complete registry:
every runnable tool, its one-line purpose, its entry command, and whether it has a test. Enki and the
cheatsheet read the registry instead of a memory. A tool that exists is therefore always known.

  python3 scripts/tool_registry.py            # rebuild data/tool_registry.json, print a summary
  python3 scripts/tool_registry.py --check     # fail if the saved registry is stale (for check_all)
  python3 scripts/tool_registry.py --list      # print every discovered tool
"""
from __future__ import annotations
import argparse
import ast
import json
from pathlib import Path

def _docline(source):
    """First non-empty line of the module docstring, or '' if none."""
    raise NotImplementedError('TODO: implement')

def _is_runnable(source):
    """A runnable tool has a __main__ guard (a CLI entry point), not just a library."""
    raise NotImplementedError('TODO: implement')

def discover():
    raise NotImplementedError('TODO: implement')

def build():
    raise NotImplementedError('TODO: implement')

def write():
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
