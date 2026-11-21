# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/build_ios_runelite_standalone.py — Standalone iOS RuneLite File & WebClip Builder.

Packages the 100% client-side RuneLite Mobile application into standalone artifacts:
1. Standalone single-file HTML5 client (runelite_mobile.html)
2. Apple WebClip configuration profile (RuneLite.mobileconfig)
3. Offline Data-URI container

Zero server required. True OSRS Mobile controls (tap-to-walk, long-press right-click, 2-finger camera orbit).
"""
from __future__ import annotations
import argparse
import base64
import hashlib
import json
from pathlib import Path
import sys
import uuid

def generate_webclip_profile(standalone_url: str=...) -> str:
    """Generates an Apple .mobileconfig profile for 1-tap installation to iPhone Home Screen."""
    raise NotImplementedError('TODO: implement')

def build_all() -> dict[str, str]:
    raise NotImplementedError('TODO: implement')

def main() -> int:
    raise NotImplementedError('TODO: implement')
