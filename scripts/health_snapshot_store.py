# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Host-scoped health history paths and strictly attributed local observations.

The legacy shared snapshots.jsonl remains historical evidence. Neither its
filename nor app-behavior paths prove which host produced a row.
"""
import json
import platform
import re
from pathlib import Path

def normalize_host(host=None):
    raise NotImplementedError('TODO: implement')

def snapshot_path(repo, host=None):
    raise NotImplementedError('TODO: implement')

def latest_local_snapshot(path, host=None):
    """Read a bounded tail of one stream; accept only explicit matching hosts.

    Legacy shared filenames, symlinks, malformed JSON and hostless/foreign rows
    never establish local health. Missing history remains unknown.
    """
    raise NotImplementedError('TODO: implement')
