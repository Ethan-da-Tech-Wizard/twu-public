# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Shared safety latches for the autonomous improvement loop (R4 hardening, 2026-11-02). stdlib only, no model, no GPU.

  halt      data/health/HALT: while the file exists NO autonomous change is made (spellbook, promote, thermal governor idle-stop,
            thermal guard resume, selfheal). Create:  python3 scripts/ethan_safety.py halt "why".  Clear: `unhalt` (a human step).
  budget    data/health/CHANGE_BUDGET.json: at most N production-affecting changes per local day (default 2,
            env ETHAN_CHANGE_BUDGET_PER_DAY). Spent by spellbook `set ID live` and by ethan_promote --apply right before the swap.
  checkers  data/health/CHECKER_MANIFEST.json: sha256 of the files that decide pass/fail (check_all, wiring_check, exec_eval, cli
            acceptance, policy suite, this module, the approval tool). Verified before any gate advances or a swap happens.
            First pin is `pin --bootstrap`; any later re-pin needs a real TTY and a typed phrase (an agent cannot do it).
  approval  data/health/approvals/RUN.json: written only by scripts/ethan_approve.py (real TTY on stdin and stdout + typed phrase),
            bound to run id, model sha256, adapter sha256, expiry (24 h), HMAC-signed with ~/.config/ethan/approval.key.
Test/override: ETHAN_HEALTH_DIR points every path at another folder.
"""
from __future__ import annotations
import hashlib
import hmac
import json
import os
import secrets
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

def health_dir() -> Path:
    raise NotImplementedError('TODO: implement')

def sha256_file(path) -> str | None:
    raise NotImplementedError('TODO: implement')

def _atomic(path: Path, data: dict) -> None:
    raise NotImplementedError('TODO: implement')

def halt_path() -> Path:
    raise NotImplementedError('TODO: implement')

def halt_reason() -> str | None:
    """None when running is allowed, else the reason text. An unreadable HALT still halts (fail closed)."""
    raise NotImplementedError('TODO: implement')

def halt(reason: str, who: str=...) -> Path:
    raise NotImplementedError('TODO: implement')

def unhalt() -> bool:
    raise NotImplementedError('TODO: implement')

def budget_limit() -> int:
    raise NotImplementedError('TODO: implement')

def _budget_file() -> Path:
    raise NotImplementedError('TODO: implement')

def _budget_load() -> dict:
    raise NotImplementedError('TODO: implement')

def budget_used(day: str | None=None) -> int:
    raise NotImplementedError('TODO: implement')

def budget_check() -> str | None:
    """None if one more change is allowed today, else the refusal reason. Does not spend."""
    raise NotImplementedError('TODO: implement')

def budget_take(kind: str, ref: str) -> str | None:
    """Spend one change. None on success, else the refusal reason (nothing spent)."""
    raise NotImplementedError('TODO: implement')

def _manifest_file() -> Path:
    raise NotImplementedError('TODO: implement')

def pin(root: Path=..., files=..., why: str=...) -> dict:
    raise NotImplementedError('TODO: implement')

def verify_checkers(root: Path=...) -> list[str]:
    """Problems (empty = every pinned checker is byte-identical). Missing manifest or missing file is a problem (fail closed)."""
    raise NotImplementedError('TODO: implement')

def key_file() -> Path:
    raise NotImplementedError('TODO: implement')

def approvals_dir() -> Path:
    raise NotImplementedError('TODO: implement')

def _sign(key: bytes, body: dict) -> str:
    raise NotImplementedError('TODO: implement')

def have_tty() -> bool:
    raise NotImplementedError('TODO: implement')

def challenge_phrase(run: str, model_sha: str) -> str:
    raise NotImplementedError('TODO: implement')

def make_approval(run: str, model_sha: str, adapter_sha: str | None, who: str, now: datetime | None=None, ttl_h: float=...) -> Path:
    """Write the signed receipt. Callers (ethan_approve.py) must have passed the TTY + phrase checks; this only signs."""
    raise NotImplementedError('TODO: implement')

def _approval_path(run: str) -> Path:
    raise NotImplementedError('TODO: implement')

def verify_approval(run: str, model_sha: str, adapter_sha: str | None, now: datetime | None=None) -> tuple[bool, str]:
    """(ok, who-or-reason). Needs a signed, unexpired, unused receipt bound to this exact run, model and adapter."""
    raise NotImplementedError('TODO: implement')

def consume_approval(run: str) -> None:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
