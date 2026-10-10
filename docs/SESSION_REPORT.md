# First engineering milestone — 2026-10-10

The first patch provides a pinned architecture/build audit, structured offline diagnostic reports, a repeatable compatibility/benchmark protocol and guarded CI. It preserves upstream runtime behavior and dependency revisions. **A reproducible native build and device baseline are still incomplete. No IPA or game-performance improvement is claimed.**

## Implemented

- Bounded JSON/Markdown analysis of exported logs, source hashes and line references, optional short excerpts, manual run metadata and explicit frame-CSV statistics. No automatic crash cause or compatibility promotion.
- Exact recursive dependency/input inspection and hashes for 301 bundled binaries.
- Build safety: fail ntdll compilation before stale objects can be archived; supply the required ARM64EC toolchain triple; normalize config catalog paths on Windows.
- Windows/Linux/macOS diagnostic CI plus a macOS iOS build/readiness workflow with logs and optional unsigned packaging after success.
- Required architecture, roadmap, compatibility, performance and build/test reports; ranked backlog and assessment of 56 open upstream issues.

## Actual local results

| Check | Result |
|---|---|
| New diagnostic behavior tests | 15 PASS |
| New Git provenance tests | 3 PASS |
| POSIX compiler-failure injection | SKIPPED on Windows; CI result pending |
| All 63 existing host check scripts attempted | 3 full PASS, 2 partial with explicit skips, 58 blocked/nonzero because required tools/platform support unavailable |
| Existing config catalog test | Failed before path normalization; PASS after fix; generated Swift unchanged |
| Native readiness | FAIL as expected: nine missing inputs plus Windows rather than macOS |
| Native iOS compilation/link/package | NOT RUN |
| Signing/install/JIT/device/game/regression tests | NOT RUN |
| Frame/CPU/GPU/thermal performance | NOT MEASURED |

Sanitized per-test output and exact pin/hash manifest are in [evidence/](evidence/). GitHub Actions outcomes will be added after the engineering branch is pushed; pending is not success.

## Next work

First reconstruct the wineserver base archive from pinned source on macOS, then bootstrap remaining inputs and prove a clean Debug build/standalone launch. The three strongest engine-wide investigations after that are ARM64EC import closure (wintypes first), Unity GC/thread suspension, and executable-memory store/exception handling. Each needs a minimal reproducer and unchanged-game regression checks.

For changed files, reasons, exact commands, report usage, limitations and reproduction protocol, see [BUILD_AND_TEST.md](BUILD_AND_TEST.md). All initial target games remain [NOT TESTED](COMPATIBILITY_MATRIX.md).
