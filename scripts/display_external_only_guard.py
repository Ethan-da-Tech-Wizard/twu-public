# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Keep the laptop panel off while external-only mode is on, and log what turned it on.

Listens to Hyprland's event socket. EVERY monitor event is logged with a timestamp, the monitor state,
the external-only marker and any display-related processes started in the last few seconds, to
data/example_host/display_events/YYYY-MM.jsonl (one file per month; finished months are gzipped, never deleted,
so the history rolls on forever). If the laptop panel (eDP/LVDS/DSI) appears while the external-only marker
exists and an external screen is live, it also disables the panel again. It never touches anything when the
marker is absent, never reloads the config, and never acts if no external screen is live (so you cannot be
left with a black screen). Read the log with scripts/display_events.py.

Run: python3 scripts/display_external_only_guard.py [--once-check]
"""
import argparse
import gzip
import json
import os
import socket
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

def is_internal(name):
    raise NotImplementedError('TODO: implement')

def decide(monitors, marker_present):
    """Return the name of the laptop panel to disable, or None. Pure, so it can be tested."""
    raise NotImplementedError('TODO: implement')

def hypr_env():
    """hyprctl needs the instance signature; a service does not inherit it, so take it from the live socket."""
    raise NotImplementedError('TODO: implement')

def hypr_monitors():
    raise NotImplementedError('TODO: implement')

def log_path(now=None):
    raise NotImplementedError('TODO: implement')

def roll_old_months(now=None):
    """Gzip every finished month's log. Nothing is deleted, so the history is permanent."""
    raise NotImplementedError('TODO: implement')

def recent_actors(seconds=10):
    """Display-related processes that started in the last few seconds (the likely cause)."""
    raise NotImplementedError('TODO: implement')

def log(row):
    raise NotImplementedError('TODO: implement')

def summarize(monitors):
    raise NotImplementedError('TODO: implement')

def check_and_fix(trigger):
    """Log the event with the monitor state, then fix the laptop panel if external-only was broken."""
    raise NotImplementedError('TODO: implement')

def socket_path():
    """The live Hyprland instance's event socket (a service has no HYPRLAND_INSTANCE_SIGNATURE, so fall back to the newest)."""
    raise NotImplementedError('TODO: implement')

def listen():
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
