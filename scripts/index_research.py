# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""
scripts/index_research.py — Automated Research Whitepaper Catalog & Database

Catalogs and hashes all 36+ research whitepapers in business/example_host/documentation/research/
into data/example_host/research_catalog.json with SHA-256 fingerprints, domains, and summaries.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

def sha256_file(path: Path) -> str:
    raise NotImplementedError('TODO: implement')

def classify_domain(filename: str) -> str:
    raise NotImplementedError('TODO: implement')

def build_catalog():
    raise NotImplementedError('TODO: implement')
