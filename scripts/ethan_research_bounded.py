# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Bounded autonomous research run: the autoresearch HPO engine under heat, RAM, STOP and deadline guards.

Runs `hpo_engine.py` for a fixed trial count in its own process group. The thresholds come from
ethan_thermal_guard (AGENTS.md): start only when cool, pause on heat, resume when cool, kill at the
abort temperature. Only the group this script started is ever signalled. Missing telemetry pauses.
"""
import argparse, os, select, signal, subprocess, sys, time
from pathlib import Path
import ethan_thermal_guard as guard
import stop_latch

def process_identity(pid):
    """Return a stable (uid, start ticks, cwd, argv) tuple for a live Linux process."""
    raise NotImplementedError('TODO: implement')

def find_supervisors():
    """Find only same-user runner processes whose cwd and script resolve to this workspace."""
    raise NotImplementedError('TODO: implement')

def status():
    raise NotImplementedError('TODO: implement')

def stop():
    """Interrupt one verified supervisor with a pidfd; never kill a guessed PID or engine process."""
    raise NotImplementedError('TODO: implement')

def readings():
    raise NotImplementedError('TODO: implement')

def supervise(child, deadline, read=..., poll=..., stopped_path=None):
    """Poll until the child exits; returns (reason, exit_code). Signals only the child's own group."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
