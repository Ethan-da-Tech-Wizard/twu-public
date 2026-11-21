# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
from __future__ import annotations
import argparse
import fnmatch
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

def ignored_globs(root: Path) -> List[str]:
    raise NotImplementedError('TODO: implement')

def line_count(path: Path, cache: Dict[Path, int]) -> int:
    raise NotImplementedError('TODO: implement')

def resolve(root: Path, ref: str) -> Optional[Path]:
    """Find the file a reference means: repo-relative first, then under scripts/ (docs often cite bare script names)."""
    raise NotImplementedError('TODO: implement')

def scan(root: Path) -> List[Tuple[str, int, str, str]]:
    """Return (doc, line_no, reference, reason) for every broken citation."""
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
