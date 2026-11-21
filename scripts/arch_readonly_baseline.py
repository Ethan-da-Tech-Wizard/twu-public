# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Read-only, unprivileged Arch Linux hardening snapshot. NOT a CIS audit.

CIS publishes no benchmark for Arch Linux, so nothing here may be reported as CIS compliance.
Checks are a small, labelled TWU baseline (sysctl, mounts, file modes, services). No sudo, no remediation.
  python3 scripts/arch_readonly_baseline.py [--out data/netguard/ARCH.READONLY.BASELINE.example_host.json]
"""
import argparse, json, os, platform, subprocess, sys
from datetime import datetime, timezone

def sysctl(path):
    raise NotImplementedError('TODO: implement')

def mode(p):
    raise NotImplementedError('TODO: implement')

def active(unit):
    raise NotImplementedError('TODO: implement')

def checks():
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
