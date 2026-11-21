# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""
PROGRAM:       command_library_query.py
PROGRAMMER:    Magi 10 (claude, example_host)
LAST MODIFIED: 2026-11-20
PURPOSE:       The QUESTION layer of the Command Library. It turns plain words ("find files modified in the last day",
               "who is using this port", "install a package") into a ranked list of commands, using the per-computer
               SQLite library built by scripts/command_library.py. Read-only: it opens the database with mode=ro and never
               writes. It does NOT import command_library.py, so it keeps working while that file is being changed.

HOW A QUESTION IS ANSWERED (every step is a separate, inspectable signal; `why` lists the signals that put a command on top)
  1. INTENTS  data/commands/intents.json: curated plain-language task phrases -> best commands (per OS where the answer
              differs: dnf on example_host, pacman on Arch, brew on macOS). Strongest signal.
  2. NAME     a word in the question that IS a command on this computer ("awk columns") ranks that command high; for a
              one- or two-word query it ranks first.
  3. SUMMARY  full-text match against each command's one-line description ("terminate a process"), the tldr-style layer.
  4. DOCS     full-text match against man pages and cheat sheets with field boosts: command name > NAME line/title > body.
  5. EXAMPLES full-text match against cheat sheet example lines.
  6. TIPS     data/commands/tips.json hand-written idioms and "secrets"; their commands count as evidence and the tips are returned.
  7. PRIOR    a small bonus for core commands named in the intents, so a standard tool beats an obscure one on equal evidence.
  Signals are combined by weighted reciprocal-rank fusion (score += weight / (K + rank)).

OS AWARENESS
  A computer's database only contains that OS's commands, so results are always runnable here. `equivalents` in search()
  shows what the same task is called on the other registered OSes (from the intents' per-OS lists) without claiming those
  tools exist on this computer.

NEVER CUT OR SUMMARISE
  Result rows carry full one-line descriptions and references (doc ids) to the full documents; the complete text of any
  document is returned by show_doc() in full. Nothing here truncates documentation text.

DID YOU MEAN
  A word that looks like a command name but is not one gets edit-distance suggestions (difflib) from this computer's names.

PUBLIC API
  rank(root, text, os_id=None, limit=30)   -> list of {command, score, why[], summary, kind}
  search(root, text, os_id=None, limit=20) -> {query, os, did_you_mean[], results[], tips[], equivalents{}}
  show_doc(root, doc_id)                   -> the complete stored document row, text uncut
  CLI: python3 scripts/command_library_query.py "plain words" [--os example_host] [--limit 10] [--json]

CHANGE HISTORY:
  2026-11-20  Magi 10  Created (MAGI_TODO cca40004).
"""
from __future__ import annotations
import argparse
import difflib
import glob
import json
import re
import socket
import sqlite3
import sys
from collections import defaultdict
from functools import lru_cache
from pathlib import Path

def stem(w):
    """A tiny English stemmer: enough to make 'files'/'file', 'modified'/'modify', 'listening'/'listen' compare equal.
    Both sides of every comparison go through it, so it only has to be consistent, not linguistically perfect."""
    raise NotImplementedError('TODO: implement')

def tokens(text):
    """Lower-case words, keeping dashes/dots/plus that appear inside command names (ssh-keygen, mkfs.ext4, g++)."""
    raise NotImplementedError('TODO: implement')

def spec_matches(spec, toks, stems):
    """spec is 'a|b*|c': true when any query word equals a (or its stem), or starts with b."""
    raise NotImplementedError('TODO: implement')

def _json(path, mtime):
    raise NotImplementedError('TODO: implement')

def load_json(path):
    raise NotImplementedError('TODO: implement')

def open_db(root, host=None):
    """This computer's library, opened READ-ONLY. Path rule matches command_library.py: data/commands/hosts/<host>/."""
    raise NotImplementedError('TODO: implement')

def detect_os(con):
    """The OS whose commands this database holds (the most common value other than the internal 'workspace')."""
    raise NotImplementedError('TODO: implement')

def fts_terms(text):
    """Content words for full-text search, stop words removed, de-duplicated, quoted for FTS5."""
    raise NotImplementedError('TODO: implement')

def _has_table(con, name):
    raise NotImplementedError('TODO: implement')

def _doc_rows(con, match, os_id, limit=120):
    """Ranked (command,) rows from the full-text index of documents: passages_fts (schema v2) or docs_fts (schema v1).
    Man pages and cheat sheets rank; books count too but only as a fallback signal through the same query."""
    raise NotImplementedError('TODO: implement')

def synonym_map():
    """word -> set of its synonym-group mates (both directions), from intents.json 'synonym_groups'. Lets 'wipe', 'erase' and
    'get rid of' all reach an intent written with 'delete'."""
    raise NotImplementedError('TODO: implement')

def expanded_tokens(text):
    """The question's words plus their synonyms (stems too). Used for INTENT matching only, never for full-text search."""
    raise NotImplementedError('TODO: implement')

def intent_hits(text, os_id, intents):
    """Yield (intent, ordered command list, specificity, literal) for every intent whose words all appear in the question.
    The question's synonyms count as its words (see expanded_tokens), but a match that needs a synonym is flagged
    literal=False so rank() can weigh it less (2026-11-20: 'copy' -> synonym 'clone' made the git vocabulary intent
    outrank the clipboard tools for 'copy text to the clipboard')."""
    raise NotImplementedError('TODO: implement')

def _add(pool, name, amount, why):
    raise NotImplementedError('TODO: implement')

def rank(root, text, os_id=None, limit=30, host=None, con=None):
    """Return the ranked commands for a plain-language question (see the module docstring for the signals)."""
    raise NotImplementedError('TODO: implement')

def match_tips(text, os_id, limit=5):
    """Score tips by how many of the question's stems appear in a tip's title, tags and text (title and tags count double)."""
    raise NotImplementedError('TODO: implement')

def suggest(text, names, n=3):
    """Edit-distance suggestions for a lone word that is not a known command name."""
    raise NotImplementedError('TODO: implement')

def known_commands(root, os_id):
    """Names of commands that really exist (or are documented) for an OS, from the staged corpora plus the curated extras.
    Cheat sheets are NOT evidence: they are platform-unspecified (a Linux-only `ss` cheat made `ss` look like a macOS command).

    2026-11-20 Magi 10: used to validate every cross-OS equivalent. macOS: tldr osx + common pages, FreeBSD man pages, and
    data/commands/os_known_extra.json (real macOS commands with no page in the corpora). Linux (arch/example_host): tldr linux + common,
    Linux/POSIX man pages, the extras, and for example_host this computer's own commands table. Cached per (root, os)."""
    raise NotImplementedError('TODO: implement')

def equivalents_for(root, text, os_id, top_commands):
    """The same job on the OTHER operating systems: {os: [commands]}.

    2026-11-20 Magi 10 fix. Before: every intent that matched the question (after synonym expansion) contributed its `os` list,
    so 'kill a process using a port' (kill -> halt via the stop/kill synonym group) matched the power intent and listed
    shutdown/reboot/pmset/halt for macOS. Now: (1) an intent only counts if one of its own commands is among the top
    EQ_TOP_N answers for this question, (2) its list for another OS is its explicit `os` entry or else its general command
    list, and (3) every name must be a real command on that OS (known_commands), so nothing invented or unrelated appears."""
    raise NotImplementedError('TODO: implement')

def search(root, text, os_id=None, limit=20, host=None):
    """The full answer used by the dashboard and CLI: ranked commands, doc references, tips and other-OS equivalents."""
    raise NotImplementedError('TODO: implement')

def show_doc(root, doc_id, host=None):
    """One stored document in FULL (nothing cut). Schema v2 keeps the text as ordered passages, which are joined here;
    schema v1 keeps it in docs.body. Returns None when the id does not exist."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
