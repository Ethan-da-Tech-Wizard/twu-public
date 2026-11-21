# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/sync_health_monitor.py — warn loudly when sync is broken, stay silent when it works.

Ethan's rule (2026-10-25): every computer either gives constant warnings that
sync is not in place, or gives no warnings, meaning sync is perfect. Data must
never be lost between boxes.

Cross-platform (Linux + macOS). Every run:
  1. Checks the local Syncthing: process up, REST API answering, no folder in
     an error/stopped state, no paused devices, no recent system errors.
  2. Writes this host's beacon to data/sync_beacons/<host>.json. Beacons travel
     through sync itself, so a fresh beacon from another host is hard proof
     that data flowed from that host recently.
  3. Archive only redundant data conflicts with before/after evidence. Different
     versions stay unhealthy and linked to a durable repair task.
  4. Journal changed faults and recovery. Routine sync findings do not bypass
     the central immediate-action notification policy.

A quiet foreign beacon alone is NOT a fault (that box may simply be off);
beacon ages are recorded in the receipt so Magi can judge. The mesh matrix
(--mesh, and the "mesh" receipt key) is informational only and never alerts.
"""
from __future__ import annotations
import json
import hashlib
import tempfile
import stat
import os
import platform
import re
import subprocess
import sys
import time
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional

def _detect_host() -> str:
    raise NotImplementedError('TODO: implement')

def config_candidates():
    raise NotImplementedError('TODO: implement')

def api_key() -> Optional[str]:
    raise NotImplementedError('TODO: implement')

def rest(endpoint: str, key: str, timeout: float=10.0) -> Any:
    raise NotImplementedError('TODO: implement')

def syncthing_running(run=...) -> Optional[bool]:
    """True/False when pgrep gave a real answer (rc 0 / rc 1); None when it could
    not run (example_host, sysctl denied, timeout): unknown is not 'not running'."""
    raise NotImplementedError('TODO: implement')

def syncthing_uptime_seconds(run=...) -> float:
    """Elapsed seconds of the syncthing process; 0.0 when unknown."""
    raise NotImplementedError('TODO: implement')

def collect_faults(key: Optional[str], run=..., rest_call=...) -> List[str]:
    """Definite local faults only; an off peer is never a fault."""
    raise NotImplementedError('TODO: implement')

def connections_summary(key: Optional[str], rest_call=...) -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def write_beacon(now: Optional[float]=None) -> Path:
    raise NotImplementedError('TODO: implement')

def foreign_beacon_ages(now: Optional[float]=None) -> Dict[str, float]:
    raise NotImplementedError('TODO: implement')

def short_host(name: Optional[str]) -> str:
    """Same rule as magi.short_host: casefolded, without a .local suffix."""
    raise NotImplementedError('TODO: implement')

def load_host_names(roles_path: Optional[Path]=None, retired_path: Optional[Path]=None):
    """(canonical host list, {short alias: canonical}, {short retired name}) from the existing data files:
    data/fleet_roles.json hosts + aliases, and data/retired_hosts.json (host -> replaced_by)."""
    raise NotImplementedError('TODO: implement')

def read_beacon_times(beacon_dir: Optional[Path]=None) -> Dict[str, float]:
    """{file stem: beacon timestamp}; a corrupt beacon falls back to file mtime, unreadable ones are skipped."""
    raise NotImplementedError('TODO: implement')

def mesh_matrix(beacons: Dict[str, float], local_connections: Dict[str, bool], now: float, hosts: List[str], alias: Dict[str, str], local: str=..., retired: frozenset=...) -> Dict[str, Any]:
    """Pure. Reachability for every ordered pair (src -> dst) of known hosts.

    direct   - this host's Syncthing reports the peer connected (pairs with this host only)
    via-peer - the relevant beacon is <= 30 min old but no direct connection (a third host carries it)
    stale    - that beacon is older; age_min is given
    unknown  - no beacon ever
    The relevant beacon is src's, except for local->peer where it is the peer's (src is us, so only
    the peer's arriving beacon shows the mesh is alive). Beacons prove data flow only toward this host,
    so a pair between two other hosts is inferred from the weaker of its two ends' beacons.
    A beacon under a retired host name never counts as its replacement being fresh: it is always
    'stale' (retired_name given) unless the replacement has a beacon of its own. A direct pair also
    carries beacon = fresh | stale | missing, so "connected but silent" differs from fully unknown.
    """
    raise NotImplementedError('TODO: implement')

def _age_text(minutes: float) -> str:
    raise NotImplementedError('TODO: implement')

def render_mesh(mesh: Dict[str, Any]) -> str:
    raise NotImplementedError('TODO: implement')

def mesh_local_connections(key: Optional[str], rest_call=...) -> Dict[str, bool]:
    """{device name: connected} from the local Syncthing API; {} when it cannot answer."""
    raise NotImplementedError('TODO: implement')

def build_mesh(now: float, key: Optional[str], rest_call=...) -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def conflict_files(root: Optional[Path]=None, limit: int=20) -> List[str]:
    """Syncthing conflict copies outside archived trees: each one is a divergence
    that silently forked someone's data and must be surfaced, never ignored."""
    raise NotImplementedError('TODO: implement')

def repair_conflicts(paths, root=None, now=None):
    """Archive only copies already retained byte-for-byte; never choose between edits.

    Divergent source, SQLite, connection ownership and official records require
    their own reviewed reconciliation. They stay in place and remain unhealthy.
    """
    raise NotImplementedError('TODO: implement')

def track_repair(result):
    """Reuse one open host-owned repair task; never auto-complete unresolved work."""
    raise NotImplementedError('TODO: implement')

def peer_silence_fault(connections: Dict[str, Any], ages_min: Dict[str, float]) -> Optional[str]:
    """Magi 6's gap (A6-SYNC-PLAN-001): an off peer is not a fault, but NO peer
    connected while every foreign beacon is over a day old means this box has
    been cut off long enough that it can no longer tell - warn."""
    raise NotImplementedError('TODO: implement')

def warn(faults: List[str], run=...) -> None:
    raise NotImplementedError('TODO: implement')

def fault_identity(result: Dict[str, Any]) -> str:
    """Bind the full fault strings and conflict paths, never the shortened journal text."""
    raise NotImplementedError('TODO: implement')

def previous_receipt() -> Optional[Dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def save_receipt(result: Dict[str, Any]) -> None:
    raise NotImplementedError('TODO: implement')

def check_once(now: Optional[float]=None, run=..., rest_call=..., auto_heal: bool=True) -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def mesh_main() -> int:
    """Read-only apart from merging the matrix into the existing receipt (no alert, no beacon)."""
    raise NotImplementedError('TODO: implement')

def main() -> int:
    """Always exit 0: unhealthy sync is reported through the receipt, beacon, notification and alarms.

    A nonzero exit made twu-sync-health.service 'failed' (which then raised its own startup alarm) every
    time sync was merely unhealthy, and a transient error (Syncthing restarting, REST refused) crashed it.
    """
    raise NotImplementedError('TODO: implement')
