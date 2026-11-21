# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Free local tax/receipt workspace using the existing TWU ledger."""
import argparse
import base64
from datetime import datetime, timezone
import hashlib
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import mimetypes
import os
from pathlib import Path
import plistlib
import secrets
import shutil
import sqlite3
import subprocess
import sys
import threading
import time
from urllib.parse import urlsplit
from urllib.request import urlopen
import uuid
import webbrowser
import ledger
import receipt_store
import tax_engine

def load(relative):
    raise NotImplementedError('TODO: implement')

def transaction_fingerprint(transaction):
    raise NotImplementedError('TODO: implement')

def review_state(transaction, reviews):
    raise NotImplementedError('TODO: implement')

def snapshot(scan_receipts=False):
    raise NotImplementedError('TODO: implement')

def build():
    raise NotImplementedError('TODO: implement')

def archive_before(include_ledger=False):
    raise NotImplementedError('TODO: implement')

def audit(action, details, backup):
    raise NotImplementedError('TODO: implement')

def apply_action(route, payload):
    raise NotImplementedError('TODO: implement')

def state_for_client(token):
    raise NotImplementedError('TODO: implement')

def make_handler(token, port):
    raise NotImplementedError('TODO: implement')

def serve(port):
    raise NotImplementedError('TODO: implement')

def open_dashboard():
    raise NotImplementedError('TODO: implement')

def install_login():
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
