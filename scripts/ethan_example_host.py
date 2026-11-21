# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Throwaway git example_host for visible Ethan CLI runs, so the shared workspace repo is never touched.

The Ethan CLI refuses to start unless its repo is clean, local-only and on main; the shared workspace is dirtied by other
agents all day, which used to force automation to commit/switch/merge in Ethan's own repo. A example_host removes that coupling:

  <home>/<id>/                 a fresh `git init -b main` repo, no remote, one baseline commit
    scripts/ethan, scripts/ethan_git_guard.py   REAL COPIES (they derive their repo root from their own location, so the
                                                CLI's start gate checks the example_host, not the shared repo)
    scripts/<everything else>                   symlinks into the workspace
    <every other top-level workspace entry>     symlinks (Cannon, data, business, apps, MAGI_0, private, GEMINI.md, ...)
    work/                                       the task's work dir (real files)
  .git/info/exclude lists every symlink name and work/, so `git status --porcelain --untracked-files=all` stays empty.

<home> defaults to ~/.cache/ethan-example_hostes (override: ETHAN_example_host_HOME); it must be outside the workspace so Syncthing
never syncs it. Receipts, logs and data written through the symlinks still land in the real workspace data dir.
Every git call here runs with cwd == the example_host root and refuses to run in the source repo. Nothing here talks to the
model server.

  ethan_example_host.py build [--keep]     build one, run the gate in it, print the root (removed unless --keep)
  ethan_example_host.py gate ROOT          run `./scripts/ethan git status` inside a example_host (read-only, no model request)
  ethan_example_host.py prune [--hours 6]  remove example_hostes older than that (only dirs carrying the example_host marker)
"""
from __future__ import annotations
import argparse, json, os, shutil, subprocess, sys, time, uuid
from pathlib import Path

class example_hostError(RuntimeError):
    pass

def example_host_home() -> Path:
    raise NotImplementedError('TODO: implement')

def _clean_env() -> dict:
    raise NotImplementedError('TODO: implement')

def _inside(child: Path, parent: Path) -> bool:
    raise NotImplementedError('TODO: implement')

def run_git(cwd, *args, check: bool=True, forbid=None):
    """(returncode, output). Refuses to run in `forbid` (the source repo): the single choke point for example_host git calls."""
    raise NotImplementedError('TODO: implement')

class example_host:

    def __init__(self, root: Path, source: Path, links: list):
        raise NotImplementedError('TODO: implement')

    @property
    def work(self) -> Path:
        raise NotImplementedError('TODO: implement')

    def git(self, *args, check: bool=False):
        raise NotImplementedError('TODO: implement')

    def dirty(self) -> str:
        raise NotImplementedError('TODO: implement')

    def branch(self) -> str:
        raise NotImplementedError('TODO: implement')

    def heal(self) -> bool:
        """example_host-local only: commit everything (the CLI's clean-tree gate), then return to main if the CLI left an ethan/* branch.
        Never touches the shared repo. True when the example_host is clean on main afterwards."""
        raise NotImplementedError('TODO: implement')

    def gate(self, timeout: int=...):
        """(ok, text): `./scripts/ethan git status` run from the example_host root (the CLI's own start gate code, read-only, no model
        request) AND the porcelain check, no remote, on main."""
        raise NotImplementedError('TODO: implement')

    def destroy(self) -> bool:
        raise NotImplementedError('TODO: implement')

def ensure_trusted(home: Path | None=None, trust_file: Path | None=None) -> bool:
    """OPT-IN ONLY (build(trust=True) or ETHAN_example_host_TRUST=1): changing a trust setting needs Ethan's explicit OK, and an agent once
    added this entry without it (reverted 2026-11-05). Mark the example_host parent TRUST_PARENT in ~/.gemini/trustedFolders.json so the CLI's approval policy and project settings
    apply inside example_hostes (an untrusted folder runs without them). Atomic, best effort, never raises."""
    raise NotImplementedError('TODO: implement')

def build(source=None, home=None, name: str | None=None, trust: bool=False, extra_links=...) -> example_host:
    """Create a example_host. Raises example_hostError (and removes the half-built dir) on any failure."""
    raise NotImplementedError('TODO: implement')

def destroy(root) -> bool:
    """Remove a example_host (symlinks are unlinked, never followed). Refuses anything without the example_host marker."""
    raise NotImplementedError('TODO: implement')

def prune(hours: float=6.0, home=None) -> list:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
