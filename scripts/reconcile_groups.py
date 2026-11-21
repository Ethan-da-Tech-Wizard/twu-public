# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Reconcile queue grouping (READ-ONLY). Usage:
  reconcile_groups.py DATA.jsonl [--rules F] [--changelog F] [--git-repo DIR] [--days N] [--now TS] [--tz-hours H] [--json]
DATA is a `sysjournal export` snapshot (JSON lines). Nothing is ever written; evidence is DATA with a cited source,
never a reason. A group's `proposed_reason` is set only when evidence NAMES the changed item and cites its source."""
import argparse, hashlib, json, os, re, subprocess, sys, time, unicodedata

def fold(text):
    raise NotImplementedError('TODO: implement')

def squash(text):
    """Folded text with every separator removed: 'S S H', 'P.A.M', 's-s-h' and 'ss<zero width>h' all become 'ssh'."""
    raise NotImplementedError('TODO: implement')

def denied(component, title):
    """True when (component, title) belongs to a class that must never be noise-excluded. Matched on the raw AND the Unicode-folded text,
    and (title/component words) on the separator-less form."""
    raise NotImplementedError('TODO: implement')

def noise_allowed(component, title, cls=...):
    """Exact match of the RAW strings: both must already be plain ASCII and equal the allowlisted literals. Normalisation is never used to
    ACCEPT (a lookalike or zero-width variant simply does not match); it is used only on the denylist side, where it can only refuse more."""
    raise NotImplementedError('TODO: implement')

def noise_refusal(component, title, cls=...):
    """None if (component, title) may be a noise rule, else the plain reason it may not. Both layers, independent."""
    raise NotImplementedError('TODO: implement')

def row_class(r):
    """Class of a journal row for the noise allowlist."""
    raise NotImplementedError('TODO: implement')

def load(path):
    raise NotImplementedError('TODO: implement')

def eid(r):
    raise NotImplementedError('TODO: implement')

def unexplained(rows, days=30, now=None):
    """Same predicate as sysjournal cmd_unexplained. Returns (unexplained, total_auto)."""
    raise NotImplementedError('TODO: implement')

def load_rules(path):
    """Noise rules are LITERAL: exact component + exact title. No regex, no globs, no wildcards."""
    raise NotImplementedError('TODO: implement')

def parse_rules(data):
    raise NotImplementedError('TODO: implement')

def noise_rule(r, rules):
    """The rule covering row r, or None. Layer 1: (class, component, title) must be on NOISE_ALLOWED. Layer 2: the denylist.
    A rules file (signed or not, hand-edited or not) can never widen either layer."""
    raise NotImplementedError('TODO: implement')

def tickall_safe(path):
    """True only for a passive file type. Pure allowlist: everything not listed is per-entry."""
    raise NotImplementedError('TODO: implement')

def is_allowlisted(title):
    raise NotImplementedError('TODO: implement')

def is_sensitive(r):
    """Not allowlisted == unsafe. The old denylist is kept as a second, independent check."""
    raise NotImplementedError('TODO: implement')

def pattern(title):
    """Normalise a title so siblings group: digits/hashes -> N, path leaf names kept only as their dir."""
    raise NotImplementedError('TODO: implement')

def item_keys(title):
    """(full path variants, exact name). Evidence must carry the whole path or the whole file/unit name as a bounded token."""
    raise NotImplementedError('TODO: implement')

def names_item(text, title):
    raise NotImplementedError('TODO: implement')

def load_changelog(path):
    """[(line_no, text, date_ts_utc_midnight or None)]; date from the nearest '## YYYY-MM-DD' heading above."""
    raise NotImplementedError('TODO: implement')

def load_git(repo):
    raise NotImplementedError('TODO: implement')

def entry_evidence(e, rows, changelog, commits, repo_label=...):
    """Evidence that names THIS entry's exact path/name AND lies inside the time window. Nothing else is evidence of a reason."""
    raise NotImplementedError('TODO: implement')

def digest(g):
    """Staleness check ONLY (anyone can recompute it; it is not authentication). Covers every entry's content and ALL evidence, uncapped."""
    raise NotImplementedError('TODO: implement')

def build_groups(rows, rules=..., changelog=..., commits=..., days=30, now=None, tz_hours=..., repo_label=...):
    raise NotImplementedError('TODO: implement')

def verify_digest(rows, key, seen_digest, **kw):
    """True only if the group `key` still exists with exactly the digest Ethan saw."""
    raise NotImplementedError('TODO: implement')

def counts(groups):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
