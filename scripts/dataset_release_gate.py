# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Read-only, fail-closed dataset release audit. Receipt claims are not attestation."""
import argparse
import hashlib
import json
from pathlib import Path

def digest(path):
    raise NotImplementedError('TODO: implement')

def confined(root, name):
    raise NotImplementedError('TODO: implement')

def rows(path):
    raise NotImplementedError('TODO: implement')

def row_digest(row):
    raise NotImplementedError('TODO: implement')

def valid_messages(messages):
    raise NotImplementedError('TODO: implement')

def audit(root, requirements, manifest):
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
