# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""BUILD MODE: one switch that brings the system's SENSORS and MONITORS up while Ethan and the Magi build.

  python3 scripts/build_mode.py on [--dry-run]      snapshot unit state, start the sensor units, record the state
  python3 scripts/build_mode.py off [--dry-run]     return every touched unit to the snapshot (and forget the mode)
  python3 scripts/build_mode.py status [--json]     on/off, boot check, per-unit now-vs-snapshot, the commands
  python3 scripts/build_mode.py restore [--dry-run] re-apply the last build-mode-on set (after a reboot cleared it)
  python3 scripts/build_mode.py boot-check          run once per login by twu-build-mode-boot.service

Sensors only. The allowlist below is the ONLY set of units this tool ever starts or stops (``systemctl --user start|stop``
and nothing else: it never enables, disables, masks, kills or edits a unit file), so a unit that was off or disabled before
is never made permanent. ``off`` stops only the units that were inactive in the snapshot; units that were already running
are left running. Heavy workers (ethan-evolve, ethan-certify, ethan-volley, ethan-tune, ethan-model, the freshness sentinel
that re-launches jobs, anything that trains, serves a model or uses the GPU) are on FORBIDDEN and refused even if asked.

State lives in $XDG_RUNTIME_DIR/twu-build-mode/state.json (tmpfs: cleared at boot) and carries /proc boot_id; a state whose
boot_id differs from the current boot is treated as OFF and logged. data/health/build_mode.last.json keeps the last "on" set
for ``restore``; data/health/build_mode.log.jsonl is the append-only log. STOP (stop_latch) blocks ``on`` and ``restore``.
No root, no model, no network.
"""
from __future__ import annotations
import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

def now() -> str:
    raise NotImplementedError('TODO: implement')

def boot_id() -> str:
    raise NotImplementedError('TODO: implement')

def state_path(env=None) -> Path:
    raise NotImplementedError('TODO: implement')

def real_runner(argv: list[str]) -> tuple[int, str]:
    """Run one systemctl --user command; the only subprocess this tool makes."""
    raise NotImplementedError('TODO: implement')

def read_json(path: Path):
    raise NotImplementedError('TODO: implement')

def write_json(path: Path, data: dict) -> None:
    raise NotImplementedError('TODO: implement')

def log(event: str, log_path: Path | None=None, **fields) -> None:
    raise NotImplementedError('TODO: implement')

class BuildMode:

    def __init__(self, runner=..., state_file: Path | None=None, last_file: Path | None=None, log_file: Path | None=None, dry_run: bool=False, sensors=..., bid: str | None=None):
        raise NotImplementedError('TODO: implement')

    def _read(self, verb: str, unit: str) -> str:
        raise NotImplementedError('TODO: implement')

    def _mutate(self, verb: str, unit: str) -> bool:
        raise NotImplementedError('TODO: implement')

    def observe(self, units=None) -> dict:
        raise NotImplementedError('TODO: implement')

    def current(self) -> dict | None:
        """The live build-mode state, or None. A state from another boot counts as OFF (and is logged and removed)."""
        raise NotImplementedError('TODO: implement')

    def on(self, units=None) -> dict:
        raise NotImplementedError('TODO: implement')

    def off(self) -> dict:
        raise NotImplementedError('TODO: implement')

    def restore(self) -> dict:
        raise NotImplementedError('TODO: implement')

    def boot_check(self) -> str:
        """Run at login: a persisted 'on' from a previous boot means the mode lapsed; say so and record it."""
        raise NotImplementedError('TODO: implement')

    def status(self) -> dict:
        raise NotImplementedError('TODO: implement')

def render(s: dict) -> str:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
