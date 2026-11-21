# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Ethan model variant switch: standard vs abliterated GGUF, per device.

Model-free: makes no model call. Default is read-only (`status`, `plan`).
`switch --execute` (or `standard`/`abli` with --execute) is the only mutating path.
Boot ALWAYS starts standard: this script never reads its state file to decide a boot.
It never creates, removes or approves anything (STOP/MODEL_STANDBY are read-only checks).
Docs: docs/ETHAN_VARIANT.md
"""
import argparse, hashlib, http.client, json, os, socket, subprocess, sys, time
from pathlib import Path

class Refuse(Exception):
    pass

class Paths:

    def __init__(self, repo=..., home=None):
        raise NotImplementedError('TODO: implement')

def http_props(timeout=2.0):
    """GET /props on loopback only. Returns dict or None."""
    raise NotImplementedError('TODO: implement')

def served_model(props):
    raise NotImplementedError('TODO: implement')

def pin_verify(paths, name, base, adapter):
    """Subprocess to scripts/ethan_adapter_pin.py verify; True when exit code is 0."""
    raise NotImplementedError('TODO: implement')

def stop_owned_llama():
    """Stop ONLY the llama-server magi_autostart owns, via its registry + pidfd identity proof
    (magi_autostart.stop_all_daemons mechanism, restricted to id llama_server). Never pkill.
    Returns (ok, detail)."""
    raise NotImplementedError('TODO: implement')

def start_cmd(paths):
    raise NotImplementedError('TODO: implement')

def run_start(cmd, env):
    """Runs the exact autostart command (inherits the TTY). Returns exit code."""
    raise NotImplementedError('TODO: implement')

def read_state(paths):
    raise NotImplementedError('TODO: implement')

def _private_dir(d):
    raise NotImplementedError('TODO: implement')

def write_state(paths, variant):
    raise NotImplementedError('TODO: implement')

def append_log(paths, rec):
    raise NotImplementedError('TODO: implement')

def load_config(paths):
    raise NotImplementedError('TODO: implement')

def entry(cfg, variant):
    raise NotImplementedError('TODO: implement')

def load_pin_file(paths, name):
    raise NotImplementedError('TODO: implement')

def pin_sha(pin):
    raise NotImplementedError('TODO: implement')

def matches(props, gguf):
    raise NotImplementedError('TODO: implement')

def status(paths, props_fn=..., out=...):
    raise NotImplementedError('TODO: implement')

def preflight(paths, variant, cfg, verify_fn=...):
    """Steps 1-3. Raises Refuse with the reason. Read-only."""
    raise NotImplementedError('TODO: implement')

def plan(paths, variant, out=...):
    raise NotImplementedError('TODO: implement')

def switch(paths, variant, execute, *, props_fn=..., verify_fn=..., stop_fn=..., start_fn=..., wait=300.0, interval=2.0, sleep=..., out=..., now=...):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
