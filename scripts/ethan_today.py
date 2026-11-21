# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""ethan_today.py: write TODAY.md, one plain page for Ethan (no model, no network, reads existing files only).

  python3 scripts/ethan_today.py          # writes ~/Desktop/TODAY.md (outside the repo) or data/health/TODAY.md, and prints it
Decisions waiting on Ethan live in data/health/decisions.json: a list of {"id","text"}; remove an entry when it is settled.
"""
import glob
import json
import os
import shutil
import sys
import time

def load(path, default):
    raise NotImplementedError('TODO: implement')

def conflicts(root):
    raise NotImplementedError('TODO: implement')

def build(root=...):
    raise NotImplementedError('TODO: implement')

def out_path():
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
