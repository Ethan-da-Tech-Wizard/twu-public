# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Tool catalog: one honest list of every tool in scripts/, grouped by what Ethan wants to do.

Static only: it parses source with ast and regex. It never imports or runs a tool, uses no model, no network, no GPU.
(--help is deliberately NOT executed: many tools have side effects at import or on bare run; docstrings and argparse
declarations give the same facts safely.) Related: scripts/enki_tools.py lists only the tools Enki can run by name;
this catalog covers the whole folder, adds safety class, owner, tests, wiring, duplicates and a consolidate list.

  python3 scripts/ethan_tools_catalog.py            # write data/tools/CATALOG.json, CATALOG.md, TOOL_INDEX.txt
  python3 scripts/ethan_tools_catalog.py --check    # exit 1 if the saved catalog is stale (tool added/removed)
  python3 scripts/ethan_tools_catalog.py --index    # print the compact tool index (<=800 tokens)

Safety classes (strictest wins): never-run-by-agents, needs-root, affects-production, writes-local, read-only.
"""
from __future__ import annotations
import argparse
import ast
import json
import re
import subprocess
import sys
from pathlib import Path

def tool_files(root: Path) -> list[Path]:
    raise NotImplementedError('TODO: implement')

def parse_source(text: str, suffix: str) -> dict:
    """Return docstring-first-line, argparse description, option names, and a parse note."""
    raise NotImplementedError('TODO: implement')

def purpose_of(info: dict, name: str) -> str:
    raise NotImplementedError('TODO: implement')

def classify(name: str, text: str) -> str:
    raise NotImplementedError('TODO: implement')

def group_of(name: str, doc: str) -> str:
    raise NotImplementedError('TODO: implement')

def load_wiring(root: Path) -> dict:
    """Map script path -> list of capability ids that name it."""
    raise NotImplementedError('TODO: implement')

def git_authors(root: Path) -> dict:
    raise NotImplementedError('TODO: implement')

def reference_counts(root: Path, names: list[str]) -> dict:
    """How many OTHER files mention each tool (by file name or module name). Scans scripts, units, docs, manifests."""
    raise NotImplementedError('TODO: implement')

def moving_parts_names(root: Path) -> str:
    raise NotImplementedError('TODO: implement')

def norm_stem(name: str) -> str:
    raise NotImplementedError('TODO: implement')

def tokens(s: str) -> set:
    raise NotImplementedError('TODO: implement')

def find_duplicates(tools: list[dict]) -> dict:
    """name -> list of {other, why}. Same normalised stem, or very similar one-line purposes."""
    raise NotImplementedError('TODO: implement')

def replaces_hint(text: str) -> str:
    raise NotImplementedError('TODO: implement')

def build(root: Path=...) -> dict:
    raise NotImplementedError('TODO: implement')

def sentence(t: dict) -> str:
    raise NotImplementedError('TODO: implement')

def render_md(cat: dict) -> str:
    raise NotImplementedError('TODO: implement')

def tool_index(cat: dict, max_chars: int=2800) -> str:
    """Compact index of safe read-only tools (about 700 tokens at 4 chars per token)."""
    raise NotImplementedError('TODO: implement')

def write_all(root: Path=...) -> dict:
    raise NotImplementedError('TODO: implement')

def stale(root: Path=...) -> list[str]:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
