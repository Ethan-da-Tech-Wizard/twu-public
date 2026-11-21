# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Offline advisory scan of an agent skill folder with Cisco's skill-scanner (Apache-2.0).

Always runs the scanner inside a network-less namespace (`unshare -rn`), so telemetry and the
optional LLM / VirusTotal / OSV / AI Defense features cannot reach anything. Never passes
--use-llm or any network flag. A clean result is advisory: "no findings" does not mean safe.

    python3 scripts/twu_skill_scan.py scan <skill_dir>      # exit 0 clean, 1 findings >= high, 2 cannot run
    python3 scripts/twu_skill_scan.py status                # is the scanner installed
Install (done once, wheels vetted by private/example_host/safety/inspector.py): see CHANGELOG 2026-11-08.
"""
from __future__ import annotations
import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

def scanner_bin() -> Path:
    raise NotImplementedError('TODO: implement')

def build_command(skill_dir: Path, out_json: Path) -> list[str]:
    raise NotImplementedError('TODO: implement')

def summarize(report: dict) -> dict:
    raise NotImplementedError('TODO: implement')

def scan(skill_dir: Path, run=...) -> int:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
