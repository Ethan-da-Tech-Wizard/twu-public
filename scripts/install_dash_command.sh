#!/bin/bash
# PROGRAM:       install_dash_command.sh - make `dash` open Yggdrasil on this Linux box
# PROGRAMMER:    Ethan Paul example_host / TWU LLC Sovereign Fleet
# LAST MODIFIED: 2026-11-21
# PURPOSE:       User-level only (no sudo, no root, no system files). Does two things:
#                1. appends ONE clearly marked block to ~/.bashrc and ~/.zshrc (only the files
#                   that already exist) defining a `dash` function: no arguments -> this repo's
#                   scripts/dash (opens Yggdrasil); arguments -> /bin/dash (POSIX shell).
#                2. links ~/.local/bin/dash to this repo's scripts/dash for non-interactive use.
#                Idempotent: running it again replaces the block, never duplicates it.
# USAGE:         scripts/install_dash_command.sh            install / refresh
#                scripts/install_dash_command.sh --status   report only (exit 0 = fully installed)
#                scripts/install_dash_command.sh --remove   take the blocks and the link out again
#                --force   allow running on macOS (the Mac already has its own function in ~/.zshrc)
# DOCS:          docs/DASH_COMMAND.md
# HOME is honoured, so tests can point it at a temp directory.

set -u
block() { :; }  # TODO: implement
has_block() { :; }  # TODO: implement
strip_block() { :; }  # TODO: implement
rewrite() { :; }  # TODO: implement
link_is_ours() { :; }  # TODO: implement
status() { :; }  # TODO: implement
