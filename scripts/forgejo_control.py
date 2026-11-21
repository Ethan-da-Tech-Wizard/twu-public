# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Private local Forgejo status and STOP-aware foreground service entrypoint."""
from __future__ import annotations
import argparse
import configparser
import hashlib
import http.client
import json
import os
from pathlib import Path
import re
import signal
import stat
import subprocess
import sys
import threading
import time

def runtime_directory():
    raise NotImplementedError('TODO: implement')

def _private_directory(path):
    raise NotImplementedError('TODO: implement')

def _read_private(path, limit=65536):
    raise NotImplementedError('TODO: implement')

def instance(runtime=None):
    raise NotImplementedError('TODO: implement')

def _service_pid():
    raise NotImplementedError('TODO: implement')

def _running_binary(pid, binary, runtime):
    raise NotImplementedError('TODO: implement')

def _json_get(path):
    raise NotImplementedError('TODO: implement')

def _binary_is_pinned(binary):
    """Hash once per stable file identity; avoid a repeated 116 MB read on every poll."""
    raise NotImplementedError('TODO: implement')

def status(runtime=None):
    """Return only measured public UI metadata, never config, credentials or identities."""
    raise NotImplementedError('TODO: implement')

def _checked_config(runtime):
    raise NotImplementedError('TODO: implement')

def serve(workspace, runtime=None):
    """Own exactly one child and stop it when the shared incident latch or unit stops."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
