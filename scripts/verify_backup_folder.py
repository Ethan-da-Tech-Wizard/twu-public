# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Verify a TWU backup folder on ANY computer. Needs only Python 3 (no other tools, no internet, no repo).

A backup folder holds independent .zip parts plus SHA256SUMS.txt. This checks that:
  1. every file listed in SHA256SUMS.txt exists and has the exact checksum (nothing changed or got damaged in copying);
  2. every .zip part opens and every file inside decompresses with a correct CRC (the zip really works).

  python3 VERIFY_BACKUP.py <backup-folder>        verify one backup
  python3 VERIFY_BACKUP.py <TWU_backups-folder>   verify every backup of every machine under it
Exit code 0 = all good, 1 = something is wrong.
"""
import hashlib
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

def sha256_of(path, chunk=...):
    raise NotImplementedError('TODO: implement')

def verify_folder(folder, say=...):
    """Return {'ok': bool, 'problems': [...], 'parts': int, 'files': int}."""
    raise NotImplementedError('TODO: implement')

def test_split_archive(folder, say=...):
    """Join an older-style split archive (.z01, .z02 ... .zip) in a LOCAL temp folder and test every file inside it.
    The join must not write next to the source: on a FAT32 drive the joined file would hit the 4 GB limit (found by the Mac,
    2026-10-22), so zip is told where to put its temp file with -b. Returns a list of problems; [] means the archive works."""
    raise NotImplementedError('TODO: implement')

def find_backup_folders(path):
    raise NotImplementedError('TODO: implement')

def main(argv):
    raise NotImplementedError('TODO: implement')
