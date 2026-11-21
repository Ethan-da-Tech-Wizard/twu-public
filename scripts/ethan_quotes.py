# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Quotes shown in the Ethan CLI header, one per new session, drawn from proverbs and writings around the world.

Each entry is (original, English, source). A shuffled cycle is kept in data/quote_state.json so no quote repeats
until every quote has been shown. Stdlib only; no network.

  ethan_quotes.py --next   print the next quote (advances the cycle)
  ethan_quotes.py --all    list every quote
"""
import json, os, random, re, sys, unicodedata
from pathlib import Path

def safe_text(text):
    """Treat catalog text as display data, never terminal commands; keep language joiners."""
    raise NotImplementedError('TODO: implement')

def display_width(text):
    """Terminal columns used by text: wide (CJK) characters take 2, combining marks take 0."""
    raise NotImplementedError('TODO: implement')

def wrap_to(text, width):
    """Wrap text to at most `width` terminal columns per line, breaking on spaces (or per character for long words)."""
    raise NotImplementedError('TODO: implement')

def terminal_columns(default=80):
    raise NotImplementedError('TODO: implement')

def fmt(q, columns=None):
    """Quote on its own line(s), then the translation and source, each wrapped to fit beside the logo."""
    raise NotImplementedError('TODO: implement')

def next_quote():
    raise NotImplementedError('TODO: implement')

def next_talos_quote(columns=None):
    raise NotImplementedError('TODO: implement')

def render_nine_divines():
    raise NotImplementedError('TODO: implement')
