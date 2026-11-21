# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Game mode holds local inference without interrupting cross-device messaging.

on: set/preserve standby, stop only the verified local model, and pause an
enabled, active overseer timer. off: release only this same-boot session's
unchanged standby and restore only its paused, still-enabled timer. Neither
command controls Syncthing, the bridge, retired timers, or model startup.
"""
import fcntl
import json
import os
import re
import signal
import stat
import subprocess
import sys
import tempfile
import time
import uuid
from contextlib import contextmanager
from pathlib import Path

def sh(cmd):
    raise NotImplementedError('TODO: implement')

def present(path):
    raise NotImplementedError('TODO: implement')

def identity(info):
    raise NotImplementedError('TODO: implement')

def snapshot(path):
    raise NotImplementedError('TODO: implement')

def boot_id():
    raise NotImplementedError('TODO: implement')

@contextmanager
def session_lock():
    raise NotImplementedError('TODO: implement')

def read_session():
    raise NotImplementedError('TODO: implement')

def save_session(session):
    raise NotImplementedError('TODO: implement')

def new_session(current_boot):
    raise NotImplementedError('TODO: implement')

def timer_state():
    raise NotImplementedError('TODO: implement')

def control_timer(action):
    raise NotImplementedError('TODO: implement')

def model_busy(port=18190):
    """Reason string when stopping the model would cut off a live request, else None. Unknown state counts as busy."""
    raise NotImplementedError('TODO: implement')

def stop_model():
    """The guard pins/revalidates the exact workspace/port/birth identity via pidfd. Never cuts off a live request."""
    raise NotImplementedError('TODO: implement')

def on():
    raise NotImplementedError('TODO: implement')

def release_owned_standby(session):
    raise NotImplementedError('TODO: implement')

def off():
    raise NotImplementedError('TODO: implement')

def boot_started_at():
    raise NotImplementedError('TODO: implement')

def reap_stale():
    """Release a game-mode standby left by a session that cannot still be running.

    A game-mode hold written before this boot belongs to a dead session (processes do
    not survive a reboot), and `off` refuses a different-boot or foreign hold, so
    without this it blocks the model forever (2026-11-08: Ethan CLI could not start).
    Touches only a regular file with the exact game-mode token format, older than
    this boot; never STOP, symlinks, operator holds or legacy-format holds.
    Returns True if it released one.
    """
    raise NotImplementedError('TODO: implement')

def gpu_free_mib():
    raise NotImplementedError('TODO: implement')

def status(head=...):
    raise NotImplementedError('TODO: implement')

def game_running():
    """Read-only game detection; never used to select a process for signaling."""
    raise NotImplementedError('TODO: implement')

def watch(poll=20):
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
