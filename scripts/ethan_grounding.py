# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Deterministic grounding for natural workspace questions (Magi 15, 2026-11-06).

The local 7B often answers "what are OUR limits / how does OUR X work" from memory instead of calling a tool
(Magi 5 and 7 witnesses, 0 tools, invented sources). This module does the retrieval for it, outside the model:

  question_text(openai_messages) -> the last user turn with complete leading/trailing harness wrappers removed
  is_workspace_question(text)    -> conservative: asks about THIS system (our/Ethan/Magi/TWU/example_host/AGENTS/...) AND is a question
  ground(text)                   -> {"block": str, "receipt": dict} or None; runs `ethan_know.py answer-pack` (CPU; transactionally refreshes its derived index before retrieval)
  add_grounding(messages)        -> the same messages with a labeled low-trust data block appended to the END of the last user message (system bytes never change)

The block is evidence, not instructions, and it carries the answer-pack's own source citations. It never creates or alters
a tool call, never touches the no-change/destructive checks, and reports retrieval/logging failures without claiming success. Host-owned receipts under
data/self_improve/<host>/grounding_log.jsonl contain hashes and status metadata, no question, excerpt, or source-path text.
Receipts describe attachment to a request, never backend delivery or verified model truth.

  python3 scripts/ethan_grounding.py "What are our GPU pause limits?"     print the block that would be injected
"""
from __future__ import annotations
import copy
import hashlib
import json
import os
import re
import socket
import stat
import subprocess
import sys
import time
from pathlib import Path

def _text_of(message: dict) -> str:
    raise NotImplementedError('TODO: implement')

def question_text(messages: list) -> str:
    """The last user turn as typed: only complete, known harness wrappers at the very start or end are removed (text inside the
    user's own words, even a literal tag, is kept)."""
    raise NotImplementedError('TODO: implement')

def search_query(text: str) -> str:
    """The question without known harness metadata (provenance prefix, trailing instructions), so BM25's term budget goes to the topic."""
    raise NotImplementedError('TODO: implement')

def is_workspace_question(text: str) -> bool:
    """True for a question about this system. Imperative build/edit/run requests are left to the normal tool path."""
    raise NotImplementedError('TODO: implement')

def expand_query(text: str) -> str:
    """Add the repo's own names for a generic term (fleet -> example_host example_host example_host Air) so BM25 finds the sentence that lists them."""
    raise NotImplementedError('TODO: implement')

class GroundedMessage(dict):
    """Keep intent provenance in memory; JSON serializes only ordinary role/content fields."""

def _hash(text: str) -> str:
    raise NotImplementedError('TODO: implement')

def _log(receipt: dict) -> bool:
    """Append private host-owned metadata without following any path component."""
    raise NotImplementedError('TODO: implement')

def ground(text: str, runner=None, log: bool=True) -> dict | None:
    """Retrieve for one workspace question. Returns None only when it is not a workspace question. Otherwise {"block", "receipt"} where
    receipt["status"] is found | none | error | timeout; non-found statuses still produce a block telling the model retrieval failed."""
    raise NotImplementedError('TODO: implement')

def add_grounding(messages: list, runner=None) -> list:
    """Attach lower-trust evidence to the actual user turn, preserving its original intent in memory."""
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
