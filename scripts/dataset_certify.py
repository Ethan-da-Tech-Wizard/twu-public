# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""dataset_certify.py — independent, read-only certifier for the central training dataset. Zero model, stdlib only.

  python3 scripts/dataset_certify.py [--data FILE] [--holdout FILE ...] [--out FILE]

Shares no code with sovereign_dataset_hub.py, so it can disagree with it. Streams the file line by line and checks:
  schema        every line is JSON with the fields its kind needs
  pair sanity   DPO chosen/rejected present, different, not the prompt, not placeholder or empty, not cut at 2000 chars
  secrets       its own patterns (keys, tokens, private keys, 9-digit tax-style ids, long hex/base64 secrets near 'key')
  contamination exact training text (whitespace/case only) also present in a held-out file = FAIL;
                same text after stripping digits and ids = reported as near_duplicate_of_holdout (a warning: it can inflate scores)
  effective     distinct DPO pairs after stripping digits and ids (what training can really learn from)
  verified      records marked verified must name a seat or tool (a provenance label, not proof of execution)
Writes a certificate JSON with the sha256 of the data file. PASS needs zero schema errors, zero secrets, zero
contamination, bad pairs and verified-without-source. A nonempty dataset and readable, nonempty,
valid holdouts are required. Duplicates and templated pairs are reported, never hidden.
"""
import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
import time

def valid_messages(messages):
    raise NotImplementedError('TODO: implement')

def norm(s):
    raise NotImplementedError('TODO: implement')

def exact(s):
    raise NotImplementedError('TODO: implement')

def h(s):
    raise NotImplementedError('TODO: implement')

def text_of(d):
    raise NotImplementedError('TODO: implement')

def fields_valid(d):
    raise NotImplementedError('TODO: implement')

def comparison_texts(d):
    raise NotImplementedError('TODO: implement')

def holdout_sets(paths):
    raise NotImplementedError('TODO: implement')

def certify(data, holdouts):
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
