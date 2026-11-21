# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Turn hand-written task specs into execution-verified training rows (stdlib only, no model calls).

Usage: python3 scripts/ethan_lang_dataset.py [--specs-dir data/lang_tasks] [--out-dir DIR] [--dry-run]
       [--lang c,rust] [--ids a,b] [--jobs 1] [--family-cap 20] [--cell-cap 40] [--seed 1116]
Heavy runs (E17): ETHAN_HOST=1 ETHAN_CAP=6G scripts/ethan_capped_run.sh nice -n 15 python3 scripts/ethan_lang_dataset.py ...
Before every verification the CPU package temperature is read (`sensors`); above 96C the run pauses.

SPEC SCHEMA: one JSON file per task at <specs-dir>/<lang>/<id>.json (file stem == id, folder == lang):
  id            str   [A-Za-z0-9._-]+, unique
  lang          str   c | cpp | csharp | rust | go | js | python | bash
  task_type     str   impl | api | scaffold | bugfix | tests | buildfix
  family        str   family name for the per-family cap
  prompt        str   the user's request; may embed starter/broken code as fenced blocks
  assistant_answer str the assistant's full reply: short prose + fenced blocks whose info string carries
                      the file name:  ```c file=solution.c   (blocks without file= are prose examples, ignored)
  test_files    {name: text}  hidden harness, never shown to the model (may be {} only when kind == "run" or task_type == "tests")
  test_cmd      optional str|list  command run in the example_host instead of the language default
  kind          "test" | "run"
  expected_stdout optional str  exact stdout required
  broken_files  {name: text}  bugfix/buildfix: the broken state, which MUST FAIL with the same harness.
                      If omitted it is extracted from the PROMPT's fenced blocks that carry file=NAME.
  reference_files, mutant_files  {name: text}  required for task_type "tests": the assistant's answer files
                      (the tests) must PASS against reference_files and FAIL against mutant_files.
  source        must be "original";  license must be "TWU-internal";  notes  optional str
Files verified are ONLY those parsed from assistant_answer fences (plus test_files). An answer file that
has the same name as a test file / reference / mutant file is rejected (the answer may not touch the harness).

PIPELINE per spec: validate -> reject empty/duplicate (normalised) prompts, benchmark names, private
paths/emails/secrets (training-gate scan) -> extract -> verify must be PASS -> bugfix/buildfix broken must
FAIL; tests: reference PASS and mutant FAIL -> build ethan-system-pair.v1 row (verified_by=execution)
-> training gate classify, rejects dropped with reason -> caps (family 20, language x task_type 40;
deterministic order by sha256(seed|id)). UNAVAILABLE (missing toolchain) is reported separately and is never
counted as verified. Output: <out-dir>/<lang>.jsonl + manifest.json; refuses to overwrite; --dry-run writes
nothing. bash is not yet a verifier language: it runs through the python verifier with an explicit
`bash <script>` test_cmd (toolchain_version says so).
"""
from __future__ import annotations
import argparse
import concurrent.futures as cf
import datetime
import hashlib
import json
import os
import re
import socket
import subprocess
import sys
import time
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
import ethan_lang_verify as LV
import ethan_training_gate as GATE

def sha(b):
    raise NotImplementedError('TODO: implement')

def norm_prompt(s):
    raise NotImplementedError('TODO: implement')

def parse_fences(text):
    """Return [(lang, file_or_None, body)] for every fenced block (``` or ~~~; closing fence >= opening)."""
    raise NotImplementedError('TODO: implement')

def files_from_text(text):
    """{file: content} from fenced blocks carrying file=NAME. Raises ValueError on duplicate/unsafe names."""
    raise NotImplementedError('TODO: implement')

def _files_ok(v, key, allow_empty=False):
    raise NotImplementedError('TODO: implement')

def validate(spec):
    """Return error string or None."""
    raise NotImplementedError('TODO: implement')

def scan_private(spec):
    raise NotImplementedError('TODO: implement')

def package_temp():
    raise NotImplementedError('TODO: implement')

def wait_cool(limit=..., max_wait_s=900):
    raise NotImplementedError('TODO: implement')

def frame():
    """(system message, tools) exactly as ethan_system_pairs uses (single system prompt)."""
    raise NotImplementedError('TODO: implement')

def _bash_version():
    raise NotImplementedError('TODO: implement')

def run_verify(spec, files, timeout_s):
    """Verify files (already merged with the harness). bash goes through the python verifier with an
    explicit test_cmd unless the verifier gains native bash support."""
    raise NotImplementedError('TODO: implement')

def file_path_identity(name):
    """Conservative collision identity for relative fixture paths."""
    raise NotImplementedError('TODO: implement')

def check_file_paths(*maps):
    raise NotImplementedError('TODO: implement')

def merge(a, b, what, allow_identical=False):
    """Merge two file maps; a name that appears on both sides is a collision. Only when allow_identical is set (the GIVEN
    broken code shown in the prompt vs the hidden harness, e.g. a header both carry) may an identical name+content pair
    pass. The model's answer, the reference and the mutant must never share a name with the harness: role separation."""
    raise NotImplementedError('TODO: implement')

def classify_failure(r, trusted_files=...):
    """Is this verifier result a REAL failure of the code under test? -> ("CAUGHT"|"INCONCLUSIVE", why).
    CAUGHT only for status FAIL at stage test/compile whose reason is a plain nonzero exit ("exit code N",
    "build exit N", 1 <= N < 126) or the exact-stdout mismatch. Timeouts, signal kills, exit 126/127 (command not
    executable / not found = infrastructure), EVERY exit >= 128 (including 134 = abort(), whatever text was printed:
    glibc's assertion message can be forged by a candidate), verifier ERROR and UNAVAILABLE are INCONCLUSIVE.
    Test code must therefore report failures with a plain nonzero exit status, not assert()/abort().
    trusted_files is accepted for call compatibility and ignored. The verifier has no structured exit_code /
    timed_out / signal fields; this parses its `reason` string."""
    raise NotImplementedError('TODO: implement')

def process_spec(spec, timeout_s=30, verify_fn=None):
    """-> dict(status VERIFIED|REJECTED|UNAVAILABLE, reason, row?, toolchain)."""
    raise NotImplementedError('TODO: implement')

def build_row(spec, spec_sha, res, seed, gen_sha, date):
    raise NotImplementedError('TODO: implement')

def load_specs(specs_dir):
    """-> [(path, spec_or_None, raw_sha, load_error)] sorted by path."""
    raise NotImplementedError('TODO: implement')

def apply_caps(rows, seed, family_cap, cell_cap):
    raise NotImplementedError('TODO: implement')

def run(a, out=...):
    raise NotImplementedError('TODO: implement')

def write_outputs(a, kept, manifest, out):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
