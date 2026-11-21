# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Start the inspected Briar peer in an isolated network namespace.

Setup opens a local terminal. Nickname and encryption password are entered
directly into Briar, never passed through EZ, this CLI, or a cloud service.
"""
from __future__ import annotations
import argparse
import fcntl
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import socket
import stat
import subprocess
import sys

def runtime_path():
    raise NotImplementedError('TODO: implement')

def safe_read(path, limit):
    raise NotImplementedError('TODO: implement')

def verify_runtime(path=None, receipts=None):
    raise NotImplementedError('TODO: implement')

def port_open():
    raise NotImplementedError('TODO: implement')

def runtime_command(path):
    raise NotImplementedError('TODO: implement')

def terminal_command():
    raise NotImplementedError('TODO: implement')

def setup_status():
    """Fixed local setup diagnostics; never expose paths, keys or profile data."""
    raise NotImplementedError('TODO: implement')

def setup():
    raise NotImplementedError('TODO: implement')

def console():
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
