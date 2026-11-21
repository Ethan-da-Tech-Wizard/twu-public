# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""EZ shared workspace: Briar messages, local code/Git and scoped Magi receipts.

The browser talks only to this allowlist proxy. Briar owns local encrypted profiles, contacts,
messages and delivery status. Explicit EZ project files and redacted project-linked Magi receipts
are separate from company files, private profiles, and full Magi outboxes.

PROGRAM: scripts/ez_briar_dashboard.py
PROGRAMMER: existing author; comments by Magi seat 5 (Claude)
LAST MODIFIED: 2026-11-21
PURPOSE: Owns the EZ web interface and its HTTP allowlist proxy: the Briar client classes,
  the single-page browser app (HTML/CSS/JS assembled below as string literals), the request
  guard that separates project members, paired phones and the local owner, and the serve/status
  command line. Why: the browser must never reach Briar, the Git workspace or Magi files
  directly, so every capability is an explicit route with strict validation.
  Invariants: Briar credentials are read only by the local client (never sent to a browser or
  to the remote backend); mutations need a matching Origin and CSRF token; replies carry short
  messages, never tracebacks; message delivery is only ever claimed as "accepted by Briar".
  Upstream (called by): systemd unit, fleet/ops scripts and tests. Downstream (calls): ez_settings,
  ez_phone_access, ez_project_access, ez_workspace, ez_magi_workspace, ez_briar_seat,
  ez_briar_runtime, ez_onion_access, ez_briar_assets (CSS), magi_task_dashboard, stop_latch.
  Reading guide: the large PAGE/JS/CSS literals are data for the browser; Python comments
  describe them from outside because their text must stay byte-for-byte unchanged.
"""
from __future__ import annotations
import argparse
import base64
import ctypes
import ctypes.util
from collections import deque
import threading
import time
import hmac
import hashlib
import json
import os
from pathlib import Path
import re
import secrets
import signal
import socket
import stat
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener
from ez_settings import BACKEND_HOST, BACKEND_LABEL, OWNER_NAME, PARTNER_NAME

class BriarError(Exception):
    """Error carrying a stable machine code, a short user-safe message and an HTTP status.

    Raised by every Briar client; handlers turn it into a JSON reply so tracebacks never reach the browser.
    """

    def __init__(self, code, message, status=503):
        """Store the code/message/status triple.

        Args:
            code: stable identifier such as "briar_offline" (the UI keys off it).
            message: plain-language text that is safe to show to the user.
            status: HTTP status to answer with (default 503, service unavailable).
        """
        raise NotImplementedError('TODO: implement')

class NoRedirect(HTTPRedirectHandler):
    """Redirect handler that refuses every redirect.

    A redirect could send the bearer token to a different host, so the Briar opener never follows any.
    """

    def redirect_request(self, *_args, **_kwargs):
        """Return None, which makes urllib raise an HTTPError instead of following the redirect.

        Args:
            *_args, **_kwargs: urllib's redirect arguments, ignored.

        Returns:
            Always None.
        """
        raise NotImplementedError('TODO: implement')

class BriarClient:
    """Client for the local Briar Headless HTTP API on 127.0.0.1.

    Owns token reading, request sending and normalising of contacts/messages. Stateless apart
    from its opener; safe to share across handler threads. RemoteBriarClient overrides request()
    to reach a profile that lives on another host.
    """

    def __init__(self, port=7000, token_path=None):
        """Prepare a client for one local Briar Headless instance.

        Args:
            port: Briar Headless port on 127.0.0.1 (1-65535 int; bool and other types rejected).
            token_path: override for the auth token file; default ~/.briar/auth_token.

        Raises:
            ValueError: port is not a plain int in range.
        """
        raise NotImplementedError('TODO: implement')

    def _token(self):
        """Read the Briar auth token from disk with strict safety checks.

        Returns:
            The token string (printable ASCII, at most 4096 characters).

        Raises:
            BriarError: account_not_ready (file missing) or token_unavailable (unreadable, not a
                private regular file owned by this user, wrong size or characters).
        """
        raise NotImplementedError('TODO: implement')

    def request(self, path, payload=None, method=None):
        """Send one request to Briar Headless and return its decoded JSON.

        Args:
            path: API path under /v1, for example "/contacts" or "/messages/3".
            payload: JSON-serialisable body; None means no body (GET by default).
            method: "GET", "POST" or "DELETE"; default GET without payload, else POST.

        Returns:
            Parsed JSON, or {} when Briar sent an empty body.

        Raises:
            BriarError: unsupported method (400), bad token, Briar offline, rejected request,
                oversized or malformed reply. Never leaks the token or a traceback.
        Side effects: one HTTP call to 127.0.0.1 with a 5 second timeout.
        """
        raise NotImplementedError('TODO: implement')

    def contacts(self):
        """List the Briar contacts in a safe, trimmed shape.

        Returns:
            List of dicts with contactId (int), name (at most 200 chars), connected and verified (bool).
            At most 2000 contacts; malformed rows are skipped silently.

        Raises:
            BriarError: from request(), or invalid_response when Briar did not return a list.
        """
        raise NotImplementedError('TODO: implement')

    def messages(self, contact_id):
        """Return the latest messages of one conversation.

        Args:
            contact_id: Briar contact id (already validated by contact_id()).

        Returns:
            Up to 500 dicts with text, local (sent by us), delivery (plain-language status) and timestamp.

        Raises:
            BriarError: from request(), or invalid_response when the reply is not a list.
        """
        raise NotImplementedError('TODO: implement')

def load_backend_config(path=None):
    """Select the existing profile host; a broken explicit selection never falls back."""
    raise NotImplementedError('TODO: implement')

def backend_setup_status():
    """Report whether local profile setup must be blocked because the profile lives elsewhere.

    Returns:
        A dict with ready=False plus code/detail when the backend config is invalid or points at
        the remote host; None when local setup may proceed.
    """
    raise NotImplementedError('TODO: implement')

class RemoteBriarClient(BriarClient):
    """BriarClient that forwards a fixed allowlist of operations to the backend host.

    Credentials stay on that host: _token() is disabled, and request() only maps recognised
    (method, path, payload-shape) combinations onto named operations sent through the fleet
    control channel. Anything else is refused before leaving this process.
    """

    def __init__(self, fleet_factory=None):
        """Create the remote client.

        Args:
            fleet_factory: optional zero-argument callable returning a Fleet-like object (tests inject
                a fake); by default fleet_control.Fleet() is built per request.
        """
        raise NotImplementedError('TODO: implement')

    def _token(self):
        """Refuse to supply a token: Briar credentials never leave the backend host.

        Raises:
            BriarError: always (invalid_request, 400).
        """
        raise NotImplementedError('TODO: implement')

    def request(self, path, payload=None, method=None):
        """Translate an allowlisted Briar request into a remote operation and return its data.

        Args:
            path, payload, method: as for BriarClient.request.

        Returns:
            The JSON dict/list from the backend (at most RESPONSE_LIMIT bytes when re-encoded).

        Raises:
            BriarError: request outside the allowlist (400), transport failure, wrong reply shape,
                or a remote error mapped through REMOTE_ERRORS.
        Side effects: one call to the fleet control channel, which may run a command on the backend host.
        """
        raise NotImplementedError('TODO: implement')

class UnavailableBriarClient(BriarClient):
    """Placeholder client used when the backend configuration is broken.

    Every request fails with a repair message, so no local profile is ever created by accident.
    """

    def request(self, path, payload=None, method=None):
        """Always fail with backend_configuration_invalid.

        Raises:
            BriarError: always.
        """
        raise NotImplementedError('TODO: implement')

def owner_client(port=7000, config_path=None):
    """Choose the Briar client for the owner interface.

    Args:
        port: local Briar Headless port, used only when the profile is local.
        config_path: optional backend.json override (tests).

    Returns:
        UnavailableBriarClient on an invalid config, RemoteBriarClient when a backend host is
        configured, otherwise a local BriarClient.
    """
    raise NotImplementedError('TODO: implement')

def client_profile_host(client):
    """Name the profile host of a client for status replies.

    Args:
        client: any object, normally a BriarClient subclass.

    Returns:
        "local", the configured backend host, or "invalid"; anything else is coerced to "local".
    """
    raise NotImplementedError('TODO: implement')

def contact_id(value):
    """Validate a contact id taken from a URL path.

    Args:
        value: the raw string from the request.

    Returns:
        The id as an int in 0..2147483647.

    Raises:
        ValueError: not a canonical decimal (no leading zeros, at most 10 digits) or out of 32-bit range.
    """
    raise NotImplementedError('TODO: implement')
from ez_briar_assets import CSS
from magi_task_dashboard import CSS as TASK_CSS, JS as TASK_JS

def pairing_qr(url):
    """Use the installed system QR library; never send a pairing link elsewhere."""
    raise NotImplementedError('TODO: implement')

def phone_route_ready(access):
    """Decide whether a phone access configuration points at a usable origin.

    Args:
        access: object with load_config() (a PhoneAccess).

    Returns:
        True for an http(s) origin that is local-network (.local, localhost, loopback, 192.168/16,
        10/8, 172.16-31/12, or a lan/mdns transport), an onion origin, or any https origin; False
        when nothing is configured, the scheme is not http(s) as required, or the config cannot be read.
        Does not contact the origin; reachability is not checked.
    """
    raise NotImplementedError('TODO: implement')

def _fill(text):
    """Replace the __EZ_*__ placeholders with the configured names (see ez_settings)."""
    raise NotImplementedError('TODO: implement')

def _lan_listener_ready(access):
    """Check that a LAN listener (0.0.0.0) is allowed by the saved phone configuration.

    Args:
        access: PhoneAccess-like object with load_config().

    Returns:
        True only when the config is a dict with transport "lan" whose origin is already in
        normalised form; False on any other or unreadable configuration.
    """
    raise NotImplementedError('TODO: implement')

class EZServer(ThreadingHTTPServer):
    """Threaded HTTP server holding all shared state for the EZ handlers.

    Owns the Briar client, phone/project access stores, workspace objects, the CSRF token, the
    pairing rate-limit queue and (once started) the Tor gateway and Briar seat manager. One
    instance serves one listener (owner 8780, phone 8782 or shared 8783).
    """

    def __init__(self, address, client=None, *, phone=False, access=None, workspace=None, magi_workspace=None, shared=False, project_access=None, handler=None, lan_listener=False):
        """Build the server and refuse unsafe listener combinations.

        Args:
            address: (host, port) to bind.
            client: Briar client; default owner_client().
            phone: True for the paired-device-only listener.
            access: PhoneAccess override; default PhoneAccess().
            workspace, magi_workspace, project_access: injectable collaborators (tests).
            shared: True for the project-member-only listener.
            handler: request handler class; default Handler.
            lan_listener: explicit opt-in required to bind 0.0.0.0.

        Raises:
            ValueError: non-loopback bind without the full LAN opt-in and ready LAN config, or phone and
                shared both set.
        """
        raise NotImplementedError('TODO: implement')

    def start_briar_warmup(self):
        """Start background preparation of per-project Briar seats on the owner listener.

        Returns:
            {"started": 0} on phone/shared listeners (they never manage seats); otherwise the result of
            BriarSeats.prewarm_existing for all current project ids.
        Side effects: creates the BriarSeats manager under briar_seats_lock on first call.
        """
        raise NotImplementedError('TODO: implement')

class Handler(BaseHTTPRequestHandler):
    """Request handler: the allowlist proxy between the browser and Briar/workspace code.

    Every request is first classified (project member, paired phone or local owner) and checked
    by _guard() before any route runs. Replies always go through _reply(), which adds no-store
    and security headers. Logging is disabled to keep message metadata out of logs.
    """

    def _seat_manager(self):
        """Return the shared BriarSeats manager, creating it lazily under its lock.

        Returns:
            The manager owned by the main owner server (a gateway server defers to seat_owner).
        """
        raise NotImplementedError('TODO: implement')

    def _member_request(self):
        """True when this request belongs to the project-member interface (shared listener or /project/ prefix)."""
        raise NotImplementedError('TODO: implement')

    def _route_prefix(self):
        """Strip a leading /project from the path and remember it, so one handler serves both layouts."""
        raise NotImplementedError('TODO: implement')

    def _invitation_navigation(self):
        """True for a top-level browser navigation to "/" with no Origin header, the only cross-site
        request allowed (opening an invitation link from another app).
        """
        raise NotImplementedError('TODO: implement')

    def _access_for_route(self, route):
        """Pick the access store for a pairing route.

        Args:
            route: "same-wifi" or "anywhere".

        Returns:
            The matching PhoneAccess.

        Raises:
            ValueError: unknown route, or the anywhere gateway is not started yet.
        """
        raise NotImplementedError('TODO: implement')

    def _health(self):
        """Build the local connection-health report.

        Returns:
            Dict with service state, avahi and firewall probe results (True/False/None when unknown),
            pairing state, the retained last successful pair time and the onion status.
        Side effects: runs two short, read-only system commands (2 second timeout each).
        """
        raise NotImplementedError('TODO: implement')

    def log_message(self, *_args):
        """Silence request logging so message paths and peers are not written to logs.

        Args:
            *_args: format string and values from http.server, ignored.
        """
        raise NotImplementedError('TODO: implement')

    def _editor_asset(self, path):
        """Serve only the inspected, hash-listed local editor distribution."""
        raise NotImplementedError('TODO: implement')

    def _workspace_request(self, payload):
        """Dispatch one /api/workspace action after strict validation.

        Args:
            payload: decoded JSON object; must contain "action" and exactly that action's fields.

        Side effects: always sends one reply. Project actions can write project files and Git history,
        issue or revoke invitations, assign tasks to Magi seats or send chat messages.
        Errors map to 400 (bad fields), 403 (member limits), 409 (STOP active), 503 (local failure).
        """
        raise NotImplementedError('TODO: implement')

    def _reply(self, status, body, mime=..., extra_headers=None):
        """Send one response with the standard security headers.

        Args:
            status: HTTP status code.
            body: dict/list (JSON-encoded) or raw bytes.
            mime: Content-Type; default JSON.
            extra_headers: optional {name: value or list}; only Set-Cookie is honoured, and values with CR/LF are dropped (header injection guard).

        Side effects: writes to the socket; no body is written for HEAD.
        """
        raise NotImplementedError('TODO: implement')

    def _guard(self, mutation=False):
        """Earlier version of the access check (member branch only, then falls off the end).

        NOTE: a second _guard is defined further down in this class and replaces this one at class
        creation time, so this definition is never called. Kept unchanged; see the later _guard for the
        live logic.
        """
        raise NotImplementedError('TODO: implement')

    def _is_phone_request(self):
        """Classify the request as coming from a paired phone (True) or the local owner (False).

        Phone if: this is the phone listener, the peer is not loopback, the Host header is the backend
        .local name / an onion / another .local name, or it matches the configured phone origin's host.
        Member requests are never phone requests. Config errors fall through to False.
        """
        raise NotImplementedError('TODO: implement')

    def _guard(self, mutation=False):
        """Authorise one request; this is the live _guard (it replaces the earlier definition above).

        Three callers are told apart and each gets its own checks, in this order:
          1. project member: exact Host/Origin/forwarding checks against the configured origin, CSRF on
             mutations, a short public route list, and a valid member cookie for everything else;
          2. paired phone: no setup/pairing-admin routes, validate_proxy on the access store, CSRF on
             mutations, and a paired-device cookie for non-public routes;
          3. local owner: loopback peer only, no proxy/forwarding headers, exact local Host and Origin,
             no cross-site requests, and Origin plus CSRF token on mutations.

        Args:
            mutation: force the mutation rules; otherwise POST/PUT/PATCH/DELETE imply it.

        Returns:
            True when the request may continue; False after a 400/401/403 reply has been sent.
        """
        raise NotImplementedError('TODO: implement')

    def do_HEAD(self):
        """Answer HEAD like GET; _reply skips writing the body."""
        raise NotImplementedError('TODO: implement')

    def do_GET(self):
        """Serve the page, assets and read-only API routes after _guard().

        Routes: /assets/monaco/*, /health, /api/health, /, /style.css, /app.js, /api/session,
        /api/phone/devices, /api/phone-access, /api/identity, /api/status, /api/messages/<id>,
        /api/pairing-link. Anything else gets 404.
        """
        raise NotImplementedError('TODO: implement')

    def do_POST(self):
        """Handle the mutating API routes after _guard(mutation=True).

        Routes: /api/workspace, /api/project/join, /api/pairing, /api/setup, /api/phone/pair,
        /api/phone/pairing-link, /api/phone/revoke, /api/phone/anywhere/retry and /api/messages/<id>.
        Bodies must be a single-length, JSON, size-limited object read within a 5 second socket timeout.
        Errors are mapped to short JSON messages; message text is never logged.
        """
        raise NotImplementedError('TODO: implement')

def _start_onion_gateway(owner):
    """One process-owned phone/project-only listener; Tor never reaches owner mode."""
    raise NotImplementedError('TODO: implement')

def serve(port=..., briar_port=7000, phone=False, shared=False, listen=...):
    """Run the EZ listener until interrupted.

    Args:
        port: TCP port to bind.
        briar_port: local Briar Headless port.
        phone: run the paired-phone-only interface.
        shared: run the project-member-only interface.
        listen: "127.0.0.1", "0.0.0.0" or "auto" (LAN only when valid LAN phone config exists in owner mode).

    Raises:
        SystemExit: from stop_latch.enforce when Workspace STOP is active.
        ValueError: unsafe listener combination (from EZServer).
    Side effects: binds a socket, installs SIGTERM/SIGINT handlers (main thread only), and on the
    owner listener starts Briar warm-up and the onion gateway; all are closed in the finally block.
    """
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    """Command line entry point.

    Args:
        argv: argument list (default sys.argv[1:]).

    Returns:
        0 on success; 1 when `status` finds Briar not ready. `serve` (default) runs until stopped.
    Side effects: `status` prints one JSON line with no secrets.
    """
    raise NotImplementedError('TODO: implement')
