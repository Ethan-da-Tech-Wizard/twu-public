# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""dashboard_registry: who owns every dashboard tab, route, button id and panel (data/relay_work/dashboard_registry.json).
Rule: read the registry before ANY dashboard edit. Id owned by another Magi -> ledger handoff note, do NOT edit. Unowned -> claim first.
  dashboard_registry.py check            exit 1 if any id discovered in the code is missing from the registry (lists them)
  dashboard_registry.py owner ID         print the owner (or UNOWNED / UNREGISTERED)
  dashboard_registry.py claim ID --owner OWNER --kind KIND --file FILE [--notes TEXT]   (under the per-file lock)
  dashboard_registry.py release ID --owner OWNER   remove an entry (only its owner may)
  dashboard_registry.py guard ID [--as OWNER]   exit 0 if OWNER may edit ID (owner matches or unowned), else 3 with the handoff hint
  dashboard_registry.py baseline-write   (once) record every route the code defines that nobody has claimed yet as GRANDFATHERED
Entry: {id, kind (tab|route|button|panel|shell), owner, file, since, notes}. Stdlib only.

2026-11-20 Magi 10 (MAGI_TODO d05abbd1): discovery now also finds page and API routes written as `route == "/x"`, `route in ("/a", "/b")`
and `route.startswith("/x/")` (prefix id "route:/x/"); every page route in twu_dashboard.py is written that way, so `check` used to pass
without a claim. /static/* and the manifest/icon files are assets, not routes. Routes that already existed unclaimed are listed in
data/relay_work/dashboard_route_baseline.json (GRANDFATHERED: reported by `check`, not blocking, so deploys keep working); any NEW route that
is neither claimed nor grandfathered makes `check` fail, exactly like a new button id."""
import json
import re
import sys
import time
from pathlib import Path

def load(path=None):
    raise NotImplementedError('TODO: implement')

def _page_routes(source: str) -> set:
    """Page and API routes (not /static assets) written as route == "/x", route in ("/a", "/b") or route.startswith("/x/") in the
    dashboard server source.  A prefix route keeps its trailing slash ("/commands/") so it is a different id from the page itself."""
    raise NotImplementedError('TODO: implement')

def grandfathered(path=None) -> set:
    """Route ids that existed unclaimed when route discovery was extended (data/relay_work/dashboard_route_baseline.json)."""
    raise NotImplementedError('TODO: implement')

def discover(scripts=...):
    """-> {id: (kind, file)} for everything the dashboard code defines right now."""
    raise NotImplementedError('TODO: implement')

def owner_of(reg, ident):
    raise NotImplementedError('TODO: implement')

def missing(reg=None, scripts=..., baseline=None):
    """Ids the code defines that are neither in the registry nor grandfathered (see the module doc).  These block `check` and deploys."""
    raise NotImplementedError('TODO: implement')

def unclaimed_grandfathered(reg=None, scripts=..., baseline=None):
    """Grandfathered routes that are still unclaimed (findings, not blocking)."""
    raise NotImplementedError('TODO: implement')

def can_edit(ident, who, reg=None):
    raise NotImplementedError('TODO: implement')

def claim(ident, owner, kind, file, notes=..., path=None):
    raise NotImplementedError('TODO: implement')

def release(ident, owner, path=None):
    """Remove an entry the OWNER no longer needs (only the owner may). Under the per-file lock."""
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
