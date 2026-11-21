# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""TWU dashboard launcher: allowlisted terminal launches plus HTTP guard helpers.

Stdlib only. No network, no model, no daemon, no HTTP server in this file.
A future POST route in the dashboard calls check_request() and then launch().

CROSS-DEVICE DESIGN (documentation only, not implemented here)
  Launching on ANOTHER box never executes remotely. The page writes a launch
  REQUEST file (id, requesting host, time, nonce; no argv) into a Syncthing
  synced folder. The target box's own local dashboard lists pending requests
  with an Approve button. Approve calls launch() locally, on that box, through
  the same allowlist, host check, loopback guard and audit. Nothing runs
  without local approval; a request older than 10 minutes (REQUEST_TTL_SECONDS)
  is expired and ignored. The request file carries only an allowlist id, never
  a command, so a forged or synced file cannot add commands.

LIMITS: a terminal window the user can type into is a shell. The allowlist
limits what the dashboard starts, not what happens after.
"""
import hashlib
import hmac
import json
import os
import secrets
import shlex
import shutil
import socket
import subprocess
import sys
import time
from pathlib import Path

class LauncherError(Exception):
    pass

def this_host():
    raise NotImplementedError('TODO: implement')

def valid_id(i):
    raise NotImplementedError('TODO: implement')

def load_allowlist(path=None):
    raise NotImplementedError('TODO: implement')

def _binary_ok(e, which=...):
    raise NotImplementedError('TODO: implement')

def list_entries(path=None, host=None, which=...):
    raise NotImplementedError('TODO: implement')

def plan(launcher_id, path=None, host=None, root=..., which=...):
    raise NotImplementedError('TODO: implement')

def shell_line(p):
    raise NotImplementedError('TODO: implement')

def terminal_command(p, system=None, which=...):
    """Return the argv of the process that opens a new terminal (not run here)."""
    raise NotImplementedError('TODO: implement')

def default_runner(cmd):
    raise NotImplementedError('TODO: implement')

def audit(p, requester, root=..., now=None):
    raise NotImplementedError('TODO: implement')

def launch(launcher_id, runner=..., requester=..., confirmed=False, path=None, host=None, root=..., system=None, which=...):
    raise NotImplementedError('TODO: implement')

def make_token():
    raise NotImplementedError('TODO: implement')

def _h(headers, name):
    raise NotImplementedError('TODO: implement')

def check_request(method, path, headers, expected_token, port, body_len=0):
    """Return (allowed, reason). Headers is a dict-like of the request."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
