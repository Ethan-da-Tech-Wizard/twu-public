# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/resilient_task_runner.py — self-recovering headless runs of the Ethan CLI.

Why this exists (2026-10-25): the thermal guard SIGSTOPs llama-server mid-generation
when the GPU runs hot. The interactive CLI flow then wedges — the stream dies, the
session sits forever, and a human had to hit Esc and relaunch. That defeats the whole
"humans out of the loop" posture. This runner automates the detect → wait → retry →
verify loop so a stalled generation recovers with no human:

  * It runs `./scripts/ethan -p <prompt>` headlessly, logging each attempt under
    data/tool_trials/resilient_runner/<UTC stamp>/attempt-N.log.
  * A background watcher checks every 20s whether llama-server is in 'T (stopped)'
    state or data/daemon_logs/llama_server.log has gone 180s without an mtime bump.
    Either means the attempt is STALLED. It then waits up to 600s for the thermal
    guard to auto-resume the server (the guard owns pause/resume — this tool never
    starts, stops, or signals the model server). If the server does not come back,
    or the attempt outlives --attempt-timeout, the attempt's whole process group is
    killed (SIGTERM, then SIGKILL) and the next attempt begins.
  * Between attempts it waits for GPU temp <= 83 C and a healthy
    http://127.0.0.1:18190/health before retrying.
  * Success means every --expect-file exists and the optional --verify-cmd exits 0.
    A twu.resilient-runner.v1 receipt JSON is written atomically either way, and one
    entry is appended to the rolling system journal (best effort, never fatal).

Exit codes: 0 success, 1 attempts exhausted, 2 STOP latch
(business/example_host/comms/STOP) was raised.

Stdlib only. All the moving parts (spawn, kill, server-state probe, log-mtime
reader, GPU-temp reader, health check, verify runner, sleeps) are module-level
functions so tests can patch them without a real CLI, GPU, or network.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import signal
import subprocess
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

def _now_iso() -> str:
    raise NotImplementedError('TODO: implement')

def spawn_attempt(prompt_text: str, log_path: Path) -> subprocess.Popen:
    """Launch one headless Ethan CLI run in its own session (so the whole
    process group can be killed on stall). Output goes to the attempt log."""
    raise NotImplementedError('TODO: implement')

def kill_attempt(proc: subprocess.Popen) -> None:
    """SIGTERM the attempt's process group, escalate to SIGKILL. Never touches
    llama-server — only the CLI run we spawned."""
    raise NotImplementedError('TODO: implement')

def llama_server_state() -> str:
    """'stopped' if any llama-server pid shows 'T (stopped)' in /proc status,
    'running' if one exists and is not stopped, 'absent' if none, 'unknown' on
    probe failure. Observation only."""
    raise NotImplementedError('TODO: implement')

def llama_log_mtime() -> Optional[float]:
    """mtime of the llama-server log, or None when it does not exist (a missing
    log never counts as a stall on its own)."""
    raise NotImplementedError('TODO: implement')

def read_gpu_temp() -> int:
    """GPU temperature via nvidia-smi; any failure reads as 0 so a box without
    a GPU (or a wedged nvidia-smi) never blocks the retry loop."""
    raise NotImplementedError('TODO: implement')

def check_health() -> bool:
    """True when the local model server's /health answers (curl exit 0)."""
    raise NotImplementedError('TODO: implement')

def run_verify(cmd: str) -> Tuple[int, str]:
    """Run the --verify-cmd (shell), return (rc, combined output)."""
    raise NotImplementedError('TODO: implement')

def _sleep(seconds: float) -> None:
    raise NotImplementedError('TODO: implement')

def _log_is_stale() -> bool:
    raise NotImplementedError('TODO: implement')

def _sleep_while_running(proc: subprocess.Popen, seconds: float) -> None:
    """Sleep up to `seconds` but wake early if the attempt finishes."""
    raise NotImplementedError('TODO: implement')

def _wait_for_resume(proc: subprocess.Popen, t0: float, attempt_timeout: float, outcome: Dict[str, Any]) -> bool:
    """A stall was seen. Wait (up to RESUME_WAIT_SECS) for the thermal guard to
    put llama-server back in a running state with a fresh log. Returns True when
    it resumed (or the attempt finished by itself); False means give up, with
    outcome['classification'] set to 'stalled' or 'timeout'."""
    raise NotImplementedError('TODO: implement')

def _watch_attempt(proc: subprocess.Popen, t0: float, attempt_timeout: float, outcome: Dict[str, Any]) -> None:
    """Background watcher: every PROGRESS_POLL_SECS, look for a paused server or
    a silent log while the attempt still runs. On an unrecovered stall or an
    attempt timeout, kill the attempt's process group."""
    raise NotImplementedError('TODO: implement')

def _run_attempt(n: int, prompt_text: str, log_path: Path, attempt_timeout: float) -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def wait_for_cooldown(notes: List[str]) -> bool:
    """Wait until GPU temp <= GPU_TEMP_MAX and /health answers. Gives up after
    COOLDOWN_MAX_SECS, records that, and retries anyway (never a hard stop)."""
    raise NotImplementedError('TODO: implement')

def _sha256(path: Path) -> Optional[str]:
    raise NotImplementedError('TODO: implement')

def _check_success(expect_files: Sequence[str], verify_cmd: Optional[str]) -> Tuple[bool, Optional[int], str]:
    raise NotImplementedError('TODO: implement')

def write_receipt(receipt: Dict[str, Any], stamp_dir: Path) -> Path:
    raise NotImplementedError('TODO: implement')

def _journal(success: bool, summary: str, receipt_path: Path) -> None:
    """Best-effort rolling-journal entry; a journal failure never fails a run."""
    raise NotImplementedError('TODO: implement')

def parse_args(argv: Optional[Sequence[str]]=None) -> argparse.Namespace:
    raise NotImplementedError('TODO: implement')

def main(argv: Optional[Sequence[str]]=None) -> int:
    raise NotImplementedError('TODO: implement')
