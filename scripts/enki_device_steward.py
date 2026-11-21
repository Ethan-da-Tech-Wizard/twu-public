# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Emit this host's Enki device-steward receipt (schema enki.device-steward.v1).

Per the Enki device-steward contract, each device publishes a fresh, host-scoped, metadata-only
receipt that Enki (owned by Magi 1) reads and reconciles into one decision brief. This is the Mac-side
PRODUCER only: it reuses the existing fleet-needs evidence this host already generates and translates
it into the agreed steward schema. It starts no new collector, service, or model, and it writes only
its own receipt, atomically.

Privacy: every check note is a fixed, bounded phrase. No paths, usernames, URLs, process content,
credentials, prompts, or raw diagnostics are ever emitted.

  python3 scripts/enki_device_steward.py            # write data/example_host/enki/stewards/<host>.json
  python3 scripts/enki_device_steward.py --stdout    # also print the receipt
"""
from __future__ import annotations
import argparse
from datetime import datetime, timedelta, timezone
import json
import sys
from pathlib import Path
import fleet_needs_emit as fn

def _risk_categories(receipt):
    """Categories whose measured metric indicates an actionable risk (no secret values)."""
    raise NotImplementedError('TODO: implement')

def build(now=None):
    raise NotImplementedError('TODO: implement')

def write_receipt(now=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
