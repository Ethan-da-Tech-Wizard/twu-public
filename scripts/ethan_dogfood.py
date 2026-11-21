# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Dogfood harness: the real Ethan CLI performs the workspace split sub-tasks inside a example_host COPY; deterministic checkers score it.

Nothing here is model-judged. Every task has (1) a fixture builder, (2) a prompt, (3) a gold tool sequence, (4) a checker that looks at
the example_host tree / file hashes / the split verifier / the final text for values recomputed from the files. The gold sequence is executed
on a fresh fixture in the tests and must pass its own checker, so a checker can never reward a wrong answer or reject the right one.

On any failure a record goes to data/dogfood/failures.jsonl (task, prompt, tool calls, error class, the verified correct answer, a
candidate harness fix). `pairs` renders each failure as a verified training pair with the SLIM prompt (ethan_cli_real_slim); local only,
secrets scrubbed. Nothing is trained or served from here.

  python3 scripts/ethan_dogfood.py list
  python3 scripts/ethan_dogfood.py stub [--mode good|printed|gaveup|unsafe|wrongtool|ignored|hallucinate|denied]   # no model, no GPU
  python3 scripts/ethan_dogfood.py run [--tasks id,id] --really-run     # real CLI through the configured local model and bridge; not during GPU windows
  python3 scripts/ethan_dogfood.py pairs        # failures.jsonl -> data/dogfood/pairs.jsonl (slim format)
  python3 scripts/ethan_dogfood.py fixes        # candidate harness fix list from the failure classes
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path
import ethan_split_plan as sp

def work_helper_source() -> str:
    raise NotImplementedError('TODO: implement')

def build_work_fixture(root: Path):
    raise NotImplementedError('TODO: implement')

def build_fixture(root: Path, with_manifest: bool=False, work_contract: bool=False) -> Path:
    raise NotImplementedError('TODO: implement')

def sp_run(root: Path, *args) -> subprocess.CompletedProcess:
    raise NotImplementedError('TODO: implement')

def tree_hashes(root: Path, sub: str=...) -> dict:
    raise NotImplementedError('TODO: implement')

def norm(s: str) -> str:
    raise NotImplementedError('TODO: implement')

def has_all(text: str, *vals) -> bool:
    raise NotImplementedError('TODO: implement')

def manifest(root: Path) -> dict:
    raise NotImplementedError('TODO: implement')

def classes_of(root: Path) -> dict:
    raise NotImplementedError('TODO: implement')

def task(id, level, prompt, gold, check, answer, tools=..., manifest_needed=False, forbid_cmds=..., work_contract=False):
    raise NotImplementedError('TODO: implement')

def sh(cmd):
    raise NotImplementedError('TODO: implement')

def top_dirs(root):
    raise NotImplementedError('TODO: implement')

def ro_unchanged(root, ctx):
    raise NotImplementedError('TODO: implement')

def cls_task(id, rel, level=2):
    raise NotImplementedError('TODO: implement')

def gi_check(r, c):
    raise NotImplementedError('TODO: implement')

def readme_check(r, c):
    raise NotImplementedError('TODO: implement')

def header_check(r, c):
    raise NotImplementedError('TODO: implement')

def move_check(r, c):
    raise NotImplementedError('TODO: implement')

def sc(sub):
    raise NotImplementedError('TODO: implement')

def counts_wo_out(r):
    raise NotImplementedError('TODO: implement')

def work(r):
    raise NotImplementedError('TODO: implement')

def split_ok(r, c):
    """Common safety gate: no original changed, and nothing outside out/ was written."""
    raise NotImplementedError('TODO: implement')

def status_check(r, c):
    raise NotImplementedError('TODO: implement')

def plan_check(r, c):
    raise NotImplementedError('TODO: implement')

def ro_unchanged_originals(r, c):
    raise NotImplementedError('TODO: implement')

def redact_check(r, c):
    raise NotImplementedError('TODO: implement')

def refuse_check(r, c):
    raise NotImplementedError('TODO: implement')

def has_any(text, *vals):
    raise NotImplementedError('TODO: implement')

def copycode_check(r, c):
    raise NotImplementedError('TODO: implement')

def copyvault_check(r, c):
    raise NotImplementedError('TODO: implement')

def verify_check(r, c):
    raise NotImplementedError('TODO: implement')

def report_check(r, c):
    raise NotImplementedError('TODO: implement')

def chain_check(r, c):
    raise NotImplementedError('TODO: implement')

def work_contract_check(root, ctx):
    """Native evidence plus a separate immutable oracle; prose alone never passes."""
    raise NotImplementedError('TODO: implement')

def parse_transcript(text: str) -> dict:
    """Normalize gemini stream-json (or any list of dict events) into calls, results and final text. Tolerant of shape drift."""
    raise NotImplementedError('TODO: implement')

def recover_missing_results(parsed: dict, root: Path) -> dict:
    raise NotImplementedError('TODO: implement')

def escapes(call: dict, root: Path) -> bool:
    raise NotImplementedError('TODO: implement')

def classify_failure(t: dict, parsed: dict, root: Path, before: dict) -> str:
    raise NotImplementedError('TODO: implement')

def scrub(s: str) -> str:
    raise NotImplementedError('TODO: implement')

def scrub_obj(o):
    raise NotImplementedError('TODO: implement')

class StubRunner:
    """No model. Plays the gold sequence (mode good) or a scripted failure so the harness can be dry-run end to end."""

    def __init__(self, mode=...):
        raise NotImplementedError('TODO: implement')

    def run(self, t, root: Path) -> str:
        raise NotImplementedError('TODO: implement')

def jline(type_, **kw):
    raise NotImplementedError('TODO: implement')

def fill_gold(args, root: Path):
    """Substitute $ROOT and the $CODE/$PRIVATE/$REVIEW counts (recomputed from the files, never typed in) into a gold step's arguments."""
    raise NotImplementedError('TODO: implement')

def execute_tool(name, args, root: Path) -> str:
    """Execute a gold step inside the example_host (only gold steps authored here run through this)."""
    raise NotImplementedError('TODO: implement')

def example_host_policy_toml(example_host: Path) -> str:
    """Caller-tier policy appended to the acceptance read-only policy for ONE example_host directory. Production policy is untouched: the
    launcher still builds its admin deny snapshot from scripts/ethan_gemini_policy.toml, and admin denies beat these allows (they already
    forbid redirection, `;`, substitution, absolute python script paths, absolute `cd`, rm, ...).
    Valid only when the CLI's cwd IS the example_host (scripts/ethan honors ETHAN_DOGFOOD_CWD under ETHAN_WITNESS=1): relative paths then
    resolve inside it. Allows (a) write_file/replace whose file_path is relative or under the example_host, with no '..', and (b) closed shell
    shapes: `python3 scripts/ethan_split_plan.py classify|copy|verify`, mkdir -p, mv, cp, read-only viewers, up to three joined with ` && `
    (optionally `| head -N` / `| wc -l`), and `sed -i 'expr' file`. Every absolute path must start with the example_host; no `..`, `$`, backtick,
    `;`, backslash. The Gemini loader rejects patterns >2048 chars or with a repeated group, so each shape is built from lookaheads."""
    raise NotImplementedError('TODO: implement')

def work_contract_policy(example_host: Path) -> str:
    raise NotImplementedError('TODO: implement')

class RealRunner:
    """Runs scripts/ethan chat -p (stream-json) through the production bridge inside bwrap (ethan_cli_acceptance.CliRunner) with the
    example_host bound READ-WRITE at example_host_VISIBLE (under /tmp: the production policy only lets write tools target TWU_LLC or /tmp) and used
    as the CLI's cwd (ETHAN_DOGFOOD_CWD, honored by scripts/ethan only under ETHAN_WITNESS=1). The caller policy is the acceptance
    read-only policy plus example_host_policy_toml; production admin denies still apply. Needs the model server and bridge up; the
    entrypoint refuses unless --really-run is given."""

    def __init__(self, evidence: Path | None=None):
        raise NotImplementedError('TODO: implement')

    def run(self, t, root: Path) -> str:
        raise NotImplementedError('TODO: implement')

def run_gold(t: dict, tmp: Path):
    """Execute the task's gold steps in a fresh fixture and run its own checker on the result: (root, calls, outputs, answer, verified)."""
    raise NotImplementedError('TODO: implement')

def score_task(t: dict, runner, work_parent: Path | None=None) -> dict:
    raise NotImplementedError('TODO: implement')

def run_all(runner, ids=None, work_parent=None, out_dir: Path=..., write=True) -> dict:
    raise NotImplementedError('TODO: implement')

def run_session(runner, ids, label: str, out_dir: Path=..., session_max: int=..., pause: float=25, cool_wait: float=900, guard=None, cool_ok=None, sleep=None, work_parent: Path | None=None, fresh: bool=False) -> dict:
    """At most `session_max` tasks, thermal-guarded, resumable: a task counts as done for this `label` once scored (pass or fail). A hot GPU/CPU
    before a task waits up to cool_wait for cooling; a latch, no cooling, or a mid-task abort stops the session WITHOUT scoring that task, so
    re-running the same command resumes at it. Failures are appended to failures.jsonl with the label."""
    raise NotImplementedError('TODO: implement')

def real_session(ids, label, session_max=..., pause=25, fresh=False) -> dict:
    """Real CLI with canonical preflight/thermal guards; preserve the owner's power profile."""
    raise NotImplementedError('TODO: implement')

def failure_to_rows(rec: dict, level: int=2) -> list:
    """One verified pair per model turn, rendered with the slim prompt. Only for failures whose gold passed its own checker."""
    raise NotImplementedError('TODO: implement')

def refresh_gold(rec: dict) -> dict:
    raise NotImplementedError('TODO: implement')

def cmd_pairs(a) -> int:
    """One verified pair set per failed TASK (the gold answer does not depend on how the model failed); every error class seen for the task
    is recorded on its rows. Latest failure record per task supplies the prompt text."""
    raise NotImplementedError('TODO: implement')

def cmd_fixes(a) -> int:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
