# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Audit the current cross-device prompt mirrors without retaining prompt text.

This is a one-shot, read-only verifier for the deterministic Ethan typo
decoder. It deliberately reports only aggregate counters and file-level
fingerprints. It is not a scraper, training-data generator, daemon, or model
caller.
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
from typing import Any, Iterable
from scripts.ethan_typo_normalizer import EthanTypoNormalizer
from ethan_typo_corpus import is_sensitive
from ethan_decoder_tokens import prose_segments

def sensitive(text: str) -> bool:
    raise NotImplementedError('TODO: implement')

def is_protected(token: str) -> bool:
    """Match the decoder's opaque-token boundary without revealing tokens."""
    raise NotImplementedError('TODO: implement')

def file_sha256(path: Path) -> str:
    raise NotImplementedError('TODO: implement')

def audit_source(path: Path) -> tuple[Counter[str], dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def audit(sources: Iterable[Path]) -> dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def main(argv: list[str] | None=None) -> int:
    raise NotImplementedError('TODO: implement')
