# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Incremental, evidence-linked conversation harvesting for Codex rollouts.

The parser is deliberately read-only with respect to Codex's own files.  It
emits a small canonical event stream and admits a training pair only when an
observed request has a failed action, a distinct repair, successful
verification, and a final outcome.  Secret-bearing and duplicate candidates
fail closed.
"""
from __future__ import annotations
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from typing import Any, Dict, Iterable, List, Optional, Tuple

def _utc_now() -> str:
    raise NotImplementedError('TODO: implement')

def _text(value: Any) -> str:
    raise NotImplementedError('TODO: implement')

def _message_text(payload: Dict[str, Any]) -> str:
    raise NotImplementedError('TODO: implement')

def _stable_id(*parts: str) -> str:
    raise NotImplementedError('TODO: implement')

def _safe_text(text: str) -> Tuple[str, bool]:
    raise NotImplementedError('TODO: implement')

class ConversationEvent:
    pass

def _new_event(*, session_id: str, source_id: str, sequence: int, timestamp: str, event_type: str, actor: str, content: str, request_event_id: str, parent_event_id: str=..., call_id: str=..., tool: str=...) -> ConversationEvent:
    raise NotImplementedError('TODO: implement')

class CodexConversationEventParser:
    """The authoritative parser for rich Codex rollout records."""

    def __init__(self, cursor_path: Path):
        raise NotImplementedError('TODO: implement')

    def _load_cursors(self) -> Dict[str, Any]:
        raise NotImplementedError('TODO: implement')

    def save_cursors(self) -> None:
        raise NotImplementedError('TODO: implement')

    @staticmethod
    def source_id(path: Path) -> str:
        raise NotImplementedError('TODO: implement')

    def parse_file(self, path: Path) -> Tuple[List[ConversationEvent], List[Dict[str, Any]]]:
        raise NotImplementedError('TODO: implement')

    @staticmethod
    def _admission_candidate(state: Dict[str, Any], outcome: ConversationEvent) -> Optional[Dict[str, Any]]:
        raise NotImplementedError('TODO: implement')

def read_jsonl_lines(path: Path) -> Iterable[str]:
    """Yield the lines of a JSONL file split ONLY on real newlines. str.splitlines() also splits on U+2028, U+2029 and a few
    control characters that can sit inside a JSON string (a pasted prompt or a tool output), which cut one record into two
    broken halves and made readers throw the whole journal away."""
    raise NotImplementedError('TODO: implement')

def append_unique_jsonl(path: Path, rows: Iterable[Dict[str, Any]], key: str=...) -> int:
    """Append unique rows, refusing to extend a malformed journal."""
    raise NotImplementedError('TODO: implement')
