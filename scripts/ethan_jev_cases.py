# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Deterministic exporter: verified policy rows -> cda_cases-schema training/eval cases for jev (0.42B Coding Decision Agent).

No network, no model, no GPU: jev and every model are NEVER loaded. Labels come only from deterministic ground truth:
  policy_engine        the REAL gemini-cli PolicyEngine decision (Oracle from ethan_ds_policy_skills) for a proposed tool call
  schema_precheck      ethan_cda_judge.validate_proposed_calls_schema (declared tool names + required args)
  select_jev_tier      ethan_cda_judge.select_jev_tier applied to the stated numeric signals          (CIRCULAR)
  evaluate_tool_gate   evaluate_tool_gate on the stated (synthetic) call_verdict answers                (CIRCULAR)
  evaluate_code_gate   evaluate_code_gate on the stated (synthetic) merge_action answers                (CIRCULAR)
Circular means the inputs to the rule are themselves synthetic answers written by the row generator, so the label proves
nothing about jev's judgment. Circular cases live ONLY in jev_cases_circular.jsonl, never in the tool-gate eval file.

  python3 -B scripts/ethan_jev_cases.py            # build
  python3 -B scripts/ethan_jev_cases.py --check    # quality gate; re-derives EVERY label from scratch (fresh oracle)
"""
from __future__ import annotations
import argparse
import atexit
import hashlib
import json
import os
import re
import shlex
import shutil
import sys
import tempfile
from collections import Counter
from pathlib import Path
import ethan_cda_judge as J
import ethan_ds_policy_skills as D

def canon(o):
    raise NotImplementedError('TODO: implement')

def sha(s):
    raise NotImplementedError('TODO: implement')

def sha_file(p):
    raise NotImplementedError('TODO: implement')

def split_of(key):
    raise NotImplementedError('TODO: implement')

def norm(t):
    raise NotImplementedError('TODO: implement')

def probs(labels, label):
    raise NotImplementedError('TODO: implement')

def decl_for(names):
    raise NotImplementedError('TODO: implement')

def tools_text(names):
    raise NotImplementedError('TODO: implement')

def calls_text(calls):
    raise NotImplementedError('TODO: implement')

def existing_cases():
    raise NotImplementedError('TODO: implement')

def existing_keys(cases):
    raise NotImplementedError('TODO: implement')

def verdict_question():
    raise NotImplementedError('TODO: implement')

def derive_all(cases, oracle):
    """Return {case_id: (gate_or_label, label_source)} derived ONLY from derivation_inputs. Uses the given (fresh) oracle."""
    raise NotImplementedError('TODO: implement')

def read_rows():
    raise NotImplementedError('TODO: implement')

def facts_of(row):
    raise NotImplementedError('TODO: implement')

def first_user(row):
    raise NotImplementedError('TODO: implement')

def row_calls(row):
    """(chosen calls, rejected calls) as [{name, arguments}] from the row's tool_calls."""
    raise NotImplementedError('TODO: implement')

def shell_arg(row, flag=None):
    raise NotImplementedError('TODO: implement')

def mk(case_id_prefix, key, family, hold, state, questions, derivation, row_ids, row_family):
    raise NotImplementedError('TODO: implement')

def candidates(rows):
    """All candidate cases (unlabelled), plus skip counters."""
    raise NotImplementedError('TODO: implement')

def finish(c, gate, source):
    raise NotImplementedError('TODO: implement')

def build(out_dir, oracle=None):
    raise NotImplementedError('TODO: implement')

def check(out_dir, oracle=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
