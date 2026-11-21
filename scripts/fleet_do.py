# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Owner-account command control over existing paired, pinned fleet SSH.

  python3 scripts/fleet_do.py HOST                 # read-only status
  python3 scripts/fleet_do.py HOST <status|list_units|collect_logs|restart_service|rerun_check|readiness|sync_status|dashboard_deploy> [param]
  python3 scripts/fleet_do.py HOST exec [--timeout 60] -- PROGRAM ARG...

Exec uses the receiver's current owner-access policy and a bounded argv request,
with no implicit shell. Replies are JSON with remote exit code, stdout/stderr,
timeout and truncation flags. A failed command is distinct from a transport error.
Interactive commands use the existing dashboard terminal. No legacy fallback.
"""
import argparse
import json
import subprocess
import sys
import fleet_registry
from fleet_control import Fleet, FleetError

def host_names():
    """Registered computers, read fresh from data/fleet_registry.json on every call."""
    raise NotImplementedError('TODO: implement')

def usage():
    raise NotImplementedError('TODO: implement')

def call(box, action, param=None, caller=..., timeout=70):
    raise NotImplementedError('TODO: implement')

def execute(box, argv, timeout=60):
    """Delegate to the shared owner gate; never construct another SSH path."""
    raise NotImplementedError('TODO: implement')

class ExecParser(argparse.ArgumentParser):

    def error(self, message):
        raise NotImplementedError('TODO: implement')

def execution_exit_code(result):
    raise NotImplementedError('TODO: implement')

def main(argv):
    raise NotImplementedError('TODO: implement')
