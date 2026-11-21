# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""twu_compress: pick the best lossless compressor for a file (NEED-340).

Tries zstd/xz/brotli CLIs when present plus stdlib lzma/zlib, verifies each
round-trip, and (with --write) writes the smallest as <file>.<ext> without
touching the original. Missing tools are skipped, never faked.
"""
from __future__ import annotations
import argparse
import lzma
import shutil
import subprocess
import sys
import zlib

def _cli(tool: str, args_c, args_d, data: bytes) -> bytes | None:
    raise NotImplementedError('TODO: implement')

def candidates(data: bytes, level: str=...) -> dict:
    raise NotImplementedError('TODO: implement')

def best(data: bytes, level: str=...):
    raise NotImplementedError('TODO: implement')

def main(argv=None) -> int:
    raise NotImplementedError('TODO: implement')
