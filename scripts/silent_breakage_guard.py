# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Catch the two silent failures that bit us, before they bite again.

Today two things broke quietly and were only found by accident: game mode left MODEL_STANDBY set for
~24h so the model stayed asleep, and a gemini update silently dropped the Ethan CLI branding/quote
patch. This deterministic, read-only guard flags both, so they are noticed in minutes, not by stumbling
into them. It changes nothing; it only reports. Cross-platform: it finds the gemini bundle wherever
`gemini` is, and reads the synced MODEL_STANDBY file, so it is the same answer on every device.

  python3 scripts/silent_breakage_guard.py            # print status, exit 1 if anything is wrong
  python3 scripts/silent_breakage_guard.py --json      # machine-readable
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import glob
import json
import os
import re
import shutil
import sys
from pathlib import Path

def check_standby(now=None):
    """ALERT if MODEL_STANDBY has been set longer than a sane bound (the game-mode-left-it-on bug)."""
    raise NotImplementedError('TODO: implement')

def _gemini_bundle():
    raise NotImplementedError('TODO: implement')

def check_cli_branding():
    """ALERT if the gemini bundle lost the Ethan header or quote patch (drift after an update)."""
    raise NotImplementedError('TODO: implement')

def run(now=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
