# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Single-instance 7-minute task-bus scheduler; never injects keystrokes."""
from __future__ import annotations
import argparse
import fcntl
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import dispatch_breaker

def load_state(path: Path=...) -> dict:
    raise NotImplementedError('TODO: implement')

def save_state(value: dict, path: Path=...) -> None:
    raise NotImplementedError('TODO: implement')

def acknowledge(state: dict, packet: str, now: float) -> None:
    raise NotImplementedError('TODO: implement')

def adopt(state: dict, packet: str, now: float) -> None:
    raise NotImplementedError('TODO: implement')

def dispatch(state: dict, now: float, runner=..., breaker=None) -> bool:
    raise NotImplementedError('TODO: implement')

def main() -> int:
    raise NotImplementedError('TODO: implement')
