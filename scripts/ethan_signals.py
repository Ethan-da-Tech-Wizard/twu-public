# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Eyes: Ethan signal watcher. Reads failure sources READ-ONLY, appends normalized
events to data/watch/events.<host>.jsonl. Event-driven: runs only when called.

Commands: scan | tail [N] | summary | rebuild   (tail/summary: --all-hosts)
Stdlib only (python 3.9 ok). No network, no model, no timers.

Event: {ts, host, source, kind, code, summary, evidence_path, sig}
ts is ISO8601 or null when the source carries no wall-clock time (never invented).
Never stores user message text: Gemini chats yield only error class + tool name.
Source formats: ethan_exits.log is written by the launcher (not yet present when this
was built); accepted lines contain "code=N" and "seconds=S" (or JSON with code/seconds/ts).
"""
import glob
import hashlib
import json
import os
import re
import socket
import stat
import sys
from collections import Counter
from datetime import datetime

def paths():
    raise NotImplementedError('TODO: implement')

def is_regular(path):
    """Regular file, not a symlink: a FIFO/device would hang or lie, a symlink could point outside."""
    raise NotImplementedError('TODO: implement')

def open_regular(path, mode=...):
    """Open a regular file for reading with O_NONBLOCK|O_NOFOLLOW where available; OSError otherwise."""
    raise NotImplementedError('TODO: implement')

def warn_skip(path):
    raise NotImplementedError('TODO: implement')

def safe_word(v):
    """Keep a chat-derived identifier only if it is short, plain and not secret-shaped; else '?'."""
    raise NotImplementedError('TODO: implement')

def clean_line(line, fixed):
    """Raw log lines are stored only when short printable ASCII; otherwise a fixed phrase."""
    raise NotImplementedError('TODO: implement')

def sig_of(source, kind, code, summary):
    raise NotImplementedError('TODO: implement')

def mk(source, kind, code, summary, evidence, ts=None):
    raise NotImplementedError('TODO: implement')

def _fp(path):
    raise NotImplementedError('TODO: implement')

def stream(path, st, first_cap=...):
    """Yield (line_text) of new complete lines; update st in place (offset, fp)."""
    raise NotImplementedError('TODO: implement')

def _stream_open(f, path, st, size, first_cap):
    raise NotImplementedError('TODO: implement')

def src_exits(st):
    raise NotImplementedError('TODO: implement')

def src_bridge(st):
    raise NotImplementedError('TODO: implement')

def platform_of(model):
    raise NotImplementedError('TODO: implement')

def src_llama(st):
    raise NotImplementedError('TODO: implement')

def _gem_files():
    raise NotImplementedError('TODO: implement')

def src_gemini(state):
    raise NotImplementedError('TODO: implement')

def _gem_line(line, p):
    raise NotImplementedError('TODO: implement')

def src_hooks(state):
    raise NotImplementedError('TODO: implement')

def src_crash(state):
    raise NotImplementedError('TODO: implement')

def load_state():
    raise NotImplementedError('TODO: implement')

def scan():
    raise NotImplementedError('TODO: implement')

def read_events(all_hosts=False):
    raise NotImplementedError('TODO: implement')

def cmd_scan():
    raise NotImplementedError('TODO: implement')

def cmd_tail(n, all_hosts):
    raise NotImplementedError('TODO: implement')

def cmd_summary(all_hosts):
    raise NotImplementedError('TODO: implement')

def cmd_rebuild():
    raise NotImplementedError('TODO: implement')

def main(argv):
    raise NotImplementedError('TODO: implement')
