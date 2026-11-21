# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/ethan_shot.py — Sovereign Hyprland/Wayland Screenshot & Clipboard Bridge for Ethan CLI.

Takes area or fullscreen screenshots on Arch Linux / Hyprland, persists them to /tmp/ethan-clip.png
and ~/Pictures/Screenshots, populates the Wayland image clipboard and primary text selection,
and provides OCR extraction for seamless pasting into Ethan CLI.

"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import os
from pathlib import Path
import shutil
import subprocess
import sys

def notify(title: str, message: str, icon_path: Path | None=None) -> None:
    raise NotImplementedError('TODO: implement')

def capture_screenshot(area: bool=True, output_path: Path=...) -> bool:
    raise NotImplementedError('TODO: implement')

def run_ocr(image_path: Path) -> str:
    raise NotImplementedError('TODO: implement')

def main(argv: list[str] | None=None) -> int:
    raise NotImplementedError('TODO: implement')
