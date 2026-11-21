# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""net_guard: user-level network monitor for every TWU box (no root, no model, no network calls of its own).

  net_guard.py learn     accept the current network state as the baseline (Ethan/Magi decision)
  net_guard.py learn --only KEY [--only KEY2]  accept just those findings (keys exactly as `check` prints them)
  net_guard.py check     compare now to baseline; write data/netguard/LATEST.<host>.json; exit 1 on findings
  net_guard.py status    print the last receipt
  net_guard.py snapshot  print the current snapshot as JSON

Detects: new non-loopback listeners, a listener whose program changed, gateway MAC change (ARP spoofing / rogue
router), DNS resolver change, new LAN neighbours, outbound connections to classic backdoor/C2/Tor ports.
Metadata only: addresses, ports, program names. Linux (ss, ip) and macOS (lsof, netstat, arp) via an injected runner.
"""
from __future__ import annotations
import hashlib
import ipaddress
import json
import os
import platform
import re
import socket
import subprocess
import sys
import time
from pathlib import Path

class ProbeUnavailable(RuntimeError):
    """A required network or firewall sensor failed, so its result is not trustworthy."""

def run(cmd, timeout=10):
    raise NotImplementedError('TODO: implement')

def split_hostport(s):
    raise NotImplementedError('TODO: implement')

def is_loopback(host):
    raise NotImplementedError('TODO: implement')

def parse_ss_listeners(text):
    raise NotImplementedError('TODO: implement')

def parse_lsof_listeners(text):
    raise NotImplementedError('TODO: implement')

def parse_ss_established(text):
    raise NotImplementedError('TODO: implement')

def parse_ip_neigh(text):
    raise NotImplementedError('TODO: implement')

def parse_arp_a(text):
    raise NotImplementedError('TODO: implement')

def parse_default_gateway(text):
    raise NotImplementedError('TODO: implement')

def parse_resolvers(text):
    raise NotImplementedError('TODO: implement')

def resolve_exe(pid, runner=..., os_name=None):
    """Best-effort executable identity of a process: {"exe": realpath, "sha256": hex, "system": bool} or None.

    Args:
        pid: integer process id from ss/lsof (None or non-int -> None).
        runner: injected command runner (used on macOS: `ps -o comm=` prints the full executable path).
        os_name: platform override for tests.
    Returns:
        dict, or None when the path cannot be resolved/read. None means "unproven", and compare() then does NOT
        exempt the listener (fail closed). Never raises: a vanished or unreadable process must not break the sensor.
    "system" is True only when the file AND its directory chain are not user-writable and the file is owned by
    root (uid 0) and lives under SYSTEM_EXE_ROOTS."""
    raise NotImplementedError('TODO: implement')

def allowed_exes(path=None):
    """Owner-reviewed (prog, realpath, sha256) executables from data/netguard/allow_exe.json -> list of dicts.
    Format: {"allow": [{"prog": "syncthing", "exe": "/home/user/bin/syncthing", "sha256": "<64 hex>"}]}.
    sha256 is REQUIRED: a path alone is not an identity (the file can be replaced). Missing/unreadable file -> []."""
    raise NotImplementedError('TODO: implement')

def exe_is_trusted(l, exes=None):
    """Does listener record `l` (with exe/exe_sha256/exe_system added by snapshot) prove it is the real program it
    claims to be? Binds process NAME AND executable path/hash (finding 3). Pure given `exes`.
    Trusted when EITHER the executable is a root-owned system install whose basename starts with the claimed name
    (comm names are truncated to 15 chars, so startswith), OR (prog, exe, sha256) exactly matches an allow_exe entry."""
    raise NotImplementedError('TODO: implement')

def snapshot(runner=..., resolv_text=None, os_name=None, exe_resolver=None):
    raise NotImplementedError('TODO: implement')

def _key(l):
    raise NotImplementedError('TODO: implement')

def allowed_listeners(path=None):
    """Reviewed (proto, port, prog) listeners from data/netguard/allow_listen.json.
    2026-11-19 Magi 10: an exact-match allow list with recorded evidence, narrower than `learn` (which accepts
    EVERYTHING currently exposed, including unreviewed LAN devices). Missing/unreadable file allows nothing."""
    raise NotImplementedError('TODO: implement')

def compare(base, now, allow=None, exes=None):
    """Return {key: text}. Pure; tests call it directly (allow=set() disables the on-disk allow list,
    exes=[] disables the on-disk allow_exe.json executable list)."""
    raise NotImplementedError('TODO: implement')

def posture(runner=..., os_name=None):
    """Is a supported host firewall actually on? Readable without root. Returns {key: text}."""
    raise NotImplementedError('TODO: implement')

def paths(host=..., d=None):
    raise NotImplementedError('TODO: implement')

def _redact(text):
    """Mask the value after password/token/secret/key words (name=value, name: value or name value)."""
    raise NotImplementedError('TODO: implement')

def _sha(path):
    raise NotImplementedError('TODO: implement')

def _write_learn_receipt(base_p, before, tool, accepted=None):
    """One JSON line per successful learn, appended with a single os.write (Syncthing-safe, per-host file).
    A failure here only warns on stderr; it never blocks learn. No secrets, no file contents."""
    raise NotImplementedError('TODO: implement')

def learn(d=None, runner=..., os_name=None):
    raise NotImplementedError('TODO: implement')

class LearnRefused(Exception):
    """learn --only was asked for a key that is not a current, baseline-acceptable finding."""

def learn_only(keys, d=None, runner=..., os_name=None, allow=None):
    """Accept ONLY the named findings (exact keys printed by `check`); every other finding stays open.
    Raises LearnRefused (baseline untouched) for an unknown key or a finding no baseline can accept."""
    raise NotImplementedError('TODO: implement')

def check(d=None, runner=..., os_name=None):
    raise NotImplementedError('TODO: implement')

def alarm_problems(now=None, d=None):
    """Used by ethan_alarm: findings from the saved receipt; a quiet sensor is itself a problem. Never raises."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
