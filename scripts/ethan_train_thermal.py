# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Run the SFT trainer thermally constrained: power-saver profile, CPU cap, niced, pinned cores. No root, no fan changes.

The CPU shares heat pipes and fans with the GPU, so CPU heat steals the GPU's thermal budget. Training is GPU-bound, so
the trainer's CPU side is cheap to cap. The previous power profile is restored in a finally block (also on SIGTERM/SIGINT).

  python3 scripts/ethan_train_thermal.py [--cores 12-15] [--quota 150] [--no-powersave] -- <python> scripts/ethan_sft_lora.py ...
"""
import argparse, os, shutil, signal, subprocess, sys

def profile_get(run=...):
    raise NotImplementedError('TODO: implement')

def profile_set(name, run=...):
    raise NotImplementedError('TODO: implement')

def build_command(cmd, cores=..., quota=150, weight=20, nice=19, have=...):
    """Wrap `cmd` as: systemd-run --user --scope (CPUQuota, CPUWeight) -> nice -> taskset -> cmd. Missing tools are skipped."""
    raise NotImplementedError('TODO: implement')

def main(argv=None, run=..., get=..., setp=...):
    raise NotImplementedError('TODO: implement')
