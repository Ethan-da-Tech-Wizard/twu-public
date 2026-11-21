# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Deterministic dataset READINESS evaluator for the single sealed Ethan LoRA training dataset.

  python3 scripts/ethan_ds_readiness.py evaluate [--token-cap N]   evaluate R1..R10, write data/registry/readiness_report.{json,md}, print a table
  python3 scripts/ethan_ds_readiness.py rollcall add --seat N --host H --verdict ACK|BLOCKER --build-sha SHA --criteria R1,R2 --note TEXT [--role attester|producer]
  python3 scripts/ethan_ds_readiness.py rollcall show        latest verdict per seat, matching hashes, blockers, chain integrity
  python3 scripts/ethan_ds_readiness.py ready                exit 0 only if evaluate is READY, every required seat ACK'd the same build sha, and every
                                                             criterion has an attester ACK from a seat other than its producer(s)

Statuses: PASS / FAIL / UNKNOWN / NEEDS_ETHAN. UNKNOWN is never PASS. Overall READY only if all ten are PASS.
Read-only on every data source; the only writes are under data/registry/ (readiness_report.json/.md, readiness_ledger.jsonl).
No model, no service, no network. Matches of secrets/paths are never printed.

R1 binds to the FROZEN manifest hash of Magi 6's freeze checker (ethan_ds_freeze_readiness.py: sha256 of <build>/manifest.json, read here
from the same file; not imported). Host ACKs for R1 must carry that hash. Other ACKs may carry it or the BUILD_SHA below.

Canonical build sha ("BUILD_SHA"): sha256 over the lines "<name>:<file sha256>\\n" for sft_train, dpo_train, sft_dev, heldout
(in that order; heldout = eval_heldout_families.jsonl), i.e. one value that pins all four files at once.
Ledger: append-only JSONL, each entry carries prev_hash and hash = sha256(prev_hash + canonical json of the entry without 'hash').
Truncating the tail is not detectable from the file alone; the report records the ledger head hash so a later run can compare.
"""
import argparse
import fcntl
import hashlib
import importlib.util
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

def sha256_bytes(b):
    raise NotImplementedError('TODO: implement')

def sha256_file(p):
    raise NotImplementedError('TODO: implement')

def canon(o):
    raise NotImplementedError('TODO: implement')

def read_jsonl(path):
    """Yield (row_dict_or_None, lineno). Bad lines yield None (counted by callers)."""
    raise NotImplementedError('TODO: implement')

def load_json(path):
    raise NotImplementedError('TODO: implement')

def res(cid, status, reason, evidence=None):
    raise NotImplementedError('TODO: implement')

def unjson(v):
    raise NotImplementedError('TODO: implement')

def vclass(row):
    """execution | fixture | regex | template | none. Reuses the registry's heuristic.v1 classifier (read-only import) when possible."""
    raise NotImplementedError('TODO: implement')

def _tokens(s):
    raise NotImplementedError('TODO: implement')

def row_messages(r):
    raise NotImplementedError('TODO: implement')

def classify_row(r):
    """-> (language, domains:set, kinds:set, basis). language in TIER1 | 'web_other' | 'other_lang' | 'macos' | 'domain_only' | 'unclassified'."""
    raise NotImplementedError('TODO: implement')

def skeleton_hash(text):
    raise NotImplementedError('TODO: implement')

def task_key(r):
    """Identity of the UNDERLYING task (bank entry / seed / family), not the row. Order: task, template_id, seed, family(+skill), prompt skeleton."""
    raise NotImplementedError('TODO: implement')

def coverage(rows_iter):
    """Count execution-verified rows per language / domain / kind. -> dict."""
    raise NotImplementedError('TODO: implement')

class Ledger:

    def __init__(self, path):
        raise NotImplementedError('TODO: implement')

    @staticmethod
    def entry_hash(prev, body):
        raise NotImplementedError('TODO: implement')

    def load(self):
        """-> (entries, problems). Non-empty problems => tamper/corruption (never silently skipped)."""
        raise NotImplementedError('TODO: implement')

    def head(self):
        raise NotImplementedError('TODO: implement')

    def add(self, seat, host, verdict, build_sha, criteria, note, ts=None, role=...):
        """Validate and append. Raises ValueError on invalid input or if the existing chain is broken."""
        raise NotImplementedError('TODO: implement')

    def summary(self, local_sha=None, required=..., extra_ok=...):
        raise NotImplementedError('TODO: implement')

def ack_covers(entry, crit):
    raise NotImplementedError('TODO: implement')

class Ctx:

    def __init__(self, root, token_cap=..., build_rel=...):
        raise NotImplementedError('TODO: implement')

    def frozen(self):
        """-> dict. Magi 6's freeze hash = sha256(<build>/manifest.json) (same file ethan_ds_freeze_readiness.Ctx reads). A recorded hash in a
        freeze receipt (<build>/../freeze/*.json with build_manifest_sha256) is the frozen value if present; a live!=recorded difference is a mismatch."""
        raise NotImplementedError('TODO: implement')

    def build_sha(self):
        raise NotImplementedError('TODO: implement')

    def train_rows(self):
        raise NotImplementedError('TODO: implement')

    def entries(self):
        raise NotImplementedError('TODO: implement')

    def rel(self, p):
        raise NotImplementedError('TODO: implement')

def r1(c):
    raise NotImplementedError('TODO: implement')

def build_inputs(c):
    raise NotImplementedError('TODO: implement')

def eval_only_ids(c):
    """(entry ids / file stems of EVAL-role registry sources, ids inside external eval files). The build's own heldout/dev are excluded
    (same-id derived copies are handled by R4)."""
    raise NotImplementedError('TODO: implement')

def privacy_exclusions(c):
    """Train rows that must not be trained on: containing /home/user paths, or sourced from an eval-only set. Counts and ids only."""
    raise NotImplementedError('TODO: implement')

def r2(c):
    raise NotImplementedError('TODO: implement')

def verifier_unverified(v):
    """True if a verifier dict claims a pass/exit that is not trustworthy: timeout, signal, exit 134, killed, or 'caught' text."""
    raise NotImplementedError('TODO: implement')

def unverified_scan(c, rep):
    """Fail-closed count of results that are NOT verified: reexec_report timeouts/signals + source/build rows whose verifier says timeout/signal/134/killed/caught."""
    raise NotImplementedError('TODO: implement')

def r3(c):
    raise NotImplementedError('TODO: implement')

def prompt_text(r):
    raise NotImplementedError('TODO: implement')

def norm_tokens(s):
    raise NotImplementedError('TODO: implement')

def r4(c):
    raise NotImplementedError('TODO: implement')

def source_pool(c):
    """Informational: id-deduplicated execution-verified rows in the SOURCE pools under the build's parent dir."""
    raise NotImplementedError('TODO: implement')

def r5(c):
    raise NotImplementedError('TODO: implement')

def find_tokenizer():
    raise NotImplementedError('TODO: implement')

def r6(c):
    raise NotImplementedError('TODO: implement')

def r7(c):
    raise NotImplementedError('TODO: implement')

def r8(c):
    raise NotImplementedError('TODO: implement')

def r9(c):
    raise NotImplementedError('TODO: implement')

def r10(c):
    raise NotImplementedError('TODO: implement')

def producers(c):
    """-> (seats:set, unknown:list). Producer seats = owners of the existing build-input registry entries (or PRODUCER_OVERRIDE). Unknown => cannot attest."""
    raise NotImplementedError('TODO: implement')

def attestation(c, local_sha=None, frozen_sha=None):
    """Per criterion: is there an ACK (role attester, covering the criterion, valid sha) from a named attester seat that is not a producer?"""
    raise NotImplementedError('TODO: implement')

def evaluate(c):
    raise NotImplementedError('TODO: implement')

def table(rep):
    raise NotImplementedError('TODO: implement')

def to_md(rep):
    raise NotImplementedError('TODO: implement')

def write_reports(c, rep):
    raise NotImplementedError('TODO: implement')

def show(c, out):
    raise NotImplementedError('TODO: implement')

def main(argv=None, out=None):
    raise NotImplementedError('TODO: implement')
