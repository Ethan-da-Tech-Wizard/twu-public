# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""twu_scan_event: event-driven scan of files that just arrived. Stdlib only, no daemon, no timer, no network.

  twu_scan_event.py scan-new PATH...   called by an event hook (launchd WatchPaths, systemd .path, Syncthing event)
        with changed paths. Skips our own receipts/rules/.git/Syncthing temp files, skips files still being
        written (size+mtime stable for 2 s), skips files unchanged since their last scan, enforces a size cap,
        scans with twu_scan.  SUSPICIOUS/INFECTED: moves NOTHING; writes data/health/scan_alerts.<host>.json.
  twu_scan_event.py scan-new --dir DIR [--since-days 1]   same, for hooks that give no file list (WatchPaths, .path)
  twu_scan_event.py usb [VOLUME...]    scan newly mounted volumes (default: every mount under /Volumes or
        /media /run/media). Depth-capped, read-only; files beyond the caps are reported, never called clean.
  gguf_header_scan(path)               importable: YARA/ClamAV pass over the first 16 MiB of a model file.

Exit 0 CLEAN, 1 SUSPICIOUS/INFECTED, 2 COULD-NOT-SCAN (same as twu_scan). Receipts: data/health/scans/.
"""
import argparse
import json
import os
import platform
import stat
import sys
import tempfile
import time
from pathlib import Path
import twu_scan

def _stamp(t=None):
    raise NotImplementedError('TODO: implement')

def _worse(a, b):
    raise NotImplementedError('TODO: implement')

def skip_reason(path, root=...):
    raise NotImplementedError('TODO: implement')

def _sig(path):
    raise NotImplementedError('TODO: implement')

def _stable(path, wait, sleeper):
    raise NotImplementedError('TODO: implement')

def _state_path(root):
    raise NotImplementedError('TODO: implement')

def _load(path, default):
    raise NotImplementedError('TODO: implement')

def sentence(path, verdict, findings):
    raise NotImplementedError('TODO: implement')

def write_alerts(root, new_alerts, now=None):
    raise NotImplementedError('TODO: implement')

def load_last_pass(root):
    raise NotImplementedError('TODO: implement')

def save_last_pass(root, ts):
    raise NotImplementedError('TODO: implement')

def expand_dirs(dirs, since_days=1.0, depth=4, max_files=2000, now=None, since_ts=0.0, root=None):
    """launchd WatchPaths / systemd .path give no changed-file list: walk the watched dirs, keep files newer than
    max(now - since_days, since_ts). since_ts is the last successful pass, so each run sees only what changed since."""
    raise NotImplementedError('TODO: implement')

def scan_new(paths, root=..., scanner=None, max_bytes=..., wait=..., sleeper=..., timeout=..., **scan_kw):
    raise NotImplementedError('TODO: implement')

def gguf_header_scan(path, scanner=None, nbytes=..., root=...):
    """YARA/ClamAV over the first nbytes of a model file. A pass is HEADER-ONLY evidence, never a full clearance."""
    raise NotImplementedError('TODO: implement')

def list_volumes(base=None):
    raise NotImplementedError('TODO: implement')

def usb_scan(volumes=None, root=..., scanner=None, depth=..., max_files=..., max_bytes=...):
    raise NotImplementedError('TODO: implement')

def mac_notify(message, title=...):
    """macOS notification; never raises. Returns True if osascript accepted it."""
    raise NotImplementedError('TODO: implement')

def write_download_status(path, watched, res, readable, error, notifier=..., now=None):
    raise NotImplementedError('TODO: implement')

def _default_holder(path):
    raise NotImplementedError('TODO: implement')

def hold_infected(alerts, holder=...):
    """Hold INFECTED files only, one path at a time, with the repo gate's receipt. Failure means alert only."""
    raise NotImplementedError('TODO: implement')

def _render(res, label):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
