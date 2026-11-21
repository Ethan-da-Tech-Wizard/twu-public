# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/visible_run_loop.py — run ONE task end to end in a real, VISIBLE Ethan CLI window.

The owner watches the real CLI work on the desktop; no human keystrokes. The tool
opens a kitty window running ./scripts/ethan, types the prompt in by bracketed
paste through kitty remote control, waits for the turn to end, verifies the result
(expect file + optional --verify-cmd) and, on failure, types a self-contained
corrective prompt into the SAME window. Up to --max-corrective-rounds retries.

Exit codes: 0 verified PASS, 1 exhausted / refused because another CLI is open /
timeout, 2 STOP latch raised (business/example_host/comms/STOP) or refused to start.

Every prompt is registered as machine-composed (harvester --register-staged)
BEFORE it is submitted. A twu.visible-run-loop.v1 receipt is written atomically
under data/tool_trials/visible_run_loop/<UTC stamp>/. Verdicts go to
frontier_verification and one entry to the system journal (both never fatal).

Hazards: never uses pkill; never touches the model server, bridge or thermal
guard; only observes and types into its own window. The window is always closed
in a finally block (/quit, then close-window if the process lingers).

Stdlib only. Every external interaction is a small module-level function so tests
can patch it.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import signal
import subprocess
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

def visible_root() -> Path:
    """Where the CLI window runs and where relative work/expect/verify paths resolve: ETHAN_VISIBLE_ROOT (a example_host repo) when
    set, else the shared workspace. Receipts and logs always stay under REPO_ROOT/data."""
    raise NotImplementedError('TODO: implement')

def show_enabled() -> bool:
    raise NotImplementedError('TODO: implement')

class RefusedToStart(Exception):
    pass

class RunHeld(Exception):
    pass

def enforce_latches() -> None:
    raise NotImplementedError('TODO: implement')

def preflight() -> Optional[str]:
    raise NotImplementedError('TODO: implement')

def _now_iso() -> str:
    raise NotImplementedError('TODO: implement')

def sha256_text(text: str) -> str:
    raise NotImplementedError('TODO: implement')

def sha256_file(path: Path) -> str:
    raise NotImplementedError('TODO: implement')

def sleep(secs: float) -> None:
    raise NotImplementedError('TODO: implement')

def clock() -> float:
    raise NotImplementedError('TODO: implement')

def stop_raised() -> bool:
    raise NotImplementedError('TODO: implement')

def other_cli_open() -> bool:
    """True when an Ethan CLI process (bin/gemini) is already running."""
    raise NotImplementedError('TODO: implement')

def register_staged(prompt_file: Path, purpose: str, staged_by: str=...) -> bool:
    """Register a machine-composed prompt before it is submitted."""
    raise NotImplementedError('TODO: implement')

def _hypr_json(*args):
    raise NotImplementedError('TODO: implement')

def user_recently_active(quiet: float=..., poll: float=0.5) -> bool:
    """True when the active window changed within `quiet` seconds (the owner is working: do not move anything).
    Watches the active window address for `quiet` seconds; unknown telemetry counts as active. Never raises."""
    raise NotImplementedError('TODO: implement')

def bring_window_to_front(title: str=..., seconds: float=12.0, show: Optional[bool]=None) -> bool:
    """Opt-in (Hyprland): move the CLI window to the workspace the owner is looking at, float it large and focus it.
    Does NOTHING unless `show` (default: ETHAN_VISIBLE_SHOW=1) is on, because focus stealing interrupted the owner's work. Even
    then it skips if the owner's active window changed in the last few seconds. Never raises."""
    raise NotImplementedError('TODO: implement')

def launch_window(sock: str, group: str, log_path: Path) -> subprocess.Popen:
    raise NotImplementedError('TODO: implement')

def _spawn_window(sock: str, group: str, fh) -> subprocess.Popen:
    raise NotImplementedError('TODO: implement')

def socket_exists(sock: str) -> bool:
    raise NotImplementedError('TODO: implement')

def kitty_remote(sock: str, args: Sequence[str], stdin_bytes: Optional[bytes]=None) -> Tuple[int, str]:
    """Run `kitty @ --to unix:<sock> <args>`; returns (rc, stdout). Never raises."""
    raise NotImplementedError('TODO: implement')

def get_screen(sock: str) -> str:
    raise NotImplementedError('TODO: implement')

def send_bytes(sock: str, data: bytes) -> None:
    raise NotImplementedError('TODO: implement')

def close_window(sock: str) -> None:
    raise NotImplementedError('TODO: implement')

def process_alive(proc: Any) -> bool:
    raise NotImplementedError('TODO: implement')

def run_verify(cmd: str, neutral_path: bool) -> Tuple[int, str]:
    raise NotImplementedError('TODO: implement')

def screen_idle(screen: str) -> bool:
    raise NotImplementedError('TODO: implement')

def wait_for_ready(sock: str, proc: Any=None) -> bool:
    raise NotImplementedError('TODO: implement')

def submit_text(sock: str, text: str) -> None:
    """A normal prompt goes in by bracketed paste, then Enter. A slash command is typed RAW (the path seen to work
    in the real CLI: pasted markers around a command were not understood by the self-test stand-in), and needs a
    second Enter because the autocomplete popup swallows the first."""
    raise NotImplementedError('TODO: implement')

def wait_for_turn_end(sock: str, timeout: float, proc: Any=None) -> bool:
    """True when the turn ended (two consecutive idle polls ~6s apart);
    False on timeout, or at once when the window's own process has exited (a dead CLI never finishes a turn).
    Never kills anything."""
    raise NotImplementedError('TODO: implement')

def read_artifact(path: Path, limit: int=...) -> str:
    """The model's output for this round: the expect file's text, bounded. Empty when absent or not a file."""
    raise NotImplementedError('TODO: implement')

def tail_lines(text: str, n: int=...) -> str:
    raise NotImplementedError('TODO: implement')

def build_corrective_prompt(expect_path: str, error_tail: str, original: str, unchanged: bool=False) -> str:
    raise NotImplementedError('TODO: implement')

def write_receipt(path: Path, receipt: Dict[str, Any]) -> Path:
    raise NotImplementedError('TODO: implement')

def _record_verdicts(task: str, prompt_text: str, rounds: List[Dict[str, Any]], state: str, corrective: int) -> None:
    raise NotImplementedError('TODO: implement')

def _journal(state: str, summary: str, receipt_path: Path) -> None:
    raise NotImplementedError('TODO: implement')

def shutdown_window(sock: str, proc: Any) -> None:
    """/quit with the slash double-Enter, wait for exit, else close the window."""
    raise NotImplementedError('TODO: implement')

def parse_args(argv: Optional[Sequence[str]]=None) -> argparse.Namespace:
    raise NotImplementedError('TODO: implement')

def protected_changes(before: Dict[str, Optional[str]]) -> List[str]:
    """Paths whose content hash differs from the recorded one."""
    raise NotImplementedError('TODO: implement')

def _check(expect_path: Path, verify_cmd: Optional[str], neutral: bool, require_output: Optional[str]=None) -> Tuple[bool, Optional[int], str, Optional[str]]:
    raise NotImplementedError('TODO: implement')

def main(argv: Optional[Sequence[str]]=None) -> int:
    raise NotImplementedError('TODO: implement')

def _run(args: argparse.Namespace) -> int:
    raise NotImplementedError('TODO: implement')
