# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""incident_checks.py - named read-only checks used as `verified_by` commands in data/incidents/signatures.json.

verified_by commands run WITHOUT a shell and may only call an allow-listed program (see ethan_incidents.py), so
checks that used to need pipes, `!`, `&&` or `python3 -c` live here as plain named functions:
    python3 scripts/incident_checks.py <name> [args...]       exit 0 = the preventer works
Every check only reads. Stdlib only, offline."""
import contextlib
import io
import os
import re
import subprocess
import sys

def _read(rel):
    raise NotImplementedError('TODO: implement')

def signals_tail_absent(text):
    """None of the last 100000 ethan_signals events mentions TEXT (replaces `! ethan_signals.py tail | grep -qF`)."""
    raise NotImplementedError('TODO: implement')

def absent_regex(rel, *pats):
    """File REL (missing = fine) has no line matching any regex in PATS, case-insensitive."""
    raise NotImplementedError('TODO: implement')

def file_has(rel, *needles):
    raise NotImplementedError('TODO: implement')

def doctor_autoupdate():
    raise NotImplementedError('TODO: implement')

def pointer_size():
    raise NotImplementedError('TODO: implement')

def perf_device():
    raise NotImplementedError('TODO: implement')

def seat():
    raise NotImplementedError('TODO: implement')

def low_power_off():
    raise NotImplementedError('TODO: implement')

def tomllib_and_proc():
    raise NotImplementedError('TODO: implement')

def unittest_ok(name):
    """`python3 -m unittest NAME` passes, run from scripts/ (name is a test module such as test_ethan_git_guard)."""
    raise NotImplementedError('TODO: implement')

def cli_patch_guard():
    raise NotImplementedError('TODO: implement')

def main(argv):
    raise NotImplementedError('TODO: implement')
