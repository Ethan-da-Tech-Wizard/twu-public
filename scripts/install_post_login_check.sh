#!/bin/bash
# ==============================================================================
# Program:       install_post_login_check.sh
# Programmer:    Ethan-da-Tech-Wizard (written by Seat 10, Mac, Claude, at his direction)
# Last Modified: November 19, 2026
# Purpose:       One-time, owner-run installer for the example_host's after-login check. Writes one per-user login item
#                (no sudo) that runs scripts/post_login_check.sh at every login, then loads it.
#                Undo:  launchctl bootout gui/$(id -u)/com.twu.post-login-check && rm ~/Library/LaunchAgents/com.twu.post-login-check.plist
# CHANGE HISTORY:
#   2026-11-19 Magi 10: Created per-user launch item installer.
# ==============================================================================
set -eu
