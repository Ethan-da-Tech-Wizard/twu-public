# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""ethan_incidents.py - thin front-end over scripts/incident_ledger.py (the ONE incident source of truth).

The ledger (data/incidents/<host>.jsonl, append-only per-host shards, fed by alarms, check_all, catchup,
stale sweep, scavenger) owns identity, status and history. This file adds only what the ledger has no
fields for: symptom signatures and read-only verified_by commands, kept in a small sidecar.

  list | show ID | add ... | fix ID ... | match [FILE|-] | verify | lint | watch | migrate FILE
  ID is a ledger id (10 hex) or a legacy id (INC-20261108-NN, kept in the sidecar as legacy_id).

Sidecar data/incidents/signatures.json (one JSON object, keyed by the ledger incident id):
  {"<ledger id>": {
      "title": str,                     # one-line human title (ledger detail may be overwritten by notes)
      "signatures": [str, ...],         # regexes (case-insensitive); an invalid regex is a plain substring
      "verified_by": str,               # ALLOW-LISTED command (no shell): grep|test|ls|cat|wc|stat <args> or
                                        #   python3 scripts/<repo script>.py <args>; exit 0 = the preventer works;
                                        #   run with cwd=repo root, scrubbed env, 20 s timeout, own process group.
                                        #   Anything needing pipes/&&/! goes in scripts/incident_checks.py
      "preventer": {"type": "test|guard|check|rule", "path": "repo-relative file", "note": str},
                                        # optional while open; the ledger demands the path exists to mark fixed
      "legacy_id": str, "root_cause": str, "lessons": str, "evidence": [str, ...]   # optional}}
Status words come from the ledger fold: open, fixed, recurred. `recurred` is printed as REGRESSED
(a verify failed on a fixed incident, or the ledger saw it again after the fix).

verify records through the ledger API (record): a failed check on a FIXED incident is a `recurred` event;
a result that changed on an OPEN incident is a `note`; a pass after `recurred` re-fixes via fix(). A
steady pass on a fixed incident writes nothing (box_watch reads the last event per id, so notes after
`fixed` would hide the fix). Notes carry the prefix "[verify pass]" / "[verify fail]"; unchanged results
are not repeated.
match reads text logs and event lines {ts,host,source,kind,code,summary,evidence_path,sig}
(data/watch/events.<host>.jsonl). watch = match for events whose sig is new; never creates incidents.
Stdlib only, offline, no AI, no timers."""
import argparse, json, os, re, shlex, shutil, signal, socket, stat, subprocess, sys, time
from pathlib import Path
import incident_ledger as led

class SidecarError(Exception):
    """signatures.json exists but is unreadable, corrupt or not shaped like {id: {...}}."""

def side_path(root=...):
    raise NotImplementedError('TODO: implement')

def is_regular(path):
    raise NotImplementedError('TODO: implement')

def read_regular_text(path, warn=True):
    """Text of a regular, non-symlink file, or None (one WARNING on stderr) for a FIFO/device/symlink/unreadable path.
    Opened O_NONBLOCK|O_NOFOLLOW where available so a pipe can never hang us."""
    raise NotImplementedError('TODO: implement')

def load_side(root=...):
    """{} when the sidecar does not exist; SidecarError (loud) when it exists but is not a JSON object of objects."""
    raise NotImplementedError('TODO: implement')

def save_side(side, root=...):
    raise NotImplementedError('TODO: implement')

def _inside(path, root):
    raise NotImplementedError('TODO: implement')

def check_command(cmd, root=...):
    """(argv, None) when `cmd` passes the allow-list, else (None, reason). Pure: runs nothing."""
    raise NotImplementedError('TODO: implement')

def is_read_only(cmd, root=...):
    raise NotImplementedError('TODO: implement')

def why_not_allowed(cmd, root=...):
    raise NotImplementedError('TODO: implement')

def resolve(ref, root=..., side=None):
    raise NotImplementedError('TODO: implement')

def view(root=...):
    """ledger id -> ledger folded state + sidecar fields (the only incident view)."""
    raise NotImplementedError('TODO: implement')

def label(v):
    raise NotImplementedError('TODO: implement')

def preventer_text(v):
    raise NotImplementedError('TODO: implement')

def title_of(v):
    raise NotImplementedError('TODO: implement')

def row(v):
    raise NotImplementedError('TODO: implement')

def catastrophic(pat):
    """Reason string when a signature could hang the matcher, else None."""
    raise NotImplementedError('TODO: implement')

def problems(side_rec, status=None, root=...):
    raise NotImplementedError('TODO: implement')

def lint(root=...):
    raise NotImplementedError('TODO: implement')

class _MatchTimeout(Exception):
    pass

def sig_hit(pat, text):
    """Bounded match: input capped at LINE_CAP chars; where SIGALRM exists the regex gets MATCH_SECONDS, and a
    timed-out signature counts as 'no match' plus one WARNING line (per pattern)."""
    raise NotImplementedError('TODO: implement')

def text_of(line):
    """Event lines match on summary (plus code); anything else is plain text."""
    raise NotImplementedError('TODO: implement')

def match_one(text, v_all):
    """[(view, first matching signature)] for every incident with a signature that hits `text`."""
    raise NotImplementedError('TODO: implement')

def match_text(text, root=...):
    """List of (view, lineno, signature) hits, one per incident per line.
    (A path to a legacy registry *.jsonl file instead of a repo root uses the legacy reader.)"""
    raise NotImplementedError('TODO: implement')

def fmt_hit(v):
    raise NotImplementedError('TODO: implement')

def read_lines(path):
    raise NotImplementedError('TODO: implement')

def current(path):
    """legacy id -> merged latest record, in first-seen order."""
    raise NotImplementedError('TODO: implement')

def legacy_match_text(text, path):
    """[(legacy record, lineno, signature)] against a legacy registry file."""
    raise NotImplementedError('TODO: implement')

def run_verify(rec, timeout=20, root=...):
    """Run a verified_by command: allow-listed argv, NO shell, cwd=root, scrubbed env, own session; on timeout the
    whole process group is killed (a sleeping grandchild would survive a plain kill)."""
    raise NotImplementedError('TODO: implement')

def emit(root, iid, event, detail):
    """Append a note/recurred event to EXACTLY this ledger id. (led.record re-derives the id from the stored
    key, which is wrong when the ledger scrubbed the key, e.g. to '[REDACTED]'.)"""
    raise NotImplementedError('TODO: implement')

def last_verify(root, iid):
    raise NotImplementedError('TODO: implement')

def verify(root=..., timeout=20, runner=None, out=...):
    """Returns the number of failures that matter (fixed incidents whose check fails, unusable checks)."""
    raise NotImplementedError('TODO: implement')

def slug(title):
    raise NotImplementedError('TODO: implement')

def add(root, title, sigs, verified_by, key=None, detail=..., ptype=None, ppath=None, pnote=..., fix_now=False, extra=None, changelog_ref=None):
    """Open (idempotent) a ledger incident and store its signatures. Returns the ledger id."""
    raise NotImplementedError('TODO: implement')

def migrate(root, legacy_file):
    """Idempotent: copy the 7 seeds into the ledger through its API, keyed by SEEDS."""
    raise NotImplementedError('TODO: implement')

def watch(root=..., again=False, out=...):
    """Name repeats of known incidents and report unknown repeating signatures. Creates nothing in the ledger."""
    raise NotImplementedError('TODO: implement')

def main(argv, root=...):
    raise NotImplementedError('TODO: implement')
