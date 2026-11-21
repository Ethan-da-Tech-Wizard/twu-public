# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/ethan_journeys.py - real journeys: reviewed, read-only runs of real tools THROUGH Enki, each with a checked expectation.

Why: "wired" on paper is not "works in real use". On 2026-11-02 Enki listed 413 callable tools and had run 2. A test proves a tool in a
fake workspace; a journey runs the real tool on the real workspace through Enki's own runner (`enki_tools.run_tool`: catalog, STOP latch,
fresh smoke receipt, class approval, run log) and checks the output, so a tool that quietly stopped working shows up as a failed journey.

The list below is CODE (reviewed in Git), not editable data, and every entry is a specific read-only invocation. Enki's class for a tool is a
conservative text match (a tool that CAN write is `writes` even when this invocation only reads), so a journey names the class it
approves; classes beyond read are allowed only for invocations in this list.

  python3 scripts/ethan_journeys.py list
  python3 scripts/ethan_journeys.py run [--id ID] [--due]     run all, one, or only those not run in the last 24 hours
  python3 scripts/ethan_journeys.py status [--json]           last result, age and streak per journey
  python3 scripts/ethan_journeys.py prove TOOL --expect RE [--rc N] -- ARGS...   run ONE candidate in a read-only, no-network example_host
  python3 scripts/ethan_journeys.py adopt CANDIDATES.json     prove each candidate; adopt the ones that pass into the batch file
  python3 scripts/ethan_journeys.py classify-rest             write data/tools/journeys_exempt.json: a heuristic reason per tool with no journey
  python3 scripts/ethan_journeys.py record-skips FILE.json   merge reviewed {tool, reason, evidence} skip reasons over the heuristic ones
  python3 scripts/ethan_journeys.py discover [--limit N] [--out FILE]   probe Enki-listed tools without a journey using a fixed list of
                                                              read-only subcommands, in the example_host; write candidates (no model, no guessing)

Batch journeys (data/tools/journeys_batch.json) are not hand-reviewed one by one: each is admitted only if it passes `prove`, and it is
re-proven inside the example_host before EVERY run, so a tool that later gains a write or a network call fails its journey instead of running.
Results: data/tools/journeys_ledger.jsonl (append-only). Stdlib only; no model, no GPU, no network.
"""
from __future__ import annotations
import datetime as dt
import json
import re
import sys
import time
from pathlib import Path

def bwrap_ok() -> bool:
    raise NotImplementedError('TODO: implement')

def prove(root: Path, script: Path, args: list, expect: str, rc=..., timeout: int=...) -> dict:
    """Run one invocation with the whole filesystem READ-ONLY, no network and a hard timeout. A write attempt (EROFS) or a network call
    fails the proof, so 'read-only' is demonstrated, not claimed. Returns {ok, rc, matched, erofs, seconds, head}."""
    raise NotImplementedError('TODO: implement')

def load_batch(root: Path=...) -> list:
    raise NotImplementedError('TODO: implement')

def all_journeys(root: Path=...) -> list:
    raise NotImplementedError('TODO: implement')

def expect_from(head: str) -> str:
    """A stable pattern from real output: the leading words of the first non-empty line (letters, spaces, a little punctuation), escaped.
    Numbers, times and paths vary between runs, so they are never part of the pattern. Empty when nothing stable is found."""
    raise NotImplementedError('TODO: implement')

def discover(root: Path, tools: list, probes=..., prover=None, limit: int=0, timeout: int=10) -> tuple:
    """For each tool try the fixed read-only probes in the example_host; the first that exits 0 with real (non-help) output becomes a candidate whose
    expectation is derived from that output and re-proved. Returns (candidates, no_probe_worked)."""
    raise NotImplementedError('TODO: implement')

def classify_rest(root: Path, tools: list) -> dict:
    """A heuristic REASON (from the tool's source) why no safe read-only journey was found for it. Honest label: this is a text match, not
    proof; a person can still write a real journey, and doing so removes the tool from this list."""
    raise NotImplementedError('TODO: implement')

def record_skips(root: Path, skips: list) -> int:
    """Merge individually-reviewed skip reasons (with evidence) over the heuristic ones. A reason with no evidence is ignored."""
    raise NotImplementedError('TODO: implement')

def load_exempt(root: Path=...) -> dict:
    raise NotImplementedError('TODO: implement')

def slug(tool: str, args: list) -> str:
    raise NotImplementedError('TODO: implement')

def adopt(root: Path, candidates: list, manifest: dict, prover=None) -> dict:
    """Admit candidates that prove read-only and correct. The Enki class comes from the manifest, never from the candidate."""
    raise NotImplementedError('TODO: implement')

def J(id, tool, args, expect, approve=..., rc=..., what=..., net=False, example_host=True):
    """net: the journey needs loopback (a local service). example_host=False only for reviewed tools that cannot run in a user-namespace example_host
    (the root-execution audit judges file OWNERS, and every file looks owned by nobody inside one); the invocation is still read-only by review."""
    raise NotImplementedError('TODO: implement')

def read_ledger(root: Path=...) -> list:
    raise NotImplementedError('TODO: implement')

def refresh_smoke(root: Path, tool: str) -> bool:
    """Enki refuses a tool whose script changed since its last smoke test. Re-smoke it through Enki's own command, then retry once."""
    raise NotImplementedError('TODO: implement')

def example_hosted_run(net: bool=False):
    """A drop-in for subprocess.run that executes the command with the filesystem READ-ONLY (and no network unless a journey needs
    loopback). Enki's run_tool takes it as `run=`, so Enki still does all of its own checks and logging; only the execution is example_hosted."""
    raise NotImplementedError('TODO: implement')

def run_one(root: Path, j: dict, runner=None, smoker=None) -> dict:
    """Run one journey through Enki's runner; the result is appended to the ledger."""
    raise NotImplementedError('TODO: implement')

def age_hours(ts: str, now: dt.datetime | None=None) -> float:
    raise NotImplementedError('TODO: implement')

def state(root: Path=..., journeys=None, now=None) -> list:
    raise NotImplementedError('TODO: implement')

def due(row: dict) -> bool:
    raise NotImplementedError('TODO: implement')

def counts(root: Path=..., journeys=None, now=None) -> dict:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
