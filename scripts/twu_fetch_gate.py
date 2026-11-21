# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""TWU fetch gate: vet git / pip / npm / yay fetches BEFORE they run code on example_host.

Called by scripts/twu_fetch_wrapper.sh (symlinked as git, yay, pip, pip3, npm in ~/.local/bin).
  twu_fetch_gate.py pre  <tool> <real-binary> [args...]   exit 0 proceed, 3 FAIL (abort), other = gate crashed
  twu_fetch_gate.py post <tool> <real-binary> [args...]   (git clone only) scan the cloned tree
  twu_fetch_gate.py check <path-or-url>                    manual: preview a file/dir or vet a repo URL

Only FAIL aborts; REVIEW prints a warning. Nothing inspected is ever executed or imported.
Reuses private/example_host/safety/{install_preview,unsafe_catalog}.py (one shared rule catalog).
"""
import ipaddress
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import urlparse
import unsafe_catalog as uc

def say(msg):
    raise NotImplementedError('TODO: implement')

class Verdict:

    def __init__(self, label):
        raise NotImplementedError('TODO: implement')

    def add(self, sev, what, evidence=...):
        raise NotImplementedError('TODO: implement')

    def extend(self, fs):
        raise NotImplementedError('TODO: implement')

    @property
    def level(self):
        raise NotImplementedError('TODO: implement')

    def report(self):
        raise NotImplementedError('TODO: implement')

def done(v):
    raise NotImplementedError('TODO: implement')

def host_of(url):
    """Return (host, scheme) for a git remote; (None, 'local') for filesystem paths."""
    raise NotImplementedError('TODO: implement')

def vet_url(url, v):
    raise NotImplementedError('TODO: implement')

def git_urls(args):
    """URL-like positional args after the subcommand."""
    raise NotImplementedError('TODO: implement')

def clone_positionals(args):
    raise NotImplementedError('TODO: implement')

def git_sub(args):
    raise NotImplementedError('TODO: implement')

def clone_dest(args, sub_args, pre):
    raise NotImplementedError('TODO: implement')

def scan_tree(root):
    """Line-scan install-time scripts in a source tree. Returns Verdict."""
    raise NotImplementedError('TODO: implement')

def git_pre(real, args):
    raise NotImplementedError('TODO: implement')

def git_post(real, args):
    raise NotImplementedError('TODO: implement')

def pip_name(spec):
    raise NotImplementedError('TODO: implement')

def pip_pre(real, args):
    raise NotImplementedError('TODO: implement')

def npm_pre(real, args):
    raise NotImplementedError('TODO: implement')

def yay_pre(real, args):
    raise NotImplementedError('TODO: implement')

def check(target):
    raise NotImplementedError('TODO: implement')

def main(argv):
    raise NotImplementedError('TODO: implement')
