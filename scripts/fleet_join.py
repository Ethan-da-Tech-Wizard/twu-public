# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""fleet_join: READ-ONLY checklist for joining THIS computer to the fleet.

OWNER / LAST CHANGED: Magi 23, 2026-11-19

PURPOSE: a beginner-friendly "what is still missing on this computer?" list (workspace, Syncthing, tunnel, fleet listener,
    pairing, dashboard, reachability) so joining a new computer is a numbered checklist instead of guesswork.
WHO USES IT: Ethan or a Magi on the computer being added; the dashboard may show the same list.
HOW TO RUN:
    python3 scripts/fleet_join.py          # exit 0 = every check passed, 1 = something needs attention
    cd scripts; ETHAN_HOST=1 python3 -m unittest test_fleet_join
SAFETY RULES:
    * Prints a numbered PASS/FAIL list and the exact next command for each FAIL.
    * It never runs setup, trust, unlock or deploy; it only prints those commands (the owner runs them).
    * It never prints IP addresses, key fingerprints, or the Syncthing key.
    * The only things it executes are read-only probes (ip/ifconfig, ping, systemctl/launchctl status, ss/lsof, fleet_do status).
    * Which computers exist comes from fleet_registry, so adding a fourth or fifth computer needs no change here.
"""
import json
import re
import socket
import subprocess
import sys
import urllib.request
from pathlib import Path

def registry(root=...):
    """(names, registry module): the one list of computers, read fresh. Every computer is equal; nothing is hard-coded."""
    raise NotImplementedError('TODO: implement')

def sh(argv, timeout=15, run=...):
    """Run a read-only command; return (exit code, stdout+stderr). Never raises: a failure to start gives (127, error name).

    `run` is injectable so tests can fake every command and never touch the real network or services.
    """
    raise NotImplementedError('TODO: implement')

def http_text(url, timeout=8):
    """GET `url` and return the body text. Used only for the local dashboard (127.0.0.1). Raises URLError/OSError on failure."""
    raise NotImplementedError('TODO: implement')

def fleet_json(run, *args):
    """Run `fleet_control.py ARGS` and parse its JSON output; any non-JSON output gives {} (treated as 'not configured')."""
    raise NotImplementedError('TODO: implement')

def status_failure(output, target=...):
    """Classify a bounded status failure without exposing host/key/remote output.

    Args: output = text from fleet_do status (only the first 8 KiB is read); target = computer name for the advice text.
    Returns (what_happened, what_to_do_next), both fixed sentences. Why fixed text: remote output can hold secrets, so it is
    matched against known phrases and then discarded. The most specific causes (host key, auth) come first so a host-key
    change is never mistaken for a plain timeout.
    """
    raise NotImplementedError('TODO: implement')

def check_all(plat=None, run=..., fetch=..., root=..., host=None, addr=None, peers=None, syncthing=None):
    """Return a list of (title, ok, detail, next_command). Pure given its injected parts.

    Args: plat ('mac'/'linux'), run/fetch (fake command and HTTP functions for tests), root, host/addr/peers/syncthing
    (preset answers so tests need no machine state). Seven checks run in order; a FAIL carries the exact next command and
    nothing here changes the computer. Tests must isolate HOME and set ETHAN_HOST because the dashboard/service checks
    look in the real home folder and the hostname lookup would otherwise describe the developer's own computer.
    """
    raise NotImplementedError('TODO: implement')

def render(items):
    """Turn check_all()'s tuples into the printable numbered checklist text (plain string, no side effects)."""
    raise NotImplementedError('TODO: implement')

def main():
    """Run all checks, print the checklist, return 0 only if every item passed (so scripts can branch on it)."""
    raise NotImplementedError('TODO: implement')
