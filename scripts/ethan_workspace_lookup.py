# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Send an explicit local citation request through the CLI's declared read-only tool."""
import hashlib
from contextlib import closing
from pathlib import Path
import re
import sqlite3
import time
from ethan_literal_note import _ALARM, fresh_context

def search_terms(prompt):
    raise NotImplementedError('TODO: implement')

def _public_doc(rel, know):
    raise NotImplementedError('TODO: implement')

def rolling_lookup(query, max_tokens, *, strict=False):
    """Use the on-device rolling index for ranking only. Return verified public text.

    The shared corpus has wider scope than Ethan's docs reader. Only candidate
    coordinates and hashes cross that boundary; never trust stored chunk text.
    """
    raise NotImplementedError('TODO: implement')

def _citation(data, terms, include_line=False):
    """Derive a concrete matching line, not just the first line of the FTS chunk."""
    raise NotImplementedError('TODO: implement')

def native_lookup_part(payload, admission, tools, unpack):
    raise NotImplementedError('TODO: implement')
