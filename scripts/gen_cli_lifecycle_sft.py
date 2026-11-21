# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""
scripts/gen_cli_lifecycle_sft.py — SFT & DPO Dataset Generator for CLI Agent Window Lifecycle

Generates high-quality training pairs training local models on:
  • Detecting frozen terminal sessions across Antigravity (agy), Claude Code (claude),
    Codex (codex), and Gemini CLI (gemini).
  • Executing clean window termination without touching systemd or rebooting the host
    (Hyprland IPC 'killactive' / Super+Q on Linux, osascript on macOS).
  • Re-launching and resuming agent sessions cleanly in new terminal clients.
  • Rejecting destructive hallucinations (never reinstall OS, never wipe disks).
"""
from __future__ import annotations
import json
from pathlib import Path

def generate_datasets():
    raise NotImplementedError('TODO: implement')
