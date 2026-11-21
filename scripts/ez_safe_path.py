# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/ez_safe_path.py: resolve-the-base-once helper for no-follow directory walks.

PROGRAM: scripts/ez_safe_path.py
PROGRAMMER: Magi seat 5 (Claude)
LAST MODIFIED: 2026-11-21
PURPOSE: EZ_AUDIT item 1. The EZ private-state walkers (project access, phone
  access, Magi workspace, Briar seat) open every path component with O_NOFOLLOW
  starting at "/". That refuses ANY symlink, including harmless system aliases
  such as macOS /var -> /private/var or /tmp, so every test and install that
  lives under such a path failed with NotADirectoryError.
  Fix: choose a trusted BASE, resolve it ONCE with realpath (this is the only
  place symlinks are followed), then walk the remaining components with
  O_NOFOLLOW exactly as before. A symlink planted below the base is still refused.
  Base choice (when the caller gives none): the user's home directory if the path
  is lexically inside it, else the first real directory owned by this user (the
  components above it are root-controlled system locations).
INVARIANTS: no symlink below the base is ever followed; the base is resolved only
  once, before any component is opened; nothing here creates files.
USED BY: ez_project_access._directory, ez_phone_access._parent,
  ez_magi_workspace.Workspace._directory (via the same call), ez_briar_seat.
"""
import os
from pathlib import Path

def _default_base(path: Path) -> Path:
    """Pick the trusted base for `path` (absolute, normalised) when none is supplied.

    Args:
        path: absolute path being opened.

    Returns:
        The directory under which symlinks are NOT trusted.
    """
    raise NotImplementedError('TODO: implement')

def split_base(path, base=None):
    """Split `path` into (resolved base, components to walk with O_NOFOLLOW).

    Args:
        path: target directory (str or Path); made absolute, never resolved.
        base: optional trusted base; symlinks at or above it are followed once.
            Must be a lexical ancestor of (or equal to) `path`.

    Returns:
        (Path resolved_base, tuple of str components below the base).

    Raises:
        ValueError: `path` is not inside `base`, or contains "..".
    """
    raise NotImplementedError('TODO: implement')
