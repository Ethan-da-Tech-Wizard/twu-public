# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Fleet flow runner (Magi 6). One command, follow-up steps across boxes, nothing free-form.
  python3 scripts/fleet_flow.py list
  python3 scripts/fleet_flow.py <flow-name> [--dry-run] [--only-box BOX] [--json]
A flow is a JSON file in data/fleet_flows/. Every step is one closed-set action run through scripts/fleet_do.py (Magi 8).
STOP is checked before every step. Every executed step is appended to a sha256-chained audit file. Stdlib only, py3.9+."""
import hashlib, json, os, re, sys, time

class FlowError(Exception):
    pass

def validate(flow):
    """Return the flow if valid, else raise FlowError with a plain reason."""
    raise NotImplementedError('TODO: implement')

def _check_param(sid, act, p):
    raise NotImplementedError('TODO: implement')

def order(steps):
    """Deterministic topological order (ties broken by file order). Raises FlowError on a cycle."""
    raise NotImplementedError('TODO: implement')

def expand(flow, only_box=None):
    """Ordered list of concrete steps (one box each). 'all' -> example_host, example_host, example_host. A dependency on an
    'all' step means every expansion. only_box drops other boxes' steps and any dependency on them."""
    raise NotImplementedError('TODO: implement')

def _h(rec):
    raise NotImplementedError('TODO: implement')

def _last_hash(path):
    raise NotImplementedError('TODO: implement')

def audit_append(path, rec):
    raise NotImplementedError('TODO: implement')

def verify_audit(path):
    """Return (ok, message). Detects edited, deleted-in-the-middle or reordered lines."""
    raise NotImplementedError('TODO: implement')

def _clean(t, n=160):
    raise NotImplementedError('TODO: implement')

def _attempt(call, c):
    raise NotImplementedError('TODO: implement')

def run_flow(flow, call, dry_run=False, only_box=None, stop_file=..., audit_path=...):
    """Returns {'flow','verdict','results':[...],'next':str}. Never reports success it did not observe."""
    raise NotImplementedError('TODO: implement')

def _advice(row):
    raise NotImplementedError('TODO: implement')

def render(res):
    raise NotImplementedError('TODO: implement')

def load_flow(name):
    raise NotImplementedError('TODO: implement')

def list_flows():
    raise NotImplementedError('TODO: implement')

def main(argv):
    raise NotImplementedError('TODO: implement')
