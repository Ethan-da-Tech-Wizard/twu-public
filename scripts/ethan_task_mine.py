# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Mine verified self-improvement tasks from our own scripts/*.py and their existing scripts/test_*.py.

A candidate is a pure, small, deterministic top-level function (ast: no I/O, no subprocess, no network, no global state,
3-40 lines, has a docstring or a descriptive name) that an existing unittest method calls and asserts on. For each one we write
a tiny self-contained work dir: the module reduced to the stdlib imports, literal constants and pure helper functions the
function needs, with the function body replaced by `raise NotImplementedError`, plus an extracted test file holding ONLY the
test methods that call it (copied verbatim, with the fixtures they need). The reference is the same reduced module with the
original body. The verifier runs the extracted test (stdlib unittest, no pytest) and prints PASS. Every task must pass the
bank's own `problems()` (reference passes, stub fails, deterministic, protected test untouched) or it is dropped.

Only our own repo code is mined (GPL-3.0-or-later release). Files and snippets that mention secrets, personal data or private
paths are skipped. No model call, no network, no repo code is executed outside the throwaway work dirs.

  ethan_task_mine.py mine [--scripts-dir DIR] [--out-dir data/self_improve/tasks_mined] [--limit N] [--no-validate]
  ethan_task_mine.py check [--out-dir DIR]   re-validate every mined task and the MANIFEST

Consume with the bank tools: `ethan_si_bank.py validate --task-dir data/self_improve/tasks_mined`, and the same --task-dir
on ethan_ladder.py, ethan_gold_trajectories.py build, ethan_si_loop.py and ethan_eval_ab.py run.
"""
import argparse, ast, builtins, collections, json, re, sys, time
from pathlib import Path
import ethan_si_bank as bank

def slug(text):
    raise NotImplementedError('TODO: implement')

def seg(src, node):
    raise NotImplementedError('TODO: implement')

def start_line(node):
    raise NotImplementedError('TODO: implement')

def lines_of(lines, node):
    raise NotImplementedError('TODO: implement')

def bound_names(imp):
    raise NotImplementedError('TODO: implement')

def is_docstring(node):
    raise NotImplementedError('TODO: implement')

def stored_names(fn):
    raise NotImplementedError('TODO: implement')

def loaded_names(node):
    raise NotImplementedError('TODO: implement')

class ModuleInfo:
    """Top-level facts about one script: importable stdlib names, immutable-ish constants, candidate-pure functions."""

    def __init__(self, src):
        raise NotImplementedError('TODO: implement')

    def _const_ok(self, v):
        raise NotImplementedError('TODO: implement')

    def deps_of(self, fn, seen=None):
        """Pure closure of fn: (imports, consts, helper functions), or None if impure/unresolvable."""
        raise NotImplementedError('TODO: implement')

def mutates(fn, name):
    raise NotImplementedError('TODO: implement')

def purity_problems(fn):
    raise NotImplementedError('TODO: implement')

def fn_lines(fn):
    raise NotImplementedError('TODO: implement')

def branching(fn):
    raise NotImplementedError('TODO: implement')

def difficulty(fn):
    raise NotImplementedError('TODO: implement')

def descriptive(fn):
    raise NotImplementedError('TODO: implement')

class TestInfo:

    def __init__(self, src, stem):
        raise NotImplementedError('TODO: implement')

    def methods_calling(self, func):
        """[(class node, method node)] for test methods that call `func` (bare name, or alias.func)."""
        raise NotImplementedError('TODO: implement')

def calls(node, func, aliases, from_names):
    raise NotImplementedError('TODO: implement')

def assertion_examples(ti, selected, func):
    """Specific statements from the selected tests that call or assert on the function, as natural-language examples."""
    raise NotImplementedError('TODO: implement')

def build_test_file(ti, exports, selected):
    """Standalone test module: only needed imports, referenced top-level helpers, and the selected methods verbatim."""
    raise NotImplementedError('TODO: implement')

def module_text(info, fn, deps, stub):
    raise NotImplementedError('TODO: implement')

def signature(info, fn):
    raise NotImplementedError('TODO: implement')

def verifier_source(test_name, n_tests):
    raise NotImplementedError('TODO: implement')

def make_task(module_stem, info, fn, deps, ti, selected, tests_text, rel):
    raise NotImplementedError('TODO: implement')

def mine_module(path, tests_path, reasons):
    """Yield one task per usable function in a script; count skip reasons in `reasons`."""
    raise NotImplementedError('TODO: implement')

def mine(scripts_dir=..., out_dir=..., limit=0, validate=True):
    raise NotImplementedError('TODO: implement')

def check(out_dir=...):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
