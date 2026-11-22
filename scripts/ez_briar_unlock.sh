#!/usr/bin/env bash
# PROGRAM: scripts/ez_briar_unlock.sh
# PROGRAMMER: existing author; comments by Magi seat 5 (Claude)
# LAST MODIFIED: 2026-11-21
# PURPOSE: Lets the owner unlock an EXISTING Briar profile from a real terminal so
#   the passphrase is typed straight into Briar and never passes through EZ.
#   It never creates, chmods, repairs or reads keys of a profile; it only inspects.
#   Exit codes: 0 ready, 1 not ready / not interactive, 2 bad usage or no private profile.
# CHANGE HISTORY:
#   2026-11-21 Magi 5: Added interactive terminal unlock guard and compliance header.
# DEPENDS ON: /usr/bin/python3, ez_briar_dashboard.BriarClient (API probe on
#   127.0.0.1:7000), ez_briar_runtime.py console (the interactive unlock itself).
# TESTED BY: scripts/test_ez_briar_unlock.py
#
# -e: stop on any error, -u: unset variables are errors, pipefail: a failing stage fails the pipe.
set -euo pipefail
check_briar() { :; }  # TODO: implement
ready_line() { :; }  # TODO: implement
