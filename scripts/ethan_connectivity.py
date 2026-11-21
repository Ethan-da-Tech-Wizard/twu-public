# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Read the existing local Syncthing link state without probing the Internet."""
from __future__ import annotations
import json
import os
import subprocess
import sys
import urllib.request
import xml.etree.ElementTree as ET

def _config_candidates():
    raise NotImplementedError('TODO: implement')

def _run(runner, cmd):
    raise NotImplementedError('TODO: implement')

def _pid_from(text):
    raise NotImplementedError('TODO: implement')

def service_state(runner=...):
    """Return running | stopped | unavailable-tool | unknown for the local Syncthing service."""
    raise NotImplementedError('TODO: implement')

def _api_key():
    """Return (key, reason). The key is never put in any message."""
    raise NotImplementedError('TODO: implement')

def rest_health(opener=...):
    """Return {"health": connected|disconnected|unknown, "reason": short text} from the local REST API."""
    raise NotImplementedError('TODO: implement')

def sync_link(runner=..., sync_module=None):
    """Return online/offline/unknown for workspace sync, never general Internet state.

    Extra keys: "service" (running|stopped|unavailable-tool|unknown) and
    "health" (connected|disconnected|unknown), reported separately.
    """
    raise NotImplementedError('TODO: implement')

def transition(previous, current):
    """Return one human notification only for a meaningful sync-link transition."""
    raise NotImplementedError('TODO: implement')
