# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""ONE terminal command for the whole fleet (2026-11-19). A thin wrapper: it adds no auth path and no free-text remote commands.

Read-only table of every registered computer:
python3 scripts/fleet_term.py status

Interactive shell (replace HOST with a computer name from the status table):
python3 scripts/fleet_term.py shell HOST

A fixed read/check action via fleet_do (ACTION is one of status list_units collect_logs readiness sync_status):
python3 scripts/fleet_term.py run HOST ACTION

One literal command, no shell, owner window open on both computers (replace HOST and COMMAND):
python3 scripts/fleet_term.py run-cmd HOST --yes -- COMMAND

One tmux session 'fleet': a window per computer plus a live status window:
python3 scripts/fleet_term.py tmux

Reuses fleet_registry (who exists), fleet_view (who measured what), fleet_do/Fleet (actions), Fleet.ssh (pinned ssh, STOP check).
mosh is used only if installed; the owner window (unlock) and the real-TTY rule are enforced here and by the receiving computer.
"""
from __future__ import annotations
import os
import shlex
import shutil
import sys
import time
from pathlib import Path
import fleet_registry
import fleet_view
from fleet_control import Fleet, FleetError

def _age(sec):
    raise NotImplementedError('TODO: implement')

def status_rows(root=None, now=None, fleet=None):
    """Read-only. Every cell is 'unknown'/'?' unless something measured it."""
    raise NotImplementedError('TODO: implement')

def cmd_status(root=None):
    raise NotImplementedError('TODO: implement')

def _transport(command, offer, addr_user):
    """plain ssh, or mosh only when installed. Returns (argv, note)."""
    raise NotImplementedError('TODO: implement')

def shell_argv(host, root=None, fleet=None, tty=None):
    """Return (argv, note) or raise FleetError with a plain message. Never executes anything."""
    raise NotImplementedError('TODO: implement')

def cmd_shell(host, root=None):
    raise NotImplementedError('TODO: implement')

def cmd_run(host, action, root=None):
    raise NotImplementedError('TODO: implement')

def cmd_run_cmd(host, words, root=None, yes=False, api=None):
    """`run-cmd HOST -- COMMAND...`: one literal command on ANOTHER computer through the same guarded function the dashboard box uses.

    `words` is the argv your local shell already split; shlex.join re-quotes it so the strict parser sees the same words
    (a pipe typed unquoted was handled by YOUR shell before we got here; nothing remote ever runs a shell).
    Confirmation: type yes at the prompt (needs a real terminal), or pass --yes. Exit code = remote code on success, else 1.
    """
    raise NotImplementedError('TODO: implement')

def tmux_commands(root=None, session=...):
    """The tmux argv lists, in order. One window per registered computer + one 'status' window."""
    raise NotImplementedError('TODO: implement')

def cmd_tmux(root=None, execute=True):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
