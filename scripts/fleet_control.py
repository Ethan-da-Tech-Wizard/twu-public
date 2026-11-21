# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Owner-approved cross-box actions and terminal transport over pinned OpenSSH.

setup installs a non-root SSH listener ONLY on this host's WireGuard address.
trust explicitly pairs one public offer; existing pins never change implicitly.
The private keys, pins, access window and receipts stay outside Syncthing.
Full terminal access is the owner's OS account, not a example_host for hostile code.

Command-reference capability (Linux/macOS): authenticated read-only catalog and
shell-notation explanations use fixed JSON stdin, never command execution. The
private forced receiver imports only explicit-setup helper snapshots whose safe
file metadata/hash matches its manifest. Trust/revoke do not refresh helpers.
Typed text, queries, bodies and returned documentation never enter audit records.
Requests/replies are bounded to16KiB/1MiB; an owned SSH process is reaped on every
postspawn exit. No owner access window is required for this read-only capability;
STOP, peer pairing, client identity and revocation remain enforced. New helpers
have no daemon, model or network dependency; personal FleetAPI is the entrypoint.
"""
from contextlib import contextmanager
import base64
import fcntl
import getpass
import hashlib
import json
import os
from pathlib import Path
import re
import secrets
import shlex
import shutil
import signal
import stat
import struct
import subprocess
import sys
import tempfile
import termios
import threading
import time

def refresh_peers(root=None):
    """Re-read data/fleet_registry.json into PEERS (same dict object, so patched users stay valid).
    No registry file -> PEERS is left exactly as it is (the three defaults).

    Args: root = workspace folder (default ROOT). Returns the PEERS dict (name -> tunnel address).
    Why mutate in place: other modules did `from fleet_control import PEERS`; rebinding the name would leave them with a
    stale copy. Why leave PEERS alone when the file is missing: the pinned private receiver copy has no registry module
    and must keep working with the built-in three. Callers: import time, cli_onboard, cli_offboard. Writes nothing.
    """
    raise NotImplementedError('TODO: implement')

def reference_request(raw):
    """Validate the fixed, duplicate-free read-only request envelope.

    Args: raw (bytes): <=16KiB JSON containing schema1/source/request. Nested
        request is search(query<=200,offset0..39040,limit1..100), detail(name<=128),
        or explain(command<=8192 chars); no paths/runtime/shell switches exist.
    Returns: dict with the original validated source and request.
    Raises: FleetError('invalid_request') for malformed/extra/duplicate fields.
    Side effects/locks: none; neither typed notation nor any expansion is run.
    """
    raise NotImplementedError('TODO: implement')

def reference_source(path):
    """Read bounded owner-controlled Python source for explicit snapshot setup.

    Args: path (Path): a fixed adjacent helper filename, never request data.
    Returns: bytes <=128KiB. Raises: OSError/FleetError for unsafe metadata/size.
    Side effects: one no-follow descriptor, always closed; no import/execution,
        network, mutation or locking. Public source may be owner-readable0644.
    """
    raise NotImplementedError('TODO: implement')

def owner_request(raw):
    """Only argv data over stdin; never a shell or an alternate runtime selector."""
    raise NotImplementedError('TODO: implement')

def receiver_stdin(limit):
    """A paired client cannot hold the receiver forever without completing its body."""
    raise NotImplementedError('TODO: implement')

def briar_request_data(raw):
    """A fixed app protocol, never a URL, command, port or profile selector."""
    raise NotImplementedError('TODO: implement')

def briar_audit_metadata(result):
    """Defence in depth: even accidental full-response audit calls cannot log content."""
    raise NotImplementedError('TODO: implement')

def briar_profile_state():
    """Inspect only metadata of the existing encrypted profile; never create or unlock it."""
    raise NotImplementedError('TODO: implement')

def local_briar_request(operation, payload):
    """Only the receiving host's local client reads its token and talks to loopback."""
    raise NotImplementedError('TODO: implement')

class FleetError(ValueError):
    pass

def local_host():
    raise NotImplementedError('TODO: implement')

def public_key(value):
    raise NotImplementedError('TODO: implement')

def fingerprint(key):
    raise NotImplementedError('TODO: implement')

def private_dir(path, create=False):
    raise NotImplementedError('TODO: implement')

def read_file(path, maximum=65536):
    raise NotImplementedError('TODO: implement')

def write_file(path, raw):
    raise NotImplementedError('TODO: implement')

def user_environment():
    """SSH without PAM has no GUI session variables; use only this user's bus."""
    raise NotImplementedError('TODO: implement')

class Fleet:

    def __init__(self, root=None, runtime=None, host=None):
        raise NotImplementedError('TODO: implement')

    @contextmanager
    def locked(self):
        """Context manager: hold the exclusive state lock for ANY change to keys, pins, access window or policy.

        Why: two processes (dashboard, CLI, receiver) editing the same state at once could corrupt it. The lock file must
        be a private regular file owned by us with one link (checked below), so a planted symlink or shared file cannot
        be used to steer the lock. Raises FleetError if a unit test points at the real runtime (see the guard below).
        """
        raise NotImplementedError('TODO: implement')

    def state(self):
        raise NotImplementedError('TODO: implement')

    def save(self, data):
        raise NotImplementedError('TODO: implement')

    def stopped(self):
        raise NotImplementedError('TODO: implement')

    def audit(self, action, peer, result):
        raise NotImplementedError('TODO: implement')

    def validate_offer(self, peer, offer):
        raise NotImplementedError('TODO: implement')

    def offer(self):
        raise NotImplementedError('TODO: implement')

    def _pins(self, state):
        raise NotImplementedError('TODO: implement')

    def initialize(self):
        raise NotImplementedError('TODO: implement')

    def trust(self, peer, offer=None, expected=None):
        raise NotImplementedError('TODO: implement')

    def revoke(self, peer):
        raise NotImplementedError('TODO: implement')

    def unlock(self, minutes=15):
        raise NotImplementedError('TODO: implement')

    def lock(self):
        raise NotImplementedError('TODO: implement')

    def summary(self):
        raise NotImplementedError('TODO: implement')

    def ping(self):
        raise NotImplementedError('TODO: implement')

    def touch(self):
        raise NotImplementedError('TODO: implement')

    def snapshot_reference_modules(self):
        """Pin the two reviewed helpers during explicit local initialize/setup.

        Args: none. Returns: None. Raises: OSError/FleetError on unsafe source.
        Side effects: atomic0600 private helper copies, then hash manifest commit;
            initialize already holds the configuration lock. Trust/revoke never
            call this method. Readers fail closed during a partial refresh.
        """
        raise NotImplementedError('TODO: implement')

    def reference_module(self, name, private=False):
        """Load a fixed helper from reviewed source, never from a request path.

        Args: name (str): one REFERENCE_MODULES member; private (bool): forced
            receiver selects private snapshot, controller selects adjacent code.
        Returns: fresh Python module. Raises: FleetError when snapshot/hash/source
            validation fails. No typed text is evaluated as code.
        Side effects: imports trusted helper definitions in this process only;
            no bytecode/cache writes, locks, network or filesystem mutation.
        """
        raise NotImplementedError('TODO: implement')

    def reference_error(self, peer, operation, code):
        """Construct a content-free selected-host documentation error.

        Args: peer (str): requested host; operation (str): known op or unknown;
            code (str): fixed REFERENCE_CODES member.
        Returns: schema1 canonical error, execution=False; unknown host/platform
            stays unknown, never replaced with local availability.
        Side effects/raises/locking: none.
        """
        raise NotImplementedError('TODO: implement')

    def _reference_local(self, body, private=False, check=None):
        """Run only read-only catalog or pure notation explanation helpers.

        Args: body (dict): validated request; private (bool): receiver snapshots;
            check (callable|None): pairing/STOP callback, checked before/after read.
        Returns: canonical result preserving explainer ok/partial/invalid/unsupported.
        Raises: FleetError for STOP/revocation/unavailable snapshot/oversized reply.
        Side effects: bounded read-only helper work; never runs typed programs,
            substitutions or suggestions. No access window or shared lock used.
        """
        raise NotImplementedError('TODO: implement')

    def _check_reference_peer(self, peer, offer):
        """Revalidate a read-only sender's STOP and exact pairing without unlock.

        Args: peer (str)/offer (dict): pinned target captured before SSH.
        Returns: None. Raises: FleetError('stopped'|'unpaired') if authority ends.
        Side effects: private metadata reads only; no locks/network/process calls.
        """
        raise NotImplementedError('TODO: implement')

    def literal_command_argv(self, command):
        """Convert only simple literal runner notation using the preview parser.

        Args: command (str): <=8192chars, no NUL. Parsing uses the fixed Bash/POSIX
            quoting subset, independently of the configured interactive shell.
        Returns: list[str] literal argv including explicitly quoted empty args.
        Raises: FleetError('shell_required') for controls, redirects, assignments,
            expansions or unsupported grammar; invalid_request for empty/bad input.
        Side effects: loads fixed reviewed pure helper only; never executes typed
            text. Unknown program/flag descriptions may be partial and still pass.
        """
        raise NotImplementedError('TODO: implement')

    def command_reference(self, peer, body):
        """Fetch bounded selected-host docs over existing paired pinned SSH.

        Args: peer (str): exact fleet host; body (dict): search/detail/explain.
        Returns: canonical result or fixed error; partial explanation remains
            partial. Offline peers never fall back to local inventory.
        Side effects: metadata-only audit, private anonymous stdin file and one
            owned SSH child (15second deadline, bounded1MiB stdout); cleanup kills
            and reaps on every postspawn path. No terminal unlock is consulted.
        """
        raise NotImplementedError('TODO: implement')

    def access_allowed(self):
        raise NotImplementedError('TODO: implement')

    def set_access_policy(self, mode):
        raise NotImplementedError('TODO: implement')

    def receiver_authorized(self, peer, client_fingerprint, needs_access=True):
        raise NotImplementedError('TODO: implement')

    def execute_error(self, code, timed_out=False):
        raise NotImplementedError('TODO: implement')

    def _run_owner_process(self, argv, timeout, check):
        """Owner account execution, not OS isolation; bounded stream and owned session."""
        raise NotImplementedError('TODO: implement')

    def execute(self, peer, argv, timeout=60):
        raise NotImplementedError('TODO: implement')

    def _check_peer_access(self, peer, offer):
        raise NotImplementedError('TODO: implement')

    def _check_local_access(self):
        raise NotImplementedError('TODO: implement')

    def receive(self, peer, client_fingerprint, original=None):
        """Per-key forced command: SSH_ORIGINAL_COMMAND is data, never evaluated."""
        raise NotImplementedError('TODO: implement')

    def _receive_shell(self, peer, client_fingerprint):
        raise NotImplementedError('TODO: implement')

    def ssh(self, peer, terminal=False):
        raise NotImplementedError('TODO: implement')

    def call(self, peer, action, param=None):
        raise NotImplementedError('TODO: implement')

    def _briar_error(self, host, operation, code, http_status=503):
        raise NotImplementedError('TODO: implement')

    def briar_request(self, peer, operation, payload=None):
        """Fixed app capability over existing pins, not a terminal or a new unlock window.

        The authenticated EZ owner chooses its private backend. Body data travels
        only on stdin; neither the SSH command nor fleet receipts contain it.
        """
        raise NotImplementedError('TODO: implement')

    def _run_briar_request(self, raw):
        raise NotImplementedError('TODO: implement')

    def run_local(self, action, param=None):
        raise NotImplementedError('TODO: implement')

    def install(self):
        raise NotImplementedError('TODO: implement')

class Terminals:
    """Private PTYs for authenticated dashboard owners; output/input never logged."""

    def __init__(self, fleet):
        raise NotImplementedError('TODO: implement')

    def open(self, peer, owner, cols=80, rows=24):
        raise NotImplementedError('TODO: implement')

    def _item(self, sid, owner):
        raise NotImplementedError('TODO: implement')

    def _read(self, sid, item):
        raise NotImplementedError('TODO: implement')

    def poll(self, sid, owner):
        raise NotImplementedError('TODO: implement')

    def write(self, sid, owner, data, seq):
        raise NotImplementedError('TODO: implement')

    def resize(self, sid, owner, cols, rows):
        raise NotImplementedError('TODO: implement')

    def close(self, sid, owner=None):
        raise NotImplementedError('TODO: implement')

    def close_all(self, owner=None):
        raise NotImplementedError('TODO: implement')

    def shutdown(self):
        raise NotImplementedError('TODO: implement')

    def _watch(self):
        raise NotImplementedError('TODO: implement')

class FleetAPI:
    """Called only after the personal dashboard verifies its owner bearer token."""

    def __init__(self, root):
        raise NotImplementedError('TODO: implement')

    def close(self, owner=None):
        raise NotImplementedError('TODO: implement')

    def browse(self, payload):
        """Read-only file browser: FIXED argv through the paired exec path (same unlock/STOP/pairing gates).

        Only the validated relative path is variable and it is a single argv element (no shell, no glob).
        The reply is re-validated here and returned as plain JSON data; nothing from the remote is trusted."""
        raise NotImplementedError('TODO: implement')

    def handle(self, payload, owner):
        raise NotImplementedError('TODO: implement')

def serve(fleet):
    raise NotImplementedError('TODO: implement')

def cli_trust(fleet, peer, expect):
    """CLI trust must not be one blind keystroke (Magi 10 review H1, fixed by Magi 23 2026-11-19).

    Without --expect it only SHOWS the two fingerprints of the offer and trusts nothing. Ethan compares them with what the
    other computer prints for itself (`fleet_control.py status` there), then re-runs with --expect HOST_FP CLIENT_FP.
    fleet.trust() re-checks that the offer still has exactly those fingerprints before pinning it.

    Args: fleet = the Fleet for this computer; peer = the OTHER computer's name; expect = None or (host_fp, client_fp).
    Returns {'status': 'confirm_needed', ...} (nothing changed) or fleet.trust()'s result. Raises FleetError for an
    unknown peer, trusting yourself, or a bad/changed offer. Why safe: a pin is only written after the owner has
    compared fingerprints out of band, so a swapped key (man-in-the-middle) is caught.
    """
    raise NotImplementedError('TODO: implement')

def owner_gate(fleet, name, verb):
    """Require a human at a keyboard before onboard/offboard changes the fleet list.

    Args: fleet (for the STOP check), name (computer being changed), verb ('onboard'/'offboard' for messages).
    Raises FleetError when STOP is active, when stdin is not a terminal (so a script, the dashboard or an AI tool cannot
    run it), or when the typed name does not match. Returns None when allowed. The test-only env bypass never skips STOP.
    """
    raise NotImplementedError('TODO: implement')

def cli_onboard(fleet, name, label, platform, address, hostnames):
    """Add a computer to the fleet LIST and print the owner's checklist. Grants NO trust and changes no keys.

    Args: name, label, platform ('linux'/'macos'), address (inside 192.0.2.1/24), hostnames (aliases it may report).
    Returns {'status': 'ok', 'trusted': False, 'owner_checklist': [...]}. Raises FleetError for a bad request or a
    refused owner_gate. Why only a list entry: WireGuard keys, firewall rules and fingerprint trust need root or the
    owner's eyes, so they are printed as steps for Ethan instead of being automated.
    """
    raise NotImplementedError('TODO: implement')

def cli_offboard(fleet, name):
    """Revoke a computer's pin, then drop it from the fleet LIST. Returns reminders for the owner's manual steps.

    Raises FleetError for an unknown name, offboarding yourself (a computer that removed itself could not tell the rest),
    or a refused owner_gate. Order matters: revoke FIRST so the key stops working even if the list edit then fails; the
    list is edited second. Each other computer must run the same command (the owner is told), because pins are local.
    """
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
