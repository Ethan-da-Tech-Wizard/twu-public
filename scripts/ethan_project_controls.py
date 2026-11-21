# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Explicit local Git and editor actions for a trusted standalone Ethan project.

The interactive CLI bundles this standard-library helper and runs it inside its
own example_host. Its arguments are the launcher's projects directory and one typed
command. Git uses the real owner's hooks and a literal pathspec. The only
working tree operation is Git's ordinary clean-tree revert of a named checkpoint.

Chat's directory determines the repository. From the collection's parent, the
operator names one immediate child of projects; from inside a project, sibling
selection is unavailable. The helper never initializes or searches for a parent
repository. A receipt is the checkpoint commit and the hash shown in the CLI.
The subsequent revert has its own hash so both revisions remain inspectable.
"""
import fcntl
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
from urllib.parse import quote

class Refusal(ValueError):
    """A scoped project action could not safely complete."""

def git(root, *args):
    """Run one fixed-argv Git operation with the actual user's normal hooks.

    Return raw bytes, including NUL separators. Project strings never reach
    a shell. Restrict executable discovery and remove Git-setting overrides.
    """
    raise NotImplementedError('TODO: implement')

def project_file(root, name):
    """Check every component before using a literal filename or creating its URL.

    root is the resolved directory selected by the CLI. name is untrusted text
    typed after the action, possibly including spaces. Return an absolute Path
    only for an existing source file. Refusal or OSError ends the operation.
    This check writes nothing and never creates a missing editor target.
    """
    raise NotImplementedError('TODO: implement')

def validate_git(root):
    """Accept a plain, idle, local worktree with no project-supplied executables.

    root must identify the standalone project itself. Every preflight check
    runs before the first Git mutation. Unrecognized configuration, external
    metadata, hidden changes and in-progress operations raise Refusal.
    Local and global hooks remain under ordinary Git control.
    """
    raise NotImplementedError('TODO: implement')

def run(projects, root, command):
    """Execute one operator command and return its display text to the CLI.

    projects is compiled into the normal installation by the launcher. root
    is the trusted terminal workspace. command is the single argument supplied
    by the operator through the built-in slash menu.

    A checkpoint is a local commit on the current branch. Undo requires a
    clean worktree and the exact current checkpoint, and appends a revert.
    The project lock covers this helper's Git actions across terminal sessions.
    """
    raise NotImplementedError('TODO: implement')
