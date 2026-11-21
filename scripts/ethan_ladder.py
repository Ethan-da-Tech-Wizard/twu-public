# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Step ladder: turn ONE self-improve bank task into an ordered ladder of single-behaviour rungs.

The local 7B model fails whole build tasks but passes when the work is cut into tiny steps. A rung is one
instruction, a prompt naming the exact file and the ONE behaviour to add, and a partial verifier (a python
snippet run exactly like the bank's hidden verifier). A rung passes only if its own check passes AND every earlier
passed rung still passes (regression check).

Rungs come from (in order): the task's hand-written `ladder` field, else the verifier's boolean checks
(`c=[a, b]` / `c.append(x)` / `ok = a and b` / `sys.exit(0 if a and b else ..)` are split one check per rung),
preceded by a "skeleton" rung when the task asks for a new .py file. Step text supplies the wording.

`ladder` override: list of {"id", "instruction", "file", "behaviour", "verifier"} (verifier = python source, exit 0 = pass).

  ethan_ladder.py plan [ID ...] [--json]     print the rungs
  ethan_ladder.py validate [ID ...]          reference passes every rung cumulatively, untouched workdir fails rung 1
  run_ladder(task, attempt_fn, max_attempts_per_rung=4)   the driver (attempt_fn(prompt, workdir) -> transcript)

An error never ends a run: a raising attempt_fn counts as a failed attempt, a rung that exhausts its budget is recorded
and the ladder moves on; the result reports partial credit. Everything is appended to data/self_improve/ladder/<task>.jsonl.
No model, server or bridge is contacted by this module; the injected attempt_fn does that.
"""
import argparse, ast, difflib, hashlib, json, re, sys, tempfile, time
from pathlib import Path
import ethan_si_bank as bank

def _clauses(text):
    """Split a sentence on requirement boundaries (; and commas / 'and' outside parentheses)."""
    raise NotImplementedError('TODO: implement')

def _tokens(text):
    raise NotImplementedError('TODO: implement')

def _best_clause(task, check_text):
    raise NotImplementedError('TODO: implement')

def _flatten_and(node, assigns):
    raise NotImplementedError('TODO: implement')

def split_checks(source):
    """(items, skip_idx) where items = [('stmt', node) | ('check', expr_node)] in source order, or (None, None)
    when the verifier has no splittable boolean structure. Check nodes replace the statements that held them."""
    raise NotImplementedError('TODO: implement')

def _is_exit(st):
    raise NotImplementedError('TODO: implement')

def _check_script(items, idx):
    """Verifier source that runs every statement before check #idx (in order) then asserts only that check."""
    raise NotImplementedError('TODO: implement')

def _assert_lines(expr):
    raise NotImplementedError('TODO: implement')

def _check_text(items, idx):
    raise NotImplementedError('TODO: implement')

def _new_py_files(task):
    raise NotImplementedError('TODO: implement')

def _func_names(task, fname):
    raise NotImplementedError('TODO: implement')

def _signature(task, fname, func):
    raise NotImplementedError('TODO: implement')

def _skeleton_rung(task, fname):
    raise NotImplementedError('TODO: implement')

def derive_rungs(task):
    """Ordered rungs for a task: hand-written `ladder`, else derived from the verifier + steps."""
    raise NotImplementedError('TODO: implement')

def verify_rung(task, workdir, rung):
    """(passed, message) for one rung's own verifier (protected files checked first, like the bank)."""
    raise NotImplementedError('TODO: implement')

def verify_cumulative(task, workdir, rungs, upto=None, only=None):
    """Check rungs[:upto] (or only the given ids). (ok, failing_rung_id, message)."""
    raise NotImplementedError('TODO: implement')

def validate_task(task):
    """Problems list: reference must pass every rung cumulatively; untouched workdir must fail rung 1."""
    raise NotImplementedError('TODO: implement')

def _read(path, limit=...):
    raise NotImplementedError('TODO: implement')

def snapshot(workdir):
    raise NotImplementedError('TODO: implement')

def diff_text(before, after):
    raise NotImplementedError('TODO: implement')

def first_prompt(task, rung, idx, total, workdir):
    raise NotImplementedError('TODO: implement')

def corrective_prompt(task, rung, idx, total, workdir, attempt, failure, prev_diff, regression=None):
    raise NotImplementedError('TODO: implement')

def _log(path, rec):
    raise NotImplementedError('TODO: implement')

def _restore_protected(task, workdir):
    raise NotImplementedError('TODO: implement')

def run_ladder(task, attempt_fn, max_attempts_per_rung=4, workdir=None, out_dir=None, rungs=None):
    """Drive a task up its ladder. attempt_fn(prompt, workdir) -> transcript (str). Returns a result dict:
    {task, rungs:[{id, passed, attempts}], passed, total, partial_credit, full_pass, workdir, log}."""
    raise NotImplementedError('TODO: implement')

def _select(ids, directory):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
