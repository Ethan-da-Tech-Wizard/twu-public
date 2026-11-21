# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Turn RESOLVED incidents into sanitized, shareable lesson records (data/lessons/<id>.json).

Commands: export [--dry-run] | list | verify.   Default-deny: any audit hit after redaction rejects the record.
Reuses (read-only import) public_release_redact.Redactor and public_export_audit.scan_text/_hostnames.
Never edits the public release allowlist; it prints the line a human would add.
"""
from __future__ import annotations
import datetime, hashlib, json, re, sys
from pathlib import Path
import public_release_redact as _red
import public_export_audit as _aud

def fleet_names(root: Path):
    raise NotImplementedError('TODO: implement')

def name_regex(names):
    """One case-insensitive regex; -, _, space, . are interchangeable inside a name; optional possessive 's."""
    raise NotImplementedError('TODO: implement')

def _parse_ts(s):
    raise NotImplementedError('TODO: implement')

def preventer_ok(prev, root=None):
    raise NotImplementedError('TODO: implement')

def build_ctx(root: Path=...):
    raise NotImplementedError('TODO: implement')

def sanitize(text, ctx):
    """-> (clean_text, [rule names that still fire]). Hits are rule names only, never values."""
    raise NotImplementedError('TODO: implement')

def _is_shard(path) -> bool:
    """Skip the curated registry (incidents.jsonl) and any file whose first line lacks 'incident_id'."""
    raise NotImplementedError('TODO: implement')

def load_events(inc_dir: Path):
    raise NotImplementedError('TODO: implement')

def fold(events, root=None):
    raise NotImplementedError('TODO: implement')

def opaque_id(iid):
    raise NotImplementedError('TODO: implement')

def _cut(s, n):
    raise NotImplementedError('TODO: implement')

def build_records(inc_dir, repo_root=..., ctx=None):
    """-> (records {id: dict}, rejects [(id, rule)]). Pure; writes nothing."""
    raise NotImplementedError('TODO: implement')

def export(inc_dir, out_dir, repo_root=..., dry_run=False, ctx=None):
    raise NotImplementedError('TODO: implement')

def verify(out_dir, ctx=None, repo_root=...):
    """-> [(file name, rule)] for every audit hit or schema violation in data/lessons."""
    raise NotImplementedError('TODO: implement')

def main(argv):
    raise NotImplementedError('TODO: implement')
