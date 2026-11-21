# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Generate three original Ruby project candidates; never execute or promote them.

The function, in-memory JSON API, and CLI scaffolds use Ruby's standard library
only. Output is candidate JSON on stdout; no files, training jobs, package
downloads, or network requests are created. All examples remain unverified and
not training-ready. Family-based holdouts do not change across seeds. Seeds
vary a few test constants; they do not create new underlying task families.

The SHA-256 is a reproducibility checksum, not proof of execution or origin.
Any later execution requires a separately reviewed example_host and evidence gate.
"""
import argparse
import hashlib
import json
import sys

def fingerprint(row):
    raise NotImplementedError('TODO: implement')

def candidates(seed=0):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
