# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Report the deterministic work available to Ethan CLI while disconnected."""
from __future__ import annotations
from pathlib import Path
import json
import os
import shutil
import stat
import sys
import enki_station as enki
import ethan_connectivity

def _file_presence(path):
    """Metadata only: presence is neither artifact verification nor execution."""
    raise NotImplementedError('TODO: implement')

def _launch_metadata():
    raise NotImplementedError('TODO: implement')

def local_components(root=..., *, launch_reader=None, which=None):
    """Inspect configured Mac argv and existing artifact references, never run them."""
    raise NotImplementedError('TODO: implement')

def recovery_coverage():
    """Describe the existing backup policy; never inspect raw backup error logs."""
    raise NotImplementedError('TODO: implement')

def report(root=...):
    raise NotImplementedError('TODO: implement')

def render(output=..., root=...):
    raise NotImplementedError('TODO: implement')
