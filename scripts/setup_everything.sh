#!/usr/bin/env bash
# PROGRAM:       setup_everything.sh - Implementation component for setup_everything.sh.
# PROGRAMMER:    Magi 6 (antigravity)
# LAST MODIFIED: 2026-11-21 09:37 MST, example_host
# PURPOSE:       Implementation component for setup_everything.sh.
#
# CHANGE HISTORY:
#   2026-11-21 09:37  Magi 6 (antigravity)  Aligned with work contract end conditions.

# setup_everything.sh: the ONE command for the example_host side of the thin-client plan.
#   bash ~/TWU_LLC/scripts/setup_everything.sh
# You will be asked for: (1) your computer password once, (2) one click in the browser to approve Tailscale,
# (3) one click in the browser to let the backup use Google Drive, (4) to save a passphrase it shows you.
# Everything else is automatic. Run it in a normal terminal window, not through Claude.
set -euo pipefail
