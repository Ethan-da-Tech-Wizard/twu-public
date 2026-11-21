# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""magi: the command every Magi seat uses to join the network, talk, and read its inbox.

A Magi is any CLI agent (Claude Code, Codex, Gemini, Antigravity, or a local-model manager) holding a seat.
Seat N writes only business/example_host/comms/agentN/ (its outbox, presence and inbox cursor). Messages are
validated connection-bound outbox events, so nothing malformed reaches the war room, the compound or the switchboard.
Start here: AGENTS.md and MAGI_0/MASTER_HANDOFF.md.

  python3 scripts/magi.py join   --seat 13 --cli codex --host example_host
  python3 scripts/magi.py who
  python3 scripts/magi.py inbox  --seat 13             # new messages for Magi 13 (marks them read)
  python3 scripts/magi.py send   --seat 13 --to 8 --kind result --packet A13-EXAMPLE-001 "Done; tests 7/7." --file path/to/report.md
  python3 scripts/magi.py room   -n 20
  python3 scripts/magi.py join   --seat auto --cli claude --host example_host   # take an unused or explicitly released ordinary slot
  python3 scripts/magi.py leave  --seat 13             # release your connection slot when you finish
  python3 scripts/magi.py inbox  --seat 13 --digest    # a read-only short summary (use --all to deliver/acknowledge)
  python3 scripts/magi.py inbox  --seat 13 --history  # read-only preserved journal, including earlier occupants
  python3 scripts/magi.py watch  --seat 13 --timeout 600  # sleep until mail arrives; no model, near-zero CPU
"""
import argparse
from contextlib import contextmanager, nullcontext
from contextvars import ContextVar
from datetime import datetime, timezone
import hashlib
import io
import importlib
import importlib.util
import json
import math
import os
import platform
from pathlib import Path
import re
import secrets
import shlex
import shutil
import stat
import subprocess
import sys
import tempfile
import threading
import time
from typing import Optional

def active_seats(root=None):
    """Current routing eligibility, not attendance or authorization to run work."""
    raise NotImplementedError('TODO: implement')

def require_active_seat(seat):
    raise NotImplementedError('TODO: implement')

def normalize_host(host):
    """'host-h' and 'ethans-example_host' are the same machine."""
    raise NotImplementedError('TODO: implement')

def reserved_seats(root=None):
    """Compatibility API: no client, host or role reserves a worker seat."""
    raise NotImplementedError('TODO: implement')

def reservation_matches(entry, cli, host):
    raise NotImplementedError('TODO: implement')

def parse_since(text, now_dt=None):
    """'30m', '2h', '1d' (ago) or an ISO timestamp -> ISO string events can be compared against."""
    raise NotImplementedError('TODO: implement')

def digest(events, newest=5):
    """A few lines that say what is waiting: counts by sender and kind, then the newest one-liners."""
    raise NotImplementedError('TODO: implement')

def startup_brief():
    """Small, read-only orientation; historical journals are deliberately not consulted."""
    raise NotImplementedError('TODO: implement')

@contextmanager
def _event_record_snapshot():
    """One validated view for a read-only report; never retained between requests."""
    raise NotImplementedError('TODO: implement')

def all_event_records():
    """Validated delivery records plus validator quarantine metadata, never raw rejected content."""
    raise NotImplementedError('TODO: implement')

def _quarantine_reason(reason):
    """Map validator detail to a public-safe category; validator text can be input-adjacent."""
    raise NotImplementedError('TODO: implement')

def quarantine_diagnostic(records=None, maximum=3):
    """A bounded, metadata-only warning for rejected outbox records.

    Rejected payloads are intentionally never printed by inbox, room, or catch-up.  The location is
    validator-generated (agentN/outbox.jsonl:line), and the reason is a fixed category.
    """
    raise NotImplementedError('TODO: implement')

def refresh_loom():
    """Best-effort projection after a durable work outcome; it never changes delivery success."""
    raise NotImplementedError('TODO: implement')

def short_host(name):
    """Hosts compare by casefolded short name; Macs report themselves with a .local suffix."""
    raise NotImplementedError('TODO: implement')

def load_beacons(now_ts=None, directory=None):
    """Read-only, untrusted input: {short_host: ts}. Symlinks, oversize/malformed files, non-numeric, non-positive or
    future timestamps, and a host field that does not match the file name are skipped (the host then reads 'unknown')."""
    raise NotImplementedError('TODO: implement')

def delivery_status(event_ts, recipient_host, beacons, now, local_hosts=...):
    """Pure. -> (status, seconds). 'same-host' (None); 'delivered-likely' (recipient beacon newer than the event; seconds
    = beacon - event; beacon timing only, not receipt proof); 'in-flight' (older beacon; seconds = now - beacon,
    the beacon age, not a transport connection check); 'unknown' (host unknown, no/invalid beacon or timestamp). No alias guessing: fails safe."""
    raise NotImplementedError('TODO: implement')

def _span(seconds):
    raise NotImplementedError('TODO: implement')

def delivery_line(event, recipient_host, now_ts=None, beacons=None):
    """One-line delivery note for an event (None when there is no single recipient host)."""
    raise NotImplementedError('TODO: implement')

def seat_host(seat):
    raise NotImplementedError('TODO: implement')

def sent_delivery_suffix(row, events_by_id, now_ts, beacons, hosts):
    """' [delivery: ...]' for an open item this seat sent; '' when not addressed to one seat."""
    raise NotImplementedError('TODO: implement')

def is_reminder(event, sender=None):
    """A nudge the original sender re-sent (fixed-form summary); it never counts as a reply or as a new thread."""
    raise NotImplementedError('TODO: implement')

class _LaterReplies:
    """Suffix witnesses for reply links and claim closers, without rescanning later events.

    Two distinct IDs suffice to answer whether a reply differs from a thread's
    own ID. Reminder witnesses stay separate by sender: only the original
    sender's reminders are excluded. Add an event after querying it so stable
    ordering, including equal timestamps, matches the forward scan.
    """

    def __init__(self):
        raise NotImplementedError('TODO: implement')

    def add(self, event):
        raise NotImplementedError('TODO: implement')

    def has_reply(self, event):
        raise NotImplementedError('TODO: implement')

def open_threads(seat=None, min_age_hours=0.0, now_dt=None):
    """Read-only: blocked/question/proposal/assignment (and claims over 4 h old) with no later event whose reply_to
    names them. Heuristic: a reply that sets no reply_to, or a result for a claim under another packet, is not seen."""
    raise NotImplementedError('TODO: implement')

def threads_text(rows, limit=None, seat=None):
    raise NotImplementedError('TODO: implement')

def seat_threads_block(seat):
    raise NotImplementedError('TODO: implement')

def carryover_rows(seat, now_dt=None):
    """Unanswered history and later old-connection mail, without transferring ownership."""
    raise NotImplementedError('TODO: implement')

def carryover_block(seat, now_dt=None):
    raise NotImplementedError('TODO: implement')

def thread_events(reference):
    """Read one conversation, including ancestors and nested replies; never acknowledge it."""
    raise NotImplementedError('TODO: implement')

def nudge_due(age_hours, nudges_sent):
    """Pure: 'nudge' | 'escalate' | None for an unanswered message of this age with this many nudges already sent."""
    raise NotImplementedError('TODO: implement')

def nudge_state_path(seat):
    raise NotImplementedError('TODO: implement')

def read_nudge_state(seat):
    """{event_id: {"nudges": int, "escalated": bool}}. Missing file is empty; anything malformed raises ValueError
    (fail closed) and the file is left untouched."""
    raise NotImplementedError('TODO: implement')

def write_nudge_state(seat, items):
    raise NotImplementedError('TODO: implement')

def _pending_rows(now_dt=None):
    """open_threads rows (reminders are never rows); an answered reminder (a later non-reminder event with reply_to =
    its id or packet) closes the original it repeats."""
    raise NotImplementedError('TODO: implement')

def _clean(value):
    raise NotImplementedError('TODO: implement')

def _occupant_since(seat):
    """ISO start of this seat's current connection (inbox_since). A new occupant never inherits an earlier occupant's
    threads, reminders or sent items (AGENTS.md). None when there is no usable presence: callers then show nothing."""
    raise NotImplementedError('TODO: implement')

def pending_for(seat, now_dt=None):
    """Read-only: open_threads(seat) rows plus nudge_due (bool) and nudges (int sent so far by the sender)."""
    raise NotImplementedError('TODO: implement')

def pending_block(seat, now_dt=None):
    """PENDING block: items addressed to this seat (not sent by it) that still need a reply; oldest first."""
    raise NotImplementedError('TODO: implement')

def sent_pending_block(seat, now_dt=None, limit=5):
    """Read-only: items this seat SENT that are still open, each with a delivery suffix (beacon lower-bound proof)."""
    raise NotImplementedError('TODO: implement')

def _is_escalation(event):
    """The send prefix ('To all: ') comes before the fixed text, so match with the same optional prefix as _REMINDER_RE."""
    raise NotImplementedError('TODO: implement')

def _merge_outbox_reminders(item, own, original_id, sender):
    """Raise the state's counters to what this seat's own outbox already holds for one original: reminders sent
    (reply_to = original), whether the escalation went out, and the latest send time (gap guard)."""
    raise NotImplementedError('TODO: implement')

def nudge(seat, connection_id=None, now_dt=None):
    """Re-send (one step per item per call) pending items this seat itself sent. Returns [(id, action, note)].
    Fixed-form text only (never the original text); reply_to = original id; reads only this seat's own outbox."""
    raise NotImplementedError('TODO: implement')

def auto_nudge(seat, connection_id, say=None):
    """Authenticated, schedule-rate-limited nudge for a seat's own heartbeat; never raises (a failure only reports)."""
    raise NotImplementedError('TODO: implement')

def _doctor_age(iso, now_dt):
    raise NotImplementedError('TODO: implement')

def _journal_capacity():
    """Measure bounded outboxes; report incomplete visibility without mutating journals."""
    raise NotImplementedError('TODO: implement')

def journal_capacity():
    raise NotImplementedError('TODO: implement')

def doctor(seat=None, now_dt=None, host=None):
    """Read-only self-check for this host. -> list of {"check", "seat", "status", "detail"}; status is PASS, FAIL or
    UNKNOWN (never a guess: an UNKNOWN names the dependency). Writes nothing, sends nothing, prints no token."""
    raise NotImplementedError('TODO: implement')

def doctor_summary(rows):
    raise NotImplementedError('TODO: implement')

def doctor_lines(rows):
    raise NotImplementedError('TODO: implement')

def catchup(host=None, now_dt=None):
    """One login brief: this host's seats, their unread mail, the handoff and the direction board.

    Reads only — never marks a cursor, never touches presence, never sends. Generated status, not instructions.
    """
    raise NotImplementedError('TODO: implement')

def write_catchup(text, host=None):
    """Atomically save the brief as data/catchup/<shorthost>.md; each host writes only its own file."""
    raise NotImplementedError('TODO: implement')

def open_seats(now_dt=None, live_minutes=..., skip_unverifiable=False):
    """Unused or released ordinary slots; an old timestamp never proves vacancy.

    Reserved device seats never enter the ordinary pool. Unverifiable records are
    excluded from allocation, never treated as vacant."""
    raise NotImplementedError('TODO: implement')

def seat_ttl_hours():
    raise NotImplementedError('TODO: implement')

def is_reserved_seat(seat):
    raise NotImplementedError('TODO: implement')

def stale_seat_hours(seat, row, now_dt=None, ttl_hours=None):
    """Hours of inactivity after the diagnostic threshold, or None.

    A running but idle CLI does not renew its lease: authenticated Magi actions and watch refresh
    last_seen. Inactivity never permits takeover. Reserved device seats are excluded."""
    raise NotImplementedError('TODO: implement')

def stale_seats(now_dt=None, ttl_hours=None):
    raise NotImplementedError('TODO: implement')

def log_occupancy(seat, event, row, reason):
    """Append-only record of who held a seat before it changed hands (the earlier-occupants journal)."""
    raise NotImplementedError('TODO: implement')

@contextmanager
def _readonly_presence():
    raise NotImplementedError('TODO: implement')

def _check_state_parent_dirs(path):
    """Verify COMMS, any intermediate directories under ROOT, and path.parent are safe directories."""
    raise NotImplementedError('TODO: implement')

class AmbiguousOwnership(ValueError):
    """A presence conflict that cannot be resolved without evicting or inventing a seat owner."""

def _sync_conflict_files(path):
    """Syncthing conflict copies sitting beside a state file (bounded, sorted)."""
    raise NotImplementedError('TODO: implement')

def _conflict_time(document, fallback):
    """Newest-wins key: a valid timezone-aware last_seen, else the file mtime."""
    raise NotImplementedError('TODO: implement')

def _atomic_state_write(path, data):
    raise NotImplementedError('TODO: implement')

def _read_conflict_bytes(path):
    """Bounded read of a plain regular single-link file; anything else is not safe to merge."""
    raise NotImplementedError('TODO: implement')

def _archive_sync_conflict(path, copy, label=None):
    """Copy the original and the conflict copy to data/resolved_sync_conflicts/<stamp>/ (0600). Returns the dir."""
    raise NotImplementedError('TODO: implement')

def _merge_jsonl_conflict(path, copy):
    raise NotImplementedError('TODO: implement')

def _pick_json_conflict(path, copy):
    """Newest valid document wins; an unparseable copy is left for repair and an unparseable original loses."""
    raise NotImplementedError('TODO: implement')

def resolve_sync_conflicts(path):
    """Self-repair Syncthing conflict copies beside a state file; never raises, never blocks a join.

    Journals (*.jsonl) are merged (union, de-duplicated, sorted by timestamp); single JSON documents keep the
    newest valid version. Both files are archived first. An unsafe or unmergeable copy is archived, left in
    place and reported by doctor as a repair task while the original file keeps being used.
    Returns [(conflict name, ambiguous_ownership)] for copies that remain unresolved.
    """
    raise NotImplementedError('TODO: implement')

def unresolved_sync_conflicts():
    """Read-only scan of seat dirs for leftover conflict copies (doctor repair tasks)."""
    raise NotImplementedError('TODO: implement')

def checked_state_path(path):
    """Reject redirected state before reading or writing; self-repair Syncthing conflict copies (never blocks)."""
    raise NotImplementedError('TODO: implement')

def read_state_text(path, maximum=...):
    raise NotImplementedError('TODO: implement')

def write_state(path, record):
    raise NotImplementedError('TODO: implement')

def _read_regular_state_json(path, maximum=...):
    """Read and parse JSON from a bounded non-symlink single-link regular file."""
    raise NotImplementedError('TODO: implement')

def _validate_presence_dict(presence, seat):
    """Validate required fields and timezone-aware timestamps of a presence dictionary."""
    raise NotImplementedError('TODO: implement')

def read_presence(seat):
    """Unknown ownership is never an available seat."""
    raise NotImplementedError('TODO: implement')

@contextmanager
def join_lock():
    """Serialize this host's joins (re-entrant per thread); Syncthing is not a distributed lock."""
    raise NotImplementedError('TODO: implement')

def ethan_seat(cli, host):
    """Legacy import alias for the next available shared worker slot."""
    raise NotImplementedError('TODO: implement')

def local_host_names():
    """This machine's names, read locally (no network): node, scutil LocalHostName/ComputerName on macOS."""
    raise NotImplementedError('TODO: implement')

def ethan_seat_help(cli, host, matches):
    """Compatibility text: every provider uses the same ascending pool."""
    raise NotImplementedError('TODO: implement')

def mail_stamp():
    """Cheap change detector for the watch loop: size and mtime of every outbox (no parsing)."""
    raise NotImplementedError('TODO: implement')

def _is_released_error(error):
    raise NotImplementedError('TODO: implement')

def watch(seat, interval=5.0, timeout=None, say=..., connection_id=None, persist=False):
    """Explicit mail wait, with one optional supervised child per workspace slot."""
    raise NotImplementedError('TODO: implement')

def _watch(seat, interval=5.0, timeout=None, say=..., connection_id=None, persist=False):
    """Sleep until a message arrives for this seat (exit 0) or the timeout passes (exit 3). Never calls a model.

    persist=True (supervised mode) never exits on mail or timeout: it prints each new mail digest once and keeps
    looping, recording watch_checked_at + last_nudge_check every <= PERSIST_HEARTBEAT_SECONDS and running
    auto_nudge. Exit codes: 0 = STOP latch present (stop, do not restart); 4 = connection released/replaced/invalid
    token (do not restart; the seat must join again); 5 = repeated heartbeat failures (restart is fine)."""
    raise NotImplementedError('TODO: implement')

def _keeper_spawn(seat, token_env):
    """Start one `watch --persist` child. The token travels only in the child's environment."""
    raise NotImplementedError('TODO: implement')

def _keeper_stop_child(proc, wait=5.0):
    raise NotImplementedError('TODO: implement')

def _keeper_read_tokens(bad, say):
    """Bound work to the configured slots and private, current local credentials."""
    raise NotImplementedError('TODO: implement')

def keeper_pass(state, clock, say=..., bad=None):
    """One scan/spawn/reap pass. state: {seat: dict(proc, token, started, backoff, next, halt)}."""
    raise NotImplementedError('TODO: implement')

def keeper(once=False, interval=10.0, say=..., sleep=None, clock=None):
    """Machine-local supervisor: one `watch --persist` child per token file. Returns 0 on STOP or --once."""
    raise NotImplementedError('TODO: implement')

def now():
    raise NotImplementedError('TODO: implement')

def seat_dir(seat):
    raise NotImplementedError('TODO: implement')

def serialize_claims(fn):
    """Serialize local read/modify/write; Syncthing cannot provide cross-host locking."""
    raise NotImplementedError('TODO: implement')

def write_claims(claims):
    raise NotImplementedError('TODO: implement')

def unexpired_claims(claims, now):
    """Retain conflict evidence; reject malformed records before removing expired claims."""
    raise NotImplementedError('TODO: implement')

def _claim_path(path):
    """Reject lexical aliases that could bypass path-specific conflict checks."""
    raise NotImplementedError('TODO: implement')

def _claim_identity(path):
    """Conservatively collapse case and Unicode variants across fleet platforms."""
    raise NotImplementedError('TODO: implement')

def _claim_key(claims, path):
    raise NotImplementedError('TODO: implement')

def _prepare_claim_parent():
    """Reject symlinks in workspace-relative claim directories before use."""
    raise NotImplementedError('TODO: implement')

def _unique_dest(directory, name):
    raise NotImplementedError('TODO: implement')

def _read_claim_ledger(path, missing_ok=False):
    """Read a bounded regular local ledger without following its final symlink."""
    raise NotImplementedError('TODO: implement')

def _claim_ledgers():
    """Return canonical records and locally visible differing conflict-copy paths.

    Copies are evidence, not a cross-host lock. A missing remote copy is unknown.
    """
    raise NotImplementedError('TODO: implement')

def _historical_claim_owner(seat, token):
    """Only modern, bounded local release evidence identifies a previous owner."""
    raise NotImplementedError('TODO: implement')

def _released_claim_owner(existing):
    """Proof for one abandoned local claim; age alone never releases ownership.

    A replaced presence needs exact modern release history; legacy records that
    omitted connection/kernel birth identities cannot establish an older owner.
    The caller already holds the join and claim locks while checking this proof.
    """
    raise NotImplementedError('TODO: implement')

def authenticated_claim(fn):
    raise NotImplementedError('TODO: implement')

@authenticated_claim
@serialize_claims
def claim_path(path: str, seat: int, connection: Optional[str]=None, ttl: int=300) -> dict:
    raise NotImplementedError('TODO: implement')

@authenticated_claim
@serialize_claims
def claim_release(path: str, seat: int, connection: Optional[str]=None) -> dict:
    raise NotImplementedError('TODO: implement')

@serialize_claims
def claim_verify(path: Optional[str]=None) -> dict:
    raise NotImplementedError('TODO: implement')

@serialize_claims
def _release_connection_claims_locked(seat, connection):
    raise NotImplementedError('TODO: implement')

def release_connection_claims(seat, connection):
    """Retire only exact, unconflicted claims when their authenticated connection ends."""
    raise NotImplementedError('TODO: implement')

def all_events():
    raise NotImplementedError('TODO: implement')

def own_events(seat):
    raise NotImplementedError('TODO: implement')

def addressed_to(event, seat):
    raise NotImplementedError('TODO: implement')

def route_alias(name):
    """Resolve a device name only when its current connection is unambiguous.

    Presence is reported state, not proof of attendance or delivery. A broken
    presence record may hide another candidate, so it makes resolution unknown.
    """
    raise NotImplementedError('TODO: implement')

def require_connection(seat, connection_id=None):
    raise NotImplementedError('TODO: implement')

def touch_presence(seat, connection_id=None):
    raise NotImplementedError('TODO: implement')

def heartbeat_for_connection(connection_id):
    """Refresh the seat holding this token (commands that carry no seat number); silent when none matches."""
    raise NotImplementedError('TODO: implement')

def recipient_check(to, sender=None, even_if_unread=False, say=None):
    """CLI-layer guard: refuse a message to a seat nobody has ever joined (unless even_if_unread); warn when the
    seat exists but no live reader is attached. Never touches `all`, unresolvable targets (send reports those),
    or reserved device seats only with even_if_unread (queued mail for a CLI that joins later). Returns the seat state or None."""
    raise NotImplementedError('TODO: implement')

def reply_reference_index(events):
    """Full event IDs are authoritative; packet names are aliases only when unique."""
    raise NotImplementedError('TODO: implement')

def reply_reference_parent(reference, indexed, packets, child_id=None):
    raise NotImplementedError('TODO: implement')

def send(seat, to, kind, packet, text, files=..., status=None, reply_to=None, connection_id=None, strict=False):
    raise NotImplementedError('TODO: implement')

def _send(seat, to, kind, packet, text, files=..., status=None, reply_to=None, strict=False):
    raise NotImplementedError('TODO: implement')

def instruction_redirect(path, archive):
    """Pointer text has no local policy to drift from the single authority."""
    raise NotImplementedError('TODO: implement')

def instruction_file(root, relative):
    raise NotImplementedError('TODO: implement')

def exact_file(path):
    """True only for a regular file whose on-disk name matches byte for byte.

    Archived history is recorded by exact path. On a case-insensitive disk (the Mac) a lookup for
    `inbox_cursor.json` is satisfied by `INBOX_CURSOR.json`, so a peer would hash the wrong file
    and report registered history as changed. Case-sensitive hosts behave exactly as before.
    """
    raise NotImplementedError('TODO: implement')

def instruction_state(root=None, host=None):
    """Fail closed on missing, modified or unregistered startup pointers; never rewrite them."""
    raise NotImplementedError('TODO: implement')

def require_current_instructions():
    raise NotImplementedError('TODO: implement')

def _process_observation(pid):
    """Kernel identity/parent, explicit dead, or None when inspection is unavailable."""
    raise NotImplementedError('TODO: implement')

def process_start(pid):
    """Kernel birth identity of a live process; None alone is not proof of death."""
    raise NotImplementedError('TODO: implement')

def _pid_namespace():
    raise NotImplementedError('TODO: implement')

def _process_arguments(pid):
    """Read bounded argv, never shell text masquerading as an executable."""
    raise NotImplementedError('TODO: implement')

def _wrapper_owner():
    raise NotImplementedError('TODO: implement')

def _shared_owner(pid):
    raise NotImplementedError('TODO: implement')

def owner_process(cli, start=None):
    """Find a real CLI executable or a verified lifecycle wrapper ancestor."""
    raise NotImplementedError('TODO: implement')

def owner_alive(presence, local_host=None):
    """True/False when this host can prove whether the seat's owning process lives; None when it cannot."""
    raise NotImplementedError('TODO: implement')

def _is_descendant_of(child_pid, ancestor_pid):
    """Return True if ancestor_pid is an ancestor of child_pid, else False."""
    raise NotImplementedError('TODO: implement')

def helper_lock_path(kind):
    """Host-private supervision locks; workspace identity prevents clone collisions."""
    raise NotImplementedError('TODO: implement')

def helper_lock(kind, wait_seconds=0.0):
    """Return one owned lock descriptor, or None when already supervised."""
    raise NotImplementedError('TODO: implement')

def adopt_helper_lock(kind, env_name):
    """Validate a parent-reserved lock or acquire one for a manual helper."""
    raise NotImplementedError('TODO: implement')

def _lifecycle_unit_properties():
    """Only fixed public fields from two fixed user units; no logs or environment."""
    raise NotImplementedError('TODO: implement')

def supervision_status():
    """Read-only bounded host health; never use it as proof of agent attendance."""
    raise NotImplementedError('TODO: implement')

def spawn_sentinel(seat, owner_pid, owner_start, connection_id):
    raise NotImplementedError('TODO: implement')

def reap(local_host=None, legacy_hours=None, dry_run=False, all_hosts=False, seats=None, force_reserved=False):
    """Release seats on this host whose owning process is gone. Returns [(seat, reason)].

    Only a proven-dead local owner releases a seat. Legacy age and remote-host
    flags are accepted for compatibility but cannot authorize a release."""
    raise NotImplementedError('TODO: implement')

def keeper_dir():
    raise NotImplementedError('TODO: implement')

def _keeper_enabled():
    """Tokens go to the keeper dir when MAGI_KEEPER_DIR is set or when running against the real comms tree."""
    raise NotImplementedError('TODO: implement')

def _private_dir(path):
    """Create/verify a 0700 directory owned by us; refuse symlinks."""
    raise NotImplementedError('TODO: implement')

def keeper_token_path(seat):
    raise NotImplementedError('TODO: implement')

def write_keeper_token(seat, connection_id, host):
    """Atomically write <keeper>/tokens/<seat> (0600 in a 0700 dir). Raises OSError; never prints the token."""
    raise NotImplementedError('TODO: implement')

def remove_keeper_token(seat):
    """Best effort; removes only the seat's own token file."""
    raise NotImplementedError('TODO: implement')

def read_keeper_token(seat):
    """Read this user's private exact-connection credential; never expose it in a roster."""
    raise NotImplementedError('TODO: implement')

def _inherited_wrapper(cli, host):
    raise NotImplementedError('TODO: implement')

def _valid_client_id(value):
    raise NotImplementedError('TODO: implement')

def ensure_client_connection(thread_id, turn_id, agent_id=None, parent_thread_id=None, connection_id=None):
    """Admit an exact client work generation; never borrow a successor's credentials."""
    raise NotImplementedError('TODO: implement')

def join(seat, cli, host, session=None, start_daemons=False, connection_id=None, client_thread_id=None, client_generation=None, client_agent_id=None, parent_thread_id=None):
    raise NotImplementedError('TODO: implement')

def release_exited_owner(seat, pid, start, connection_id):
    """Release and journal a proven-dead local owner, bound to its exact connection.

    A sentinel's earlier observation is insufficient: recheck both ownership and
    kernel identity while holding the join lock so a replacement cannot be freed.
    Unknown or remote process state never authorizes release.
    """
    raise NotImplementedError('TODO: implement')

def leave(seat, connection_id=None, force=False, reason=...):
    """Release a connection slot so the next auto-join can take it at once. The presence row and history stay."""
    raise NotImplementedError('TODO: implement')

def _presence_revision(row):
    raise NotImplementedError('TODO: implement')

def _connection_state(row):
    raise NotImplementedError('TODO: implement')

def _roster_events(seat):
    """Only bounded arrival/departure metadata; no private messages or credentials."""
    raise NotImplementedError('TODO: implement')

def roster_snapshot():
    """Shared, read-only source of truth for CLI and Herder; never equate freshness with activity."""
    raise NotImplementedError('TODO: implement')

def confirm_closed(seat, revision, source, confirmed=False):
    """Explicit owner confirmation for an exact unknown local record, never an age-based takeover."""
    raise NotImplementedError('TODO: implement')

def lifecycle_once():
    """Bounded local maintenance: verified exits and a host-owned diagnostic receipt; no model calls."""
    raise NotImplementedError('TODO: implement')

def _presence_fresh(p):
    raise NotImplementedError('TODO: implement')

def who():
    raise NotImplementedError('TODO: implement')

def cursor_seen(cursor_path):
    """Read modern and legacy cursors; never overwrite malformed delivery evidence."""
    raise NotImplementedError('TODO: implement')

def connection_seen(seat, path):
    raise NotImplementedError('TODO: implement')

def acknowledge(seat, event_ids, connection_id=None):
    raise NotImplementedError('TODO: implement')

def _acknowledge(seat, event_ids):
    """Atomically acknowledge only explicitly handled events in this seat's cursor."""
    raise NotImplementedError('TODO: implement')

def session_mail(seat, events, seen, presence=None, history=False):
    """Connection delivery is separate from the append-only work journal."""
    raise NotImplementedError('TODO: implement')

def inbox(seat, mark=True, since=None, history=False, connection_id=None):
    raise NotImplementedError('TODO: implement')

def _operator_events(seat):
    """Tasks the human operator sent from the dashboard (not a seat); see scripts/operator_tasks.py. Never raises."""
    raise NotImplementedError('TODO: implement')

def _inbox(seat, mark=True, since=None, history=False):
    raise NotImplementedError('TODO: implement')

def fmt(e):
    raise NotImplementedError('TODO: implement')

def brief_set(text, now_dt=None, root=None):
    """Validate then atomically replace MAGI_0/MASTER_HANDOFF.md, archiving the old brief first. Raises SystemExit on refusal."""
    raise NotImplementedError('TODO: implement')

def rules_notice(**kw):
    """Stage B: the one 'Rules vN (digest): K changed' line (+ CORE.md pointer). WARN ONLY: any failure becomes a short warning, never an error or exit."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
