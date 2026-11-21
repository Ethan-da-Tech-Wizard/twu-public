# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/ethan_hotkey_typo_gate.py — Cross-Platform Hotkey Prompt & Typo Gate.

Provides a global hotkey prompt dialog across Linux (Hyprland/Wayland via rofi/zenity)
and macOS (via osascript/pbcopy).
Offers a review dialog before copying a suggested reading to the clipboard.
Uncertain suggestions and damaged learning records never silently change input.

"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import subprocess
import sys
from typing import Any, Dict, List, Optional, Tuple
from scripts.ethan_typo_normalizer import EthanTypoNormalizer

def copy_to_clipboard(text: str) -> None:
    """Copies text to the system clipboard on Linux or macOS."""
    raise NotImplementedError('TODO: implement')

def get_clipboard() -> str:
    """Reads text from the system clipboard."""
    raise NotImplementedError('TODO: implement')

def send_notification(title: str, message: str) -> None:
    """Sends desktop notification."""
    raise NotImplementedError('TODO: implement')

def prompt_user_input(placeholder: str=...) -> Optional[str]:
    """Displays an input dialog (rofi/zenity on Linux, osascript on Mac)."""
    raise NotImplementedError('TODO: implement')

def confirm_did_you_mean(original: str, corrected: str, corrections: List[Tuple[str, str]], result=None) -> str:
    """Presents a Did You Mean confirmation dialog."""
    raise NotImplementedError('TODO: implement')

def run_hotkey_gate(mode: str=...) -> None:
    raise NotImplementedError('TODO: implement')

def main() -> None:
    raise NotImplementedError('TODO: implement')
