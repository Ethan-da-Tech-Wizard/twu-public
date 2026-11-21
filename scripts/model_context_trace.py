# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Observe local request transformations; hashes are evidence, never causal explanations.

Only existing user requests are observed. No model/network calls are made here.
Private, scrubbed JSON records live outside the synced workspace.
"""
from __future__ import annotations
import hashlib
import inspect
import json
import marshal
import os
from pathlib import Path
import sys
import time
import uuid

def _json(value):
    raise NotImplementedError('TODO: implement')

def fingerprint(value):
    raise NotImplementedError('TODO: implement')

def _bounded(value, depth=0):
    raise NotImplementedError('TODO: implement')

def _safe(value):
    raise NotImplementedError('TODO: implement')

def default_directory():
    raise NotImplementedError('TODO: implement')

def _directory_fd(directory):
    raise NotImplementedError('TODO: implement')

def _source(function):
    raise NotImplementedError('TODO: implement')

class Trace:

    def __init__(self, origin, payload, directory=None):
        raise NotImplementedError('TODO: implement')

    def _warning(self, error):
        raise NotImplementedError('TODO: implement')

    def snapshot(self, payload):
        raise NotImplementedError('TODO: implement')

    def stage(self, name, function, before, after, error=None):
        raise NotImplementedError('TODO: implement')

    def apply(self, name, function, payload, *args, trace_result_index=None, **kwargs):
        raise NotImplementedError('TODO: implement')

    def attempt(self, kind, response=None, error=None, request=None):
        raise NotImplementedError('TODO: implement')

    def finish(self, outcome):
        raise NotImplementedError('TODO: implement')

class _UnavailableTrace:

    def apply(self, name, function, payload, *args, trace_result_index=None, **kwargs):
        raise NotImplementedError('TODO: implement')

    def snapshot(self, payload):
        raise NotImplementedError('TODO: implement')

    def stage(self, *args, **kwargs):
        raise NotImplementedError('TODO: implement')

    def attempt(self, *args, **kwargs):
        raise NotImplementedError('TODO: implement')

    def finish(self, outcome):
        raise NotImplementedError('TODO: implement')

def start(origin, payload, directory=None):
    raise NotImplementedError('TODO: implement')
