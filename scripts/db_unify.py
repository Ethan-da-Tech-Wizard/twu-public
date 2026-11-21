# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""db_unify.py — build ONE deduplicated, read-only view of the per-machine databases. Never writes to a source.

  python3 scripts/db_unify.py plan  [--root DIR]                 # report groups, rows, duplicates (read-only)
  python3 scripts/db_unify.py build [--root DIR] [--out FILE]    # write a NEW unified db; sources are hashed before and after
  python3 scripts/db_unify.py verify --out FILE                   # recount the unified db against its own manifest

Why this shape: per-machine files (x.mac.db / x.linux.db, x_macos_darwin.db, *.sync-conflict-*.db) stay separate on purpose
(two machines must never write one SQLite file). This tool only READS them and writes a separate unified.db with every
distinct row once, tagged with the source file and a content hash. There is no delete or update operation to get wrong.
Refused: twu_ledger.db (the books change only through the TWU tools, Rule 7), anything under archive/, private/, or a *.db
that is a symlink. Stdlib only. A local model may call plan/build/verify; it cannot pass arbitrary SQL.
"""
import argparse
import glob
import hashlib
import json
import os
import re
import sqlite3
import sys
import time

def stem(path):
    """Group key: file name with the per-box / conflict suffixes removed."""
    raise NotImplementedError('TODO: implement')

def sha256(path):
    raise NotImplementedError('TODO: implement')

def discover(root):
    raise NotImplementedError('TODO: implement')

def ro(path):
    raise NotImplementedError('TODO: implement')

def quote_identifier(name):
    """Return one SQLite identifier, rejecting characters that can alter SQL."""
    raise NotImplementedError('TODO: implement')

def tables(con):
    raise NotImplementedError('TODO: implement')

def columns(con, table):
    raise NotImplementedError('TODO: implement')

def row_hash(values):
    raise NotImplementedError('TODO: implement')

def read_rows(path, table, cols):
    raise NotImplementedError('TODO: implement')

def plan(root):
    raise NotImplementedError('TODO: implement')

def build(root, out):
    raise NotImplementedError('TODO: implement')

def verify(out):
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
