# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""ethan_doctor: tell a human in 10 seconds whether the Ethan web lookup path works, and what to do if not.

Usage: ethan_doctor.py [--json] [--no-fix] [--offline] [--quiet]
Exit: 0 PASS/WARN only, 1 any FAIL remaining, 2 usage error. Stdlib only.
"""
import argparse
import datetime
import json
import os
import platform
import shutil
import secrets
import socket
import stat
import subprocess
import sys
import threading

def _res(name, status, detail=..., fix=..., recovered=False):
    raise NotImplementedError('TODO: implement')

def _ensure_path():
    raise NotImplementedError('TODO: implement')

def _run(cmd, timeout):
    raise NotImplementedError('TODO: implement')

def check_ethan_cli(ctx=None, fix=True):
    raise NotImplementedError('TODO: implement')

def _failing_component(data):
    raise NotImplementedError('TODO: implement')

def check_ethan_ready(ctx=None, fix=True):
    raise NotImplementedError('TODO: implement')

def check_mcp_tools(ctx=None, fix=True):
    raise NotImplementedError('TODO: implement')

def denylist_path():
    raise NotImplementedError('TODO: implement')

def check_denylist(ctx=None, fix=True):
    raise NotImplementedError('TODO: implement')

def check_gateway_fetch(ctx=None, fix=True):
    raise NotImplementedError('TODO: implement')

def check_audit_log(ctx=None, fix=True):
    raise NotImplementedError('TODO: implement')

def check_python_version(ctx=None, fix=True):
    raise NotImplementedError('TODO: implement')

def run_one(name, fn, ctx, fix, timeout=None):
    """Run a check under a timeout; any crash becomes a FAIL result."""
    raise NotImplementedError('TODO: implement')

def collect(fix, offline):
    raise NotImplementedError('TODO: implement')

def summarize(results):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
