# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""os_alignment: every computer in the fleet must run an operating system the Command Library has mastered.

PROGRAM:       os_alignment.py
PROGRAMMER:    Magi 10 (claude, example_host), at Ethan's request
LAST MODIFIED: 2026-11-19
MAGI_TODO:     fd313a9f (child 2 of the Command Library, spec docs/COMMAND_LIBRARY_SPEC.md section 4)

PURPOSE (beginner picture):
    Ethan wants the Command Library to know every command for each OS he uses (Arch, example_host, macOS today). If he wires a NEW
    computer into the fleet and its OS is not one we have mastered, the system must "freak out" (raise a loud alarm) until that OS
    is registered and documented. This script is the checker. It never fixes or accepts anything by itself.

WHAT IT READS (all read-only except the one fact file this computer writes about ITSELF):
    data/commands/os_registry.json         the registered OSes, their source packs and minimum coverage (edited by people/Magi).
    data/fleet_registry.json (via fleet_registry.py)   which computers are in the fleet.
    /etc/os-release or macOS facts         what THIS computer runs (detect_local).
    data/commands/os_facts.<host>.json     the OS each computer reports about itself. One file PER computer, so Syncthing never sees
                                           two computers writing the same file (the conflict-copy problem fixed on 2026-11-19).
    data/netguard/OS_UPDATES.<node>.json   fallback evidence for a computer that has not written its own fact yet (macOS only).
    data/commands/coverage.<host>.json     written later by the Command Library indexer: {"os_id","total_commands","documented","built_at"} (older spelling {"os","total","documented","at"} still accepted).

STATES per computer:
    ALIGNED          OS id is registered (and coverage is fine, or coverage is not enforced yet).
    UNREGISTERED_OS  HIGH. The computer reports an OS with no registry entry. Alarms until an entry exists. ID_LIKE never matches:
                     a derivative (Manjaro, Ubuntu, Pop!_OS) is a different OS to master, on purpose.
    BELOW_COVERAGE   HIGH, only when the registry flag "enforce_coverage" is true (set it when the indexer exists): coverage file
                     missing, older than coverage_max_age_days, or below the OS's min_coverage_percent.
    UNVERIFIED       MEDIUM, only for a fleet computer that no registry entry expects (a NEW computer) and that has reported no OS yet.
    NO_OS_FACT       info only: an expected computer (e.g. example_host) that has not reported yet. Never alarms.

ALARM + TASK: alarm_problems() returns keys "os-alignment:<host>:<unregistered-os|below-coverage|unverified>" for ethan_alarm.py.
    The first time a state appears it creates ONE MAGI_TODO task ("Master <OS>") via magi_todo_board.py, remembered per computer in
    data/commands/os_master_tasks.<host>.json (and de-duplicated against every computer's file). Nothing here edits the registry.

HOW TO RUN:
    python3 scripts/os_alignment.py             # table of every fleet computer (records this computer's fact first)
    python3 scripts/os_alignment.py --json      # same, machine readable
    python3 scripts/os_alignment.py check       # one line per alarm, exit 1 if any (what the alarm check uses)
    python3 scripts/os_alignment.py check --create-tasks   # also create the Master-OS MAGI_TODO task once per state

CHANGE HISTORY
    2026-11-19  Magi 10  Created.
"""
from __future__ import annotations
import argparse
import json
import os
import platform
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

class RegistryError(Exception):
    """The OS registry is missing or damaged. This is itself an alarm: a guard that cannot read its list must not look clean."""

def load_registry(root=None) -> dict:
    """Read and validate data/commands/os_registry.json. Raises RegistryError (never returns a half-valid registry)."""
    raise NotImplementedError('TODO: implement')

def parse_os_release(text: str) -> dict:
    """Parse /etc/os-release style KEY=VALUE lines (values may be quoted). Unknown lines are ignored."""
    raise NotImplementedError('TODO: implement')

def local_host_id(root=None, node=None) -> str:
    """This computer's fleet name (example_host, example_host, example_host...), via the fleet registry when possible, else the lowercase hostname."""
    raise NotImplementedError('TODO: implement')

def detect_local(os_release_text=None, system=None, mac_version=None, kernel=None, host=None, now=None, root=None) -> dict:
    """What THIS computer says it runs. Every argument can be injected for tests; defaults read the real machine."""
    raise NotImplementedError('TODO: implement')

def _atomic_write(path: Path, data: dict) -> None:
    """Write JSON atomically (temp file in the same folder, then rename) so a sync or crash never sees half a file."""
    raise NotImplementedError('TODO: implement')

def record_fact(fact: dict, root=None) -> Path:
    """Write THIS computer's own fact file (data/commands/os_facts.<host>.json). Only the local computer ever writes its own."""
    raise NotImplementedError('TODO: implement')

def read_fact(host: str, root=None):
    """The OS fact a computer reported about itself, or the macOS fallback from OS_UPDATES, or None."""
    raise NotImplementedError('TODO: implement')

def fleet_hosts(registry: dict, root=None) -> list:
    """Every computer in the fleet (fleet_registry.py), falling back to the hosts the OS registry expects."""
    raise NotImplementedError('TODO: implement')

def match_system(registry: dict, fact: dict):
    """The registry entry whose 'match' fits this fact, or None. Exact ID only; ID_LIKE is never used."""
    raise NotImplementedError('TODO: implement')

def _receipt_time(rec) -> float:
    """Epoch seconds a coverage receipt was written. Accepts the original field `at` (epoch) and the field the Command
    Library indexer really writes, `built_at` (ISO-8601 with offset, e.g. 2026-11-20T00:31:27-0700). 0.0 when absent/unparseable."""
    raise NotImplementedError('TODO: implement')

def coverage_for(host: str, root=None, now=None, max_age_days=14):
    """(percent or None, reason). None means unknown (no file, unreadable, or older than max_age_days).

    2026-11-20 Magi 10 fix: the indexer writes `total_commands` and `built_at` (ISO string); this function used to demand `total`
    and `at`, so every real receipt read as 'not measured'. Both spellings are accepted now. The reason text says WHICH kind of
    unknown it is: missing, unreadable, empty, or stale (with its age in hours/days)."""
    raise NotImplementedError('TODO: implement')

def _library_progress(host: str, root=None) -> str:
    """2026-11-20 Magi 10 (task 94c6c335): when a computer has no coverage report yet, say WHY from its library build status
    (data/commands/library_status.<host>.json, written by `command_library.py auto` in the stale sweep): still building, skipped
    because busy, failed, or no status at all. '' when there is no status file."""
    raise NotImplementedError('TODO: implement')

def _age_text(seconds: float) -> str:
    """Short age: '5 min', '3.2 h' or '2.1 days'."""
    raise NotImplementedError('TODO: implement')

def evaluate(root=None, now=None, local_fact=None, record=True) -> list:
    """One result per fleet computer: {host, state, os_id, system, detail, severity, coverage}.

    When `record` is true this computer's own fact is detected and written first (the only write this function does).
    `local_fact` lets tests inject what 'this computer' reports. Raises RegistryError if the registry is unreadable.
    """
    raise NotImplementedError('TODO: implement')

def _task_markers(root: Path) -> dict:
    """Every computer's marker file merged: {key: task id}. Per-computer files so Syncthing never conflicts."""
    raise NotImplementedError('TODO: implement')

def _default_runner(args):
    raise NotImplementedError('TODO: implement')

def task_payload(result: dict, registry: dict) -> dict:
    """What the Master-OS task would contain: {key, title, checklist, why}. Pure function, used by tests too."""
    raise NotImplementedError('TODO: implement')

def ensure_master_task(result: dict, registry: dict, root=None, host=None, runner=None):
    """Create the Master-OS MAGI_TODO task ONCE for this state (de-duplicated across computers). Returns task id or None."""
    raise NotImplementedError('TODO: implement')

def alarm_problems(root=None, now=None, local_fact=None, create_tasks=False, runner=None, record=True) -> dict:
    """{alarm key: text} for ethan_alarm.py. Empty when everything aligns. Never raises: a broken guard becomes its own alarm."""
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
