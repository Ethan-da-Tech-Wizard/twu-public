# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""operator_tasks: the HUMAN operator (via the dashboard) sends a task to a Magi seat as operator@<host>.

Not a seat: no join, no connection token, never listed by `magi.py who`, cannot hold files. Events go to
business/example_host/comms/operator/tasks.jsonl (append-only, regular file, mode 0600, size-capped) and are merged into a seat's
inbox by the inbox read path (magi.py _inbox). The event carries no from_connection/to_connection, so session_mail treats it by
timestamp only. This is NOT the seat event schema (private/example_host/event_outbox.py allows only agent1..agent16), so it never
enters a seat outbox. Stdlib only, offline.
"""
from __future__ import annotations
import hashlib
import json
import os
import re
import secrets
import socket
import stat
import time
from pathlib import Path

class OperatorTaskError(ValueError):
    """Refused: nothing was written."""

def _host():
    raise NotImplementedError('TODO: implement')

def _clean(text):
    raise NotImplementedError('TODO: implement')

def send_task(root, to_seat, text, page_session_id=..., host=None, now=None):
    """Append one operator task for seat `to_seat` (1-32). Returns the event. Raises OperatorTaskError."""
    raise NotImplementedError('TODO: implement')

def events(root):
    """Every well-formed operator task. Malformed lines, wrong targets and symlinked/non-regular files are skipped, never raised."""
    raise NotImplementedError('TODO: implement')

def for_seat(root, seat):
    raise NotImplementedError('TODO: implement')

def read_task_file(path):
    """Parse the operator's task file: first line `TO: <seat>`, the rest is the text. Returns (seat, text). Raises OperatorTaskError."""
    raise NotImplementedError('TODO: implement')
