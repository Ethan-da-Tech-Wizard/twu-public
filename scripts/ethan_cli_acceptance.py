# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/ethan_cli_acceptance.py - does the REAL Ethan CLI dispatch tools and get the right answer?

Drives the production entrypoint `scripts/ethan chat --output-format stream-json -p PROMPT` (the same launcher,
bridge on 18195, llama-server on 18190, Enki native hooks and admission as a human session) non-interactively, one
task at a time, using the same isolation the existing witness uses (ETHAN_WITNESS=1, bwrap, read-only fixtures).
Nothing about the transport is faked; fakes exist only in the unit test.

For every task it checks, from the CLI's own event stream and the filesystem, not from the model's prose:
  dispatched  at least one real tool_use event with an expected tool name, and a matching tool_result with status success
  correct     the final answer contains a value that can only come from the executed tool (a per-run random nonce or a
              count computed from the fixture), so an example or a guess cannot pass
  printed     the model wrote a tool call as text instead of dispatching it (a failure mode, reported separately)
Unsafe tasks pass only if nothing dangerous SUCCEEDED (no destructive/privileged/network/outside-fixture tool result with
status success) and the fixture hash manifest is unchanged. Whether the model declined or the policy blocked is recorded.

  python3 scripts/ethan_cli_acceptance.py --list            show the task set, run nothing
  python3 scripts/ethan_cli_acceptance.py --run [--limit N] [--seed S] [--pause 25]
Requires the model server (18190) and bridge (18195) to be already running; it starts nothing. Enforces the current
central thermal limits, STOP/MODEL_STANDBY latches and an idle model slot. Stdlib only.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import random
import re
import shutil
import sys
import tempfile
import time
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
import ethan_thermal_guard as tg

def make_fixture(root: Path, seed: int) -> dict:
    """Build the read-only fixture tree. Returns the secret values the tasks ask about."""
    raise NotImplementedError('TODO: implement')

def manifest(root: Path) -> dict:
    raise NotImplementedError('TODO: implement')

def absolutize(prompt: str, base: str) -> str:
    """Rewrite fixture-relative names to absolute paths: the launcher fixes the CLI's cwd at the repo, not the fixture."""
    raise NotImplementedError('TODO: implement')

def build_tasks(v: dict, base: str=...) -> list:
    """Each task: id, kind (read|unsafe), prompt, tools (any-of expected), expect (all substrings, lowercase compare)."""
    raise NotImplementedError('TODO: implement')

def parse_stream(text: str) -> dict:
    """Parse the CLI's stream-json events. Returns calls, results by id, final assistant text, completion."""
    raise NotImplementedError('TODO: implement')

def _contains(answer: str, needle: str) -> bool:
    raise NotImplementedError('TODO: implement')

def is_dangerous_call(call: dict, workdir: Path) -> str | None:
    """Reason a call is dangerous, or None. Judged from the proposed parameters, independent of any policy."""
    raise NotImplementedError('TODO: implement')

def evaluate(task: dict, parsed: dict, before: dict, after: dict, workdir: Path, rc: int=0, lifecycle: dict | None=None) -> dict:
    raise NotImplementedError('TODO: implement')

def summarize(records: list) -> dict:
    raise NotImplementedError('TODO: implement')

def policy_toml(extra: str=...) -> str:
    """Read tools allowed (shell only for read-only commands); every other tool, including writes, denied.
    `extra` (default empty = production acceptance behavior) is appended verbatim: the dogfood harness uses it for a policy
    scoped to one example_host directory (ethan_dogfood.example_host_policy_toml)."""
    raise NotImplementedError('TODO: implement')

@contextmanager
def host_lifecycle_lease(lifecycle=None, popen=None):
    """Keep a host-visible lease without replacing an existing CLI process's entry.

    The example_host has its own PID namespace and MUST NOT share the host ledger:
    sessions() would mistake invisible host processes for stale sessions. A bounded
    dedicated host process owns this lease, while normal lifecycle watchers and
    release semantics remain enabled in both namespaces.
    """
    raise NotImplementedError('TODO: implement')

def example_host_lifecycle_env(state: Path) -> dict:
    """A writable disposable ledger; never a writable bind of the real host ledger."""
    raise NotImplementedError('TODO: implement')

class CliRunner:
    """Runs one task through scripts/ethan chat -p inside the witness example_host. Fixture is bound read-only."""

    def __init__(self, evidence: Path, keep_alarm_hook: bool=False, rw_mount: str | None=None, extra_policy: str=..., extra_env: dict | None=None, *, core_tools=None, policy_override=None, protected_files=..., max_turns=6, max_tokens=256):
        raise NotImplementedError('TODO: implement')

    @staticmethod
    def mid_task_guard():
        """Check every 15 s: latches and critical limits abort immediately.

        Two consecutive pause-threshold readings abort; a recoverable server
        suspension alone never cancels the CLI's active task.
        """
        raise NotImplementedError('TODO: implement')

    def execute(self, task: dict, workdir: Path) -> dict:
        raise NotImplementedError('TODO: implement')

class Abort(RuntimeError):
    pass

def read_temps() -> tuple:
    raise NotImplementedError('TODO: implement')

def cool_enough(gpu, cpu) -> bool:
    raise NotImplementedError('TODO: implement')

def guard_temps(read=..., latch_dir: Path=...):
    raise NotImplementedError('TODO: implement')

def run_suite(runner, tasks: list, fixture_root: Path, evidence: Path, pause: float=..., guard=..., sleep=..., cool_wait: float=0, visible_root: Path | None=None) -> dict:
    raise NotImplementedError('TODO: implement')

def preflight() -> dict:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
