# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""magi_gemini_mcp: a stdio MCP server that lets a Gemini CLI window read and post to the Magi bus.

Tools (A7-MAGI-MCP-002, from the A4-GEMINI-WINDOW-014 spec):
  magi_cluster_status  seats (who), STOP flag, whether the local model and the Gemini bridge are listening
  magi_inbox_poll      new messages for a seat (only this server's own seat is marked read)
  magi_dispatch_task   post one validated message through scripts/magi.py (default kind: assignment)
  magi_web_read        read one public HTTPS page as text (A7-MCP-WEB-004)
  magi_github_lookup   read a public GitHub repository's README as text (A7-MCP-WEB-004)
  magi_github_search   find public repositories and return a bounded list of source links

The two web tools exist only when MAGI_WEB_ENABLED=1, and they go through scripts/magi_web.py, the single web
gateway governed by AGENTS.md (HTTPS GET only, public addresses only, fail-closed private deny-list,
robots, rate limits, Linux-only logs). Results are labelled web-untrusted and capped for small-model contexts.

The sending seat comes from the MAGI_SEAT environment variable, never from the model, so a window cannot speak
for another seat. Without MAGI_SEAT the server is read-only. Posting stops while comms/STOP exists, and each
server process may post at most MAGI_MCP_MAX_SENDS messages (default 20). Attachments are not offered.

Register in Gemini CLI settings (mcpServers), e.g.:
  "magi": {"command": "python3", "args": ["<TWU folder>/scripts/magi_gemini_mcp.py"], "env": {"MAGI_SEAT": "13"}}
"""
import json
import os
from pathlib import Path
import re
import secrets
import socket
import sys
import time
from urllib.parse import urlencode
import magi

class ToolError(Exception):
    pass

class Server:

    def __init__(self, env=None):
        raise NotImplementedError('TODO: implement')

    def _allowed_coordination_names(self):
        raise NotImplementedError('TODO: implement')

    def tools(self):
        raise NotImplementedError('TODO: implement')

    def gateway_fetch(self, url, *, foreground=False):
        raise NotImplementedError('TODO: implement')

    def web_fetch(self, url, max_chars, *, visible=False):
        raise NotImplementedError('TODO: implement')

    def web_read(self, args, *, visible=False):
        raise NotImplementedError('TODO: implement')

    def github_lookup(self, args):
        raise NotImplementedError('TODO: implement')

    def github_search(self, args):
        raise NotImplementedError('TODO: implement')

    def fact_check(self, args):
        raise NotImplementedError('TODO: implement')

    def visible_browser(self, args):
        raise NotImplementedError('TODO: implement')

    def prospect_finder(self, args):
        raise NotImplementedError('TODO: implement')

    @staticmethod
    def listening(port):
        raise NotImplementedError('TODO: implement')

    def cluster_status(self, args):
        raise NotImplementedError('TODO: implement')

    def enki_status(self, args):
        """Expose only Enki's safe projection to a Gemini session."""
        raise NotImplementedError('TODO: implement')

    def own_connection(self):
        raise NotImplementedError('TODO: implement')

    def inbox_poll(self, args):
        raise NotImplementedError('TODO: implement')

    def dispatch_task(self, args):
        raise NotImplementedError('TODO: implement')

    def system_diagnostics(self, args):
        raise NotImplementedError('TODO: implement')

    def knowledge_query(self, args):
        raise NotImplementedError('TODO: implement')

    def copy_outreach(self, args):
        raise NotImplementedError('TODO: implement')

    def package_safety_inspect(self, args):
        raise NotImplementedError('TODO: implement')

    def web_safety_check(self, args):
        raise NotImplementedError('TODO: implement')

    def call(self, name, args):
        raise NotImplementedError('TODO: implement')

    def handle(self, msg):
        """One JSON-RPC message in, one response out (None for notifications)."""
        raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
