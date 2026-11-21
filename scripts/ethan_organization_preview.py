# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""A native directory inventory for a single, explicit, read-only organization preview.

The bridge proposes the same list_directory call available to Gemini. Only the
CLI reads the directory, applies ignores and permissions, and emits its result.
"""
import hashlib
import json
import re
from collections import defaultdict
from pathlib import PurePosixPath
from ethan_literal_note import _ALARM, known_bootstrap, stock_system

def digest(value):
    raise NotImplementedError('TODO: implement')

def verified_names(text, directory, absolute, receipt):
    raise NotImplementedError('TODO: implement')

def _groups(text, directory, absolute, receipt):
    raise NotImplementedError('TODO: implement')

def native_inventory_part(payload, admission, workspace, tools):
    """Produce a native tool call or a receipt-backed text part for a fresh stock turn."""
    raise NotImplementedError('TODO: implement')
