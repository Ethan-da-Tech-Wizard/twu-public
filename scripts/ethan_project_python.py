# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Validate generated project source before returning a native write_file candidate."""
import copy
from http.client import HTTPException
import json
import re
import sys

def project_python_mode(prompt):
    raise NotImplementedError('TODO: implement')

def compilation_issue(source):
    raise NotImplementedError('TODO: implement')

def check_project_writes(reply, request, post):
    """Keep sibling calls unchanged. Allow one local correction affecting only a single source line."""
    raise NotImplementedError('TODO: implement')
