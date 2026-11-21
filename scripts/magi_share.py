# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Share any FILE or FOLDER across the Magi lanes, the way text and photos already cross.

The message bus is text; magi_image carried pictures; this carries arbitrary files and whole folders.
It copies the item into the synced comms share folder (business/example_host/comms/shared/), host-tagged
and bounded, so Syncthing replicates it to every device. The other side reads it with `list` or from
that folder. A model on the CLI can call this via its shell tool to hand a file or folder to the fleet.

Share deliberately: binary content is not text-scanned, so do not share anything holding a secret,
credential, or private record. Symlinks are refused; size and file-count are bounded.

  python3 scripts/magi_share.py send <file-or-folder> [--note "what it is"]
  python3 scripts/magi_share.py list
"""
from __future__ import annotations
import argparse
import json
import platform
import shutil
import sys
import time
from pathlib import Path

def host_slug():
    raise NotImplementedError('TODO: implement')

def safe_name(name):
    raise NotImplementedError('TODO: implement')

def _measure_folder(root):
    """Total bytes and file count; raises if a symlink is present (traversal safety)."""
    raise NotImplementedError('TODO: implement')

def send(path, note=..., now=None):
    raise NotImplementedError('TODO: implement')

def list_shared():
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
