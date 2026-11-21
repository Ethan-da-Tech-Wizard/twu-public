# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Suggest-only live decoding of Ethan's typed prompt for the Ethan CLI bridge.

Authorized as isolated candidate work (M9-M10-LIVE-DECODE-CANDIDATE-20261025). The bridge —
owned by the Mac coordinator — may call `annotation_for()` between Enki admission and model
dispatch. This module NEVER mutates the admitted payload: it returns either None or one extra
system-channel text block, marked with the harness provenance marker (prompt_provenance.MARKER),
that offers a decoded reading of the human turn. The original bytes, and therefore the
prompt_sha256 recorded by the native hooks and the admission suffix-hash invariant, are untouched.

Guarantees (each one tested):
  * fail open — any error, oversize input, or disabled mode returns None and the bridge
    forwards the payload byte-identical to today;
  * suggestions are explicitly non-authoritative in the block's own wording;
  * protected text is preserved by construction: decoding uses EthanTypoNormalizer, whose
    exact-pair rules skip code spans, names, acronyms, paths, flags and ambiguous words;
  * ETHAN_LIVE_DECODE=0 disables everything;
  * the feedback log keeps pairs + prompt hash only — never prompt text (corpus privacy rule).
"""
from __future__ import annotations
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from ethan_typo_normalizer import EthanTypoNormalizer
from prompt_provenance import MARKER_PREFIX

def enabled() -> bool:
    raise NotImplementedError('TODO: implement')

def annotation_for(turn_text: str | bytes, context_prefix_bytes: int=0) -> str | None:
    """One suggest-only annotation block for the human part of an admitted turn, or None.

    `context_prefix_bytes` is the length of harness-injected context at the start of the
    admitted turn (enki_station admission); decoding only ever reads the human remainder.
    Never raises; never alters its input.
    """
    raise NotImplementedError('TODO: implement')

def _log(raw: bytes, pairs) -> None:
    """Append pairs + prompt hash only; the prompt text itself is never persisted here."""
    raise NotImplementedError('TODO: implement')
