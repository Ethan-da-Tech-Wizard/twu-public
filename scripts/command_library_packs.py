# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""
PROGRAM:       command_library_packs.py
PROGRAMMER:    Magi 10 (claude, example_host), MAGI_TODO 32299ef8 (Command Library source packs)
LAST MODIFIED: 2026-11-20
PURPOSE:       Fetch, VET and STAGE free/open reference material into the Command Library corpus.

WHY: Ethan wants free and open books, man pages and datasets inside the command index, in FULL (nothing cut). Downloads are
untrusted data, so every source goes through the same protocol:

  1. fetch   : into its OWN NEW EMPTY scratch directory (never the workspace), by `git clone --depth 1` with hooks disabled
               or by curl with a size cap and a generic client name. No personal data is ever sent. Nothing downloaded is executed.
  2. vet     : the source's LICENSE file must contain the marker text the survey expects (data/commands/sources_survey_20261119.json).
               A mismatch REFUSES the source (it becomes LINK ONLY in sources.json). Archives are read with tarfile/zipfile only,
               rejecting absolute paths, `..`, links and device nodes, and any file or total over the size caps.
  3. stage   : copy the document text in FULL (HTML is converted to text by stripping markup only: headings, lists and code blocks
               are kept) to data/commands/corpus/<source-id>/files/..., save license texts to data/commands/licenses/<id>.txt, and write
               data/commands/corpus/<source-id>/manifest.jsonl with sha256 of every staged file.

MANIFEST LINE (one JSON object per line, this is the hook the indexer reads):
  {"id": "<source>/<relative path>", "source": "<source-id>", "path": "<relative to data/commands/corpus>", "sha256": "...",
   "title": "...", "os": ["arch","example_host","macos","generic"], "kind": "man|tldr|cheat|book|wiki|dataset|tip",
   "license": "<SPDX>", "url": "...", "bytes": N, "notice": "<optional: copyright/invariant-section notice, verbatim>"}

Run (from the workspace root):  python3 scripts/command_library_packs.py stage tldr   |  list  |  verify
Only an explicit command runs a download: no timer, no daemon (docs/FLEET_COMMAND_REFERENCE.md rule: no automatic download).

CHANGE HISTORY:
  2026-11-20  Magi 10  Created.
"""
from __future__ import annotations
import argparse
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import time
import zipfile
from html.parser import HTMLParser
from pathlib import Path

class VetError(Exception):
    """A source or archive failed a safety or license check; it must NOT be staged."""

def sha256_file(path):
    raise NotImplementedError('TODO: implement')

def sha256_bytes(data):
    raise NotImplementedError('TODO: implement')

def new_scratch(source_id):
    """A NEW EMPTY scratch directory for one download (an existing non-empty one is cleared first, never reused)."""
    raise NotImplementedError('TODO: implement')

def run(cmd, cwd=None, timeout=1800):
    """Run a fixed argv (never a shell). Git hooks are disabled and terminal prompts refused."""
    raise NotImplementedError('TODO: implement')

def git_clone(url, dest, sparse=None):
    """Shallow clone with hooks disabled; optional sparse checkout of the listed paths (blobless to stay small)."""
    raise NotImplementedError('TODO: implement')

def curl_download(url, dest_file):
    """Download one URL with a size cap and a generic client name; returns sha256 of the artifact."""
    raise NotImplementedError('TODO: implement')

def _bad_name(name):
    raise NotImplementedError('TODO: implement')

def safe_extract_tar(archive, dest, max_total=..., max_file=..., links=..., skipped=None, select=None):
    """Extract a tar(.gz/.xz/.bz2) into dest, refusing path traversal, absolute names, devices and oversize.
    links="refuse" (default) rejects the whole archive if it holds a symlink/hardlink; links="skip" never creates the link and
    records its name in the `skipped` list (a link is never followed or written, so it cannot escape).
    `select(name)->bool`, if given, limits which regular files are WRITTEN (every member is still validated first).
    Returns the list of extracted regular-file paths (relative)."""
    raise NotImplementedError('TODO: implement')

def safe_extract_zip(archive, dest, max_total=..., max_file=...):
    """Same rules as safe_extract_tar for zip archives (symlinks are detected from the external attributes)."""
    raise NotImplementedError('TODO: implement')

def tree_size(path):
    """Total bytes of regular files under path (symlinks are not followed and not counted)."""
    raise NotImplementedError('TODO: implement')

def vet_license(license_text, markers):
    """True if EVERY marker (case-insensitive, whitespace-normalised) appears in the license text; otherwise VetError."""
    raise NotImplementedError('TODO: implement')

class _Text(HTMLParser):
    """Convert HTML to plain text keeping headings (# marks), list bullets, <pre>/<code> blocks and link targets in full."""

    def __init__(self):
        raise NotImplementedError('TODO: implement')

    def handle_starttag(self, tag, attrs):
        raise NotImplementedError('TODO: implement')

    def handle_endtag(self, tag):
        raise NotImplementedError('TODO: implement')

    def handle_data(self, data):
        raise NotImplementedError('TODO: implement')

def html_to_text(raw):
    """Return the full text of an HTML document with markup removed (no section is dropped)."""
    raise NotImplementedError('TODO: implement')

def stage_files(source_id, items, license_spdx, url, notice=..., kind=..., os_tags=...):
    """Copy staged documents into the corpus and write manifest.jsonl.
    items: iterable of (relative_name, bytes_or_Path, title, os_tags|None, kind|None). Returns (count, total_bytes)."""
    raise NotImplementedError('TODO: implement')

def save_license(source_id, text, header=...):
    """Keep the license text locally: data/commands/licenses/<source-id>.txt (verbatim, with a provenance header)."""
    raise NotImplementedError('TODO: implement')

def read_text(path):
    raise NotImplementedError('TODO: implement')

def verify_manifest(source_id):
    """Recompute sha256 of every staged file and compare with its manifest line. Returns (ok_count, problems)."""
    raise NotImplementedError('TODO: implement')

def _record(source_id, **kw):
    raise NotImplementedError('TODO: implement')

def src_tldr():
    raise NotImplementedError('TODO: implement')

def src_cheat():
    raise NotImplementedError('TODO: implement')

def _fetch_tar(sid, url, suffix, links=...):
    raise NotImplementedError('TODO: implement')

def src_manpages():
    raise NotImplementedError('TODO: implement')

def src_posix():
    raise NotImplementedError('TODO: implement')

def _gnu_notice(text):
    """Extract the verbatim copyright/permission paragraph (the part that states Invariant Sections) from a GNU manual's text."""
    raise NotImplementedError('TODO: implement')

def _latest_gnu_tarball(project):
    """Pick the newest release tarball (tar.xz preferred, else tar.gz) for a GNU project from the ftp.gnu.org listing."""
    raise NotImplementedError('TODO: implement')

def src_gnu(name):
    raise NotImplementedError('TODO: implement')

def src_aoc():
    raise NotImplementedError('TODO: implement')

def src_homebrew():
    raise NotImplementedError('TODO: implement')

def src_abs():
    raise NotImplementedError('TODO: implement')

def src_nl2bash():
    raise NotImplementedError('TODO: implement')

def src_freebsd():
    raise NotImplementedError('TODO: implement')

def src_arch_wiki_lite():
    raise NotImplementedError('TODO: implement')

def _git_head(d):
    raise NotImplementedError('TODO: implement')

def build_sources_json():
    """Write data/commands/sources.json: one verified row per survey row with the staging decision, license evidence and hashes."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
