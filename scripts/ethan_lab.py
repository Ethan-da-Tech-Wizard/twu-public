# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Ethan lab: a clean, remote-less git copy of the workspace so the real Ethan CLI can start (its git gate needs a clean
main with no remote) even while other seats dirty the shared workspace.

  ethan_lab.py refresh [--lab DIR]            copy scripts/ Cannon/ MAGI_0/ AGENTS.md CLAUDE.md + small data files into the
                                              lab (default ~/TWU_ethan_lab), commit a baseline, drop any remote
  ethan_lab.py run --task-id ID [--lab DIR]   materialise data/self_improve/tasks/ID.json into lab/work/ID-<stamp>, write the
                                              prompt, put the HIDDEN verifier in the real workspace
                                              data/tool_trials/ethan_lab/ID/verify.py (outside the lab), then run the lab's
                                              visible_run_loop.py (real CLI in a visible kitty window) with --verify-cmd,
                                              --require-output and --protect. Prints the receipt path.

Refuses a lab that is, contains, or is inside the workspace. Stdlib only; reuses ethan_si_bank for task loading.
"""
import argparse, os, shutil, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path
import ethan_si_bank as bank

class LabError(Exception):
    pass

def check_lab(lab, workspace=...):
    raise NotImplementedError('TODO: implement')

def git(lab, *args, check=True):
    raise NotImplementedError('TODO: implement')

def commit_all(lab, message):
    raise NotImplementedError('TODO: implement')

def refresh(lab=..., workspace=...):
    raise NotImplementedError('TODO: implement')

def load_task(task_id, task_dir=...):
    raise NotImplementedError('TODO: implement')

def prompt_for(task, work_rel):
    raise NotImplementedError('TODO: implement')

def prepare(task, lab, workspace=..., stamp=None):
    """Create work dir, prompt and hidden verifier; return the visible_run_loop argv (after the script path)."""
    raise NotImplementedError('TODO: implement')

def run(task_id, lab=..., workspace=..., task_dir=..., runner=...):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
