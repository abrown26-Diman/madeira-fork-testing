# Full host-test inventory findings

Run: [38031490803](https://github.com/abrown26-Diman/madeira-fork-testing/actions/runs/38031490803), code `0c0eee1279bf904687a6bdcd321865863e10fc3e`. Both jobs attempted all 63 upstream scripts. Subsequent functional changes only complete a fixture under `tests/ci`, not the upstream host checks or their runtime subjects. No timeout occurred. The workflow correctly reports failure because some checks returned nonzero.

| Runner | Full PASS | Partial (exit zero with explicit skip) | Nonzero |
|---|---:|---:|---:|
| ubuntu-24.04 | 56 | 2 | 5 |
| macos-15, arm64 | 54 | 0 | 9 |

Exact per-test exit codes, durations and skips: [Linux inventory](evidence/upstream-linux-results.json), [macOS inventory](evidence/upstream-macos-results.json). Durable nonzero output: [Linux](evidence/upstream-linux-failures.md), [macOS](evidence/upstream-macos-failures.md). Full raw output is also in the downloaded Actions artifacts in local `work/actions/host-linux` and `work/actions/host-macos` (ignored by Git); remote artifact retention is 14 days. A host pass does not certify an iOS or guest/game execution path.

## Failures and next checks

| Check / platform | Observed failure | Assessment and next action |
|---|---|---|
| cfg-early-docs / macOS | C reads BOM+CRLF key, Swift returns `inproc-sync=unset` | **Behavioral discrepancy reproduced on host.** Current Swift parser does not explicitly remove a BOM, while C handles it. Isolate decoding versus parsing with direct string/byte fixtures on Darwin and Linux before changing app code; assess first-line settings and edit/round-trip behavior |
| dock-installers / macOS | `paths resolve case-insensitively` assertion fails | **Behavioral assertion reproduced on host.** Resolver can take an exact-path existence shortcut on a case-insensitive filesystem; returned URL spelling may differ while referring to the same file. Test file identity/openability and containment on both filesystem types before deciding whether this is a runtime defect or an overly strict fixture |
| d3d9-splitlock / macOS | `-latomic` library unavailable | Host harness assumes Linux linking; use platform-appropriate atomic support while retaining the actual concurrency checks |
| dock-components / macOS | Redefined `zlib` module | Harness-provided module map collides with Apple SDK map; use the native SDK module on Darwin |
| lazy-windows / macOS | Harness `mach_port_t` typedef conflicts with system unsigned type | Platform-specific harness shim issue; separate mock names/native types without weakening ownership/alias assertions |
| steam-library / Linux | Unresolved `lzma_alone_decoder`, `lzma_code`, `lzma_end` at final Swift link | Link failure; cause is not yet proven. Test Swift driver/link order and actual liblzma selection. Do not mark Steam download behavior tested until compiled fixture runs |
| steam-library / macOS | Host shim module collisions / hardcoded `/usr/include/zlib.h` absent | Harness documents Linux dependencies; add a Darwin harness path or explicitly require Linux. Do not change app decoder code to silence a harness failure |
| swap-coverage / macOS | `linux/falloc.h` unavailable | Linux-only test model dependency; run on Linux (passed there), port only with equivalent semantics |
| wg-parser / macOS | ASan reports leak detection unsupported | Harness enables unsupported sanitizer option. Retain address checks and distinguish unavailable leak instrumentation from a passing leak test |
| jit-network / Linux | Swift module `Darwin` absent | Darwin-specific production probe; macOS check passed |
| steam-cloud / Linux | Swift module `CryptoKit` absent | Apple framework dependency; macOS check passed. Does not validate device save/cloud flows |
| wine-mono / Linux | `xcrun` absent | macOS tool dependency; macOS check passed. Does not validate in-game Mono/GC |
| wma-decoder / both | Missing configured `wine/build-macos/include/config.h` | Same generated-header build prerequisite as native readiness; bootstrap pinned Wine, then rerun |

Linux partials: dock-installers could not reach `cmd.exe` (batch flow only checked textually); wg-parser had no real MP3 input. macOS dock-installers also reports that batch skip, but its nonzero assertion takes precedence over a partial classification. Neither missing portion is a pass.

These results establish additional baseline work, not regressions caused by this patch: app/runtime sources and upstream test bodies were unchanged, apart from the independently tested config-catalog path-normalization tool. No safety check was removed, unsupported test relabeled green, or speculative engine fix applied.
