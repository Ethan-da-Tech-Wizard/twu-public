# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Outreach Dispatcher and Preview Utility for TWU LLC.

Allows previewing, testing Gmail connectivity, and sending value-first
audit emails directly to local business owners.

Usage:
  python3 scripts/send_outreach.py --test-connection
  python3 scripts/send_outreach.py --list
  python3 scripts/send_outreach.py --preview <id>
  python3 scripts/send_outreach.py --send <id>           (dry-run by default)
  python3 scripts/send_outreach.py --send <id> --live    (actually sends via SMTP)
"""
import argparse
import email.utils
import json
import os
import re
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

def load_credentials():
    raise NotImplementedError('TODO: implement')

def test_connection():
    raise NotImplementedError('TODO: implement')

def load_audits():
    raise NotImplementedError('TODO: implement')

def save_audits(audits):
    raise NotImplementedError('TODO: implement')

def list_audits(audits):
    raise NotImplementedError('TODO: implement')

def parse_audit_num(audit_id_str):
    raise NotImplementedError('TODO: implement')

def get_audit(audits, audit_id):
    raise NotImplementedError('TODO: implement')

def read_dossier_email(audit_record):
    raise NotImplementedError('TODO: implement')

def preview_audit(audits, audit_id):
    raise NotImplementedError('TODO: implement')

def send_audit(audits, audit_id, live=False):
    raise NotImplementedError('TODO: implement')

def main():
    raise NotImplementedError('TODO: implement')
