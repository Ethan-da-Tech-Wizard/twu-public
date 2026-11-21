# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Opt-in behavioral check through Ethan's native headless session and resume path."""
import argparse
import json
import os
from pathlib import Path
import secrets
import signal
import subprocess
import tempfile
import time
import uuid

def conversation():
    raise NotImplementedError('TODO: implement')

def grade(output, expected, previous_session):
    raise NotImplementedError('TODO: implement')

def stop_group(process):
    raise NotImplementedError('TODO: implement')

def invoke(prompt, session, policy, timeout):
    raise NotImplementedError('TODO: implement')

def run(timeout, runner=...):
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
