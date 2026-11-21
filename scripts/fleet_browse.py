# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Read-only workspace file browser, run on the box being browsed through the paired fleet exec path.

  python3 -B scripts/fleet_browse.py list  RELATIVE_DIR     (empty string = workspace root)
  python3 -B scripts/fleet_browse.py fetch RELATIVE_FILE

Security model (fail closed, no writes of any kind):
  * The only root is the workspace this script lives in. Paths are RELATIVE; absolute paths, "..", ".",
    backslashes, NUL, "%" (encoded traversal) and over-long paths are refused before the disk is touched.
  * Each component is opened with O_NOFOLLOW relative to the parent directory descriptor, so ANY symlink on
    the way (even one that points inside the workspace) is refused and a swap race cannot escape the root.
  * Dotfiles/dot-directories, private/ and similar folders, and secret-looking names (home_secret_scan.KEYNAME
    plus name words) are refused and not listed. Fetched text is also scanned with the repo's own
    secret_scan/home_secret_scan rules; a hit refuses the whole file (nothing is partially shown).
  * fetch: regular files only, <= MAX_FETCH bytes, valid UTF-8 text without NUL (binary is refused).
  * list: at most MAX_ENTRIES entries.
Output is exactly one JSON object on stdout. Nothing here opens a file for writing or runs a program.
"""
import json
import os
import re
import stat
import sys
from pathlib import Path

def refuse(code):
    raise NotImplementedError('TODO: implement')

def split_path(rel):
    """Return validated components for a relative path, or None."""
    raise NotImplementedError('TODO: implement')

def secret_name(name):
    """True for dotfiles, denied folders and names the repo's secret rules flag. Reuses home_secret_scan.KEYNAME."""
    raise NotImplementedError('TODO: implement')

def in_allowed_area(parts):
    """True when the path (list of components) lies inside a browsable area; [] (the root) is allowed for listing."""
    raise NotImplementedError('TODO: implement')

def area_entry_ok(parts, name):
    """True when listing directory `parts` may show the child `name` (hides non-allowlisted children at root and data/)."""
    raise NotImplementedError('TODO: implement')

def secret_text(text):
    raise NotImplementedError('TODO: implement')

def open_dir(parts):
    """Walk parts under ROOT without following any symlink; returns an fd or raises OSError/ValueError."""
    raise NotImplementedError('TODO: implement')

def kind_of(mode):
    raise NotImplementedError('TODO: implement')

def do_list(rel):
    raise NotImplementedError('TODO: implement')

def do_fetch(rel):
    raise NotImplementedError('TODO: implement')

def run(op, rel):
    raise NotImplementedError('TODO: implement')

def main(argv):
    raise NotImplementedError('TODO: implement')
