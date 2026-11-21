# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Turn classifier + never-repeating corrective prompts + strategy bandit for the local CLI agent.

Pure functions; no model, bridge, window or network access. visible_run_loop imports this:

    c = ethan_nudge.classify_turn(transcript, before, after, [expect], exit_code=rc, timed_out=..., ...)
    plan = ethan_nudge.plan_next(c, task, history)      # {"strategy","prompt","restart_window","rungs"}
    ethan_nudge.record_outcome(prev_class, prev_strategy, fixed)   # after the following round

Transcript formats understood (from data/self_improve/runs/*.jsonl and visible-run receipts):
  "[tool] write_file {json}" lines, "[final] text", CLI "Git safety gate: ..." (exit 43),
  the loop note "window did not reach the idle prompt", and model "tool calls" printed as JSON text.
"""
from __future__ import annotations
import ast
import json
import random
import re
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

class Classification(str):
    """A class name (compares equal to the plain string) carrying .detail text."""

    def __new__(cls, kind: str, detail: str=...):
        raise NotImplementedError('TODO: implement')

def tool_calls(transcript: str) -> List[str]:
    raise NotImplementedError('TODO: implement')

def _syntax_problem(path: str, content: Any) -> str:
    raise NotImplementedError('TODO: implement')

def classify_turn(transcript_text: str, files_before: Dict[str, Any], files_after: Dict[str, Any], expect_files: Sequence[str], *, exit_code: Optional[int]=None, timed_out: bool=False, reached_prompt: bool=True, verify_ok: Optional[bool]=None, verify_output: str=...) -> Classification:
    """files_* map path -> content (or hash); None/missing means absent."""
    raise NotImplementedError('TODO: implement')

def _load_stats(path: Path) -> List[dict]:
    raise NotImplementedError('TODO: implement')

def record_outcome(classification: str, strategy: str, fixed: bool, path: Optional[Path]=None, next_classification: str=...) -> None:
    """Append which strategy was tried on which classification and whether the next turn passed."""
    raise NotImplementedError('TODO: implement')

def strategy_scores(classification: str, path: Optional[Path]=None) -> Dict[str, float]:
    raise NotImplementedError('TODO: implement')

def strategy_ladder(history: Sequence[dict], classification: Optional[str]=None, stats_path: Optional[Path]=None, rng: Optional[random.Random]=None, epsilon: float=...) -> str:
    """Pick the next strategy. Never reuses one already tried this run while an untried one remains;
    among untried, epsilon-greedy over the learned fix rate for this classification."""
    raise NotImplementedError('TODO: implement')

def _norm(s: str) -> str:
    raise NotImplementedError('TODO: implement')

def _task_fields(task: Any) -> Dict[str, Any]:
    raise NotImplementedError('TODO: implement')

def _rel(p: str) -> str:
    raise NotImplementedError('TODO: implement')

def _requirements(t: Dict[str, Any]) -> List[str]:
    raise NotImplementedError('TODO: implement')

def split_rungs(task: Any) -> List[str]:
    """Interface for the split-into-steps strategy: returns a list of rung prompts, one per step.
    Delegates to scripts/ethan_ladder.py `build_rungs(task_dict) -> list[str]` when it exists."""
    raise NotImplementedError('TODO: implement')

def _contents(t: Dict[str, Any]) -> str:
    raise NotImplementedError('TODO: implement')

def _skeleton(t: Dict[str, Any]) -> str:
    raise NotImplementedError('TODO: implement')

def _smallest_edit(cls: str, detail: str, f: str) -> str:
    raise NotImplementedError('TODO: implement')

def next_prompt(classification: str, task: Any, history: Sequence[dict], strategy: Optional[str]=None) -> str:
    """A corrective prompt different from every earlier prompt in history, escalating in specificity."""
    raise NotImplementedError('TODO: implement')

def plan_next(classification: str, task: Any, history: Sequence[dict], stats_path: Optional[Path]=None, rng: Optional[random.Random]=None) -> Dict[str, Any]:
    """One-call hook: choose strategy, build prompt. restart_window tells the loop to open a new window."""
    raise NotImplementedError('TODO: implement')
