# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Single-use project invitations and private device sessions, without cloud signup.

This grants one shared coding project only. The HTTP caller must separately
authenticate owner-management routes and check that the project exists.

PROGRAM: scripts/ez_project_access.py
PROGRAMMER: existing author; comments by Magi seat 5 (Claude)
LAST MODIFIED: 2026-11-21
PURPOSE:
    Owns invitation, session and trusted-device state for shared projects.
    Why: a partner should join one project from a link, with no account and no
    cloud service, and the host must be able to list and revoke each device.
    Invariants: only sha256 hashes are stored; invites are single use and last
    at most 300 s; every device is bound to one project, one role and one
    origin; state is a private (0600/0700) non-symlinked file outside the
    workspace, replaced atomically under a non-blocking file lock; unreadable
    or invalid state fails closed (503) and is never overwritten.
    Upstream: owner-authenticated routes call issue_invite/revoke; request
    handlers call authenticate/renew. Downstream: ez_safe_path (directory
    resolution) and ez_phone_access (origin and cookie parsing). The helpers
    _directory, _project and _regular are also reused by ez_briar_seat.
"""
from __future__ import annotations
from contextlib import contextmanager
import fcntl
import hashlib
import hmac
import json
import math
import os
from pathlib import Path
import re
import secrets
import stat
import time
from urllib.parse import urlsplit
from ez_safe_path import split_base

class ProjectAccessError(ValueError):
    """Error with an HTTP-style status for the route layer.

    Subclasses ValueError. Messages are user-safe and never contain tokens or
    hashes. Attributes:
        status: 400 bad input, 403 invalid token, 409 busy, 429 limit, 503 storage.
    """

    def __init__(self, message, status=400):
        """Build the error.

        Args:
            message: Neutral text safe to show to a caller.
            status: HTTP-style code, 400 by default.
        """
        raise NotImplementedError('TODO: implement')

def _hash(value):
    """Return the lowercase hex sha256 of an ASCII string.

    Args:
        value: Token, key or origin text; must be ASCII.
    Returns:
        64 hex characters. Only these hashes are ever written to disk.
    Raises:
        UnicodeEncodeError: if value is not ASCII.
    """
    raise NotImplementedError('TODO: implement')

def _project(value):
    """Validate a project identifier.

    Args:
        value: Candidate name.
    Returns:
        The same string when it is 1 to 48 chars of lowercase letters, digits and
        hyphens starting with a letter or digit.
    Raises:
        ProjectAccessError: (400) for anything else, including path-like names.
    """
    raise NotImplementedError('TODO: implement')

def _origin(value):
    """Normalise a configured origin, or pass None through.

    Args:
        value: Origin string such as an https or onion address, or None.
    Returns:
        The normalised origin, or None when value is None.
    Raises:
        ProjectAccessError: if the origin is not an accepted kind.
    """
    raise NotImplementedError('TODO: implement')

def _directory(path, base=None):
    """Open (creating, mode 0700) the private state directory and return its fd.

    The trusted base is resolved once (ez_safe_path) so system symlinks such as
    macOS /var or /tmp work; every component below it is opened with O_NOFOLLOW so
    a planted symlink is still refused.
    """
    raise NotImplementedError('TODO: implement')

def _regular(descriptor, name, maximum):
    """Read a small private file relative to an open directory.

    Args:
        descriptor: Open directory file descriptor.
        name: File name inside it.
        maximum: Largest acceptable size in bytes.
    Returns:
        The file's bytes.
    Raises:
        FileNotFoundError: if absent (callers treat this as empty state).
        ProjectAccessError: (503) if it is not a private regular single-link file
        owned by us, or exceeds maximum.
    """
    raise NotImplementedError('TODO: implement')

class ProjectAccess:
    """File-backed store of single-use invites, sessions and trusted devices.

    State is one JSON file (hashes only) guarded by a lock file next to it. Each
    public method takes the lock, loads and validates the file, may change it and
    saves atomically. A device only works for the origin it was invited for.
    Args are documented on __init__.
    """

    def __init__(self, state_path=None, clock=..., origin=None):
        """Configure the store (no state file is created yet).

        Args:
            state_path: Location of the JSON state file; defaults under the user's
                local state directory.
            clock: Callable returning the current time in seconds (replaced in tests).
            origin: The verified origin invites are issued for, or None (invites refused).
        Raises:
            ProjectAccessError: for '..' in the path, a path inside the shared workspace,
            an unsafe file name, an invalid origin or an unsafe parent directory.
        """
        raise NotImplementedError('TODO: implement')

    def _now(self):
        """Return the current time, validated.

        Returns:
            A finite non-negative int or float.
        Raises:
            ProjectAccessError: (503) if the clock misbehaves; bool is rejected too.
        """
        raise NotImplementedError('TODO: implement')

    @contextmanager
    def _locked(self, exclusive=True):
        """Hold the file lock and yield the private directory descriptor.

        Args:
            exclusive: True for a writer lock; False for a shared reader lock.
        Raises:
            ProjectAccessError: 503 for unsafe or replaced storage, 409 when another
            holder has the lock (it never waits).
        Side effects: may create the lock file (mode 0600); always closes both
        descriptors when the block ends.
        """
        raise NotImplementedError('TODO: implement')

    def _load(self, fd):
        """Read and validate the state file.

        Args:
            fd: Directory descriptor from _locked.
        Returns:
            The state dict; a fresh empty state when the file does not exist.
        Raises:
            ProjectAccessError: (503) for bad JSON, wrong schema, too many rows or any
            malformed row. The file is left untouched so nothing is lost.
        """
        raise NotImplementedError('TODO: implement')

    def _save(self, fd, data):
        """Write the state atomically.

        Args:
            fd: Directory descriptor from _locked.
            data: State dict to store.
        Raises:
            ProjectAccessError: (503) if the encoded size exceeds MAX_STATE.
        Side effects: writes a temp file (0600), fsyncs, renames it over the state
        file and fsyncs the directory; the temp file is removed if anything fails.
        """
        raise NotImplementedError('TODO: implement')

    def _purge(self, data, now):
        """Drop expired rows in place.

        Args:
            data: State dict, modified.
            now: Current time.
        Sessions with a trusted-device key are kept after expiry so the device stays
        listed and renewable until explicitly revoked.
        """
        raise NotImplementedError('TODO: implement')

    def issue_invite(self, project, role=..., device_name=..., ttl=300):
        """Create a single-use invitation and store only its hash.

        Args:
            project: Project identifier.
            role: 'viewer' or 'editor'.
            device_name: Label for the invited device (1-80 printable characters).
            ttl: Lifetime in whole seconds, 1 to 300.
        Returns:
            Dict with the join url (token in the URL fragment), project, role,
            device_name, expires and scope 'project-only'. The raw token appears only here.
        Raises:
            ProjectAccessError: 503 without a configured origin, 400 for bad input,
            429 when 20 invites are already active.
        Side effects: takes the exclusive lock and rewrites the state file.
        """
        raise NotImplementedError('TODO: implement')

    def invite(self, project, role=..., device_name=..., base_url=None, ttl=300):
        """Issue an invitation, optionally checking a caller-supplied base URL.

        Args:
            project, role, device_name, ttl: as for issue_invite.
            base_url: Optional origin the caller expects; must equal the configured one.
        Returns:
            Same as issue_invite.
        Raises:
            ProjectAccessError: if base_url names a different origin.
        """
        raise NotImplementedError('TODO: implement')

    def redeem(self, token):
        """Exchange an invite token for a session and a trusted-device key.

        Args:
            token: Raw invite token from the join link.
        Returns:
            Dict with 'cookie' and 'device_cookie' Set-Cookie strings plus the public
            device fields.
        Raises:
            ProjectAccessError: 503 without an origin, 403 for any wrong, used,
            expired or other-origin token, 429 when 32 sessions already exist.
        Side effects: exclusive lock; deletes the invite and stores the new session
        in one atomic save, so a token works once.
        """
        raise NotImplementedError('TODO: implement')

    def _cookie(self, name, value, ttl):
        """Format a Set-Cookie value.

        Args:
            name: Cookie name.
            value: Cookie value.
            ttl: Max-Age in seconds.
        Returns:
            A HttpOnly, SameSite=Strict cookie, marked Secure on https origins only.
        """
        raise NotImplementedError('TODO: implement')

    @staticmethod
    def _public(record):
        """Project a stored row into the fields safe to return to callers.

        Args:
            record: Session row.
        Returns:
            Dict with project, role, device id/name, timestamps and a trusted flag;
            never any hash.
        """
        raise NotImplementedError('TODO: implement')

    def _trusted(self, data, cookie):
        """Find the session row matching a trusted-device cookie.

        Args:
            data: Loaded state.
            cookie: Raw Cookie header (or a bare value).
        Returns:
            (row, normalised device cookie value) or None.
        The row must match device id, key hash and this origin.
        """
        raise NotImplementedError('TODO: implement')

    def _session_row(self, data, cookie):
        """Find the unexpired session row for a cookie.

        Args:
            data: Loaded state.
            cookie: Raw session token or a Cookie header.
        Returns:
            The matching row, or None for malformed, unknown, expired or other-origin input.
        """
        raise NotImplementedError('TODO: implement')

    def authenticate(self, cookie):
        """Identify the caller from a cookie, without changing state.

        Args:
            cookie: Cookie header string (at most 4096 chars).
        Returns:
            The public device dict, or None. The trusted-device key is tried first,
            then the short session cookie.
        Takes a shared lock, so many readers may run together.
        """
        raise NotImplementedError('TODO: implement')

    def renew(self, cookie):
        """Renew a project session from its origin/project-bound trusted key."""
        raise NotImplementedError('TODO: implement')

    def devices(self, project):
        """List devices for a project on this origin.

        Args:
            project: Project identifier.
        Returns:
            A list of public device dicts: unexpired sessions plus trusted devices.
            Empty when no origin is configured.
        """
        raise NotImplementedError('TODO: implement')

    def revoke(self, project, device_id=None):
        """Remove a device, or everything for a project.

        Args:
            project: Project identifier.
            device_id: 32-hex device id; None removes all invites and sessions of the project.
        Returns:
            Dict with the number of removed rows and the project.
        Raises:
            ProjectAccessError: (400) for an invalid device id.
        Side effects: exclusive lock and an atomic save.
        """
        raise NotImplementedError('TODO: implement')
