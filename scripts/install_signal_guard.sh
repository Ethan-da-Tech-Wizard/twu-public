#!/usr/bin/env bash
# PROGRAM:       install_signal_guard.sh - Implementation component for install_signal_guard.sh.
# PROGRAMMER:    Magi 6 (antigravity)
# LAST MODIFIED: 2026-11-21 09:37 MST, example_host
# PURPOSE:       Implementation component for install_signal_guard.sh.
#
# CHANGE HISTORY:
#   2026-11-21 09:37  Magi 6 (antigravity)  Aligned with work contract end conditions.

# Install the test-time signal guard for EVERY Python on this account of THIS machine (run once per box:
# example_host, example_host, any Mac). Adds two small files to the user's Python site folder; nothing else is touched.
#   scripts/install_signal_guard.sh            install
#   scripts/install_signal_guard.sh --remove   uninstall
#   scripts/install_signal_guard.sh --status   show state
# What it does: while a unittest is loaded, os.kill/os.killpg refuse pid 0/1/-1, mocks, our own group/parent
# (see scripts/signal_guard.py). Production daemons never import unittest, so they are unaffected. Fail-open.
set -euo pipefail
