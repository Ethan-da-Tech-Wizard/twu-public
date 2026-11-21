# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Listener-side admission gate for the owner-only fleet SSH door (DESIGN, not wired in).

OWNER / LAST CHANGED: Magi 23, 2026-11-19

PURPOSE: decide, on the computer BEING ENTERED, whether an incoming fleet SSH session may run its command. Beginner picture:
    a doorman who checks the request against a short list, and who only lets risky requests through while the owner has
    unlocked THIS computer.
WHO USES IT: the forced command in authorized_keys (once wired in); fleet_control.py installs/pins it. Not wired in yet.
HOW TO RUN: not run by hand. Tests: `cd scripts; ETHAN_HOST=1 python3 -m unittest test_fleet_gate`.
SAFETY RULES: fail closed (STOP file, unreadable state, root user, unknown peer -> deny); never allow a shell outside an
    open owner window; every decision is written to receipts.jsonl; the pinned receiver re-checks everything afterwards.

Intended use: the per-key authorized_keys forced command becomes
  command="exec python3 -I -B <runtime>/gate.py --runtime <rt> --peer <host> -- <receiver argv...>"
so every inbound session passes this gate BEFORE the pinned receiver runs.

Policy, decided on the LISTENING box from its own local state only:
  * SSH_ORIGINAL_COMMAND must be exactly `python3 -B <ws>/scripts/fleet_control.py run <ACTION> --workspace <ws>`
    (optionally `--param X` only for restart_service/collect_logs/rerun_check) with ACTION allow-listed,
    OR the exact owner-shell marker, OR a command_reference/briar_request envelope.
  * Everything except the read-only trio (status, list_units, collect_logs) and the two fixed
    envelopes needs the LOCAL owner window (runtime/state.json 'until' in the future, or 'standing').
  * The window is only set by the owner on THIS box (its authenticated dashboard Unlock, 15 min max).
    A caller cannot open it from the entering box. Model chosen: "Ethan approves on the box being
    entered". Tradeoff: slower (he must be at, or dashboard-reach, that box) but a stolen peer key
    or a compromised peer dashboard cannot approve itself.
  * A shell is never granted outside an open window. Every admit/deny is appended to receipts.jsonl.
"""
from __future__ import annotations
import json
import os
import shlex
import sys
import time
from pathlib import Path

def window_open(state: dict, now: float | None=None) -> bool:
    """True if the LOCAL owner has unlocked this computer.

    Args: state = parsed runtime/state.json; now = test clock. Open when the policy is 'standing' or 'until' is in the
    future. Why safe: bad or missing values return False (closed), never an exception.
    """
    raise NotImplementedError('TODO: implement')

def decide(original: str, workspace: str, state: dict, stopped: bool=False, now: float | None=None):
    """Return (allowed, kind, reason). kind is the action name, 'terminal' or ''.

    Pure function (no I/O) so it is easy to test. Args: original = the SSH_ORIGINAL_COMMAND text, workspace = this
    computer's TWU folder, state = owner-window state, stopped = STOP file present. reason is one of 'stopped', 'window',
    'locked', 'read', 'invalid_request'.
    Why safe: the command must match the exact token layout below; anything extra (other flags, other scripts) is denied,
    so a stolen peer key cannot smuggle arbitrary shell text.
    """
    raise NotImplementedError('TODO: implement')

def _log(runtime: Path, peer: str, kind: str, allowed: bool, reason: str) -> None:
    """Append one admit/deny receipt line. O_NOFOLLOW refuses a symlinked log; mode 0600 keeps it private. Raises OSError."""
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    """Gate entry point: validate, decide, log, then exec the pinned receiver or print an error and return 1.

    Args: argv = `--runtime RT --peer HOST -- RECEIVER_ARGV...`. Returns 1 on any refusal; on admit it replaces this
    process with the receiver and never returns.
    """
    raise NotImplementedError('TODO: implement')
