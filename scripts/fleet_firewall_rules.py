# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Fleet firewall + WireGuard snippet generator (READ-ONLY; Magi 23, 2026-11-19).

Ethan's rule: no one boss computer. Every computer must let every OTHER registered computer reach its fleet SSH door
(tcp 2222 on the tunnel) and must list every other computer as a WireGuard peer (a FULL MESH, not a star).

    python3 scripts/fleet_firewall_rules.py --for example_host            # nftables rule + WireGuard [Peer] blocks
    python3 scripts/fleet_firewall_rules.py --for example_host           # macOS: pf anchor snippet + [Peer] blocks
    python3 scripts/fleet_firewall_rules.py --all                   # one section per registered computer
    python3 scripts/fleet_firewall_rules.py --for example_host --root DIR # read DIR/data/fleet_registry.json instead

It only PRINTS text. It never writes a system file, never runs sudo, never reads or prints a private key, and prints
placeholders where a public key or a public/LAN endpoint belongs (the owner fills those in). Addresses are the private
tunnel addresses from the fleet registry, listed one by one (never the whole /24, other WireGuard peers share that subnet).
There is no hub: every computer is treated the same. Every [Peer] block gets PersistentKeepalive 25 (cheap, and it keeps a
laptop's NAT mapping open toward each peer; harmless on a desktop).
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path
import fleet_registry

def _others(reg: dict, me: str) -> dict:
    raise NotImplementedError('TODO: implement')

def nft_lines(reg: dict, me: str) -> list:
    """The nftables rule for `me`: tcp 2222 on wg0 from every OTHER computer's tunnel address, listed explicitly."""
    raise NotImplementedError('TODO: implement')

def pf_lines(reg: dict, me: str) -> list:
    """macOS pf anchor text for `me` (only matters if pf is enabled; the Application Firewall does not filter by port)."""
    raise NotImplementedError('TODO: implement')

def peer_blocks(reg: dict, me: str) -> list:
    """FULL MESH: one [Peer] per other computer. Public keys and endpoints are placeholders. /32 only."""
    raise NotImplementedError('TODO: implement')

def section(reg: dict, me: str) -> str:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
