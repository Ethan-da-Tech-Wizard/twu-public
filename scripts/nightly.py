# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Nightly rebuild (run by the LaunchAgent com.twu.contacts-midnight at 12:01 AM, and at login).
Rebuilds every generated file and cross-checks the databases, then refreshes Apple Reminders (macOS)."""
import os
import subprocess
import sys
