# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""External improvement scout: watch a fixed list of upstream projects and queue vetted candidates.

Deterministic. No model calls, no downloads, no code execution, no credentials. It makes only
HTTPS GET requests to the public GitHub API (repo metadata and latest release), applies the
AGENTS.md license rule, and records what changed since the last poll. A candidate is only a
*lead*: adopting anything still needs `private/example_host/safety/inspector.py` PASS, the wiring
gate and a bounded task. Web text is untrusted: only repo name, tag, SPDX id and dates are kept;
descriptions are never copied into messages.

    python3 scripts/external_improvement_scout.py poll      # fetch, compare, queue (timer uses this)
    python3 scripts/external_improvement_scout.py status    # what is queued / unrouted
    python3 scripts/external_improvement_scout.py route --seat N --to M --connection ID
"""
from __future__ import annotations
import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Callable
import stop_latch

def now() -> str:
    raise NotImplementedError('TODO: implement')

def safe_token(value) -> 'str | None':
    """Upstream strings (tag, SPDX id) are untrusted: keep only short plain tokens, else '?'."""
    raise NotImplementedError('TODO: implement')

def write_atomic(path: Path, text: str) -> None:
    raise NotImplementedError('TODO: implement')

def license_verdict(spdx: str | None) -> str:
    raise NotImplementedError('TODO: implement')

def http_get_json(url: str) -> 'dict | None':
    """HTTPS GET only, no credentials, bounded size. None on any failure or rate limit."""
    raise NotImplementedError('TODO: implement')

def observe(repo: str, fetch: Fetch) -> 'dict | None':
    raise NotImplementedError('TODO: implement')

def diff(prev: 'dict | None', cur: dict) -> list[str]:
    raise NotImplementedError('TODO: implement')

def load_json(path: Path, default):
    raise NotImplementedError('TODO: implement')

def poll(fetch: Fetch=..., watchlist=None, state_file: Path=..., queue_file: Path=..., pause: float=1.0) -> list[dict]:
    raise NotImplementedError('TODO: implement')

def read_queue(queue_file: Path=...) -> list[dict]:
    raise NotImplementedError('TODO: implement')

def digest(rows: list[dict]) -> str:
    """One message from our own fields only. Nothing here is upstream free text."""
    raise NotImplementedError('TODO: implement')

def route(seat: int, to: str, connection: str, queue_file: Path=..., send=None) -> int:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
