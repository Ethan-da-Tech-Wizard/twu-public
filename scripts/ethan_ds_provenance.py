# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Provenance registry checker for external dataset sources (ethan.provenance.v1).

  python3 -B scripts/ethan_ds_provenance.py check [--registry PATH] [--decisions PATH] [--inspections PATH]
  python3 -B scripts/ethan_ds_provenance.py --list-training-inputs [--registry PATH]
  python3 -B scripts/ethan_ds_provenance.py manifest <dir>      (prints the sha256 manifest hash of a directory)

`check` re-verifies every source: licence on the allowlist (base list plus ALLOWED decisions in
data/example_host/licences/ethan_licence_decisions.json), a quoted licence line and file, a revision, an inspector verdict
PASS (and, if the inspections log is present, a matching PASS record), an existing local path, and a recomputed manifest
hash equal to the registered one. eval_holdout sources must never be in any training input list.
Sources under "quarantined" (inspector verdict not PASS) are never used; they are only checked to not be training inputs.
Downloaded files are only read as bytes (never imported or executed).
"""
import argparse
import hashlib
import json
import os
import re
import sys

def manifest_hash(path):
    """sha256 over sorted 'relpath<TAB>filesha256' lines for every regular file, skipping .git."""
    raise NotImplementedError('TODO: implement')

def allowed_licences(decisions_path):
    raise NotImplementedError('TODO: implement')

def licence_ok(spdx, allowed):
    """An 'A OR B' expression is fine if any alternative is allowed; 'AND' needs all."""
    raise NotImplementedError('TODO: implement')

def load_registry(path):
    raise NotImplementedError('TODO: implement')

def training_inputs(reg):
    raise NotImplementedError('TODO: implement')

def check_inspection(report_id, verdict, path):
    raise NotImplementedError('TODO: implement')

def check(reg_path, decisions_path, inspections_path):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
