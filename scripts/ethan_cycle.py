# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Deterministic self-improvement cycle orchestrator for Ethan's local model (PLAN + receipts only).

  ethan_cycle.py plan   [--cycle-id ID] [eval/acceptance options]   run/resume stages 1-7 as far as the evidence allows
  ethan_cycle.py status [--cycle-id ID]                              stage table, chain head, promotion-blocked report
  ethan_cycle.py verify [--cycle-id ID]                              re-hash every receipt + inputs, check order and chain

Stages (strict order, each receipt embeds the sha256 of the previous receipt file = tamper-evident chain):
  1 freeze  2 data_gate  3 train_plan  4 eval_plan  5 gate  6 promote_plan  7 rollback_receipt

HARD RULES (AGENTS.md E4/E15/E17/E20): refuses under business/example_host/comms/STOP; makes NO model call, starts NO GPU
work, imports no torch, never launches llama-server or training; it only PRINTS the train/eval/promote commands.
MODEL_STANDBY does not block planning or verifying, it is only reported as "promotion blocked". This tool never
removes a latch and never applies a promotion: approval (scripts/ethan_approve.py) is Ethan's terminal step.

Receipts: data/autoimprove/cycle/<cycle-id>/NN_<stage>.json. Magi logging: append-only data/autoimprove/cycle/magi_events.jsonl
(a non-seat event journal, source "ethan_cycle", seat null). It never writes a seat outbox/ping and never claims attendance.
"""
import argparse, glob, hashlib, json, math, os, re, socket, sys, time
from pathlib import Path

class Refused(Exception):
    pass

def sha_bytes(b):
    raise NotImplementedError('TODO: implement')

def sha_file(p):
    raise NotImplementedError('TODO: implement')

def canon(o):
    raise NotImplementedError('TODO: implement')

def now():
    raise NotImplementedError('TODO: implement')

def who():
    raise NotImplementedError('TODO: implement')

def latches(root):
    raise NotImplementedError('TODO: implement')

def require_no_stop(root):
    raise NotImplementedError('TODO: implement')

def hash_inputs(root, paths):
    raise NotImplementedError('TODO: implement')

def cycle_dir(root, cid):
    raise NotImplementedError('TODO: implement')

def receipt_path(root, cid, idx):
    raise NotImplementedError('TODO: implement')

def load_chain(root, cid):
    """Return list of (idx, path, doc) for existing receipts in order of stage index."""
    raise NotImplementedError('TODO: implement')

def body_hash(doc):
    raise NotImplementedError('TODO: implement')

def write_receipt(root, cid, idx, status, data, inputs, prev_sha, events=True):
    raise NotImplementedError('TODO: implement')

def magi_event(root, cid, stage, status, receipt_sha):
    """Non-seat, append-only stage-transition journal. No seat, no outbox, no attendance claim."""
    raise NotImplementedError('TODO: implement')

def verify_chain(root, cid):
    """Returns (ok, problems list, stages_present)."""
    raise NotImplementedError('TODO: implement')

def write_head(root, cid):
    raise NotImplementedError('TODO: implement')

def read_temps():
    raise NotImplementedError('TODO: implement')

def stage_freeze(root, cfg):
    raise NotImplementedError('TODO: implement')

def row_keys(row):
    raise NotImplementedError('TODO: implement')

def read_jsonl(p):
    raise NotImplementedError('TODO: implement')

def check_overlap_and_verifier(train_paths, holdout_paths):
    raise NotImplementedError('TODO: implement')

def manifest_gate(man):
    raise NotImplementedError('TODO: implement')

def stage_data_gate(root, cfg):
    raise NotImplementedError('TODO: implement')

def stage_train_plan(root, cfg):
    raise NotImplementedError('TODO: implement')

def stage_eval_plan(root, cfg):
    raise NotImplementedError('TODO: implement')

def _sum(res, sets, field):
    raise NotImplementedError('TODO: implement')

def _rate(res, sets):
    raise NotImplementedError('TODO: implement')

def parse_pn(v):
    raise NotImplementedError('TODO: implement')

def is_sha(v):
    raise NotImplementedError('TODO: implement')

def bypass_wrong(res, suite_sha=None):
    """Complete run receipt required: same suite sha as the pinned suite, n == 145, all 145 rows, both lists consistent."""
    raise NotImplementedError('TODO: implement')

def validate_eval(res, required, trusted_ids=None, expect_sha=None, role=None):
    """Check complete item-level evidence and consistency with its summary.

    A receipt describes an execution; it is not authentication of who ran it.
    """
    raise NotImplementedError('TODO: implement')

def evaluate_gate(cand, cand_base, prod, bypass_cand, acceptance, acceptance_baseline, margin=..., primary=..., heldout=..., bypass_baseline=..., trusted_ids=None, pins=None, bypass_suite_sha=None):
    """Pure, deterministic. Returns {"verdict": "PASS"|"FAIL", "checks": {...}, "reasons": [...]}. Missing evidence fails."""
    raise NotImplementedError('TODO: implement')

def load_json(root, p):
    raise NotImplementedError('TODO: implement')

def trusted_eval_ids(root, cid, cfg):
    """Item IDs per set from the eval manifest pinned in the freeze receipt; every file must still match its manifest hash."""
    raise NotImplementedError('TODO: implement')

def stage_gate(root, cfg):
    raise NotImplementedError('TODO: implement')

def stage_promote(root, cfg):
    raise NotImplementedError('TODO: implement')

def stage_rollback(root, cfg):
    raise NotImplementedError('TODO: implement')

def new_cycle_id():
    raise NotImplementedError('TODO: implement')

def latest_cycle(root):
    raise NotImplementedError('TODO: implement')

def plan(root, cid, cfg):
    raise NotImplementedError('TODO: implement')

def status_report(root, cid):
    raise NotImplementedError('TODO: implement')

def main(argv=None, root=...):
    raise NotImplementedError('TODO: implement')
