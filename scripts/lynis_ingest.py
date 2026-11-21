# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/lynis_ingest.py - turn a Lynis report into a small trend summary (independent auditor, read-only input).

Lynis (external GPL auditor, never copied or linked) runs as root weekly via system/example_host/lynis/; the root side
publishes only /var/lib/twu/lynis/lynis-report.dat.  This tool reads that file (key=value lines: hardening_index=,
warning[]=ID|text|..., suggestion[]=ID|text|..., lynis_tests_done=) and writes exactly two outputs:
  data/health/lynis_summary.json   {checked, source, hardening_index, tests, warnings, suggestions, new_since_last, resolved_since_last}
  data/health/lynis_history.jsonl  one trend line per ingest
  python3 scripts/lynis_ingest.py [--report FILE] [--from-text FILE] [--json]
Exit 1 if any warning or the index dropped >=3 since the last summary.  --from-text parses pasted console output.
"""
from __future__ import annotations
import argparse
import json
import re
import sys
import time
from pathlib import Path

def parse_report(text):
    raise NotImplementedError('TODO: implement')

def parse_console(text):
    raise NotImplementedError('TODO: implement')

def _int(v):
    raise NotImplementedError('TODO: implement')

def _bag(ids):
    raise NotImplementedError('TODO: implement')

def build(parsed, prev, source, now=None):
    """Summary dict; new/resolved compare unique suggestion+warning ids with the previous summary."""
    raise NotImplementedError('TODO: implement')

def verdict(summary, prev):
    raise NotImplementedError('TODO: implement')

def ingest(report_text, source, root=..., console=False, now=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
