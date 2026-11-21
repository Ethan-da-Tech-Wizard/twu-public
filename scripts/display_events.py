# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Read the display event log written by display_external_only_guard.py (read-only).

  python3 scripts/display_events.py [--tail N] [--json]     # newest events, newest last
  python3 scripts/display_events.py --summary [--json]       # counts by event and by month
Reads data/example_host/display_events/*.jsonl and *.jsonl.gz.
"""
import argparse
import gzip
import json
import sys
from collections import Counter
from pathlib import Path

def load(log_dir=None):
    raise NotImplementedError('TODO: implement')

def summary(rows):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
