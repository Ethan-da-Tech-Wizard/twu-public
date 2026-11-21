# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""relay_transport: synced file queue between the Mac and Linux sides (spec: data/relay_work/dashboard_spec.md section 3).
enqueue() scrubs the body with relay_scrub first and refuses (fail closed) if the scrubber blocks or any identifier would survive;
receive() re-scrubs, ignores unknown kinds / oversize / bad JSON, and REJECTS (moves aside) any message whose body changes under
scrubbing. Messages carry an opaque host alias only. Stdlib only, offline."""
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path
import relay_scrub as S

class TransportRefused(Exception):
    pass

def _clean(text):
    raise NotImplementedError('TODO: implement')

def enqueue(qdir, kind, body, alias, now=None):
    raise NotImplementedError('TODO: implement')

def receive(qdir):
    """-> (accepted messages, [(name, reason)] rejected). Rejected files are renamed *.rejected, never deleted."""
    raise NotImplementedError('TODO: implement')
