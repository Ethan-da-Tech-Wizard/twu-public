# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Ethan's own approval step for a model swap. Run it yourself in a real terminal:

    python3 scripts/ethan_approve.py RUN_NAME

It reads the dry-run receipt (data/autoimprove/20261101/promotions/RUN_NAME.dry_run.json), shows what would be served, and
needs BOTH stdin and stdout to be a real TTY plus you typing the phrase it shows. Agents run without a TTY and are refused.
It writes data/health/approvals/RUN_NAME.json: bound to the run id, model sha256 and adapter sha256, valid 24 h, used once.
Note: Claude Code's `!` shell escape has no TTY; open your own terminal.
"""
import argparse
import getpass
import json
import sys
from pathlib import Path
import ethan_safety as es

def main(argv=None, promo=..., read_line=...) -> int:
    raise NotImplementedError('TODO: implement')
