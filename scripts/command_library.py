# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""
PROGRAM:       command_library.py
PROGRAMMER:    Magi 10 (claude, example_host), MAGI_TODO 0cdbcc6a (Command Library 3: schema and indexer)
LAST MODIFIED: 2026-11-20
PURPOSE:       Per-computer, searchable database of every command OBSERVED on this computer plus the documentation we hold
               for it, stored IN FULL, with a coverage report that lists what is NOT documented.
               Spec: docs/COMMAND_LIBRARY_SPEC.md.

FULL TEXT RULE (Ethan, 2026-11-20): NO TEXT IS EVER CUT. Every manual page (all sections 1-9, n, l) and every text document of
the offline library is stored whole. A long document is split into ordered PASSAGES (for search ranking and display) but the
passages concatenate back to exactly the document text, and `show` reassembles the whole thing. The only things not stored are
markup and page chrome (HTML tags, scripts, styles, repeated navigation sidebars) which are not document text, and non-text
assets (images, fonts, JavaScript, CSS); both are COUNTED in the build record, never hidden.

WHAT IT STORES (SQLite FTS5, one file per computer: data/commands/hosts/<host>/library.sqlite3, ignored by Syncthing)
  sources       every source with license, url, sha256 of what was read, when
  commands      executables seen in PATH, shell builtins, our own project scripts (name, os, kind, path, package, summary)
  docs          one row per document (man page, cheat sheet, library page, project doc): metadata, char count, alias_of
  passages      the full text of every document, in order (doc_id, seq, text); passages_fts indexes ALL of it
  examples      example lines from cheat sheets
  ingest_state  per source file: size, mtime, sha256, characters in the source text, characters stored, status (makes builds resumable)
  coverage      the per-OS numbers (also written to data/commands/coverage.<host>.json for the OS alignment guard)
  options / subcommands / synopsis / doc_json   (schema 3) every flag of every man page with its FULL description, parsed by
                scripts/command_library_options.py; options_fts and subcommands_fts make them searchable ("follow symlinks" finds -L)
  best_doc      (schema 3) for every command, the best documentation row and why it won
  docs.os_list  (schema 3) the OS list of every document (arch, example_host, macos, generic, workspace); docs.os stays the single primary
                token ('any' = generic) for older readers; docs.dialect (gnu|bsd|posix) and docs.notice (verbatim license notice)
  Staged source corpora (data/commands/corpus/<source-id>/manifest.jsonl, vetted by scripts/command_library_packs.py) are ingested in
  FULL after each file's sha256 is checked against its manifest line; a mismatch is refused and listed, never ingested.

RULES THIS FILE KEEPS
  * Never runs any discovered program (no --help, no --version): commands are found by listing PATH directories and reading
    manuals as literal text (no roff renderer, no `man`, no shell, no `.so` beyond one same-root hop).
  * Builds are RESUMABLE and INCREMENTAL: a document whose size and mtime (or sha256) are unchanged is not read again. A run may
    be limited with --max-seconds / --max-pages (default: no limit); when a limit stops a run, it prints how many documents remain
    and the next run continues. Nothing is dropped: the receipt says complete=false until every document is ingested.
  * `verify-fulltext` re-decodes a random sample of 200 documents plus EVERY document above 100,000 characters straight from the
    source files (different decompression code path) and requires the stored text to be identical, and the totals must match:
    characters in sources == characters stored, truncated == 0.
  * Coverage = observed commands with at least one documentation row, divided by observed commands. `verify` recounts the
    PATH executables with an independent method and fails if the stored total differs.
  * No downloads. Package ownership: example_host uses ONE bounded `rpm -qa`; Arch reads /var/lib/pacman/local/*/files (no program run);
    macOS follows Homebrew Cellar symlinks (no program run). The only programs this tool ever runs are `rpm -qa` (example_host),
    `sw_vers -productVersion` and `pmset -g batt` (macOS), each bounded by a timeout. 2026-11-20 Magi 10: Arch and macOS support.
  * Readers always see a consistent database: writes commit in batches under WAL, and a finished build returns it to a plain file.

COMMANDS (all accept --root PATH for tests and --json)
  build           [--max-seconds N] [--max-pages N] [--sections all|1,5,...] [--no-packages] [--no-library] [--no-corpus]
  search          "plain words or a command" [--os OS] [--source ID] [--kind KIND] [--limit N]
  show            NAME [--os OS]            (every document for the name, in full)
  options         NAME [--os OS]            (every flag with its full description, subcommands, synopsis, see also)
  option-search   "plain words" [--os OS]    (search flag descriptions: "follow symlinks" finds -L / --dereference)
  diff            NAME OSA OSB              (GNU vs BSD flag table: only_a, only_b, same, different_meaning)
  sources         (per source: license, url, documents, characters)
  coverage        [--os OS]                 (prints the FULL undocumented list)
  status
  verify                                    (PATH recount)
  verify-fulltext [--sample N] [--seed N]   (stored text equals a fresh decode of the source, plus totals)

CHANGE HISTORY:
  2026-11-19  Magi 10  Created.
  2026-11-20  Magi 10  Removed every cut: the 12,000-character limit (1,120 manuals were cut), the section skips (2, 3, 4 and the
                       rest: 9,000+ pages), the 1 MiB manual read limit, the 2,000/900/1,200-character alias and builtin slices and
                       the references-only library. Full-text storage in passages, resumable incremental build, library ingest,
                       verify-fulltext, schema version 2.
  2026-11-20  Magi 10  Schema 3 (MAGI_TODO 0cdbcc6a / 5734d10d): staged source corpora ingested in full with sha256 checks, options /
                       subcommands / synopsis tables from command_library_options.py, os_list + dialect + notice per document, BSD
                       (mdoc) pages rendered to text with their macros expanded (the man-macro cleaner drops mdoc text), best_doc,
                       coverage split into installed-command coverage and library-only commands, options/diff/option-search/sources.
"""
from __future__ import annotations
import argparse
import bz2
import fcntl
import gzip
import hashlib
import html as _html
import json
import lzma
import os
import random
import platform
import re
import socket
import sqlite3
import stat
import subprocess
import sys
import time
import zlib
from pathlib import Path
import command_library_options as clo

def man_roots_for(osn):
    """Manual roots for an OS id (example_host/arch share the Linux roots; macOS adds Homebrew's)."""
    raise NotImplementedError('TODO: implement')

def now_iso():
    raise NotImplementedError('TODO: implement')

def os_id():
    """Short OS id: 'example_host', 'arch', 'macos', or the /etc/os-release ID (never guessed beyond that)."""
    raise NotImplementedError('TODO: implement')

def os_version():
    """OS version string for the receipt. Linux: /etc/os-release (VERSION_ID or BUILD_ID or PRETTY_NAME). macOS: ONE bounded
    `sw_vers -productVersion`. Never raises; '' when unknown."""
    raise NotImplementedError('TODO: implement')

def db_path(root, host=None):
    raise NotImplementedError('TODO: implement')

def receipt_path(root, host=None):
    raise NotImplementedError('TODO: implement')

def sha256_bytes(data):
    raise NotImplementedError('TODO: implement')

def _path_dirs(env_path=None):
    """Absolute PATH directories, in order, de-duplicated by real path. Relative entries are reported, not followed."""
    raise NotImplementedError('TODO: implement')

def scan_path(env_path=None):
    """Executables in PATH. Returns (commands, stats). commands: name -> path of the FIRST executable found (shell order).

    Method A (used by build): os.scandir + entry.stat(follow_symlinks=True) + S_ISREG + any execute bit.
    """
    raise NotImplementedError('TODO: implement')

def count_path_independent(env_path=None):
    """Method B (used by verify): os.listdir + os.stat + mode bits. Same DEFINITION as scan_path (a regular file with any
    execute bit, symlinks followed) but a different code path (no scandir/DirEntry), so a bug in one shows up as a mismatch."""
    raise NotImplementedError('TODO: implement')

def rpm_owners(paths, max_seconds=60):
    """{path: package} from ONE `rpm -qa` call (example_host/RHEL). Returns (map, note). Paths are matched exactly, then by real path.
    `%{=NAME}` repeats the package name for every file (a plain NAME with the FILENAMES array is an rpm 6 format error)."""
    raise NotImplementedError('TODO: implement')

def _want_map(paths):
    """{lookup path: original path}: exact, real path, and real parent + name (so /bin/ls finds usr/bin/ls on merged-usr systems)."""
    raise NotImplementedError('TODO: implement')

def pacman_owners(paths, db_dir=None, max_seconds=60):
    """{path: package} on Arch by READING /var/lib/pacman/local/<pkg>-<ver>-<rel>/files (no program is run, no sudo).
    The `files` list holds paths relative to / after a %FILES% header. Bounded by max_seconds. Returns (map, note)."""
    raise NotImplementedError('TODO: implement')

def brew_owners(paths):
    """{path: formula} on macOS by following Homebrew symlinks into .../Cellar/<formula>/<version>/... (no program is run, no network).
    Apple system tools (/usr/bin etc.) have no package-manager owner here and are left out, which the note says."""
    raise NotImplementedError('TODO: implement')

def owners_for(osn, paths, max_seconds=60):
    """Package owner map for this OS. Returns (map, note)."""
    raise NotImplementedError('TODO: implement')

def _safe_regular(path):
    """Root-owned, regular, not group/world-writable (same rule as scripts/command_catalog.py), unless running as a test."""
    raise NotImplementedError('TODO: implement')

def read_manual_bytes(path, limit=...):
    """Return (text or None, reason). Decodes .gz/.bz2/.xz/.zst COMPLETELY (streaming, no 1 MiB cut); plain files as is.
    A document larger than `limit` decompressed bytes is NOT cut: it returns (None, 'too_large') so it is counted and listed.
    This is the BUILD decode path (zlib/bz2/lzma incremental decompressors); verify-fulltext uses a different one."""
    raise NotImplementedError('TODO: implement')

def read_text_independent(path):
    """A DIFFERENT decode path (gzip.open / bz2.open / lzma.open / zstd.decompress, whole-file) used only by verify-fulltext, so a
    bug in read_manual_bytes cannot hide itself. Returns text or None."""
    raise NotImplementedError('TODO: implement')

def html_to_text(raw):
    """Return (text, title, chrome_removed). Removes markup and page chrome (scripts, styles, svg, nav sidebars, comments), which
    are not document text; keeps EVERY word of the page content, with <pre> blocks (code) kept exactly, whitespace included.
    chrome_removed is the number of removed non-text blocks (counted in the build record)."""
    raise NotImplementedError('TODO: implement')

def _unescape(s):
    raise NotImplementedError('TODO: implement')

def roff_to_text(raw):
    """Very small literal roff cleaner: drops comments and macro definitions, keeps text and section titles.
    Returns (text, summary, names). summary/names come from the NAME section ('ls - list directory contents')."""
    raise NotImplementedError('TODO: implement')

def man_files(roots, sections, stats):
    """List (path, name, section) for EVERY manual file in man<N>/ directories. `sections` is 'all' (default) or a comma list of
    base section digits; sections NOT wanted are counted in stats['skipped_sections'] (only when the caller limits them on purpose).
    Names that do not look like manual files are listed in stats['skipped_names'] (all of them, never just a count)."""
    raise NotImplementedError('TODO: implement')

def split_passages(text, limit=...):
    """Split text into ordered passages of about `limit` characters, on line boundaries (a single longer line is split by characters).
    LOSSLESS: "".join(split_passages(t)) == t for every t. Passages exist for search ranking and display only."""
    raise NotImplementedError('TODO: implement')

def _os_primary(os_list, osn):
    """The single primary OS token kept in docs.os for older readers: this computer's OS when the document applies to it,
    otherwise the first listed OS; a purely generic document is 'any' (the label every earlier reader already uses)."""
    raise NotImplementedError('TODO: implement')

def insert_document(cur, command, osn, source_id, kind, title, text, url, lic, section, ref, state_key, alias_of=None, derived=0, os_list=None, dialect=None, notice=None):
    """Store ONE document completely: a docs row plus its passages (and their FTS rows). Returns (doc_id, chars_stored).
    `os_list` is the list of OS ids the document applies to (arch, example_host, macos, generic, workspace); `osn` stays the primary token."""
    raise NotImplementedError('TODO: implement')

def dialect_of_os(osn):
    """Tool dialect of an OS: macOS ships BSD userland, every Linux here ships GNU userland."""
    raise NotImplementedError('TODO: implement')

def store_structure(cur, doc_id, command, os_list, dialect, source_id, section, ex):
    """Persist command_library_options.extract() output for one man page: every option with its FULL description (searchable),
    subcommands, synopsis lines, man EXAMPLES blocks, and the whole structure as JSON for the dashboard. Nothing is shortened."""
    raise NotImplementedError('TODO: implement')

def mdoc_to_text(text, name=...):
    """Render a BSD mdoc manual page to plain text with every macro EXPANDED (.Nm, .Fl, .Ar, .Xr ...). The man-macro cleaner
    (roff_to_text) drops mdoc macro arguments, which loses words such as the command name and every flag, so BSD pages use this.
    Structure: section titles, sub-headings, paragraphs, and each list item as its tag line followed by its indented paragraphs."""
    raise NotImplementedError('TODO: implement')

def is_mdoc(text):
    """True for BSD mdoc source (it always carries a .Dd date macro)."""
    raise NotImplementedError('TODO: implement')

def page_body(text, name, section):
    """(body, summary, names, format) of one manual page source: mdoc pages are rendered with macros expanded, man pages cleaned."""
    raise NotImplementedError('TODO: implement')

def delete_state(cur, key):
    """Remove every document (and its passages and FTS rows) that came from state key `key`, and the state row itself."""
    raise NotImplementedError('TODO: implement')

def resolve_manual_text(path, roots, reader):
    """Read a manual file with `reader(path)->text|None` and follow ONE `.so` redirect stub (same-root). Returns (text, why, followed)."""
    raise NotImplementedError('TODO: implement')

def _build_reader(path):
    raise NotImplementedError('TODO: implement')

def ingest_man(cur, path, name, sec, roots, osn, skipped):
    """Ingest one installed manual page IN FULL. Returns (chars_src, chars_stored, docs, status, note)."""
    raise NotImplementedError('TODO: implement')

def lib_text(rel, text):
    """Clean one library file's text. Returns (body, title, chrome_removed, command)."""
    raise NotImplementedError('TODO: implement')

def ingest_lib(cur, library, rel, osn, catalog, skipped):
    """Ingest one library text file IN FULL. Returns (chars_src, chars_stored, docs, status, note)."""
    raise NotImplementedError('TODO: implement')

def corpus_dialect(source_id, rel):
    """gnu | bsd | posix | None for a corpus document, from its source (and for tldr, its platform folder)."""
    raise NotImplementedError('TODO: implement')

def man_name_section(rel):
    """('ls', '1p') from a corpus path such as .../man1p/ls.1p ; names that contain dots keep them (only the LAST suffix is the section)."""
    raise NotImplementedError('TODO: implement')

def parse_tldr(text):
    """(summary, [example text]) from a tldr page: '# name', '> description', then '- what it does:' followed by a `command` line."""
    raise NotImplementedError('TODO: implement')

def read_corpus_file(path):
    """(bytes, why). Refuses symlinks and non-regular files (the corpus is untrusted data until its hash is checked)."""
    raise NotImplementedError('TODO: implement')

def corpus_body(rec, text):
    """The document text stored for one corpus file: man pages (roff or mdoc) go through page_body, everything else is the text as is.
    Returns (body, summary, names, command, section, fmt)."""
    raise NotImplementedError('TODO: implement')

def ingest_corpus(cur, croot, rec, osn, skipped):
    """Ingest ONE staged corpus document IN FULL after checking its sha256 against the manifest line. Returns the usual
    (chars_src, chars_stored, docs, status, note) tuple."""
    raise NotImplementedError('TODO: implement')

def passages_chars(con, where=...):
    """Characters in the passages table, counted in PYTHON (SQLite length() stops at an embedded NUL character, which some source
    documents legitimately contain, for example git object headers and GNU info markers). `where` filters on alias `d` (docs)."""
    raise NotImplementedError('TODO: implement')

def doc_text(con, doc_id):
    """The WHOLE stored text of a document: its passages concatenated in order."""
    raise NotImplementedError('TODO: implement')

def _migrate_columns(con):
    """Add the schema-3 columns to tables created by schema 2 (CREATE TABLE IF NOT EXISTS cannot add columns), then backfill them:
    os_list from the single os token ('any' = generic), dialect from the OS for installed manuals, os_list on cheat examples."""
    raise NotImplementedError('TODO: implement')

def _init_db(final):
    """Open (creating) the per-computer database. A schema-2 database is MIGRATED in place (columns and tables added, nothing lost);
    any other version is replaced by a fresh full build."""
    raise NotImplementedError('TODO: implement')

def build(root=..., max_seconds=0.0, max_pages=0, sections=..., packages=True, env_path=None, man_roots=None, host=None, out=..., library=True, library_root=None, corpus=True, corpus_root=None, sources_file=None):
    """Build or CONTINUE this computer's library. Returns the coverage dict that is also written as the receipt.
    max_seconds / max_pages = 0 means NO limit. A limit stops the run cleanly; the receipt then says complete=false and how many
    documents remain; the next run continues where this one stopped."""
    raise NotImplementedError('TODO: implement')

def status_path(root, host=None):
    raise NotImplementedError('TODO: implement')

def corpus_digest(root):
    """Digest of what the library is built FROM: data/commands/sources.json plus every corpus manifest.jsonl (their file hashes).
    A change means new or changed source documents, so the library must be rebuilt."""
    raise NotImplementedError('TODO: implement')

def power_ok():
    """(ok, why). Refuses a build when load is high or the battery is low and unplugged. Unknown means proceed (never blocks forever).
    Linux reads /sys/class/power_supply; macOS runs ONE bounded `pmset -g batt`."""
    raise NotImplementedError('TODO: implement')

def _atomic_json(path, data):
    raise NotImplementedError('TODO: implement')

def _age_seconds(iso):
    raise NotImplementedError('TODO: implement')

def auto_build(root=..., max_seconds=240.0, force=False, host=None, out=...):
    """The stale sweep's step: build or CONTINUE this computer's library when it is missing, incomplete, older than 24 h or the
    corpus changed; otherwise do nothing. Bounded by max_seconds, niced, refused while the computer is busy or on a low battery.
    ALWAYS writes data/commands/library_status.<host>.json (atomically) so the cockpit can show the state and its age.
    Returns the status dict."""
    raise NotImplementedError('TODO: implement')

def _open(root, host=None):
    raise NotImplementedError('TODO: implement')

def _fts_query(text, any_term=False):
    raise NotImplementedError('TODO: implement')

def _option_hits(con, text, os_filter, limit):
    """Flags whose name or FULL description matches the words (e.g. 'follow symlinks' finds -L / --dereference)."""
    raise NotImplementedError('TODO: implement')

def search(root, text, os_filter=None, source=None, kind=None, limit=20, host=None):
    """Search ALL stored text (every passage of every document). Results are one row per document (its best passage)."""
    raise NotImplementedError('TODO: implement')

def show(root, name, os_filter=None, host=None):
    """Everything known about NAME, every document IN FULL (reassembled from its passages). An alias row also carries the whole
    target page as `target_body`."""
    raise NotImplementedError('TODO: implement')

def _pick_man_doc(con, name, os_id):
    """The man page row to compare for NAME on OS: this computer's installed page first, then a corpus page whose os_list names the OS."""
    raise NotImplementedError('TODO: implement')

def options_for(root, name, os_filter=None, host=None):
    """Every flag of NAME with its FULL description, plus subcommands, synopsis, examples and see-also, one entry per man page."""
    raise NotImplementedError('TODO: implement')

def diff_command(root, name, os_a, os_b, host=None):
    """GNU vs BSD (or any two OS) flag table for NAME: {labels, only_a, only_b, same, different_meaning} with both full descriptions.
    Both sides must have a stored man page; a missing side is reported, never guessed."""
    raise NotImplementedError('TODO: implement')

def option_search(root, text, os_filter=None, limit=20, host=None):
    raise NotImplementedError('TODO: implement')

def sources_report(root, host=None):
    """Per source: license, url, version, hash, documents and characters (the provenance page of the dashboard)."""
    raise NotImplementedError('TODO: implement')

def coverage_report(root, os_filter=None, host=None):
    raise NotImplementedError('TODO: implement')

def verify(root, host=None, env_path=None):
    """Independent recount of PATH executables vs the stored total. Returns (ok, message)."""
    raise NotImplementedError('TODO: implement')

def verify_fulltext(root, sample=200, seed=None, host=None, man_roots=None, library_root=None, big_chars=100000):
    """Prove nothing was cut. For a random sample of `sample` documents PLUS every document above `big_chars` characters, decode the
    SOURCE FILE again with a different decompression path (gzip/bz2/lzma modules) and require sha256(stored text) == sha256(fresh
    text). Also require, over ALL ingested documents, characters in sources == characters stored == characters in the passages table.
    Returns a dict; result['ok'] is True only when there are no mismatches and no truncation."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
