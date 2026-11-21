# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/prompt_provenance.py — the autonomous-prompt marker (ground truth for "was this prompt autonomous?").

Ethan (2026-10-20): autonomous prompts should start with a specific symbol that appears unnaturally at the
beginning of the prompt without taking anything away from it, so scrapers can tell autonomous from human prompts
by fact, not by guessing from keywords.

Design:
  * MARKER = "◈" (U+25C8) followed by one space, placed at the BEGINNING. The beginning survives truncation
    (the injector clips to 1400 chars and the prompter telemetry logs only the first 250 chars; an end marker
    would be cut off). The prompt text itself is never altered, only prefixed.
  * Applied in exactly one place: NativePromptInjector.inject() (every autonomous daemon goes through it).
  * NOT applied to slash commands (a prompt starting with "/" such as "/compact" must stay a command); those
    stay identifiable through the compactor daemon's own log instead.
  * Humans do not type U+25C8; if a human ever pastes it, the auditor reports it as a marker collision.

"""
from __future__ import annotations

def has_marker(text: str) -> bool:
    raise NotImplementedError('TODO: implement')

def strip_marker(text: str) -> str:
    raise NotImplementedError('TODO: implement')

def should_mark(text: str) -> bool:
    raise NotImplementedError('TODO: implement')

def mark(text: str) -> str:
    """Prefix the marker (idempotent; leaves slash commands and empty text untouched)."""
    raise NotImplementedError('TODO: implement')
