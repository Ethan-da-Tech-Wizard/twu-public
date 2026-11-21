# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Self-heal our own failed/inactive user units so a startup alarm never has to be fixed by hand.

Zero-model, one-shot (run from ethan-alarm.service after the alarm check). For units named ethan-*, twu-*
or enki-* only. Escalation ladder per failed unit, with atomic state in selfheal_state.<host>.json:
  1. capture root cause (systemctl show Result/ExecMainStatus -> timeout/exit-code/signal/oom class plus a
     one-line suggested fix, logged only; unit files are never edited),
  2. `reset-failed`, then verify (is-failed),
  3. a oneshot SERVICE on the explicit RETRY allowlist (cheap monitors) whose timer is active is re-triggered
     with `systemctl --user start <service>` and verified; model/training/GPU units are never retried,
  4. crash-loop breaker: more than MAX_HEALS_PER_HOUR (3) heals of one unit in a rolling hour stops healing it,
     captures `journalctl --user -u <unit> -n 30` into the state file and raises the alarm
     'needs-human: <unit> keeps failing' (ethan_alarm.check_selfheal reads this host's state file).
Also starts an ENABLED timer that is inactive. Never enables a disabled unit. Does nothing under the STOP
latch; under MODEL_STANDBY or a PAUSE marker it still clears failed state and restarts the sensor timers
(build_mode.SENSORS) but no others. Heavy starts (retries, non-sensor timers) are skipped while CPU>=99C or
GPU>=90C. A unit listed in data/health/SELFHEAL_HOLD (one name per line, or `all`) is untouched; ethan-evolve,
ethan-certify and ethan-volley are held by default. One run at a time per host (`selfheal.<host>.lock`) and at
most MAX_ACTIONS (5) mutations per run. Missing host state seeds from the legacy shared state without modifying it.
CLI: --dry-run (no mutation, no state write), --status. Results go to `selfheal.<host>.jsonl`.
"""
from __future__ import annotations
import fcntl, json, math, os, platform, re, subprocess, sys, time
from pathlib import Path
import stop_latch
from build_mode import SENSORS

def host_path(stem, suffix, host=None):
    """Return a shared-workspace runtime path with one writer per host."""
    raise NotImplementedError('TODO: implement')

def sh(cmd, run=..., timeout=20):
    raise NotImplementedError('TODO: implement')

def global_hold(stop_path=None, markers=None, soft=False):
    """Return the reason self-heal must do nothing, or None. STOP is always hard; the standby/pause markers
    are 'soft' holds (see heal): they only stop timers outside the sensor set from being restarted."""
    raise NotImplementedError('TODO: implement')

def held_units(hold_file=None):
    """Names (without suffix) that must not be touched; the string 'all' means everything."""
    raise NotImplementedError('TODO: implement')

def is_held(unit, held):
    raise NotImplementedError('TODO: implement')

def failed_units(run=...):
    """Return the observed failures, or None when enumeration is unavailable."""
    raise NotImplementedError('TODO: implement')

def idle_enabled_timers(run=...):
    raise NotImplementedError('TODO: implement')

def thermal_hot(gpu=None, cpu=None):
    """Reason string when CPU>=99C or GPU>=90C (thermal guard limits), else None. Unreadable sensors are not hot."""
    raise NotImplementedError('TODO: implement')

def classify(run, unit):
    """(cause, hint) from `systemctl --user show -p Result,ExecMainStatus,ExecMainCode`; call BEFORE reset-failed."""
    raise NotImplementedError('TODO: implement')

def journal_tail(unit, run=...):
    raise NotImplementedError('TODO: implement')

class StateReadError(RuntimeError):
    pass

def load_state(path=None):
    raise NotImplementedError('TODO: implement')

def save_state(state, path=None):
    raise NotImplementedError('TODO: implement')

def needs_human(path=None):
    """{unit: evidence summary} for units the breaker gave up on (read by ethan_alarm)."""
    raise NotImplementedError('TODO: implement')

def _verify_failed(run, unit):
    raise NotImplementedError('TODO: implement')

def _path_state(run, unit):
    raise NotImplementedError('TODO: implement')

def heal(run=..., hold=None, held=None, soft=None, state_path=None, dry_run=False, hot=None, now=None, max_actions=..., journal=None):
    """Return a list of actions taken (or a single skip record)."""
    raise NotImplementedError('TODO: implement')

def load_alarm_fix_state(path=None):
    raise NotImplementedError('TODO: implement')

def fix_commands(problems):
    """Distinct `fix: <cmd>` strings carried by alarm texts (dict of key -> text, or {key: {"text":..}})."""
    raise NotImplementedError('TODO: implement')

def gpu_busy(run=...):
    """True when GPU utilisation >= GPU_BUSY_PCT (a heavy GPU job). Unreadable counts as not busy."""
    raise NotImplementedError('TODO: implement')

def heal_alarms(problems, popen=..., now=None, state_path=None, hold=None, hot=None, busy=None, dry_run=False, lock_path=None):
    """Start (detached, under `flock -n`, so a run never overlaps another) the allow-listed fix for each alarm that
    carries one. Per-command debounce ALARM_FIX_DEBOUNCE, recorded when started so failures are debounced too."""
    raise NotImplementedError('TODO: implement')

def _own_alarms():
    raise NotImplementedError('TODO: implement')

def _log(actions):
    raise NotImplementedError('TODO: implement')

def run_once(dry_run=False, lock_path=None):
    raise NotImplementedError('TODO: implement')

def status(path=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
