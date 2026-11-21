# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""
scripts/ethan_model_personality_registry.py — Host System Administrator Persona &
`/models` personality and training-recipe switcher for Ethan CLI (`scripts/ethan`).

Ethan's Directive (2026-10-20):
  1. "Can you make it so that whenever I open up gemini cli known as ethan cli, it's already
      loaded in with the proper System Administrator for each computer?"
  2. "And also I should be able to do `/models` and load in other models and their appropriate
      personalities and that of course already come prewired in with the right adapters along
      with the models you understand."

Architecture:
  - Detects the current host platform and constructs
    the hardware-aware Host System Administrator & Sovereign Liaison system prompt.
  - Maintains a persistent active profile in `data/example_host/active_ethan_personality.json`
    (defaulting to `sysadmin`), pre-wired with:
      * Base local GGUF model path/identifier
      * Role-specific LoRA/DPO adapter name & dataset path
      * Specialized system persona prompt & toolbelt directives
  - Intercepts `/models`, `/model`, `/model <name>`, and `/models <name>` inside both
    `scripts/gemini_broker_bridge.py` (live chat) and `scripts/ethan` (CLI subcommand).
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import platform
import sys
from typing import Any, Dict, List, Optional, Tuple

def is_apple_silicon_m1(platform_override: Optional[str]=None) -> bool:
    """True if running on Apple Silicon M1 / arm64 macOS."""
    raise NotImplementedError('TODO: implement')

def is_example_host(platform_override: Optional[str]=None) -> bool:
    """True if running on example_host Linux (outside client / canary MBP14,1)."""
    raise NotImplementedError('TODO: implement')

def configured_model_for_host(host: str, variant: str=...) -> Optional[str]:
    """Read the same explicit host selection used by the model switcher."""
    raise NotImplementedError('TODO: implement')

def get_abliterated_model_for_platform(platform_override: Optional[str]=None) -> str:
    """Returns device-specific abliterated model variant."""
    raise NotImplementedError('TODO: implement')

def detect_host_environment(platform_override: Optional[str]=None) -> Dict[str, Any]:
    """Returns hardware-specific System Administrator context for the current computer."""
    raise NotImplementedError('TODO: implement')

def resolve_profile_key(query: str) -> Optional[str]:
    """Resolves a profile key or alias (e.g. 'howitzer' -> 'cannon', 'sysadmin' -> 'sysadmin')."""
    raise NotImplementedError('TODO: implement')

def get_adapter_pair_count(dataset_filename: str) -> int:
    """Returns the number of verified DPO training pairs currently in the pre-wired adapter JSONL."""
    raise NotImplementedError('TODO: implement')

def live_model_name() -> Optional[str]:
    """Name of the GGUF the local llama-server is actually running, or None (Linux only; /proc is read-only)."""
    raise NotImplementedError('TODO: implement')

def get_active_profile(state_file: Optional[Path]=None, platform_override: Optional[str]=None) -> Dict[str, Any]:
    """Loads the active model+personality+adapter profile, defaulting to the Host System Administrator (`sysadmin`)."""
    raise NotImplementedError('TODO: implement')

def set_active_profile(profile_query: str, state_file: Optional[Path]=None, platform_override: Optional[str]=None, receipt_dir: Optional[Path]=None) -> Tuple[bool, Dict[str, Any], str]:
    """Switches the active Ethan CLI model + personality + adapter profile and persists it."""
    raise NotImplementedError('TODO: implement')

def build_combined_system_instruction(existing_system_text: str=..., state_file: Optional[Path]=None, platform_override: Optional[str]=None, compact: bool=False) -> str:
    """
    Constructs the combined Host System Administrator + Active Personality + Pre-Wired Adapter
    system instruction that is automatically prepended to Ethan CLI sessions.
    """
    raise NotImplementedError('TODO: implement')

def format_models_catalog_table(state_file: Optional[Path]=None, platform_override: Optional[str]=None) -> str:
    """Formats the interactive `/models` catalog showing all pre-wired models, personalities, and adapters."""
    raise NotImplementedError('TODO: implement')

def extract_last_user_text(gemini_payload: Dict[str, Any]) -> str:
    """Extracts the latest user message text from a Gemini generateContent request payload."""
    raise NotImplementedError('TODO: implement')

def trigger_live_model_reload(target: str=..., repo_root: Optional[Path]=None) -> Tuple[bool, str]:
    """
    Triggers the live model reloading via ethan_abli.
    target is 'abli' or 'vanilla'.
    """
    raise NotImplementedError('TODO: implement')

def intercept_models_command(user_text: str, state_file: Optional[Path]=None, platform_override: Optional[str]=None, receipt_dir: Optional[Path]=None) -> Optional[str]:
    """
    Checks if the user typed `/models`, `/model`, `/model <name>`, `/abli`, or `/abli <name>`.
    If so, returns the immediate formatted response (and switches profile if a target name was given).
    Returns None if the message is normal conversation.
    """
    raise NotImplementedError('TODO: implement')

def main() -> int:
    raise NotImplementedError('TODO: implement')
