# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""twu_pty_reset: non-destructive reset of a frozen tty you own (NEED-002).

Resumes stopped output (the Ctrl-S freeze), flushes nothing, restores sane
line-discipline flags (echo, canonical, ICRNL, OPOST, ISIG) and optionally
writes a soft terminal reset sequence. Never touches foreign-owned ttys,
never kills processes, never clears scrollback.
"""
from __future__ import annotations
import argparse
import os
import stat
import sys
import termios

def check_tty(path: str) -> None:
    raise NotImplementedError('TODO: implement')

def reset(path: str, sequence: bool=True) -> dict:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
