# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""The interactive Ethan CLI front door for Enki; never starts a model itself."""
from __future__ import annotations
import json
from pathlib import Path
import select
import sys
import enki_station as enki
import ethan_connectivity
import ethan_offline

def render_status(output=..., connectivity_fn=...):
    raise NotImplementedError('TODO: implement')

def foreground_request(previous_link, connectivity_fn, poll_seconds=2.0):
    """Read one terminal request while visibly reporting a sync-link transition.

    This runs only while the foreground Ethan window waits for input. It starts
    no thread, timer service, or background daemon; platforms without a
    selectable terminal fall back to normal input and check at the next prompt.
    """
    raise NotImplementedError('TODO: implement')

def run(input_fn=..., output=..., connectivity_fn=...):
    raise NotImplementedError('TODO: implement')
