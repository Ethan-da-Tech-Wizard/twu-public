# DevSecOps CI/CD & Automated Container Architecture

<!-- managed-pipeline-specification: current -->

This document describes the automated Continuous Integration, Continuous Delivery (CI/CD), containerization, and DevSecOps security architecture implemented for the TWU LLC developer platform.

---

## 1. Architectural Overview

The DevSecOps pipeline automates quality gates, static security analysis, container image builds, vulnerability scanning, and multi-version test execution on every commit and pull request.

```
       [ Git Push / PR ]
               |
    +----------+----------+
    |                     |
    v                     v
[ Job 1: SAST & Lint ]   [ Job 2: YARA Vetting ]
 - ShellCheck (Bash)      - twu_yara_vet.py
 - python3 compileall     - YARA engine compile
 - Bandit (Python SAST)   - Test suites
    |                     |
    +----------+----------+
               |
               v
  [ Job 3: Docker Build & DevSecOps ]
   - Multi-stage Dockerfile
   - Non-root user (UID 10001)
   - SPDX SBOM Generation
   - Aqua Security Trivy Scan
   - Container health check
               |
               v
  [ Job 4: Multi-Runtime Matrix ]
   - Python 3.10, 3.11, 3.12, 3.13
   - Core certification suites
```

---

## 2. Pipeline Stages

### Stage 1: Static Application Security Testing (SAST) & Linting
- **ShellCheck**: Statically analyzes all workspace shell scripts (`scripts/*.sh`) to eliminate quoting bugs, subshell vulnerabilities, and POSIX incompatibilities.
- **Bytecode Compilation**: Validates syntax across all Python scripts using `python3 -m compileall -q scripts/`.
- **Bandit SAST**: Scans Python source code for security anti-patterns, unsafe deserialization, insecure subprocess usage, and hardcoded credentials.

### Stage 2: YARA Threat Pattern & Rule Vetting Gate
- **Rule Verification**: Runs `scripts/twu_yara_vet.py verify` to ensure all 5,300+ YARA detection rules compile without syntax errors.
- **Scanner Certification**: Executes unit tests for `twu_yara.py`, `twu_scan.py`, `twu_scan_event.py`, and `twu_yara_vet.py`.

### Stage 3: Containerization, SBOM & Vulnerability Scanning
- **Multi-Stage Dockerfile**: Builds on `python:3.12-slim-bookworm` with layer caching, stripping build tools and unnecessary packages from the final runtime image.
- **Least Privilege Enforcement**: Runs strictly under a non-root system account (`appuser:appgroup`, UID/GID 10001).
- **Software Bill of Materials (SBOM)**: Automatically generates an SPDX-JSON formatted SBOM via Trivy and archives it as a pipeline artifact.
- **Trivy Vulnerability Scan**: Scans OS packages and application dependencies for known CVEs (`severity: CRITICAL,HIGH`), gating releases on unmitigated security risks.
- **Container Health Check**: Runs an in-container self-test using `/app/scripts/twu_scan.py status`.

### Stage 4: Multi-Version Test Matrix
- Tests core certification suites in parallel across multiple Python minor versions (Python 3.10, 3.11, 3.12, 3.13).
- Validates system wiring (`test_wiring_check.py`), tool registry (`test_tool_registry.py`), workspace certification (`test_ethan_certify.py`), scanner engines, and remote syslog receivers.

---

## 3. Local Parity & Consistency

The remote GitHub Actions workflow mirrors the local verification commands executed on developer workstations:

| CI/CD Pipeline Step | Local Command Equivalent |
|---|---|
| Shell script linting | `shellcheck scripts/*.sh` |
| Python compile check | `python3 -m compileall -q scripts/` |
| YARA rule vetting | `python3 scripts/twu_yara_vet.py verify` |
| Security scanner test | `python3 scripts/twu_scan.py status` |
| Repository quality gate | `python3 scripts/check_all.py --no-build` |
| Architecture wiring gate | `python3 scripts/wiring_check.py --check` |
| Resume verification | `python3 scripts/resume.py check` |

---

## 4. STAR Interview Talking Points for DevOps / DevSecOps

- **Situation**: Needed a production-grade CI/CD and containerization pipeline to shift security left and enforce automated compliance across a distributed 3-node environment.
- **Task**: Design and implement a GitHub Actions pipeline with zero cloud spend, automated container builds, software supply chain auditing, and vulnerability gating.
- **Action**: Created a hardened multi-stage Dockerfile running as a dedicated non-root user (UID 10001). Implemented ShellCheck linting, Bandit SAST analysis, YARA threat signature compilation verification, Trivy container vulnerability scanning, and automated SPDX SBOM generation.
- **Result**: Established an end-to-end automated DevSecOps pipeline that validates container security, blocks high/critical CVEs before deployment, produces audit-ready SBOMs, and tests across Python 3.10-3.13 matrices.
