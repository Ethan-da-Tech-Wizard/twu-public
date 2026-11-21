# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""twu_claims: read-only view of who has claimed which repo paths, from Magi outbox packets.

A claim is only what a packet SAID. No packet means "no recorded claim" (unknown, not free).
Reads business/example_host/comms/agent*/outbox.jsonl only; never writes, sends, or touches the network.

  twu_claims.py list [--hours N] [--all] [--json]
  twu_claims.py check PATH... [--me N] [--hours N] [--json]     (exit 3: held by another seat)
  twu_claims.py overlaps [--hours N] [--json]

A packet counts as a claim when kind == "claim", or status == "running" with kind in
assignment/result (question/heartbeat/review never claim). It must name repo paths.
CLOSED when: the same packet_id later shows completed/blocked/reviewed, or a newer packet
from the same seat says "release" and names that path (per path; a release naming no path
closes nothing).
"""
import argparse
import collections
import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

def comms_dir(root=None):
    raise NotImplementedError('TODO: implement')

def norm(p):
    raise NotImplementedError('TODO: implement')

def extract_paths(text, root=None):
    """Conservative repo-relative paths: first directory must exist under root; bare names must exist."""
    raise NotImplementedError('TODO: implement')

def parse_ts(s):
    raise NotImplementedError('TODO: implement')

def seat_of(rec, fallback):
    raise NotImplementedError('TODO: implement')

def _tail_lines(path, stats):
    """Stream the newest MAX_TAIL_BYTES of a file; never hold more than MAX_LINE_BYTES+1 of one line.
    Returns (deque of lines, total_lines_seen, oversize_lines)."""
    raise NotImplementedError('TODO: implement')

def read_packets(comms):
    """Stream every outbox (newest bytes/lines only); return (packets, stats). Malformed lines are counted."""
    raise NotImplementedError('TODO: implement')

def is_claim(p):
    raise NotImplementedError('TODO: implement')

def covers(a, b):
    """True when path a equals b or a is a directory containing b (or the reverse)."""
    raise NotImplementedError('TODO: implement')

def snippet(text, path, width=160):
    raise NotImplementedError('TODO: implement')

def released_paths(text, root=None):
    """Paths a packet actually RELEASES: positive, past/imperative release clause, exact paths named in that sentence."""
    raise NotImplementedError('TODO: implement')

def build_claims(packets, now, hours, root=None, stats=None):
    raise NotImplementedError('TODO: implement')

def active(claims):
    raise NotImplementedError('TODO: implement')

def find_overlaps(claims):
    raise NotImplementedError('TODO: implement')

def norm_query(p, root=None):
    raise NotImplementedError('TODO: implement')

def _warnings(stats):
    raise NotImplementedError('TODO: implement')

def fmt(c):
    raise NotImplementedError('TODO: implement')

def main(argv=None, now=None, root=None):
    raise NotImplementedError('TODO: implement')
