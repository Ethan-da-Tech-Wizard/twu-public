#!/bin/bash
# ==============================================================================
# Program:       post_login_check.sh
# Programmer:    Ethan-da-Tech-Wizard (written by Seat 10, Mac, Claude, at his direction)
# Last Modified: November 19, 2026
# Purpose:       Runs by itself at every login on the example_host so Ethan does not have to remember a command.
#                It retries for about ten minutes (Wi-Fi and the tunnel are often not ready right after login),
#                starts the twu-mesh tunnel if it is off, runs the read-only reboot_ready checks, and shows ONE
#                notification with the result. It never uses sudo, never changes trust, keys, firewall or tokens.
#                Stop it any time: launchctl bootout gui/$(id -u)/com.twu.post-login-check
# CHANGE HISTORY:
#   2026-11-19 Magi 10: Created automated post-login tunnel and reboot check sentinel.
# ==============================================================================
