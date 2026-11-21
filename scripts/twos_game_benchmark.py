# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Read a bounded frame CSV into a reproducible TWOS game benchmark summary.

This is analysis only: it neither launches a game nor modifies graphics,
processes, power settings, or telemetry files.
"""
from __future__ import annotations
import argparse
import csv
import json
import math
from pathlib import Path
import sys

def number(value, field):
    raise NotImplementedError('TODO: implement')

def percentile(values, fraction):
    raise NotImplementedError('TODO: implement')

def analyze(path):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
