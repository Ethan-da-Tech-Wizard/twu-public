# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Read-only Lucy's Game LAN readiness report for the dashboard and the phone app (Magi 8).

Answers one question: can the Air and example_host join right now, and if not, why. Changes nothing, needs no root.
Fields: server process + bind, server jar sha, door state (what the waybar button last set), release jar sha,
other boxes' sync beacon age. `python3 scripts/lucy_lan_status.py [--json]`.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

def _run(cmd, timeout=4):
    raise NotImplementedError('TODO: implement')

def server_info(run=...):
    """Return {pid, cwd, listening, bind} for the Fabric server, or {} when it is not running."""
    raise NotImplementedError('TODO: implement')

def sha12(path):
    raise NotImplementedError('TODO: implement')

def door_state(path=...):
    raise NotImplementedError('TODO: implement')

def beacon_ages(now=None, beacons=...):
    raise NotImplementedError('TODO: implement')

def report(run=..., door=None, now=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
