#!/bin/bash
# PROGRAM:       join_tailscale_mac.sh - Implementation component for join_tailscale_mac.sh.
# PROGRAMMER:    Magi 6 (antigravity)
# LAST MODIFIED: 2026-11-21 09:37 MST, example_host
# PURPOSE:       Implementation component for join_tailscale_mac.sh.
#
# CHANGE HISTORY:
#   2026-11-21 09:37  Magi 6 (antigravity)  Aligned with work contract end conditions.

# Run on the MAC AIR (one command):  bash ~/TWU_LLC/scripts/join_tailscale_mac.sh
# Installs the Tailscale app if missing, opens it and logs in. If it prints a link, open it on your phone and sign in with
# your usual account. Safe to run again.
set -u
