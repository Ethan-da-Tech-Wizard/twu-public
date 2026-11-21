# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Beginner coding room, served only by the existing authenticated local dashboard."""
from __future__ import annotations
import html
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import json
import threading

def workspace_root():
    raise NotImplementedError('TODO: implement')

def rust_toolchain():
    raise NotImplementedError('TODO: implement')

def csharp_toolchain():
    """Find a stable SDK, reference pack and runtime from the selected .NET installation."""
    raise NotImplementedError('TODO: implement')

def run(language, source):
    raise NotImplementedError('TODO: implement')

def _run(language, source):
    raise NotImplementedError('TODO: implement')

def page(token):
    raise NotImplementedError('TODO: implement')
