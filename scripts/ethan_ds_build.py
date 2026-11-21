# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Dataset BUILD STEP for Ethan's local-model fine-tuning (schema ethan-traj.v1 -> SFT / DPO / held-out eval).

Run with the train312 interpreter (needs `transformers`, CPU only, local_files_only, no network, no model weights loaded):
  ETHAN_CAP=3G scripts/ethan_capped_run.sh /mnt/GameDrive/example_host/venvs/train312/bin/python -B scripts/ethan_ds_build.py       --inputs data/autoimprove/20261116/trajectories/traj_v1.jsonl data/autoimprove/20261116/policy/policy_v1.jsonl                data/autoimprove/20261101/tooluse/pairs_v3.jsonl --out data/autoimprove/20261116/build --seed 1116
  ... --check      validate an existing build against the quality gate without rewriting anything.

Steps: normalise inputs -> verifier filter -> secret/PII scrub (quarantine) -> eval/holdout overlap drop (normalised prompt hash
+ 8-gram) -> exact + near-dup (MinHash/LSH, Jaccard>=0.85) -> per-family cap -> family-level held-out eval -> stratified
train/dev -> render with the REAL Qwen3.5 chat template (system = .gemini/ETHAN_CLI_GUIDANCE.md verbatim, tools = Gemini CLI
schemas, enable_thinking=False) with an assistant-only loss mask -> DPO pairs -> manifest + quality gate.
Never writes to existing eval files. Output files are written only under --out.
A non-empty quarantine.jsonl fails the gate until a human writes quarantine.reviewed.json = {"sha256": <sha256 of quarantine.jsonl>}.
"""
import argparse
import hashlib
import json
import math
import os
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

def set_profile(profile):
    raise NotImplementedError('TODO: implement')

def serve_view(answer_rule=False, profile=None):
    """-> {'system': system prompt, 'tools': {name: serve schema}, 'env', 'sha', 'profile'}; cached per profile.
    Both profiles drive the bridge's own functions: ensure_tool_system_prompt, then apply_slim_prompt(level 2 or 3)."""
    raise NotImplementedError('TODO: implement')

def serve_system():
    raise NotImplementedError('TODO: implement')

def called_names(row):
    raise NotImplementedError('TODO: implement')

def served_names(row, profile=None):
    """Tool names the bridge would serve for this row. tuned: the CLI's 5 core tools, plus replace+write_file only for rows that
    use them. bridge2: the row's own declared tool list. Unknown names -> None."""
    raise NotImplementedError('TODO: implement')

def tool_names_ok(names):
    raise NotImplementedError('TODO: implement')

def guidance_text():
    raise NotImplementedError('TODO: implement')

def sha256_bytes(b):
    raise NotImplementedError('TODO: implement')

def sha256_file(p):
    raise NotImplementedError('TODO: implement')

def norm_calls(calls):
    raise NotImplementedError('TODO: implement')

def norm_msg(m):
    raise NotImplementedError('TODO: implement')

def parse_call_text(text):
    """'<tool_call>{json}</tool_call>' -> assistant msg with structured tool_calls; anything else stays prose."""
    raise NotImplementedError('TODO: implement')

def convert_pair_v3(r):
    raise NotImplementedError('TODO: implement')

def convert_system_pair(r):
    """ethan-system-pair.v1 (Magi 9, scripts/ethan_system_pairs.py) -> ethan-traj.v1. 'messages' holds [system, user]; the verified
    assistant tail is 'chosen_messages' and the violating one 'rejected_messages' (hard negatives / violations -> `rejected`).
    Their per-message train markers are preserved (train:false -> no loss); their system text is dropped (the serve prompt replaces it)."""
    raise NotImplementedError('TODO: implement')

def load_inputs(paths):
    raise NotImplementedError('TODO: implement')

def resolve_tools(row):
    """-> the bridge-slimmed serve schemas for the row's tool names, in the CLI's order; None if a name is unknown."""
    raise NotImplementedError('TODO: implement')

def norm_text(s):
    raise NotImplementedError('TODO: implement')

def h64(s):
    raise NotImplementedError('TODO: implement')

def user_texts(row_msgs):
    raise NotImplementedError('TODO: implement')

def boilerplate_lines(corpora, min_rows=20, frac=0.03):
    """Lines (normalised) present in many prompts of a corpus = template boilerplate, ignored for overlap/dedup."""
    raise NotImplementedError('TODO: implement')

def strip_bp(text, bp):
    raise NotImplementedError('TODO: implement')

def ngrams(text, n=8):
    raise NotImplementedError('TODO: implement')

def row_prompt_keys(row, bp):
    raise NotImplementedError('TODO: implement')

def row_grams(row, bp, n=8):
    raise NotImplementedError('TODO: implement')

def load_eval_sets(extra=...):
    raise NotImplementedError('TODO: implement')

class EvalIndex:

    def __init__(self, prompts, ids, bp, n=8):
        raise NotImplementedError('TODO: implement')

    def overlap(self, row):
        raise NotImplementedError('TODO: implement')

def _simple_commands(cmd):
    raise NotImplementedError('TODO: implement')

def command_problems(cmd):
    """Reasons a run_shell_command string is not a valid invocation in THIS repo: invoked script paths must exist, and the repo's own
    CLIs (magi, enki_tools, git guard, cda judge) must parse under their REAL argparse (via ethan_ds_policy_skills.parse_cli)."""
    raise NotImplementedError('TODO: implement')

def private_path_calls(row):
    """True when a non-refusal row has a call touching a private location (private/, profile/, business/, grants/, backups/, keys/,
    .env, .ssh). Refusal families legitimately name them in the request or in a blocked call."""
    raise NotImplementedError('TODO: implement')

def policy_oracle():
    """The same cache of REAL PolicyEngine decisions the policy generator uses (ethan_ds_policy_skills.Oracle -> node)."""
    raise NotImplementedError('TODO: implement')

def _policy_calls(row):
    raise NotImplementedError('TODO: implement')

def prime_policy(rows):
    """Resolve all distinct calls of `rows` in ONE batch of real-engine decisions."""
    raise NotImplementedError('TODO: implement')

def is_build_file_call(tool, args):
    """replace/write_file on exactly a build-config basename: the real CLI asks the human, who approves, so ASK_USER is legitimate."""
    raise NotImplementedError('TODO: implement')

def _decision_ok(tool, args, decision):
    raise NotImplementedError('TODO: implement')

def policy_not_allowed(row):
    raise NotImplementedError('TODO: implement')

def ask_user_build_calls(row):
    """Number of calls in `row` allowed only because ASK_USER on a build-config file is legitimate."""
    raise NotImplementedError('TODO: implement')

def invalid_command_reasons(row):
    raise NotImplementedError('TODO: implement')

def _kv_value_is_secret(quote, val):
    raise NotImplementedError('TODO: implement')

def _entropy(t):
    raise NotImplementedError('TODO: implement')

def _numeric_context(s, a, b):
    """A digit run inside df -i / stat / lsblk output, a column table, a timestamp or a hash is an identifier, not a card number."""
    raise NotImplementedError('TODO: implement')

def _luhn(d):
    raise NotImplementedError('TODO: implement')

def _secret_like_token(t):
    """True for high-entropy, mixed-class tokens. Hashes, paths and snake_case identifiers are NOT secrets."""
    raise NotImplementedError('TODO: implement')

def scrub_string(s):
    raise NotImplementedError('TODO: implement')

def row_strings(row):
    raise NotImplementedError('TODO: implement')

def scrub_flags(row):
    raise NotImplementedError('TODO: implement')

def shingles(text, k=3):
    raise NotImplementedError('TODO: implement')

class NearDup:

    def __init__(self, seed, perms=64, bands=16, thr=0.85):
        raise NotImplementedError('TODO: implement')

    def sig(self, sh):
        raise NotImplementedError('TODO: implement')

    def add_if_new(self, sh):
        """Return True if kept (no near-dup among kept rows), False if a duplicate."""
        raise NotImplementedError('TODO: implement')

def dedup_text(row, bp):
    raise NotImplementedError('TODO: implement')

class Renderer:

    def __init__(self, model_dir=...):
        raise NotImplementedError('TODO: implement')

    @staticmethod
    def to_template_msgs(msgs, system):
        raise NotImplementedError('TODO: implement')

    def apply(self, tmsgs, tools, gen):
        raise NotImplementedError('TODO: implement')

    def serve_prompt(self, msgs, tools, system):
        """The prompt exactly as the server builds it for a request carrying `msgs` (generation prompt, thinking off)."""
        raise NotImplementedError('TODO: implement')

    def render(self, msgs, tools, system):
        """-> (text, spans, problems). spans = char [start,end) of every assistant completion (after the generation
        prompt incl. the empty think block, through <|im_end|>)."""
        raise NotImplementedError('TODO: implement')

    def encode_mask(self, text, spans, flags=None):
        raise NotImplementedError('TODO: implement')

def build_rendered(rd, row, system):
    """Render one normalised row -> (output dict, problems)."""
    raise NotImplementedError('TODO: implement')

def parity_check(rd, out_row, system=None, serve_fn=None):
    """Train-time prompt must EQUAL the serve/eval-time prompt. Returns list of problems ([] = parity holds).
    serve_fn(msgs, tools, system) lets a test inject a deliberately wrong serve render."""
    raise NotImplementedError('TODO: implement')

def _expected_assistant_text(m):
    raise NotImplementedError('TODO: implement')

def token_audit(rd, out_row, system=None):
    """Independent token-level check: tokenize the rendered text, decode ONLY the supervised tokens, and require that they
    hold nothing but assistant output (+ <|im_end|> and the XML tool-call syntax): never system, user or tool text."""
    raise NotImplementedError('TODO: implement')

def gguf_template_parity(rd, gguf_path, rows):
    """Render with the chat template embedded in a GGUF (what llama-server's Jinja uses) and compare to the HF render.
    Returns {'template_equal': bool|None, 'mismatches': n, 'checked': n}; None if the gguf/template is unavailable."""
    raise NotImplementedError('TODO: implement')

def build_dpo(rd, row, system):
    raise NotImplementedError('TODO: implement')

def _call_targets(c):
    raise NotImplementedError('TODO: implement')

def valid_alternative(chosen_tail, rej_tail):
    """True when the rejected side is merely another VALID way to do the same thing (so it is not a preference signal):
    built-in read tool vs shell command on the same target, or the same `ls` with only different flags. A different target
    (wrong file), different flag semantics (cut -f1 vs -f2), a dangerous call or a refusal never counts as an alternative."""
    raise NotImplementedError('TODO: implement')

def _dpo_pair(rd, row, system, prompt_msgs, chosen_tail, tail, rej):
    raise NotImplementedError('TODO: implement')

def pct(xs, p):
    raise NotImplementedError('TODO: implement')

def token_stats(lens, limit=4096):
    raise NotImplementedError('TODO: implement')

def mix_class(r):
    raise NotImplementedError('TODO: implement')

def _round_robin(rows, n, seed, tag):
    """Deterministic family-balanced pick of n rows: rows with a 'rejected' side first, then hash order."""
    raise NotImplementedError('TODO: implement')

def target_mix(rows, seed, r_range=..., b_range=..., skill_floor=0):
    """Pick the largest subset whose refusal share lies in r_range and benign-lookalike share in b_range, weights chosen
    from the actual class counts (grid search, maximising kept rows). Family caps are untouched (we only remove rows)."""
    raise NotImplementedError('TODO: implement')

def quarantine_reviewed(out_dir):
    raise NotImplementedError('TODO: implement')

def opener_stats(rows):
    """Most common 2-word opener of the final assistant answers (non-empty prose) in `rows` -> (opener, share, n)."""
    raise NotImplementedError('TODO: implement')

def lang_skill(s):
    raise NotImplementedError('TODO: implement')

def task_identity(row):
    """-> (task_id, is_proxy). Real `task_id` from the generator when present; otherwise a LABELLED proxy
    source + family + first tool-call name + first path basename (older generators carry no task_id)."""
    raise NotImplementedError('TODO: implement')

def cap_per_task(train, seed, cap=...):
    """At most `cap` train rows per (source, task_id): rows with a `rejected` side first, then stable hash order."""
    raise NotImplementedError('TODO: implement')

def task_report(o_train):
    """Per source and per skill: rows, distinct_task_ids, rows_per_task max/p95, proxy_share (over TRAIN rows)."""
    raise NotImplementedError('TODO: implement')

def distinct_task_gate_reasons(o_train, present, min_tasks=...):
    raise NotImplementedError('TODO: implement')

def family_prompt_stats(o_train, min_rows=20):
    raise NotImplementedError('TODO: implement')

def family_prompt_gate_reasons(o_train, min_ratio=...):
    raise NotImplementedError('TODO: implement')

def language_gate_reasons(train_skill_counts, present, min_rows=100):
    """Skills 31-39 (language datasets) need >= min_rows in train, but only when the skill is present in the inputs."""
    raise NotImplementedError('TODO: implement')

def compute_gate(parity_mismatches, eval_overlap, family_counts, skill_counts, cap, min_skill, quarantine_n, reviewed, family_leak=0, dup_ids=0, invalid_rows=0, opener=None, lang_reasons=...):
    raise NotImplementedError('TODO: implement')

def write_jsonl(path, rows):
    raise NotImplementedError('TODO: implement')

def hkey(seed, s):
    raise NotImplementedError('TODO: implement')

def parse_exclusions(extra):
    """--exclude-family PATTERN[:SOURCE][=REASON] entries extend (never replace) the defaults."""
    raise NotImplementedError('TODO: implement')

def excluded_by(row, exclusions):
    raise NotImplementedError('TODO: implement')

def run_filters(rows, eval_prompts, eval_ids, seed, cap, ngram_n=8, jaccard=0.85, exclusions=None):
    raise NotImplementedError('TODO: implement')

def choose_holdout(rows, seed, n_target, min_skill_left):
    """Whole families are withheld. Families of rows flagged _force_holdout (a generator's own dev holdout, e.g. system_pairs dev)
    go first and are never trimmed; random families then fill up to n_target."""
    raise NotImplementedError('TODO: implement')

def regex_cap(rows, cap, seed, source=...):
    """Limit regex-verified rows of `source` to at most `cap` of that source's rows (execution-verified rows always kept)."""
    raise NotImplementedError('TODO: implement')

def final_answer_key(r):
    raise NotImplementedError('TODO: implement')

def expand_segments(rows):
    """Rows with several user turns become one sample per user segment. The chat template drops the think block of assistant turns
    that precede the last user turn, so only the LAST segment of a sample can be supervised exactly as it is served; earlier
    segments stay as context (train:false). `rejected` (a tail of the final segment) goes to the last sample only."""
    raise NotImplementedError('TODO: implement')

def split_train_dev(rows, seed, dev_frac):
    """Deterministic, stratified by skill; samples expanded from one conversation (same _orig_id) always stay on the same side."""
    raise NotImplementedError('TODO: implement')

def render_all(rd, rows, system, mismatch_log):
    raise NotImplementedError('TODO: implement')

def count_invalid_in_outputs(o_train, o_dev, o_ho, dpo_rows=...):
    raise NotImplementedError('TODO: implement')

def final_eval_overlap(out_rows, ev):
    raise NotImplementedError('TODO: implement')

def build(args):
    raise NotImplementedError('TODO: implement')

def _strkeys(o):
    """Recursively stringify dict keys so sort_keys works when inputs label skills with ints (policy) and strings (pairs_v3)."""
    raise NotImplementedError('TODO: implement')

def make_manifest(rd, args, srcs, efiles, stats, quarantine, mism, o_train, o_dev, o_ho, dpo, dpo_skip, ho_fams, ho_unused, ev, out_dir, lang_present=...):
    raise NotImplementedError('TODO: implement')

def check(args):
    """Validate an existing build against the gate WITHOUT rewriting any output."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
