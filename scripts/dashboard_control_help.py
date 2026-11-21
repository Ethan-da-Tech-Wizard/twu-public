# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""
PROGRAM:       dashboard_control_help.py
PROGRAMMER:    Magi 10 (claude, example_host), MAGI_TODO 1675dfd2
LAST MODIFIED: 2026-11-20
PURPOSE:       Put a plain-language explanation on EVERY dashboard control, without any script on the page.

HOW:  data/dashboard/control_help.json holds rules (regex on a stable control id) -> help text.  annotate(page, html)
      finds each control (button, link, summary, select, input, textarea) in the HTML the dashboard is about to send,
      looks up its help, and adds two inert attributes to its start tag:
        title="..."            (hover / long-press tooltip: what it does, what it will NOT do, what it runs and where)
        aria-description="..." (read by screen readers)
      Nothing else in the page changes.  No JavaScript is added, so the strict Content-Security-Policy is untouched.
      A control that already has a title keeps it; only aria-description is added then.  A page that cannot be parsed is
      returned unchanged (the help is a convenience and must never break a page).

SAFETY: read-only; never runs a dashboard action; the help JSON is data, not code.
CHANGE HISTORY:
  2026-11-20  Magi 10  Created.
  2026-11-20  Magi 10  (MAGI_TODO 4cf8fa90) Rules can match attributes (see dashboard_control_inventory.match_help); help text may use {title} and
                       {label}; /cockpit and every /commands/<name> page are annotated (ROUTE_PAGE and ROUTE_PREFIX_PAGE).
"""
from __future__ import annotations
import html as _html
import json
import os
import sys
from pathlib import Path
import dashboard_control_inventory as inv

def _help() -> dict:
    """Load control_help.json, re-reading when the file changes."""
    raise NotImplementedError('TODO: implement')

def help_text(entry: dict, control: dict=None) -> str:
    """One short paragraph from a help entry: what it does, what it will not do, what it runs, why it may be disabled.

    2026-11-20 Magi 10: the text may hold {title} and {label}; they are replaced by the control's own tooltip text and visible label,
    so one rule can cover a whole family of buttons (for example every panel button) and still say what THIS button does."""
    raise NotImplementedError('TODO: implement')

def _line_starts(text: str) -> list:
    raise NotImplementedError('TODO: implement')

def annotate(page: str, html: str) -> str:
    """Return html with title / aria-description added to every control that has help.  Never raises."""
    raise NotImplementedError('TODO: implement')

def annotate_response(route: str, body: bytes) -> bytes:
    """Entry point for the dashboard's response writer: annotate HTML bytes for a known route, else return them unchanged."""
    raise NotImplementedError('TODO: implement')
