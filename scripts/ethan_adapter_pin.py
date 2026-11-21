# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Pin LoRA adapters to their base model and verify before serving (deterministic, read-only on weights).

  create / verify / launch-args / list / register-hint

No network, no model or GPU calls, never writes next to weights. Only `create` writes, and only one small JSON
into the pins dir (default data/example_host/adapters, override with --pins-dir or ETHAN_ADAPTER_PINS_DIR).
GGUF headers are parsed with a minimal pure-python reader (no gguf package needed; arrays are skipped).
`launch-args` only prints arguments after verify passes; it never starts a server.
"""
import argparse, hashlib, json, os, re, shlex, socket, struct, sys, time

class PinError(Exception):
    pass

def pins_dir(arg):
    raise NotImplementedError('TODO: implement')

def pin_path(name, pdir):
    raise NotImplementedError('TODO: implement')

def refuse_symlink(path, label):
    raise NotImplementedError('TODO: implement')

def sha256_file(path):
    raise NotImplementedError('TODO: implement')

def hash_artifact(path, label):
    """File -> (sha256, size). Directory (HF base) -> sha256 over sorted 'relpath:sha:size' lines, total size."""
    raise NotImplementedError('TODO: implement')

def _u32(f):
    raise NotImplementedError('TODO: implement')

def _u64(f):
    raise NotImplementedError('TODO: implement')

def _str(f):
    raise NotImplementedError('TODO: implement')

def _skip_value(f, t):
    raise NotImplementedError('TODO: implement')

def read_gguf(path, tensors=False):
    """Return {'version','tensor_count','kv':{scalars/strings only},'tensors':[(name,dims)] if asked}."""
    raise NotImplementedError('TODO: implement')

def lora_rank(tensors):
    """Rank from lora_a tensors (ggml ne = [in, r]); None if absent; error if inconsistent."""
    raise NotImplementedError('TODO: implement')

def base_info(path):
    raise NotImplementedError('TODO: implement')

def adapter_info(path):
    raise NotImplementedError('TODO: implement')

def check_approval(ref, required):
    """Only checks that the referenced promotion receipt/disposition file EXISTS. Never creates or approves."""
    raise NotImplementedError('TODO: implement')

def cmd_create(a):
    raise NotImplementedError('TODO: implement')

def load_pin(name, pdir):
    raise NotImplementedError('TODO: implement')

def do_verify(a):
    raise NotImplementedError('TODO: implement')

def cmd_verify(a):
    raise NotImplementedError('TODO: implement')

def cmd_launch(a):
    raise NotImplementedError('TODO: implement')

def model_info(path):
    raise NotImplementedError('TODO: implement')

def cmd_create_model(a):
    raise NotImplementedError('TODO: implement')

def load_model_pin(name, pdir):
    raise NotImplementedError('TODO: implement')

def do_verify_model(a):
    raise NotImplementedError('TODO: implement')

def cmd_verify_model(a):
    raise NotImplementedError('TODO: implement')

def cmd_launch_model(a):
    raise NotImplementedError('TODO: implement')

def cmd_list(a):
    raise NotImplementedError('TODO: implement')

def cmd_hint(a):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
