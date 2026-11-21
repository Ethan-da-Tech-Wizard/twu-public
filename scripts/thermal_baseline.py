# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Bounded, read-only Linux thermal baseline sampler.

Default: 15 minutes of passive observation.  It never starts workload, changes
kernel/governor/fan/firmware settings, or signals a process.  A future tuning
proposal must compare its own equivalent receipt against this baseline.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
import math
import os
from pathlib import Path
import socket
import sys
import tempfile
import time
import ethan_thermal_guard as guard

def finite(value):
    raise NotImplementedError('TODO: implement')

def load_one():
    raise NotImplementedError('TODO: implement')

def aggregate(samples):
    raise NotImplementedError('TODO: implement')

def collect(duration=..., interval=5, *, sample=..., sleeper=..., monotonic=...):
    raise NotImplementedError('TODO: implement')

def save(receipt, path=...):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
