# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/ethan_evolve.py - the workspace improves itself by measured math, with no model and no GPU.

The loop (one "pull"):  measure J  ->  choose an improvement action  ->  apply it  ->  measure J again  ->  keep or roll back  ->  learn.

J ("system debt", lower is better) is read from artifacts, never from anyone's claim:
    J = (missing touchpoints over all wired-in code files, from the wiring sheet)  +  5 x (scavenger errors)  +  2 x (knowledge index stale)
        + 1 x (problems reported by `enki tools check`) + 3 x (failing real journeys) + 1 x (journeys not run in 48 hours)

Choosing: every action is an arm of a multi-armed bandit.  Success of a pull = J went DOWN and no guard got worse (a guard compares its problem list before and after, so a failure that
  already existed is not blamed on the arm).
  - Thompson sampling: draw theta_a ~ Beta(1 + successes, 1 + failures); expected value per second = theta_a * mean_gain_a / mean_cost_a.
    Pick the arm with the highest draw.  Rarely-tried arms stay uncertain, so they get explored; proven arms get exploited.
  - mean_gain is shrunk toward a prior (1 point, weight 2 pulls) so one lucky pull cannot dominate.
  - Retirement: an arm with at least MIN_PULLS_TO_RETIRE pulls whose success rate is clearly below RETIRE_FLOOR (Bayesian check from
    scripts/ethan_doe.py) is retired and never pulled again until a person resets it (floor 20 percent, probability 0.95: about 13 straight failures).
  - An arm with nothing to do (not eligible) is skipped, not counted as a failure.
Measurement rules (Goodhart guard; the whole philosophy is in docs/SELF_IMPROVEMENT_MATH.md):
  - Files under private/ stay IN J (real code, the sheet scores them on purpose) but no arm may edit them: they are reported as gaps_private,
    "debt only a person can pay".  Nothing is hidden; J is never lowered by dropping files.
  - NO exclusions: every failing journey counts, including the one that reports the others' count (nothing proves it cannot fail on its own).
  - Junk is reported (from one_touch.py, which owns the cleaner and its audit); it is not added to J.
Safety: honours the STOP latch; backs up every file an arm may change to archive/<date>/evolve-<time>/ first; restores them if J got
worse or a guard failed; stdlib only; arms are a closed, reviewed list of existing deterministic commands.  Reflections and results
are evidence, not authority: this never edits policy, instructions, tests or code; it only regenerates derived registries/indexes.

  python3 scripts/ethan_evolve.py status            J now, trend (slope with 95% interval), each arm's posterior and decision
  python3 scripts/ethan_evolve.py propose [--n 3]   Thompson-ranked arms that are eligible now (no changes)
  python3 scripts/ethan_evolve.py run [--max-pulls 1] [--seed S] [--dry-run] [--arm NAME]
  python3 scripts/ethan_evolve.py reset ARM         lift a retirement (owner decision)
"""
from __future__ import annotations
import argparse
import datetime as dt
import fcntl
import hashlib
import json
import math
import random
import re
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path

def measure(root: Path=...) -> dict:
    """J from artifacts. Rebuilds the wiring sheet in memory (reads sources) and re-runs the scavenger check; both are read-only."""
    raise NotImplementedError('TODO: implement')

def journey_counts(root: Path) -> dict:
    """Failing/stale journey counts. Every failing journey counts; nothing is excluded."""
    raise NotImplementedError('TODO: implement')

def failing_journeys(root: Path) -> list:
    raise NotImplementedError('TODO: implement')

def sense(root: Path) -> None:
    """Sensing, not improving: run the real journeys that are due, so J reflects what actually works today. Its results are
    evidence and are never rolled back."""
    raise NotImplementedError('TODO: implement')

def problems(root: Path, argv: list) -> set:
    """What a guard command complains about, as a set. JSON {"problems": [...]} is read when present; otherwise a non-zero exit is one problem."""
    raise NotImplementedError('TODO: implement')

def scavenger_errors(root: Path) -> int:
    raise NotImplementedError('TODO: implement')

def knowledge_stale(root: Path) -> bool:
    raise NotImplementedError('TODO: implement')

def _sh(root: Path, args: list, timeout: int=600) -> bool:
    raise NotImplementedError('TODO: implement')

def _untested_unlisted(root: Path) -> list:
    raise NotImplementedError('TODO: implement')

class Arm:
    """files = what the arm may change (backed up, restored). allow = evidence it may append to that is never rolled back.
    proof = a win also needs apply() to return {"fixed": [...]}. gain_cap = the most J-gain one pull of this arm may be credited."""

    def __init__(self, name, files, eligible, apply, guards=..., allow=..., proof=False, gain_cap=None):
        raise NotImplementedError('TODO: implement')

def _load(root: Path, rel: str, default):
    raise NotImplementedError('TODO: implement')

def wiring_candidates(root: Path) -> list:
    """scripts/X.py with a scripts/test_X.py, in no manifest row and not named in MOVING_PARTS.md: the 'wiring' touchpoint is missing and fixable."""
    raise NotImplementedError('TODO: implement')

def _run_test(root: Path, stem: str, mode: str=...) -> int | None:
    """Return code of the test inside the capped example_host; None when it timed out. mode '' = real tool; 'raise' = importing the tool raises;
    'noop' = every public function and method of the tool returns None."""
    raise NotImplementedError('TODO: implement')

def _test_passes(root: Path, stem: str) -> bool:
    """A test earns a wiring row only if it is MEANINGFUL: it passes on the real tool, FAILS when importing the tool raises, and FAILS when
    every public function of the tool returns None. A test that survives the sabotage proves nothing about the tool (assertTrue(True)) and earns nothing."""
    raise NotImplementedError('TODO: implement')

def wiring_rows_apply(root: Path, tester=None) -> bool:
    raise NotImplementedError('TODO: implement')

def rerun_candidates(root: Path) -> list:
    """Failing journeys whose cause has been recorded AND marked resolved by a fix (`ethan_evolve.py resolve ID note`): the re-run only CONFIRMS the fix.
    A failing journey with an unresolved cause is never re-run until green."""
    raise NotImplementedError('TODO: implement')

def _journey_last(root: Path, jid: str):
    raise NotImplementedError('TODO: implement')

def rerun_apply(root: Path, runner=None, last=None) -> dict:
    """Re-run up to 3 candidate journeys. The first failure is the truth: a journey is FIXED only if it passes RERUN_N times in a row (stop at the
    first failure, so a flaky journey ends on a failed run and stays failing). Records cause_before and the flake rate for every journey."""
    raise NotImplementedError('TODO: implement')

def default_arms(root: Path=...) -> list:
    raise NotImplementedError('TODO: implement')

def _sync_and_smoke(root: Path) -> bool:
    raise NotImplementedError('TODO: implement')

def betainc_sample(rng: random.Random, a: float, b: float) -> float:
    raise NotImplementedError('TODO: implement')

def read_ledger(root: Path) -> list:
    raise NotImplementedError('TODO: implement')

def eff_update(state: tuple, t: int, success: bool) -> tuple:
    """Exponentially forgotten counts. state = (weighted wins, weighted losses, time of last update). Pure; one pull at time t."""
    raise NotImplementedError('TODO: implement')

def eff_read(state: tuple, now: int) -> tuple:
    raise NotImplementedError('TODO: implement')

def eff_fields(state: tuple, now: int) -> dict:
    raise NotImplementedError('TODO: implement')

def arm_stats(ledger: list, name: str) -> dict:
    """Raw counts (pulls, successes, failures) plus forgetting-weighted eff_* counts used for choosing and retiring. A 'reinstated' marker starts the arm fresh."""
    raise NotImplementedError('TODO: implement')

def thompson_value(stats: dict, rng: random.Random) -> float:
    raise NotImplementedError('TODO: implement')

def retired_decision(stats: dict) -> str:
    """Bayesian stop rule reused from ethan_doe: clearly below the floor after enough pulls -> retire. It uses the RAW record, so a bad arm is
    stopped for good measure; forgetting (eff_*) steers choosing, and scheduled probes (probe_due/reinstated) are how a retired arm can come back."""
    raise NotImplementedError('TODO: implement')

def probe_due(t: int, last_t: int, failed_probes: int, last_probe_ok: bool=False) -> bool:
    """One probe of a retired arm: every PROBE_EVERY pulls, doubling (to x64) after each failed probe, back to base after a good one."""
    raise NotImplementedError('TODO: implement')

def _p_above(successes: int, n: int, floor: float) -> float:
    raise NotImplementedError('TODO: implement')

def reinstated(probes: list) -> bool:
    """Bayesian evidence to lift a retirement: among the last 3 probes at least 2 won and P(rate > floor) >= 0.95. One lucky probe is not evidence."""
    raise NotImplementedError('TODO: implement')

def trend(points: list) -> dict:
    """Ordinary least squares of J on time (days) with a normal-approximation 95% interval for the slope.
    points = [(ts_days, J)] or [(ts_days, J, measure_version)].  Only points at the CURRENT measure version are used, and a jump of more than JUMP
    between two consecutive points is a re-baseline (the code or the measurement changed), so the fit starts after the last jump."""
    raise NotImplementedError('TODO: implement')

def retired_set(root: Path) -> set:
    raise NotImplementedError('TODO: implement')

def rank(arms: list, ledger: list, rng: random.Random, root: Path, eligible_only: bool=True) -> list:
    raise NotImplementedError('TODO: implement')

def on_battery() -> bool:
    """True when the machine reports mains power is absent (a laptop on battery should not do upkeep work)."""
    raise NotImplementedError('TODO: implement')

def calm() -> str:
    """Empty when it is fine to run; otherwise why not. This loop is CPU work: it waits while the laptop is hot or busy."""
    raise NotImplementedError('TODO: implement')

def stopped(root: Path) -> bool:
    raise NotImplementedError('TODO: implement')

def redact(text: str, n: int=220) -> str:
    raise NotImplementedError('TODO: implement')

def classify_cause(text: str) -> str:
    raise NotImplementedError('TODO: implement')

def read_causes(root: Path) -> list:
    raise NotImplementedError('TODO: implement')

def record_cause(root: Path, kind: str, ident: str, cause: str, evidence: str=..., resolved: bool=False, note: str=...) -> None:
    raise NotImplementedError('TODO: implement')

def cause_state(root: Path) -> dict:
    """Latest record per id: {id: {"cause","resolved","time"}}. A new unresolved record after a resolve re-opens the cause."""
    raise NotImplementedError('TODO: implement')

def record_journey_causes(root: Path) -> int:
    """Classify every currently failing journey (the echo journey counts like any other) and note its cause once per change."""
    raise NotImplementedError('TODO: implement')

def blocked(root: Path, ledger: list, name: str) -> bool:
    raise NotImplementedError('TODO: implement')

def top_causes(root: Path, n: int=3) -> list:
    raise NotImplementedError('TODO: implement')

class NeedsHuman(OSError):
    """A rollback could not be completed or verified. The loop stops until a person clears data/autoimprove/evolve/NEEDS_HUMAN."""

def watched_files(root: Path) -> list:
    raise NotImplementedError('TODO: implement')

def fingerprint(root: Path) -> dict:
    raise NotImplementedError('TODO: implement')

def _declared(rel: str, arm: Arm) -> bool:
    raise NotImplementedError('TODO: implement')

def _sha(p: Path) -> str:
    raise NotImplementedError('TODO: implement')

def backup(root: Path, arm: Arm, stamp: str) -> Path:
    """Copy declared paths and every small watched file, and record a sha256 for each copy so a corrupt backup is never trusted."""
    raise NotImplementedError('TODO: implement')

def _manifest(dest: Path) -> dict:
    raise NotImplementedError('TODO: implement')

def verify_backup(dest: Path) -> None:
    raise NotImplementedError('TODO: implement')

def restore(root: Path, arm: Arm, dest: Path, undeclared=...) -> None:
    """Verify the backup, put every declared path (and any undeclared write) back, then verify the live files byte for byte. Raises NeedsHuman if anything is off."""
    raise NotImplementedError('TODO: implement')

def _append(root: Path, rec: dict) -> None:
    raise NotImplementedError('TODO: implement')

def pull(root: Path, arm: Arm, before: dict, measure_fn, seed: int, probe: bool=False) -> dict:
    raise NotImplementedError('TODO: implement')

def load_budget(root: Path) -> dict:
    raise NotImplementedError('TODO: implement')

def _ts_age_s(ts: str, now: dt.datetime) -> float:
    raise NotImplementedError('TODO: implement')

def budget_block(ledger: list, budget: dict, now: dt.datetime | None=None) -> str:
    raise NotImplementedError('TODO: implement')

def apply_priority(budget: dict) -> None:
    """Lower this process's CPU and disk priority (best effort; never fatal)."""
    raise NotImplementedError('TODO: implement')

def junk_status(root: Path):
    """Measured junk from `one_touch.py junk --status --json` (J1/J2 own the cleaner and the independent audit). None when that command does not exist yet."""
    raise NotImplementedError('TODO: implement')

def junk_apply(root: Path) -> dict:
    """Run the owner's sweep once. A win needs the measured junk to fall (checked here) and the J/guard/undeclared-write rules of every pull (checked in pull)."""
    raise NotImplementedError('TODO: implement')

def run(root: Path, arms: list, measure_fn, max_pulls: int=1, seed: int | None=None, dry: bool=False, calm_fn=..., sense_fn=..., only: str | None=None, budget: dict | None=None, sleep_fn=...) -> list:
    """One run. Only one run at a time (flock); honours STOP, NEEDS_HUMAN, thermal, battery and the work budget (budget=None means no limits)."""
    raise NotImplementedError('TODO: implement')

def _probe_pick(root: Path, arms: list, ledger: list, only):
    """A retired arm whose turn for one probe has come (None otherwise)."""
    raise NotImplementedError('TODO: implement')

def _maybe_reinstate(root: Path, name: str) -> bool:
    raise NotImplementedError('TODO: implement')

def _run_locked(root, arms, measure_fn, max_pulls, seed, dry, calm_fn, sense_fn, only, budget, sleep_fn) -> list:
    raise NotImplementedError('TODO: implement')

def measure_cached(root: Path):
    raise NotImplementedError('TODO: implement')

def status(root: Path, arms: list) -> str:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
