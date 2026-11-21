# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""fleet_roles: every machine has an assigned ROLE; this checks each one is really doing its assigned work and is not holding what it must not.

  fleet_roles.py check     check THIS machine (duties proven by fresh receipts, data-placement rules), write its receipt, then judge every machine from the synced receipts; exit 1 on any problem
  fleet_roles.py report    one table: every machine, its role, where it lives (inside/outside), each duty and whether it is proven, who is silent
  fleet_roles.py status    open problems from the last check

Roles live in data/fleet_roles.json (plain data; edit it to change a role or add a duty). A DUTY is proven by an evidence file (path with {host}) that must be younger than max_age_s:
the receipts the other tools already write (data/netguard/*.<host>.json etc.), so nothing new has to run for a duty to count. A PLACEMENT rule says what an outside machine must NOT hold
(paths relative to the workspace or to the home folder); every machine checks ITSELF, because only it can see its own disk. The inside hub reads all machines' receipts (synced by Syncthing)
and raises `role:<host>:<what>` alarms; a machine marked `travels` may be offline (it shows 'last seen', not an alarm) until its `max_silent_s`.
An unreadable manifest/receipt is a problem, never 'fine'. Stdlib only, no model, no network. Receipt: data/netguard/FLEETROLE.<host>.json (names/ages only, never file contents).
"""
from __future__ import annotations
import glob, json, os, shutil, socket, sys, time
from pathlib import Path

def load(path=...):
    raise NotImplementedError('TODO: implement')

def canon(host, m):
    """Map a raw hostname (host-g, Ethans-example_host) onto the manifest's host name."""
    raise NotImplementedError('TODO: implement')

def me(m, host=None):
    raise NotImplementedError('TODO: implement')

def evidence_age(rel, host, root, now):
    raise NotImplementedError('TODO: implement')

def placement(m, host, root=..., home=None):
    """Violations of the 'must not hold' rules of this host's role, evaluated on THIS machine's disk. Paths only; never contents."""
    raise NotImplementedError('TODO: implement')

def _nonempty(p, cap=20000):
    """True if p is a non-empty file, or a folder holding at least one non-empty file (empty folders hold nothing sensitive)."""
    raise NotImplementedError('TODO: implement')

def judge_host(m, host, root=..., now=None):
    """[(duty_id, what, state, age_s)] for one machine from synced evidence. state: ok | STALE | MISSING."""
    raise NotImplementedError('TODO: implement')

def requirements(m, host, root=...):
    """[{id, level, state, detail}] for the role's `requires` (a live fact each machine must satisfy, checked ON that machine via twu_facts).
    state: ok | FAIL (fact says no) | UNKNOWN (could not be determined: for a `must` this is a problem too, so it cannot hide)."""
    raise NotImplementedError('TODO: implement')

def d_is_self(m, host, duty_id):
    raise NotImplementedError('TODO: implement')

def check(root=..., d=None, manifest=None, host=None, now=None, home=None):
    raise NotImplementedError('TODO: implement')

def units_for(root=..., host=None, manifest=None):
    """Systemd units this machine may install (its role's install_units). No manifest at all = both (old behaviour); a manifest that does not know this machine, or is unreadable = the safe subset."""
    raise NotImplementedError('TODO: implement')

def outside_block(m, host, root=...):
    """Syncthing ignore lines that keep sensitive folders, and every OTHER machine's conversation archive, off an outside machine."""
    raise NotImplementedError('TODO: implement')

def apply_ignore(root=..., manifest=None, host=None):
    """Append/refresh the outside-profile block in THIS machine's own .stignore. Only on an outside machine; adds ignore lines, never deletes a file. Returns (changed, msg)."""
    raise NotImplementedError('TODO: implement')

def purge_outside(root=..., manifest=None, host=None, apply=False):
    """The explicit step that makes the outside profile effective: remove, from THIS outside machine only, the sensitive folders its role lists in sync_ignore.
    Dry run unless apply=True. Touches only paths that (a) the role lists, (b) are already in this machine's managed .stignore block (so Syncthing will not bring them back),
    (c) are real files/folders inside the workspace (never a symlink, never outside it). The inside machines keep their copies. Returns {'refused': why} or a list of items."""
    raise NotImplementedError('TODO: implement')

def _write(d, host, rc):
    raise NotImplementedError('TODO: implement')

def fleet_problems(root=..., d=None, manifest=None, now=None):
    """The inside hub's view: every machine judged from its own synced receipt + the evidence its duties name."""
    raise NotImplementedError('TODO: implement')

def alarm_problems(now=None, d=None):
    raise NotImplementedError('TODO: implement')

def report(root=..., d=None, manifest=None, now=None):
    raise NotImplementedError('TODO: implement')

def main(a=None):
    raise NotImplementedError('TODO: implement')
