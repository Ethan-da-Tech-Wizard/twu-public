# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Record each self-improvement cycle through Enki Waypoint (stage contract + receipt) with a Loom-readable reflection.

Uses enki_waypoint.Waypoint unchanged: its local JobQueue (sqlite, outside the workspace). No model, service or network
is touched, so the "local-queue path" IS the adapter's own path. Roles: Forge runs the rollout, Probe's checks are the
mechanical acceptance receipts, Lens is the stage verifier (a mechanical gate on those checks, not a semantic review),
Relay is the receipt. The reflection candidate is stored in the Waypoint receipt (where enki_loom reads it) and is
NEVER applied automatically.
"""
import hashlib, json, sys, time
from pathlib import Path
import enki_waypoint as wp
from example_host_job_queue import default_state_dir

def default_state():
    raise NotImplementedError('TODO: implement')

def _sha(path):
    raise NotImplementedError('TODO: implement')

def begin_cycle(name, formulas_version, tasks, k, budget=..., *, root=None, state_dir=None):
    """State outcome, scope, acceptance checks and repair budget BEFORE the stage; claim it as Forge. Returns a handle."""
    raise NotImplementedError('TODO: implement')

def weakest_category(records, categories):
    raise NotImplementedError('TODO: implement')

def reflection_for(handle, records, stop_reason):
    raise NotImplementedError('TODO: implement')

def finish_cycle(handle, records, stop_reason=None):
    """Write fresh hash-bound evidence + check receipts, Lens gate, and finish the Waypoint. Returns the receipt."""
    raise NotImplementedError('TODO: implement')
