# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Build a cleaned TRAINING copy of the central dataset. The original file is never changed.

Drops: records that copy the held-out test files (exact or digits-only different), schema errors (empty responses),
bad DPO pairs, secrets, and template repeats (keeps the first DPO pair for each distinct chosen/rejected text once
digits and ids are ignored). Then runs dataset_certify.py on the result; the copy is only usable if that PASSES.

  build_clean_train_set.py            write private/.../central_dataset/train_clean.jsonl and print the before/after counts
"""
import json
import os
import re
import sys
import tempfile
from pathlib import Path
import dataset_certify as dc

def is_junk(d):
    raise NotImplementedError('TODO: implement')

def build(data=..., holdouts=..., out=None):
    raise NotImplementedError('TODO: implement')
