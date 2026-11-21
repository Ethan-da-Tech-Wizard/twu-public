#!/usr/bin/env bash
# PROGRAM:       ethan_example_host_harden.sh - Implementation component for ethan_example_host_harden.sh.
# PROGRAMMER:    Magi 6 (antigravity)
# LAST MODIFIED: 2026-11-21 09:37 MST, example_host
# PURPOSE:       Implementation component for ethan_example_host_harden.sh.
#
# CHANGE HISTORY:
#   2026-11-21 09:37  Magi 6 (antigravity)  Aligned with work contract end conditions.

# ==============================================================================
# scripts/ethan_example_host_harden.sh — Zero-Impact Security & Power Hardening
# ==============================================================================
# Applies high-value Lynis hardening recommendations and battery/power safety
# on example_host WITHOUT removing compilers or breaking developer workflows.
#
# Changes applied:
# 1. Disable legacy 1990s network protocols (dccp, sctp, rds, tipc) [NETW-3200]
# 2. Disable core dumps in limits.conf to save SSD writes [KRNL-5820]
# 3. Apply standard kernel sysctls (anti-spoof, protected symlinks) [KRNL-6000]
# 4. Set legal login warning banner [BANN-7126]
# 5. Make intel-rapl energy_uj readable by user-space for power benchmarking
# 6. Set ASUS battery charge limit to 80% to protect 57% remaining capacity
#
# Must be run with sudo:
#   sudo bash scripts/ethan_example_host_harden.sh
# ==============================================================================

set -euo pipefail
