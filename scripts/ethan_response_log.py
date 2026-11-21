# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Per-host SQLite log of Ethan CLI/model exchanges, with redaction and deterministic ratings.

No model calls, no network, stdlib only. Default DB: ~/.local/share/twu/ethan_responses.<hostname>.sqlite
(OUTSIDE the Syncthing-shared repo; binary DBs conflict under sync, so a path inside the repo is refused).
Share results only via export_jsonl(path) (text, already redacted).

SCHEMA (version 2; agreed with Magi 6's ethan-rater.v1 `report` query, which must work unchanged:
  SELECT r.id,r.ts,r.model_id,r.adapter_sha256,t.score,t.passed,t.violations_json FROM responses r
  JOIN ratings t ON t.response_id=r.id AND t.rater_version=?)
  schema_version(version, applied_utc)
  requests(id, ts_utc, host, app, model, endpoint, prompt_sha256, prompt_text, system_sha256, params_json,
           redactions, model_id, adapter_sha256, session_id, turn_idx)
  responses(id, request_id -> requests.id, ts, model_id, adapter_sha256 (denormalized from the request),
            text, tool_calls_json, latency_ms, tokens_in, tokens_out, finish_reason, redactions,
            pair_id, gate_status, gate_reason)
  ratings(id, response_id -> responses.id, rater_version, score REAL 0..1, passed INT, violations_json TEXT
          [{rule,id,detail}], skipped_json, prompt_class, ts_utc, verdict, verified_by, checker_manifest_sha,
          legacy_total, legacy_components_json (v1 rows only); UNIQUE(response_id, rater_version))
  verdict PASS/FAIL/INCOMPLETE; verified_by 'rules' for every live rating (no expected value, no example_host run: weaker than
  an eval PASS; 'execution' is never written by this module).
Migration: init_db upgrades a version-1 DB in place (ALTER responses ADD COLUMN + backfill; ratings rebuilt with
v1 total/components kept in legacy_* columns; no row is dropped).
Privacy: text, prompt, params and tool calls are redacted before storage with gate SECRET_RES (public name) plus
regexes copied into this file (so a rater/split_plan refactor cannot break the scrub), replaced by [REDACTED:<kind>];
the redaction counts are stored; hashes are of the REDACTED text; the system
prompt is stored only as a hash. Reserved example domains (example.com etc.) are not redacted.

Usage: python3 scripts/ethan_response_log.py [--db PATH] (--stats | --recent N | --rate-unrated | --export-jsonl PATH)
"""
import argparse, hashlib, json, os, re, socket, sqlite3, sys
from datetime import datetime, timezone
import ethan_training_gate as G
import ethan_response_rater as R

class _Leak:

    @staticmethod
    def search(t):
        raise NotImplementedError('TODO: implement')

def now_utc():
    raise NotImplementedError('TODO: implement')

def default_db_path(host=None):
    raise NotImplementedError('TODO: implement')

def _inside_repo(path):
    raise NotImplementedError('TODO: implement')

def redact(text):
    """(redacted_text, count). Layers: gate SECRET_RES (reserved example domains kept), then the copied regexes
    (emails not in _EMAIL_OK). Then a verify pass: if _LEAK_RX still matches, blank the whole text."""
    raise NotImplementedError('TODO: implement')

def _redact_obj(obj):
    """Redact every string inside a JSON-able object; returns (obj, count)."""
    raise NotImplementedError('TODO: implement')

def _sha(s):
    raise NotImplementedError('TODO: implement')

def _safe_metadata(value):
    raise NotImplementedError('TODO: implement')

def _cols(conn, table):
    raise NotImplementedError('TODO: implement')

def _migrate_v1(conn):
    """In place v1 -> v2. responses gains ts/model_id/adapter_sha256 (backfilled from requests); ratings is rebuilt
    (total/components kept in legacy_*; score = total/100, violations_json '[]' because v1 had none)."""
    raise NotImplementedError('TODO: implement')

def init_db(path=None):
    raise NotImplementedError('TODO: implement')

def _manifest_sha():
    raise NotImplementedError('TODO: implement')

def _mask_violations(vs):
    """Persist only fixed diagnostic identifiers; never persist input excerpts."""
    raise NotImplementedError('TODO: implement')

def _safe_skips(skipped):
    raise NotImplementedError('TODO: implement')

def _store_rating(conn, response_id, res, ts=None):
    raise NotImplementedError('TODO: implement')

def _record(prompt, text, tool_calls, finish_reason, tokens_out):
    """The record shape ethan-rater.v1 normalize() reads: prompt_text, response_text, tool_calls, finish_reason."""
    raise NotImplementedError('TODO: implement')

def log_exchange(conn, *, prompt, text, host=None, app=None, model=None, endpoint=None, system=None, params=None, tool_calls=None, latency_ms=None, tokens_in=None, tokens_out=None, finish_reason=None, thinking=False, rate=True, ts_utc=None, model_id=None, adapter_sha256=None, session_id=None, turn_idx=None, pair_id=None, gate_status=None, gate_reason=None):
    """Store one exchange (redacted). If rate, rate the RAW exchange (so leaks are seen) and store the rating.
    Returns the response id."""
    raise NotImplementedError('TODO: implement')

def recent(conn, n=20):
    raise NotImplementedError('TODO: implement')

def classify_rating(score, passed, violations_json, skipped_json, verdict, assessment):
    """Classify only internally consistent, coverage-marked stored ratings."""
    raise NotImplementedError('TODO: implement')

def stats(conn):
    raise NotImplementedError('TODO: implement')

def rate_unrated(conn, rater_version=None):
    """Rate every response with no rating for the current rater version. Stored text is redacted, so a nonzero
    redaction count is passed to the rater as response_redactions (counts as a leak). Returns number rated."""
    raise NotImplementedError('TODO: implement')

def export_jsonl(conn, path, overwrite=False):
    """Write redacted exchanges + ratings as JSONL (one object per response). Refuses sqlite-looking paths and
    existing files unless overwrite. Returns row count."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
