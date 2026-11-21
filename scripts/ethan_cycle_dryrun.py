# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Dry-run-only improvement-cycle orchestrator (plan / preflight / run --dry-run / verify).

Stages: S0 preflight, S1 data, S2 train PLAN, S3 eval PLAN, S4 promote DRY-RUN plan, S5 feedback proposal.
Nothing here starts a model, server or trainer, changes a latch, or promotes. Live stages need Ethan's explicit
opt-in and are NOT implemented: `run` without --dry-run refuses. The only writes are under data/self_improve/cycle_dryrun/
(hash-chained <run>.jsonl, outbox/, proposals/, NEEDS_ETHAN note). Stage ends are reported to Magi (kind report) through
`scripts/magi.py send`, seat from --seat / ETHAN_CYCLE_SEAT, connection from --connection / ETHAN_CYCLE_CONN (passed to the
child by environment only, never logged); with no seat or on failure the packet goes to cycle/outbox/ instead.

  python3 scripts/ethan_cycle_dryrun.py plan | preflight | run --dry-run | verify RUN
"""
import argparse, ast, hashlib, json, os, random, re, shutil, subprocess, sys, time
from collections import Counter, defaultdict
from pathlib import Path

def sha_bytes(b):
    raise NotImplementedError('TODO: implement')

def sha_file(p):
    raise NotImplementedError('TODO: implement')

def canon(o):
    raise NotImplementedError('TODO: implement')

def res(stage, status, summary, **detail):
    """status: pass | warn | fail | skip | plan"""
    raise NotImplementedError('TODO: implement')

class Probes:

    def __init__(self, repo):
        raise NotImplementedError('TODO: implement')

    def temps(self):
        raise NotImplementedError('TODO: implement')

    def ram_gib(self):
        raise NotImplementedError('TODO: implement')

    def vram_free_mib(self):
        raise NotImplementedError('TODO: implement')

    def disk_free_gib(self, path):
        raise NotImplementedError('TODO: implement')

    def live_cli(self):
        """argv basenames of running Ethan/Gemini CLI sessions (read /proc only)."""
        raise NotImplementedError('TODO: implement')

    def hour(self):
        raise NotImplementedError('TODO: implement')

class Cycle:

    def __init__(self, repo=..., probes=None, sender=None, seat=None, conn=None, seed=...):
        raise NotImplementedError('TODO: implement')

    def latch_state(self):
        raise NotImplementedError('TODO: implement')

    def pin_files(self):
        raise NotImplementedError('TODO: implement')

    def make_run_id(self, mode):
        raise NotImplementedError('TODO: implement')

    def chain_path(self, run=None):
        raise NotImplementedError('TODO: implement')

    def append(self, stage_result, extra=None):
        raise NotImplementedError('TODO: implement')

    @staticmethod
    def verify_chain(path):
        raise NotImplementedError('TODO: implement')

    def _send_subprocess(self, argv, env):
        raise NotImplementedError('TODO: implement')

    def report(self, r):
        """One packet per stage end (skips and refusals included). Returns 'sent' | 'outbox'."""
        raise NotImplementedError('TODO: implement')

    def finish_stage(self, r):
        raise NotImplementedError('TODO: implement')

    def s0(self):
        raise NotImplementedError('TODO: implement')

    def s1(self):
        raise NotImplementedError('TODO: implement')

    def _lanes(self):
        raise NotImplementedError('TODO: implement')

    def s2(self):
        raise NotImplementedError('TODO: implement')

    def s3(self):
        raise NotImplementedError('TODO: implement')

    def s4(self, prior):
        raise NotImplementedError('TODO: implement')

    def s5(self):
        raise NotImplementedError('TODO: implement')

    def refuse_if_stopped(self):
        raise NotImplementedError('TODO: implement')

    def cmd_preflight(self):
        raise NotImplementedError('TODO: implement')

    def cmd_plan(self):
        raise NotImplementedError('TODO: implement')

    def cmd_run(self):
        raise NotImplementedError('TODO: implement')

def main(argv=None, cycle=None):
    raise NotImplementedError('TODO: implement')
