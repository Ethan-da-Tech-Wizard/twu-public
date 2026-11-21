# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""The /guide/where page. Standard library only; works offline."""
from __future__ import annotations
import html
import re
import sys
from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import code_locator

def _e(v: Any) -> str:
    """HTML-escape any value (quotes included)."""
    raise NotImplementedError('TODO: implement')

def clean_query(q: Any, limit: int=120) -> str:
    """Search words: control characters removed, whitespace collapsed, at most `limit` characters."""
    raise NotImplementedError('TODO: implement')

def _copy(text: str) -> str:
    """Real Copy button (hidden until /static/copy.js runs); '' on failure (click-to-select text remains)."""
    raise NotImplementedError('TODO: implement')

def _with_script(body: str) -> str:
    raise NotImplementedError('TODO: implement')

def page(ctx: Optional[Dict[str, Any]]=None, q: str=..., kind: str=..., show_all: bool=False) -> str:
    raise NotImplementedError('TODO: implement')

def respond(root: Any, path: str) -> Tuple[int, bytes, str]:
    """Route /guide/where. Returns (status, body, mime) like dashboard_command_library_page.respond."""
    raise NotImplementedError('TODO: implement')
