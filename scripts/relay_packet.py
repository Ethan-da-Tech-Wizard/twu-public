# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Build one paste-ready, scrubbed packet for DeepSeek from Claude's reply. Stdlib only, offline, read-only.

Never writes anything (data/relay_work/ is the only place any caller may write)."""
import importlib
import json
import sys
from pathlib import Path

class RelayScrubMissing(RuntimeError):
    """The outbound scrubber is not importable; fail closed."""

def _load_scrubber():
    raise NotImplementedError('TODO: implement')

def _import_local(name, root):
    """Import scripts/<name>.py from the given root (read-only)."""
    raise NotImplementedError('TODO: implement')

def _stat_incidents(root):
    raise NotImplementedError('TODO: implement')

def _stat_watch(root):
    raise NotImplementedError('TODO: implement')

def _stat_index(root):
    raise NotImplementedError('TODO: implement')

def gather_stats(root):
    raise NotImplementedError('TODO: implement')

def _read_round(root):
    raise NotImplementedError('TODO: implement')

def _cut(text, limit):
    """Cut text to <= limit chars at a word boundary; return (text, omitted_chars)."""
    raise NotImplementedError('TODO: implement')

def build_packet(claude_text, root, max_chars=12000, round_no=None):
    raise NotImplementedError('TODO: implement')
