# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""directive_scrub: flag STALE TEMPORAL DIRECTIVES (time-of-day framing) in a message. Stdlib only, offline, never blocks.

Time-of-day framing ("good night", "in the morning", "go to sleep", "defer to tomorrow" ...) is noise: it never changes the queue,
closes a fire or authorizes a deferral. This lint prints one line per hit and exits 0 either way; exit 1 only when the input cannot be read.
Phrases inside backticks, inside ``` fences, or inside file-path-like tokens are data, not directives, and are ignored.

  directive_scrub.py [FILE]     read FILE, or stdin when no FILE is given
  directive_scrub.py --hook     read a CLI hook's JSON on stdin (field "prompt", "user_prompt" or "message"), scan that text;
                                plain text or bad JSON is scanned as-is. Always exit 0: a hook must never block a turn.
  directive_scrub.py --gemini-hook EVENT   same, for Gemini CLI: prints {} or {"hookSpecificOutput": {"hookEventName": EVENT,
                                "additionalContext": "<warnings>"}} (the same shape ethan_alarm.py --gemini-hook uses)
"""
from __future__ import annotations
import json
import re
import sys

def _blank(m):
    raise NotImplementedError('TODO: implement')

def mask(text):
    """Replace code and path-like text with spaces, keeping every newline so line numbers stay true."""
    raise NotImplementedError('TODO: implement')

def scan(text):
    """-> [{'line': N, 'phrase': matched text}] in order."""
    raise NotImplementedError('TODO: implement')

def line_for(hit):
    raise NotImplementedError('TODO: implement')

def hook_text(raw):
    """The text to scan from a hook payload: the JSON prompt field when there is one, else the raw input."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
