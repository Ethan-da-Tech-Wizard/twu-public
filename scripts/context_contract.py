# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Resolve explicit app names and verify app identity before opening a local UI.

This is a routing boundary, not a grant of permission to execute a tool.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import subprocess
import sys
import time
from urllib.parse import urlsplit
from urllib.error import URLError
import urllib.request

def contracts(path=None):
    raise NotImplementedError('TODO: implement')

def resolve_context(alias, path=None):
    raise NotImplementedError('TODO: implement')

def validate_action(context_id, tool, path=None):
    raise NotImplementedError('TODO: implement')

class _NoRedirect(urllib.request.HTTPRedirectHandler):

    def redirect_request(self, *args, **kwargs):
        raise NotImplementedError('TODO: implement')

def verify_identity(app):
    raise NotImplementedError('TODO: implement')

def ensure_running(app):
    """An explicit EZ open may start its local UI; occupied ports stay untouched."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
