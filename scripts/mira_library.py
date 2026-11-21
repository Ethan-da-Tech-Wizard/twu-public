# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Mira, Enki's deterministic offline-library steward.

Mira searches the existing local FTS library before research is proposed.  A
miss creates a bounded approval card only; this program never fetches, calls a
model, opens a browser, or starts a researcher.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import sys

def now():
    raise NotImplementedError('TODO: implement')

def clean_query(value):
    raise NotImplementedError('TODO: implement')

def search(db_path, query, limit=5):
    raise NotImplementedError('TODO: implement')

def load_requests(path):
    raise NotImplementedError('TODO: implement')

def save_requests(path, data):
    raise NotImplementedError('TODO: implement')

def request_id(question):
    raise NotImplementedError('TODO: implement')

def propose(path, question):
    raise NotImplementedError('TODO: implement')

def approve(path, ident, approver):
    raise NotImplementedError('TODO: implement')

def ask(args):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
