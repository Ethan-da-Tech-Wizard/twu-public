# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""scripts/ez_settings.py: one place for EZ's deployment-specific names, hosts and paths.

PROGRAM: scripts/ez_settings.py
PROGRAMMER: Magi seat 5 (Claude)
LAST MODIFIED: 2026-11-21
PURPOSE: EZ_AUDIT items 5 and 7. EZ code must not hard-code people, device names
  or download locations. Every such value is read here, in this order:
    1. an environment variable (EZ_* below),
    2. an optional JSON file named by $EZ_SETTINGS_FILE (default
       ~/.config/ez/settings.json), keys are the lower-case env names without "EZ_",
    3. a neutral default.
  Other modules import the constants; nothing here touches the network or writes files.
KEYS (env name -> default):
  EZ_OWNER_NAME ("Owner")            display name of the first chat participant
  EZ_PARTNER_NAME ("Partner")        display name of the second chat participant
  EZ_OWNER_PRODUCER ("agent00")      event-bus producer id for the owner's messages
  EZ_PARTNER_PRODUCER ("partner")    event-bus producer id for everyone else
  EZ_BACKEND_HOST ("example_host")         fleet host id of the machine holding the Briar profile.
      NOTE: kept at the legacy value only because test_ez_briar_dashboard.py could not
      be claimed (sync-conflict on its claim row) so it could not be updated; set the
      variable or settings file on every other deployment.
  EZ_BACKEND_LABEL (capitalised host id)  wording used in user-facing messages
  EZ_BRIAR_VERSION ("1.5.24"), EZ_BRIAR_JAR_DIR (~/.local/share/ez-briar/downloads),
  EZ_BRIAR_JAR_NAME (briar-headless-linux-x86_64-<version>.jar)
"""
import json
import os
from pathlib import Path

def _file_settings() -> dict:
    """Read the optional JSON settings file; any problem means 'no file settings'.

    Returns:
        dict of string keys to values (empty when the file is absent or malformed).
    """
    raise NotImplementedError('TODO: implement')

def get(name: str, default: str) -> str:
    """Resolve one setting: env var, then settings file, then the default.

    Args:
        name: environment variable name, e.g. "EZ_OWNER_NAME".
        default: neutral fallback used when neither source has a non-empty value.

    Returns:
        The stripped string value.
    """
    raise NotImplementedError('TODO: implement')

def producer_for(sender: str) -> str:
    """Map a chat/commit author name to an event-bus producer id.

    Args:
        sender: display name; compared case-insensitively by prefix with OWNER_NAME.

    Returns:
        OWNER_PRODUCER when the name starts with the owner name, else PARTNER_PRODUCER.
    """
    raise NotImplementedError('TODO: implement')
