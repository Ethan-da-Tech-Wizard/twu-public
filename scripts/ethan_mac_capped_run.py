# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Run COMMAND under macOS Seatbelt with sampled RSS and wall bounds.

Usage: ethan_mac_capped_run.py COMMAND [ARG ...]
RSS is sampled across observed descendants, not a kernel memory quota. A process
that detaches entirely between samples may be missed. The filesystem remains
accessible for workspace tests; this is not a disposable VM.
"""
import ctypes
from dataclasses import dataclass
import errno
import fcntl
import math
import os
from pathlib import Path
import re
import resource
import signal
import stat
import subprocess
import sys
import tempfile
import time
import stop_latch

class BSDInfo(ctypes.Structure):
    pass

class ProcessIdentity:
    pass

class InspectionError(OSError):
    """Only fixed phase names and numeric diagnostics; never command arguments."""

    def __init__(self, phase, error=None, pid=None, native_size=None):
        raise NotImplementedError('TODO: implement')

def diagnostic(exc, phase):
    raise NotImplementedError('TODO: implement')

def seatbelt_probe_detail(stderr):
    """Map example_host stderr to a fixed, non-sensitive diagnostic category."""
    raise NotImplementedError('TODO: implement')

class SeatbeltProbeError(ValueError):

    def __init__(self, returncode, stderr):
        raise NotImplementedError('TODO: implement')

def confirmed_zombie(pid):
    """Permission denial alone proves nothing; accept only an exact PID's Z state."""
    raise NotImplementedError('TODO: implement')

def process_info(pid):
    raise NotImplementedError('TODO: implement')

def identity(info):
    raise NotImplementedError('TODO: implement')

def same_process(expected):
    raise NotImplementedError('TODO: implement')

def memory_bytes(value):
    raise NotImplementedError('TODO: implement')

def process_tree(leader, known):
    """Keep birth identities even after observed descendants detach/reparent."""
    raise NotImplementedError('TODO: implement')

def stop_child(child, known):
    raise NotImplementedError('TODO: implement')

class RunnerInterrupted(Exception):

    def __init__(self, signum):
        raise NotImplementedError('TODO: implement')

def acquire_slot(directory, count, wait, check_stop=...):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
