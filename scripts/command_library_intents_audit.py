# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""
PROGRAM:       command_library_intents_audit.py
PROGRAMMER:    Magi 10 (claude, example_host)
LAST MODIFIED: 2026-11-20
PURPOSE:       Audit data/commands/intents.json: for every intent, show the commands per OS and flag any that is not a
               real command for that OS (per command_library_query.known_commands) or is on a power-command denylist for an
               intent that is not about power. Read-only except the optional report file.
USAGE:         python3 scripts/command_library_intents_audit.py [--write]      (--write saves data/commands/intents_audit.md)
CHANGE HISTORY
  2026-11-20  Magi 10  Created after 'kill a process using a port' listed shutdown/reboot/pmset/halt for macOS.
"""
import json
import sys
from pathlib import Path
import command_library_query as q

def audit(root=...):
    """Return (rows, problems). rows: one dict per intent. problems: list of strings (explicit per-OS entries only are errors;
    general-list names missing on an OS are informational because the equivalents code filters them)."""
    raise NotImplementedError('TODO: implement')

def render(rows, problems):
    raise NotImplementedError('TODO: implement')

def main(argv):
    raise NotImplementedError('TODO: implement')
