# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""twu_rules: the rules registry, STAGE A (report only; nothing here blocks a join, a send or any gate). Offline, no AI, no network.

  twu_rules.py list [--all]            every current rule: id, label, status, scope, core, enforcement
  twu_rules.py lint                    size caps, unique ids, seals, write-once, enforcement refs, generated-region check; counts unenforced debt
  twu_rules.py render [--essentials|--check]   write data/rules/CORE.md (generated); --essentials prints the AGENTS.md block; --check compares AGENTS.md to it
  twu_rules.py digest                  'v22 (abcd1234)' plus the full digest
  twu_rules.py line [--acked DIGEST]   the one status line a join could print later
  twu_rules.py changed [--since-digest D] [--seat N]   rules changed since an ack (or digest): id, label, one line each
  twu_rules.py ack [--seat N] [--connection ID]        record that you read the current digest (manual ack; join records an auto one)
  twu_rules.py audit                   every rule's source quote, so Ethan can check a scribe quoted him truthfully
  twu_rules.py propose --by NAME --text "..." --why "..."   append to this host's data/rules/proposals/<host>.jsonl (anyone may; nobody is bound)
  twu_rules.py ratify PID --quote "..." --date YYYY-MM-DD --witness NAME [--enforcement REF] [--scope S] [--owner O]
  twu_rules.py seed [--from FILE]      one-time migration: write R0001..R0022 from the AGENTS.md ESSENTIALS block (refuses to overwrite)

Layout: data/rules/ledger/R<NNNN>.v<N>.json (write-once; a change is a new vN that names the old), data/rules/proposals/<host>.jsonl, data/rules/acks/<host>.jsonl,
data/rules/seals/<host>.jsonl (a second witness of each file's seal), data/rules/CORE.md (generated), data/rules/golden/ (frozen copy of the migrated block).
Enforcement is NEVER a shell string: wiring:<manifest id> | check_all:<name> | test:<path>[::test_name] | magi:<subcommand ...> | unenforced: <why>.
A reference 'resolves' when its target exists; lint does not run the check. Honest limit: nothing can prove a scribe quoted Ethan truthfully; `audit` makes it checkable in a minute.
"""
from __future__ import annotations
import datetime, hashlib, json, os, platform, re, stat, sys, time, uuid
from pathlib import Path

def words(s):
    raise NotImplementedError('TODO: implement')

def host():
    raise NotImplementedError('TODO: implement')

def seal(rec):
    raise NotImplementedError('TODO: implement')

def D(root):
    raise NotImplementedError('TODO: implement')

def read_regular(path, cap=..., tail=False, strict=False):
    """Text of a REGULAR file only (never a FIFO, device, directory or symlink: opening those can block forever). lstat first, then O_NONBLOCK|O_NOFOLLOW and an fstat re-check.
    Over `cap` bytes: OSError, or with tail=True only the last `cap` bytes (the cut first line is dropped). strict=True raises UnicodeDecodeError instead of replacing bad bytes."""
    raise NotImplementedError('TODO: implement')

def _ts(j):
    """A numeric timestamp from an ack record whatever its ts holds (number, ISO string, garbage -> 0)."""
    raise NotImplementedError('TODO: implement')

def load_rules(root=...):
    """(records, problems). Never raises: a half-synced, empty, malformed or conflicted file is reported and skipped; the rest still load."""
    raise NotImplementedError('TODO: implement')

def _load(root=...):
    """(records, problems, bad) where bad counts only files that LOOK like rules (R<digits>.v<digits>.json) but could not be used."""
    raise NotImplementedError('TODO: implement')

def current_rules(recs):
    """Highest version of each id."""
    raise NotImplementedError('TODO: implement')

def live_rules(recs):
    raise NotImplementedError('TODO: implement')

def digest_and_version(recs):
    """(sha256 hex, version N = number of ledger files). Digest over sorted 'id@v|scope|text' of ratified current rules; file order cannot matter."""
    raise NotImplementedError('TODO: implement')

def short(recs):
    raise NotImplementedError('TODO: implement')

def rules_changed_since(recs, acked, hashes=None):
    """Rules changed since an ack. `acked` = collection of 'id@v' strings, or a digest string (equal to today's: nothing changed; anything else: unknown, so all).
    `hashes` = {id: seal(rule)} from a new-style ack: a live rule is changed when its content hash differs (an in-place edit keeps id@v but not its seal).
    A rule the acker had that is now retired comes back as a copy marked _retired=True (announced as 'RETIRED: ...'). Old acks (ids only) stay supported."""
    raise NotImplementedError('TODO: implement')

def _ack_basis(j):
    """(ids, hashes) from an ack record, tolerating old acks and garbage."""
    raise NotImplementedError('TODO: implement')

def _rtext(r, n=60):
    raise NotImplementedError('TODO: implement')

def status_line(recs, acked=None):
    raise NotImplementedError('TODO: implement')

def _label_num(r):
    raise NotImplementedError('TODO: implement')

def render_essentials(recs):
    """The AGENTS.md ESSENTIALS block (intro, E-lines, source line), no trailing newline."""
    raise NotImplementedError('TODO: implement')

def render_core(recs):
    """(text, problems). CORE.md: first line carries the digest; the core rules only; <= 450 words."""
    raise NotImplementedError('TODO: implement')

def _wiring_ids(root):
    raise NotImplementedError('TODO: implement')

def resolve_ref(root, ref):
    """(ok, why). Existence only: the target must exist; nothing is executed."""
    raise NotImplementedError('TODO: implement')

def agents_block(root):
    """(state, text): state 'absent' | 'ok' | 'broken'."""
    raise NotImplementedError('TODO: implement')

def _seal_log(root):
    raise NotImplementedError('TODO: implement')

def rules_lint(root=...):
    """dict: problems (must fix), warnings, counts. Never raises."""
    raise NotImplementedError('TODO: implement')

def _atomic_write(path, text):
    raise NotImplementedError('TODO: implement')

def write_rule(root, rec):
    """Write a sealed, write-once rule file. Raises FileExistsError if that id+version exists (atomic: hard link, never replace).
    Fallback (decision 2026-11-08): on a filesystem without hard links (os.link raises OSError other than FileExistsError) create the target with O_CREAT|O_EXCL, which is
    also write-once; the only cost is that a reader may briefly see a partial file, which load_rules already reports as 'empty/not valid JSON (half-synced?)' and skips."""
    raise NotImplementedError('TODO: implement')

def parse_essentials(text):
    raise NotImplementedError('TODO: implement')

def seed(root=..., golden=None):
    """One-time migration of E1-E22 into R0001..R0022. Skips ids that exist (never overwrites). Returns (written, skipped)."""
    raise NotImplementedError('TODO: implement')

def propose(root, by, text, why):
    raise NotImplementedError('TODO: implement')

def proposals(root):
    raise NotImplementedError('TODO: implement')

def ratify(root, pid, quote, date, witness, enforcement=None, scope=..., owner=...):
    """Write the next write-once rule from a proposal. Refuses: empty quote/witness, bad date, witness == proposer, unknown or already-ratified proposal, over-long text."""
    raise NotImplementedError('TODO: implement')

def record_ack(root, who, digest, ids, mode=..., hashes=None):
    """Append to this host's ack shard. who = {'seat':..,'cli':..,'connection':..}. One writer per host, so hosts never share a file.
    hashes = {rule id: seal(rule)} so a later in-place edit or retirement is noticed; a partial last line (no newline) gets a newline first."""
    raise NotImplementedError('TODO: implement')

def last_ack(root, who):
    raise NotImplementedError('TODO: implement')

def bypassed():
    """True when MAGI_RULES=off or the local, unsynced ~/.twu/rules_off file exists."""
    raise NotImplementedError('TODO: implement')

def who_key(seat=None, connection=None, cli=None, host_=None):
    """Per-seat key: seat + connection_id when there is one, else host + cli."""
    raise NotImplementedError('TODO: implement')

def find_ack(root, seat=None, connection=None, cli=None, host_=None):
    """Latest ack for this connection, else for this seat (any connection: a rejoin is the same slot), else for host+cli. None if none."""
    raise NotImplementedError('TODO: implement')

def seen_path(root, h=None):
    raise NotImplementedError('TODO: implement')

def write_seen(root, recs):
    raise NotImplementedError('TODO: implement')

def _changed_text(ch):
    raise NotImplementedError('TODO: implement')

def notice_lines(root=..., seat=None, connection=None, cli=None, host_=None, ack_auto=False, core=False, seen=False):
    """The Stage B lines for join/catchup/inbox. Never raises, never blocks, no network, no subprocess.
    ack_auto records an auto ack (delivered, not understood) AFTER the line is computed; seen records data/rules/seen/<host>.json."""
    raise NotImplementedError('TODO: implement')

def seen_report(root=...):
    """(ledger digest or None, this host's seen digest or None, {other host: digest}). Never raises."""
    raise NotImplementedError('TODO: implement')

def changed_view(root, since_digest=None, seat=None):
    """(header, lines): the live rules whose id@v is not in the chosen ack. since_digest picks an ack that recorded that digest (prefix ok)."""
    raise NotImplementedError('TODO: implement')

def _opt(a, name, default=None):
    raise NotImplementedError('TODO: implement')

def main(a=None, root=None):
    raise NotImplementedError('TODO: implement')
