# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""MagiPhone on/off switch. example_host is the only authority; no model calls, stdlib only.

Desired state lives in ONE example_host-local file (data/magi_phone/desired.json) with a revision number. Any
device (dashboard, example_host, M1 over the mesh later) only *asks* example_host to change it; a stale click is
refused with "changed" rather than silently overwriting another device (compare-and-swap on --expected-rev).

  off = disable+stop the heal timer first, then the app, then drop the tailnet forward on 8771
  on  = enable+start the app and heal timer, then restore the forward (refused while STOP is latched)

phone_path_heal.py reads the same file, so the 2-minute heal timer never undoes an intentional "off".
magi-responder (the Magi 0 clerk), tailscaled and every network/security unit are never touched.
Usage: magi_phone_toggle.py status [--json] | on | off  [--by NAME] [--expected-rev N]
"""
from __future__ import annotations
import argparse
import fcntl
import json
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

def real_runner(cmd):
    raise NotImplementedError('TODO: implement')

def real_health():
    raise NotImplementedError('TODO: implement')

def stop_present(root: Path=...) -> bool:
    raise NotImplementedError('TODO: implement')

def read_state(path: Path=...) -> dict:
    """Missing or unreadable file means the long-standing default: on, revision 0."""
    raise NotImplementedError('TODO: implement')

def is_off(path: Path=...) -> bool:
    raise NotImplementedError('TODO: implement')

def _write(state: dict, path: Path) -> None:
    raise NotImplementedError('TODO: implement')

def actual(runner=..., health=...) -> dict:
    raise NotImplementedError('TODO: implement')

def apply(desired: str, runner=...) -> list:
    """Idempotent. Every step is a fixed argv; failures are recorded, never raised."""
    raise NotImplementedError('TODO: implement')

def set_desired(desired: str, set_by: str, expected_rev=None, runner=..., health=..., state_path: Path=..., lock_path: Path=..., root: Path=...) -> dict:
    """Compare-and-swap then apply. Returns {ok, changed, state, reason, steps, actual}."""
    raise NotImplementedError('TODO: implement')

def status(runner=..., health=..., state_path: Path=...) -> dict:
    raise NotImplementedError('TODO: implement')

def main(argv=None, runner=..., health=...) -> int:
    raise NotImplementedError('TODO: implement')
