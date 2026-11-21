# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""RETIRED 2026-11-01: One-off conversation scraper / compactor-adapter stager.

Why: it was tied to one past session, has no callers, and never trained anything; the base is not the served model family.
Use instead: scripts/ethan_sft_lora.py to train, then scripts/ethan_promote.py to promote (the promote pipeline writes the
receipt that scripts/ethan_model_identity.py --check requires).
Original kept at archive/2026-11-01/identity-resolve/assess_current_conversation_and_train_adapter.py.orig (and in git history).
"""
import sys

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
