# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/ethan_exposure_check.py - fail when a file or preview server is reachable from the network.

Found 2026-11-03: `python3 -m http.server 8080 --directory <the whole workspace>` ran for 1h46m bound to 0.0.0.0 and served company records
to the whole LAN. Rule: a preview or dev server binds 127.0.0.1 and serves one non-private folder. This check reads `ss -ltnp` and fails when a
listener on a non-loopback address belongs to a process that looks like a web or file server (python http.server, serve, a workspace path),
unless the process is on the small reviewed allowlist (Syncthing's sync port).

  python3 scripts/ethan_exposure_check.py [--json]       exit 0 checked, 1 exposure, 2 unverified
Read-only; stdlib only; no network; it never stops anything (stopping another agent's process is the owner's call).
"""
from __future__ import annotations
import json
import ipaddress
import os
import platform
import plistlib
import re
import shlex
import stat
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

def loopback(address: str) -> bool:
    raise NotImplementedError('TODO: implement')

def sync_listener(row: dict) -> bool:
    raise NotImplementedError('TODO: implement')

def parse_ss(text: str) -> list:
    """Rows from `ss -ltnp`: {addr, port, proc, pid}. Unparseable lines are skipped."""
    raise NotImplementedError('TODO: implement')

def cmdline(pid: int) -> str:
    raise NotImplementedError('TODO: implement')

def parse_lsof(text: str, protocol: str=...) -> list:
    """Parse lsof field output, retaining every TCP listener and its process label."""
    raise NotImplementedError('TODO: implement')

def parse_netstat(text: str, protocol: str) -> list:
    """macOS numeric kernel socket inventory, including other users' sockets."""
    raise NotImplementedError('TODO: implement')

def kernel_listeners(protocol: str) -> list:
    raise NotImplementedError('TODO: implement')

def udp_listeners(full_host: bool=False) -> list:
    raise NotImplementedError('TODO: implement')

def process_identity(pid: int) -> dict:
    """Identify an executable using the OS, never execute it or disclose its arguments."""
    raise NotImplementedError('TODO: implement')

def classify_listener(row: dict, identity: dict) -> dict:
    raise NotImplementedError('TODO: implement')

def inventory_report() -> dict:
    """Current TCP and bound UDP metadata for the dashboard; no network or state writes."""
    raise NotImplementedError('TODO: implement')

def dashboard_launch_identity(home: Path | None=None) -> dict:
    """Attribute the local dashboard role, without treating a Python signature as script trust."""
    raise NotImplementedError('TODO: implement')

def listeners(full_host: bool=False) -> list:
    raise NotImplementedError('TODO: implement')

def exposures(rows: list, cmd_of=..., root: str=...) -> list:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
