# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Read-only local folder discovery for a signed, explicit human request.

Called by the Magi MCP server after an Enki receipt binds the query to an
active local human turn. The bridge renders only the returned directory names.
No file contents, cloud services, index writes or background jobs are involved.
macOS queries Spotlight for the standard protected user folders. Linux uses a
bounded directory walk. Search roots are fixed by the application, so model
arguments cannot turn a name lookup into an arbitrary filesystem walk.
"""
import hashlib
import os
import re
import selectors
import subprocess
import sys
import time
from collections import deque
from pathlib import Path
from ethan_literal_note import _ALARM
from ethan_locate import PRIVATE_DIRS, SECRET_NAME

def folder_terms(prompt):
    """Return the requested name terms, or None for ambiguous/compound instructions."""
    raise NotImplementedError('TODO: implement')

def signed_request(client_id, question):
    """Bind private name reads to this client's current human turn, even if a model calls the tool itself."""
    raise NotImplementedError('TODO: implement')

def visible(name):
    """Admit a single nonprivate, terminal-safe display component from an OS listing."""
    raise NotImplementedError('TODO: implement')

def match_name(name, terms):
    """Match every requested token on the basename itself, irrespective of capitalization."""
    raise NotImplementedError('TODO: implement')

def spotlight_names(base, terms):
    """Bound the index service by bytes and time; never buffer an unbounded result set."""
    raise NotImplementedError('TODO: implement')

def folder_names(terms, home, workspace):
    """Use independent budgets for each root so a large Downloads cannot starve the workspace."""
    raise NotImplementedError('TODO: implement')

def folder_answer(data, terms):
    """Render only validated matches from the paired tool response and always describe coverage."""
    raise NotImplementedError('TODO: implement')
