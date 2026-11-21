# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Performance-per-watt probe: fixed CPU work, timed, with power sampled where the OS lets a normal user read it.

  ethan_power_bench.py [--seconds 8] [--workers 4] [--kind int|matmul|vector]

  --kind int     (default) one integer loop per worker; light (~17 W package), never reaches a power cap.
  --kind matmul  float32 matrix multiply (this numpy has a single-threaded generic BLAS: light, use vector instead).
  --kind vector  one numpy exp/sin loop per worker (SIMD-heavy); use --workers 16 to load every thread.

Prints one JSON line. Compare lines before/after a tuning change; a change is kept only if work_per_joule rises
(or watts fall) without work_per_second falling more than a few percent. Read-only: it changes no setting.
CPU package watts come from intel-rapl energy_uj, which is root-only on this machine, so cpu_watts is null
until that file is readable (the nvidia-smi GPU reading never needs root). One bounded run, no daemon.
"""
import argparse
import json
import multiprocessing as mp
import subprocess
import time
from pathlib import Path

def _work(deadline):
    raise NotImplementedError('TODO: implement')

def rapl_joules():
    raise NotImplementedError('TODO: implement')

def gpu_watts():
    raise NotImplementedError('TODO: implement')

def _matmul(deadline, n=1536):
    raise NotImplementedError('TODO: implement')

def _vector(deadline, n=...):
    raise NotImplementedError('TODO: implement')

def run(seconds=8.0, workers=4, kind=...):
    raise NotImplementedError('TODO: implement')
