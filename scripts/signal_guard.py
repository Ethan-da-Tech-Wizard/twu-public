# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Process-wide safety net: while a unittest is running, refuse signals that can reach the whole session.

Why: on 2026-10-31 a mocked Popen's pid (a MagicMock, which converts to 1) reached os.killpg(1, SIGKILL) == kill(-1, SIGKILL)
and ended Ethan's desktop session three times. The example_hosted runner contains that, but anyone can run a test by hand.
This guard works for every launcher: install() wraps os.kill/os.killpg, and the wrapper checks AT CALL TIME whether
unittest is loaded, so production daemons (which never import unittest) are unaffected.

Blocked while testing: pid 0 / 1 / negative targets for kill, group <= 1 or our own group for killpg, non-integers
(mocks), and our own parent. Everything else (a test killing its own child) passes through unchanged.
"""
import os
import sys

def blocked_reason(pid, group=False):
    """Why this signal target is unsafe during a test, or None."""
    raise NotImplementedError('TODO: implement')

def _testing():
    raise NotImplementedError('TODO: implement')

def install():
    """Idempotent. Safe to call from sitecustomize/.pth at interpreter start."""
    raise NotImplementedError('TODO: implement')
