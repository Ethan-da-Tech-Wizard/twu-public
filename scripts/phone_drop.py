# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Upload-only phone inbox, loopback receiver behind the existing private mesh.

No models, commands from uploads, cloud storage, or access to the dashboard API.
"""
from __future__ import annotations
import base64
import hashlib
import hmac
import html
import http.client
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import re
import secrets
import shutil
import stat
import subprocess
import sys
import threading
import time
from urllib.parse import quote, unquote, urlsplit
from dashboard_control import opened, read_bytes, runtime_directory

class Store:

    def __init__(self, root, runtime=None):
        raise NotImplementedError('TODO: implement')

    def authorized(self, header):
        raise NotImplementedError('TODO: implement')

    def receive(self, stream, length, filename):
        raise NotImplementedError('TODO: implement')

class Handler(BaseHTTPRequestHandler):

    def log_message(self, *_args):
        raise NotImplementedError('TODO: implement')

    def respond(self, status, body, content_type=...):
        raise NotImplementedError('TODO: implement')

    def do_GET(self):
        raise NotImplementedError('TODO: implement')

    def do_POST(self):
        raise NotImplementedError('TODO: implement')

def health(port=...):
    raise NotImplementedError('TODO: implement')

def private_url():
    """Use an existing private Tailscale mapping. HTTP is encrypted by the mesh.

    https://tailscale.com/docs/servers documents the HTTP-over-WireGuard case.
    Never enable a new mapping, publish a Funnel, or disable TLS verification.
    """
    raise NotImplementedError('TODO: implement')

def open_local(path):
    raise NotImplementedError('TODO: implement')

def pair(root):
    raise NotImplementedError('TODO: implement')

class Receiver(ThreadingHTTPServer):

    def __init__(self, address, store):
        raise NotImplementedError('TODO: implement')

    def process_request(self, request, address):
        raise NotImplementedError('TODO: implement')

    def process_request_thread(self, request, address):
        raise NotImplementedError('TODO: implement')

def serve(root, port=...):
    raise NotImplementedError('TODO: implement')

def start(root):
    raise NotImplementedError('TODO: implement')
