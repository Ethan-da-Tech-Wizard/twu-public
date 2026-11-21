# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Mac-side INBOUND validator for Ron-messenger evidence cards (schema ron.evidence-card.v1).

Ron is the messenger between Enki (our fleet) and a friend's completely different system. This module
validates a card that ARRIVED from that external system. A card is data, never a command: this code
never executes, installs, fetches, or adopts anything. It validates the card's shape, freshness, and
privacy, then assigns one receiver state. The strongest disposition it can assign is
`accepted_for_independent_recheck` — a card is NEVER marked verified or adopted here. Adoption happens
only after Enki's own independent recheck on our fleet (owned by Magi 1).

Scope boundary (per M1-ENKI-RON-FEDERATION-182): local fixture files only. No network, shared git,
account, remote shell, or delivery. Transport remains NOT_RUN until an explicit external scope is set.

  python3 scripts/ron_inbound.py <card.json>    # validate one local card file, print its disposition
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
import sys
from pathlib import Path
import ron_update

def _parse_ts(value):
    raise NotImplementedError('TODO: implement')

def _private_hit(text):
    raise NotImplementedError('TODO: implement')

def validate_card(card, now=None):
    """Return (receiver_state, reason). A malformed/expired/private/unknown card is 'rejected'.

    A clean card is classified into a non-adopting state; it is never trusted as verified here.
    """
    raise NotImplementedError('TODO: implement')

def adapt_raw_card(raw):
    """Translate a raw inbound payload from Ron's system into our neutral ron.evidence-card.v1 shape.

    We do not yet know what Ron is or what format it emits, and that is fine: this is the single seam
    where that adaptation lives. By default it is the identity, assuming the sender already speaks the
    neutral card. When we see a real Ron sample, the Ron-specific field mapping goes HERE and nowhere
    else, so validate_card and every safety guarantee stay unchanged no matter what Ron turns out to be.
    """
    raise NotImplementedError('TODO: implement')

def process_file(path, now=None, adapter=...):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
