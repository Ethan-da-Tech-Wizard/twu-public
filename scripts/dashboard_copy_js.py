# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Real Copy buttons for the read-only dashboard pages (/commands, /cockpit, /power).

PROGRAM:       dashboard_copy_js.py
PROGRAMMER:    Magi 10 (Seat 10, claude, example_host)
LAST MODIFIED: 2026-11-20
PURPOSE:       Give every selectable command on the pages a real Copy button without weakening the page security policy.
               It reuses the SAME copy logic as the owner-card Copy buttons (ygCopyExact in dashboard_command_center.py):
               navigator.clipboard.writeText, then a hidden-textarea execCommand fallback for non-secure contexts, then
               selecting the text so Ctrl+C works. The string in the data-copy attribute is the ONLY thing ever copied: no label,
               no newline added.
CSP:           The default page policy is script-src 'self' plus sha256 hashes of the built-in inline scripts. This module does
               NOT add an inline script and does NOT loosen the policy: the pages load /static/copy.js, a same-origin file that
               script-src 'self' already allows. The route is served from twu_dashboard.py.
PROGRESSIVE:   Buttons are emitted with the `hidden` attribute. The script un-hides them, so if JavaScript is blocked or fails there
               is no dead button and the existing click-to-select text (user-select:all) still works exactly as before.
SAFETY:        Payloads are HTML-escaped into a data attribute (quote-safe), comment lines are dropped (owner-card lint rule: one
               command per button, no prose), and nothing is ever executed.

CHANGE HISTORY
  2026-11-20  Magi 10  Created (MAGI_TODO 5115e654).
  2026-11-20  Magi 10  Phone-width CSS (tables scroll, long commands wrap) after the real-browser check showed sideways overflow at 390 px.
"""
from __future__ import annotations
import html
import re

def clean_command(text: str) -> str:
    """One command per button: drop blank lines and # comment lines, keep each remaining line verbatim (stripped)."""
    raise NotImplementedError('TODO: implement')

def button(text: str) -> str:
    """HTML for one hidden-until-JS Copy button; the payload is the exact command text in an escaped data attribute."""
    raise NotImplementedError('TODO: implement')

def inject(page_html: str) -> str:
    """Add the stylesheet rule and the same-origin script tag once, before the final </body>. Safe to call twice."""
    raise NotImplementedError('TODO: implement')
