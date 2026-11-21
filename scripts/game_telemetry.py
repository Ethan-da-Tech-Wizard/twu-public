# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Sits beside a game session and records what the hardware actually did, so lag claims become measurable facts.

Waits for the game (enlisted.exe/dagor), then samples every 5 s while it runs: GPU use, VRAM, GPU/CPU temperature,
GPU clock and the GPU's own throttle reasons (nvidia-smi clocks_event_reasons: thermal, power, sync). Stops when the
game exits and writes data/game_telemetry/<stamp>.jsonl plus a SUMMARY line. Read-only: it never touches the game.
"""
import json, subprocess, sys, time
from pathlib import Path

def sh(cmd):
    raise NotImplementedError('TODO: implement')

def game_pid():
    raise NotImplementedError('TODO: implement')

def session_live(misses=4, gap=5):
    """True while the game runs; a session only ends after `misses` consecutive empty checks, because Steam's
    launcher chain makes the process name flicker for a few seconds around startup."""
    raise NotImplementedError('TODO: implement')

def sample():
    raise NotImplementedError('TODO: implement')

def throttle_names(bits):
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
