# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Seeded Monte-Carlo of ethan_si_math.gate_decision: false-promotion rate, power, regression-guard rate.
Deterministic (random.Random(seed), no clock, no network). Never writes data/self_improve/formulas.json; the CLI writes
data/self_improve/formulas.proposed.json (a full copy with only gate.z / gate.min_eval_attempts changed).

  python3 -B scripts/ethan_si_sim.py calibrate [--delta 0.2] [--trials 2000] [--seed 146] [--no-write]
"""
import argparse, bisect, copy, json, math, random, sys
from pathlib import Path
import ethan_si_math as M

def _binom_sampler(n, p):
    """Inverse-CDF binomial: one rng.random() per draw, so streams are cheap and reproducible."""
    raise NotImplementedError('TODO: implement')

def _samples(true_base, true_cand, n_eval, n_train, trials, seed):
    raise NotImplementedError('TODO: implement')

def _score(samples, n_eval, n_train, formulas):
    raise NotImplementedError('TODO: implement')

def simulate_gate(true_base, true_cand, n_eval, n_train, formulas, trials, seed):
    """Promotion rate and regression-guard trigger rate over `trials` simulated baseline/candidate evaluations."""
    raise NotImplementedError('TODO: implement')

def _with_gate(formulas, z, n):
    raise NotImplementedError('TODO: implement')

def _false_rates(n, n_train, trials, seed):
    raise NotImplementedError('TODO: implement')

def _power_sets(n, n_train, delta, trials, seed):
    raise NotImplementedError('TODO: implement')

def calibrate(target_false_promotion=0.05, target_power=0.8, delta=0.2, formulas=None, seed=146, trials=2000, n_train=..., n_grid=..., z_grid=...):
    """Smallest eval-attempt count n (and a z) with worst-case false promotion <= target (over true rates 0.1..0.9)
    and worst-case power >= target (over base rates where base+delta <= 0.95). Reads formulas; never writes."""
    raise NotImplementedError('TODO: implement')

def propose(formulas, result, path=...):
    """Write the proposed formulas (full copy, only gate.z / gate.min_eval_attempts changed). Refuses the live file."""
    raise NotImplementedError('TODO: implement')

def current_profile(formulas, trials, seed, n_train=..., deltas=...):
    raise NotImplementedError('TODO: implement')

def _logit(p):
    raise NotImplementedError('TODO: implement')

def _draw_task_probs(rng, n_tasks, mean, kappa):
    """Per-task true pass probability ~ Beta(mean*kappa, (1-mean)*kappa); small kappa = strong heterogeneity."""
    raise NotImplementedError('TODO: implement')

def _binomial(rng, n, p):
    raise NotImplementedError('TODO: implement')

def _clustered_trial(rng, n_tasks, attempts, mean, kappa, delta, tau, mode):
    raise NotImplementedError('TODO: implement')

def _old_gate_on_tasks(base, cand, f):
    raise NotImplementedError('TODO: implement')

def _cluster_formulas(formulas, n_tasks, attempts, alpha=None, old_z=None):
    raise NotImplementedError('TODO: implement')

def simulate_clustered(n_tasks, attempts, delta, formulas, trials=800, seed=146, mean=0.5, kappa=6.0, tau=0.5, mode=..., old_z=None, alpha=None):
    """Promotion rates of the OLD attempt-level gate (pooled counts, min_eval_attempts relaxed to 1 so small designs are
    visible) and the NEW clustered gate on identical simulated data. delta=0 is the no-true-gain case (tau still moves
    individual tasks up and down, as real candidates do). Deterministic in `seed`."""
    raise NotImplementedError('TODO: implement')

def calibrate_clustered(formulas=None, trials=800, seed=146, mean=0.5, kappa=6.0, tau=0.5, mode=..., tasks=..., attempts=..., deltas=..., target_power=0.8, power_delta=0.2, old_z=None):
    raise NotImplementedError('TODO: implement')

def propose_clustered(formulas, best, path=..., alpha=0.05):
    raise NotImplementedError('TODO: implement')

def _cmd_clustered(a):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
