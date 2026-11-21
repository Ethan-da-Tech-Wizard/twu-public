# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Export the public self-audit file website/claims.json from the claim registry.

Every claim registered for a document under website/ is re-evaluated against company records (scripts/claim_check.py)
and written with a friendly source label. Unverified claims are included and labeled, never hidden. Internal file
paths and probe details are NOT published; only the label. Run after editing the site, then publish website/claims.json.

  python3 scripts/website_claims_export.py          # write website/claims.json
  python3 scripts/website_claims_export.py --check  # exit 1 if claims.json is stale or any claim failed
"""
from __future__ import annotations
import json
import sys
from datetime import date
from pathlib import Path
import claim_check as cc
import re

def trivial(snippet: str) -> bool:
    """Years, status codes, dates and bare references pad a count without telling a reader anything."""
    raise NotImplementedError('TODO: implement')

def label(claim: dict) -> str:
    raise NotImplementedError('TODO: implement')

def build(root: Path=...) -> dict:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
