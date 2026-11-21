# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Adds verified command recipes to the Ethan CLI model's prompt when the question matches them.

Serves the loop step "model answers better today" without training: the recipes in system_command_knowledge.db are written
by hand, so a match is put in front of the model instead of leaving it to guess. Stays silent when nothing matches well.
"""
import re
import sys
from pathlib import Path

def _words(text):
    raise NotImplementedError('TODO: implement')

def pick(question, recipes, min_hits=..., limit=...):
    """recipes: dicts with canonical_command, description, intent_keywords, domain. Best matches first, weak ones dropped."""
    raise NotImplementedError('TODO: implement')

def knowledge_block(question, recipes=None):
    """Text to append to the system prompt, or '' when no recipe matches."""
    raise NotImplementedError('TODO: implement')
