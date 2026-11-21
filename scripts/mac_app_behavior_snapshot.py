# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""One-shot, metadata-only macOS app-behavior snapshot -> data/health/app_behavior.<host>.jsonl.

The Mac-native counterpart to the Linux app receipt in ethan_health_snapshot.py. It reads only
process metadata (pid, executable basename, CPU percent, resident bytes, thread count, state) for the
busiest processes, plus an available-memory figure and the coarse macOS memory-pressure level. It never
reads argv, environment, open files, clipboard, credentials, window content, or network traffic, and it
never signals, renices, or otherwise changes a process. It is one-shot (no service), host-scoped, and
cheap enough to be safe on an 8 GB machine.

macOS has no Linux-style PSI (pressure stall information), so the cpu/memory/io pressure fields stay
null for schema parity with the Linux receipt; the honest macOS signal is reported separately as
memory_pressure_level (1 normal, 2 warn, 4 critical) from kern.memorystatus_vm_pressure_level.
"""
import json
import platform
import subprocess
import sys
import time
from pathlib import Path

def _run(args, timeout):
    raise NotImplementedError('TODO: implement')

def host_name():
    raise NotImplementedError('TODO: implement')

def out_path():
    raise NotImplementedError('TODO: implement')

def thread_count(pid):
    """Thread count for one pid via `ps -M`; None if unavailable. Metadata only."""
    raise NotImplementedError('TODO: implement')

def processes():
    """Top processes by CPU, metadata only. Executable basename, never argv or full path leakage."""
    raise NotImplementedError('TODO: implement')

def available_memory_bytes():
    """free + inactive + speculative pages * page size, from vm_stat. Aggregate only."""
    raise NotImplementedError('TODO: implement')

def memory_pressure_level():
    raise NotImplementedError('TODO: implement')

def thermal_pressure():
    """Honest no-sudo macOS thermal signal from `pmset -g therm`.

    No CPU temperature is readable on this Mac without sudo or an extra tool, so instead of inventing
    a number this records the throttle state the OS already exposes: CPU_Speed_Limit below 100 means
    the processor is being thermally (or power) limited, i.e. the Mac is hot. This is the real
    heat-detection signal the continuous beacon was missing, with no fabricated temperature.
    """
    raise NotImplementedError('TODO: implement')

def behavior():
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')

def family(name):
    """Group a process name into its app family so helper processes count with their parent."""
    raise NotImplementedError('TODO: implement')

def load_recent(limit):
    """Read up to the newest `limit` logged records for this host. Read-only."""
    raise NotImplementedError('TODO: implement')

def advise(records):
    """Turn logged metadata into one actionable read-only insight: the sustained CPU and memory hog.

    This is what makes the collector benefit the Mac directly. On macOS the shared needs pipeline
    cannot flag app contention because it gates on Linux PSI, so this gives the same per-app signal
    from data already collected, over several samples so a transient spike does not mislead.
    """
    raise NotImplementedError('TODO: implement')

def advise_cmd(limit=12):
    raise NotImplementedError('TODO: implement')

def append_bounded(path, line):
    """Append one record and keep only the newest MAX_RECORDS, written atomically.

    Bounded retention means the metadata receipt cannot grow without limit, and the atomic
    replace keeps fleet readers (which take the last line) from seeing a truncated file.
    """
    raise NotImplementedError('TODO: implement')
