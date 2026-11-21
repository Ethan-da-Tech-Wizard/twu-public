# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Completion-only SFT LoRA/QLoRA trainer for the tool-use plan's first run (TRAINING_PLAN.md section 4).

Data: data/autoimprove/20261101/tooluse/pairs.jsonl, 'prompt' -> 'chosen' (rejected unused), minus the ids in
data/autoimprove/20261101/verify/drop_ids_*.json. Loss is computed on the completion tokens only.
Thermal pacing is a software duty cycle between optimizer steps; ethan_thermal_guard limits are the backstop and
any guard-level event is a FAULT (checkpoint, log, stop). Never kills or restarts the model server.

Modes:
  --dry-run  validate data, split, tokenization (if a tokenizer is available) and config. No torch, no GPU.
  --smoke    2 optimizer steps on the real model (needs the GPU free). Run with the train312 venv python.
  (default)  full run. Real runs refuse to start while the model server is up or free VRAM is too low.

  /mnt/GameDrive/example_host/venvs/train312/bin/python scripts/ethan_sft_lora.py --dry-run
"""
import argparse, copy, hashlib, json, math, os, random, re, socket, subprocess, sys, time
from pathlib import Path

def chosen_text(c):
    raise NotImplementedError('TODO: implement')

def row_hash(row):
    raise NotImplementedError('TODO: implement')

def load_drops(directory=None, pattern=None):
    raise NotImplementedError('TODO: implement')

def _kept(idx, r):
    """Kept-row record. v3 rows also carry their exact eval request ('messages' + 'tools'); those drive --render row."""
    raise NotImplementedError('TODO: implement')

def load_rows(path, drop_ids=..., drop_hashes=None, lenient_hash=False):
    """Return (rows, report). Each kept row carries its original line index as 'idx'. Fails closed on hash mismatch."""
    raise NotImplementedError('TODO: implement')

def split_dev(rows, seed=..., dev_n=48):
    """Seeded, family-round-robin dev split. Dev rows have a unique chosen call and no train row shares their prompt."""
    raise NotImplementedError('TODO: implement')

def default_data(directory=None):
    """Newest existing of pairs_v3.jsonl then pairs_v2.jsonl in tooluse/. Falls back to the v2 path (may not exist)."""
    raise NotImplementedError('TODO: implement')

def _norm_name(s):
    raise NotImplementedError('TODO: implement')

def base_matches_target(base, target=...):
    """True if the base model path names the declared serving target (e.g. .../Qwen2.5-Coder-7B-Instruct/...)."""
    raise NotImplementedError('TODO: implement')

def serving_check(base, target=..., lane=None):
    """(ok, decision). Training a base other than the serving target is refused unless the run is explicitly a
    candidate for a declared second-port lane, whose base must also be the lane's declared model."""
    raise NotImplementedError('TODO: implement')

def bridge_messages(prompt, tools, system=None):
    """The exact messages the bridge forwards: the CLI user turn, run through gemini_broker_bridge.ensure_tool_system_prompt."""
    raise NotImplementedError('TODO: implement')

def default_tools():
    raise NotImplementedError('TODO: implement')

def qwen_chat_render(messages, tools=None, add_generation_prompt=True, enable_thinking=False):
    """Pure-python mirror of the Qwen3 chat template for system/user messages plus the native tools block
    (tests compare it to the real tokenizer template when one is available)."""
    raise NotImplementedError('TODO: implement')

def render_bridge_prompt(prompt, tools=None, tokenizer=None):
    """Prompt text exactly as the served model sees a CLI turn: bridge system-prompt injection + native tools block +
    generation prompt (thinking off). Uses the tokenizer's real template when given, else the pure mirror."""
    raise NotImplementedError('TODO: implement')

def file_sha256(path):
    raise NotImplementedError('TODO: implement')

def tree_sha256(path, patterns=...):
    """Deterministic digest of a model/adapter dir's weight files (name + per-file sha256); a single file is hashed directly."""
    raise NotImplementedError('TODO: implement')

def git_state(repo=...):
    raise NotImplementedError('TODO: implement')

def build_receipt(args, data_path, serving_decision, adapter_path=None, sha_fn=..., git_fn=...):
    """Provenance record: base model sha, adapter sha, data file sha, git + policy + code shas, serving decision."""
    raise NotImplementedError('TODO: implement')

def adapter_gguf_command(adapter_dir, base, outfile, outtype=..., python=..., script=...):
    raise NotImplementedError('TODO: implement')

def export_adapter_gguf(args, run_fn=...):
    """Dry-run by default: prints the exact conversion command. Executes only with --run-conversion (CPU only)."""
    raise NotImplementedError('TODO: implement')

def format_example(prompt, chosen, think_prefix=True):
    """Fallback (no tokenizer template): Qwen ChatML text chosen, used as given."""
    raise NotImplementedError('TODO: implement')

def split_with_template(tokenizer, prompt, chosen, bridge_tools=None):
    """(prompt_text, completion_text) via the model chat template. Text chosen is appended as given; structured
    chosen (assistant message dict/list incl. tool_calls) is rendered by the template itself."""
    raise NotImplementedError('TODO: implement')

def encode_example(tokenizer, prompt, chosen, max_len, think_prefix=True, bridge_tools=None):
    """dict(input_ids, labels) with prompt labels = -100, or None if longer than max_len (never truncated)."""
    raise NotImplementedError('TODO: implement')

def _apply(tokenizer, messages, tools, chat_template=None, **kw):
    """tokenizer.apply_chat_template with the SAME kwargs the eval/bridge request render uses
    (tools=..., enable_thinking=False; the Qwen2.5 template ignores the extra kwarg)."""
    raise NotImplementedError('TODO: implement')

def row_messages_tools(row, render=..., bridge_tools=None):
    """(messages, tools) for a kept row. 'row' = the row's own recorded eval request (fail closed if absent);
    'bridge' = rebuilt from row['prompt'] through the bridge (must agree with 'row' on v3); 'plain' = bare user turn."""
    raise NotImplementedError('TODO: implement')

def split_row(tokenizer, row, render=..., bridge_tools=None, chat_template=None):
    """(prompt_text, completion_text). prompt = chat template of messages (+tools) with the generation prompt, exactly the
    eval request render; completion = the chosen assistant tail + <|im_end|> (loss target). Text chosen is verified to be
    what the template itself renders after the generation prompt (see template_tail)."""
    raise NotImplementedError('TODO: implement')

def template_tail(tokenizer, row, render=..., bridge_tools=None, chat_template=None):
    """The template's own rendering of messages + assistant(chosen), minus the generation prompt. For text chosen this
    equals completion_text + '\\n' when the training completion is byte-identical to what the template would emit."""
    raise NotImplementedError('TODO: implement')

def encode_row(tokenizer, row, max_len, render=..., bridge_tools=None, chat_template=None):
    """dict(input_ids, labels, n_prompt) with prompt labels = -100, or None if longer than max_len (never truncated)."""
    raise NotImplementedError('TODO: implement')

def length_stats(lens):
    """Percentile summary of a list of token lengths."""
    raise NotImplementedError('TODO: implement')

def estimate_resources(cfg, max_len, micro, n_rows, epochs, mean_len=None, mean_completion=None, chunked_logits=True, tok_per_s=..., sleep_fraction=0.25, shared_prefix_tokens=0, group=16):
    """Analytic QLoRA budget from a HF config dict (NO measurement; every number is an [estimate] to verify on --smoke).
    bytes: NF4 weights ~0.53 B/param (double-quant), embeddings fp32 (peft prepare_model_for_kbit_training upcasts bf16 params),
    LoRA r16 all-linear fp32 weights + grads + 8-bit Adam, checkpointed activations (bf16) + one recomputed layer, logits."""
    raise NotImplementedError('TODO: implement')

def build_schedule(n, micro, accum, epochs, seed):
    """Deterministic list of optimizer steps; each step is a list of micro-batches of example indices."""
    raise NotImplementedError('TODO: implement')

def lr_at(step, total, warmup, peak):
    """Cosine with linear warmup; step is 0-based."""
    raise NotImplementedError('TODO: implement')

def cooling_plan(gpu, cpu_streak=0):
    """(sleep_target_c or None, fixed_sleep_s, max_sleep_s, checkpoint_first). Unknown/guard-level handled by caller."""
    raise NotImplementedError('TODO: implement')

def guard_fault(gpu, cpu):
    """Reason string if telemetry is unknown or at a guard pause/abort level, else None."""
    raise NotImplementedError('TODO: implement')

class ThermalPacer:
    """After each optimizer step: read temps, sleep per the duty-cycle bands, log every sleep, flag faults."""

    def __init__(self, log_path, gpu_fn=None, cpu_fn=None, sleep_fn=..., now_fn=..., stop_path=None, fine=False, target=..., kp=..., ki=...):
        raise NotImplementedError('TODO: implement')

    def _log(self, **kw):
        raise NotImplementedError('TODO: implement')

    def _track(self, gpu, cpu):
        raise NotImplementedError('TODO: implement')

    def _sleep(self, step, seconds, gpu, cpu, reason):
        raise NotImplementedError('TODO: implement')

    def duty_update(self, gpu):
        """Velocity-form PI on GPU temp: duty (work share of wall time) falls when hot or heating, rises when cool."""
        raise NotImplementedError('TODO: implement')

    def after_unit(self, step, work_s, checkpoint_fn=None):
        """Fine pacing after one share-group of `work_s` seconds of GPU work. Returns 'ok' or 'fault'.
        Guard-level temperatures remain faults (checkpoint, stop); the STOP latch is honoured."""
        raise NotImplementedError('TODO: implement')

    def after_step(self, step, checkpoint_fn=None):
        """Returns 'ok', 'fault' (stop now) or 'thermally_bound' (finish at current checkpoint)."""
        raise NotImplementedError('TODO: implement')

    def summary(self):
        raise NotImplementedError('TODO: implement')

def server_is_up(port=...):
    """True if the workspace llama-server is found by the guard's identity check or the port accepts connections."""
    raise NotImplementedError('TODO: implement')

def gpu_free_mib():
    raise NotImplementedError('TODO: implement')

def preflight(args, server_fn=..., free_fn=..., temp_fn=None):
    """Returns a list of blocking reasons for a real (non dry-run) start. Empty = go."""
    raise NotImplementedError('TODO: implement')

def write_json(path, obj):
    raise NotImplementedError('TODO: implement')

def dir_size_bytes(path):
    raise NotImplementedError('TODO: implement')

def latest_checkpoint(out_dir):
    raise NotImplementedError('TODO: implement')

def config_dict(args):
    raise NotImplementedError('TODO: implement')

def prepare(args):
    """Data + split + (optional) tokenization. No torch import. Returns dict with train/dev rows and a report."""
    raise NotImplementedError('TODO: implement')

def tokenize_all(args, rows):
    """Tokenizer-only (no model, no GPU). Returns (examples, stats) or (None, reason)."""
    raise NotImplementedError('TODO: implement')

class RenderedError(ValueError):
    """A rendered dataset that must not be trained on (fail closed)."""

def base_template_sha256(base, tok=None):
    """Same definition as ethan_ds_build.Renderer.template_sha256: chat_template.jinja file sha, else sha of tokenizer.chat_template."""
    raise NotImplementedError('TODO: implement')

def load_build_manifest(rendered_path):
    raise NotImplementedError('TODO: implement')

def check_rendered_gate(manifest, tok, base, files, allow_unreviewed=False):
    """Fail closed unless: manifest quality_gate.passed is True (or the override flag is given, recorded loudly), the manifest's chat
    template sha256 equals the base's, and every given rendered file's sha256 equals manifest outputs_sha256. -> receipt dict."""
    raise NotImplementedError('TODO: implement')

def read_rendered(path):
    raise NotImplementedError('TODO: implement')

def _span_mask(offsets, spans):
    """Replicates ethan_ds_build.Renderer.encode_mask: a token is supervised if inside, or partly inside, a supervised span."""
    raise NotImplementedError('TODO: implement')

def _audit_fn(tok):
    """The builder's token_audit when importable (its Renderer needs only .tok here), else a replica of its core checks."""
    raise NotImplementedError('TODO: implement')

def encode_rendered_row(tok, row, audit=None):
    """Re-tokenize the stored text (no re-render), apply the stored supervised spans, and require the result to equal the builder's
    token count, loss mask and token_audit. -> dict(input_ids, labels, n_prompt)."""
    raise NotImplementedError('TODO: implement')

def tokenize_rendered(args, rows):
    """Like tokenize_all for --rendered rows. Fails closed (RenderedError); rows above --max-len are dropped, never truncated."""
    raise NotImplementedError('TODO: implement')

def rendered_vram_estimate(args, stats):
    raise NotImplementedError('TODO: implement')

def prepare_rendered(args):
    """Load + verify (tokenizer, gate, hashes). Returns {'train','dev','report','manifest'} like prepare()."""
    raise NotImplementedError('TODO: implement')

def collate(torch, examples, pad_id):
    raise NotImplementedError('TODO: implement')

def completion_loss(torch, model, ids, lab, att, chunked=True):
    """(mean CE over completion tokens, k). chunked=True runs the decoder, then lm_head ONLY on completion positions, so the
    [tokens x 151936] fp32 logits/grad (the largest buffer at max-len 1280-2048) shrinks to [completion x 151936]. Same value as
    model(labels=...).loss (tested on a tiny model); chunked=False is the plain HF path."""
    raise NotImplementedError('TODO: implement')

def group_prefix_len(exs):
    """Longest token prefix shared by every example in the group, capped so that all prefix labels are masked
    (<= min n_prompt) and every example keeps >= 1 suffix token."""
    raise NotImplementedError('TODO: implement')

def pack_tree(exs, prefix_len=None):
    """Pack one shared prefix + K suffixes into ONE sequence. Returns dict of python lists:
    ids, pos (suffix positions restart at the prefix length), seg (-1 prefix, i suffix i), pred (index of the hidden
    state that predicts each target), tgt (target token ids, completion only). Pure python, no torch."""
    raise NotImplementedError('TODO: implement')

def tree_mask(torch, seg, P, dtype=None, leak=False):
    """[1,1,L,L] attention mask: query q may attend key kk iff kk<=q and (kk in prefix or same suffix).
    dtype None/bool -> boolean (True = attend, for sdpa); a float dtype -> additive (0 / -inf-ish, for eager).
    leak=True is a deliberately WRONG variant (suffixes see earlier suffixes) used only by tests."""
    raise NotImplementedError('TODO: implement')

def shared_prefix_loss(torch, model, exs, mask_dtype=None, prefix_len=None, _leak=False, _pos_bug=False):
    """(mean CE over the group's completion tokens, k). Prefix runs ONCE with gradients under the CURRENT weights (LoRA touches
    the prefix too), each suffix attends to the prefix and itself only (4D mask) at its true positions, so the value and every
    gradient equal the per-row loss (sum over rows of per-row mean*k / total k). _leak/_pos_bug are deliberately wrong variants for tests."""
    raise NotImplementedError('TODO: implement')

def share_groups(batch_indices, share_group):
    """Flatten one optimizer step's micro-batches into groups of <= share_group row indices (deterministic, order kept)."""
    raise NotImplementedError('TODO: implement')

def tokens_per_step(exs_by_step, share_group=None):
    """Analytic tokens the model processes. exs_by_step: list of lists of examples (one list per optimizer step).
    Returns (standard_total, shared_total) -- shared packs share_group rows per tree, prefix counted once per tree."""
    raise NotImplementedError('TODO: implement')

def train(args, tok, ex_train, ex_dev, out_dir, pacer):
    raise NotImplementedError('TODO: implement')

def common_prefix_len(seqs):
    """Length of the token prefix shared by ALL sequences (the system + tools block on v3)."""
    raise NotImplementedError('TODO: implement')

def estimate_report(args, prep):
    """Token-length distribution + analytic VRAM/time at max-len 1280 and 2048 (QLoRA, micro 1-2, grad ckpt, 4-bit). No model, no GPU."""
    raise NotImplementedError('TODO: implement')

def measure_cpu_ratio(step_exs, share_group, reps=2):
    """Measured CPU wall-time ratio (shared / standard) of one forward+backward over one optimizer step's real rows, on a tiny
    random Qwen3-style model (token ids folded into its vocab). CPU only; torch/transformers optional (returns None)."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
