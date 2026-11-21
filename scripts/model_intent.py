# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/model_intent.py - tools say WHY they are about to stop or restart the local model server.

Without this, a deliberate benchmark restart looked identical to a crash ("Model stopped mid-work"), and a benchmark
that left the server down went unnoticed. A tool declares an intent with a time limit; the activity beacon explains
the stop with that reason, and raises a flag (never starts a model itself) if the server is still down when the
limit passes.
"""
from __future__ import annotations
import contextlib
import json
import os
import platform
import time
from pathlib import Path
from typing import Any, Dict, Iterator, Optional

def declare(by: str, intent: str, ttl_seconds: float, path: Optional[Path]=None, now: Optional[float]=None) -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def current(path: Optional[Path]=None) -> Optional[Dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def is_live(rec: Optional[Dict[str, Any]], now: Optional[float]=None) -> bool:
    raise NotImplementedError('TODO: implement')

def is_overdue(rec: Optional[Dict[str, Any]], now: Optional[float]=None) -> bool:
    raise NotImplementedError('TODO: implement')

def clear(path: Optional[Path]=None) -> None:
    raise NotImplementedError('TODO: implement')

@contextlib.contextmanager
def restarting(by: str, intent: str, ttl_seconds: float, path: Optional[Path]=None) -> Iterator[Dict[str, Any]]:
    """Declare for the duration of the block. The intent is cleared only on a clean exit; if the block raises it stays,
    so it becomes overdue and the beacon flags the unfinished restart."""
    raise NotImplementedError('TODO: implement')
