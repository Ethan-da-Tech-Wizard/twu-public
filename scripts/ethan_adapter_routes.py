# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Offline per-turn LoRA policy for Ethan. Only the host owner can approve routes.

A successful decision supplies llama.cpp's request-local `lora` field. Omitting
the field preserves the running server's defaults, including the owner's LoRA.
The classifier never accepts a filename, scale, or adapter ID from chat.
"""
import copy
import json
import os
from pathlib import Path
import re
import stat
import time
import uuid

def classify_task(text):
    """Return one narrow task label or abstain; the caller supplies signed user text."""
    raise NotImplementedError('TODO: implement')

def _digest(value):
    raise NotImplementedError('TODO: implement')

def _scale(value):
    raise NotImplementedError('TODO: implement')

def _adapter(row):
    raise NotImplementedError('TODO: implement')

def _unique(pairs):
    raise NotImplementedError('TODO: implement')

def current_human_only(payload, text, workspace):
    """Only an initial user turn of the stock client can ask the learned judge."""
    raise NotImplementedError('TODO: implement')

def jev_task(human, receipt):
    """Jev can disambiguate coding only. A recent tool message never reaches this function."""
    raise NotImplementedError('TODO: implement')

def load_policy(path=None):
    """Read a small real owner-only policy. A missing/malformed policy disables overrides."""
    raise NotImplementedError('TODO: implement')

def select_route(policy, task, model_path, observed, file_hash):
    """Use only verified loaded files on one backend. Return (wire override, reason).

    IDs are ephemeral and unique per server start. Resolve them from fresh
    metadata, never from a filename heuristic or a persisted integer.
    """
    raise NotImplementedError('TODO: implement')

def record_latest(request_id, receipt):
    """Publish one private, bounded selection record independently of full trace retention."""
    raise NotImplementedError('TODO: implement')
