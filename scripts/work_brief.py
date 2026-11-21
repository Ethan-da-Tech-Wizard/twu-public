# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
from __future__ import annotations
import argparse
import ast
import hashlib
import json
import os
import re
import sys
from pathlib import Path

class BriefError(Exception):
    """Raised when a brief cannot be built honestly; the message is plain words for Ethan."""

def configure(root) -> None:
    """Point the builder at a repo root (a frozen dashboard release runs this file from the release folder, not the repo)."""
    raise NotImplementedError('TODO: implement')

def load_kinds() -> dict:
    raise NotImplementedError('TODO: implement')

def load_cards() -> dict:
    raise NotImplementedError('TODO: implement')

def path_refusal(rel: str, read: bool=True) -> str | None:
    """Why a path may not be used in a brief, or None. read=True (code that will be excerpted) uses exactly the dashboard file browser's rules;
    read=False (a file that is only NAMED, never shown) additionally allows data/ files that are not secret."""
    raise NotImplementedError('TODO: implement')

def read_source(rel: str) -> str:
    raise NotImplementedError('TODO: implement')

def _parsed(src: str):
    """ast.parse is the expensive part; parse each distinct text once."""
    raise NotImplementedError('TODO: implement')

def _assign_names(n) -> list:
    raise NotImplementedError('TODO: implement')

def _py_symbol_span(src: str, symbol: str):
    raise NotImplementedError('TODO: implement')

def _brace_symbol_span(lines: list, symbol: str, suffix: str):
    raise NotImplementedError('TODO: implement')

def excerpt(rel: str, symbol: str=...) -> dict:
    """Cut a symbol (or the first 60 lines when symbol is empty) out of a live file. Splits on \\n only so line numbers match editors."""
    raise NotImplementedError('TODO: implement')

def validate_card(card: dict, families: set | None=None) -> list:
    """Every thing a card points at must exist and be readable by the rules above. Returns a list of plain-language problems."""
    raise NotImplementedError('TODO: implement')

def cards_fingerprint() -> str:
    """Hash of every card, the kinds file, families.json and the size+mtime of every file a card points at. If it is unchanged since the
    last good check, the cards cannot have gone stale, so the (slow) validation can be skipped."""
    raise NotImplementedError('TODO: implement')

def check_all() -> list:
    raise NotImplementedError('TODO: implement')

def egress_code(text: str) -> str:
    """Reversible: code excerpts keep their exact shape, personal literals become unique tokens (see restore)."""
    raise NotImplementedError('TODO: implement')

def restore(text: str) -> str:
    """Inverse of egress_code, used on a model's reply before it is matched against the real files."""
    raise NotImplementedError('TODO: implement')

def egress_prose(text: str) -> str:
    """One-way, readable: names become 'the owner', workflow-internal lines are dropped, then the reversible literals are applied."""
    raise NotImplementedError('TODO: implement')

def _neutralise(text: str) -> str:
    """Card prose may say where private things live (useful for people). A prompt going to a third-party site must not advertise that,
    so any line naming such a place is DROPPED (the fixed off-limits sentence is stated once, in the rules). Deterministic; card text only."""
    raise NotImplementedError('TODO: implement')

def _clip(text: str, limit: int) -> str:
    raise NotImplementedError('TODO: implement')

def _fit_list(items: list, limit: int) -> str:
    """Keep whole bullet items in order until the cap; never cut an item in the middle."""
    raise NotImplementedError('TODO: implement')

def _excerpt_block(ex: dict) -> str:
    raise NotImplementedError('TODO: implement')

def _signature_only(ex: dict) -> dict:
    """For an excerpt too big for its cap: keep the opening lines (def line and docstring) and say how much was left out."""
    raise NotImplementedError('TODO: implement')

def _safe_excerpt(ex: dict, notes: list):
    raise NotImplementedError('TODO: implement')

def _fill(excerpts: list, cap: int, omitted: list, shown: list, notes: list) -> str:
    """Add excerpts in priority order while they fit; a big one falls back to its opening lines; otherwise it is listed as omitted."""
    raise NotImplementedError('TODO: implement')

def _scrub_goal(goal: str) -> str:
    raise NotImplementedError('TODO: implement')

def build(area: str, kind: str, goal: str=..., constraints: list | None=None, tier: str=..., style: str=...) -> dict:
    """Returns {prompt, fingerprint, chars, tier, sections, excerpts, omitted, files, warnings}. Raises BriefError when it cannot be honest."""
    raise NotImplementedError('TODO: implement')

def _symbol_index() -> dict:
    """name -> [relative paths that define it at module level], over scripts/*.py (not tests). Built once per process, deterministic order."""
    raise NotImplementedError('TODO: implement')

def goal_mentions(goal: str, limit: int=6) -> tuple:
    """Files and symbols the goal sentence names, resolved to live excerpts. Returns (excerpts, unresolved). Deterministic: sorted, capped."""
    raise NotImplementedError('TODO: implement')

def test_style_excerpts(card: dict) -> list:
    """The head of the card's first test file and its first test function, so a model can copy the real style."""
    raise NotImplementedError('TODO: implement')

def _words(text: str) -> set:
    raise NotImplementedError('TODO: implement')

def suggest(goal: str, top: int=3) -> dict:
    """Deterministic guess of the area and kind from the goal sentence (word overlap, no AI). Ties break alphabetically. Never required:
    it only pre-selects the clicks. Returns {'areas': [(id, score)], 'kinds': [(id, score)]}."""
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
