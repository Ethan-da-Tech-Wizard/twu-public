# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""RETIRED 2026-11-01: Unified 1B training/GGUF pipeline (Unsloth).

Why: Unsloth needs unsloth_zoo (LGPL-3.0), which the permissive-license rule forbids; the base is not the served model family.
Use instead: scripts/ethan_sft_lora.py to train, then scripts/ethan_promote.py to promote (the promote pipeline writes the
receipt that scripts/ethan_model_identity.py --check requires).
Original kept at archive/2026-11-01/identity-resolve/train_and_export_pipeline.py.orig (and in git history).
"""
import sys

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
