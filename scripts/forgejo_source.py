# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Reviewable source-only checkpoints for a private loopback Forgejo repository.

Never copy canonical Git objects, change its task/index/remotes, or import its
history. Prepare reads exact code paths; checkpoint and seed require the reviewed
receipt hash. A fresh checkpoint records previously uncommitted source honestly.
Credential scans are bounded checks, not a substitute for source review.
"""
from __future__ import annotations
import argparse
import ast
import base64
import configparser
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import tempfile
import urllib.error
import urllib.request

class SourceError(ValueError):
    pass

def require_running(root):
    raise NotImplementedError('TODO: implement')

def digest(raw):
    raise NotImplementedError('TODO: implement')

def encoded(value):
    raise NotImplementedError('TODO: implement')

def read_regular(root, relative, limit=..., *, private=False):
    raise NotImplementedError('TODO: implement')

def audit_source(path, raw):
    raise NotImplementedError('TODO: implement')

def private_directory(path):
    raise NotImplementedError('TODO: implement')

def git_env(home):
    raise NotImplementedError('TODO: implement')

def git(root, arguments, home, *, extra=None, binary=False):
    raise NotImplementedError('TODO: implement')

def canonical_state(root):
    raise NotImplementedError('TODO: implement')

def prepare(root, store, paths=None):
    raise NotImplementedError('TODO: implement')

def verified_stage(stage, expected_sha256):
    raise NotImplementedError('TODO: implement')

def checkpoint_message(expected_sha256):
    raise NotImplementedError('TODO: implement')

def checkpoint(stage, expected_sha256):
    raise NotImplementedError('TODO: implement')

def verify_checkpoint(stage, tree, receipt, expected_sha256):
    """Require one reviewed root commit, with no history/config redirection."""
    raise NotImplementedError('TODO: implement')

class NoRedirect(urllib.request.HTTPRedirectHandler):

    def redirect_request(self, *args, **kwargs):
        raise NotImplementedError('TODO: implement')

def seed(stage, expected_sha256, base_url, owner, repository, token_file):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
