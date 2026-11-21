# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Watch one exact local process/connection binding without extending its life.

Linux pidfds wake promptly on process exit. Bounded two-second checks also let
released or replaced connections stop their obsolete watchers while a shared
application process remains alive. Unknown ownership never authorizes release.
"""
from __future__ import annotations
import argparse
import os
import re
import select
import sys
import time
from pathlib import Path
import scripts.magi as magi
import scripts.stop_latch as stop_latch

def _binding(seat, pid, start, connection_id):
    """A read-only snapshot: current, obsolete, or unknown; never repair state."""
    raise NotImplementedError('TODO: implement')

def _unknown():
    raise NotImplementedError('TODO: implement')

def _close_pidfd(fd):
    raise NotImplementedError('TODO: implement')

def watch_process(seat: int, pid: int, start: int, connection_id: str) -> int:
    """Release only a proven exited owner; stop when this binding stops existing."""
    raise NotImplementedError('TODO: implement')

def main(argv: list[str] | None=None) -> int:
    raise NotImplementedError('TODO: implement')
