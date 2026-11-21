# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""dispatch_breaker.py: persisted circuit breaker for prompt dispatchers (stdlib, no model).

allow(path, text) records one attempt and returns False once the same text was tried more than MAX_ATTEMPTS times within
WINDOW_SEC; the circuit then stays open for OPEN_SEC. State lives in a small JSON file so one-shot dispatchers keep it too.
"""
import hashlib
import json
import os
import time

def _key(text):
    raise NotImplementedError('TODO: implement')

def allow(path, text, now=None):
    raise NotImplementedError('TODO: implement')
