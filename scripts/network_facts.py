# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Read-only network facts for every computer and phone.

WHAT IT KNOWS AND WHERE IT COMES FROM (nothing is invented; a missing fact is the word "unknown"):
  * THIS computer, live:   `ip -j addr`, `ip -j route`, `nmcli -t -f ACTIVE,SSID,SIGNAL dev wifi` (no sudo, no scan,
                           never a Wi-Fi password: the nmcli field list names no secret).
  * OTHER computers:       only already-synced files: data/netguard/baseline.<host>.json (gateway, gateway MAC, DNS
                           resolvers, neighbour count, the time it was recorded). Those files carry NO netmask, IP or
                           Wi-Fi name, so those show "unknown" for other computers, with the age of the record.
  * PHONES:                data/magi_phone/cluster_nodes.json (address and status the MagiPhone service reports).

PRIVACY RULES (kept from the existing network panel, registry id panel:network, owner magi11):
  * MAC addresses are redacted to their last 3 bytes.
  * `public_summary()` contains NO IP address and NO MAC: it is safe for the public dashboard card.
  * `owner_detail()` contains the addresses and must only be shown behind the owner unlock (/network).
  * Nothing here writes a file, runs sudo, or contacts the network.
"""
from __future__ import annotations
import ipaddress
import json
import socket
import subprocess
import time
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

def run(argv: List[str], timeout: int=5) -> str:
    """Run one read-only command (no shell). Returns stdout, or '' on any failure."""
    raise NotImplementedError('TODO: implement')

def redact_mac(mac: Optional[str]) -> str:
    """'00:00:5e:00:53:00' -> '**:**:**:28:d9:0a' (keep the last 3 bytes only). Anything odd -> 'unknown'."""
    raise NotImplementedError('TODO: implement')

def prefix_to_mask(prefix: int) -> str:
    """24 -> '255.255.255.0'."""
    raise NotImplementedError('TODO: implement')

def age_text(then: Optional[float], now: Optional[float]=None) -> str:
    """Seconds since `then` as '5 min', '3.2 h', '2.1 days', or 'unknown'."""
    raise NotImplementedError('TODO: implement')

def local_facts(runner: Callable[[List[str]], str]=...) -> Dict[str, Any]:
    """Live facts of THIS computer. `runner` is injectable so tests never touch the real system."""
    raise NotImplementedError('TODO: implement')

def peer_facts(root: Path=..., now: Optional[float]=None) -> List[Dict[str, Any]]:
    """Facts for the other computers, read only from synced netguard baselines. Missing file or field -> unknown."""
    raise NotImplementedError('TODO: implement')

def phone_facts(root: Path=...) -> List[Dict[str, Any]]:
    """Phones/other nodes the MagiPhone service lists (non-local entries only); address and status as reported."""
    raise NotImplementedError('TODO: implement')

def owner_detail(root: Path=..., runner: Callable[[List[str]], str]=...) -> Dict[str, Any]:
    """Everything, including addresses. ONLY for the owner-unlocked view."""
    raise NotImplementedError('TODO: implement')

def public_summary(root: Path=..., runner: Callable[[List[str]], str]=...) -> List[Dict[str, str]]:
    """One line per computer or phone with NO IP and NO MAC: which facts exist and how old they are."""
    raise NotImplementedError('TODO: implement')
