# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Local-only OUTBOUND emitter for Ron-messenger evidence cards (schema ron.evidence-card.v1).

This prepares a card that WE could one day share with Ron's (unknown, different) system. It is the
matching lane to ron_inbound.py. Hard boundaries (per M1-RON-OUTBOUND-OWNER-187):
  * No transport, delivery, shared repo, network, provider, or service. A card is an EXPORT CANDIDATE,
    written to a local candidates folder. It is NEVER sent. Actual sharing needs explicit Ethan
    approval plus a real Ron sample plus a transport scope, none of which exist yet.
  * No automatic selection: the human supplies exactly what to share. This tool never scans the system
    and decides on its own what leaves.
  * Privacy fail-closed: if the content carries any private pattern (path, email, the fleet passphrase)
    the card is refused, not scrubbed-and-sent.
  * Every emitted card must pass our own ron_inbound validator (round-trip), so what we send is exactly
    what we would accept. The outbound adapter seam mirrors the inbound one for a future Ron format.

  python3 scripts/ron_outbound.py --summary "..." --classification READ --status NOT_RUN       [--artifact label:/path/to/file ...]
"""
from __future__ import annotations
import argparse
from datetime import datetime, timedelta, timezone
import hashlib
import json
import sys
from pathlib import Path
import ron_update
import ron_inbound

class RefuseToEmit(Exception):
    """Raised to fail closed rather than emit an unsafe or malformed card."""

def _private_hit(text):
    raise NotImplementedError('TODO: implement')

def adapt_to_ron(card):
    """Translate our neutral card into Ron's format. Identity by default: we do not know Ron yet.

    This mirrors ron_inbound.adapt_raw_card. When we learn Ron's real format, the outbound mapping goes
    HERE only, so the card contract and every safety check above stay unchanged whatever Ron turns out to be.
    """
    raise NotImplementedError('TODO: implement')

def build_card(summary, classification, status, artifacts=None, household=..., fingerprint=..., now=None):
    """Build one export-candidate card from EXPLICITLY SUPPLIED inputs. Fails closed on anything unsafe."""
    raise NotImplementedError('TODO: implement')

def write_candidate(card):
    """Write the card as a LOCAL export candidate. It is not sent; there is no transport."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
