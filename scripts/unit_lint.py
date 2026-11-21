# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Read-only linter for systemd user units (live, scripts/units, system/example_host/config user__*).

Rules (severity): path-trigger-limit (HIGH), timeout-vs-quota (HIGH), missing-execstart (HIGH), timer-missing-service (HIGH),
model-no-latch (HIGH), oneshot-nonzero-exit (MED), timer-not-enabled (MED), monitor-no-limits (LOW),
monitor-no-example_host (LOW: oneshot without any systemd example_host directive; baseline-grandfathered, new units need one).
Only HIGH findings absent from data/unit_lint_baseline.json make the exit code nonzero.
The baseline is shrink-only: --update-baseline drops fixed entries and never adds new ones.
Nothing here starts, stops or edits a unit.
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

def parse(path: Path) -> dict[str, dict[str, list[str]]]:
    raise NotImplementedError('TODO: implement')

def merged(path: Path) -> dict[str, dict[str, list[str]]]:
    raise NotImplementedError('TODO: implement')

def one(d, sec, key, default=None):
    raise NotImplementedError('TODO: implement')

def seconds(text: str | None) -> float | None:
    raise NotImplementedError('TODO: implement')

def expand(text: str, name: str) -> str:
    raise NotImplementedError('TODO: implement')

def find(unit: str, dirs: list[Path]) -> Path | None:
    raise NotImplementedError('TODO: implement')

def exec_target(cmd: str, workdir: str) -> Path | None:
    raise NotImplementedError('TODO: implement')

def finding(unit, rule, sev, msg, fix):
    raise NotImplementedError('TODO: implement')

def lint_unit(path: Path, name: str, dirs: list[Path], enabled: set[str] | None) -> list[dict]:
    raise NotImplementedError('TODO: implement')

def enabled_timers(live: Path) -> set[str] | None:
    raise NotImplementedError('TODO: implement')

def lint_dirs(dirs: list[Path], check_enabled: bool=True) -> list[dict]:
    raise NotImplementedError('TODO: implement')

def load_baseline(path: Path) -> set[str]:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
