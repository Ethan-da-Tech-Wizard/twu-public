#!/usr/bin/env bash
# PROGRAM:       example_host_hardware_lock.sh - Implementation component for example_host_hardware_lock.sh.
# PROGRAMMER:    Magi 6 (antigravity)
# LAST MODIFIED: 2026-11-21 09:37 MST, example_host
# PURPOSE:       Implementation component for example_host_hardware_lock.sh.
#
# CHANGE HISTORY:
#   2026-11-21 09:37  Magi 6 (antigravity)  Aligned with work contract end conditions.

# ==============================================================================
# scripts/example_host_hardware_lock.sh — Permanent example_host example_host Hardware Lock
# ==============================================================================
# Permanently locks Touchpad, Display, and Battery/Power settings on example_host 45
# (example_hostPro14,1) so they NEVER revert on AC unplug, sleep/resume, or reboot.
#
# Addresses root causes identified by multi-agent audit:
#   1. GNOME Wayland lacks dconf local.d database and locks -> resets touchpad
#   2. Blind PCI runtime PM autosuspends LPSS SPI controllers (00:15.0, 00:15.2,
#      00:1e.3) -> freezes / lags Apple SPI touchpad and keyboard
#   3. Conflicting power daemons (power-profiles-daemon, tuned, tuned-ppd)
#      fight over EPP and governors on AC unplug
#   4. Broken /usr/local/sbin/twu-responsive-power (orphaned fi from sed)
#
# Usage (run once on example_host with root):
#   sudo bash scripts/example_host_hardware_lock.sh
# ==============================================================================
set -euo pipefail
set -euo pipefail
