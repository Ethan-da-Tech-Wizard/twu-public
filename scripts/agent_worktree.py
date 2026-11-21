# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Per-agent git worktrees: file fights are structurally impossible.

Each agent gets its own worktree + branch (agent/<AGENT>-<ts>) and never touches the
shared main worktree. Only the integrator (TWU_INTEGRATOR=1) merges into `main`.
Stdlib + git only. Never pushes, never adds remotes.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time

class Fail(Exception):

    def __init__(self, msg, code=1):
        raise NotImplementedError('TODO: implement')

def git(cwd, *args, check=True):
    raise NotImplementedError('TODO: implement')

def gout(cwd, *args):
    raise NotImplementedError('TODO: implement')

def main_worktree(repo):
    raise NotImplementedError('TODO: implement')

def common_dir(repo):
    raise NotImplementedError('TODO: implement')

def snapshot(main):
    raise NotImplementedError('TODO: implement')

def registry_path(repo):
    raise NotImplementedError('TODO: implement')

def load_reg(repo):
    raise NotImplementedError('TODO: implement')

def save_reg(repo, reg):
    raise NotImplementedError('TODO: implement')

def default_root(main):
    raise NotImplementedError('TODO: implement')

def guarded(repo, fn):
    """Run fn() with the main-worktree isolation invariant enforced."""
    raise NotImplementedError('TODO: implement')

def get_entry(repo, agent):
    raise NotImplementedError('TODO: implement')

def cmd_new(repo, agent, base=..., root=None):
    raise NotImplementedError('TODO: implement')

def _copy_one(src_root, rel, dst_root):
    raise NotImplementedError('TODO: implement')

def cmd_seed(repo, agent, paths):
    raise NotImplementedError('TODO: implement')

def cmd_list(repo):
    raise NotImplementedError('TODO: implement')

def cmd_status(repo, agent):
    raise NotImplementedError('TODO: implement')

def cmd_remove(repo, agent, force=False):
    raise NotImplementedError('TODO: implement')

def cmd_integrate(repo, agent, test_cmd, into=..., root=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
