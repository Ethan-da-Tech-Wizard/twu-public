# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Host-scoped rescue writes and lossless read union of legacy/host histories.

Unknown historical host identity stays unknown. Filename scope selects files;
it never supplies missing row metadata. The complete row identifies an event;
shared copies deduplicate using maximum occurrence multiplicity per source.
"""
import collections
import datetime
import json
from pathlib import Path
import re
from health_snapshot_store import normalize_host

def rescue_log_path(repo, host=None):
    raise NotImplementedError('TODO: implement')

def rescue_paths(path):
    """An explicit custom file reads alone; the legacy base selects its union."""
    raise NotImplementedError('TODO: implement')

def rescue_records(path):
    """Return (source, zero-based line, original text), preserving provenance.

    Malformed lines remain available to consumers that count input failures.
    Reads never rewrite, relabel, move or delete source histories.
    """
    raise NotImplementedError('TODO: implement')

def rescue_rows(path):
    raise NotImplementedError('TODO: implement')
