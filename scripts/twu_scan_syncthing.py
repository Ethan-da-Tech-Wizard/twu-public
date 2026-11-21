# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""twu_scan_syncthing: scan every file Syncthing RECEIVES from another device. Python 3.9 stdlib, loopback only.

Long-polls Syncthing's own event feed (GET /rest/events?events=ItemFinished,RemoteChangeDetected, timeout=60):
the wait happens inside Syncthing, so there is no timer and no CPU use while idle. ItemFinished is emitted by the
puller, i.e. only for changes that arrived from a remote device; local edits never produce it. Only files with
action update/metadata and no error are scanned; deletes and directories are ignored. RemoteChangeDetected only
announces a change that has not arrived yet, so it is not acted on. Events are batched for 3 s, then handed to
twu_scan_event.scan_new (no scanning logic here). Nothing is ever moved or deleted: flagged files only produce
alerts via scan_event's alert file. The last event id is kept in ~/.local/state/twu/syncthing-scan.state, the log
in ~/.local/state/twu/syncthing-scan.log. The API key is read like sync_health_monitor does and is never printed.

  twu_scan_syncthing.py [--once-seconds N]     run in the foreground (a service unit runs exactly this)
"""
import argparse
import json
import os
import signal
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
import twu_scan_event
import sync_health_monitor

class Terminated(Exception):
    pass

def stamp():
    raise NotImplementedError('TODO: implement')

def skip_item(rel):
    """Reason to skip a folder-relative path, or None. *.sync-conflict-* files are deliberately NOT skipped."""
    raise NotImplementedError('TODO: implement')

def event_target(ev, folders):
    """Absolute path to scan for one event, or (None, reason)."""
    raise NotImplementedError('TODO: implement')

class Listener:

    def __init__(self, key, base=..., state_dir=..., scan=None, root=..., sleep=..., poll_seconds=..., batch_seconds=...):
        raise NotImplementedError('TODO: implement')

    def log(self, msg):
        raise NotImplementedError('TODO: implement')

    def load_since(self):
        raise NotImplementedError('TODO: implement')

    def save_since(self):
        raise NotImplementedError('TODO: implement')

    def get(self, path, timeout):
        raise NotImplementedError('TODO: implement')

    def refresh_folders(self):
        raise NotImplementedError('TODO: implement')

    def poll(self, timeout):
        raise NotImplementedError('TODO: implement')

    def sync_ids(self):
        """Syncthing restarts reset event ids; if our saved id is ahead of the newest event, start over."""
        raise NotImplementedError('TODO: implement')

    def flush(self, paths):
        raise NotImplementedError('TODO: implement')

    def take(self, events, pending):
        raise NotImplementedError('TODO: implement')

    def run(self, max_seconds=None):
        raise NotImplementedError('TODO: implement')

def install_sigterm(listener):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
