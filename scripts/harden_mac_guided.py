# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""harden_mac_guided: the Mac security steps that need YOU (password or decision), one at a time. Nothing runs without a 'y'.

  python3 scripts/harden_mac_guided.py --dry-run     show every step and its undo, change nothing
  python3 scripts/harden_mac_guided.py               walk the steps; answer y / n / q for each
  python3 scripts/harden_mac_guided.py --yes-only ID,ID   run only those steps (still asks)

Steps never delete an account and never change Syncthing; they only open the right screen or set a reversible preference. Stdlib only, no network.
"""
import subprocess, sys

def run(argv=None, ask=..., runner=..., out=...):
    raise NotImplementedError('TODO: implement')
