# Skeleton: interfaces only. Implementation intentionally omitted (TODO).
"""Near-zero-CPU thermal governor for the local model server (llama-server on 18190).

Policy (decide() is pure; everything else is thin I/O):
  * busy + hot       -> request power-saver (hysteresis: HOT_ENTER/HOT_EXIT, needs COOL_SAMPLES cool reads to leave)
  * we changed the profile -> always restore the ORIGINAL profile (also on exit/signal)
  * idle > IDLE_STOP_MIN and no connections and no slot processing -> stop the model server (identity-checked PID)
  * process table bloat (zombie storm, e.g. a parent that never wait()s) -> log it; a scan of /proc with ~20k
    zombies costs every pgrep/ps ~0.3-0.7 s of CPU and was measured as the dominant "idle" heat source.
Dry run is the default; --apply is opt-in. One log line per decision. Reads only sysfs, /proc and one cheap
nvidia-smi call per poll. Never edits fan curves. Never kills by name.
"""
import argparse, json, os, signal, subprocess, sys, time, urllib.request
from pathlib import Path
import ethan_safety
import ethan_thermal_guard as thermal_guard

def saver_enabled(env=..., flag=None):
    raise NotImplementedError('TODO: implement')

def decide(state, r, now, saver=False):
    """state: dict(profile_orig, profile_set, cool_n, idle_since). r: readings dict
    (cpu, gpu, busy, conns, tasks, profile). Returns (new_state, [action dicts])."""
    raise NotImplementedError('TODO: implement')

def cpu_temp(root=...):
    raise NotImplementedError('TODO: implement')

def gpu_temp():
    raise NotImplementedError('TODO: implement')

def task_total(path=...):
    raise NotImplementedError('TODO: implement')

def connections(port=..., path=...):
    """ESTABLISHED sockets whose LOCAL port is `port` (server side) -- no subprocess."""
    raise NotImplementedError('TODO: implement')

def slots_busy(port=...):
    raise NotImplementedError('TODO: implement')

def get_profile():
    raise NotImplementedError('TODO: implement')

def set_profile(p):
    raise NotImplementedError('TODO: implement')

def server_pid(proc=..., port=...):
    """Identity-checked: argv[0] basename llama-server AND --port <port>. Never by name alone."""
    raise NotImplementedError('TODO: implement')

def stop_server(pid, busy_fn=..., conn_fn=..., kill=...):
    """SIGTERM only when re-checked idle at the moment of stopping."""
    raise NotImplementedError('TODO: implement')

def log(event, **kw):
    raise NotImplementedError('TODO: implement')

def read_all(profile_fn=...):
    raise NotImplementedError('TODO: implement')

def run(apply, once=False, sleep=..., reader=..., clock=..., max_loops=None):
    raise NotImplementedError('TODO: implement')

def main(argv=None):
    raise NotImplementedError('TODO: implement')
