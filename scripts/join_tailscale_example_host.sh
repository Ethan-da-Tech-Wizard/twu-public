#!/bin/bash
# PROGRAM:       join_tailscale_example_host.sh - Implementation component for join_tailscale_example_host.sh.
# PROGRAMMER:    Magi 6 (antigravity)
# LAST MODIFIED: 2026-11-21 09:37 MST, example_host
# PURPOSE:       Implementation component for join_tailscale_example_host.sh.
#
# CHANGE HISTORY:
#   2026-11-21 09:37  Magi 6 (antigravity)  Aligned with work contract end conditions.

# Run on example_host (one command):  bash ~/TWU_LLC/scripts/join_tailscale_example_host.sh
# Installs Tailscale if missing, starts it, and prints a login link. Open the link on your phone and sign in with your usual
# account. Then it prints this box's Tailscale address. Safe to run again.
set -u
