# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Publish this computer's system settings into the shared folder so the other computer can read them.

Each machine writes only its own subfolder: system/<hostname>/. Nothing here changes any setting; it
only records them. Secrets are redacted (Syncthing API key, anything that looks like a token or
password). Run on demand:

    python3 scripts/system_settings_export.py            # writes system/<hostname>/
    python3 scripts/system_settings_export.py --out DIR  # for tests

Source: Ethan, 2026-10-23: "be able to see each other's internal documents and everything and even
system settings, Mac for Linux and Linux for Mac".
"""
from __future__ import annotations
import argparse
import datetime as dt
import json
import os
import platform
import re
import shutil
import subprocess
import sys
from pathlib import Path

def redact(text: str) -> str:
    raise NotImplementedError('TODO: implement')

def run(cmd: list[str], timeout: int=20) -> str:
    """Run a read-only command; return its output or a one-line note if it is unavailable."""
    raise NotImplementedError('TODO: implement')

def copy_text(src: Path, dest_dir: Path, name: str | None=None) -> str | None:
    """Copy a config file with secrets redacted; return the published name or None."""
    raise NotImplementedError('TODO: implement')

def collect(out: Path) -> dict:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
