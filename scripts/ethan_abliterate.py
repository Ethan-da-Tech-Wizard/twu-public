# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Deterministic refusal-direction abliteration pipeline for the local Ethan CLI models (Arditi et al. 2024 style).

  prompt-sets   build + hash the refuse/comply prompt splits from our SFT data (no model, no torch)
  run           activations -> direction -> layer selection -> weight orthogonalisation -> eval -> RECEIPT.json
  print-export  print (never run) the GGUF convert / quantize / adapter-pin commands for a finished output

Safety posture: the source weights are only READ. Output goes to NEW files under
/mnt/GameDrive/example_host/models/abliterated/<model>/<rev>/ (staging dir first, renamed on success; a failed gate leaves
<rev>.FAILED with its RECEIPT.json and the run exits 3). No network. CPU only unless --allow-gpu is passed explicitly
(the GPU is scheduled by Ethan; the default load mode is cpu and CUDA is hidden before torch is imported).
The deterministic tool-layer guards (policy engine, allowlists, STOP latch, loopback servers) are NOT touched by this tool.
See docs/ETHAN_ABLITERATION.md.
"""
import argparse, collections, gc, hashlib, json, math, os, random, re, shlex, shutil, subprocess, sys, time

class AbliError(Exception):
    pass

def sha256_file(path, chunk=...):
    raise NotImplementedError('TODO: implement')

def sha256_json(obj):
    raise NotImplementedError('TODO: implement')

def _jload(path):
    raise NotImplementedError('TODO: implement')

def read_jsonl(path):
    raise NotImplementedError('TODO: implement')

def _text(content):
    raise NotImplementedError('TODO: implement')

def _turn(row):
    """(last user text, first assistant message after it) or None."""
    raise NotImplementedError('TODO: implement')

def classify(row):
    """'refuse' | 'comply' | None.
    refuse: skill 25, family refusal.* (not refusal.injection*), the chosen answer is a plain-text refusal (no tool call).
    comply: the chosen first answer is a tool call, in skill tool_call / benign_lookalike / 25 benign.*."""
    raise NotImplementedError('TODO: implement')

def _round_robin(rows, rng):
    raise NotImplementedError('TODO: implement')

def _entry(r):
    raise NotImplementedError('TODO: implement')

def _splits(n_avail, n_fit, n_sel, n_eval):
    raise NotImplementedError('TODO: implement')

def build_prompt_sets(rows, seed, n_fit=48, n_sel=16, n_eval=32):
    """Deterministic by (rows, seed). Returns {'refuse':{'fit','sel','eval'}, 'comply':{...}, 'hashes':{...}}.
    Splits are disjoint by row id and by user text."""
    raise NotImplementedError('TODO: implement')

def dev_sample(dev_rows, seed, n):
    raise NotImplementedError('TODO: implement')

def serve_view_default():
    """The tuned serve profile used by the bridge (system prompt + tuned tools)."""
    raise NotImplementedError('TODO: implement')

def render(tok, system, tools, user):
    raise NotImplementedError('TODO: implement')

def render_set(tok, entries, serve_view):
    raise NotImplementedError('TODO: implement')

def opener_tokens(tok, rows, min_count=2):
    """First-token ids of the chosen refusal answers (>= min_count occurrences), keeping only tokens that start refusals at least 4x
    as often as they start non-refusal assistant text answers (generic openers like 'The'/'I' are dropped)."""
    raise NotImplementedError('TODO: implement')

def _torch():
    raise NotImplementedError('TODO: implement')

def is_writer(name):
    raise NotImplementedError('TODO: implement')

def orthogonalise_tensor(name, t, r):
    """W <- W - r r^T W for linear writers (out x in, out == hidden); E <- E - E r r^T for the embedding (vocab x hidden).
    Computed in float32 (r is a unit float32 vector), cast back to the original dtype."""
    raise NotImplementedError('TODO: implement')

def writer_modules(model):
    raise NotImplementedError('TODO: implement')

class Ablate:
    """Context manager: forward hooks that project r out of every residual-stream writer's output. Mathematically
    equal to the weight edit (used for layer selection without writing weights)."""

    def __init__(self, model, r):
        raise NotImplementedError('TODO: implement')

    def __enter__(self):
        raise NotImplementedError('TODO: implement')

    def __exit__(self, *a):
        raise NotImplementedError('TODO: implement')

def _ids(tok, text, device):
    raise NotImplementedError('TODO: implement')

def forward_stats(model, tok, texts, want_hidden=False, device=None):
    """Per prompt: last-token hidden states at every layer (optional) and first-generated-token log-probs."""
    raise NotImplementedError('TODO: implement')

def diff_of_means(refuse_h, comply_h):
    """[n,L+1,H] x2 -> (unit directions [L+1,H] float64, norms [L+1])."""
    raise NotImplementedError('TODO: implement')

def opener_mass(lp, ids):
    raise NotImplementedError('TODO: implement')

def opener_rate(lp, ids):
    raise NotImplementedError('TODO: implement')

def mean_kl(lp_base, lp_new):
    raise NotImplementedError('TODO: implement')

def changed_rate(lp_base, lp_new):
    raise NotImplementedError('TODO: implement')

def choose_layer(scores, th):
    """Deterministic selection rule. scores: list of dicts with idx, reduction, kl, changed. Eligible = kl <= sel_kl_max and
    changed <= sel_changed_max and reduction >= sel_min_reduction. Pick the largest reduction; ties -> lowest idx.
    Returns the chosen dict or None (fail closed)."""
    raise NotImplementedError('TODO: implement')

def candidate_indices(n_hidden_states, stride=1, lo_frac=0.25, hi_frac=0.75):
    """hidden_states indices 1..L-1 (index i = output of layer i-1; the last entry is post-final-norm and skipped)."""
    raise NotImplementedError('TODO: implement')

def parse_first_tool_call(text, tools):
    """-> (valid, (name, args) | None). Accepts the Qwen3.5 XML form and a JSON {"name","arguments"} fallback.
    Valid: name is a declared tool and every required parameter is present."""
    raise NotImplementedError('TODO: implement')

def generate_text(model, tok, text, max_new, device=None):
    raise NotImplementedError('TODO: implement')

def capability(model, tok, dev, serve_view, max_new):
    """Per dev prompt: the generated first tool call."""
    raise NotImplementedError('TODO: implement')

def capability_metrics(base, new):
    raise NotImplementedError('TODO: implement')

def check_gates(m, th):
    """-> (ok, [failure strings]). Fail closed: any breach is a failure; missing metrics are a failure."""
    raise NotImplementedError('TODO: implement')

def source_shards(src):
    raise NotImplementedError('TODO: implement')

def hidden_and_layers(src):
    raise NotImplementedError('TODO: implement')

def write_abliterated(src, dst, r):
    """Read src shards, write NEW shards in dst (same file names), copy every non-weight file byte-for-byte.
    Returns {'edited': [names], 'shards': {name: sha256}}. Never writes under src."""
    raise NotImplementedError('TODO: implement')

def verify_untouched(src, dst, edited):
    """True iff every non-edited tensor is bitwise equal and key sets match; edited tensors keep shape/dtype."""
    raise NotImplementedError('TODO: implement')

def tree_fingerprint(path):
    raise NotImplementedError('TODO: implement')

def load_model(path, mode):
    raise NotImplementedError('TODO: implement')

def free(model):
    raise NotImplementedError('TODO: implement')

def run_pipeline(a, serve_view=None, log=...):
    raise NotImplementedError('TODO: implement')

def _core(receipt):
    raise NotImplementedError('TODO: implement')

def _write_receipt(receipt, d):
    raise NotImplementedError('TODO: implement')

def _fail(receipt, cur_dir, failed, failures, create):
    raise NotImplementedError('TODO: implement')

def export_commands(out_dir, model_name, gguf_dir=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
