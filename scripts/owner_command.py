# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""owner_command: how a Magi hands Ethan a command to run. It shows on his dashboard ("Commands for Ethan").

OWNER / LAST CHANGED: Magi 23, 2026-11-19

WHAT IT IS (beginner picture): a command Ethan must run must not live only in chat. Post it here with a label, where
    to run it, whether it needs sudo, why, how to undo it and how to check it worked. This tool only STORES text
    (data/owner_commands/<this computer>.jsonl); nothing is ever run.
HOW TO RUN (see docs/OWNER_COMMANDS.md). START HERE: run it with no arguments for the 30 second guide.
    python3 scripts/owner_command.py add 'Restart the dashboard' --on example_host,example_host --run 'systemctl --user restart twu-dashboard.service'
        (--on one name, a comma list, all or any; add --note/--check/--why/--undo/--verify/--sudo/--dry-run as needed)
    The older, fuller form is still supported:
    python3 scripts/owner_command.py post --seat N --label '...' --where example_host [--sudo] --why '...' [--undo '...']         [--notes '...'] [--sequence] [--task ID] --step 'gui:Open the app ...' --step 'command:cd ~/TWU_LLC && python3 scripts/x.py'         --step 'check:python3 scripts/x.py --check'        (ordered; a bad command step REFUSES the post, exit 1)
    ... -- 'cmd1' 'cmd2'                                   (each positional is a command step and is linted too)
    python3 scripts/owner_command.py revise ID --step ... [--notes ...] [--where ...]   (appends a revision event; old lines untouched)
    python3 scripts/owner_command.py lint-all [--original]  (read-only: lints every card in data/owner_commands/*.jsonl)
    python3 scripts/owner_command.py migrate-v2             (one-time clean step split of the old prose cards; safe to repeat)
    python3 scripts/owner_command.py list [--open]      python3 scripts/owner_command.py show ID
    python3 scripts/owner_command.py done ID --by NAME --note '...'      python3 scripts/owner_command.py withdraw ID
    python3 scripts/owner_command.py seed               (posts today's known pending items once; safe to repeat)
Storage, checks and state rules live in scripts/dashboard_panels/owner_commands.py. Secrets and STOP are refused.
"""
from __future__ import annotations
import argparse
import os
import sys
from pathlib import Path
from dashboard_panels import owner_commands as oc

def C(text):
    """A command step."""
    raise NotImplementedError('TODO: implement')

def G(text):
    """A GUI (tick-box) step."""
    raise NotImplementedError('TODO: implement')

def K(text, expect=...):
    """A read-only check step."""
    raise NotImplementedError('TODO: implement')

def _trust_steps(other):
    """Steps for one computer's trust card: the command, then the fingerprint comparison, then the status check."""
    raise NotImplementedError('TODO: implement')

def _fw(host, label, sudo, note):
    """Seed for the fleet firewall and reboot checks on one computer."""
    raise NotImplementedError('TODO: implement')

def migrate_v2(root=None, host=None, now=None) -> list:
    """Append a revision (clean steps; original text kept in notes) for each old card in _REVISE that is still v1, and post
    the extra per-computer trust card. Safe to repeat. Returns [(id, message)]."""
    raise NotImplementedError('TODO: implement')

def quickstart(root=None) -> str:
    """The 30 second guide as plain text (12 lines plus the examples)."""
    raise NotImplementedError('TODO: implement')

class _Parser(argparse.ArgumentParser):
    """ArgumentParser whose errors end with a corrective example (exit code 1, not 2)."""

    def error(self, message):
        raise NotImplementedError('TODO: implement')

def _cmd_quickstart(a) -> int:
    """quickstart subcommand (also what no arguments prints)."""
    raise NotImplementedError('TODO: implement')

def _preview(a, cards) -> str:
    """Dry-run preview: one block per card (computer, label, numbered steps by kind, sudo badge, group note). Commands verbatim."""
    raise NotImplementedError('TODO: implement')

def _cmd_add(a) -> int:
    """add subcommand: one card per computer named by --on."""
    raise NotImplementedError('TODO: implement')

def _parse_steps(raw, positional):
    """Turn --step 'kind:text [ //expect// text]' strings and positional commands into step dicts. Raises ValueError."""
    raise NotImplementedError('TODO: implement')

def sudo_mix_problem(steps):
    """Plain reason a card must be split, or "" when its COMMAND steps are all sudo or all non-sudo.

    2026-11-20 Magi 10 (MAGI_TODO d05abbd1): owner_command_lint refuses sudo mixed with non-sudo inside ONE line, but `post` accepted a card whose
    steps were `sudo ...` in one step and a plain command in the next, so the card's "needs sudo" badge was wrong for half of it. A leading `cd ...`
    segment does not count, and check/gui steps are read-only text, so only kind=command steps are compared."""
    raise NotImplementedError('TODO: implement')

def _cmd_post(a) -> int:
    """post subcommand."""
    raise NotImplementedError('TODO: implement')

def _cmd_revise(a) -> int:
    """revise subcommand."""
    raise NotImplementedError('TODO: implement')

def _cmd_lint_all(a) -> int:
    """lint-all subcommand: read-only per-card problems for every card in every file."""
    raise NotImplementedError('TODO: implement')

def _cmd_migrate(a) -> int:
    """migrate-v2 subcommand."""
    raise NotImplementedError('TODO: implement')

def _cmd_list(a) -> int:
    """list subcommand."""
    raise NotImplementedError('TODO: implement')

def _cmd_show(a) -> int:
    """show subcommand."""
    raise NotImplementedError('TODO: implement')

def _cmd_done(a) -> int:
    """done subcommand."""
    raise NotImplementedError('TODO: implement')

def _cmd_withdraw(a) -> int:
    """withdraw subcommand."""
    raise NotImplementedError('TODO: implement')

def seed(root=None, host=None) -> list:
    """Post every SEEDS item once (stable ids make repeats no-ops). Returns the results."""
    raise NotImplementedError('TODO: implement')

def _cmd_seed(a) -> int:
    """seed subcommand."""
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    """CLI entry."""
    raise NotImplementedError('TODO: implement')
