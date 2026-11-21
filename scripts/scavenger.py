# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/scavenger.py - deterministic scavenger: find what is outdated, unlabeled, unverified or undocumented.

Read-only over the workspace (stdlib only, no model, no network, no service). Each rule is a precise
file/age/hash/regex condition, so the same tree always gives the same findings. It never certifies
semantic truth: a finding says "this condition holds", a clean run says "none of these conditions hold".

  python3 scripts/scavenger.py                  # scan, print a summary, save data/tool_trials/scavenger/LATEST.json
  python3 scripts/scavenger.py --list           # print every finding
  python3 scripts/scavenger.py --check          # exit 1 on any error finding (for check_all)
  python3 scripts/scavenger.py --selfcheck      # scan twice, prove findings are identical (determinism of the verifier)
  python3 scripts/scavenger.py --repair         # apply bounded mechanical repairs (registry, catalog, baseline pruning); defer full-history audits
  python3 scripts/scavenger.py --write-baseline # record known untested tools / unreferenced data; only shrinks (--prune-baseline)
  python3 scripts/scavenger.py --waypoint       # queue one bounded Enki Waypoint stage per rule group with findings
  python3 scripts/enki scavenge ...             # same tool through the Enki entry point

Severities: error = something claimed is broken or contradicts its own evidence; warn = outdated or
unverified; info = counted, not listed as a failure.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import subprocess
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path
import sys as _sys
import host_paths

def _finding(rule, severity, path, detail):
    raise NotImplementedError('TODO: implement')

def _skip(rel):
    raise NotImplementedError('TODO: implement')

def _load(path):
    raise NotImplementedError('TODO: implement')

class Scan:

    def __init__(self, root=..., now=None, run=..., home=None):
        raise NotImplementedError('TODO: implement')

    def add(self, *args):
        raise NotImplementedError('TODO: implement')

    def age_days(self, path):
        raise NotImplementedError('TODO: implement')

    def live_docs(self):
        raise NotImplementedError('TODO: implement')

    def tools(self):
        """S1/S2: the registry knows every tool; every test has a tool; untested tools are counted."""
        raise NotImplementedError('TODO: implement')

    def tool_index(self):
        """Stems of every tool file in the roots that hold code under test."""
        raise NotImplementedError('TODO: implement')

    def imported(self, test):
        """Tool stems a test reaches by import, path literal, or by being a prefix of the tool's name."""
        raise NotImplementedError('TODO: implement')

    def references(self):
        """S3: live docs may not point at repo files that do not exist."""
        raise NotImplementedError('TODO: implement')

    def labels(self):
        """S4: every registered label path exists; every stored fingerprint matches the file it names."""
        raise NotImplementedError('TODO: implement')

    def receipts(self):
        """S5: LATEST receipts must be fresh enough to mean anything."""
        raise NotImplementedError('TODO: implement')

    def journey_pass_evidence(self, rel, journey):
        """A journey may say PASS only with a receipt that exists, matches its hash, and was run against the current sources."""
        raise NotImplementedError('TODO: implement')

    def evidence(self):
        """S7: decoder/CLI-contract receipts older than their sources are stale; journey fixtures must parse."""
        raise NotImplementedError('TODO: implement')

    def documentation(self):
        """S6/S8: the changelog and the handoff keep pace with what changed."""
        raise NotImplementedError('TODO: implement')

    def verifiers(self):
        """S9: the verifiers themselves: every script check_all runs exists, and has a test."""
        raise NotImplementedError('TODO: implement')

    def corpus(self):
        """word -> files that mention it, over live text (code, docs, units, config); receipts and data excluded."""
        raise NotImplementedError('TODO: implement')

    def wiring(self):
        """S2/S11/S12: no floating tools or data. An untested tool must be wired into something; the untested set
        and the unreferenced-data set may only shrink against data/scavenger_baseline.json."""
        raise NotImplementedError('TODO: implement')

    def permanence(self):
        """S13: the checks that keep this system running must themselves stay installed, enabled, unchanged and recent."""
        raise NotImplementedError('TODO: implement')

    def rule_coverage(self):
        """S14: verify the verifier. Every rule id this file can emit must be exercised by name in its test file."""
        raise NotImplementedError('TODO: implement')

    def run_all(self):
        raise NotImplementedError('TODO: implement')

def digest(findings):
    raise NotImplementedError('TODO: implement')

def report(findings, root=...):
    raise NotImplementedError('TODO: implement')

def repair(root=..., run=..., now=None, clock=...):
    """Use a 180s repair deadline with a 30s rescan reserve; checkpoint every action.

    The unit has a 300s outer deadline. Source scans remain observations, never
    evidence that a timed-out repair completed. Full-history audits are explicit work.
    """
    raise NotImplementedError('TODO: implement')

def update_baseline(root=..., allow_grow=False, run=..., prune=False):
    """Write data/scavenger_baseline.json. It may only shrink: an entry not already in it is refused unless allow_grow."""
    raise NotImplementedError('TODO: implement')

def queue_waypoints(findings, root=...):
    """One bounded Waypoint stage per rule group: Forge repairs, Probe re-runs this scan. Never starts a worker."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
