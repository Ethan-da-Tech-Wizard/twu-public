# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Run a self-improve bank task as a step ladder inside ONE visible Ethan CLI window.

  ethan_ladder_visible.py run --task-id ID [--max-attempts-per-rung 4] [--turn-timeout 600]

Loads data/self_improve/tasks/<ID>.json, writes its setup files into
data/tool_trials/ladder_visible/<ID>-<stamp>/work (the hidden verifier and all receipts stay in the PARENT dir, outside
the work dir), opens one visible kitty window (visible_run_loop.launch_window / wait_for_ready), then walks the rungs of
scripts/ethan_ladder.py: submit the rung prompt, wait for the turn to end, run the rung verifier plus the cumulative
regression check. A failed attempt gets ethan_ladder's escalating corrective prompt combined with
ethan_nudge.plan_next(classify_turn(window screen ...)) so no prompt is ever repeated; the 'fresh-session' strategy (and any
timeout) closes and reopens the window. A rung that exhausts its attempts is recorded and the run moves on.

Safety is visible_run_loop's: STOP / MODEL_STANDBY latches checked before every prompt, every prompt registered as
machine-composed (register_staged) BEFORE it is typed, the window closed in a finally block. The Ethan CLI refuses to
start on a dirty repo, so a dirty `git status --porcelain --untracked-files=all` prints 'repo dirty: commit first' and
exits 3 without launching (work files live under the git-ignored data/ tree, and are written after the window is up).

ISOLATION (default): the run happens in a throwaway git example_host (scripts/ethan_example_host.py, ~/.cache/ethan-example_hostes/<id>/, outside the
workspace) holding copies of scripts/ethan + the Git guard and symlinks to everything else. The kitty window runs
`./scripts/ethan chat` from the example_host root, the work dir is <example_host>/work, and receipts/logs/screens still go to the real
data dir. The shared repo and Ethan's branch are never touched (no checkpoint commits, no branch switches, no merges). Set
ETHAN_VISIBLE_ROOT to run in an existing prepared root instead. The legacy path (heal_repo: commit the shared repo, return to
main) is used ONLY with `--heal-shared` and ETHAN_VISIBLE_ROOT unset. Windows are never moved or focused unless `--show`.

Exit codes: 0 full pass, 1 not a full pass (incl. runtime error, recorded in the receipt), 2 STOP/standby/refused,
3 repo dirty. Receipt: <run dir>/receipt.json (twu.ethan-ladder-visible.v1); per-attempt screen text in <run dir>/screens/.
"""
from __future__ import annotations
import argparse, json, os, shutil, signal, subprocess, sys, time, uuid
from datetime import datetime, timezone
from pathlib import Path
import ethan_si_bank as bank
import ethan_ladder as ladder
import ethan_nudge as nudge
import visible_run_loop as vrl

class Aborted(Exception):
    pass

def repo_dirty(root=None) -> str:
    """'' when `git status --porcelain --untracked-files=all` is empty, else the status text (or the git error). Checks `root`
    (default: the visible root, which is the shared workspace only when no example_host is in use)."""
    raise NotImplementedError('TODO: implement')

def requirements_block(task: dict, limit: int=1800) -> str:
    """The task's full requirement text in every rung prompt. A rung such as 'make n == 5 true' only makes sense next to the
    sentence that explains it ('skip rows with a missing game_id or non-numeric scores'), which lives in another step: the 7B
    failed rung 2 four times in a row because it never saw that sentence."""
    raise NotImplementedError('TODO: implement')

def data_files_block(work: Path, target: str, limit: int=2000, total: int=5000) -> str:
    """Contents of the small non-target files already in the work dir (e.g. the input CSV), so the model works from the real
    column names instead of guessing them: the 7B invented 'id'/'team_1' columns for a CSV it never opened."""
    raise NotImplementedError('TODO: implement')

def heal_example_host(root) -> bool:
    """Commit/return-to-main INSIDE a example_host root (never the shared repo). True when it is clean on main afterwards."""
    raise NotImplementedError('TODO: implement')

def heal_repo() -> bool:
    """LEGACY, shared-repo only (`--heal-shared`, never with a example_host root). Self-heal for the CLI's clean-tree gate: local checkpoint commit of everything, then return to main if the CLI left
    the repo on an ethan/* task branch (scripts/ethan_tree_keeper.py; local only, no push, no history rewrite). Never raises."""
    raise NotImplementedError('TODO: implement')

def load_task(task_id: str, directory=None) -> dict:
    raise NotImplementedError('TODO: implement')

class Window:
    """One owned kitty window; reopen() = the fresh-session strategy."""

    def __init__(self, run_dir: Path, dirty=None, healer=None):
        raise NotImplementedError('TODO: implement')

    def _dirty(self) -> str:
        raise NotImplementedError('TODO: implement')

    def _heal(self):
        raise NotImplementedError('TODO: implement')

    def open(self):
        raise NotImplementedError('TODO: implement')

    def close(self):
        raise NotImplementedError('TODO: implement')

    def reopen(self):
        raise NotImplementedError('TODO: implement')

def _abs_files(snap: dict, workdir: Path) -> dict:
    raise NotImplementedError('TODO: implement')

def _rel_to_repo(path: Path, root=None) -> str:
    raise NotImplementedError('TODO: implement')

def run_visible(task: dict, run_dir: Path, max_attempts=4, turn_timeout=600.0, rng=None, say=..., heal_shared=False, root=None) -> dict:
    """Drive the ladder in one window. Returns the receipt dict (never raises except KeyboardInterrupt).

    Default: runs in a fresh example_host repo (built here, removed after). `root` (or ETHAN_VISIBLE_ROOT) = use that prepared root
    instead (not removed). `heal_shared=True` with no root = the legacy path in the shared workspace."""
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
