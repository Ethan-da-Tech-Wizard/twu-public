# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Outbox presenter: turn drafts written by a person or a local model into a copy-and-send page. Nothing is ever sent.

  python3 scripts/outbox_presenter.py data/outbox/<name>.json      writes apps/outbox_<name>.html

Input JSON:
  {"title": "...", "storage_key": "twu_<name>_sent", "tiers": {"1": "Send first", "2": "Later", "hold": "Hold: ask first"},
   "drafts": [{"id": "unique", "name": "Person", "dept": "Where they work", "tier": "1", "to": "address", "phone": "",
               "subject": "...", "body": "...", "note": "optional warning", "to_source": "where the address was published"}]}
Rules: every draft needs id, name, dept, tier, to, subject and body. A draft with no `to_source` is shown with a red
"do not send until verified" banner (AGENTS.md Rule 14: never guess addresses). Local models may write this file; a person
clicks Copy and sends. "Copy my sent list" gives text to paste back so the sends can be logged in the contact tracker.
"""
import html
import json
import sys
from pathlib import Path

def build(cards, out_path, title, tiers, storage_key):
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
