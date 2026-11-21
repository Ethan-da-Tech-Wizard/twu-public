# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""owner_card_reconcile: per-host, read-only evaluation of opt-in cards.

RULES: only OPEN cards whose `where` is THIS computer and that carry `done_check` are evaluated (other computers close
their own cards when their own sweep runs; `any` cards are never auto-closed). The check runs as an argv list of
[python, scripts/owner_check.py, NAME, ARG?], never through a shell, never with sudo, and NAME must be in owner_check.CHECKS.
Closing appends a `done` event (by 'auto-reconcile', note 'auto-closed: check passed') to this computer's own file;
no history is edited or deleted. A failing, unknown or erroring check leaves the card open.
HOW TO RUN: python3 scripts/owner_card_reconcile.py [--dry-run]     Called from stale_sweep.sweep().
"""
from __future__ import annotations
import re
import subprocess
import sys
import time
from pathlib import Path
from dashboard_panels import owner_commands as oc
import owner_check

def run_check(spec, runner=None):
    """True only when the named check exits 0. spec is 'name' or 'name arg'; anything malformed is False."""
    raise NotImplementedError('TODO: implement')

def reconcile(root=None, host=None, dry_run=False, runner=None, now=None):
    """Close this computer's passing cards. Returns (closed_ids, skipped) where skipped lists (id, reason)."""
    raise NotImplementedError('TODO: implement')

def _norm_label(label):
    raise NotImplementedError('TODO: implement')

def _read_only(it):
    """True only for a card that is safe to drop unattended: no sudo, no done_check, at least one step, ALL steps 'check'
    kind (no command, gui or bad step)."""
    raise NotImplementedError('TODO: implement')

def sweep_stale(root=None, host=None, dry_run=False, now=None, ttl=...):
    """Deterministic, model-free pass over THIS computer's open cards. Returns [(id, 'expired'|'superseded')].
    TTL: read-only check-only cards older than ttl are withdrawn (tombstone note EXPIRE_NOTE). Supersede: an open card is
    withdrawn when a newer open card has the same normalized label and the same `where`; superseding applies only to
    read-only cards too, so a human-actionable older card is never silently dropped. Humans' done always wins (a done
    card is no longer open, so it is never touched)."""
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
