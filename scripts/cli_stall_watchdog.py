# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/cli_stall_watchdog.py — notice a wedged interactive Ethan CLI session.

Observed 2026-10-25: the local model answered a tool result with a completely
empty turn and the CLI sat "thinking" forever while the GPU idled. The bridge
now retries empty turns (gemini_broker_bridge.py), but if a session ever wedges
again for any reason, this watchdog notices and says so instead of letting it
sit silently.

A WEDGED session is distinguishable from an idle one by how its transcript ends:
  * wedged — the last meaningful event is a tool result (functionResponse) or an
    empty model message: the model never finished its turn.
  * idle   — the last meaningful event is a model message with real text; the
    session is simply waiting for Ethan.

On detection (CLI process running + transcript quiet past the threshold +
wedged-shaped ending) it journals an incident, sends a desktop notification,
and writes a receipt. It never touches the session itself. One alert per
session per quiet-period (deduped by transcript mtime).
"""
from __future__ import annotations
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

def cli_session_running(run=...) -> bool:
    raise NotImplementedError('TODO: implement')

def newest_transcript(chats_root: Optional[Path]=None) -> Optional[Path]:
    raise NotImplementedError('TODO: implement')

def transcript_shape(path: Path) -> str:
    """Returns 'STALE_ADMISSION', 'WEDGED', 'IDLE', or 'UNKNOWN' from how the transcript ends."""
    raise NotImplementedError('TODO: implement')

def gpu_idle(run=...) -> bool:
    raise NotImplementedError('TODO: implement')

def _load_state() -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def _save_state(state: Dict[str, Any]) -> None:
    raise NotImplementedError('TODO: implement')

def _alert(session: Path, quiet_sec: float, shape: str=...) -> None:
    raise NotImplementedError('TODO: implement')

def check_once(now: Optional[float]=None, quiet_seconds: float=..., chats_root: Optional[Path]=None, run=...) -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def main() -> int:
    raise NotImplementedError('TODO: implement')
