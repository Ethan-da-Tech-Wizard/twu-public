# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""persistence_guard: alarm when something new sets itself up to survive a reboot or steal a login. No root, no model, no network.

  persistence_guard.py learn    accept the current state as the baseline
  persistence_guard.py check    compare to baseline; write data/netguard/PERSIST.<host>.json; exit 1 on findings

Watches the places malware and bad installers use: shell startup files, ssh authorized_keys/config, autostart entries,
user systemd units (new or changed, other than our own twu-/ethan-/magi- units which are reported as info), ~/.local/bin,
environment.d, cron files, /etc/ld.so.preload, /etc/systemd/system, and /etc/profile.d. Stores content hashes when readable;
for permission-denied regular files, stores a metadata fingerprint (device, inode, mode, size, mtime and ctime), never contents.
"""
from __future__ import annotations
import fnmatch, glob, hashlib, json, os, socket, sys, time
from pathlib import Path

class GuardUnavailable(RuntimeError):
    """The persistence scan could not inspect every item it found."""

def digest(p):
    raise NotImplementedError('TODO: implement')

def _metadata_digest(st):
    """Stable file metadata hash; omit uid/gid because systemd can id-map them in the unit namespace."""
    raise NotImplementedError('TODO: implement')

def _glob_checked(pattern):
    raise NotImplementedError('TODO: implement')

def snapshot(home=None, patterns=None):
    raise NotImplementedError('TODO: implement')

def is_ours(path):
    raise NotImplementedError('TODO: implement')

def compare(base, now):
    """-> (problems, info). Pure.

    Args:
        base: {path: digest} recorded by `learn` (the owner's accepted state).
        now:  {path: digest} from snapshot().
    Returns:
        problems {key: text}, info [text].
    Security rule (2026-11-21, review B_security finding 1): quietness is bound to CONTENT, never to a name.
    An item whose digest equals the baseline digest is quiet whatever it is called (that is how the owner's real
    twu-/magi- jobs stay silent: learn recorded their digests). A NEW item or a CHANGED digest is ALWAYS a problem,
    even when the file is called twu-backdoor or magi-evil.service. The OURS prefix only adds a hint to the text.
    """
    raise NotImplementedError('TODO: implement')

def _journal_db_trusted(db):
    """True only if the journal DB is a regular file (not a symlink) owned by the current user and NOT group/world-writable.
    Review B_security finding 2: anyone who can write the DB could forge an acceptance row. Never raises."""
    raise NotImplementedError('TODO: implement')

def _blob_tokens(cols):
    """Split journal text columns into whitespace tokens with surrounding quotes/punctuation stripped, so a path must
    appear as its OWN token (exact equality) rather than as a substring of a longer name such as toolbox-long."""
    raise NotImplementedError('TODO: implement')

def journal_accepts(path, home=None, db=None, now=None):
    """True if a sysjournal change record names this EXACT path and is not older than the file's mtime (Magi 17, 2026-11-16).
    Hardened 2026-11-21 (review B_security finding 2):
      - exact path equality against whole tokens (was: substring, so a record for ~/.local/bin/toolbox-long accepted `tool`);
      - a row timestamp in the future is ignored (was: a ts far in the future satisfied ts>=mtime forever);
      - the DB must be owned by the user and not group/world-writable (otherwise it is untrusted and nothing is accepted).
    A deliberate, logged edit is accepted; an edit with no record, or made AFTER the last record, still alarms. Never raises."""
    raise NotImplementedError('TODO: implement')

def paths(host=..., d=None):
    raise NotImplementedError('TODO: implement')

def _redact(text):
    """Mask the value after password/token/secret/key words (name=value, name: value or name value)."""
    raise NotImplementedError('TODO: implement')

def _sha(path):
    raise NotImplementedError('TODO: implement')

def _write_learn_receipt(base_p, before, tool, accepted=None):
    """One JSON line per successful learn, appended with a single os.write (Syncthing-safe, per-host file).
    A failure here only warns on stderr; it never blocks learn. No secrets, no file contents."""
    raise NotImplementedError('TODO: implement')

def learn(d=None, home=None):
    raise NotImplementedError('TODO: implement')

class LearnRefused(Exception):
    """learn --only was asked for a key that is not a current, baseline-acceptable finding."""

def learn_only(keys, d=None, home=None):
    """Accept ONLY the named findings (exact persist:new|changed|removed:PATH keys from `check`); the rest stay open.
    Raises LearnRefused (baseline untouched) for an unknown key."""
    raise NotImplementedError('TODO: implement')

def check(d=None, home=None, journal=None):
    raise NotImplementedError('TODO: implement')

def alarm_problems(now=None, d=None):
    """For ethan_alarm. Quiet sensor is a problem. Never raises."""
    raise NotImplementedError('TODO: implement')

def main(a=None):
    raise NotImplementedError('TODO: implement')
