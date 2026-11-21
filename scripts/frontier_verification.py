# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/frontier_verification.py — frontier-verified local-model outcomes.

When a frontier Magi independently verifies work the local model produced (for
example: the 20B wrote a test file through Ethan's CLI and a frontier Magi ran
it and saw it pass), that verification is recorded here instead of vanishing
into a chat message:

  * data/example_host/frontier_verified/verified_outcomes.jsonl — every verdict,
    PASS or FAIL, append-only, with content hashes and the evidence line.
  * data/example_host/frontier_verified/verified_sft_pairs.jsonl — PASS outcomes
    only, stored as training-ready prompt/response pairs with provenance.
    This is the quality-labeled stream a future bounded training run consumes;
    recording pairs here does not itself train anything (training remains a
    separate, explicitly authorized decision).

Each verdict is also journaled in the rolling system journal (fail-open), so
the journey record and the training stream grow from the same event.

Prompts and outputs are stored verbatim (evidence is never rewritten).
"""
from __future__ import annotations
import argparse
import hashlib
import json
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

def _merged(pattern: str, legacy: Path, dedupe_keys: Sequence[str]) -> List[Dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def merged_outcomes() -> List[Dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def merged_pairs() -> List[Dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def _sha256(text: str) -> str:
    raise NotImplementedError('TODO: implement')

def _append_jsonl(path: Path, record: Dict[str, Any]) -> None:
    raise NotImplementedError('TODO: implement')

def _journal(kind: str, summary: str, refs: Sequence[str]) -> bool:
    """Mirror the verdict into the rolling system journal; never fatal."""
    raise NotImplementedError('TODO: implement')

def record_verification(task: str, prompt_text: str, output_text: str, verifier: str, verdict: str, evidence: str, source: str=..., model: str=..., output_path: str=..., outcomes_path: Optional[Path]=None, pairs_path: Optional[Path]=None, journal: bool=True) -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def main(argv: Optional[Sequence[str]]=None) -> int:
    raise NotImplementedError('TODO: implement')
