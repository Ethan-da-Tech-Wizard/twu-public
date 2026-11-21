#!/usr/bin/env bash
# PROGRAM:       magi_mcp_launch.sh - Implementation component for magi_mcp_launch.sh.
# PROGRAMMER:    Magi 6 (antigravity)
# LAST MODIFIED: 2026-11-21 09:37 MST, example_host
# PURPOSE:       Implementation component for magi_mcp_launch.sh.
#
# CHANGE HISTORY:
#   2026-11-21 09:37  Magi 6 (antigravity)  Aligned with work contract end conditions.

# Used by .gemini/settings.json. An explicit MAGI_SEAT permits that assigned
# seat's bounded mailbox actions; an absent seat is deliberately read-only.
set -euo pipefail
