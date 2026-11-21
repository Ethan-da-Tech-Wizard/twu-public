# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Search the first 2 MiB of an explicit GGUF file for listed text patterns.

This bounded byte-prefix heuristic does not parse GGUF metadata or Jinja templates,
validate structure, modify files, or provide security/download approval. A clean
prefix says nothing about unscanned bytes or patterns this tool does not recognize.
"""
import sys
import re
from pathlib import Path

def scan_file_text_for_injections(path: Path) -> list:
    raise NotImplementedError('TODO: implement')

def inspect_gguf(path: str) -> bool:
    """True means only magic present and no listed prefix patterns, never safe to load."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
