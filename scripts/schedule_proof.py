# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""schedule_proof: read-only proof that every scheduled job actually ran on time.

  schedule_proof.py report [--json] [--since "YYYY-MM-DD HH:MM"]   exit 1 if any job is not OK

Sources (all read-only): data/scheduled_jobs.json (what should run), data/netguard/catchup_state.<host>.json
(where scripts/catchup_runner.py records last_success / fails / last_error), launchd evidence files, LaunchAgents plists,
`launchctl list`, ~/Library/Logs/twu-*.log. Verdicts per job, judged against 2x its cadence (daily = 48 h):
  OK       last success inside 2x cadence and not failing
  LATE     last success older than 2x cadence
  NEVER    no recorded success and no evidence file
  FAILING  failed 3+ times in a row (catchup_runner's own alarm threshold)
  OFF      disabled in the manifest on purpose (not counted against the exit code)
Stdlib only. Nothing is written, nothing is run except `launchctl list`.
"""
from __future__ import annotations
import json, os, plistlib, re, shutil, socket, subprocess, sys, time
from pathlib import Path

def parse_since(s):
    """'YYYY-MM-DD HH:MM -0700' (explicit UTC offset) or 'YYYY-MM-DD HH:MM' (local) -> epoch."""
    raise NotImplementedError('TODO: implement')

def scrub(text):
    """Remove MAC addresses, hostnames, IPs, home paths, and secret-looking tokens before anything is printed."""
    raise NotImplementedError('TODO: implement')

def human(sec):
    raise NotImplementedError('TODO: implement')

def cadence_s(job):
    raise NotImplementedError('TODO: implement')

def load_state(state_dir, host=...):
    raise NotImplementedError('TODO: implement')

def evidence_time(job, root, host=...):
    """(epoch, source) for a job's evidence file: its own recorded last_success if it has one, else file mtime."""
    raise NotImplementedError('TODO: implement')

def judge(job, js, root, now, host=...):
    """One job -> dict. Never raises on odd state: unreadable means NEVER, not fine."""
    raise NotImplementedError('TODO: implement')

def parse_launchctl(text):
    """`launchctl list` lines 'PID	STATUS	LABEL' -> {label: (pid|None, status|None)} for com.twu.* only."""
    raise NotImplementedError('TODO: implement')

def agents(launch_dir, launchctl_text, now):
    """Rows for each com.twu LaunchAgent plist: loaded? last exit? output fresh within 2x StartInterval?"""
    raise NotImplementedError('TODO: implement')

def log_errors(logs_dir, n=5):
    raise NotImplementedError('TODO: implement')

def disk(path=...):
    raise NotImplementedError('TODO: implement')

def leak_check(state_dir_root, since, host=...):
    """Did the leak watch record a run after `since`?"""
    raise NotImplementedError('TODO: implement')

def build(root=..., state_dir=None, launch_dir=None, logs_dir=None, launchctl_text=None, now=None, since=..., host=...):
    raise NotImplementedError('TODO: implement')

def fmt_time(t):
    raise NotImplementedError('TODO: implement')

def render(rep):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
