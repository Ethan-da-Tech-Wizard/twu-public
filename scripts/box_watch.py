# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""box_watch: unprivileged watcher for the gaps the other guards leave. No root, no model, no network, never kills anything.

  box_watch.py check    run every check, write data/netguard/box_watch.<host>.json, print plain sentences; exit 1 on problems
  box_watch.py learn [--yes] [--accept-shrink]
                        accept the CURRENT state as the baseline (only ever run by hand, after reading `check`). Prints what
                        changed since the last manifest first; more than 5 changed files needs --yes (or an interactive y);
                        a guard baseline that lost more than 30% of its entries needs --accept-shrink
  box_watch.py show     print the current inventory without comparing

Checks: (1) watcher-of-watchers: hashes of monitor scripts, their systemd units (repo copy vs installed copy) and
baselines/ledgers against the learned manifest, plus every expected twu-* guard timer active and recently run;
(3) docker containers/images (honestly 'unavailable' when the daemon is not reachable unprivileged);
(4) USB devices and bluetooth devices; (7) new/removed RPM or pacman packages, disk usage and growth rate, and which
process holds a camera or microphone. Each problem is one sentence ending in `fix:`.
"""
from __future__ import annotations
import glob, hashlib, json, os, re, shutil, socket, subprocess, sys, time
from pathlib import Path

def alarm_unit_name(host):
    raise NotImplementedError('TODO: implement')

def timer_specs(host):
    raise NotImplementedError('TODO: implement')

class Env:
    """Everything the checks touch from the machine, injectable for tests."""

    def __init__(self, root=..., home=..., host=..., run=None, now=None, usb_root=..., pacman_log=..., proc_root=..., disk=None, uptime=None):
        raise NotImplementedError('TODO: implement')

    @staticmethod
    def _real_run(cmd, timeout=10):
        raise NotImplementedError('TODO: implement')

    def run(self, cmd, timeout=10):
        raise NotImplementedError('TODO: implement')

    def up(self):
        raise NotImplementedError('TODO: implement')

def sha(path):
    raise NotImplementedError('TODO: implement')

def _full_sha(path):
    """Receipt fingerprints compare the exact inputs, never act as approval."""
    raise NotImplementedError('TODO: implement')

def jload(path, default):
    raise NotImplementedError('TODO: implement')

def jsave(path, data):
    raise NotImplementedError('TODO: implement')

def watched_files(env):
    """label -> (path, kind). kind: script | unit | installed | baseline | ledger."""
    raise NotImplementedError('TODO: implement')

def file_hashes(env):
    raise NotImplementedError('TODO: implement')

def head_hash(env, path):
    """Hash of the committed (git HEAD) version of a repo file, or None when git cannot say (not a repo, untracked)."""
    raise NotImplementedError('TODO: implement')

def entry_count(data):
    """How much coverage a baseline holds: scalars count 1, lists and dicts count their length."""
    raise NotImplementedError('TODO: implement')

def baseline_counts(env):
    raise NotImplementedError('TODO: implement')

def ledger_shape(path):
    """({key: first_seen}, None) for a well-formed port ledger, else (None, why)."""
    raise NotImplementedError('TODO: implement')

def usb_inventory(env):
    raise NotImplementedError('TODO: implement')

def bt_inventory(env):
    raise NotImplementedError('TODO: implement')

def docker_inventory(env):
    raise NotImplementedError('TODO: implement')

def pacman_events(env, since=...):
    raise NotImplementedError('TODO: implement')

def rpm_identity(value):
    """Return the package name/architecture separately from its installed version."""
    raise NotImplementedError('TODO: implement')

def rpm_inventory(env):
    """Only a successful, nonempty, well-formed whole RPM query is comparable."""
    raise NotImplementedError('TODO: implement')

def disk_now(env):
    raise NotImplementedError('TODO: implement')

def pid_comm(env, pid):
    raise NotImplementedError('TODO: implement')

def av_holders(env):
    """{'camera': [names], 'mic': [names]} or None per kind when it cannot be read."""
    raise NotImplementedError('TODO: implement')

def snapshot(env):
    raise NotImplementedError('TODO: implement')

def parse_systemd_time(text):
    raise NotImplementedError('TODO: implement')

def check_integrity(env, base, notes=None):
    raise NotImplementedError('TODO: implement')

def check_ledgers(env, base, state):
    """A self-refreshing ledger changes every run, so pin its SHAPE not its bytes: valid JSON, well-formed entries, no entry
    deleted, no first_seen moved later. Tampering that rewrites history shows; normal growth does not."""
    raise NotImplementedError('TODO: implement')

def check_baseline_coverage(env, base, state):
    """A guard's baseline may only shrink its coverage by an explicit human command (learn --accept-shrink)."""
    raise NotImplementedError('TODO: implement')

def check_timers(env):
    raise NotImplementedError('TODO: implement')

def diff_list(label, cur, was, noun, fixword):
    raise NotImplementedError('TODO: implement')

def check_usb_bt(env, base):
    raise NotImplementedError('TODO: implement')

def check_docker(env, base):
    raise NotImplementedError('TODO: implement')

def check_pacman(env, base):
    raise NotImplementedError('TODO: implement')

def check_free_space(env, state):
    """Alarm on LOW ABSOLUTE FREE SPACE, which the percentage limit in check_disk misses on small disks.
    PROGRAM: box_watch.py check_free_space   PROGRAMMER: Magi 10   LAST MODIFIED: 2026-11-19
    PURPOSE: a 111 GB disk at 85% (16 GB free) never reaches the 90% alarm, yet is close to trouble.
    Read-only. On example_host (btrfs) the fix text names the real causes found 2026-11-19: Steam games,
    Syncthing .stversions and archived conflict copies, journal size. Snapper snapshots cover only /
    (not /home), so they are mentioned only for / and never blamed for /home data."""
    raise NotImplementedError('TODO: implement')

def check_disk(env, state):
    raise NotImplementedError('TODO: implement')

def check_av(env, base):
    raise NotImplementedError('TODO: implement')

def check_self_improvement_math(env, problems, base):
    """Deterministic mathematical self-improvement telemetry for box_watch.

    Formalizes the 4 philosophical equations into live numeric observables:
      1. Free Energy / Surprise (F): ratio of surprise events / unexpected drift to baseline
      2. No-Regret Learning (R_T): preventable recurrence count from incident ledger
      3. Lyapunov Invariant Energy V(x): magnitude of invariant drift
      4. Compounding Velocity: ratio of resolved incidents with preventers + exported lessons
    """
    raise NotImplementedError('TODO: implement')

def paths(env):
    raise NotImplementedError('TODO: implement')

def run_checks(env, write=True):
    raise NotImplementedError('TODO: implement')

class LearnRefused(Exception):
    pass

def diff_summary(env, old, snap):
    """Plain lines describing what accepting `snap` would change relative to the last manifest `old`."""
    raise NotImplementedError('TODO: implement')

def learn(env, accept_shrink=False):
    raise NotImplementedError('TODO: implement')

def learn_command(env, yes=False, accept_shrink=False, interactive=None):
    """Show what would change, ask for confirmation when it is a lot, then learn. Returns an exit code."""
    raise NotImplementedError('TODO: implement')

def alarm_problems(now=None, env=None):
    """For ethan_alarm: problems from the last box_watch run; a missing or stale result is itself a problem."""
    raise NotImplementedError('TODO: implement')

def main(argv=None, env=None):
    raise NotImplementedError('TODO: implement')
