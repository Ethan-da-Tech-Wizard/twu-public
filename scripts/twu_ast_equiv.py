# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""twu_ast_equiv: AST invariant equivalence verifier for refactors (NEED-075, recursive self-hosting).

Given a Python file before and after a refactor, decide whether the change is behaviour-preserving at the syntax
level. Stdlib `ast` only. Ignores comments, formatting, line numbers and docstrings; optionally ignores renames of
function-local variables and parameters inside bodies (`--ignore-local-renames`). It reports three things apart:

  public_api   signature (names, defaults, annotations, kw-only, decorators) of every public top-level function,
               class and method (public = no leading underscore, or listed in __all__). A parameter rename IS an
               API change even with --ignore-local-renames, because callers can pass it by keyword.
  imports      set of (module, name, alias, level) over the whole file; order and placement ignored.
  body         every top-level definition's full normalized AST, keyed by name; plus the non-definition statements.

Limits (honest): syntactic, not semantic. Moving code between functions, changing evaluation order that the AST
shows, or any real edit is reported as different; equivalent-but-different-AST rewrites (e.g. inlining) are also
reported as different. Dynamic effects (getattr, exec, monkeypatching) are not modelled.

  python3 scripts/twu_ast_equiv.py BEFORE.py AFTER.py [--ignore-local-renames] [--json]
  exit 0 equivalent, 1 different, 2 unreadable / syntax error
Optional libs isidentical/refactor (MIT), google/pasta (Apache-2.0), ast-refactor (BSD-3) are NOT used: they
rewrite source, this tool only compares trees, and the stdlib covers that without a dependency.
"""
from __future__ import annotations
import argparse
import ast
import copy
import json
import sys
from pathlib import Path

def _strip_docstrings(tree):
    raise NotImplementedError('TODO: implement')

class _Alpha(ast.NodeTransformer):
    """Rename each function's params and locally bound names to v0, v1, ... by first appearance."""

    def _fn(self, node):
        raise NotImplementedError('TODO: implement')

    def visit_FunctionDef(self, node):
        raise NotImplementedError('TODO: implement')

def normalize(src, ignore_local_renames=False):
    raise NotImplementedError('TODO: implement')

def _dump(node):
    raise NotImplementedError('TODO: implement')

def _sig(fn):
    raise NotImplementedError('TODO: implement')

def _all_names(tree):
    raise NotImplementedError('TODO: implement')

def public_api(tree):
    raise NotImplementedError('TODO: implement')

def imports(tree):
    raise NotImplementedError('TODO: implement')

def bodies(tree):
    raise NotImplementedError('TODO: implement')

def compare(before_src, after_src, ignore_local_renames=False):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
