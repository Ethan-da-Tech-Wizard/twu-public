# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Deterministic multi-language execution verifier (stdlib only, no model calls).

verify(lang, files, test_cmd=None, kind="test", timeout_s=20, expected_stdout=None)
  -> {status: PASS|FAIL|UNAVAILABLE|ERROR, stage: compile|run|test, reason, stdout_tail,
      stderr_tail, seconds, toolchain_version, example_host: 'bwrap'|'none'}

The candidate and its harness are written into a fresh temp dir, really compiled and run inside
bubblewrap (--unshare-all: no network, new pid/ipc/uts/user ns; --die-with-parent; read-only system
binds; only the temp dir is writable) with a wall-clock timeout, RLIMIT_DATA memory cap, CPU, file size
and process-count limits. PASS means: build exit 0, then the harness exit 0 (kind="test"), or exit 0
(kind="run"), and, when expected_stdout is given, stdout equal to it EXACTLY. Nothing is downloaded:
cargo --offline, go GOPROXY=off, dotnet restores only from the SDK's bundled packs (a project needing
NuGet/crates cannot fetch them -> ERROR, never PASS).

example_host policy: if bwrap is unusable the run is refused (ERROR) unless allow_unexample_hosted=True, in which
case example_host='none' is reported honestly. Heavy runs: wrap with scripts/ethan_capped_run.sh (E17).
Note: inside ethan_capped_run.sh WITHOUT ETHAN_HOST=1 the nested user namespace may be unavailable.
"""
from __future__ import annotations
import argparse
import glob
import json
import os
import re
import resource
import shutil
import signal
import subprocess
import sys
import tempfile
import time

def _run_plain(cmd, timeout=15):
    raise NotImplementedError('TODO: implement')

def _which(name, must_contain=None):
    """Resolve a real tool; skip shell wrapper scripts that shadow it (e.g. a fake `go` in ~/.local/bin)."""
    raise NotImplementedError('TODO: implement')

def _rust_sysroot():
    raise NotImplementedError('TODO: implement')

def _spec(lang):
    raise NotImplementedError('TODO: implement')

def bwrap_works() -> bool:
    raise NotImplementedError('TODO: implement')

def _limits(mem_bytes, cpu_s):
    raise NotImplementedError('TODO: implement')

def _tail(b):
    raise NotImplementedError('TODO: implement')

def _exec(spec, argv, work, timeout_s, mem_bytes, use_bwrap):
    """Run argv in the example_host. Returns (rc|None on timeout, stdout, stderr, timed_out)."""
    raise NotImplementedError('TODO: implement')

def _write_files(work, files):
    raise NotImplementedError('TODO: implement')

def _by_ext(files, *exts):
    raise NotImplementedError('TODO: implement')

def _entry(files, exts, prefer):
    raise NotImplementedError('TODO: implement')

def _plan(lang, files):
    """Return (extra_files, build_cmds, run_argv, error). build_cmds: list of argv."""
    raise NotImplementedError('TODO: implement')

def _result(status, stage, reason, out=..., err=..., t0=None, ver=..., example_host=...):
    raise NotImplementedError('TODO: implement')

def _finish(spec, lang, work, builds, run_argv, files_ok_stage, t0, timeout_s, mem_bytes, use_bwrap, kind, expected_stdout, test_cmd, allow_unexample_hosted):
    raise NotImplementedError('TODO: implement')

def verify(lang, files, test_cmd=None, kind=..., timeout_s=20, expected_stdout=None, mem_mb=2048, allow_unexample_hosted=False):
    raise NotImplementedError('TODO: implement')

def verify_project(files, build_cmd=None, smoke_cmd=None, timeout_s=60, mem_mb=3072, allow_unexample_hosted=False):
    """Project mode: real build (Makefile -> make, CMakeLists.txt -> cmake, Cargo.toml -> cargo --offline,
    *.csproj -> dotnet build) then a smoke command (exit 0, and optionally listed output) in the example_host."""
    raise NotImplementedError('TODO: implement')

def selftest(langs=None, timeout_s=15):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
