# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Read-only EXPLORER backend for the Ethan dashboard (library + small CLI; no HTTP, no network, no model, stdlib only).

  list REL | cat REL [--max-bytes N] | db-tables REL | db-rows REL TABLE [--limit N] [--offset N]   (all print JSON)

Every result is a plain dict with a `mark` {tier, reason} so the UI can explain what it shows.  Tiers:
  OPEN           normal docs/code: content may be shown (secrets still scrubbed with ethan_know.scrub).
  METADATA_ONLY  private areas: name, size, mtime, type and (for SQLite) table row counts, but NO content.
  HIDDEN         secrets (.env, keys, tokens, .aws ...): not listed, not statted, not readable.
Rejected outright: absolute paths, `..`, NUL bytes, symlinks anywhere in the path, special files, anything outside the
repo root, and anything under .git/.  data/dashboard/explorer_policy.json may LATER reveal chosen private paths
(METADATA_ONLY -> OPEN only; HIDDEN can never be revealed).  Defaults are conservative.  Paths are always repo-relative.
"""
import argparse
import html
import json
import os
import re
import sqlite3
import stat
import sys
import unicodedata
from contextlib import closing
from pathlib import Path
import ethan_know as _ek

class ExplorerError(Exception):

    def __init__(self, msg, tier=None, reason=None):
        raise NotImplementedError('TODO: implement')

def _mark(tier, reason):
    raise NotImplementedError('TODO: implement')

def load_policy(root=None):
    """Policy file is optional; malformed or unexpected content falls back to the (conservative) defaults."""
    raise NotImplementedError('TODO: implement')

def _key(name):
    """Comparison form: NFC then casefold (then NFC again, casefold can denormalize)."""
    raise NotImplementedError('TODO: implement')

def _under(rel, prefix):
    raise NotImplementedError('TODO: implement')

def tier_of(rel, root=None):
    """rel: validated posix path ('' = root) built from REAL on-disk names.  -> mark dict.  Compared casefold+NFC."""
    raise NotImplementedError('TODO: implement')

def _resolve(rel, root=None):
    """Validate rel and return (root Path, clean rel, absolute Path).  Raises ExplorerError."""
    raise NotImplementedError('TODO: implement')

def _guard(rel, root, need_open=True):
    """-> (clean, path, mark, lstat).  Raises ExplorerError carrying the mark when not allowed."""
    raise NotImplementedError('TODO: implement')

def _fail(e, rel):
    raise NotImplementedError('TODO: implement')

def _meta(clean, st, mark):
    raise NotImplementedError('TODO: implement')

def list_dir(rel=..., root=None):
    raise NotImplementedError('TODO: implement')

def read_text(rel, max_bytes=..., root=None):
    raise NotImplementedError('TODO: implement')

def _is_sqlite(path):
    raise NotImplementedError('TODO: implement')

def _connect_ro(path):
    raise NotImplementedError('TODO: implement')

def _q(ident):
    raise NotImplementedError('TODO: implement')

def _tables(con):
    raise NotImplementedError('TODO: implement')

def sqlite_tables(rel, root=None):
    """OPEN: tables with columns + row counts.  METADATA_ONLY: tables with row counts only.  Never any row content."""
    raise NotImplementedError('TODO: implement')

def _cell(v):
    raise NotImplementedError('TODO: implement')

def sqlite_rows(rel, table, limit=50, offset=0, root=None):
    raise NotImplementedError('TODO: implement')

def _e(v):
    raise NotImplementedError('TODO: implement')

def _mark_html(r):
    raise NotImplementedError('TODO: implement')

def render_list(r):
    raise NotImplementedError('TODO: implement')

def render_text(r):
    raise NotImplementedError('TODO: implement')

def render_tables(r):
    raise NotImplementedError('TODO: implement')

def render_rows(r):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
