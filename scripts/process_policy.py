# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""process_policy: deterministic process watcher with a human-editable policy and a safe responder.

Policy: data/policy/process_policy.toml (plain, commented). Emergency stop: data/policy/PAUSE.
Decisions are appended to data/netguard/process_policy.<host>.jsonl; latest receipt in
data/netguard/process_policy.LATEST.<host>.json (read by scripts/ethan_alarm.py).

Commands (no AI needed): status | check | dry-run | report | explain PID | explain-last
                         allow NAME | deny NAME | pause | resume | mode observe|enforce | learn
No model, no network. The only action it can take is SIGTERM then SIGKILL of one of the user's own processes
by PID, after re-verifying the PID's start time and exe, never on a protected process, rate limited.
The process lister and the killer are injected so tests never touch a real PID.
"""
from __future__ import annotations
import fnmatch
import json
import os
import re
import signal
import socket
import subprocess
import sys
import time
from pathlib import Path

def _strip_comment(line):
    raise NotImplementedError('TODO: implement')

def parse_toml_subset(text):
    """Minimal TOML reader for process_policy.toml: key = string/int/bool/array (JSON-like, multi-line ok),
    [table] and [[array-of-tables]] headers. Raises ValueError on anything else; never guesses."""
    raise NotImplementedError('TODO: implement')

def _toml_value(val):
    raise NotImplementedError('TODO: implement')

def read_toml(fh_bytes, use_stdlib=True):
    raise NotImplementedError('TODO: implement')

class Paths:

    def __init__(self, policy_dir=None, data_dir=None, host=None):
        raise NotImplementedError('TODO: implement')

def list_processes():
    """Linux /proc lister. Returns dicts: pid, ppid, sid, uid, name, exe, deleted, cmdline, start."""
    raise NotImplementedError('TODO: implement')

def _read_proc(pid):
    raise NotImplementedError('TODO: implement')

def list_listeners(runner=None):
    """{pid: [ports]} for every listening socket ss can attribute. Best effort; {} if ss is unavailable."""
    raise NotImplementedError('TODO: implement')

def real_kill(pid, sig):
    """The only place a signal is sent. A single positive pid; never a group."""
    raise NotImplementedError('TODO: implement')

def expand(s):
    raise NotImplementedError('TODO: implement')

def load_policy(paths):
    raise NotImplementedError('TODO: implement')

def _name_match(pattern, name):
    raise NotImplementedError('TODO: implement')

def _exe_match(patterns, exe):
    raise NotImplementedError('TODO: implement')

def _in_dirs(exe, dirs):
    raise NotImplementedError('TODO: implement')

def _base(p):
    raise NotImplementedError('TODO: implement')

class Context:

    def __init__(self, procs, listeners, self_pid):
        raise NotImplementedError('TODO: implement')

def classify(p, pol, ctx):
    """Return (verdict, rule, why). verdict: skip | protected | deny | allow | review."""
    raise NotImplementedError('TODO: implement')

def _load_json(path, default):
    raise NotImplementedError('TODO: implement')

def _write_json(path, obj):
    raise NotImplementedError('TODO: implement')

def log_decision(paths, rec):
    raise NotImplementedError('TODO: implement')

def read_log(paths):
    raise NotImplementedError('TODO: implement')

def check(paths=None, lister=None, listeners=None, killer=None, sleeper=None, now=None, self_pid=None, force_mode=None, dry=False):
    """One pass. Returns the receipt dict. Never kills unless mode is enforce, not paused, not dry."""
    raise NotImplementedError('TODO: implement')

def stop_process(p, pol, ctx, procs_after, killer, sleeper, classify_fn):
    """SIGTERM, wait, SIGKILL one verified process. Returns an action string."""
    raise NotImplementedError('TODO: implement')

def alarm_problems(now=None, paths=None, os_name=None):
    """For ethan_alarm: deny hits and the review count from the latest receipt. Silent before the first run.
    Off Linux nothing is measured (no /proc), so say so instead of reporting clean."""
    raise NotImplementedError('TODO: implement')

def say_receipt(r, out):
    raise NotImplementedError('TODO: implement')

def explain(paths, pid, lister=None, listeners=None, self_pid=None, out=...):
    raise NotImplementedError('TODO: implement')

def explain_last(paths, out=...):
    raise NotImplementedError('TODO: implement')

def append_entry(paths, kind, name, exe=None, extra=...):
    raise NotImplementedError('TODO: implement')

def set_mode(paths, mode):
    raise NotImplementedError('TODO: implement')

def report(paths, since_hours=24, now=None, out=...):
    raise NotImplementedError('TODO: implement')

def main(argv=None, out=..., paths=None):
    raise NotImplementedError('TODO: implement')
