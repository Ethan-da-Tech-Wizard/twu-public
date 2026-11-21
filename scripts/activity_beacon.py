# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/activity_beacon.py — passive visibility for the autonomous system.

Ethan's rule (2026-10-25): he must never be NEEDED to make things happen, but
he must SEE things happening. The beacon turns autonomous activity into quiet
desktop notifications, so watching requires no action:

  1. Every new rolling-journal entry (any Magi, any sweep) since the last run
     becomes one batched notification; repeated identical incidents are coalesced.
  2. Local-model state transitions are announced: started working, finished,
     paused for cooling (thermal guard), resumed.

Faults keep their own louder channels (watchdog, sync monitor); the beacon is
normal-urgency and never alarms. Cross-platform: notify-send on Linux,
osascript on macOS. State is host-sharded so boxes never conflict.
"""
from __future__ import annotations
import hashlib
import json
import os
import platform
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional
import model_intent

def notify(title: str, body: str, run=...) -> None:
    raise NotImplementedError('TODO: implement')

def _load_state() -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def _save_state(state: Dict[str, Any]) -> None:
    raise NotImplementedError('TODO: implement')

def journal_entries() -> List[Dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def model_state(run=..., now: Optional[float]=None) -> str:
    """'off' | 'paused' | 'generating' | 'idle' from process + log evidence."""
    raise NotImplementedError('TODO: implement')

def is_thermal_transition(previous: str, current: str) -> bool:
    """Whether a state transition is only a temporary cooling change."""
    raise NotImplementedError('TODO: implement')

def thermal_notice_allowed(state: Dict[str, Any], now: float) -> bool:
    """Limit cooling/resume toasts without hiding model-stop notifications."""
    raise NotImplementedError('TODO: implement')

def explained_stop(previous: str, current: str, intent_path: Optional[Path]=None, now: Optional[float]=None):
    """A stop that a tool declared in advance gets its real reason instead of the generic 'shut down' text."""
    raise NotImplementedError('TODO: implement')

def flag_overdue_restart(state: Dict[str, Any], current: str, intent_path: Optional[Path]=None, now: Optional[float]=None) -> Optional[str]:
    """Server still down after the tool's promised time: journal ONE incident (flag only; never starts a model)."""
    raise NotImplementedError('TODO: implement')

def journal_notice_allowed(entry: Dict[str, Any], incidents: Dict[str, str]) -> bool:
    """Coalesce an unchanged incident per source; explicit recovery resets it."""
    raise NotImplementedError('TODO: implement')

def check_once(run=..., now: Optional[float]=None) -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def main() -> int:
    raise NotImplementedError('TODO: implement')
