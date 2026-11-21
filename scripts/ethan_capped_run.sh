#!/usr/bin/env bash
# Run any command inside a hard memory cap AND an isolated example_host so a runaway or a misbehaving test cannot
# freeze the laptop or signal Ethan's desktop session.
#   scripts/ethan_capped_run.sh python3 -B -m unittest -q scripts.test_something
# Cap defaults to 3G (set ETHAN_CAP=6G for a known-large job). CPU is capped at 400% (4 of 16 threads, ETHAN_CPU=800% to raise)
# so test/eval runs cannot heat-soak the laptop (CPU hit 100C on 2026-11-01 from many parallel runs). No root needed.
# The run gets: a hard MemoryMax, no swap use, a high OOM score (the kernel kills it first), an opt-in
# to systemd-oomd (effective once scripts/ethan_memory_safety_setup.sh has been run), and, by default, a user+pid+net+mount
# namespace: the command is PID 1 of its own process tree, so kill(-1)/killpg(1) (a mocked pid became 1 and ended the
# whole desktop session three times on 2026-10-31) cannot reach real processes; the user systemd bus, Wayland socket
# and network are unreachable. Files in the repo stay writable.
# ETHAN_HOST=1 runs on the host without the namespace (needed for the local model server, GPU or desktop); it is
# announced on stderr. If namespaces are unavailable the command is NOT run unless ETHAN_HOST=1 is set.
set -euo pipefail
[ "$#" -ge 1 ] || { echo "usage: $0 <command...>" >&2; exit 2; }
if [ "$(uname -s)" = "Darwin" ]; then
  exec python3 "$(cd "$(dirname "$0")" && pwd)/ethan_mac_capped_run.py" "$@"
fi
# NOT exec: inside the pid namespace this shell is PID 1, and PID 1 must reap orphaned grandchildren. With exec the command became
# PID 1 and every orphan it left (git helpers, sleeps) stayed <defunct> until the run ended (18,561 zombies on 2026-11-01 made every
# ps/pgrep poll cost 0.3-0.7 s of CPU and heated the laptop). Bash as PID 1 reaps them; exit status is preserved.
inner='echo 500 > /proc/self/oom_score_adj 2>/dev/null || true; "$@"; exit $?'
if [ "${ETHAN_HOST:-0}" = "1" ]; then
  echo "ethan_capped_run: ETHAN_HOST=1, running on the host without the namespace example_host" >&2
  prefix=()
else
  # Loopback only: a fresh --net namespace has `lo` down, so local test servers (127.0.0.1) could not bind/connect. External
  # network stays unreachable (no other interface exists). Best effort; harmless if `ip` is absent.
  inner='ip link set lo up 2>/dev/null || true; '"$inner"
  unshare --user --map-root-user --pid --fork --net --mount-proc true 2>/dev/null || {
    echo "ethan_capped_run: namespace example_host unavailable; refusing. Set ETHAN_HOST=1 to run on the host." >&2; exit 3; }
  home="$(mktemp -d /tmp/ethan-example_host-home.XXXXXX)"
  prefix=(unshare --user --map-root-user --pid --fork --net --mount-proc
          env -i PATH=/usr/bin:/bin ETHAN_CAPPED_INNER=1 "HOME=$home" "LANG=${LANG:-C.UTF-8}" ${PYTHONPATH:+"PYTHONPATH=$PYTHONPATH"}
          ${TWU_DASHBOARD_RELEASE:+"TWU_DASHBOARD_RELEASE=$TWU_DASHBOARD_RELEASE"}
          ${TWU_DASHBOARD_WORKSPACE:+"TWU_DASHBOARD_WORKSPACE=$TWU_DASHBOARD_WORKSPACE"}
          ${TWU_ROOT:+"TWU_ROOT=$TWU_ROOT"})
fi
# Thermal gate (2026-11-05): the GPU sits at 87-90 C even while nearly idle because CPU-heavy jobs heat the shared chassis, and the
# owner removed routine-temperature stops on 2026-11-19. Only wait near the measured hardware critical limit: below
# ETHAN_THERMAL_GATE (default 99 C, GPU shutdown is 101 C). No wait at routine 88-98 C. Fail-open: no nvidia-smi,
# unreadable temperature or timeout means run anyway; the model guard independently enforces its critical limit.
# ETHAN_THERMAL_WAIT=0 disables it.
if [ "${ETHAN_THERMAL_WAIT:-120}" != "0" ] && command -v nvidia-smi >/dev/null 2>&1; then
  twaited=0
  while :; do
    gt="$(timeout 3 nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits 2>/dev/null | head -n1 | tr -dc '0-9')"
    { [ -z "$gt" ] || [ "$gt" -lt "${ETHAN_THERMAL_GATE:-99}" ]; } && break
    [ "$twaited" -ge "${ETHAN_THERMAL_WAIT:-120}" ] && { echo "ethan_capped_run: GPU still ${gt} C after ${twaited}s, running anyway" >&2; break; }
    [ "$twaited" -eq 0 ] && echo "ethan_capped_run: GPU ${gt} C >= ${ETHAN_THERMAL_GATE:-99}, waiting for it to cool (ETHAN_THERMAL_WAIT=0 skips)" >&2
    sleep 5; twaited=$((twaited + 5))
  done
fi
# Concurrency limit: defaults to 0 (unthrottled hardware as directed by Ethan).
# Never lock slots when already inside an existing capped container (ETHAN_CAPPED_INNER=1).
if [ "${ETHAN_SLOTS:-0}" != "0" ] && [ "${ETHAN_CAPPED_INNER:-0}" != "1" ]; then
  slot_dir="${ETHAN_SLOT_DIR:-${XDG_RUNTIME_DIR:-/tmp}/ethan-capped-slots}"
  mkdir -p "$slot_dir" 2>/dev/null || true
  if [ ! -d "$slot_dir" ] || [ ! -w "$slot_dir" ]; then
    slot_dir="/tmp/ethan-capped-slots-${UID:-$(id -u)}"
    mkdir -p "$slot_dir" 2>/dev/null || true
  fi
  waited=0; got=0
  while :; do
    for i in $(seq 1 "${ETHAN_SLOTS:-2}"); do
      if { exec {slotfd}>"$slot_dir/slot$i"; } 2>/dev/null; then
        if flock -n "$slotfd" 2>/dev/null; then got=1; break 2; else exec {slotfd}>&-; fi
      fi
    done
    [ "$waited" -ge "${ETHAN_SLOT_WAIT:-1800}" ] && break
    [ "$waited" -eq 0 ] && echo "ethan_capped_run: all ${ETHAN_SLOTS:-2} run slots busy, waiting (limits heat); ETHAN_SLOTS=0 skips" >&2
    sleep 5; waited=$((waited + 5))
  done
  [ "$got" = "1" ] || echo "ethan_capped_run: waited ${waited}s for a slot, running anyway" >&2
fi
if [ -S "${XDG_RUNTIME_DIR:-/run/user/${UID:-$(id -u)}}/bus" ]; then
  exec systemd-run --user --scope --quiet --collect \
    -p "MemoryMax=${ETHAN_CAP:-3G}" -p MemorySwapMax=0 -p "CPUQuota=${ETHAN_CPU:-400%}" \
    -p ManagedOOMMemoryPressure=kill -p ManagedOOMMemoryPressureLimit=40% \
    -- "${prefix[@]}" bash -c "$inner" _ "$@"
else
  exec "${prefix[@]}" bash -c "$inner" _ "$@"
fi
