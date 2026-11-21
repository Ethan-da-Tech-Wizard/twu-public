# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""The one shared STOP latch every long-running TWU worker uses.

`business/example_host/comms/STOP` stops work except safe shutdown and receipts (AGENTS.md).
A worker calls ``stop_latch.enforce("<name>")`` once at its entrypoint:

* if STOP is present it refuses to start (exit 0, one stderr line), and
* otherwise a daemon thread checks the file every few seconds (a single ``stat``; near-zero
  CPU) and, when STOP appears, sends the process SIGTERM so its normal shutdown handlers run,
  then hard-exits after a grace period if the process is still alive.

``refuse_if_stopped`` is the entry check alone, for one-shot commands. Nothing here starts a
process, model, service or network request. ``stop_coverage_auditor.py`` recognises these calls.
"""
from __future__ import annotations
import os
import signal
import sys
import threading
import time
from pathlib import Path

def stop_present(path: Path | None=None) -> bool:
    """True when the fleet-wide incident latch exists."""
    raise NotImplementedError('TODO: implement')

def refuse_if_stopped(name: str, path: Path | None=None) -> None:
    """Exit cleanly before doing any work when STOP is present."""
    raise NotImplementedError('TODO: implement')

def _default_on_stop(name: str, grace: float) -> None:
    raise NotImplementedError('TODO: implement')

def watch(name: str, interval: float=..., path: Path | None=None, on_stop=None, grace: float | None=None) -> threading.Thread:
    """Start (once per name) a daemon thread that reacts when STOP appears."""
    raise NotImplementedError('TODO: implement')

def enforce(name: str, interval: float=..., path: Path | None=None) -> threading.Thread:
    """Entry check plus a running watch: the standard call for any daemon or server."""
    raise NotImplementedError('TODO: implement')
