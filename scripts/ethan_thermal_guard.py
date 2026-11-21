#!/usr/bin/env python3
# >>> HOW THIS WORKS
# FLOW:    1 main() parses --status / --ensure; with neither it calls run(), the endless guard loop.
#          2 run() takes an exclusive lock on data/thermal_guard.lock (a second guard just exits 0) and refuses if the legacy /tmp lock is held.
#          3 Every second find_server() looks for a process named llama-server; inspect_server() accepts it only if the port is exactly 18190 and its cwd is this repo.
#          4 It reads gpu_temp(), cpu_temp(), ram_gib() and asks action_for() what to do: SIGSTOP (pause), SIGCONT (resume), SIGKILL (abort) or nothing.
#          5 signal_managed() re-checks the process identity (pid + start time + args) right before signalling, so a reused PID is never hit.
#          6 Each pause/resume/abort is appended to the per-host log (data/thermal_guard.jsonl via per_host).
# DATA:    reads /proc, nvidia-smi, sensors, /sys/class/hwmon, pmset/vm_stat (macOS); reads the files business/example_host/comms/STOP and MODEL_STANDBY (their existence = blocked).
#          writes data/thermal_guard.lock and the log. Callers (grep): boot_readiness.py, muster.py, prompt_tuner.py, thermal_baseline.py, ethan_tune.py, ethan_eval_ab.py, local_runner_build_gate.py.
# FAILS:   Any unreadable temperature or RAM (None/NaN/negative) counts as unknown, and unknown means PAUSE (fails closed). GPU >= 100 C kills the server. RAM under 1.5 GiB pauses.
#          STOP or MODEL_STANDBY present means pause. On exit or signal the guard pauses its server and never resumes it. If signalling fails run() logs signal_failed and returns 1.
#          After 1800 s with no server the guard exits 0. Resume needs GPU <= 98, CPU <= 99 and RAM >= 2.0 GiB.
# EXTEND:  Thresholds are the constants near the top (SOFT_/PAUSE_/RESUME_/ABORT_GPU, *_CPU, MIN_RAM_GIB); decisions live in action_for() and start_blocker(). Test file: scripts/test_ethan_thermal_guard.py
#          Test: scripts/ethan_capped_run.sh env PYTHONPATH=scripts python3 -B -m unittest -q scripts.test_ethan_thermal_guard
# GLOSSARY: SIGSTOP freezes a process, SIGCONT unfreezes it, SIGKILL ends it. On macOS the "temperature" is a made-up scale from pmset throttle percent, not degrees.
# <<< HOW THIS WORKS
"""Fresh-telemetry Linux guard for this workspace's llama-server on port 18190.

Unknown heat/RAM pauses work; GPU abort kills only the identity-checked server.
A stopped guard never resumes unguarded work. No model calls or server starts.
"""
import argparse, fcntl, glob, json, math, os, re, signal, subprocess, sys, time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from host_paths import per_host  # per-host log name, see host_paths.py (2026-11-19 Magi 10)
LOG = REPO / per_host("data/thermal_guard.jsonl")  # was the shared data/thermal_guard.jsonl: two computers appended to one synced file
LOCK = REPO / "data" / "thermal_guard.lock"
LEGACY_LOCK = Path("/tmp/ethan_thermal_guard.lock")
PROC = Path("/proc")
STOP = REPO / "business/example_host/comms/STOP"
STANDBY = REPO / "business/example_host/comms/MODEL_STANDBY"
# Ethan, 2026-11-19: routine hot operation must not stop useful work. Native
# telemetry reports GPU slowdown 98 C / shutdown 101 C and CPU critical 100 C.
# Keep only the near-critical margin; 87 C is a cooling target, not a fault.
SOFT_GPU, PAUSE_GPU, RESUME_GPU, ABORT_GPU, START_MAX_GPU = 98, 99, 98, 100, 98
SOFT_CPU, PAUSE_CPU, RESUME_CPU = 99, 100, 99
MIN_RAM_GIB = 1.5


def inspect_server(pid, *, port=18190):
    """Observe the executable, requested port and workspace; retain birth identity."""
    if sys.platform == "darwin":
        return _inspect_server_darwin(pid, port=port)
    try:
        folder = PROC / str(pid)
        args = tuple(arg.decode() for arg in (folder / "cmdline").read_bytes().split(b"\0") if arg)
        if not args or Path(args[0]).name != "llama-server":
            return None
        if (folder / "exe").resolve(strict=True).name != "llama-server":
            return None
        ports = [args[i + 1] for i in range(len(args) - 1) if args[i] in {"--port", "-p"}]
        ports.extend(arg.split("=", 1)[1] for arg in args if arg.startswith("--port="))
        if ports != [str(port)]:
            return None
        if (folder / "cwd").resolve(strict=True) != REPO.resolve():
            return None
        fields = (folder / "stat").read_text().rsplit(")", 1)[1].split()
        if fields[0] in {"Z", "X"}:
            return None
        return {"pid": pid, "identity": (pid, int(fields[19]), args),
                "stopped": fields[0] in {"T", "t"}}
    except (OSError, ValueError, IndexError, UnicodeError):
        return None


def _inspect_server_darwin(pid, *, port=18190):
    """Same identity requirements as the /proc path, read through ps and lsof.
    Identity uses the kernel-reported start time in place of /proc stat field 21."""
    try:
        result = subprocess.run(["ps", "-p", str(pid), "-o", "state=,lstart=,command="],
                                capture_output=True, text=True, timeout=5)
        line = result.stdout.strip()
        if result.returncode or not line:
            return None
        state, rest = line.split(None, 1)
        parts = rest.split(None, 5)  # lstart is five fields: weekday month day time year
        if len(parts) < 6:
            return None
        started, command = " ".join(parts[:5]), parts[5]
        args = tuple(command.split())
        if not args or Path(args[0]).name != "llama-server":
            return None
        ports = [args[i + 1] for i in range(len(args) - 1) if args[i] in {"--port", "-p"}]
        ports.extend(arg.split("=", 1)[1] for arg in args if arg.startswith("--port="))
        if ports != [str(port)]:
            return None
        if state.startswith(("Z", "X")):
            return None
        cwd = subprocess.run(["lsof", "-a", "-p", str(pid), "-d", "cwd", "-Fn"],
                             capture_output=True, text=True, timeout=5)
        folders = [row[1:] for row in cwd.stdout.splitlines() if row.startswith("n")]
        if len(folders) != 1 or Path(folders[0]).resolve() != REPO.resolve():
            return None
        return {"pid": pid, "identity": (pid, started, args), "stopped": state.startswith("T")}
    except (OSError, ValueError, IndexError, subprocess.SubprocessError):
        return None


def find_server(*, port=18190):
    """Read-only observation; control callers retain their default port identity."""
    try:
        result = subprocess.run(["pgrep", "-x", "llama-server"], capture_output=True, text=True, timeout=5)
        candidates = [inspect_server(int(value), port=port) for value in result.stdout.split()]
        matches = [item for item in candidates if item is not None]
        if len(matches) > 1:
            raise RuntimeError("multiple managed server identities; refusing an ambiguous target")
        return matches[0] if matches else None
    except (OSError, ValueError, subprocess.SubprocessError):
        return None


def server_pid():
    server = find_server()
    return server["pid"] if server else None


def signal_managed(server, action):
    """Pin a kernel process handle before revalidation so PID reuse cannot retarget it."""
    if sys.platform == "darwin":
        # No pidfd on macOS: revalidate the full identity (including start time)
        # immediately before signalling; a reused PID cannot match the birth identity.
        current = inspect_server(server["pid"])
        if current is None or current["identity"] != server["identity"]:
            return False
        try:
            os.kill(server["pid"], action)
            return True
        except OSError:
            return False
    try:
        descriptor = os.pidfd_open(server["pid"])
        try:
            current = inspect_server(server["pid"])
            if current is None or current["identity"] != server["identity"]:
                return False
            signal.pidfd_send_signal(descriptor, action)
            return True
        finally:
            os.close(descriptor)
    except (OSError, AttributeError):
        return False


def darwin_pressure_percent():
    """Unprivileged macOS thermal signal: the lowest of CPU_Speed_Limit / CPU_Scheduler_Limit
    from `pmset -g therm`. 100 means nominal. None when unreadable, so callers fail closed."""
    try:
        result = subprocess.run(["pmset", "-g", "therm"], capture_output=True, text=True, timeout=5, check=True)
        values = [int(v) for v in re.findall(r"CPU_(?:Speed|Scheduler)_Limit\s*=\s*(\d+)", result.stdout)]
        if values:
            return min(values)
        # Intel Macs output 'No thermal warning level'; Apple Silicon (M-series fanless) outputs
        # 'Error:Failed to get thermal warning level with error code 0xe00002bc' (kIOReturnUnsupported).
        # Both represent nominal operating temperature with zero active throttling.
        if "No thermal warning level" in result.stdout or "0xe00002bc" in result.stdout or "Failed to get thermal warning level" in result.stdout:
            return 100
    except (OSError, ValueError, subprocess.SubprocessError):
        pass
    return None


def darwin_gate_value(percent, resume, pause, abort_at=None):
    """Map macOS thermal pressure onto the Linux-calibrated gate scale. NOT a physical
    temperature: nominal (>=100%) reads just under the resume gate, mild throttling just
    under the pause gate, heavy throttling at the pause gate, severe (<50%) at abort."""
    if percent is None:
        return None
    if percent >= 100:
        return resume - 1
    if abort_at is not None and percent < 50:
        return abort_at
    if percent >= 80:
        return pause - 1
    return pause


def gpu_temp():
    if sys.platform == "darwin":
        return darwin_gate_value(darwin_pressure_percent(), START_MAX_GPU, PAUSE_GPU, ABORT_GPU)
    try:
        result = subprocess.run(["nvidia-smi", "--query-gpu=temperature.gpu", "--format=csv,noheader"],
                                capture_output=True, text=True, timeout=5, check=True)
        return max(int(float(value)) for value in result.stdout.strip().splitlines())
    except (OSError, ValueError, subprocess.SubprocessError):
        pass
    try:
        for p in glob.glob("/sys/class/hwmon/hwmon*"):
            try:
                name = (Path(p) / "name").read_text().strip()
            except OSError:
                continue
            if name == "applesmc":
                for lbl in glob.glob(f"{p}/temp*_label"):
                    try:
                        if Path(lbl).read_text().strip() in ("TCGC", "TG0D", "TG0P"):
                            inp = Path(lbl.replace("_label", "_input"))
                            val = float(inp.read_text().strip()) / 1000.0
                            if val > 0:
                                return val
                    except (OSError, ValueError):
                        continue
            elif name in ("amdgpu", "nouveau"):
                for inp_file in glob.glob(f"{p}/temp*_input"):
                    try:
                        val = float(Path(inp_file).read_text().strip()) / 1000.0
                        if val > 0:
                            return val
                    except (OSError, ValueError):
                        continue
        if Path("/sys/class/drm/card0").exists() and not Path("/proc/driver/nvidia/gpus").exists():
            return 45.0
    except Exception:
        pass
    return None


def cpu_temp():
    if sys.platform == "darwin":
        return darwin_gate_value(darwin_pressure_percent(), SOFT_CPU, PAUSE_CPU)
    try:
        result = subprocess.run(["sensors"], capture_output=True, text=True, timeout=5, check=True)
        values = re.findall(r"Package id \d+:\s*\+?(\d+(?:\.\d+)?)", result.stdout)
        if values:
            return max(float(value) for value in values)
    except (OSError, ValueError, subprocess.SubprocessError):
        pass
    try:
        for p in glob.glob("/sys/class/hwmon/hwmon*"):
            try:
                name = (Path(p) / "name").read_text().strip()
            except OSError:
                continue
            if name in ("coretemp", "k10temp", "cpu_thermal"):
                for lbl in glob.glob(f"{p}/temp*_label"):
                    try:
                        label = Path(lbl).read_text()
                        if "Package id" in label or "Tdie" in label or "Tctl" in label:
                            inp = Path(lbl.replace("_label", "_input"))
                            return float(inp.read_text().strip()) / 1000.0
                    except (OSError, ValueError):
                        continue
                inp = Path(p) / "temp1_input"
                if inp.exists():
                    try:
                        return float(inp.read_text().strip()) / 1000.0
                    except (OSError, ValueError):
                        pass
        for p in glob.glob("/sys/class/thermal/thermal_zone*"):
            try:
                t = (Path(p) / "type").read_text().strip()
                if t in ("x86_pkg_temp", "cpu-thermal", "soc-thermal"):
                    return float((Path(p) / "temp").read_text().strip()) / 1000.0
            except (OSError, ValueError):
                continue
    except Exception:
        pass
    return None


def ram_gib():
    if sys.platform == "darwin":
        try:
            result = subprocess.run(["vm_stat"], capture_output=True, text=True, timeout=5, check=True)
            page = re.search(r"page size of (\d+)", result.stdout)
            counts = dict(re.findall(r"Pages (free|inactive|speculative):\s+(\d+)\.", result.stdout))
            if page and counts:
                pages = sum(int(value) for value in counts.values())
                return pages * int(page[1]) / 1073741824
        except (OSError, ValueError, subprocess.SubprocessError):
            pass
        return None
    try:
        for line in (PROC / "meminfo").read_text().splitlines():
            match = re.fullmatch(r"MemAvailable:\s+(\d+)\s+kB", line)
            if match:
                return int(match[1]) / 1048576
    except (OSError, ValueError):
        pass
    return None


def known(value):
    return type(value) in (int, float) and math.isfinite(value) and value >= 0


def start_blocker(gpu, cpu, ram, minimum_ram=MIN_RAM_GIB):
    if not all(known(value) for value in (gpu, cpu, ram)):
        return "fresh GPU, CPU and available-RAM readings are required"
    if gpu > START_MAX_GPU or cpu >= PAUSE_CPU:
        return f"unsafe start temperature: GPU={gpu}, CPU={cpu}"
    if ram < minimum_ram:
        return f"insufficient available RAM: {ram:.2f} GiB, need {minimum_ram:.2f} GiB"
    return None


def action_for(gpu, cpu, ram, *, stopped, starting=False, blocked=False):
    if known(gpu) and gpu >= ABORT_GPU:
        return signal.SIGKILL
    if blocked or not all(known(value) for value in (gpu, cpu, ram)):
        return None if stopped else signal.SIGSTOP
    if gpu >= PAUSE_GPU or cpu >= PAUSE_CPU or ram < MIN_RAM_GIB or (starting and gpu > START_MAX_GPU):
        return None if stopped else signal.SIGSTOP
    if stopped and gpu <= RESUME_GPU and cpu <= RESUME_CPU and ram >= MIN_RAM_GIB + 0.5:
        return signal.SIGCONT
    return None


def log(event, **kw):
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG, "a") as stream:
        stream.write(json.dumps({"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                                 "event": event, **kw}) + "\n")


def guard_running():
    LOCK.parent.mkdir(parents=True, exist_ok=True)
    with LOCK.open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            return True
        return False


def legacy_guard_running():
    """An old controller must be stopped explicitly before this safer controller runs."""
    try:
        with LEGACY_LOCK.open("r") as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                return True
        return False
    except FileNotFoundError:
        return False
    except OSError:
        return True


def platform_supported():
    """Linux needs pidfd signalling; macOS uses the revalidate-then-kill fallback."""
    if sys.platform == "darwin":
        return True
    return sys.platform.startswith("linux") and hasattr(os, "pidfd_open") and hasattr(signal, "pidfd_send_signal")


def ensure_guard():
    if not platform_supported():
        return False
    if legacy_guard_running():
        return False
    if guard_running():
        return True
    proc = subprocess.Popen([sys.executable, str(Path(__file__).resolve())],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
    deadline = time.monotonic() + 2.0
    while time.monotonic() < deadline:
        if guard_running():
            return True
        if proc.poll() is not None:
            return False
        time.sleep(0.05)
    if proc.poll() is None:
        proc.terminate()
    return False


def run():
    if not platform_supported():
        return 1
    if legacy_guard_running():
        return 1
    LOCK.parent.mkdir(parents=True, exist_ok=True)
    with LOCK.open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            return 0
        current = previous_identity = None
        idle_since = None

        def release(*_):
            raise SystemExit(0)  # finally pauses our exact server; never resume on exit.

        handlers = {sig: signal.getsignal(sig) for sig in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP)}
        try:
            for sig in handlers:
                signal.signal(sig, release)
            log("guard_start")
            while True:
                observed = find_server()
                if observed is None:
                    if current is not None:
                        signal_managed(current, signal.SIGSTOP)
                    current = None
                    previous_identity = None
                    idle_since = time.monotonic() if idle_since is None else idle_since
                    if time.monotonic() - idle_since > 1800:
                        return 0
                    time.sleep(1)
                    continue
                current = observed
                idle_since = None
                gpu, cpu, ram = gpu_temp(), cpu_temp(), ram_gib()
                action = action_for(gpu, cpu, ram, stopped=current["stopped"],
                                    starting=current["identity"] != previous_identity,
                                    blocked=STOP.exists() or STANDBY.exists())
                previous_identity = current["identity"]
                if action is not None:
                    if not signal_managed(current, action):
                        log("signal_failed", pid=current["pid"], signal=int(action))
                        return 1
                    log({signal.SIGSTOP: "pause", signal.SIGCONT: "resume", signal.SIGKILL: "abort"}[action],
                        pid=current["pid"], gpu=gpu, cpu=cpu, ram_gib=ram)
                time.sleep(1)
        finally:
            if current is not None:
                signal_managed(current, signal.SIGSTOP)
            for sig, handler in handlers.items():
                signal.signal(sig, handler)
            log("guard_exit", reason="no unguarded resume")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ensure", action="store_true")
    parser.add_argument("--status", action="store_true")
    args = parser.parse_args()
    if args.status:
        print(f"gpu={gpu_temp()}C cpu={cpu_temp()}C ram_free={ram_gib()}GiB server_pid={server_pid()}")
        return 0
    if args.ensure:
        return 0 if ensure_guard() else 1
    return run()


if __name__ == "__main__":
    raise SystemExit(main())
