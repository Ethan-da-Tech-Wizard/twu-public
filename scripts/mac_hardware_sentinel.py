# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Mac Hardware & Thermal Safety Sentinel Daemon.

Protects local macOS hardware during autonomous AI agent runs (Ethan, 2026-10-19):
  1. Priority 1 & 3: Safety, Hardware Health, and Thermal limits.
  2. Samples CPU load average, thermal pressure, and memory RSS every 5 seconds.
  3. Writes real-time status to private/example_host/safety/log/hardware_health.json.
  4. Signals pacing throttle if load average exceeds safe thresholds (>4.5 on 2-core CPU).
  5. Ultra-lightweight footprint (<10MB RAM, <0.2% CPU).
"""
import json
import os
import subprocess
import sys
import time
from pathlib import Path

def get_system_metrics():
    raise NotImplementedError('TODO: implement')

def run_daemon(interval_s=5.0):
    raise NotImplementedError('TODO: implement')
