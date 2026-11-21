# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""twu_docs: find the rule or fact you need in the big documents without reading them. No AI, no network.

  twu_docs.py find "loose words"      the 5 best matching paragraphs/rows/bullets: file:line, heading, short text
  twu_docs.py find "words" --full     also print the full text of the best match
  twu_docs.py show FILE:LINE          the full unit (bullet, table row or paragraph) that starts at that line
  twu_docs.py list                    the documents searched and how many units each has
  twu_docs.py links [DOC] [--broken]  index markdown links across documents and verify local targets
  twu_docs.py rules list|lint|render|digest|changed|ack|audit|propose|ratify|seed|line   the rules registry (scripts/twu_rules.py)

Why: AGENTS.md (~7,100 words) and MOVING_PARTS.md (~27,000 words) are the 'read first' set, and no model reads that reliably. The rules already say 'read the part you need';
this makes that possible. Documents are split into UNITS (a bullet with its continuation lines, a table row, a paragraph) that remember their heading, and searched with SQLite FTS5 (BM25) plus a small
synonym table and typo tolerance. Always reads the live files, so it is never stale. Honest limit: word-based, not meaning-based; if nothing matches it says so instead of guessing.
"""
from __future__ import annotations
import difflib, hashlib, json, os, re, sqlite3, sys
from pathlib import Path

def workspace_markdown(root=...):
    raise NotImplementedError('TODO: implement')

def reference_lines(target, root=...):
    raise NotImplementedError('TODO: implement')

def unlinked(root=..., summary=False):
    raise NotImplementedError('TODO: implement')

def graph(target, root=..., full=False):
    raise NotImplementedError('TODO: implement')

def strip_md(s):
    raise NotImplementedError('TODO: implement')

def units_of(path, rel):
    """[{file, line, heading, text}] for one document."""
    raise NotImplementedError('TODO: implement')

def all_units(root=..., docs=None):
    raise NotImplementedError('TODO: implement')

def links_of(path, rel, root=...):
    """Extract all markdown links [{file, line, text, target, exists}] from a document."""
    raise NotImplementedError('TODO: implement')

def all_links(root=..., docs=None):
    raise NotImplementedError('TODO: implement')

def expand(words):
    raise NotImplementedError('TODO: implement')

def find(query, root=..., docs=None, limit=5):
    raise NotImplementedError('TODO: implement')

def show(spec, root=..., docs=None):
    raise NotImplementedError('TODO: implement')

def show_range(spec, root=..., token_cap=1200, line_cap=80):
    raise NotImplementedError('TODO: implement')

def export_vault(output_dir: Path=...) -> int:
    """Generate lightweight Obsidian markdown stub notes with [[wikilinks]] and YAML frontmatter."""
    raise NotImplementedError('TODO: implement')

def main(a=None):
    raise NotImplementedError('TODO: implement')
