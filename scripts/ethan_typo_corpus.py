# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Build a bounded, sanitized typo-correction evidence corpus.

This is deliberately not a training-data generator and not a daemon.  It reads
the two fixed cross-box transcript mirrors once, considers only explicitly
human-interactive rows, and writes token-pair aggregates with source-content
hashes.  It never writes prompt text, session IDs, paths, model output, or
commands to its result.
"""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from typing import Any, Iterable
from ethan_typo_normalizer import CONTEXT_ADJACENT, CONTEXT_NEXT, ETHAN_TYPO_DICTIONARY, REVIEW_CANDIDATES, EthanTypoNormalizer
from ethan_decoder_tokens import core_of, protected_token, prose_segments

def is_sensitive(text: str) -> bool:
    raise NotImplementedError('TODO: implement')

def safe_exact_typo(raw: str) -> str | None:
    """Return an exact reviewed typo token, or None for opaque/code-like text."""
    raise NotImplementedError('TODO: implement')

def safe_candidate_token(raw: str) -> tuple[str, str, str | None] | None:
    """Return sanitized token-only discovery metadata, never a promotion.

    Exact reviewed spellings retain their proposed target.  New repeated-letter
    prose tokens have no proposed replacement and must be explicitly reviewed.
    """
    raise NotImplementedError('TODO: implement')

def source_hash(text: str) -> str:
    """A source pointer only; prompt text is never persisted in the corpus."""
    raise NotImplementedError('TODO: implement')

def iter_candidates(source: Path) -> Iterable[tuple[str, str, str, str, str | None]]:
    """Yield token-only candidates; no prompt text, commands, or raw rows persist."""
    raise NotImplementedError('TODO: implement')

def build(sources: Iterable[Path]) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def atomic_write_json(path: Path, value: dict[str, Any]) -> None:
    """Publish a completed corpus atomically; interruption keeps the prior bytes."""
    raise NotImplementedError('TODO: implement')

def main(argv: list[str] | None=None) -> int:
    raise NotImplementedError('TODO: implement')
