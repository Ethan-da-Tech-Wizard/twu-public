# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/dsce_route.py: decide, deterministically, whether DSCE should handle a coding request.

  dsce_route.py route "make me a new python module called parser"

Prints one JSON object: {applies, language, kind, name, argv, confidence, reason}. Keywords and regex only:
no model, no network, and it NEVER executes anything. `argv` is the exact DRY-RUN `dsce_catalog.py make`
command; a caller that wants the file adds `--write` itself, and should do so only when applies is true and
confidence is "high". DSCE saves about 9% on logic-heavy code but about 22x on boilerplate, so logic-heavy or
ambiguous requests are left to the model (applies=false with a reason).
"""
from __future__ import annotations
import argparse
import difflib
import json
import re
import sys
from pathlib import Path
import dsce_catalog as _cat

def _result(applies, reason, language=None, kind=None, name=None, argv=None, confidence=...):
    raise NotImplementedError('TODO: implement')

def _fuzzy(tok, vocab, cutoff=0.8):
    raise NotImplementedError('TODO: implement')

def _find_languages(text: str):
    """Return (set of language ids, set of unsupported names, fuzzy_used)."""
    raise NotImplementedError('TODO: implement')

def _has_word(text: str, words):
    raise NotImplementedError('TODO: implement')

def route(text: str) -> dict:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
