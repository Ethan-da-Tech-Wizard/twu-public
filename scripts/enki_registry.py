# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/enki_registry.py - Enki typed-ID registry, host-scoped receipts, readiness projection.

Schemas: enki.system-registry.v1 (static synced file), enki.registry-receipt.v2
(append-only, one jsonl per host under data/example_host/enki/receipts/<host-uuid>.jsonl so two
boxes can never sync-conflict), enki.host-enrollment.v1 (host-local, outside the workspace).

Commands (stdlib only; machine-readable JSON on stdout):
  validate   read-only; exit 1 on any validation error
  project    read-only; validates first, then prints readiness; exit 1 on any validation error
  init-host  the ONLY command that writes, and it writes OUTSIDE the repo: the host enrollment
             record under --state-dir (default ~/.local/state/twu-enki), dir 0700, file 0600.
             Refuses to overwrite an existing enrollment. Never runs at import time.

Readiness is seven SEPARATE states (specified, implemented, installed, enabled, running,
healthy, accepted). A state counts only with its own evidence (a valid fresh receipt for that
exact state, or for `specified` unchanged declared source files); none is inferred from another.
Connectivity is an observed input: a host that is not observed `online` never projects healthy.

Hosts are never named by mutable labels. A typed host-slot (host-slot.<slug>) is bound to exactly
one ACTIVE host.<uuid>.. through an evidenced binding; replacing hardware retires the old binding
and adds a new one. A product requires slots; readiness needs THAT slot's active host to hold its
own valid current PASS receipt (a receipt from one host never satisfies another host's slot).
The registry also records the system hierarchy (typed entities plus typed relations); its
implementation_state/startup fields are descriptive metadata, never readiness evidence.

Schema notes (also in the registry's schema_notes): subject_revision is the sha256 of the sorted
(declared-source path, file hash) pairs; a subject with no declared sources only needs a non-empty
revision string. Currency failures (registry hash mismatch, expiry, source drift) are fail-closed
validation errors. Non-PASS receipts are valid but never counted. One host is active in only one
slot, and a slot cannot be superseded. A receipt whose host was once bound to its slot but is no
longer the slot's active host (hardware replaced) is INACTIVE history: it must pass every integrity
check, is never counted toward readiness, does not fail validation, and is reported as a count.
A receipt for a host never bound to that slot is rejected (receipt_binding_mismatch).
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import platform
import re
import stat
import subprocess
import sys
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Sequence, Set, Tuple

def canonical_json(obj: Any) -> str:
    raise NotImplementedError('TODO: implement')

def registry_hash(registry: Dict[str, Any]) -> str:
    raise NotImplementedError('TODO: implement')

def sha256_file(path: Path) -> str:
    raise NotImplementedError('TODO: implement')

def _err(errors: List[Dict[str, str]], code: str, detail: str) -> None:
    raise NotImplementedError('TODO: implement')

def id_type(identifier: Any) -> Optional[str]:
    raise NotImplementedError('TODO: implement')

def parse_time(value: Any) -> Optional[datetime]:
    raise NotImplementedError('TODO: implement')

def _run_command(argv: Sequence[str], timeout: float) -> str:
    """Run a command and return stdout; raises OSError / CalledProcessError / TimeoutExpired."""
    raise NotImplementedError('TODO: implement')

def macos_binding_id(system: str, machine: str, runner: Optional[Callable[[Sequence[str], float], str]]=None) -> str:
    """Derived binding hash from IOPlatformUUID, or "" if unavailable. The raw UUID never leaves
    this function. Only call when platform.system() == 'Darwin'."""
    raise NotImplementedError('TODO: implement')

def host_facts(runner: Optional[Callable[[Sequence[str], float], str]]=None) -> Dict[str, str]:
    """Facts that bind an enrollment to this machine. Hostname is excluded on purpose
    (identity must survive a rename). Only a hash of the machine id is recorded.
    Linux: sha256 of /etc/machine-id. macOS (Darwin only): see macos_binding_id."""
    raise NotImplementedError('TODO: implement')

def binding_hash(host_id: str, facts: Dict[str, str]) -> str:
    raise NotImplementedError('TODO: implement')

def enrollment_path(state_dir: Path) -> Path:
    raise NotImplementedError('TODO: implement')

class EnrollmentError(RuntimeError):
    """An enrollment path refusal; `code` is the distinct validation error code."""

    def __init__(self, code: str, detail: str) -> None:
        raise NotImplementedError('TODO: implement')

def _lstat(path: Path) -> Any:
    raise NotImplementedError('TODO: implement')

def _current_uid() -> int:
    raise NotImplementedError('TODO: implement')

def _inspect_node(path: Path, is_dir: bool) -> Tuple[str, Optional[Tuple[str, str]]]:
    """('absent'|'present', refusal). Never follows symlinks, never modifies anything."""
    raise NotImplementedError('TODO: implement')

def _require_safe(path: Path, is_dir: bool) -> str:
    raise NotImplementedError('TODO: implement')

def _read_bounded(path: Path, limit: int) -> bytes:
    """Open without following symlinks or blocking; read at most limit+1 bytes."""
    raise NotImplementedError('TODO: implement')

def init_host(state_dir: Path, facts_fn: Callable[[], Dict[str, str]]=..., now: Optional[datetime]=None) -> Dict[str, Any]:
    """Create the host enrollment. The only writer; refuses to overwrite and refuses unsafe paths.
    Creates the state dir 0700 and the file 0600; never chmods a path it did not create."""
    raise NotImplementedError('TODO: implement')

def check_enrollment(state_dir: Path, facts_fn: Callable[[], Dict[str, str]]=..., errors: Optional[List[Dict[str, str]]]=None) -> Optional[Dict[str, Any]]:
    """Return the enrollment if present, safely stored and bound to this machine; else None.
    Absent enrollment appends no error; any refusal appends a distinct coded error."""
    raise NotImplementedError('TODO: implement')

def _find_cycle(edges: Dict[str, List[str]]) -> Optional[str]:
    raise NotImplementedError('TODO: implement')

def _check_ids(registry: Dict[str, Any], errors: List[Dict[str, str]]) -> Dict[str, Dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def _check_aliases(registry: Dict[str, Any], entities: Dict[str, Dict[str, Any]], errors: List[Dict[str, str]]) -> None:
    raise NotImplementedError('TODO: implement')

def _check_refs_and_routes(entities: Dict[str, Dict[str, Any]], errors: List[Dict[str, str]]) -> None:
    raise NotImplementedError('TODO: implement')

def _check_sources(entities: Dict[str, Dict[str, Any]], root: Path, errors: List[Dict[str, str]]) -> List[Dict[str, str]]:
    raise NotImplementedError('TODO: implement')

def _listed(registry: Dict[str, Any], key: str, errors: List[Dict[str, str]]) -> List[Any]:
    raise NotImplementedError('TODO: implement')

def _registered(entities: Dict[str, Dict[str, Any]], value: Any, kind: str) -> bool:
    raise NotImplementedError('TODO: implement')

def _check_descriptive(entities: Dict[str, Dict[str, Any]], errors: List[Dict[str, str]]) -> None:
    """Descriptive metadata: implementation_state, startup, slot participation, actor identity."""
    raise NotImplementedError('TODO: implement')

def _check_startup(ident: str, item: Dict[str, Any], errors: List[Dict[str, str]]) -> None:
    raise NotImplementedError('TODO: implement')

def _check_slot_declarations(entities: Dict[str, Dict[str, Any]], errors: List[Dict[str, str]]) -> None:
    raise NotImplementedError('TODO: implement')

def _check_relations(registry: Dict[str, Any], entities: Dict[str, Dict[str, Any]], errors: List[Dict[str, str]]) -> None:
    raise NotImplementedError('TODO: implement')

def _known(entities: Dict[str, Dict[str, Any]], value: Any) -> bool:
    raise NotImplementedError('TODO: implement')

def _evidence_digest(root: Path, rel: str) -> Tuple[Optional[str], Optional[Tuple[str, str]]]:
    """(sha256, None) for a confined, bounded evidence file, else (None, (code, detail))."""
    raise NotImplementedError('TODO: implement')

def check_evidence_item(item: Any, root: Path, label: str, errors: List[Dict[str, str]]) -> None:
    """One evidence item: an artifact id, or {path, sha256} re-hashed against the repo file."""
    raise NotImplementedError('TODO: implement')

def check_evidence_list(items: Any, root: Path, label: str, errors: List[Dict[str, str]]) -> None:
    raise NotImplementedError('TODO: implement')

def _check_binding(item: Any, entities: Dict[str, Dict[str, Any]], root: Path, errors: List[Dict[str, str]]) -> bool:
    """True if this binding is well-formed and fully evidenced (only such bindings can be active)."""
    raise NotImplementedError('TODO: implement')

def _check_bindings(registry: Dict[str, Any], entities: Dict[str, Dict[str, Any]], root: Path, errors: List[Dict[str, str]], retired: Optional[Set[Tuple[str, str]]]=None) -> Dict[str, List[str]]:
    """Active hosts per slot. Two active bindings for one slot (or one host in two slots) are errors."""
    raise NotImplementedError('TODO: implement')

def _slot_table(entities: Dict[str, Dict[str, Any]], active: Dict[str, List[str]]) -> Dict[str, Dict[str, Any]]:
    raise NotImplementedError('TODO: implement')

def slot_host(validation: Dict[str, Any], slot: str) -> Optional[str]:
    """The slot's single active host, or None when the slot is unresolved or excluded."""
    raise NotImplementedError('TODO: implement')

def slot_summary(validation: Dict[str, Any]) -> Dict[str, str]:
    raise NotImplementedError('TODO: implement')

def envelope_hash(rec: Dict[str, Any]) -> str:
    raise NotImplementedError('TODO: implement')

def seal_receipt(rec: Dict[str, Any]) -> Dict[str, Any]:
    """Return rec with its envelope_sha256 set over every other field."""
    raise NotImplementedError('TODO: implement')

def subject_fingerprint(entity: Dict[str, Any], root: Path) -> Optional[Dict[str, Any]]:
    """Recompute {sources, revision} from the subject's declared source files; None if none declared."""
    raise NotImplementedError('TODO: implement')

@dataclass
class ReceiptContext:
    pass

def is_inactive_pair(slot: Any, host: Any, ctx: 'ReceiptContext') -> bool:
    """True when host was once bound to slot (retired binding) and is not the slot's active host."""
    raise NotImplementedError('TODO: implement')

def _read_receipt_lines(path: Path, errors: List[Dict[str, str]]) -> Optional[List[str]]:
    """Bounded, fail-closed read of one receipt file. None (with an error) if any bound fails."""
    raise NotImplementedError('TODO: implement')

def load_receipts(receipts_dir: Path, ctx: ReceiptContext, errors: List[Dict[str, str]]) -> List[Dict[str, Any]]:
    """Return the receipts that COUNT: structurally valid, current, independent, and status PASS."""
    raise NotImplementedError('TODO: implement')

def _check_receipt(rec: Any, path: Path, ctx: ReceiptContext, where: str, errors: List[Dict[str, str]]) -> None:
    raise NotImplementedError('TODO: implement')

def _hash_map_ok(value: Any) -> bool:
    raise NotImplementedError('TODO: implement')

def _check_receipt_shape(rec: Any, where: str, errors: List[Dict[str, str]]) -> bool:
    """Schema, required fields, envelope hash, status, hash maps. False if nothing else is checkable."""
    raise NotImplementedError('TODO: implement')

def _check_receipt_place(rec: Dict[str, Any], path: Path, ctx: ReceiptContext, where: str, errors: List[Dict[str, str]]) -> None:
    """Host, slot binding and subject."""
    raise NotImplementedError('TODO: implement')

def _check_receipt_actors(rec: Dict[str, Any], ctx: ReceiptContext, where: str, errors: List[Dict[str, str]]) -> None:
    """Builder and verifier must be registered actors with different canonical identities."""
    raise NotImplementedError('TODO: implement')

def _check_receipt_times(rec: Dict[str, Any], ctx: ReceiptContext, where: str, errors: List[Dict[str, str]]) -> None:
    raise NotImplementedError('TODO: implement')

def _check_receipt_currency(rec: Dict[str, Any], ctx: ReceiptContext, where: str, errors: List[Dict[str, str]]) -> None:
    """The receipt must describe the CURRENT registry and the subject's CURRENT declared sources."""
    raise NotImplementedError('TODO: implement')

def validate(registry_path: Path=..., receipts_dir: Optional[Path]=None, state_dir: Path=..., repo_root: Path=..., now: Optional[datetime]=None, max_age: timedelta=..., facts_fn: Callable[[], Dict[str, str]]=...) -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def _check_enrollment_against_registry(state_dir: Path, facts_fn: Callable[[], Dict[str, str]], entities: Dict[str, Dict[str, Any]], errors: List[Dict[str, str]], warnings: List[Dict[str, str]]) -> Optional[str]:
    """Absent enrollment is a warning; an enrolled host the registry does not know is an error."""
    raise NotImplementedError('TODO: implement')

def _evidence(subject: str, entities: Dict[str, Dict[str, Any]], receipts: List[Dict[str, Any]], drift: List[Dict[str, str]], connectivity: str, slot: Optional[str]=None, host: Optional[str]=None) -> Dict[str, bool]:
    """Which of the seven states have their own evidence. With a slot, only THAT host's receipts count."""
    raise NotImplementedError('TODO: implement')

def _missing(flags: Dict[str, bool]) -> List[str]:
    raise NotImplementedError('TODO: implement')

def _subject(ident: str, validation: Dict[str, Any], connectivity: str) -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def _blocker(member: str, subject: Dict[str, Any], validation: Dict[str, Any]) -> List[str]:
    raise NotImplementedError('TODO: implement')

def _list_states(missing: List[str]) -> str:
    raise NotImplementedError('TODO: implement')

def _product_blockers(ident: str, item: Dict[str, Any], subjects: Dict[str, Any], validation: Dict[str, Any], connectivity: str) -> List[str]:
    raise NotImplementedError('TODO: implement')

def project(validation: Dict[str, Any], connectivity: str=...) -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def _public(validation: Dict[str, Any]) -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def main(argv: Optional[List[str]]=None) -> int:
    raise NotImplementedError('TODO: implement')
