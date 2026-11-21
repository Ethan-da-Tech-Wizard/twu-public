#!/usr/bin/env bash
# PROGRAM:       example_host_browser_gate.sh - Implementation component for example_host_browser_gate.sh.
# PROGRAMMER:    Magi 6 (antigravity)
# LAST MODIFIED: 2026-11-21 09:37 MST, example_host
# PURPOSE:       Implementation component for example_host_browser_gate.sh.
#
# CHANGE HISTORY:
#   2026-11-21 09:37  Magi 6 (antigravity)  Aligned with work contract end conditions.

# Point browser download folders at ~/Downloads/.twu-staging (watched by the download safety daemon).
#   example_host_browser_gate.sh --check   report per browser/profile: ok / needs-apply / running
#   example_host_browser_gate.sh --apply   apply what is safe now; for a RUNNING Chromium/Brave prints 'quit X then re-run'
# Firefox: user.js block (read at next start; safe while running). Chromium/Brave: edits Preferences only when the
# browser is NOT running (it rewrites Preferences on exit), after a .twu-bak backup. Never kills a browser.
set -u
running() { :; }  # TODO: implement
firefox_profiles() { :; }  # TODO: implement
do_firefox() { :; }  # TODO: implement
do_chromium_like() { :; }  # TODO: implement
