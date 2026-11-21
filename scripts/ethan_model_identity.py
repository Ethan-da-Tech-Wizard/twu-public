# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Model identity guard: a trained model must be the model the CLI actually serves.

Ethan's rule (2026-11-01): "models get trained but never reach what the CLI serves". This is a deterministic
invariant checker. It reads, read-only: the running server (GET /props, /lora-adapters on 127.0.0.1:18190), the
bridge (GET /health on 18195), trainer sources, the personality registry, trained artifacts on disk, and the
promotion receipts under data/autoimprove/20261101/promotions/. It never starts, stops or calls a model.

Fails (exit 1) when:
  trainer_base      a trainer's base model family/size differs from the model the CLI serves
  artifact_record   a trained adapter/checkpoint/export has no promotion receipt or disposition
  receipt_valid     a receipt says "promoted" but records no serving path or sha
  bridge_adapter    the bridge /health reports no adapter while one is recorded as promoted
  bridge_model      the bridge reports a different model than the server runs
  registry_active   a promoted adapter/model is recorded active but the server is not running it
  unrecorded_adapter the server runs an adapter no promotion receipt accounts for
  registry_model    the active personality profile names a different model family than the server
  adapter_base      the promoted adapter was trained on a different base than the served model

  python3 scripts/ethan_model_identity.py            # human report, exit 1 on failure
  python3 scripts/ethan_model_identity.py --check    # quiet when clean, exit 1 on failure (for check_all / alarm)
  python3 scripts/ethan_model_identity.py --json     # machine report
  python3 scripts/ethan_model_identity.py --grandfather   # record legacy never-served artifacts (see function)
"""
from __future__ import annotations
import argparse
import contextlib
import io
import json
import os
import re
import socket
import sys
import tokenize
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple

def family(text: Any) -> Optional[Dict[str, Any]]:
    """Parse the model-bearing path component, ignoring unrelated parent-directory tokens."""
    raise NotImplementedError('TODO: implement')

def family_label(fam: Optional[Dict[str, Any]]) -> str:
    raise NotImplementedError('TODO: implement')

def same_family(a: Optional[Dict[str, Any]], b: Optional[Dict[str, Any]]) -> bool:
    """True only if they are provably the same architecture and size. Unknown size on either side is not a mismatch."""
    raise NotImplementedError('TODO: implement')

def http_get_json(url: str, timeout: float=2.0) -> Tuple[Any, Optional[str]]:
    """Read-only GET. Returns (json, None) or (None, reason). No proxy, no redirects followed."""
    raise NotImplementedError('TODO: implement')

def autostart_chain_model() -> Optional[str]:
    """Model the next server start would load (magi_autostart candidate chain). No process is started."""
    raise NotImplementedError('TODO: implement')

def registry_active_profile() -> Optional[Dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def host_key(name: Any) -> str:
    """Normalise a hostname so 'host-h' and 'ethans-example_host' compare equal."""
    raise NotImplementedError('TODO: implement')

def code_only_lines(text: str) -> List[str]:
    """Source lines with comments and docstrings blanked (line numbers preserved), so prose that merely
    mentions a model or tool name is not read as a training target. Falls back to the raw lines if the
    text cannot be tokenised (non-Python or broken file): a check must not go blind on a parse error."""
    raise NotImplementedError('TODO: implement')

class Env:

    def __init__(self, repo: Path=..., promo_dir: Path=..., roots: Optional[List[Path]]=None, get: Callable[[str], Tuple[Any, Optional[str]]]=..., chain: Callable[[], Optional[str]]=..., profile: Callable[[], Optional[Dict[str, Any]]]=..., trainers: Optional[List[str]]=None, now: Optional[datetime]=None, server: str=..., bridge: str=..., host: Optional[str]=None):
        raise NotImplementedError('TODO: implement')

def finding(cid: str, ok: bool, what: str, fix: str=..., severity: str=..., **extra: Any) -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def observe_server(env: Env) -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def discover_trainers(env: Env) -> List[str]:
    """Any other non-test script under scripts/, private/example_host, turnkey_appliance that builds a LoRA/SFT/DPO trainer."""
    raise NotImplementedError('TODO: implement')

def find_trainer_bases(env: Env) -> List[Dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def load_receipts(promo_dir: Path) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[str]]:
    """(receipts, dispositions, problems). A dispositions file holds {"dispositions": [...]}."""
    raise NotImplementedError('TODO: implement')

def receipt_paths(r: Dict[str, Any]) -> List[str]:
    raise NotImplementedError('TODO: implement')

def scan_artifacts(env: Env) -> Dict[str, List[str]]:
    """run directory -> trained files in it (adapter weights, tuned/merged GGUFs)."""
    raise NotImplementedError('TODO: implement')

def under(child: str, parent: str) -> bool:
    raise NotImplementedError('TODO: implement')

def run_base_family(run: str) -> Optional[Dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def lane_applies_here(lane: Dict[str, Any], env: Env) -> bool:
    """A lane with a `hosts` list only excuses a mismatch on those hosts (e.g. the Air serves a smaller
    model than example_host). A lane without `hosts` applies everywhere, as before."""
    raise NotImplementedError('TODO: implement')

def check_trainers(env: Env, served: Dict[str, Any], lanes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def check_artifacts(env: Env, receipts, dispositions, served) -> List[Dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def check_receipts(receipts, problems) -> List[Dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def expected_state(receipts) -> Optional[Dict[str, Any]]:
    """The newest applied promotion still in force. A rollback removes the promotion it names in 'reverts',
    or all of them when it names none."""
    raise NotImplementedError('TODO: implement')

def check_serving(env: Env, served, receipts, deep: bool) -> List[Dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def check_bridge(env: Env, served, receipts) -> List[Dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def check_registry_model(env: Env, served) -> List[Dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def lanes_from(env: Env) -> List[Dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def run_checks(env: Optional[Env]=None, deep: bool=False) -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def render(report: Dict[str, Any], quiet_ok: bool=False) -> str:
    raise NotImplementedError('TODO: implement')

def grandfather(env: Env) -> Dict[str, Any]:
    """One-time, explicit: record artifacts that predate this guard and were provably never served as
    'legacy_not_served'. Skips anything the serving config (autostart chain or registry) references by name: those need a real
    receipt. New artifacts after this are not covered, so they fail until promoted or dispositioned."""
    raise NotImplementedError('TODO: implement')

def alarm_problems(env: Optional[Env]=None) -> Dict[str, str]:
    """For ethan_alarm.collect(): {key: plain-English text} for every failure. Never raises; an internal error is itself a problem."""
    raise NotImplementedError('TODO: implement')

def main(argv: Optional[List[str]]=None) -> int:
    raise NotImplementedError('TODO: implement')
