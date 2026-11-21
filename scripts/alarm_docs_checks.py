# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
import json
import platform
from pathlib import Path

def check_codebase_guide(now, health_dir=None):
    """The codebase guide (docs/CODEBASE_GUIDE) must keep covering every script: a NEW file with no family, or a receipt that
    stopped being refreshed, means the map is going stale. Reads the small receipt only (never walks the tree). LOW severity:
    the fix is one command, `python3 scripts/codebase_guide_build.py assign --apply` then `build`."""
    raise NotImplementedError('TODO: implement')

def check_owner_control(now, health_dir=None):
    """The lockout watch (scripts/owner_control_check.py) writes a receipt; a BLOCK means the owner cannot edit something right now
    (HIGH), a WARN is a thing to tidy (LOW), a receipt older than 3 days means the watch itself stopped. Reads the receipt only."""
    raise NotImplementedError('TODO: implement')
