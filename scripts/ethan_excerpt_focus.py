# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Focus retrieved excerpts for a small model (Magi 15, 2026-11-06).

Evidence: the local 7B was handed the correct policy paragraph (one 1,500-character chunk) and still swapped "may START at GPU <=88"
for "pauses at GPU <=88" (data/tool_trials/example_host/2026-11-06-m9-cli-continuation/thermal/). The relevant sentence was buried mid-chunk.
focus_pack(pack, question) keeps each [n] chunk's own words but shows only the sentences that share the most terms with the question
(max 2, original order) and labels each with its file:line, so the model reads the clause, not the paragraph. No answers are baked in:
the choice is term overlap with the question only. A chunk with no overlapping sentence is cut to its first 300 characters.

  python3 scripts/ethan_excerpt_focus.py "<question>" < answer-pack-output
"""
from __future__ import annotations
import re
import sys

def _terms(text: str) -> set[str]:
    raise NotImplementedError('TODO: implement')

def focus_text(chunk: str, question_terms: set[str], max_sentences: int=2, max_chars: int=1000) -> str:
    raise NotImplementedError('TODO: implement')

def focus_pack(pack: str, question: str) -> str:
    """Rewrite the body items of an answer-pack. Header lines and the SOURCES footer are kept exactly. Unparseable input is returned unchanged."""
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
