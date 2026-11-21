# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Lint for owner-command steps.

OWNER / LAST CHANGED: Magi 23, 2026-11-19

WHAT IT IS (beginner picture): a command card has a Copy button. Whatever is behind that button is pasted into Ethan's
    terminal, so it must be exactly one command and nothing else. This file checks a line and says, in plain words,
    why it is not safe to put behind Copy.
WHO USES IT: scripts/dashboard_panels/owner_commands.py (post time and render time), scripts/owner_command.py (CLI).
HOW TO RUN: python3 scripts/owner_command_lint.py 'cd ~/TWU_LLC && python3 scripts/fleet_join.py'   (prints problems, exit 1 if any)
    Test: cd scripts; ETHAN_HOST=1 python3 -m unittest test_owner_command_lint
DATA FLOW: text in -> list of plain-English problems out ([] means clean). Nothing is stored.
SAFETY: the text is NEVER executed. The only process started is `bash -n -c TEXT` (fixed argv, no shell): the -n flag
    makes bash read and syntax-check the line without running any part of it.
RULES (a command step must pass all): one line, <= 240 chars, bash -n and shlex parse, no # comment, no <PLACEHOLDER> or
    HOST_FP style token, ASCII only, no prompt ($ > %) or label ('(on the example_host)', 'Step 1:'), at most two &&,
    sudo not mixed with a non-sudo command (a leading cd is fine), not prose (first word looks like a program or path,
    fewer than 2 bare stopwords).
"""
from __future__ import annotations
import re
import shlex
import subprocess
import sys

def _scan(text):
    """(unquoted text with each quoted piece replaced by Q, list of quoted pieces, has_comment, balanced)."""
    raise NotImplementedError('TODO: implement')

def _tokens(unq):
    """Bare words of the unquoted text."""
    raise NotImplementedError('TODO: implement')

def _program_known(word) -> bool:
    """True when the word is a program here (PATH or builtin lookup) or a well-known command on another OS."""
    raise NotImplementedError('TODO: implement')

def _looks_prose(text) -> bool:
    """True when the line reads like English rather than a command.

    2026-11-20 Magi 10 (MAGI_TODO d05abbd1): also true for a lower-case sentence such as 'please run the update now' or 'restart the server
    after you finish': three or more bare lower-case words whose first word is not a program (the old test needed two stop-words from a short
    list, so these passed and got a Copy button). A real command has a flag, a path, a digit or a program first word, and passes."""
    raise NotImplementedError('TODO: implement')

def classify_line(text) -> str:
    """'comment' (blank or starts with #), 'gui' (reads like prose, label or prompt) or 'command' (command-shaped)."""
    raise NotImplementedError('TODO: implement')

def lint_command(text) -> list:
    """Plain reasons the text may not sit behind a Copy button; [] means it is one clean command.

    Memoised by exact text (a fresh list is returned every call, so callers may mutate it). Undo: call _lint_command_uncached directly."""
    raise NotImplementedError('TODO: implement')

def _lint_command_uncached(text) -> list:
    """The real lint (see lint_command)."""
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    """CLI: lint each argument as one command step."""
    raise NotImplementedError('TODO: implement')
