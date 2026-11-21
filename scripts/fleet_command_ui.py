# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""
================================================================================
MODULE:        fleet_command_ui
ROLE:          'Run a command on another computer' box: HTML section + the ONE guarded entry function
================================================================================

PURPOSE:
    Lets Ethan type one plain command, pick another registered computer, confirm, and see the result, from the
    dashboard Fleet and Sync popup, the panel door, or `ethan fleet term run-cmd HOST -- COMMAND...`.
    It adds NO execution path. Every run goes through the EXISTING dashboard fleet door:
    fleet_control.FleetAPI.handle({'action': 'execute', ...}) -> Fleet.literal_command_argv (strict parser, no shell)
    -> Fleet.execute (pinned SSH, receiver forced command, owner window checked on BOTH computers).

ARCHITECTURE & SYSTEM ROLE:
    - Upstream callers: dashboard_command_center._fleet_sync_inner (calls _fleet_command_section), dashboard_panels/
      fleet_command.py (panel action 'command-run'), fleet_term.cmd_run_cmd (CLI).
    - Downstream: fleet_registry (who exists), fleet_control (parse + execute + receipts), dashboard_actions.scrub.

DATA FLOW & LIFECYCLE:
    host + command text -> validate here (type, length, control characters, registry membership, not this computer,
    STOP) -> FleetAPI.handle passes the TEXT as data -> literal argv list -> Fleet.execute sends argv as JSON on the
    SSH stdin (never a shell string) -> reply (rc, stdout, stderr) -> scrub + cap here -> dict for the caller.

KEY INVARIANTS:
    - The command text is never joined into a shell string or an argv built in this file.
    - Confirmation is the caller's job (panel door confirm=True / CLI prompt); this module re-checks nothing about the
      owner window itself, the fleet layer does (caller window and the receiving computer's own window).
    - Output shown to people is scrubbed (dashboard_actions.scrub) and capped; receipts never hold the command.

SECURITY & BOUNDARIES:
    STOP refuses. Unknown host refuses (re-read from the registry on every call). Control characters (newline, tab,
    escape, NUL...) refuse. Length cap 1000 characters (the fleet layer's own cap is 8192). Shell notation (pipes,
    redirects, $, *, ;, assignments) is rejected by the fleet parser with code shell_required.

SYNOPSIS / USAGE:
    import fleet_command_ui as ui
    result = ui.run_command(root, 'example_host', 'uptime')      # {'ok', 'code', 'message', 'rc', 'stdout', 'stderr', ...}
    html = ui._fleet_command_section(root)                  # the dashboard section
================================================================================
"""
from __future__ import annotations
import ast
import html
import json
import os
import time
import unicodedata
from pathlib import Path
import sys

def _esc(value) -> str:
    """HTML-escape anything (quotes included) so typed or returned text can never become markup."""
    raise NotImplementedError('TODO: implement')

def _scrub(text) -> str:
    """Hide secret-shaped tokens and addresses with the dashboard's own scrubber; never raises."""
    raise NotImplementedError('TODO: implement')

def _api(root):
    """The existing dashboard fleet door for this workspace (tests replace this; no state is read here)."""
    raise NotImplementedError('TODO: implement')

def _fail(code, message, host=...):
    """One uniform refusal dict. `ok` False, rc None, no output."""
    raise NotImplementedError('TODO: implement')

def validate(root, host, command):
    """Return a refusal dict, or None when host and command pass every check made in this file.

    Order: types, length, control characters, registry membership, STOP. Pure reads, nothing is executed.
    """
    raise NotImplementedError('TODO: implement')

def run_command(root, host, command, api=None):
    """Run ONE literal command on ANOTHER registered computer through the existing fleet door.

    Args: root (workspace folder); host (registered name); command (str, typed text, passed as data);
          api (tests only: object with .handle(payload, owner) and .fleet.host).
    Returns: dict {ok, code, message, host, rc, stdout, stderr, truncated, timed_out}; stdout/stderr scrubbed and capped.
    Side effects: the fleet layer does the SSH and writes its receipt (no command text, no output). Confirmation must
    already have happened in the caller. Never raises for ordinary failures.
    """
    raise NotImplementedError('TODO: implement')

def _log_command(runtime, host, command, rc, code):
    """Append ONE line to this computer's private command log: when, where, what (scrubbed, capped), how it ended.

    Why: fleet receipts deliberately hold no command text, so on their own they cannot answer 'what did I run on
    example_host?'. This log is the owner's own record. It lives in the private fleet runtime folder (outside the synced
    workspace, mode 600), the text goes through dashboard_actions.scrub first, and a failure to write is silent:
    logging must never block or change a command. `runtime` None (tests with a mocked API) or a missing folder -> skipped.
    """
    raise NotImplementedError('TODO: implement')

def recent_commands(runtime=None, n=...):
    """The last `n` entries of this computer's private command log, newest first. Missing/damaged file -> []."""
    raise NotImplementedError('TODO: implement')

def last_runs(runtime=None, n=...):
    """The last `n` finished 'execute' receipts, newest first: [{when, host, status, code, rc}].

    Receipts hold only status/code/rc/flags, never the command or output, so nothing secret can appear here.
    `runtime` is the fleet private folder (default ~/.local/share/twu/fleet-access). Missing file -> [].
    """
    raise NotImplementedError('TODO: implement')

def _window_line(root):
    """(state, plain sentence) for THIS computer's owner window. The other computer's window is only known when it answers."""
    raise NotImplementedError('TODO: implement')

def _fleet_command_section(root):
    """HTML for the 'Run a command on another computer' box (inserted into the Fleet and Sync popup).

    The Run button carries data-panel='fleet_command' data-panel-action='command-run' so it passes the dashboard's
    door rules; fleet_command_ui.JS (served in /static/command_center.js) intercepts its click, shows the confirm
    dialog with the computer name and exact command, and posts target+command as payload fields.
    """
    raise NotImplementedError('TODO: implement')
