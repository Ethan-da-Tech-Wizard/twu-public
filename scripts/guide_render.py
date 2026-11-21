# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
from __future__ import annotations
import html
import json
import os
import re
import sys
import tempfile
from pathlib import Path

def _href(url: str) -> str:
    """Only relative links and http(s)/mailto survive; .md becomes .html; anything else (javascript:, data:) becomes '#'."""
    raise NotImplementedError('TODO: implement')

def inline(text: str) -> str:
    """Escape first, then re-introduce a small safe set of inline markup."""
    raise NotImplementedError('TODO: implement')

def slug(text: str) -> str:
    raise NotImplementedError('TODO: implement')

def convert(md: str) -> tuple[str, str]:
    """Markdown -> (title, body html). Supports headings, paragraphs, bullet/numbered lists, fenced code, tables, rules."""
    raise NotImplementedError('TODO: implement')

def page(title: str, body: str, back: bool=True) -> str:
    raise NotImplementedError('TODO: implement')

def source_pages() -> list:
    raise NotImplementedError('TODO: implement')

def _put(path: Path, text: str, only_if_changed: bool) -> None:
    raise NotImplementedError('TODO: implement')

def render(only_if_changed: bool=False) -> dict:
    raise NotImplementedError('TODO: implement')

def render_manual(only_if_changed: bool=False) -> int:
    """The Owner's Manual as its own book (chapters are docs/OWNER_MANUAL/*.md). Returns the number of pages; 0 when the folder does not exist."""
    raise NotImplementedError('TODO: implement')

def _registered() -> bool:
    raise NotImplementedError('TODO: implement')

def register() -> None:
    """Add or refresh our one catalog entry; every other entry is preserved byte-for-byte in meaning (JSON re-written atomically)."""
    raise NotImplementedError('TODO: implement')
