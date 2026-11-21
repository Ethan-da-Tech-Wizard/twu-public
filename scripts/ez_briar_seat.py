# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Project-scoped managed Briar peers; browser guests install no Briar application.

This does not unlock or replace the owner's existing encrypted profile. Guest
profile passwords are machine-generated and remain in owner-private storage.
Only authenticated project routes may invoke this API; authors are server-derived.

PROGRAM: scripts/ez_briar_seat.py
PROGRAMMER: existing author; comments by Magi seat 5 (Claude)
LAST MODIFIED: 2026-11-21
PURPOSE:
    Owns the lifecycle of one isolated Briar peer per project (ManagedPeer) and
    the registry that pairs each peer with the host's Briar profile (BriarSeats).
    Why: web guests must chat over real Briar without installing anything, yet
    must not touch the host's own encrypted profile or the shared source tree.
    Invariants: peers run in a resource-limited systemd user scope behind a
    network namespace; secrets and pinned bindings live in private (0600/0700),
    non-symlinked files outside the workspace; at most two peers are active;
    a revoked binding is never resumed; destructive Briar calls are allow-listed.
    Upstream: authenticated project routes (see ez_project_access) call the
    BriarSeats API. Downstream: ez_briar_dashboard (HTTP client), ez_briar_runtime
    (JAR verification) and the stop latch that can pause all startup.
"""
from __future__ import annotations
import atexit
import fcntl
import json
import os
from pathlib import Path
import pty
import re
import secrets
import select
import shutil
import signal
import socket
import stat
import subprocess
import termios
import threading
import time
from ez_briar_dashboard import BriarClient, BriarError
from ez_briar_runtime import verify_runtime
from ez_project_access import _directory, _project, _regular

class BriarSeatError(ValueError):
    """Raised for any refusal in the managed-peer layer.

    Subclasses ValueError so callers that already catch bad input also catch it.
    Attributes:
        status: HTTP-style status code the route layer should relay (503 default).
    """

    def __init__(self, message, status=503):
        """Build the error.

        Args:
            message: Neutral, user-safe text; never include secrets or prompt bytes.
            status: HTTP-style code; 503 means "temporarily unavailable".
        """
        raise NotImplementedError('TODO: implement')

def _private(path):
    """Validate that a profile directory is private and outside the source tree.

    Args:
        path: Candidate directory for managed-peer state.
    Returns:
        The absolute Path, after confirming it is a safe directory.
    Raises:
        BriarSeatError: if the path contains '..' or sits inside the shared workspace.
    Side effects: opens and immediately closes the directory via the safe opener,
    which may raise if it is a symlink or has unsafe ownership/permissions.
    """
    raise NotImplementedError('TODO: implement')

def _free_port():
    """Ask the OS for a currently unused loopback TCP port.

    Returns:
        An int port number. There is a small race between closing the probe socket
        and the peer binding it; callers accept that and rely on startup failing
        cleanly rather than adopting another process.
    """
    raise NotImplementedError('TODO: implement')

def _request(client, path, payload=None, method=None):
    """Send one request to a Briar API client, allowing only safe deletions.

    Args:
        client: Object with request(path, payload, method=None).
        path: API path, e.g. '/contacts/7' or '/contacts/add/pending'.
        payload: Optional JSON-serialisable body.
        method: None for the client's default verb, or the literal 'DELETE'.
    Returns:
        Whatever the client returns.
    Raises:
        BriarSeatError: for any explicit method other than a DELETE of a numeric
        contact or the pending-contact list; this is an allow-list so that
        project routes can never reach other destructive endpoints.
    """
    raise NotImplementedError('TODO: implement')

class ManagedPeer:
    """One process-owned namespace and inspected JAR; never adopts arbitrary PIDs."""

    def __init__(self, directory, nickname=..., port=None):
        """Create (but do not start) a managed peer description.

        Args:
            directory: Private per-project directory; validated by _private.
            nickname: Display name fed to the Briar account-creation prompt.
            port: Host loopback port for the API; a free port is chosen when omitted.
        Raises:
            BriarSeatError: if the directory is unsafe.
        No process is spawned until start() is called.
        """
        raise NotImplementedError('TODO: implement')

    def _milestone(self, name):
        """Record elapsed milliseconds for a startup stage, first occurrence only.

        Args:
            name: Stage label such as 'process_spawned'.
        No-op before start() set the clock.
        """
        raise NotImplementedError('TODO: implement')

    def _observe_startup(self, raw):
        """Scan terminal output for non-sensitive progress markers.

        Args:
            raw: Bytes just read from the pty.
        Only a timing is kept; addresses, prompts and passwords are discarded.
        """
        raise NotImplementedError('TODO: implement')

    def command(self):
        """Build the isolated launch command line for the Briar JAR.

        Returns:
            argv list: systemd-run user scope with memory/CPU caps, wrapping pasta
            (a user-space network namespace that forwards only one loopback port in)
            wrapping java running the verified runtime JAR.
        Raises:
            BriarSeatError: if pasta, java or systemd-run is not installed.
        Side effects: reads /proc/self/cgroup; runs verify_runtime() which checks the JAR.
        """
        raise NotImplementedError('TODO: implement')

    def _password(self):
        """Load or create the machine-generated profile password.

        Returns:
            The 64-character URL-safe password string.
        Raises:
            BriarSeatError: if an existing secret file has an unexpected format (it is
            preserved, never overwritten).
        Side effects: may create 'profile.secret' with mode 0600, exclusively, no symlink
        following; the directory descriptor is always closed.
        """
        raise NotImplementedError('TODO: implement')

    def _launch(self):
        """Take the profile lock and spawn the isolated peer process.

        Returns:
            The profile password, which start() feeds to the interactive prompts.
        Raises:
            BriarSeatError: if the lock file is unsafe, already held, or the user scope
            never appears in 3 seconds.
        Side effects: honours the global stop latch; opens a pty; sets umask 077 while
        spawning; leaves self.lock, self.master and self.process populated.
        """
        raise NotImplementedError('TODO: implement')

    def start(self, timeout=70):
        """Start the peer, answer its setup prompts and wait for the API.

        Args:
            timeout: Seconds to wait for the API to answer.
        Returns:
            The BriarClient bound to the peer's API.
        Raises:
            BriarSeatError: if closed, if the peer exits early, or on timeout (the
            peer is closed first in the last two cases).
        Side effects: spawns a process and a drain thread; writes prompts to the pty.
        """
        raise NotImplementedError('TODO: implement')

    def _drain(self):
        """Keep reading the pty after startup so the peer never blocks on a full pipe.

        Runs in a daemon thread until closed or the process exits. Output is parsed
        only for timings and then discarded.
        """
        raise NotImplementedError('TODO: implement')

    def close(self):
        """Stop the peer and free its resources (thread-safe, idempotent)."""
        raise NotImplementedError('TODO: implement')

    def _scope_empty(self):
        """Report whether our systemd scope has no running processes.

        Returns:
            True when the scope is gone or provably empty; False when it may still
            hold processes or its state cannot be verified safely (fail closed).
        """
        raise NotImplementedError('TODO: implement')

    def _close_owned(self):
        """Tear down the process tree, pty and lock (caller holds the lifecycle lock).

        Escalates from SIGTERM to SIGKILL on the whole scope, then on the process
        group, then stops the scope, and records cleanup_complete from what it can
        verify. Safe to call repeatedly.
        """
        raise NotImplementedError('TODO: implement')

class BriarSeats:
    """Registry of per-project managed Briar peers and their contact bindings.

    State is a dict project -> row, guarded by self._lock. Row states are
    starting, connecting, ready, unavailable, needs_owner_unlock and revoked.
    At most two peers may be active at once. Downstream: authenticated project
    routes call prepare/list/send/revoke; the owner's own Briar client is used
    for the host side of every pairing.
    """

    def __init__(self, owner=None, directory=None, peer_factory=..., timeout=180):
        """Create the registry.

        Args:
            owner: Client for the host's existing Briar profile (default client if None).
            directory: Where per-project profile directories live.
            peer_factory: Callable building a peer; replaced by fakes in tests.
            timeout: Seconds to allow contact exchange before reporting unavailable.
        Side effects: registers close() to run at interpreter exit.
        """
        raise NotImplementedError('TODO: implement')

    @staticmethod
    def _status(row):
        """Project a row into the public status dict (no internal handles).

        Args:
            row: Internal row with at least a 'state'.
        Returns:
            Dict with state, detail, a suggested action and transport markers;
            briar_delivery is always False here because no delivery is proven.
        """
        raise NotImplementedError('TODO: implement')

    def prepare(self, project):
        """Start (or report) the dedicated Briar peer for a project.

        Args:
            project: Project identifier; validated by _project.
        Returns:
            A status dict. Existing live rows are returned unchanged; otherwise a
            background connect thread is started, unless the owner profile is locked
            (needs_owner_unlock) or two peers are already active (capacity).
        Side effects: takes self._lock; may spawn a daemon thread running _connect.
        """
        raise NotImplementedError('TODO: implement')

    def prewarm_existing(self, projects):
        """Resume at most two previously invited, pinned peers before serving links.

        Discovery reads existing private bindings only. Never manufacture a new
        identity/contact for an uninvited project or resume a revoked binding.
        """
        raise NotImplementedError('TODO: implement')

    def _connect(self, project, row):
        """Background worker: start one peer and pair it with the host profile.

        Args:
            project: Validated project identifier.
            row: The shared state dict for this project, mutated in place.
        Flow: start the guest peer, reuse a matching persisted binding if present,
        otherwise exchange contact links and poll until both sides list each other,
        then persist the new binding. Any failure marks the row unavailable (unless
        revoked) and the peer is closed on the way out.
        Side effects: network calls to both Briar APIs, file writes to the binding,
        and mutations of row under self._lock where noted.
        """
        raise NotImplementedError('TODO: implement')

    @staticmethod
    def _matches_side(binding, contacts, side):
        """Check that a binding's contact for one side exists with the pinned author.

        Args:
            binding: Persisted dict with <side>_contact and <side>_remote_author.
            contacts: Live list of contact dicts.
            side: 'owner' or 'guest'.
        Returns:
            True only if a contact has the same id and author id and the pinned
            author id is not None.
        """
        raise NotImplementedError('TODO: implement')

    @classmethod
    def _matches(cls, binding, own, guest):
        """Return True when both owner and guest contacts match the binding."""
        raise NotImplementedError('TODO: implement')

    @staticmethod
    def _binding(directory, value=None):
        """Read (value None) or atomically write the persisted binding file.

        Args:
            directory: Project directory.
            value: Dict to store, or None to read.
        Returns:
            The dict read ({} when no file), or the dict written.
        Raises:
            BriarSeatError: if the stored JSON is not an object.
        Side effects: writes a temp file and renames it over binding.json (mode 0600,
        no symlink following) so readers never see a partial file.
        """
        raise NotImplementedError('TODO: implement')

    def _ready(self, project):
        """Return the row for a project, starting it if unknown.

        Raises:
            BriarSeatError: 403 if the project was revoked.
        """
        raise NotImplementedError('TODO: implement')

    def list(self, project):
        """List recent messages for a project in a display-safe form.

        Args:
            project: Project identifier.
        Returns:
            Status dict plus 'messages' (last 200). Non-ready rows return an empty list.
            Authors are labelled generically; delivery is 'confirmed' only when the
            peer reports the message seen.
        """
        raise NotImplementedError('TODO: implement')

    def send(self, project, text, author=...):
        """Send a text message on behalf of a project member or the host.

        Args:
            project: Project identifier.
            text: 1 to 4000 characters after stripping.
            author: 'Project member' (default) or 'Host'; the caller derives it
                server-side from authentication, never from client input.
        Returns:
            Dict marking the message accepted by Briar with unconfirmed delivery.
        Raises:
            BriarSeatError: 400 for bad text, or a status error if the peer is not ready.
        """
        raise NotImplementedError('TODO: implement')

    def _cancel_pending(self, row):
        """Delete the owner's pending contact for this row, ignoring failures."""
        raise NotImplementedError('TODO: implement')

    def _validate_owner(self, row):
        """Confirm the owner's pinned contact still exists with the same author.

        Raises:
            BriarSeatError: if no binding directory is known or the owner identity changed.
        """
        raise NotImplementedError('TODO: implement')

    def revoke(self, project):
        """Revoke a project's peer: stop it, mark the binding and remove the owner contact.

        Args:
            project: Project identifier.
        Returns:
            Dict with revoked, presence_stopped (peer fully cleaned up) and
            owner_contact_removed. Unknown projects return revoked False.
        Side effects: takes self._lock, rewrites the binding, closes the peer and may
        delete the owner's contact.
        """
        raise NotImplementedError('TODO: implement')

    def close(self):
        """Mark every row revoked in memory and close all peers (shutdown path).

        Does not rewrite binding files, so previously invited projects can resume
        on the next start.
        """
        raise NotImplementedError('TODO: implement')
