# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""ethan_owner_run: the ONE command Ethan runs (Ethan, 2026-11-19: "give me all the commands you need ran and put them into one command").

HOW TO RUN (on any ONE computer, in a terminal):
    cd ~/TWU_LLC && python3 scripts/ethan_owner_run.py            # numbered checklist; every step asks first
    python3 scripts/ethan_owner_run.py --dry-run                   # prints every step, runs NOTHING
    python3 scripts/ethan_owner_run.py --only 2                    # one step
    python3 scripts/ethan_owner_run.py --resume                    # skip steps already finished on this computer

WHAT IT DOES (each step prints what it will do and why, then asks: Type y to run, s to skip, q to quit; Enter = quit):
    1 fleet firewall + reboot checks for THIS computer (reuses scripts/fleet_owner_apply.py: preview, then --apply under sudo)
    2 install the new dashboard release here (scripts/dashboard_deploy.py) and restart the dashboard
    3 SSH-door trust check (scripts/fleet_join.py); prints the `trust` lines to run on the other computers, never runs trust
    4 rule ratification (optional; only when proposals are pending; only Ethan's own typed sentence is used)
    5 final proof: scripts/ethan_master_check.py --quick
    6 HANDOFF SUMMARY: ran / skipped / failed (with undo or retry), what is left per other computer, where the task lists are

SAFETY: there is no "yes to all" flag. sudo runs inherited on your terminal so ITS prompt asks you for the password; this
script never reads, passes or stores a password. Refuses everything when business/example_host/comms/STOP exists.
State: ~/.local/state/twu/owner_run_state.json (mode 600, this computer only). Log: ~/.local/state/twu/owner_run.log (no secrets).
"""
from __future__ import annotations
import datetime
import json
import os
import socket
import subprocess
import sys
import tempfile
from pathlib import Path

class Runner:
    """Runs a command on the real terminal. Terminal I/O is inherited so sudo can ask for the password itself."""

    def run(self, cmd, capture=False):
        raise NotImplementedError('TODO: implement')

class Ctx:

    def __init__(self, root=..., state_dir=None, ask=..., out=..., runner=None, platform=None, hostname=None, today=None):
        raise NotImplementedError('TODO: implement')

    @property
    def state_path(self):
        raise NotImplementedError('TODO: implement')

    @property
    def log_path(self):
        raise NotImplementedError('TODO: implement')

    def script(self, name):
        raise NotImplementedError('TODO: implement')

def load_state(ctx):
    raise NotImplementedError('TODO: implement')

def save_state(ctx, step, status):
    raise NotImplementedError('TODO: implement')

def log(ctx, msg):
    raise NotImplementedError('TODO: implement')

def choose(ctx, prompt=...):
    """Returns 'y', 's' or 'q'. Enter, end of input or too many bad answers = q (default quit)."""
    raise NotImplementedError('TODO: implement')

def cmd_block(out, line):
    """Copy-target printing: the command alone on its own line with a blank line before and after (no label, no indent)."""
    raise NotImplementedError('TODO: implement')

def describe(ctx, n, what, why, cmds):
    raise NotImplementedError('TODO: implement')

def run_cmd(ctx, step, cmd, capture=False):
    raise NotImplementedError('TODO: implement')

def stop_exists(ctx):
    raise NotImplementedError('TODO: implement')

def tail(text, n=15):
    raise NotImplementedError('TODO: implement')

def finish(ctx, step, rc, retry):
    raise NotImplementedError('TODO: implement')

def is_mac(ctx):
    raise NotImplementedError('TODO: implement')

def step1(ctx, dry):
    raise NotImplementedError('TODO: implement')

def restart_cmd(ctx):
    raise NotImplementedError('TODO: implement')

def step2(ctx, dry):
    raise NotImplementedError('TODO: implement')

def other_hosts(ctx):
    raise NotImplementedError('TODO: implement')

def step3(ctx, dry):
    raise NotImplementedError('TODO: implement')

def pending_proposals(ctx):
    raise NotImplementedError('TODO: implement')

def step4(ctx, dry):
    raise NotImplementedError('TODO: implement')

def step5(ctx, dry):
    raise NotImplementedError('TODO: implement')

def load_open_owner_cards(ctx):
    """Read open cards from data/owner_commands/ (text only; never executed)."""
    raise NotImplementedError('TODO: implement')

def print_owner_cards(ctx, header, cards):
    raise NotImplementedError('TODO: implement')

def summary(ctx, dry=False):
    raise NotImplementedError('TODO: implement')

def main(argv=None, ctx=None):
    raise NotImplementedError('TODO: implement')
