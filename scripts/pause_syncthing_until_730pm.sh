#!/usr/bin/env bash
# PROGRAM:       pause_syncthing_until_730pm.sh - Implementation component for pause_syncthing_until_730pm.sh.
# PROGRAMMER:    Magi 6 (antigravity)
# LAST MODIFIED: 2026-11-21 09:37 MST, example_host
# PURPOSE:       Implementation component for pause_syncthing_until_730pm.sh.
#
# CHANGE HISTORY:
#   2026-11-21 09:37  Magi 6 (antigravity)  Aligned with work contract end conditions.

# ==============================================================================
# scripts/pause_syncthing_until_730pm.sh — Pause Syncthing Until 7:30 PM
# ==============================================================================
# Stops background Syncthing CPU churn immediately while on hotspot,
# and automatically restarts it at 7:30 PM (19:30) local time.
# ==============================================================================
set -euo pipefail
