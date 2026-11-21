# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Share an image over the Magi bus so other devices (including the Linux box) can see it.

Text-only bus could not carry a screenshot; this copies an image into the synced comms images folder
(business/example_host/comms/images/), host-tagged and bounded, so Syncthing replicates it to every
device. The other side reads it with `list` or straight from that folder. A model on the CLI can call
`magi_image.py send <path>` via its shell tool to hand a picture to the fleet.

Images are shared deliberately by the sender; binary pixels are not text-scanned, so do not send a
screenshot that contains a secret, password, or private record. Only image types, bounded size.

  python3 scripts/magi_image.py send <path> [--note "what it is"]
  python3 scripts/magi_image.py list
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

def send(path, note=..., now=None):
    raise NotImplementedError('TODO: implement')

def list_images():
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
