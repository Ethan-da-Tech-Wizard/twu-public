# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Objective rotation oracles for ethan_rotation: facts the OS already keeps, so the human need not be trusted.

Reads only metadata: the date of the last login-password change (`passwd -S`, no root needed for your own
account on Linux) and the FINGERPRINTS of public keys (`ssh-keygen -lf` on *.pub files only). Never opens a
private key, never reads a password or hash, no shell, fixed argv. Anything unavailable is skipped silently.
"""
import datetime as dt, getpass, os, subprocess
from pathlib import Path

def _run(argv):
    raise NotImplementedError('TODO: implement')

def password_changed(user=None, run=...):
    """Date (ISO) of the last password change from `passwd -S`, or None (macOS and unreadable cases)."""
    raise NotImplementedError('TODO: implement')

def pubkey_fingerprints(home=None, run=...):
    """Sorted fingerprints of the public keys in the user's key folder (public files only)."""
    raise NotImplementedError('TODO: implement')
