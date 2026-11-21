# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Compile saved Magi presence and outbox observations into structured JSON.

These records do not prove live attendance or authorize work. Current coordination
lives in MAGI_0/MASTER_HANDOFF.md; workspace rules live in AGENTS.md.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import time
from typing import Any, Dict, Optional

def get_latest_seat_event(seat_id: str) -> Optional[Dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def get_seat_presence(seat_id: str) -> Optional[Dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def get_fleet_agent_roster() -> Dict[str, Any]:
    """Return attributed saved presence metadata, never inferred roles or models."""
    raise NotImplementedError('TODO: implement')

def _live_cannon_counts() -> Optional[Dict[str, int]]:
    """Read saved registry counts without treating them as current test results."""
    raise NotImplementedError('TODO: implement')

def get_proven_accomplishments_stats() -> Dict[str, Any]:
    """Keep the legacy API shape while distinguishing saved counts from proof."""
    raise NotImplementedError('TODO: implement')

def compile_war_room_state() -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def run_compiler_daemon(interval: float=4.0):
    raise NotImplementedError('TODO: implement')
