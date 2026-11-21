# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""
generate_database_guide.py - Comprehensive SQLite Database Catalog & Explorer Generator.

Audits every SQLite database in TWU_LLC, extracts schema DDLs, column definitions,
row counts, and writes an interactive, high-contrast HTML guide at:
    data/lessons/library/databases/index.html
and refreshes data/dashboard/discovered_databases.json.
"""
import os
import sys
import json
import sqlite3
import html
import time
from pathlib import Path

def inspect_db_full(rel_path):
    """Safely extracts all tables, columns, CREATE SQL, and row counts in read-only mode."""
    raise NotImplementedError('TODO: implement')

def format_bytes(n):
    raise NotImplementedError('TODO: implement')

def generate_catalog():
    raise NotImplementedError('TODO: implement')
