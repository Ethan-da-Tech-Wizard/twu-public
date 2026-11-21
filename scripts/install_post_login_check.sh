#!/bin/bash
# PROGRAM:       install_post_login_check.sh - Implementation component for install_post_login_check.sh.
# PROGRAMMER:    Magi 6 (antigravity)
# LAST MODIFIED: 2026-11-21 09:37 MST, example_host
# PURPOSE:       Implementation component for install_post_login_check.sh.
#
# CHANGE HISTORY:
#   2026-11-21 09:37  Magi 6 (antigravity)  Aligned with work contract end conditions.

# ==============================================================================
# Program:       install_post_login_check.sh
# Programmer:    Ethan-da-Tech-Wizard (written by Seat 10, Mac, Claude, at his direction)
# Last Modified: November 19, 2026
# Purpose:       One-time, owner-run installer for the example_host's after-login check. Writes one per-user login item
#                (no sudo) that runs scripts/post_login_check.sh at every login, then loads it.
#                Undo:  launchctl bootout gui/$(id -u)/com.twu.post-login-check && rm ~/Library/LaunchAgents/com.twu.post-login-check.plist
# ==============================================================================
set -eu
