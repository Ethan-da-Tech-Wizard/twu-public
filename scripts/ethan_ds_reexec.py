# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Independent re-execution (readiness criterion R3) of execution-verified Ethan training rows.

WRITTEN INDEPENDENTLY of the generators (ethan_ds_lang_*.py, ethan_ds_web.py, ...) and of their verifiers. What is reused, exactly:
  * scripts/ethan_lang_verify.py (Magi 11): the bwrap example_host layer only (bwrap_works, _spec, _exec). No generator code is imported,
    no fixture-building function, no hidden harness, no checker. All replay and judgement logic below is new.
Everything else (row parsing, workspace reconstruction, edit application, claim detection, per-source checks) is this file.

Rule of honesty: a row is only counted `pass` when the chosen trajectory was actually replayed from material INSIDE THE ROW and the
re-computed outcome agrees with what the row claims. If the row lacks the initial workspace / hidden harness / stub tools the status is
UNREPLAYABLE (with the reason); that is a finding (the row has no receipt), never a pass. example_host missing => never PASS.

Statuses per row: PASS, FAIL, UNREPLAYABLE, TIMEOUT. (example_host_UNAVAILABLE is reported as UNREPLAYABLE with reason example_host_unavailable.)
Extra evidence that does NOT count as pass: `partial` (e.g. standalone rustc --test of a self-contained written module) and
`consistency` (replace/write receipts and claim-vs-tool-result agreement reconstructed from the row's own tool results).

  nice -n 19 python3 scripts/ethan_ds_reexec.py --root . [--sources a,b] [--seed 20261116]
"""
from __future__ import annotations
import argparse
import hashlib
import html.parser
import json
import math
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile
import time
import ethan_lang_verify as LV

class example_host:
    """Thin wrapper over ethan_lang_verify's bwrap layer. Never runs unexample_hosted."""

    def __init__(self):
        raise NotImplementedError('TODO: implement')

    def available(self):
        raise NotImplementedError('TODO: implement')

    def spec(self, lang=...):
        raise NotImplementedError('TODO: implement')

    def run(self, lang, argv, work, timeout=..., mem_mb=2048):
        """-> (rc|None, out, err, timed_out). Raises RuntimeError('example_host_unavailable') rather than run unexample_hosted."""
        raise NotImplementedError('TODO: implement')

def tool_versions():
    raise NotImplementedError('TODO: implement')

def read_jsonl(path):
    raise NotImplementedError('TODO: implement')

def unjson(x):
    raise NotImplementedError('TODO: implement')

def norm_calls(msgs):
    """Flat list of {name,args,out} from a messages list (supports flat and OpenAI-function tool_call shapes)."""
    raise NotImplementedError('TODO: implement')

def final_text(msgs):
    raise NotImplementedError('TODO: implement')

def rc_of(out):
    """Exit status shown in a recorded shell tool result (None = looks successful)."""
    raise NotImplementedError('TODO: implement')

def strip_prefix(path):
    raise NotImplementedError('TODO: implement')

def safe_rel(p):
    raise NotImplementedError('TODO: implement')

def write_tree(root, files):
    raise NotImplementedError('TODO: implement')

def tree_hash(root):
    raise NotImplementedError('TODO: implement')

def res(status, reason, **kw):
    raise NotImplementedError('TODO: implement')

def sample_rows(dev, train, seed, name):
    """All dev rows + 10% of train (min 25, cap 300 total per source). Deterministic by (seed, source name, row id order)."""
    raise NotImplementedError('TODO: implement')

class Ws:
    """Workspace as reconstructed ONLY from the row's own tool results."""

    def __init__(self):
        raise NotImplementedError('TODO: implement')

def _excerpt_ok(out, new_text):
    """Tool result after an edit shows 'Here is the updated code:' + snippet(s) joined by '...'; each chunk must be in the new file."""
    raise NotImplementedError('TODO: implement')

def reconstruct(calls):
    raise NotImplementedError('TODO: implement')

def claim_backed(calls, final):
    """Independent claim check: a build/test-pass claim needs a successful shell tool result after the last edit."""
    raise NotImplementedError('TODO: implement')

class _Bal(html.parser.HTMLParser):

    def __init__(self):
        raise NotImplementedError('TODO: implement')

    def handle_starttag(self, tag, attrs):
        raise NotImplementedError('TODO: implement')

    def handle_endtag(self, tag):
        raise NotImplementedError('TODO: implement')

def check_text_file(path, text, tmpwork):
    """Independent structural check of an edited file. -> ('ok'|'bad'|'none', reason)."""
    raise NotImplementedError('TODO: implement')

def rust_standalone(ws, tmpwork):
    """Partial evidence only: compile+run `rustc --test` on each written *.rs that is self-contained (no crate::/super::/mod/use of siblings)."""
    raise NotImplementedError('TODO: implement')

def rejected_check(row, calls_prefix_final):
    """Static confirmation that the `rejected` side violates what it is said to violate. -> (status, reason). Never a pass of the row."""
    raise NotImplementedError('TODO: implement')

def _common_prefix_len(a, tail):
    raise NotImplementedError('TODO: implement')

def _strip_train(m):
    raise NotImplementedError('TODO: implement')

def replay_lang(row, src, tmpwork):
    raise NotImplementedError('TODO: implement')

def cmd_of(call):
    raise NotImplementedError('TODO: implement')

def setup_fixture(work, fx):
    raise NotImplementedError('TODO: implement')

def replayable_reason(row, calls_list):
    raise NotImplementedError('TODO: implement')

def apply_dict_call(work, c):
    """write_file / replace / read_file as dict calls against the fixture tree. -> None ok, else error string."""
    raise NotImplementedError('TODO: implement')

def run_calls(work, calls_list, observed_prefix_ok=True):
    """Run chosen calls in the example_host; -> list of dicts(cmd, rc, out) or raises."""
    raise NotImplementedError('TODO: implement')

def _norm(s):
    raise NotImplementedError('TODO: implement')

def _obs(o):
    raise NotImplementedError('TODO: implement')

def _classify_mismatch(cmd, rec, got):
    """-> 'fail' | 'unreplayable:<why>' for a recorded-vs-replayed output difference."""
    raise NotImplementedError('TODO: implement')

def tool_outputs(msgs):
    raise NotImplementedError('TODO: implement')

def eval_checks(check, final, observed, calls_cmds, work_before, work_after, fx):
    """Independent re-implementation of a SUBSET of the check ops. -> (failures, implemented, unimplemented)."""
    raise NotImplementedError('TODO: implement')

def replay_fixture(row, src, tmpwork):
    raise NotImplementedError('TODO: implement')

def replay_shell(row, src, tmpwork):
    raise NotImplementedError('TODO: implement')

def replay_pairs_web(row, src, tmpwork):
    raise NotImplementedError('TODO: implement')

def run_row(kind, row, src, tmpwork):
    raise NotImplementedError('TODO: implement')

def exec_rows(rows):
    raise NotImplementedError('TODO: implement')

def load_source(root, spec):
    raise NotImplementedError('TODO: implement')

def run_source(root, name, seed, tmpwork, failures_fh, max_seconds=None):
    raise NotImplementedError('TODO: implement')

def source_notes(name, st):
    raise NotImplementedError('TODO: implement')

def build_report(results, seed, versions, extra_sources=None):
    raise NotImplementedError('TODO: implement')

def write_md(rep, path):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
