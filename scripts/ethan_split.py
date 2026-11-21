# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""ONE small entrypoint for the workspace split, built so a small model only has to follow a chain.

Every subcommand is a single step. Output is short plain text and always ends with a line `NEXT: <exact next command>`
(or `DONE.`), so the model copies that command and the chain finishes without planning. Wraps ethan_split_plan.py (the planner
stays the source of truth for classification and verification).

  python3 scripts/ethan_split.py status
  python3 scripts/ethan_split.py classify              # classify every file, write MANIFEST.json under the work folder
  python3 scripts/ethan_split.py classify PATH         # one path: PRIVATE, CODE or REVIEW (relative path, e.g. docs/guide.md)
  python3 scripts/ethan_split.py plan                  # counts and what would be copied
  python3 scripts/ethan_split.py copy-code             # COPY the CODE files into <work>/code_repo
  python3 scripts/ethan_split.py copy-vault            # COPY the PRIVATE files into <work>/private_vault
  python3 scripts/ethan_split.py verify                # run the planner's proofs on both copies
  python3 scripts/ethan_split.py report                # write <work>/SPLIT_REPORT.md with the three counts

Safety: reads the project, writes ONLY under the work folder (default /mnt/GameDrive/twu_scratch/split_work; tests and the
dogfood example_host set ETHAN_SPLIT_WORK together with ETHAN_SPLIT_ALLOW_ANY_DEST=1). Originals are never moved, changed or deleted;
there is no delete or move subcommand, and asking for one is refused with an explanation.
"""
from __future__ import annotations
import os
import sys
from collections import Counter
from pathlib import Path
import ethan_split_plan as sp

def project_root() -> Path:
    raise NotImplementedError('TODO: implement')

def work_dir() -> Path:
    raise NotImplementedError('TODO: implement')

def nxt(cmd: str | None) -> str:
    raise NotImplementedError('TODO: implement')

def manifest_path() -> Path:
    raise NotImplementedError('TODO: implement')

def load_manifest():
    raise NotImplementedError('TODO: implement')

def counts(m) -> Counter:
    raise NotImplementedError('TODO: implement')

def cmd_status(args) -> str:
    raise NotImplementedError('TODO: implement')

def cmd_classify(args) -> str:
    raise NotImplementedError('TODO: implement')

def need_manifest():
    raise NotImplementedError('TODO: implement')

def cmd_plan(args) -> str:
    raise NotImplementedError('TODO: implement')

def _copy(kind: str, dest: Path, nextcmd: str) -> str:
    raise NotImplementedError('TODO: implement')

def cmd_copy_code(args) -> str:
    raise NotImplementedError('TODO: implement')

def cmd_copy_vault(args) -> str:
    raise NotImplementedError('TODO: implement')

def cmd_verify(args) -> str:
    raise NotImplementedError('TODO: implement')

def cmd_report(args) -> str:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
