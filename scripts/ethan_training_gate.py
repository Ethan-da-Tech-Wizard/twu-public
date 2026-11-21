# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Deterministic training-data gate: classify every row ACCEPT / REJECT(reason).

No model calls, no network, stdlib only. Reads one dataset (.jsonl or .json array),
never modifies it. Writes accepted rows only to --out (refuses to overwrite, refuses
paths inside data/training or equal to the input). --dry-run writes nothing.
Summary JSON (counts per reason, input sha256) goes to stdout.

Usage: python3 scripts/ethan_training_gate.py INPUT [--out NEW.jsonl] [--dry-run] [--details]
Reject reasons: bad_json, bad_schema, not_verified, marked_failed, model_labelled_unverified,
secret_or_private, duplicate_prompt, contradicts_essentials.
Structured rows (ethan-system-pair.v1, ethan-traj.v1): prompt = first user message (or task);
a row needs >=1 assistant turn in messages/chosen_messages. Verified = verified_by execution
(or regex, accepted with note regex_weak so a lane can weight it) or verifier.passed true.
All message content/tool calls are scanned for secrets; the contradiction check looks only at
what an assistant turn ISSUES (tool calls, or non-refusal text), never refusals or tool results.
Accepted rows may carry a note (summary accept_notes).
"""
import argparse, hashlib, json, os, re, sys
from collections import Counter

def sha256_file(p):
    raise NotImplementedError('TODO: implement')

def load_rows(path):
    """Return list of (obj_or_None, raw_error)."""
    raise NotImplementedError('TODO: implement')

def _s(v):
    raise NotImplementedError('TODO: implement')

def _msgs(r):
    raise NotImplementedError('TODO: implement')

def _content(m):
    raise NotImplementedError('TODO: implement')

def first_user(r):
    raise NotImplementedError('TODO: implement')

def has_assistant_turn(r):
    raise NotImplementedError('TODO: implement')

def _call_text(c):
    raise NotImplementedError('TODO: implement')

def issued_text(r):
    """Text an assistant actually issues: tool calls, plus non-refusal assistant prose."""
    raise NotImplementedError('TODO: implement')

def prompt_key(r):
    """Prompt identity: task if present (v3 prompts share a system preamble), else prompt/instruction+input,
    else the first user message of a structured row."""
    raise NotImplementedError('TODO: implement')

def response_text(r):
    raise NotImplementedError('TODO: implement')

def has_schema(r):
    raise NotImplementedError('TODO: implement')

def is_failed(r):
    raise NotImplementedError('TODO: implement')

def verification_note(r):
    """'' when strong/unspecified, 'regex_weak' when verified only by a call/text regex."""
    raise NotImplementedError('TODO: implement')

def has_verified_marker(r):
    raise NotImplementedError('TODO: implement')

def scan(r):
    """Scan all string content except fields that intentionally hold the bad side of a pair."""
    raise NotImplementedError('TODO: implement')

def contradiction(r):
    raise NotImplementedError('TODO: implement')

def classify(rows):
    """Return list of (verdict, reason) aligned with rows."""
    raise NotImplementedError('TODO: implement')

def out_path_ok(out, inp):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
