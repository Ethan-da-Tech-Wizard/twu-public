# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""mesh_watch: unprivileged WireGuard mesh health ledger (no root, no model; network = overlay probes only).

  mesh_watch.py run      probe each peer (ICMP + TCP 22000 over the overlay), read wg0 sysfs counters, update the ledger
  mesh_watch.py status   print the last ledger state and alarms

Alarms: a peer unreachable (neither ICMP nor TCP) for 3 consecutive runs; wg0 missing/down; wg0 rx+tx counters unchanged
for 2 consecutive runs (keepalive is 25s, so a live tunnel always moves); ledger silent for 20 min once it exists.
ICMP-filtered but TCP-reachable peers (macOS stealth mode) are healthy. Ledger: data/netguard/mesh_watch.<host>.json
(state) and .jsonl (history).
"""
from __future__ import annotations
import json, os, socket, sys, time
from pathlib import Path
import twu_wg

def paths(host=None, d=None):
    raise NotImplementedError('TODO: implement')

def load(state_path):
    raise NotImplementedError('TODO: implement')

def run(host=None, d=None, now=None, ping=None, tcp=None, iface=None, hosts=None):
    """Probe, update state, append history. Injected probes/iface keep tests hermetic."""
    raise NotImplementedError('TODO: implement')

def problems_from(state, now):
    raise NotImplementedError('TODO: implement')

def alarm_problems(now=None, host=None, d=None):
    raise NotImplementedError('TODO: implement')

def main(a=None):
    raise NotImplementedError('TODO: implement')
