# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""
PROGRAM:       internals_citation_check.py
PROGRAMMER:    Magi 10 (claude, example_host), MAGI_TODO a4440a78
LAST MODIFIED: 2026-11-20
PURPOSE:       Check every `file:line` citation in docs/internals/*.md: the cited file must exist and the cited line (or
               line range) must lie inside it. Read-only. Never imports or runs any cited file.

WHY: the internals pages explain the system by pointing at exact lines. Dashboard and sweep files are edited by many seats, so line numbers drift
(ARCHITECTURE.md cited `serve` at 3854; it was at 3872 two days later). A page that points at the wrong line is worse than none, so the citations
are checked by a script and this tool is meant to run from the stale sweep / check_all so drift is reported, not discovered by a reader.

HOW IT READS A CITATION
  * `path/to/file.py:123` or `file.py:123-130` is a full citation (the file is resolved under the workspace, then scripts/, then docs/).
  * A bare `:123` or `:123-130` (preceded by a space, comma, parenthesis, or semicolon) borrows the MOST RECENT file named before it (a full
    citation, or a mention of a .py/.sh file). A page may declare `<!-- cite-default: scripts/x.py -->`: then every paragraph starts at that file and
    only a full citation changes it (use this for pages about one main source).
  * Citations inside fenced code blocks are ignored (diagrams).
  * A number written like a time (12:34) or a port (:8777) is not a citation: bare numbers must be followed by a non-digit and the borrowed
    file must be known, and numbers above the file's length are reported as BROKEN, so a stray port number would show; keep ports out of
    parentheses-adjacent positions or write them as `port 8777`.

USAGE:  python3 scripts/internals_citation_check.py [--dir docs/internals] [--root .] [--show-lines] [--json]
EXIT:   0 all citations resolve; 1 at least one broken citation; 2 usage error.

CHANGE HISTORY
  2026-11-20  Magi 10  Created for the internals pages.
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

def resolve(root: Path, name: str):
    """Find the cited file: as given, then under scripts/, docs/, data/ (first match). Returns Path or None."""
    raise NotImplementedError('TODO: implement')

def line_count(path: Path) -> int:
    raise NotImplementedError('TODO: implement')

def paragraphs(text: str):
    """Yield (first_line_no, text) for each blank-line-separated paragraph, skipping fenced code blocks."""
    raise NotImplementedError('TODO: implement')

def check_file(md: Path, root: Path):
    """Return (citations, broken) for one markdown file. A citation is a dict with doc, line, file, a, b, ok, reason.

    A bare `:123` borrows the file of the MOST RECENT file mention before it, with or without a line number, and the borrowed file carries over
    from one paragraph to the next within the same document (a page is written about one main source at a time). If a page mixes files in one
    sentence, name the file explicitly: the checker cannot know."""
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
