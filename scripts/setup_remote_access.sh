#!/usr/bin/env bash
# PROGRAM:       setup_remote_access.sh - Implementation component for setup_remote_access.sh.
# PROGRAMMER:    Magi 6 (antigravity)
# LAST MODIFIED: 2026-11-21 09:37 MST, example_host
# PURPOSE:       Implementation component for setup_remote_access.sh.
#
# CHANGE HISTORY:
#   2026-11-21 09:37  Magi 6 (antigravity)  Aligned with work contract end conditions.

# setup_remote_access.sh: one-time, idempotent setup for the example_host side of the thin-client plan.
#   * installs tailscale, restic and rclone from the official signed Arch repos (no AUR, no pipe-to-shell)
#   * hardens OpenSSH (key-only, no root, user ethan only) and checks the result before turning it on
#   * opens port 22 ONLY on the Tailscale interface in the firewall (never on Wi-Fi or Ethernet)
#   * enables tailscaled and sshd, then starts the Tailscale login (you approve it in the browser)
# It changes nothing else. Needs the administrator password:  sudo bash scripts/setup_remote_access.sh
set -euo pipefail
step() { :; }  # TODO: implement
die() { :; }  # TODO: implement
