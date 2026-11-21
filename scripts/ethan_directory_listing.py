# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Compact one authenticated native directory lookup without guessing a result."""
import json
import re
from pathlib import Path
from ethan_literal_note import _ALARM, fresh_context
from ethan_organization_preview import verified_names

def format_filenames(names, one, limit):
    raise NotImplementedError('TODO: implement')

def listing_turn(payload, admission, workspace, tools):
    """Return (path, verified answer or None) or abstain from this optimization."""
    raise NotImplementedError('TODO: implement')

def compact_request(request, directory, human):
    """One real model call. Required native tool and argument enum bind the exact named directory."""
    raise NotImplementedError('TODO: implement')

def verified_model_call(reply, directory):
    """Only release a genuine structured call with the authenticated path."""
    raise NotImplementedError('TODO: implement')
