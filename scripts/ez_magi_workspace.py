# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Project-scoped Magi work receipts for EZ; no models, execution or demo state.

Seats describe reported connections. Assignment only queues a human operator
request; an agent's later result is reported evidence, not independent review.
"""
from __future__ import annotations
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import importlib.util
import json
import os
from pathlib import Path
import re
import secrets
import socket
import stat
from ez_safe_path import split_base

def _stamp():
    raise NotImplementedError('TODO: implement')

def _short(value, maximum=200):
    raise NotImplementedError('TODO: implement')

def _public_hint(project, task_id):
    raise NotImplementedError('TODO: implement')

def _unique_pairs(pairs):
    raise NotImplementedError('TODO: implement')

def _shared_text(text):
    raise NotImplementedError('TODO: implement')

class MagiWorkspace:

    def __init__(self, workspace, root=None, state_path=None, local_host=None):
        raise NotImplementedError('TODO: implement')

    def _project_exists(self, project):
        raise NotImplementedError('TODO: implement')

    def _project(self, project, branch=...):
        raise NotImplementedError('TODO: implement')

    def _directory(self, base=None):
        raise NotImplementedError('TODO: implement')

    @contextmanager
    def _locked(self):
        raise NotImplementedError('TODO: implement')

    @staticmethod
    def _regular(fd, maximum):
        raise NotImplementedError('TODO: implement')

    def _read(self, directory):
        raise NotImplementedError('TODO: implement')

    def _save(self, directory, rows):
        raise NotImplementedError('TODO: implement')

    def seats(self):
        """Shared read-only view of the same connection evidence used by Herder."""
        raise NotImplementedError('TODO: implement')

    def _events(self):
        raise NotImplementedError('TODO: implement')

    @staticmethod
    def _public(row, events):
        raise NotImplementedError('TODO: implement')

    def _reconcile(self, rows):
        """Recover receipts only; never resend an ambiguous operator request."""
        raise NotImplementedError('TODO: implement')

    def tasks(self, project):
        raise NotImplementedError('TODO: implement')

    @staticmethod
    def _task(rows, project, task_id):
        raise NotImplementedError('TODO: implement')

    @staticmethod
    def _question_public(question, row):
        raise NotImplementedError('TODO: implement')

    @staticmethod
    def _shared_reply(row, event, allowed):
        raise NotImplementedError('TODO: implement')

    def thread(self, project, task_id):
        raise NotImplementedError('TODO: implement')

    def ask(self, project, task_id, text):
        raise NotImplementedError('TODO: implement')

    def assign(self, project, seat, text, branch=...):
        raise NotImplementedError('TODO: implement')
