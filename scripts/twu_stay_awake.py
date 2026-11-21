# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
from __future__ import annotations
import argparse
import glob
import json
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

def ac_online(sysroot: str=...) -> bool | None:
    """True if any mains supply is online, False if all are offline, None if none can be read (then we change nothing)."""
    raise NotImplementedError('TODO: implement')

class Gs:
    """Wrapper over `gsettings` (tests substitute a fake). Values are the plain text gsettings prints, minus a 'uint32 ' prefix."""

    def get(self, name: str) -> str | None:
        raise NotImplementedError('TODO: implement')

    def set(self, name: str, value: str) -> bool:
        raise NotImplementedError('TODO: implement')

def load_saved(state: Path=...) -> dict | None:
    raise NotImplementedError('TODO: implement')

def save(values: dict, state: Path=...) -> None:
    raise NotImplementedError('TODO: implement')

def _restore(gs, state: Path) -> list:
    raise NotImplementedError('TODO: implement')

def apply(gs, sysroot: str=..., state: Path=...) -> dict:
    """One idempotent pass. Changes nothing when the AC state cannot be read."""
    raise NotImplementedError('TODO: implement')

def check(gs, sysroot: str=...) -> tuple:
    raise NotImplementedError('TODO: implement')

def release(gs, state: Path=...) -> list:
    raise NotImplementedError('TODO: implement')

def watch(interval: float, gs=None) -> int:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
