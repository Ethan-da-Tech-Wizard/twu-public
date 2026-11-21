# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Offline advisory scan of MCP tool definitions with Cisco mcp-scanner (Apache-2.0).

Static mode only, on a JSON file of tool definitions: it never starts or connects to an MCP server.
Always runs in a network-less namespace (`unshare -rn`) with a scrubbed environment (no keys, no
home), and only with the offline `yara` analyzer, so the LLM / API / VirusTotal analyzers cannot run.
Advisory: "no findings" does not mean safe.

    python3 scripts/twu_mcp_scan.py scan <tools.json>    # exit 0 clean, 1 findings, 2 cannot run
    python3 scripts/twu_mcp_scan.py status
Install (inspector-vetted wheels, PyPI hashes verified): see CHANGELOG 2026-11-08.
"""
from __future__ import annotations
import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

def scanner_bin() -> Path:
    raise NotImplementedError('TODO: implement')

def build_command(tools_json: Path) -> list[str]:
    raise NotImplementedError('TODO: implement')

def summarize(output: str) -> dict:
    raise NotImplementedError('TODO: implement')

def scan(tools_json: Path, run=...) -> int:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
