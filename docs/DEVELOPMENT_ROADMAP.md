# Development roadmap

Milestone date: 2026-10-10. Foundation: Madeira `48f976429c189f8396e23d251d8a82f43c705922` with unchanged dependency gitlinks. A reproducible, instrumented baseline is the first goal; it has not yet been achieved end to end.

| Phase | Deliverable and exit evidence | Current state |
|---|---|---|
| 0 — source/build | Exact dependency manifest; fresh macOS build; complete logs; unsigned package; licensed inputs; independent rebuild and standalone installation | Milestone 0.3: source-built wineserver archive and validation pass; Wine headers/toolchain bootstrapped; full LLVM/native/app build in progress, no IPA yet |
| 1 — diagnostics/benchmarking | Exported launch/config/exception evidence; bounded logging modes; persisted pre-termination context; validated frame capture; repeatable device protocol | Offline JSON/Markdown analyzer and tests implemented; device capture and native integration untested |
| 2 — compatibility | Reproduced engine failure, minimal regression case, single fix, unchanged working-game checks | Ranked backlog only; no game compatibility changed |
| 3 — graphics | Shader/capability microtests and real-game captures demonstrating corrected rendering | Deferred |
| 4 — FEX/Wine/JIT/memory | One-variable hypotheses with identical-scene A/B measurements and sustained thermal checks | Deferred |
| 5 — profiles | Versioned per-game defaults with source/build/device provenance, user override and rollback | Extend existing Madeira settings later; no global speculative tuning |
| 6 — interface/release | Controller navigation, recovery flows, signing/install instructions, licensing/relink evidence and regression matrix | Deferred |

Immediate build work: source-only wineserver reconstruction passed in Milestone 0.3. Finish the pinned LLVM host/iOS, FreeType and remaining native/app compilation; record Xcode/SDK/tool versions and rebuild all shipped architecture farms. No cache is valid until an uncached build succeeds. Build caches must key on dependency SHAs, SDK/compiler versions, flags and patches.

Immediate diagnostics work after a build: compare unchanged standalone and LiveContainer launch logs, verify the build stamp, and validate crash/freeze/memory signatures with controlled test programs. Add an atomically persisted lifecycle record and bounded memory-pressure breadcrumbs at safe app callbacks; interrupted records must say "termination unknown", never automatically "jetsam". GPU timing and per-frame export require an identified, correctly scoped native measurement point.

Use [ISSUE_BACKLOG.md](ISSUE_BACKLOG.md) for actionable priorities. Every runtime change needs a minimal reproducer, baseline evidence and a regression gate covering sign-in, downloads, library/saves, controllers/touch, audio/video, Wine desktop and JIT. Preserve dependency forks and upstream mergeability. High-risk alternatives use separate branches. A failed or unmeasured optimization is reverted rather than advertised.
