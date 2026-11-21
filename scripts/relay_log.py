# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/relay_log.py - append-only log of Claude->DeepSeek->Claude relay rounds (per-host shards).

data/relay/<host>.jsonl: events out / in / decision. Only hashes, counts and sanitized ids are stored, never raw text.
Item ids: kept only as i<digits>, item-<digits> or a <=3 digit number (else sha256[:10]); decision reasons: length + sha256[:10] only.
Hosts: kept only if ^[a-z0-9]{1,16}$ (else sha256[:10]). Every string field passes a final relay_scrub guard.
keep_raw was removed (no caller used it): passing keep_raw=True raises RelayError.
Idempotent on (round, kind, hash). Locking: flock around check+append, then write_guard.safe_append.
Stdlib only, no network.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import platform
import re
import stat
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
import incident_ledger
import relay_scrub
import write_guard

class RelayError(Exception):
    pass

def _h10(x: Any) -> str:
    raise NotImplementedError('TODO: implement')

def _norm_host(host: Any) -> str:
    raise NotImplementedError('TODO: implement')

def _norm_id(item_id: Any) -> str:
    raise NotImplementedError('TODO: implement')

def _guard(v: Any) -> Any:
    """Final guard for a string field: anything relay_scrub would change (or refuse) becomes its hash."""
    raise NotImplementedError('TODO: implement')

def _guard_event(ev: Dict[str, Any]) -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def relay_dir(root: Path) -> Path:
    raise NotImplementedError('TODO: implement')

def _safe_host(host: str) -> str:
    raise NotImplementedError('TODO: implement')

def shard_path(root: Path, host: str=...) -> Path:
    raise NotImplementedError('TODO: implement')

def _iso(ts: float) -> str:
    raise NotImplementedError('TODO: implement')

def sha(text: str) -> str:
    raise NotImplementedError('TODO: implement')

def scrub_text(text: Any):
    """Return (scrubbed_text, {category: count}). Uses incident_ledger's secret patterns."""
    raise NotImplementedError('TODO: implement')

def _scrub_short(x: Any, limit: int) -> str:
    raise NotImplementedError('TODO: implement')

def _check_shard_path(root: Path, path: Path) -> None:
    """Refuse (RelayError) a symlink on data/, data/relay/ or the shard, a non-regular or hardlinked shard.
    Runs BEFORE any dir or lock is created. Missing components are fine."""
    raise NotImplementedError('TODO: implement')

def _read_lines(path: Path, guard: bool=False) -> List[Dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def read_events(root: Path) -> List[Dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def _key(rec: Dict[str, Any]):
    raise NotImplementedError('TODO: implement')

def _locked_append(root: Path, ev: Dict[str, Any], host: str) -> bool:
    """Append ev unless (round, kind, hash) already in this host's shard. True if written."""
    raise NotImplementedError('TODO: implement')

def next_round(root: Path=...) -> int:
    raise NotImplementedError('TODO: implement')

def _no_keep_raw(keep_raw: Any) -> None:
    raise NotImplementedError('TODO: implement')

def _check_round(rnd: Any) -> int:
    raise NotImplementedError('TODO: implement')

def record_out(root: Path, rnd: int, text: str, keep_raw: bool=False, host: str=..., now: Optional[float]=None) -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def record_in(root: Path, rnd: int, text: str, items: Optional[List[Dict[str, Any]]]=None, keep_raw: bool=False, host: str=..., now: Optional[float]=None) -> Dict[str, Any]:
    """items: [{'id': str, 'flagged': bool, 'injection': bool}]. Injection items are bridged to incident_ledger."""
    raise NotImplementedError('TODO: implement')

def bridge_injection(root: Path, rnd: int, item_id: str, host: str=..., now: Optional[float]=None) -> str:
    """Call incident_ledger.record(root, source='relay', key, detail) per its real API.
    The real API only accepts SOURCES (no 'relay'): it raises Refused. We do NOT guess another source;
    we return 'refused: ...' and print it to stderr so the gap is visible."""
    raise NotImplementedError('TODO: implement')

def record_decision(root: Path, item_id: str, verdict: str, reason: str=..., rnd: Optional[int]=None, host: str=..., now: Optional[float]=None) -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def history(root: Path=..., limit: int=20) -> List[Dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def _n(v: Any) -> int:
    raise NotImplementedError('TODO: implement')

def summary(root: Path=...) -> str:
    raise NotImplementedError('TODO: implement')

def main(argv: Optional[List[str]]=None, root: Path=...) -> int:
    raise NotImplementedError('TODO: implement')
