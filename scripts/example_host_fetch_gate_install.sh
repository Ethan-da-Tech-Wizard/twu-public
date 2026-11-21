#!/usr/bin/env bash
# PROGRAM:       example_host_fetch_gate_install.sh - Implementation component for example_host_fetch_gate_install.sh.
# PROGRAMMER:    Magi 6 (antigravity)
# LAST MODIFIED: 2026-11-21 09:37 MST, example_host
# PURPOSE:       Implementation component for example_host_fetch_gate_install.sh.
#
# CHANGE HISTORY:
#   2026-11-21 09:37  Magi 6 (antigravity)  Aligned with work contract end conditions.

# Install the TWU fetch gate for this user: wrappers in ~/.local/bin + git fsck config. No sudo. Idempotent.
set -eu
