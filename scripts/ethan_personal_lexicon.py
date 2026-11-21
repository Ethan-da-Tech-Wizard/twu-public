# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Ethan's personal lexicon: typos, shorthand and standing "extra work he assumes".

Pure stdlib and deterministic.  No model calls, no network, no clock.  Two jobs:

* runtime: ``normalize(prompt)`` applies ONLY confirmed lexicon entries and flags
  (never rewrites) uncertain ones; ``expected_followups(task_kind)`` lists the
  extra work Ethan assumes for a kind of task.
* build: ``build()`` regenerates lexicon.json, assumptions.json and pairs.jsonl
  from the allowed local sources listed in PRIVACY.md.  It never reads chat or
  session logs, and everything it writes is scrubbed.

Evidence rule: nothing is labeled by a model's guess.  A typo is "confirmed"
only when Ethan accepted it, or the same variant was measured >= 3 times, or it
is unambiguous by edit distance (non-word, target >= 5 letters, distance <= 2,
or a unique nearest dictionary neighbour).  Everything else is "uncertain".
"""
from __future__ import annotations
import ast
import hashlib
import json
import re
import stat
import sys
from pathlib import Path

def _load_system_words(paths=...) -> frozenset[str]:
    """Load one bounded, root-owned system wordlist; return empty when none is trustworthy."""
    raise NotImplementedError('TODO: implement')

def scrub(text: str, limit: int=160) -> str:
    """Remove secrets/emails/phones/paths from text and bound its length."""
    raise NotImplementedError('TODO: implement')

def is_sensitive(text: str) -> bool:
    raise NotImplementedError('TODO: implement')

def load_lexicon(path: Path | str | None=None) -> dict:
    raise NotImplementedError('TODO: implement')

def _match_case(original: str, replacement: str) -> str:
    raise NotImplementedError('TODO: implement')

def _protected(token: str) -> bool:
    raise NotImplementedError('TODO: implement')

def normalize(prompt: str, lexicon: dict | None=None) -> tuple[str, list[str], list[str]]:
    """Return (normalized text, applied lexicon ids, flags).

    Only ``confirmed`` typo/shorthand entries change text.  Flags are
    ``uncertain:<id>`` (token matches an uncertain entry; text untouched) and
    ``marker:<kind>`` (emphasis annotations; text untouched, not anger).
    Code spans, paths, identifiers and anything with digits are left alone.
    """
    raise NotImplementedError('TODO: implement')

def expected_followups(task_kind: str, assumptions: dict | None=None) -> list[str]:
    """Extra work Ethan assumes gets done for ``task_kind`` (sorted, stable)."""
    raise NotImplementedError('TODO: implement')

def damerau(a: str, b: str) -> int:
    """Optimal-string-alignment distance (insert/delete/substitute/transpose)."""
    raise NotImplementedError('TODO: implement')

def _edits1(word: str) -> set[str]:
    raise NotImplementedError('TODO: implement')

def _swaps(word: str) -> set[str]:
    raise NotImplementedError('TODO: implement')

def rivals(token: str, intended: str, dist: int, words: frozenset[str]) -> list[str]:
    """Other dictionary words at least as close to ``token`` as ``intended`` is."""
    raise NotImplementedError('TODO: implement')

def unique_neighbour(token: str, words: frozenset[str]) -> str | None:
    """The single dictionary word nearest to ``token`` (distance 1, or 2 for long tokens), else None."""
    raise NotImplementedError('TODO: implement')

def _lid(kind: str, surface: str, intended: str) -> str:
    raise NotImplementedError('TODO: implement')

def _read(root: Path, rel: str) -> str:
    raise NotImplementedError('TODO: implement')

def _source_text(root: Path, source: str) -> str:
    raise NotImplementedError('TODO: implement')

def _vocab(text: str) -> set[str]:
    raise NotImplementedError('TODO: implement')

def _review_queue_human(root: Path) -> list[str]:
    """Human-origin prompts (by the queue's deterministic rule label), scrubbed, harness tags removed."""
    raise NotImplementedError('TODO: implement')

def _window(text: str, word: str) -> str:
    raise NotImplementedError('TODO: implement')

def build(root: Path=..., out_dir: Path | None=None, use_transcripts: bool=True, claude_dir: Path | None=None, corpus_override: list[dict] | None=None) -> dict:
    """Regenerate lexicon.json, assumptions.json and pairs.jsonl.  Deterministic; returns summary."""
    raise NotImplementedError('TODO: implement')

class SourceBlocked(RuntimeError):
    """A transcript source could not be read (permission).  Callers stop and report; they never work around it."""

def clean_prompt(text: str) -> str:
    """Strip harness wrappers, pasted blocks, image markers and paths from a user message; returns '' if nothing typed remains."""
    raise NotImplementedError('TODO: implement')

def rows_from_claude_records(records, session: str) -> list[dict]:
    """User-typed text from Claude Code session records (type user, not meta/sidechain, not tool_result)."""
    raise NotImplementedError('TODO: implement')

def rows_from_mirror_records(records) -> list[dict]:
    raise NotImplementedError('TODO: implement')

def looks_machine_written(t: str) -> bool:
    """Prompts relayed by agents/harnesses arrive in the same logs; Ethan's own typing is informal, lower-case and typo-rich.
    Reject structured, formal or agent-voiced text.  (Errs towards dropping: counts only need to be representative.)"""
    raise NotImplementedError('TODO: implement')

def build_corpus(rows: list[dict]) -> list[dict]:
    """Filter, clean and de-duplicate raw rows into the in-memory typed-message corpus (sorted by time)."""
    raise NotImplementedError('TODO: implement')

def load_corpus(root: Path=..., claude_dir: Path | None=None) -> tuple[list[dict], dict]:
    """Read both authorized sources.  Returns (corpus, status).  Missing dir -> skipped; permission error -> SourceBlocked."""
    raise NotImplementedError('TODO: implement')

def _snip(text: str, m: re.Match | None=None) -> str:
    raise NotImplementedError('TODO: implement')

def _examples(hits: list[tuple[str, str]]) -> list[dict]:
    """<=3 scrubbed snippets from distinct prompts, picked by hash order (deterministic, not cherry-picked)."""
    raise NotImplementedError('TODO: implement')

def message_kind(text: str) -> str:
    raise NotImplementedError('TODO: implement')

def _edit_kind(tok: str, cand: str) -> str:
    raise NotImplementedError('TODO: implement')

def _expand_known(words: frozenset[str]) -> frozenset[str]:
    raise NotImplementedError('TODO: implement')

def mine(corpus: list[dict], words: frozenset[str], known: frozenset[str], existing: list[dict]) -> dict:
    """Pure function: counts + short scrubbed snippets from a typed-message corpus.  Returns new entries and side outputs."""
    raise NotImplementedError('TODO: implement')

def _gap_hours(a: str, b: str) -> float:
    raise NotImplementedError('TODO: implement')

def next_signal(text: str) -> str:
    """Deterministic label for a following message: confirm / correct / other (anchored, no model)."""
    raise NotImplementedError('TODO: implement')

def make_eval(corpus: list[dict], lexicon: dict, cutoff: str, size: int=100, train_share: int=70) -> list[dict]:
    """100 real scrubbed prompts split by time.  The intended ACTION cannot be derived from user text alone, so rows carry
    the deterministic normalisation (confirmed entries only; the test side uses only entries seen >=3 times before the cutoff)
    plus the signal in his next message (confirm/correct/other)."""
    raise NotImplementedError('TODO: implement')

def entry_count(entry: dict) -> int:
    raise NotImplementedError('TODO: implement')

def confident_typos(lexicon: dict | None=None) -> dict[str, str]:
    """surface -> intended for confirmed typo entries seen in >= 3 prompts, excluding profanity."""
    raise NotImplementedError('TODO: implement')

def interpretation_note(prompt: str, lexicon: dict | None=None) -> str:
    """One line telling the model which words in ``prompt`` are typos, WITHOUT rewriting ``prompt``.

    Only confident fixes (see ``confident_typos``); code spans, quoted text, paths and identifiers are masked
    first, and emphasis/profanity is never touched.  Returns "" when nothing applies.
    """
    raise NotImplementedError('TODO: implement')

def user_conventions(lexicon: dict | None=None) -> str:
    """Compact standing-conventions line (<= MAX_CONVENTION_CHARS), each part licensed by a confirmed lexicon entry."""
    raise NotImplementedError('TODO: implement')

def main(argv: list[str] | None=None) -> int:
    raise NotImplementedError('TODO: implement')
