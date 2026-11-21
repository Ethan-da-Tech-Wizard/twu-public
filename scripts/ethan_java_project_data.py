# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Original Java project candidates, NOT a training or publication pipeline.

Prints three deterministic function/API/CLI project candidates as JSON. By
default none are executed or verified. --verify uses the existing language
verifier only when its bubblewrap isolation probe succeeds; it refuses an
unexample_hosted fallback. Even a successful result is candidate evidence, not
permission to train, publish, or claim broad Java competence. Family-based
splits stay fixed across seeds. The generated code uses only the Java standard
library; no package download or network is requested. There are three template
families; seeds vary a few checks, not the underlying task or source diversity.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

def artifact_sha256(candidate):
    raise NotImplementedError('TODO: implement')

def candidates(seed=0):
    raise NotImplementedError('TODO: implement')

def verify_candidate(candidate, adapter=None):
    """Record bounded evidence only; never permit an unexample_hosted execution.

    ``adapter`` is an injectable test seam, not authenticated execution
    provenance. No in-band label or reproducibility hash proves execution;
    downstream use requires independently bound evidence and review.
    """
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
