# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/cis_hardening_remediator.py — Automated Remediator for macOS CIS Level 1 Controls.

Categorizes and safely remediates remaining automated CIS controls on macOS:
1. User-level controls (applied immediately without sudo: home permissions, Bluetooth sharing).
2. Root-level controls (generates scripts/apply_macos_cis_hardening.sh for audited execution).
Runs 100% offline, zero network, zero pip dependencies.

Usage:
  python3 scripts/cis_hardening_remediator.py plan      # Display detailed remediation plan
  python3 scripts/cis_hardening_remediator.py apply-user # Apply zero-risk user-level remediations
  python3 scripts/cis_hardening_remediator.py export    # Export audited root-level hardening script
"""
from __future__ import annotations
import argparse
import os
from pathlib import Path
import subprocess
import sys
from typing import Dict, List, Tuple

def print_plan() -> None:
    """Print the complete hardening breakdown."""
    raise NotImplementedError('TODO: implement')

def apply_user_actions() -> int:
    """Apply safe user-level actions."""
    raise NotImplementedError('TODO: implement')

def export_root_script() -> int:
    """Generate the root-level hardening script."""
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
