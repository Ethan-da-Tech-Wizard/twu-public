# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""/abli: switch the served weights between the vanilla and the abliterated variant of the SAME model family.

  ethan_abli.py status                    one machine-readable line (reads files only)
  ethan_abli.py plan on|off               print exactly what --apply would do; changes nothing
  ethan_abli.py on|off --apply            do it (guarded, bounded, rolls back on failure, always writes a receipt)
  ethan_abli.py init-map --host H         write a skeleton data/config/abli_models.<H>.json (never overwrites)

Scope: weights/LoRA selection only.  Never touches the PolicyEngine, STOP, hooks, claims or tool permissions.
Selection mechanism: ETHAN_CHAT_MODEL / ETHAN_CHAT_LORA (read by magi_autostart.py) are set in the systemd user
manager environment (`systemctl --user set-environment`), mirrored into data/config/abli_env.<host>.env.
Restart: `systemctl --user restart ethan-model.service` (the same call ethan_model_lifecycle makes; it has no
restart subcommand of its own).  Stdlib only.  Tests never call the restart path (hooks are injected).
"""
import argparse
import hashlib
import json
import os
import socket
import subprocess
import sys
import tempfile
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

def host_key(name=None):
    raise NotImplementedError('TODO: implement')

def default_models_root(host=None):
    raise NotImplementedError('TODO: implement')

def platform_search_roots(host=None):
    raise NotImplementedError('TODO: implement')

def now_iso():
    raise NotImplementedError('TODO: implement')

def sha256_file(path, chunk=...):
    raise NotImplementedError('TODO: implement')

def atomic_write_json(path, obj):
    raise NotImplementedError('TODO: implement')

def atomic_write_text(path, text):
    raise NotImplementedError('TODO: implement')

class Ctx:
    """Paths and injectable side effects.  Tests replace the hooks; real runs use the defaults."""

    def __init__(self, repo=..., host=None, models_root=None, port=None):
        raise NotImplementedError('TODO: implement')

    def _thermal(self):
        """None when safe to proceed, else a reason string.  Unknown readings refuse (E17)."""
        raise NotImplementedError('TODO: implement')

    def _set_env(self, model, lora):
        raise NotImplementedError('TODO: implement')

    def _restart(self):
        raise NotImplementedError('TODO: implement')

    def service_status(self):
        """Bounded diagnostic fields only; no environment or service mutation."""
        raise NotImplementedError('TODO: implement')

    def _served(self):
        """Served model path from /props, or None."""
        raise NotImplementedError('TODO: implement')

def load_json(path):
    raise NotImplementedError('TODO: implement')

def resolve_model(ctx, value):
    """Relative values resolve under the models root; absolute values must live under it."""
    raise NotImplementedError('TODO: implement')

def lora_spec(lora):
    """Mirror magi_autostart.parse_lora_spec's path rules: absolute .gguf, no spaces/commas/colons."""
    raise NotImplementedError('TODO: implement')

def load_map(ctx):
    raise NotImplementedError('TODO: implement')

def read_state(ctx):
    raise NotImplementedError('TODO: implement')

def sync_personality_state(repo, target):
    raise NotImplementedError('TODO: implement')

def current_is_abli(ctx):
    raise NotImplementedError('TODO: implement')

def blockers(ctx):
    raise NotImplementedError('TODO: implement')

def build_plan(ctx, target):
    """Returns dict: ok, problems, steps, entry, model, lora, sha."""
    raise NotImplementedError('TODO: implement')

def print_plan(plan):
    raise NotImplementedError('TODO: implement')

def env_text(model, lora):
    raise NotImplementedError('TODO: implement')

def wait_served(ctx, want):
    raise NotImplementedError('TODO: implement')

def write_receipt(ctx, rec):
    raise NotImplementedError('TODO: implement')

def apply(ctx, target, by=...):
    """Returns (exit_code, one-line message).  Always writes a receipt once past the early usage checks."""
    raise NotImplementedError('TODO: implement')

def status_line(ctx):
    raise NotImplementedError('TODO: implement')

def init_map(ctx):
    raise NotImplementedError('TODO: implement')

def main(argv=None, ctx=None):
    raise NotImplementedError('TODO: implement')
