# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Deterministic attempt scheduler for the self-improvement loop.

Decides how many attempts each task gets in the next rollout from a total budget, weighting tasks by
ethan_si_math.task_priority (untried and ~50% tasks get the most). Pure functions, no randomness.

  ethan_si_sched.py plan --budget 40 [--runs NAME ...] [--include-eval]
"""
import argparse, json, sys
from fractions import Fraction
from pathlib import Path
import ethan_si_bank as bank
import ethan_si_math as sim

def task_stats(records):
    """{task_id: (passes, n)} from run records; only label PASS counts as a pass."""
    raise NotImplementedError('TODO: implement')

def allocate(tasks, stats, budget, formulas, include_eval=False, min_each=1):
    """{task_id: attempts}; sums exactly to budget (if any task is selected). Ties break by task id."""
    raise NotImplementedError('TODO: implement')

def order(allocation):
    """Round-robin task order: one attempt per task per pass, so a cutoff still samples every task."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
