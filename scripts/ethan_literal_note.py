# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Dispatch small, explicit note creations through Gemini's declared write_file tool."""
import hashlib
import os
import re
import stat
from contextlib import ExitStack
from pathlib import Path

def stock_system(payload):
    raise NotImplementedError('TODO: implement')

def known_bootstrap(text, workspace):
    raise NotImplementedError('TODO: implement')

def fresh_context(payload, prompt, workspace, path, *, read_only=False):
    raise NotImplementedError('TODO: implement')

def parse_note(prompt):
    """Only a single imperative with a literal destination and content takes this route."""
    raise NotImplementedError('TODO: implement')

def note_state(workspace, relative, content):
    """Look only inside the chosen workspace, with no-follow reads of a bounded regular file."""
    raise NotImplementedError('TODO: implement')

def native_note_part(payload, admission, workspace, tools):
    """Return one native candidate part or None to let the existing dispatcher handle the turn."""
    raise NotImplementedError('TODO: implement')
