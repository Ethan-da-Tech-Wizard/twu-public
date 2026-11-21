# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Owned EZ projects: bounded files, text editing and isolated local Git worktrees.

No canonical company checkout, remote, shell, hooks, credential or execution API.
PROGRAM: scripts/ez_workspace.py
PROGRAMMER: existing author; comments by Magi seat 5 (Claude)
LAST MODIFIED: 2026-11-21
PURPOSE:
    Owns the on-disk side of "EZ projects": small shared project folders, each
    with its own local git repository (branch "main" in repo/) plus optional
    extra branches as git worktrees under worktrees/<branch>.  It exists so a
    chat/editor front end can let a partner create, read, edit, upload,
    download, diff and commit files without ever receiving a general shell,
    remote, hook, credential or arbitrary-path API.
    Invariants kept throughout: every path is validated by _parts(); every
    file or directory is opened relative to a directory file descriptor with
    O_NOFOLLOW; files must be regular, owned by this user, with one hard
    link; secret-looking content is refused; git runs with a scrubbed
    environment and a short timeout; one flock per project serialises work.
    Upstream: dashboards/seats that import Workspace (see HOW THIS WORKS).
    Downstream: the local filesystem and /usr/bin/git only.
    Tests: scripts/test_ez_workspace.py.
"""
from __future__ import annotations
from contextlib import contextmanager
from datetime import datetime, timezone
import base64
import binascii
import fcntl
import hashlib
import json
import mimetypes
import os
from pathlib import Path
import re
import secrets
import stat
import subprocess
import tempfile

class WorkspaceError(ValueError):
    """Failure raised by every Workspace operation.

    Subclasses ValueError so callers can catch it broadly; the status attribute carries an
    HTTP-style code (400 bad input, 404 missing, 409 busy or changed) for the web layer.
    """

    def __init__(self, message, status=400):
        """Build the error.

        Args:
            message: Plain-language, user-safe explanation.
            status: HTTP-style status code, default 400.
        """
        raise NotImplementedError('TODO: implement')

def _sha(raw):
    """Return the lower-case hex SHA-256 of raw bytes (used as the optimistic-concurrency token).

    Args:
        raw: Bytes to hash.
    Returns:
        A 64-character hex string.
    """
    raise NotImplementedError('TODO: implement')

def _name(value, branch=False):
    """Validate a project name or branch name against a strict allow-list pattern.

    Args:
        value: Candidate name.
        branch: True to use the looser branch pattern (letters of either case, underscore, up to 64);
            False for project ids (lower-case letters, digits, hyphen, up to 48).
    Returns:
        The unchanged value when valid.
    Raises:
        WorkspaceError: 400 if the value is not a string or does not fully match.
    """
    raise NotImplementedError('TODO: implement')

def _parts(value):
    """Split and vet a project-relative file path.

    Every user-supplied path goes through here before touching the disk.  Rejects empty,
    long, backslash-containing, dotted/hidden (except .gitignore), traversal, trailing-space or
    trailing-dot components, denied directory names, key/cert file extensions, well-known
    key file names and anything that mentions credential-like words.

    Args:
        value: Slash-separated relative path.
    Returns:
        List of path components.
    Raises:
        WorkspaceError: 400 with a generic message (it does not say which rule matched).
    """
    raise NotImplementedError('TODO: implement')

def _file_metadata(path, raw):
    """Describe a file for listings and downloads.

    Args:
        path: Project-relative path (used only for MIME guessing and echoed back).
        raw: File bytes.
    Returns:
        Dict with path, size, sha256, mime_type and editable (True only for small UTF-8 text
        without NUL bytes that is not image/audio/video/PDF).
    """
    raise NotImplementedError('TODO: implement')

def _check_shared_content(raw):
    """Refuse content that looks like a private key or service credential.

    Args:
        raw: File bytes (decoded leniently as UTF-8).
    Raises:
        WorkspaceError: 400 if any secret_scan.RULES pattern matches.
    Side effects:
        Imports secret_scan lazily so merely importing this module does not require it.
    """
    raise NotImplementedError('TODO: implement')

def _directory(path, create=False):
    """Open a directory by absolute path without following any symlink.

    Walks from the filesystem root one component at a time with O_NOFOLLOW so a symlinked
    component raises instead of redirecting.  The final directory must be owned by this user.

    Args:
        path: Directory path (made absolute and resolved once up front).
        create: If True, create missing components with mode 0700.
    Returns:
        An open directory file descriptor; the caller must os.close() it.
    Raises:
        WorkspaceError: if the directory is owned by someone else.
        OSError: (FileNotFoundError, NotADirectoryError, ...) if a component is missing or a symlink.
    """
    raise NotImplementedError('TODO: implement')

def _read_at(fd, name, maximum=...):
    """Read a bounded regular file by name relative to a directory fd.

    Args:
        fd: Open directory descriptor containing the file.
        name: Single file name (not a path).
        maximum: Largest allowed size in bytes.
    Returns:
        The file bytes.
    Raises:
        WorkspaceError: if it is not a regular file owned by this user with exactly one link,
            or it is larger than maximum.
        OSError: if the file is missing or is a symlink (O_NOFOLLOW).
    """
    raise NotImplementedError('TODO: implement')

class Workspace:
    """A collection of owned EZ projects under one private root folder.

    Each public method takes the project id (and usually a branch) and performs one
    bounded operation under a per-project lock.  Methods raise WorkspaceError on any
    refusal; they never return paths outside the project.
    """

    def __init__(self, root=None):
        """Create or open the projects root.

        Args:
            root: Folder for all projects; defaults to a per-user data folder.
        Raises:
            WorkspaceError: if the root is the company checkout or inside it, or is owned by another user.
        Side effects:
            Creates the folder (mode 0700) and records its device/inode so later calls detect replacement.
        """
        raise NotImplementedError('TODO: implement')

    @contextmanager
    def _root(self):
        """Open the projects root directory and verify its identity.

        Yields:
            Directory file descriptor of the root; closed on exit.
        Raises:
            WorkspaceError: 409 if the root was replaced since construction.
        """
        raise NotImplementedError('TODO: implement')

    @contextmanager
    def _locked(self, project=None):
        """Serialise operations with an flock.

        Args:
            project: Project id to lock and validate, or None to lock the projects root (used when creating a project).
        Yields:
            Directory fd (the project folder, or the root).
        Raises:
            WorkspaceError: 404 if the project folder is missing; 409 if another operation holds the lock;
                400 if the lock file is not a safe owned regular file; identity errors from _metadata().
        Side effects:
            Creates .ez-lock (mode 0600) if absent; releases the lock and closes fds on exit.
        """
        raise NotImplementedError('TODO: implement')

    def _metadata(self, project, fd=None):
        """Load and validate a project's .ez-project.json identity file.

        Args:
            project: Project id.
            fd: Open directory fd of the project; if None, open it by path.
        Returns:
            The parsed metadata dict.
        Raises:
            WorkspaceError: 404 if the file is missing/unreadable/invalid JSON (not an EZ project);
                409 if the schema or id do not match.
        """
        raise NotImplementedError('TODO: implement')

    def _branch_root(self, project, branch):
        """Locate and verify the checkout folder for a branch.

        Re-checks, on every call, that the git directory/worktree link really belongs to this project
        and that the repository config still matches the hash recorded at creation.

        Args:
            project: Project id.
            branch: "main" (the repo/ folder) or a worktree branch name.
        Returns:
            Path of the checkout folder.
        Raises:
            WorkspaceError: 404 if the worktree is missing; 400 if its metadata points elsewhere;
                409 if config changed (from _check_git_config).
        """
        raise NotImplementedError('TODO: implement')

    def project_root(self, project, branch=...):
        """Private local accessor; callers must not expose it as an arbitrary path API."""
        raise NotImplementedError('TODO: implement')

    def _check_git_config(self, project):
        """Verify the main repository's config is unchanged and has no external object stores.

        Args:
            project: Project id.
        Raises:
            WorkspaceError: 409 if config's SHA-256 differs from the value recorded in the identity file
                (someone edited it outside EZ); 400 if alternates or shallow files exist.
        """
        raise NotImplementedError('TODO: implement')

    def _git(self, cwd, arguments, check=True):
        """Run /usr/bin/git locally and capture its output.

        The environment is rebuilt from scratch (no user/system config, no prompts), hooks, pager,
        fsmonitor, credential helpers and every network protocol are disabled on the command line.

        Args:
            cwd: Directory to run in (a checkout folder).
            arguments: git arguments after the fixed safety options.
            check: If True, a non-zero exit becomes an error; if False the caller reads the return code.
        Returns:
            Tuple (stdout text, return code).
        Raises:
            WorkspaceError: 409 on timeout (15 s) or failed command; 400 if output exceeds 2 * MAX_PROJECT.
        Side effects:
            Runs a subprocess; may modify the repository for write commands.
        """
        raise NotImplementedError('TODO: implement')

    def list_projects(self):
        """List valid projects in the root.

        Returns:
            List of {id, name, default_branch} sorted by id.
        Raises:
            WorkspaceError: if more than MAX_ENTRIES entries exist in the root.
        """
        raise NotImplementedError('TODO: implement')

    def create_project(self, name):
        """Create a project with a starter README and hello script, committed on main.

        Args:
            name: Human project name (1-80 chars); lower-cased with spaces turned into hyphens for the id.
        Returns:
            Dict with id, name, default_branch and branch.
        Raises:
            WorkspaceError: 400 for a bad name; 409 if the project exists or git fails.
        Side effects:
            Makes folders (0700), runs git init and commit, writes .ez-project.json (0600) last so an
            interrupted creation never looks like a valid project.
        """
        raise NotImplementedError('TODO: implement')

    def _tree(self, path):
        """Walk a checkout and return metadata for every shared file and directory.

        Also acts as a safety audit: it raises if it meets a symlink, special file, foreign-owned or
        multi-link entry, secret-looking content, too many entries or too many bytes.

        Args:
            path: Checkout folder.
        Returns:
            Rows sorted by path: {path, type: "directory", size: 0} or file metadata plus type "file".
        Raises:
            WorkspaceError: on any unsafe or oversized content.
        """
        raise NotImplementedError('TODO: implement')

    def tree(self, project, branch=...):
        """List all shared files in a branch.

        Args:
            project: Project id.
            branch: Branch name, default "main".
        Returns:
            Dict with project, branch and files (see _tree).
        Raises:
            WorkspaceError: see _locked, _branch_root, _tree.
        """
        raise NotImplementedError('TODO: implement')

    @contextmanager
    def _parent(self, root, path, create=False):
        """Resolve a validated path to its parent directory fd and final name.

        Args:
            root: Checkout folder.
            path: Project-relative file path (validated by _parts).
            create: If True, create missing intermediate directories (mode 0700).
        Yields:
            (directory fd, file name); fd is closed on exit.
        Raises:
            WorkspaceError: 400 for bad paths or a foreign-owned directory.
            OSError: if an intermediate directory is missing (when not creating) or is a symlink.
        """
        raise NotImplementedError('TODO: implement')

    def read_file(self, project, path, branch=...):
        """Read one UTF-8 text file for editing.

        Args:
            project: Project id.
            path: Project-relative file path.
            branch: Branch name.
        Returns:
            Dict with path, text, sha256 (the token to pass back on save) and branch.
        Raises:
            WorkspaceError: 404 if missing; 400 if not UTF-8 text, too large, unsafe or secret-looking.
        """
        raise NotImplementedError('TODO: implement')

    def save_file(self, project, path, text, expected_sha256, branch=...):
        """Save text into an existing or new file.

        Args:
            project: Project id.
            path: Project-relative file path.
            text: New contents (UTF-8, no NUL, at most MAX_FILE bytes).
            expected_sha256: SHA-256 of the version the caller opened, or None when creating a new file.
            branch: Branch name.
        Returns:
            Dict with path, text, new sha256 and branch.
        Raises:
            WorkspaceError: 400 for bad text, 409 if the file changed or STOP is active (see _save_bytes).
        Side effects:
            Atomically replaces the file on disk.
        """
        raise NotImplementedError('TODO: implement')

    def _save_bytes(self, project, path, raw, expected_sha256, branch):
        """Shared atomic writer behind save_file and upload_file.

        Order of checks: STOP flag, path rules, secret content, hash format, then (under the lock)
        project size and the optimistic-concurrency comparison.  The write goes to a temp file in the
        same directory, is fsynced, then renamed over the target so readers never see a partial file.

        Args:
            project: Project id.
            path: Project-relative file path.
            raw: New file bytes.
            expected_sha256: Previous file's hash, or None for a new file.
            branch: Branch name.
        Raises:
            WorkspaceError: 409 if STOP exists, the project is busy, or the file changed; 400 for rule violations.
        Side effects:
            Creates intermediate directories; writes and fsyncs a file; removes any leftover temp file.
        """
        raise NotImplementedError('TODO: implement')

    def upload_file(self, project, path, content_base64, expected_sha256, branch=...):
        """Import explicit bytes into an owned project; never execute or unpack them."""
        raise NotImplementedError('TODO: implement')

    def download_file(self, project, path, branch=...):
        """Return bounded project bytes as data, with MIME metadata only."""
        raise NotImplementedError('TODO: implement')

    def branches(self, project):
        """List local branches.

        Args:
            project: Project id.
        Returns:
            List of {name, head, current}; "current" is simply name == "main".
        """
        raise NotImplementedError('TODO: implement')

    def create_branch(self, project, name, base=...):
        """Create a branch as a new git worktree.

        Args:
            project: Project id.
            name: New branch name (not "main").
            base: Existing branch to start from.
        Returns:
            Dict with name, branch and the new head commit.
        Raises:
            WorkspaceError: 409 if main is requested or the worktree exists; others from _git/_branch_root.
        Side effects:
            Runs git worktree add; creates worktrees/<name>.
        """
        raise NotImplementedError('TODO: implement')

    def history(self, project, branch=...):
        """Return up to 40 recent commits across all branches.

        Args:
            project: Project id.
            branch: Branch whose checkout the command runs in (log covers all refs).
        Returns:
            List of dicts: hash, parents, subject, author, date, refs.
        """
        raise NotImplementedError('TODO: implement')

    def diff(self, project, branch=...):
        """Show uncommitted changes against HEAD.

        Args:
            project: Project id.
            branch: Branch name.
        Returns:
            Dict with patch (cut to 1 MiB), truncated flag, porcelain status text and branch.
        """
        raise NotImplementedError('TODO: implement')

    def commit(self, project, message, branch=...):
        """Commit all current project files on a branch.

        Args:
            project: Project id.
            message: One-line message of 1-300 characters, no control characters.
            branch: Branch name.
        Returns:
            Dict with the new commit hash, branch and message.
        Raises:
            WorkspaceError: 400 for a bad message; 409 if there is nothing to commit or git fails.
        Side effects:
            Stages every audited file and creates a commit.
        """
        raise NotImplementedError('TODO: implement')
