# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""ethan perf: evidence layer for local-model speed. Offline, stdlib only, no timers.

  parse   read data/daemon_logs/llama_server.log, append new per-request records
          to data/daemon_logs/ethan_perf.jsonl (idempotent, rotation-safe)
  report  [N]  (Mac/metal records only; --cuda or --all to change) plain summary of the last N requests (default 20) + one-line verdict
  check   exit 1 and print one line per failed threshold (also parses first)

Thresholds: data/ethan_perf_thresholds.json overrides the defaults below.
Everything is rebuildable: delete ethan_perf.jsonl and ethan_perf.state.json, run parse.
The llama-server log stamps lines M.SS.mmm.uuu since that server process started, so
absolute time is only an estimate (ts_est, from the log file's mtime, last session only).
The bridge log has no per-request timing fields, so it is not used.
"""
import hashlib
import json
import os
import re
import stat
import sys
import time

def is_regular(path):
    """True only for a regular file that is not a symlink (a FIFO or device would hang or lie)."""
    raise NotImplementedError('TODO: implement')

def open_regular(path):
    """Binary read handle for a regular file only; O_NONBLOCK|O_NOFOLLOW where available. Raises IOError."""
    raise NotImplementedError('TODO: implement')

def rel_s(m):
    raise NotImplementedError('TODO: implement')

def load_state():
    raise NotImplementedError('TODO: implement')

def head_hash(path, n):
    raise NotImplementedError('TODO: implement')

def device_of_path(path):
    raise NotImplementedError('TODO: implement')

def parse_lines(lines, src, sess=0, cur=None, sel=None, dev=None):
    """Pure parser. Returns (records, sess, cur, sel, dev). dev is cuda, metal or None, taken from
    the model path on the loading-model line (/Users = Mac metal; /home or /mnt = Linux cuda) or CUDA lines."""
    raise NotImplementedError('TODO: implement')

def _one_line(line, src, recs, cur, sel, dev, sess):
    """Handle one log line; returns the updated (cur, sel, dev, sess). Appends finished records to recs."""
    raise NotImplementedError('TODO: implement')

def read_records():
    raise NotImplementedError('TODO: implement')

def do_parse(quiet=False):
    raise NotImplementedError('TODO: implement')

def thresholds():
    raise NotImplementedError('TODO: implement')

def verdict_for(r, t):
    """List of plain failure lines for one record."""
    raise NotImplementedError('TODO: implement')

def select(recs, dev):
    """Mac (metal) records by default. dev: metal (default), cuda, or all."""
    raise NotImplementedError('TODO: implement')

def note_dev(allrecs, dev):
    raise NotImplementedError('TODO: implement')

def mark_first(recs):
    raise NotImplementedError('TODO: implement')

def do_report(n, dev=...):
    raise NotImplementedError('TODO: implement')

def do_check(dev=...):
    raise NotImplementedError('TODO: implement')

def main(argv):
    raise NotImplementedError('TODO: implement')
