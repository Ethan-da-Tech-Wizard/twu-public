# Distributed Multi-Agent Communication Bus (MAGI_0) — Architecture & Transport Specification

<!-- workspace-authority: current; technical architecture specification -->
> **Status:** Active Production Architecture  
> **Hosts:** Arch Linux (`example_host`), example_host Linux (`example_host`), macOS (`Ethans-example_host`)  
> **Routing Roster:** 16 Concurrent Leased Slots (`data/workspace_labels.json` -> `magi.active_seats`)

---

## 1. Executive Summary & The Interviewer's Question

> **"How Does the Multi-Agent Bus Actually Communicate?"**  
> *"You mention coordinating 16 worker slots across Arch Linux, example_host, and macOS nodes with a schema-validated JSONL message bus. What is the transport layer? Is it TCP/Unix domain sockets, SSH pipes, HTTP, or file-backed queues synced over Syncthing?"*

### Direct Answer
The **MAGI_0 Multi-Agent Bus** is an **offline-first, peer-to-peer, append-only, file-backed message bus replicated over TLS via Syncthing's Block Exchange Protocol (BEP v1), with reactive local filesystem wakeups (`inotify` on Linux, `kqueue`/`FSEvents` on macOS) and kernel-level file locking (`flock`)**.

It is **deliberately not** a centralized broker (Redis, RabbitMQ, Kafka) and **not** an open TCP/gRPC daemon. 

```
                                  PEER REPLICATION (TLS 1.3 / BEP v1)
  [Host 1: Arch Linux] <===============================================> [Host 2: macOS]
   ├── Agent 1 (Orchestrator)                                              └── Agent 4 (Local CLI)
   ├── Agent 2 (Ethan CLI)                                                       │
   └── Agent 5 (Worker)                                                          │
          │ (Append via flock)                                                  │
          ▼                                                                     ▼
   business/example_host/comms/agent5/outbox.jsonl                           business/example_host/comms/agent4/outbox.jsonl
          │                                                                     │
          └─────────────► Syncthing P2P Replicator ◄───────────────────────────┘
                                 │
                                 ▼
                     [Host 3: example_host Linux]
                      ├── Agent 3 (Ethan CLI)
                      └── Agent 11 (Worker)
```

---

## 2. The Physical & Network Transport Layer

| Layer | Implementation Mechanism | Purpose & Guarantees |
|---|---|---|
| **L7 Application Protocol** | Schema-1 JSONL Messages with RFC-3339 UTC timestamps and SHA-256 event digests. | Strict schema conformance, immutable event recording, zero binary pickle/serialization risks. |
| **L6 Serialization** | Strict UTF-8 JSON Lines, one self-contained event per line. | Stream-parseable, inspectable via standard Unix coreutils (`tail -f`, `jq`, `grep`). |
| **L5 Session / Concurrency** | Ephemeral `connection_id` tokens bound to owning OS process handles (PID + kernel start ticks). | Prevents PID-reuse race conditions; automatic dead-lease reaping without zombie locks. |
| **L4 Local IPC & Mutex** | OS-level atomic non-blocking advisory file locks (`fcntl.flock(LOCK_EX)`). | Multi-process writer safety on the same node; guarantees line-level atomicity on disk. |
| **L3 Cross-Node Transport** | **Syncthing Block Exchange Protocol (BEP v1) over TLS 1.3 with Perfect Forward Secrecy.** | Zero-cloud, peer-to-peer mesh replication; works across LAN, Wi-Fi, and ad-hoc networks without public IP addresses or port forwards. |
| **L2 Notification / Wakeup** | Linux `inotify` / macOS `kqueue` / Python watchdog file watchers. | Zero polling overhead; workers sleep in near-zero CPU state until filesystem write events trigger wakeups. |

---

## 3. Wire Format & Schema Validation

Every packet emitted on the bus is validated by `scripts/magi.py` against strict schema rules before touching disk.

### 3.1 Packet Structure
```json
{
  "event_id": "EVT-20261102T220500Z-A05-001",
  "connection_id": "7cba80a65e0a1c5eee186db544390e52",
  "from_seat": 5,
  "from_cli": "agy",
  "from_host": "example_host",
  "to_seat": 1,
  "type": "result",
  "reply_to": "EVT-20261102T215000Z-A01-042",
  "timestamp": "2026-11-02T22:05:00.123456Z",
  "authority_digest": "45ffe42785d502e3fe027409259fc1887b8690094b20f1d76b36ee479633e8b1",
  "payload": {
    "status": "passed",
    "summary": "Completed root-exec security audit with 0 findings",
    "artifacts": ["data/tool_trials/example_host/root_exec_audit.json"]
  }
}
```

### 3.2 Permitted Message Types
Agents are restricted to 8 semantic packet types. Unrecognized types are rejected at the gate:
- `assignment`: Orchestrator assigns a bounded stage contract to a worker seat.
- `claim`: Worker acknowledges and locks an assignment.
- `result`: Worker reports completed deliverable, metrics, and artifact paths.
- `review`: Independent reviewer verifies deliverable against acceptance tests.
- `question`: Worker requests an ambiguous architectural decision from Ethan.
- `proposal`: Worker proposes an engineering optimization or refactoring.
- `blocked`: Worker reports an environmental or dependency roadblock.
- `heartbeat`: Bounded liveness confirmation emitted during long operations.

### 3.3 Dead-Letter & Quarantine Discipline
If an outbox contains a malformed line (syntax error, truncated write from a crashed process, or unauthorized schema version):
- The transport layer isolates the record into quarantine.
- It does not block processing of subsequent valid messages.
- A diagnostic warning is emitted (`Transport diagnostic: N outbox record(s) quarantined`).

---

## 4. Concurrency Control & The PID Rollover Solution

In distributed systems running on multi-core workstations, seat leases can become orphaned if an agent crashes, exits abruptly, or is killed by an OOM event.

### 4.1 The Classic Unix PID Rollover Bug
On Linux systems under high process turnover, a dead agent's process ID (e.g. PID `3145`) may be re-allocated by the kernel to an unrelated process (such as a browser tab or compiler). A naive lease reaper that only checks `kill(pid, 0)` will observe that PID `3145` is alive and falsely conclude the old agent is still running.

### 4.2 The MAGI_0 Solution: Kernel Start Time Binding
When an agent claims a seat slot via `python3 scripts/magi.py join`, the bus captures two values:
1. The OS Process ID (`pid`).
2. The exact **kernel process start time in jiffies** read directly from `/proc/[pid]/stat` (field 22 on Linux) or `ps -p [pid] -o lstart=` on macOS.

```python
def cli_owner_start(pid: int) -> str:
    if sys.platform.startswith("linux"):
        # Field 22 (starttime) is immutable for the lifetime of that specific process instance
        fields = Path(f"/proc/{pid}/stat").read_text().rsplit(") ", 1)[1].split()
        return "linux-start-ticks:" + fields[19]
    # macOS fallback
    res = subprocess.run(["ps", "-p", str(pid), "-o", "lstart="], capture_output=True, text=True)
    return "ps-start:" + res.stdout.strip()
```

When any agent joins or runs `magi.py reap`, it inspects local seats:
- If the recorded PID is gone, the seat is reaped immediately.
- If the PID exists **but its current start ticks differ from the recorded lease**, the original process has provably died and the PID was recycled. The seat is reaped atomically without human intervention.
- Remote seats on other physical machines are never reaped via local PID inspection; they require cryptographic timeouts or explicit release.

---

## 5. Why Not Redis, gRPC, or NATS? (Architectural Decision Record)

| Decision Factor | Centralized Broker (Redis / NATS / RabbitMQ) | File-Backed Syncthing Mesh (MAGI_0) |
|---|---|---|
| **Single Point of Failure** | **High.** If the broker host crashes, sleeps, or disconnects, all agents across all machines fail simultaneously. | **None.** Fully decentralized peer-to-peer. Every node retains local queues and continues working offline. |
| **Network Partitions** | **Brittle.** Requires constant network reachability. Airplanes, mobile hotspots, and VPN reconnects break active connections. | **Resilient.** Syncthing synchronizes whenever peers reconnect. Messages queue durably on disk without loss. |
| **Security Surface** | **High.** Requires listening TCP ports on all hosts, TLS certificate authorities, authentication tokens, and firewall exceptions. | **Zero open listening ports.** Syncthing handles mutual TLS (mTLS) device authentication with pinned cryptographic device IDs. |
| **Memory Footprint** | **Non-zero.** Demands running resident daemons consuming 100–300 MB RAM per machine. | **Near-Zero.** Pure standard library Python + existing Syncthing sync engine already running on hosts. |
| **Auditability & Forensics** | **Ephemeral.** Requires specialized metric scrapers or log forwarders to inspect in-flight queues. | **Transparent.** Plain-text JSONL files on disk. Completely auditable via standard Unix tools (`git`, `grep`, `jq`, `diff`). |
| **Kill-Switch Enforcement** | Complex distributed RPC cancellation protocols. | Atomic filesystem check: creating `business/example_host/comms/STOP` immediately freezes all non-essential workers. |
