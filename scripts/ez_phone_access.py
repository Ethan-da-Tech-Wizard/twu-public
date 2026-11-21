# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Private EZ phone pairing; no hosted account, network calls or automatic setup.

A paired browser controls this computer's Briar profile, not a new peer identity.
Pairing uses an explicitly configured LAN, mDNS, onion or HTTPS origin. Device
sessions are origin-bound HMAC credentials; proxy account headers grant no access.

PROGRAM: scripts/ez_phone_access.py
PROGRAMMER: existing author; comments by Magi seat 5 (Claude)
LAST MODIFIED: 2026-11-21
PURPOSE:
    Owns phone pairing and device sessions for the browser dashboard. A pairing
    URL carries a single-use token; redeeming it yields a 24 h signed session
    cookie and a long-lived trusted-device cookie, both bound to the configured
    origin and transport. Also validates proxy headers (exact Host and Origin,
    no forged forwarding, no cross-site) before any credential is considered.
    Why: a phone should join over a LAN, mDNS, onion or HTTPS address with no
    hosted account, and the host must be able to revoke each device.
    Invariants: no network calls and no automatic setup; only hashes of tokens
    and keys are stored (the signing key is private to the state file); files
    are 0600 in 0700 directories outside the workspace, opened without
    following symlinks; unsafe or invalid state fails closed.
    Upstream: the dashboard server calls validate_proxy, issue_pairing,
    redeem, authenticate, renew, devices and revoke. Downstream: ez_safe_path.
    ez_project_access reuses normalize_origin and the cookie parser.
"""
from __future__ import annotations
from contextlib import contextmanager
import fcntl
import hashlib
import hmac
import ipaddress
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

def _cookie_value(header, name):
    """Extract one cookie's value from a Cookie header.

    Args:
        header: Raw Cookie header text.
        name: Cookie name to find.
    Returns:
        The stripped value, or None if the header is not a string, longer than
        4096 chars, or the name is missing or repeated (a duplicate is ambiguous
        and treated as absent, so a smuggled second value cannot win).
    """
    raise NotImplementedError('TODO: implement')

def _cookie(name, value, origin, ttl):
    """Format a Set-Cookie value for this origin.

    Args:
        name: Cookie name.
        value: Cookie value.
        origin: Configured origin; https adds the Secure flag.
        ttl: Max-Age in seconds.
    Returns:
        A HttpOnly, SameSite=Strict, Path=/ cookie string.
    """
    raise NotImplementedError('TODO: implement')

def normalize_origin(value, allow_root_path=False):
    """Admit one exact authority; public cleartext HTTP is never a pairing origin."""
    raise NotImplementedError('TODO: implement')

def _binding(config):
    """Hash the origin and transport into a binding tag stored with each credential.

    Args:
        config: Dict with 'origin' and 'transport'.
    Returns:
        64-hex sha256. Credentials created for one origin fail checks under another.
    """
    raise NotImplementedError('TODO: implement')

def _session_signature(key, nonce, expiry, config):
    """Compute the HMAC-SHA256 signature of a session.

    Args:
        key: Hex signing key held in the private state file.
        nonce: Random session nonce.
        expiry: Expiry timestamp (int or its decimal string).
        config: Dict with 'origin' and 'transport'; both are signed in.
    Returns:
        64-hex signature over a versioned message, so a session cannot be moved
        to another origin or have its expiry edited.
    """
    raise NotImplementedError('TODO: implement')

def _default_directory():
    """Return the default private configuration directory (honours XDG_STATE_HOME)."""
    raise NotImplementedError('TODO: implement')

@contextmanager
def _parent(path, create=False, base=None):
    """Open the private directory that holds a credential file.

    Args:
        path: File whose parent directory is opened.
        create: If True, missing directories are created with mode 0700.
        base: Optional trusted base for tests; resolved once.
    Yields:
        (directory file descriptor, file name).
    Raises:
        ValueError: if the path is inside the shared workspace or the directory is
        not owned by us or is accessible to others.
        FileNotFoundError: if a component is missing and create is False.
    """
    raise NotImplementedError('TODO: implement')

def _read_at(folder, name):
    """Read and parse a small private JSON object.

    Args:
        folder: Open directory descriptor.
        name: File name within it.
    Returns:
        The parsed dict.
    Raises:
        ValueError: for unsafe permissions, links, size over MAX_BYTES, or non-object JSON.
        FileNotFoundError: if absent.
    """
    raise NotImplementedError('TODO: implement')

def load_config(path=None):
    """Read explicitly installed configuration; absent config means disabled."""
    raise NotImplementedError('TODO: implement')

def configured(path=None):
    """Report whether phone access is configured and valid.

    Args:
        path: Config path or None for the default.
    Returns:
        True only if a valid config can be loaded; any error means False (never raises).
    """
    raise NotImplementedError('TODO: implement')

def _headers(headers):
    """Group header values by lowercase name.

    Args:
        headers: Mapping with items() that may repeat names (e.g. email.message.Message).
    Returns:
        Dict of lowercase name -> list of values, so duplicate headers can be detected.
    """
    raise NotImplementedError('TODO: implement')

class PhoneAccess:
    """Origin-bound pairing and device-session store for a phone browser.

    Owns two files next to each other: the config (origin and transport) and a
    state file with a signing key, pending pairings and device sessions. Only
    hashes are stored for pairing tokens and keys. Every credential is bound to the
    configured origin and transport. Mutations hold an exclusive lock and replace
    the state file atomically.
    """

    def __init__(self, config_path=None, state_path=None, clock=...):
        """Remember where config and state live (nothing is read or created here).

        Args:
            config_path: Config file; defaults under the user's state directory.
            state_path: Session state file; defaults next to the config.
            clock: Callable returning seconds (replaced in tests).
        """
        raise NotImplementedError('TODO: implement')

    def load_config(self):
        """Load this instance's config; see the module-level load_config."""
        raise NotImplementedError('TODO: implement')

    def configured(self):
        """Return True when this instance's config is valid; never raises."""
        raise NotImplementedError('TODO: implement')

    def validate_proxy(self, headers, client_ip, mutation=False):
        """Check transport admission only; a pairing token/session is still required."""
        raise NotImplementedError('TODO: implement')

    @contextmanager
    def _state(self, mutate=False):
        """Open the state file under the proper lock and yield its content.

        Args:
            mutate: If True, take an exclusive lock, create the directory if needed
                and write the (possibly modified) state back atomically on exit.
        Yields:
            The state dict (schema, signing key, pairings, sessions).
        Raises:
            ValueError: for unsafe files or locks, invalid state, an invalid signing
            key, or a state larger than MAX_BYTES.
        Side effects: when mutating, creates a lock file and temp file (0600), fsyncs
        and renames over the state file. If the body raises, nothing is written.
        """
        raise NotImplementedError('TODO: implement')

    def _prune(self, state, config=None):
        """Delete malformed or expired pairings and sessions in place.

        Args:
            state: State dict, modified.
            config: Unused here; kept for symmetry with other helpers.
        Trusted sessions (with a device key) are kept after expiry so the device
        stays listed and can be renewed until explicitly revoked.
        """
        raise NotImplementedError('TODO: implement')

    @staticmethod
    def _trusted_row(row):
        """Return True if a session row carries a valid device-key hash."""
        raise NotImplementedError('TODO: implement')

    def _trusted(self, state, header, config):
        """Match a trusted-device cookie to a stored session.

        Args:
            state: State dict.
            header: Cookie header.
            config: Current config (for the origin binding).
        Returns:
            (device id, row, normalised cookie value) or None when the cookie is
            malformed, the device is unknown, the origin differs, or the key hash does
            not match (constant-time comparisons).
        """
        raise NotImplementedError('TODO: implement')

    def _session_row(self, state, header, config):
        """Match a signed short-session cookie to a stored session.

        Args:
            state: State dict.
            header: Cookie header.
            config: Current config.
        Returns:
            (device id, row) or None. Checks the format, schema 2, expiry, the HMAC
            signature and the stored nonce hash and origin binding.
        """
        raise NotImplementedError('TODO: implement')

    def _now(self):
        """Return the clock value.

        Raises:
            ValueError: unless it is a finite, non-negative int or float.
        """
        raise NotImplementedError('TODO: implement')

    def issue_pairing(self, device_name=..., ttl=300):
        """Create a pending pairing and return its one-time URL.

        Args:
            device_name: Label (1-80 chars, no control characters).
            ttl: Lifetime in seconds, 30 to 600.
        Returns:
            Dict with 'url' (token in the fragment) and 'expires_at'.
        Raises:
            ValueError: if unconfigured, inputs are invalid or 8 pairings are pending.
        Side effects: exclusive lock; stores only the token's sha256.
        """
        raise NotImplementedError('TODO: implement')

    def redeem(self, token):
        """Exchange a pairing token for a device session.

        Args:
            token: Raw token from the pairing URL.
        Returns:
            Dict with 'cookie', 'device_cookie', 'device_id' and 'expires_at'.
        Raises:
            ValueError: for an invalid, expired, used or other-origin pairing, an
            unconfigured service, or when 32 devices are already paired.
        Side effects: exclusive lock; the pairing is deleted so it works once.
        """
        raise NotImplementedError('TODO: implement')

    def authenticate(self, cookie):
        """Check a Cookie header for a valid trusted device or signed session.

        Args:
            cookie: Raw Cookie header text.
        Returns:
            True or False; any problem (unconfigured, bad input, unsafe storage) is False.
        """
        raise NotImplementedError('TODO: implement')

    def renew(self, cookie):
        """Silently renew a short session only with a persistent trusted key."""
        raise NotImplementedError('TODO: implement')

    def devices(self):
        """List this origin's paired devices.

        Returns:
            A list of dicts (id, name, expiry, creation and last-seen times, trusted
            flag). Empty if unconfigured, legacy state or no state file.
        """
        raise NotImplementedError('TODO: implement')

    def last_pair_time(self):
        """Non-secret timestamp retained even when every device is revoked."""
        raise NotImplementedError('TODO: implement')

    def revoke(self, device_id=None):
        """Revoke one device, or all devices and pending pairings.

        Args:
            device_id: 32-hex id, or None for everything.
        Returns:
            Number of removed sessions.
        Raises:
            ValueError: for an invalid id.
        Side effects: exclusive lock and atomic save.
        """
        raise NotImplementedError('TODO: implement')
