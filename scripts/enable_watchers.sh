#!/bin/bash
# PROGRAM:       enable_watchers.sh - Implementation component for enable_watchers.sh.
# PROGRAMMER:    Magi 6 (antigravity)
# LAST MODIFIED: 2026-11-21 09:37 MST, example_host
# PURPOSE:       Implementation component for enable_watchers.sh.
#
# CHANGE HISTORY:
#   2026-11-21 09:37  Magi 6 (antigravity)  Aligned with work contract end conditions.

# enable_watchers.sh - ONE command that turns on the GitHub leak watch + stale sweep on THIS machine, whatever it is (Mac or Linux).
#   bash scripts/enable_watchers.sh            install and start (safe to re-run)
#   bash scripts/enable_watchers.sh --check    show whether they are running here
#   bash scripts/enable_watchers.sh --dry-run  write the files but do not start anything
# Mac: installs the three user LaunchAgents (leak watch, stale sweep, and the catch-up runner that runs every scheduled job missed while the Mac was off or asleep). Linux: copies the units from MAGI_0/ into ~/.config/systemd/user (workspace path filled in),
# reloads systemd and starts the timers. It also installs the short launchers (twu-fix, twu-status, twu-find, twu-watch) into ~/.local/bin so
# commands work from any folder. No sudo, no network. It never touches another machine: run it ON each machine (a Linux box also runs it by itself,
# through freshness_sentinel.py, so nobody has to).
set -u
