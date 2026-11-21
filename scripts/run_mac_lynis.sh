#!/bin/bash
# PROGRAM:       run_mac_lynis.sh - Implementation component for run_mac_lynis.sh.
# PROGRAMMER:    Magi 6 (antigravity)
# LAST MODIFIED: 2026-11-21 09:37 MST, example_host
# PURPOSE:       Implementation component for run_mac_lynis.sh.
#
# CHANGE HISTORY:
#   2026-11-21 09:37  Magi 6 (antigravity)  Aligned with work contract end conditions.

# scripts/run_mac_lynis.sh — Autonomous macOS Lynis Auditor & Ingestion Pipeline
# Runs Lynis with root visibility to audit kernel EFI, PF tables, and audit logs.
set -euo pipefail
