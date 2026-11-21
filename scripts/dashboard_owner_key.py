# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Verify a typed owner access key against the dashboard's private runtime key file."""
from __future__ import annotations
import hmac
import os
import re
import stat
from pathlib import Path

def _runtime_key_path(root) -> Path:
    raise NotImplementedError('TODO: implement')

def verify(supplied, root) -> bool:
    """True only when `supplied` is exactly the owner's access key for the workspace `root`.

    Args: supplied (the typed key, any type), root (server-owned workspace root).
    Returns bool. Any problem (missing/unsafe key file, wrong shape, mismatch) is False, never an exception.
    """
    raise NotImplementedError('TODO: implement')
