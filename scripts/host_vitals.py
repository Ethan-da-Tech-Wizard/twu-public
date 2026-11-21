# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Read-only vitals. Standard library only. No sudo, no shell, no network, fixed argv lists with a short timeout.
Pure parsers (parse_meminfo, parse_pmset, parse_vm_stat, parse_os_release) take text so they can be tested anywhere."""
from __future__ import annotations
import os
import platform
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, Optional

def _run(argv) -> Optional[str]:
    """Run a fixed argv list (no shell) and return stdout text, or None on any failure."""
    raise NotImplementedError('TODO: implement')

def parse_meminfo(text: str) -> Dict[str, Optional[float]]:
    """/proc/meminfo text -> {total_gib, avail_gib}. MemAvailable is what the kernel says is usable without swapping."""
    raise NotImplementedError('TODO: implement')

def parse_vm_stat(text: str, total_bytes: Optional[int]) -> Dict[str, Optional[float]]:
    """macOS vm_stat text -> {total_gib, avail_gib}. Available = free + inactive + speculative pages (the usual approximation)."""
    raise NotImplementedError('TODO: implement')

def parse_pmset(text: str) -> Dict[str, Any]:
    """macOS `pmset -g batt` text -> {pct, ac, state}. Example line: ' -InternalBattery-0 (id=...) 84%; charging; 1:02 remaining'."""
    raise NotImplementedError('TODO: implement')

def parse_os_release(text: str) -> Dict[str, Optional[str]]:
    """/etc/os-release text -> {os_id, os_name}. Values may be quoted."""
    raise NotImplementedError('TODO: implement')

def _read(path: str) -> Optional[str]:
    raise NotImplementedError('TODO: implement')

def _linux_cpu_temp() -> Optional[float]:
    """Hottest readable CPU package/core temperature in C from sysfs thermal zones and coretemp hwmon, else None."""
    raise NotImplementedError('TODO: implement')

def _linux_battery() -> Dict[str, Any]:
    """Battery percent and whether mains power is connected, from /sys/class/power_supply."""
    raise NotImplementedError('TODO: implement')

def collect(now: Optional[float]=None) -> Dict[str, Any]:
    """One vitals snapshot for THIS computer. Never raises: anything unreadable is None."""
    raise NotImplementedError('TODO: implement')
