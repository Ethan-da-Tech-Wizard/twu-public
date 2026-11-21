# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Promotion path: how a trained model reaches what the CLI serves. Fail-closed state machine.

Follows ADAPTER_SERVING_PLAN.md section 4 (steps 0-11). --dry-run is the default: every read-only gate runs for real,
destructive steps are only printed. --apply (with Ethan's approval receipt) additionally performs the swap.

  python3 scripts/ethan_promote.py --run cand1 --model-gguf BASE.gguf --adapter-gguf LORA.gguf:1.0 \\
      --adapter-dir RUN/adapter --base-eval base7b.json --cand-base-eval cand_base.json --cand-tuned-eval cand_tuned.json \\
      --acceptance-baseline 7/9                       # dry run
  ... --apply                                         # real swap; needs Ethan's receipt (python3 scripts/ethan_approve.py RUN)

Steps: 0 preconditions, 1 baseline, 2 in-flight check, 3 trained artifacts, 4 production healthy, 5 converted artifacts +
sha256, 6 candidate serving identity (second port 18191), 7 execution eval gates (McNemar, non-inferiority, zero unsafe),
8 CLI acceptance (after the swap; failure rolls back), 9 promote via ethan-model.service, 10 automatic rollback,
11 receipt under data/autoimprove/20261101/promotions/.

Hard refusals: the model/adapter that will be served must be byte-identical (sha256) to what the evals measured; the swap
happens only with zero established connections on 18190 and an idle /slots; after the swap the live server, the bridge and
the identity guard (ethan_model_identity.py) must all agree or the previous model is restored.
No GPU work, no training, no model request is made by this tool; it never kills by name.
"""
from __future__ import annotations
import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple
import ethan_model_identity as mi
import ethan_safety as safety

class Ops:
    """All reads and effects. Tests replace this with a fake; nothing else touches the system."""

    def get_json(self, url: str, timeout: float=3.0) -> Tuple[Any, Optional[str]]:
        raise NotImplementedError('TODO: implement')

    def established(self, port: int) -> Optional[int]:
        raise NotImplementedError('TODO: implement')

    def sha(self, path: str) -> Optional[str]:
        raise NotImplementedError('TODO: implement')

    def run(self, cmd: List[str], timeout: int=7200) -> Tuple[int, str]:
        raise NotImplementedError('TODO: implement')

    def stop_model(self) -> bool:
        raise NotImplementedError('TODO: implement')

    def env_get(self) -> Dict[str, str]:
        raise NotImplementedError('TODO: implement')

    def env_set(self, values: Dict[str, str], unset: List[str]) -> bool:
        raise NotImplementedError('TODO: implement')

    def start_unit(self) -> bool:
        raise NotImplementedError('TODO: implement')

    def wait_health(self, port: int, timeout: float) -> bool:
        raise NotImplementedError('TODO: implement')

    def wait_port_closed(self, port: int, timeout: float=30) -> bool:
        raise NotImplementedError('TODO: implement')

    def latest_acceptance(self) -> Optional[Dict[str, Any]]:
        raise NotImplementedError('TODO: implement')

    def guard(self, promo_dir: Path) -> Dict[str, Any]:
        raise NotImplementedError('TODO: implement')

    def latches(self) -> List[str]:
        raise NotImplementedError('TODO: implement')

    def now(self) -> datetime:
        raise NotImplementedError('TODO: implement')

    def halted(self) -> Optional[str]:
        raise NotImplementedError('TODO: implement')

    def checker_problems(self) -> List[str]:
        raise NotImplementedError('TODO: implement')

    def approval(self, run: str, model_sha: str, adapter_sha: Optional[str]) -> Tuple[bool, str]:
        raise NotImplementedError('TODO: implement')

    def consume_approval(self, run: str) -> None:
        raise NotImplementedError('TODO: implement')

    def budget_check(self) -> Optional[str]:
        raise NotImplementedError('TODO: implement')

    def budget_take(self, run: str) -> Optional[str]:
        raise NotImplementedError('TODO: implement')

def parse_spec(spec: Optional[str]) -> Optional[Tuple[str, float]]:
    raise NotImplementedError('TODO: implement')

def safe_alias(run: str) -> str:
    raise NotImplementedError('TODO: implement')

def active_adapters(ident: Dict[str, Any]) -> List[Tuple[Optional[str], float]]:
    raise NotImplementedError('TODO: implement')

class Refuse(Exception):
    pass

class Pipeline:

    def __init__(self, a: argparse.Namespace, ops: Ops):
        raise NotImplementedError('TODO: implement')

    def record(self, num: int, name: str, status: str, detail: Any=...) -> None:
        raise NotImplementedError('TODO: implement')

    def need(self, cond: bool, why: str) -> None:
        raise NotImplementedError('TODO: implement')

    def load_eval(self, path: str, what: str) -> Dict[str, Any]:
        raise NotImplementedError('TODO: implement')

    def step0_preconditions(self) -> None:
        raise NotImplementedError('TODO: implement')

    def production_identity(self) -> Dict[str, Any]:
        raise NotImplementedError('TODO: implement')

    def step1_baseline(self) -> None:
        raise NotImplementedError('TODO: implement')

    def inflight(self) -> Tuple[bool, str]:
        raise NotImplementedError('TODO: implement')

    def step2_inflight(self) -> None:
        raise NotImplementedError('TODO: implement')

    def step3_artifacts(self) -> None:
        raise NotImplementedError('TODO: implement')

    def step4_production_healthy(self) -> None:
        raise NotImplementedError('TODO: implement')

    def step5_converted(self) -> None:
        raise NotImplementedError('TODO: implement')

    def candidate_command(self) -> str:
        raise NotImplementedError('TODO: implement')

    def step6_candidate(self) -> None:
        raise NotImplementedError('TODO: implement')

    def bind(self, name: str, path: str, want_adapter: bool) -> Dict[str, Any]:
        raise NotImplementedError('TODO: implement')

    def step7_eval(self) -> None:
        raise NotImplementedError('TODO: implement')

    def step8_acceptance_plan(self) -> None:
        raise NotImplementedError('TODO: implement')

    def expected_cmd(self) -> Dict[str, str]:
        raise NotImplementedError('TODO: implement')

    def verify_live(self, model_path: str, model_sha: str, adapter: Optional[Tuple[str, float]]) -> Optional[str]:
        """None if the live server and bridge match exactly; else the reason."""
        raise NotImplementedError('TODO: implement')

    def swap(self) -> Optional[str]:
        """Returns None on success, else a reason (the caller rolls back)."""
        raise NotImplementedError('TODO: implement')

    def acceptance(self) -> Optional[str]:
        raise NotImplementedError('TODO: implement')

    def rollback(self, reason: str) -> bool:
        raise NotImplementedError('TODO: implement')

    def receipt(self, decision: str, reason: str, applied: bool, extra: Optional[Dict[str, Any]]=None) -> Path:
        raise NotImplementedError('TODO: implement')

    def run(self) -> int:
        raise NotImplementedError('TODO: implement')

def build_parser() -> argparse.ArgumentParser:
    raise NotImplementedError('TODO: implement')

def main(argv: Optional[List[str]]=None, ops: Optional[Ops]=None) -> int:
    raise NotImplementedError('TODO: implement')
