# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/ez_onion_access.py: owner-user Tor v3 transport for the dedicated EZ phone/project gateway.

PROGRAM: scripts/ez_onion_access.py
PROGRAMMER: existing author; comments by Magi seat 5 (Claude)
LAST MODIFIED: 2026-11-21
PURPOSE: Runs one Tor child process per dashboard that publishes the dedicated
  phone/project listener (port 8782) as a persistent v3 onion service, and reports a
  non-secret status dict for the UI. Owns the private onion state folder (torrc,
  data, service keys, lock, log) and the pinned-hash check on the Tor executable.
  This transport needs a Tor-capable client. It cannot make an onion address
  reachable in ordinary Safari/Chrome without Tor routing on the client.
INVARIANTS: forwarding is restricted to 127.0.0.1:8782 (never the desktop port,
  because Tor's loopback source cannot identify an owner browser); all state files
  are owner-only, single-link regular files opened with O_NOFOLLOW; the Tor binary
  must match TOR_SHA256 and come from the already-inspected Briar runtime; status()
  never starts Tor and never returns log contents; one process holds the folder lock.
UPSTREAM: ez_safe_path (symlink-safe directory walk), ez_briar_runtime (verified jar),
  stop_latch (global stop switch). DOWNSTREAM: the dashboard that shows the onion
  origin; tests in test_ez_onion_access.py.
"""
from __future__ import annotations
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import threading
import zipfile
from ez_safe_path import split_base

def _private_directory(path, base=None):
    """Walk without following symlinks below a once-resolved base; the final directory must be private.

    Symlinks at or above the trusted base (macOS /var, /tmp) are followed exactly
    once by ez_safe_path.split_base; any symlink below it is refused (O_NOFOLLOW).

    Args:
        path: directory to create/validate; made absolute, not resolved.
        base: optional trusted base passed through to split_base.
    Returns: the absolute Path.
    Raises: ValueError if the final directory is not owned by us or is group/other
        accessible; OSError (e.g. ELOOP/ENOTDIR) if a component below the base is a symlink.
    Side effects: creates missing components with mode 0700.
    """
    raise NotImplementedError('TODO: implement')

def _read(path, maximum=65536):
    """Read a small owner-only state file safely.

    Args:
        path: file to read.
        maximum: size cap in bytes; larger files are rejected.
    Returns: up to maximum+1 bytes of content.
    Raises: OSError if the path is a symlink (O_NOFOLLOW); ValueError if it is not a
        regular file, not owned by us, group/other accessible, hard-linked, or too large.
    """
    raise NotImplementedError('TODO: implement')

def _write(path, data, mode=384):
    """Write a state file in place, refusing links and foreign files.

    Args:
        path: target file (created if missing).
        data: bytes to write.
        mode: permission bits applied to the file.
    Returns: None.
    Raises: OSError on symlink; ValueError if the file is not a regular, owned,
        single-link file.
    Side effects: truncates then rewrites the file and fsyncs it.
    """
    raise NotImplementedError('TODO: implement')

def tor_binary(directory):
    """Extract only the pinned native member from the already-inspected Briar JAR.

    Args:
        directory: private folder in which the executable "tor" lives or is created.
    Returns: Path of the verified executable.
    Raises: ValueError if an existing file or the extracted bytes do not match
        TOR_SHA256, is not executable, or the member is oversized; KeyError/BadZipFile
        if the jar lacks the member; whatever verify_runtime raises for a bad jar.
    Side effects: may write the executable (mode 0700).
    """
    raise NotImplementedError('TODO: implement')

class OnionService:
    """One Tor child per dashboard; persisted v3 keys survive ordinary restarts.

    The target MUST be the dedicated phone/project listener. Never pass the
    desktop port: Tor's loopback TCP source cannot identify an owner browser.

    State: process (Tor child or None), _lock_fd (folder flock), _thread_lock
    (serialises start/close), _error (user-facing message or None).
    """

    def __init__(self, directory=None, target_port=8782, socks_port=19050):
        """Configure, but do not start, the service.

        Args:
            directory: state folder; default ~/.local/state/ez-briar/onion.
            target_port: must be exactly 8782 (the dedicated gateway).
            socks_port: loopback SOCKS port, int in 1024..65535.
        Raises: ValueError for any other target port or an invalid socks port.
        """
        raise NotImplementedError('TODO: implement')

    def start(self):
        """Return immediately; Tor bootstrap continues without blocking the UI.

        Args: none.
        Returns: the status() dict (state "starting" once the child is spawned).
        Raises: nothing for expected failures; OSError/ValueError/BadZipFile are
            caught and surfaced as status()["error"]. Other exceptions propagate.
        Side effects: takes the folder lock, writes torrc and tor.log, spawns Tor.
        Locking: serialised by _thread_lock; _lock_fd stays held until close().
        """
        raise NotImplementedError('TODO: implement')

    def status(self):
        """Report non-secret service state; never starts Tor.

        Args: none.
        Returns: dict with state ("ready"/"starting"/"stopped"), running, ready,
            bootstrap_percent, origin (validated http://<name>.onion or None),
            socks_host/port, client_requirement, action and error.
        Side effects: none (reads the hostname file and the tail of tor.log).
        """
        raise NotImplementedError('TODO: implement')

    def close(self):
        """Stop our Tor child and release the folder lock.

        Args: none.
        Returns: None.
        Side effects: terminate (then kill after 5 s) the child; closes _lock_fd.
        Locking: serialised by _thread_lock. Safe to call when nothing is running.
        """
        raise NotImplementedError('TODO: implement')
