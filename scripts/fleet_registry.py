# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Fleet registry: the ONE list of Ethan's computers.

OWNER / LAST CHANGED: Magi 23, 2026-11-19

PURPOSE:
    Ethan wants every report to follow the fleet as it grows ("3, then 4, then 5") and shrinks, without anyone editing
    code. So no script hard-codes host names; they all ask this module "who is in the fleet?".

WHO USES IT:
    fleet_control.py (peers, onboard/offboard), fleet_view.py, fleet_join.py, fleet_gate.py and the dashboard panels.
    Beginner picture: it is the address book. It says who exists and where to reach them; it never opens a door.

HOW TO RUN (read-only; changing the list is done through `fleet_control.py onboard/offboard`):
    python3 scripts/fleet_registry.py            # prints one line per computer
    from fleet_registry import hosts, label, address, platform_of, hostname_to_host

DATA: data/fleet_registry.json (synced between computers). It holds NO secrets: only names, labels, platform, the private
    tunnel address and the hostnames a computer may report. Missing or damaged file -> the three original computers
    (DEFAULTS), so nothing breaks.

SAFETY RULES:
    * This module only edits the LIST. It never grants access: a computer in the list is NOT trusted until the owner runs
      the pairing steps (fleet_control.py setup, then trust with fingerprints checked on both computers).
    * Removing a computer here does not revoke its key; `fleet_control.py offboard NAME` revokes first and then calls remove().
    * Every entry is validated (name shape, platform, address inside the private tunnel subnet); bad entries are ignored.
    * Writes are atomic (temp file + rename) so a crash or a sync never sees half a file.
"""
from __future__ import annotations
import ipaddress
import json
import os
import re
import tempfile
import time
from pathlib import Path

class RegistryError(ValueError):
    """Raised by add()/remove() with a plain-English reason that is safe to show to the owner."""

def _path(root=None) -> Path:
    """Where the registry file lives; `root` lets tests point at a temporary folder instead of the real workspace."""
    raise NotImplementedError('TODO: implement')

def _label(text, name):
    """One safe display line: control characters and newlines removed, 40 characters at most (falls back to the name)."""
    raise NotImplementedError('TODO: implement')

def _clean(name, entry):
    """Return a validated copy of one entry or None if it is not trustworthy (a bad entry is ignored, never half-used).

    WHY ignore instead of repair: the file is synced from other computers. A guessed repair could point a name at the wrong
    address, so we drop the entry and keep the rest of the fleet working.
    """
    raise NotImplementedError('TODO: implement')

def load(root=None) -> dict:
    """name -> entry, in a stable order (by name). Never raises.

    Args: root: optional workspace folder (tests). Returns: dict of validated entries.
    Why safe: read-only; any read/parse error falls back to DEFAULTS rather than an empty fleet.
    """
    raise NotImplementedError('TODO: implement')

def hosts(root=None) -> list:
    """Return the fleet names, sorted. Read-only."""
    raise NotImplementedError('TODO: implement')

def peers(root=None) -> dict:
    """The shape fleet_control.PEERS has always had: name -> address."""
    raise NotImplementedError('TODO: implement')

def label(name, root=None) -> str:
    """Friendly display name (e.g. "example_host Air"); falls back to the raw name for an unknown computer."""
    raise NotImplementedError('TODO: implement')

def address(name, root=None):
    """Private tunnel address of `name`, or None if it is not in the fleet."""
    raise NotImplementedError('TODO: implement')

def platform_of(name, root=None):
    """"linux" or "macos" for `name`, or None if unknown (callers choose commands per platform)."""
    raise NotImplementedError('TODO: implement')

def hostname_to_host(raw, root=None):
    """Map what a computer calls itself (hostname) to its fleet name, or None."""
    raise NotImplementedError('TODO: implement')

def _write(data: dict, root=None) -> None:
    """Atomically replace the registry file (write a temp file in the same folder, then rename over it).

    WHY: a sync or crash must never see a half-written list; os.replace is atomic on one filesystem, which is why the
    temp file is created next to the target and not in /tmp. The finally block removes the temp file if anything failed.
    """
    raise NotImplementedError('TODO: implement')

def add(name, label_text, platform, addr, hostnames=None, root=None) -> dict:
    """Add one computer to the LIST (grants nothing). Raises RegistryError with a plain reason.

    Args: name (fleet name), label_text (display), platform ("linux"/"macos"), addr (tunnel IP in 192.0.2.1/24),
    hostnames (names it may report; defaults to [name]). Returns the stored entry.
    Why safe: it only writes the list. Trust (keys) is a separate owner-approved step in fleet_control.py.
    Duplicate names, addresses and hostnames are refused so two computers can never share an identity.
    """
    raise NotImplementedError('TODO: implement')

def remove(name, root=None) -> dict:
    """Remove one computer from the LIST. Any computer may be removed, but the last two cannot be.

    Raises RegistryError if unknown or if only two remain (a fleet of one has nobody to sync with). Returns the removed
    entry. It does NOT revoke SSH keys; use `fleet_control.py offboard` which revokes first.
    """
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    """CLI: print the fleet list (read-only). Returns 0."""
    raise NotImplementedError('TODO: implement')
