# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Deterministic claim checker for grant, resume and outreach text.

Every factual claim in a governed document must be registered in ``grants/claims.json`` with a
snippet (exact text as it appears in the document) and probes that read workspace records.
No model calls and no network: each probe is a pure function of files in this workspace.

Claim results
  VERIFIED     every probe passed (kind "measured": a count/metric read from data; "recorded": the
               workspace record says so, which is attributed evidence rather than a fresh measurement)
  FAILED       a probe ran and the record disagrees with the claim text: the claim may be false
  UNVERIFIED   no probe exists (kind "manual"), or a probe's source file is absent: cannot be confirmed
  PLAN         forward-looking target or proposal, not a claim of fact (kind "plan")
  STALE        the registered snippet no longer appears in the document: registry and text drifted
  SKIP_REMOTE_HOST  every probe points at out-of-band evidence (tax, formation, banking records) that is kept
               off this machine by design; it is checked only on the designated holder host and only as a
               path-exists / file-count fact (file contents are never read). Never counts as VERIFIED.
  UNREGISTERED a number in the document that no registered snippet covers (an unchecked claim)

Exit 1 on FAILED or STALE. ``--strict`` also exits 1 on UNVERIFIED or UNREGISTERED, for use as a
pre-submission gate. Usage:
  python3 scripts/claim_check.py            # all governed documents
  python3 scripts/claim_check.py --strict   # submission gate
  python3 scripts/claim_check.py --json
  python3 scripts/claim_check.py --init-baseline | --shrink-baseline

Coverage: ``outbound_globs`` in the registry lists documents that leave the building (grant answers,
outreach drafts, resume source). A new outbound document that carries numbers and is not governed
fails the check; documents already in ``data/claims_baseline.json`` only warn, and the baseline may
only shrink.
"""
from __future__ import annotations
import argparse
import glob
import json
import os
import posixpath
import re
import socket
import sys
from pathlib import Path

def this_host(root: Path=None):
    """Manifest name of this machine (TWU_FLEET_HOST or hostname matched to fleet_roles names/aliases), or None if unknown."""
    raise NotImplementedError('TODO: implement')

def out_of_band(rel) -> bool:
    """True if a registry path points into out-of-band evidence. Decided on the TEXT of the path only (lexically
    normalised, so data/../Company_Documents/x counts); nothing is stat()ed, opened or globbed."""
    raise NotImplementedError('TODO: implement')

def probe_paths(probe: dict) -> list:
    raise NotImplementedError('TODO: implement')

def presence_only(probe: dict, root: Path) -> tuple:
    """Holder host only: boolean existence / file count. File contents are never read, logged or reported."""
    raise NotImplementedError('TODO: implement')

def norm(text: str) -> str:
    raise NotImplementedError('TODO: implement')

def doc_text(path: Path) -> str:
    """Text of a governed document. For .html files this is the visible text (no tags, styles, scripts or SVG)."""
    raise NotImplementedError('TODO: implement')

def load_registry(root: Path=...) -> dict:
    raise NotImplementedError('TODO: implement')

def _json_at(data, path: str):
    raise NotImplementedError('TODO: implement')

def run_probe(probe: dict, root: Path) -> tuple[str, str]:
    """Return (PASS|FAIL|MISSING|SKIP_REMOTE_HOST, detail). Never raises on a bad record."""
    raise NotImplementedError('TODO: implement')

def evaluate(claim: dict, doc_text: str, root: Path) -> dict:
    raise NotImplementedError('TODO: implement')

def unregistered_numbers(doc_text: str, snippets: list[str]) -> list[str]:
    raise NotImplementedError('TODO: implement')

def outbound_documents(root: Path, registry: dict) -> list[str]:
    """Documents that leave the building or feed ones that do, and carry at least one number."""
    raise NotImplementedError('TODO: implement')

def coverage(root: Path, registry: dict) -> dict:
    """Shrink-only gate: a new ungoverned outbound document is a problem; legacy ones are warnings."""
    raise NotImplementedError('TODO: implement')

def shrink_baseline(root: Path=...) -> int:
    """Rewrite the baseline without governed or deleted documents. Never adds an entry."""
    raise NotImplementedError('TODO: implement')

def init_baseline(root: Path=...) -> int:
    """One-time creation of the baseline from the current state. Refuses to overwrite."""
    raise NotImplementedError('TODO: implement')

def check(root: Path=...) -> dict:
    raise NotImplementedError('TODO: implement')

def exit_code(report: dict, strict: bool=False) -> int:
    raise NotImplementedError('TODO: implement')

def render(report: dict) -> str:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
