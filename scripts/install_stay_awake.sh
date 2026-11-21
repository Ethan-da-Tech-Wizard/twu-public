#!/usr/bin/env bash
# PROGRAM:       scripts/install_stay_awake.sh - let this laptop stay awake while plugged in (task 177dfcc2). Run as YOUR user: bash scripts/install_stay_awake.sh
# PROGRAMMER:    Magi 7 (claude, example_host), for Ethan
# LAST MODIFIED: 2026-11-20, example_host
# PURPOSE:       one idempotent command that lets this laptop stay awake while plugged in (see WHAT IT DOES below).
# WHAT IT DOES:  1. (sudo) removes exactly two lock lines from /etc/dconf/db/local.d/locks/01-power, so the screen idle time and the AC sleep
#                   setting can be changed by the user watcher; the DEFAULT values in 01-power stay as they are. Then `dconf update`.
#                2. installs the user unit scripts/units/twu-stay-awake.service and starts it (Nice 19, 5% CPU cap).
# WHAT IT DOES NOT: touch the lid, the power/suspend buttons, battery settings, the power policy, or any other lock.
# UNDO:          bash scripts/install_stay_awake.sh --undo     (re-adds the two lock lines, runs dconf update, stops and removes the unit)
# IDEMPOTENT:    safe to run again.
#
# CHANGE HISTORY:
#   2026-11-20  Magi 7  Created (task 177dfcc2).
set -euo pipefail
