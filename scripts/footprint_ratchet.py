# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""footprint_ratchet.py — deterministic, zero-model footprint tracker for ONE machine (run on demand or once a day).

  python3 scripts/footprint_ratchet.py record     # append today's numbers to data/health/footprint.<box>.jsonl
  python3 scripts/footprint_ratchet.py check      # compare the latest record to the best earlier one; exit 1 on a regression
  python3 scripts/footprint_ratchet.py show       # print the latest record

Measures only: free disk, size of the known waste categories (Syncthing old versions, package caches, local model
files, node_modules under the repo), count of launchd/systemd jobs we own, and the resident memory of our own
processes. Per-machine file, so Syncthing never sees two writers. A category counts as a regression when it grew by
more than max(100 MB, 10%) over its best earlier value. It reports; it deletes nothing. Stdlib only.
"""
import json
import os
import platform
import shutil
import subprocess
import sys
import time

def du(path):
    raise NotImplementedError('TODO: implement')

def our_rss():
    raise NotImplementedError('TODO: implement')

def jobs():
    raise NotImplementedError('TODO: implement')

def measure():
    raise NotImplementedError('TODO: implement')

def load():
    raise NotImplementedError('TODO: implement')

def regressions(records):
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
