# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Resumable, thermally paced QLoRA SFT of Qwen2.5-Coder-7B-Instruct on the gold trajectories. CANDIDATE ONLY.

  plan    print the exact config, token-length stats, VRAM and time estimates; exit 2 and list every missing prerequisite
  run     train (needs the GPU free); --smoke = 2 optimizer steps to measure peak VRAM first; resumes from the latest checkpoint
  export  convert the adapter to a GGUF LoRA for `llama-server --lora` (CPU only; the base GGUF is never touched)

Run with the train312 venv python (the plain system python has no torch):
  /mnt/GameDrive/example_host/venvs/train312/bin/python scripts/ethan_train_gold.py plan

Rules kept here (AGENTS.md): never promotes (RECEIPT.json says candidate_only/promoted false; promotion is only
scripts/ethan_promote.py --approved-by after ethan_si_loop.py rollout --split eval + gate); never stops or starts the model
server; refuses while port 18190 has a listener, a llama-server is found, GPU_WINDOW is held, STOP is set, or the GPU is
above the guard's start limit. Heat limits come from ethan_thermal_guard (pause 90/99, resume 87/95, abort 93): a pause is a
real fault, so the trainer checkpoints first, waits, and gives up (checkpointed) after --max-pause-s.
Outputs: data/training/gold_adapter/<stamp>/ {config.json, train.log.jsonl, checkpoint-N/, adapter/, RECEIPT.json, *.gguf}.
"""
import argparse, hashlib, json, math, os, random, socket, subprocess, sys, time
from pathlib import Path
import ethan_thermal_guard as tg

def sha256_file(p):
    raise NotImplementedError('TODO: implement')

def latest_gold(root=...):
    raise NotImplementedError('TODO: implement')

def load_manifest(gold_dir):
    raise NotImplementedError('TODO: implement')

def find_base(extra=...):
    """HF-format base (config.json + *.safetensors + tokenizer) or None. QLoRA cannot start from the GGUF."""
    raise NotImplementedError('TODO: implement')

def fix_messages(msgs):
    """Bridge rows carry tool_call arguments as JSON strings; the Qwen2.5 template wants dicts (else it double-encodes)."""
    raise NotImplementedError('TODO: implement')

def row_tools(row):
    raise NotImplementedError('TODO: implement')

def encode_row(tok, row, max_len):
    """-> {'input_ids','labels'} loss on the completion tokens only, or None if longer than max_len (never truncated)."""
    raise NotImplementedError('TODO: implement')

def length_stats(lens):
    raise NotImplementedError('TODO: implement')

def estimate_vram_gib(max_len, cfg=..., r=16, quant_lm_head=True):
    """Analytic [estimate] for micro-batch 1, NF4 base, bf16 embeddings, LoRA r16 fp32 + grads + 8-bit Adam, grad checkpointing."""
    raise NotImplementedError('TODO: implement')

def estimate_wall(tokens_per_epoch, epochs, tok_per_s=..., duty=0.8):
    raise NotImplementedError('TODO: implement')

def build_schedule(n, accum, epochs, seed=...):
    raise NotImplementedError('TODO: implement')

def lr_at(step, total, warmup, peak):
    raise NotImplementedError('TODO: implement')

def latest_checkpoint(out_dir):
    raise NotImplementedError('TODO: implement')

def find_resumable(root, data_sha):
    """Newest run dir with the same data hash, a checkpoint and no finished receipt."""
    raise NotImplementedError('TODO: implement')

def write_json(path, obj):
    raise NotImplementedError('TODO: implement')

def server_listening(port=...):
    raise NotImplementedError('TODO: implement')

def gpu_free_mib():
    raise NotImplementedError('TODO: implement')

def preflight(min_free_mib, owner=..., listen_fn=..., find_fn=None, free_fn=..., temp_fn=None, window=..., stop=None, ram_fn=None):
    """Plain-language reasons the run cannot start now. Empty list = GPU is free."""
    raise NotImplementedError('TODO: implement')

class ThermalPause:
    """Called before every micro-batch. Pauses (after a checkpoint) at the guard's pause levels and resumes at its resume levels."""

    def __init__(self, gpu_fn=None, cpu_fn=None, sleep_fn=..., now_fn=..., stop_path=None, log=None, max_pause_s=1800, poll_s=10):
        raise NotImplementedError('TODO: implement')

    def _read(self):
        raise NotImplementedError('TODO: implement')

    def check(self, step, checkpoint_fn=None):
        """'ok' (carry on, possibly after a pause) or 'abort' (checkpointed; self.reason says why)."""
        raise NotImplementedError('TODO: implement')

def make_receipt(cfg, status, losses, seconds, thermal, steps_done, total_steps, peak_vram_mib, extra=None):
    raise NotImplementedError('TODO: implement')

def build_config(a, gold_dir, manifest, data_sha, base):
    raise NotImplementedError('TODO: implement')

def measure_lengths(gold_dir, tok_dir, max_len):
    """Token lengths of train.jsonl. Uses the Qwen2.5 tokenizer when the HF base is present, else the Qwen3 proxy (labelled)."""
    raise NotImplementedError('TODO: implement')

def plan(a):
    raise NotImplementedError('TODO: implement')

def run(a):
    raise NotImplementedError('TODO: implement')

def export(a):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
