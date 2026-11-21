# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""twu_pdf_shrink.py - shrink a PDF into a NEW file (never modifies the input).

Modes:
  lossless  qpdf --recompress-flate --object-streams=generate (qpdf, Apache-2.0)
  lossy     gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook (Ghostscript, AGPL-3.0-or-later;
            used only as an untouched system binary through subprocess, never linked
            or bundled. AGPL is allowed for this use by Ethan's 2026-11-05 license rule.)

Safety: input and output must resolve inside $HOME or the workspace; output must not
exist and must differ from the input; the output is verified with pdfinfo (poppler)
and the page count must match. A failed result is deleted. If the needed tool is
absent, prints an install hint and the pure-python fallback
(scripts/pdf_diet_compactor_cannon.py) and exits 2.

Usage: twu_pdf_shrink.py {lossless|lossy} IN.pdf OUT.pdf [--setting /ebook]
"""
from __future__ import annotations
import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

def allowed_roots() -> list[Path]:
    raise NotImplementedError('TODO: implement')

def check_path(p: Path) -> Path:
    raise NotImplementedError('TODO: implement')

def pdf_pages(path: Path) -> int:
    raise NotImplementedError('TODO: implement')

def build_cmd(mode: str, src: Path, dst: Path, setting: str) -> tuple[str, list[str]]:
    raise NotImplementedError('TODO: implement')

def shrink(mode: str, src: Path, dst: Path, setting: str=...) -> dict:
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
