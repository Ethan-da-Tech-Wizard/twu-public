# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""MagiPhone's owner-only seat view and private local Git projects.

Reuses the checked project and presence adapters. Phone projects have a separate
store from EZ; no company checkout or Briar contact gains access through this API.
"""
from pathlib import Path
from urllib.parse import urlparse
import json
from ez_workspace import Workspace, WorkspaceError
from ez_magi_workspace import MagiWorkspace

class PhoneWorkbench:

    def __init__(self, project_root=None, source_root=None):
        raise NotImplementedError('TODO: implement')

    def seats(self):
        raise NotImplementedError('TODO: implement')

    def get(self, action, query):
        raise NotImplementedError('TODO: implement')

    def post(self, action, body):
        raise NotImplementedError('TODO: implement')

def handle(handler, method, path, query=None, workbench=None):
    """Handle only this namespace; authenticate before reading state or a body."""
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
