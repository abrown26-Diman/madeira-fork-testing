# First engineering milestone — 2026-10-10

Milestone 0.3 continuation: see [the native-build execution report](MILESTONE_03_REPORT.md). The complete source-built wineserver archive now passes macOS/iOS build validation; the full app/IPA milestone is still in progress. The first milestone record below is retained.

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
| POSIX compiler-failure injection | SKIPPED on Windows; passed on Linux/macOS CI after fixture correction |
| All 63 existing host check scripts attempted | 3 full PASS, 2 partial with explicit skips, 58 blocked/nonzero because required tools/platform support unavailable |
| Existing config catalog test | Failed before path normalization; PASS after fix; generated Swift unchanged |
| Native readiness | FAIL as expected: nine missing inputs plus Windows rather than macOS |
| Native iOS compilation/link/package | NOT RUN |
| Signing/install/JIT/device/game/regression tests | NOT RUN |
| Frame/CPU/GPU/thermal performance | NOT MEASURED |

Sanitized per-test output and exact pin/hash manifests are in [evidence/](evidence/).

## GitHub Actions evidence

Engineering code: `ba9d950a5b872323db093755fcd8850b9d226ad2` on `engineering/instrumented-baseline`. `main` retains the unchanged upstream baseline. Later documentation-only commits record these results without claiming the runtime was rebuilt.

- [Instrumented baseline checks — PASS](https://github.com/abrown26-Diman/madeira-fork-testing/actions/runs/38031524162): all four jobs passed. All 15 diagnostics and three provenance tests passed on Windows/Linux/macOS. Compiler-failure injection plus its negative control passed on Linux/macOS; Windows explicitly skips the POSIX test. Recursive audit verified all 24 gitlinks. BCn decoder: 47 checks, zero failures. D3D12 tiling C harness and existing catalog/JIT/library source checks passed.
- [Native iOS readiness — FAIL](https://github.com/abrown26-Diman/madeira-fork-testing/actions/runs/38031367997): checkout, host dependency installation and environment recording succeeded; readiness failed on nine missing inputs. Compile/package skipped; build evidence artifact uploaded. This tested `cd66a35d0c9a00fbd367a3626f0dbe4235a7c893`; subsequent changes only touch diagnostics/test tooling, with the native recipe unchanged.
- [Full upstream host inventory — FAIL](https://github.com/abrown26-Diman/madeira-fork-testing/actions/runs/38031490803): all 63 host scripts attempted on each platform at `0c0eee1279bf904687a6bdcd321865863e10fc3e`. Linux: 56 full passes, 2 partial results, 5 nonzero. macOS: 54 passes, 9 nonzero. No timeout. See [HOST_TEST_FINDINGS.md](HOST_TEST_FINDINGS.md) for every failure, including two macOS behavioral assertions (BOM configuration agreement and installer path casing), platform-specific harness failures and missing Wine headers. These are not dismissed as successful tests.

The initial POSIX test fixture failed because it omitted a code-generation prerequisite, before reaching the intended compiler-failure assertion. The fixture was corrected and the succeeding run above validates both the guard and the negative control. Superseded duplicate runs were cancelled; cancellations are not test results.

## Next work

First reconstruct the wineserver base archive from pinned source on macOS, then bootstrap remaining inputs and prove a clean Debug build/standalone launch. The three strongest engine-wide investigations after that are ARM64EC import closure (wintypes first), Unity GC/thread suspension, and executable-memory store/exception handling. Each needs a minimal reproducer and unchanged-game regression checks.

For changed files, reasons, exact commands, report usage, limitations and reproduction protocol, see [BUILD_AND_TEST.md](BUILD_AND_TEST.md). All initial target games remain [NOT TESTED](COMPATIBILITY_MATRIX.md).
