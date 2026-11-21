# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Dataset generator for Mac model personalities (Orchestrator, Coder, Checker, Aggregator).

Generates verified, synthetic SFT/distillation training pairs conforming to the role schemas
in private/example_host/distill/roles/. Enforces cloud_guard privacy invariants on every record.
"""
import json
import os
import sys
from pathlib import Path

def generate_all():
    raise NotImplementedError('TODO: implement')
