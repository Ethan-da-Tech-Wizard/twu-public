# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Offline speech-to-text wrapper around whisper.cpp (MIT, ggml-org/whisper.cpp).

Usage: twu_transcribe.py transcribe FILE [--format text|srt] [--model PATH] [--out FILE]
       twu_transcribe.py status

Runs CPU-only at nice 19, no network. Refuses paths outside HOME or the workspace. Output is a
machine transcript: it may be wrong and is never evidence of what was said or agreed.
"""
import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

class TranscribeError(Exception):
    pass

def allowed(path):
    raise NotImplementedError('TODO: implement')

def find_cli():
    raise NotImplementedError('TODO: implement')

def find_model(explicit=None):
    raise NotImplementedError('TODO: implement')

def transcribe(file, fmt=..., model=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
