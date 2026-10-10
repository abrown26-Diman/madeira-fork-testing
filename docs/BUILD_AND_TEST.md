# Build and test — Milestone 0.3 (in progress)

No successful application build or IPA is claimed yet. The active branch is `engineering/native-ios-build`, based on `497f04430685bec284df536beff1a496cb7ff706`. Historical Milestone 0.2 findings below are retained as evidence; this section supersedes their build recipe.

## Native workflow

`.github/workflows/ios-baseline.yml` runs on the GitHub-hosted `xcode-27` arm64 image and explicitly selects Xcode 27.0. The existing StikJIT interface was produced with Swift 6.4; a real Swift import check now precedes the dependency build. Runner images and Homebrew packages remain moving inputs, so this is not yet a bit-reproducibility claim. Actions are pinned, submodules are recursively checked out at recorded gitlinks, credentials are not persisted, and no object/archive cache is restored. Host/SDK/compiler/package-manager versions are uploaded on each attempt.

From a **fresh** macOS checkout with the workflow's host tools installed:

```sh
bash build/ci/bootstrap-wine.sh
bash build/wineserver/build.sh
bash build/ci/bootstrap-libraries.sh
xcodebuild -downloadComponent MetalToolchain
python3 tools/ci/audit_inputs.py --require-native --output work/ci/native-inputs.json
PACKAGE_IPA=1 bash build/ci/build-ios.sh
```

Bootstrap refuses existing Wine/toolchain source destinations instead of overlaying a stale build. On Windows, push the dedicated branch to the fork to execute these commands on Actions. No local Mac or Apple signing credentials are needed for the unsigned build. `build-ios.sh` requires the bootstraps and reconstructed wineserver to have succeeded. It runs the original dependency scripts, Wine PE builds, native Wine shims, FEX, DXMT, native D3D12, pairing, Dock tests and WoW64 builds before `xcodebuild` in Debug (upstream's tested runtime configuration). The initial DXMT combined archive is explicitly created using the documented libtool merge.

Wineserver is built from 48 known source objects, with no seed archive: see [Wineserver construction](WINESERVER_BUILD.md). The previously listed `wine/build-macos/include/wine/version.h` dependency was an audit error; it has no consumer or generation rule in the pinned tree. `config.h` and actual widl headers are generated from Wine configure plus `make include/all`.

## New dependency provenance

| Input | Exact revision / source | SHA-256 of downloaded bytes |
|---|---|---|
| LLVM-MinGW | [20260421 universal macOS toolchain](https://github.com/mstorsjo/llvm-mingw/releases/download/20260421/llvm-mingw-20260421-ucrt-macos-universal.tar.xz) | `bd85a3975723815cef28dbbd2ca2cb0c926f6b348a12a0453f39f7af273cb3f7` |
| LLVM 15.0.7 | [8dfdcc7b7bf66834a761bd8de445840ef68e4d1a source archive](https://codeload.github.com/llvm/llvm-project/tar.gz/8dfdcc7b7bf66834a761bd8de445840ef68e4d1a) | `b7f15ee379144b0c26a64ff9a1f27d0ea341a0db0c91b71c66bbfa8b310788ac` |
| FreeType 2.13.3 | [42608f77f20749dd6ddc9e0536788eaad70ea4b5 source archive](https://codeload.github.com/freetype/freetype/tar.gz/42608f77f20749dd6ddc9e0536788eaad70ea4b5) | `68ce87bb59ea209eb7350f41a94a27519ce16b37011b475a1e62d4abee154b66` |

The toolchain hash is inherited from upstream Madeira and was verified by Actions run 38032706137. LLVM/FreeType hashes were measured from the exact official GitHub source archives after resolving their release tags to full commits, then pinned in the bootstrap. They are download-integrity pins, not claims of an upstream signature. LLVM receives only the documented `Darwin|iOS` dead-strip CMake correction; context must match exactly. Host llvm-tblgen generates the iOS headers; LLVMBitWriter and LLVMPasses build the same transitive component set requested by DXMT. Host Homebrew LLVM is used for tools such as Mach-O symbol rewriting, not linked as the iOS LLVM runtime.

GMP/Nettle/GnuTLS and FFmpeg retain the tracked source tarballs and SHA256SUMS; the orchestration verifies the GnuTLS stack before extraction. Cargo uses its committed lockfile. The tracked Apple converter and StikJIT framework remain binary inputs with the existing notices and provenance limitations; neither is replaced or downloaded from an unrecorded source. CI does not fetch the Apple installer or Microsoft runtime DLLs. The ARM64EC/aarch64 farms still contain tracked modules beyond the documented rebuild subset; a complete clean reconstruction of every existing PE is a separate remaining provenance task, not something to claim from an app link.

## Validation and packaging gates

The wineserver build records exact members, architectures, global/undefined symbols and hash before atomically staging its output. A compiler or objcopy failure leaves the previous app archive intact. LLVM archives are checked for arm64. The final Xcode link must resolve native symbols; its result bundle and link maps are retained. Static archive undefined-symbol listings are evidence, not link success.

After Xcode succeeds, `tools/ci/verify_app.py` checks native executables and arm64 architecture, JIT helper/framework, Wine/FEX/graphics DLL paths, NLS, certificates, shortcut, assets, notices and byte-for-byte copying of staged PE/NLS/legal resources. Only then can `Payload/Madeira.app` be packaged. The artifact includes a file hash manifest, native input manifest, dependency download ledger, original entitlement reference and IPA SHA-256. An unsigned IPA may contain upstream ad-hoc signatures; none authorizes installation on the user's device.

## Signing and first device test

1. Download the successful unsigned artifact and verify its SHA-256. If no successful artifact exists, do not treat build-evidence logs as a package.
2. Use the user's existing authorized signing/sideloading tool, such as SideStore, with a valid device provisioning profile. Keep signing credentials, certificates, profiles and pairing files out of Git and Actions artifacts.
3. Sign the app, `PlugIns/MadeiraJITHelper.appex`, `Frameworks/StikJIT.framework`, and `d3d12/libmetalirconverter.dylib` consistently. Keep the helper's bundle identifier related to the main app identifier, and verify nested components survive the sideloader.
4. Compare the effective signed entitlements with the original reference: `get-task-allow`, `com.apple.security.cs.allow-jit`, and `com.apple.developer.kernel.increased-memory-limit`. Provisioning capabilities vary; an entitlement appearing in the source plist does not guarantee the signer or device will grant it. Record the actual result without changing JIT requirements.
5. Install standalone first, enable Developer Mode and follow [the existing JIT setup](JIT.md). Confirm JIT initialization, Wine desktop, input/audio and a known-working game with disposable test data before LiveContainer comparisons. Installing or launching alone does not establish game compatibility.

## Milestone 0.2 historical record

# Build and test record â€” 2026-10-10

## Status

The audited source and portable diagnostics are available. **A clean native iOS build has not succeeded in this session and no IPA has been produced.** The upstream build documentation contains unresolved bootstrap steps. The new native workflow fails explicitly at readiness until those are supplied; it must not be reported as a working reproducible build.

Source baseline: `48f976429c189f8396e23d251d8a82f43c705922`; dependency pins and binary hashes: [source-inputs.json](evidence/source-inputs.json). Remote engineering repository: [abrown26-Diman/madeira-fork-testing](https://github.com/abrown26-Diman/madeira-fork-testing). Final run results and URLs are recorded in [SESSION_REPORT.md](SESSION_REPORT.md).

## Requirements and blockers

Start with upstream [BUILDING.md](BUILDING.md); its historical "verified this session" statements refer to the upstream author, not this audit. Native compilation requires macOS, Xcode with the iPhoneOS SDK, clang/Metal tools, CMake, Ninja, Meson, bison 3, pkg-config, autotools, LLVM utilities, Rust/Cargo/rustup and `aarch64-apple-ios`. Windows supports source analysis and Python diagnostics. Git's bundled MSYS helper failed under the restricted Windows process, so this checkout initialized submodules using native Git commands at the exact recorded revisions. CI uses standard recursive checkout.

| Input | Current evidence / required action |
|---|---|
| LLVM-MinGW `20260421` macOS universal | Official recipe pins SHA-256 `bd85a3975723815cef28dbbd2ca2cb0c926f6b348a12a0453f39f7af273cb3f7`; absent locally; verify download/extraction before building |
| LLVM host tools and iOS libraries | Recipe refers to LLVM 15.0.7 source `8dfdcc7b7`; resolve full commit, pin host tablegen, document AddLLVM iOS change and reproduce iOS static libraries. Homebrew LLVM is not a replacement for the iOS build |
| Wine generated headers | `wine/build-macos/include/config.h`, version header and ARM64EC widl outputs are required but absent; bootstrap from pinned Wine before native shims |
| FreeType 2.13.3 | `research/freetype` is required by the font build but not initialized by the top-level recipe; pin `VER-2-13-3` to a full commit and verify build |
| **wineserver base archive** | `build/wineserver/build.sh` updates selected objects in an existing `libwineserver.a`; no complete seed recipe is provided. Reconstruct full source/object membership and renames. Never use an empty or unexplained binary seed |
| DXMT combined archive | Original script refreshes/stages only when destination archive already exists. New orchestration explicitly performs the initial libtool merge documented in `build/dxmt-ios/README.md`; native execution remains untested |
| GMP/Nettle/GnuTLS/FFmpeg | Tracked source tarballs and hashes; retain LGPL configuration/notices and verify macOS scripts |
| In-app pairing and StikJIT | Cargo.lock is present; tracked StikJIT XCFramework provenance/source rebuild still needs independent verification |
| Microsoft VC runtimes | Absent and not redistributed by CI. Empty folder satisfies the Xcode folder reference; games needing a runtime still require a lawful runtime installation. Do not copy arbitrary System32 DLLs into a published package |
| Apple Metal Shader Converter | Existing tracked iOS library and agreement preserved; `deps.sh` records SHA-256 `073f903be98e973ff38f4d79f2c48d61ef938754a77b1caedda79c9f05a068c2`. No Apple installer, SDK or signing material is uploaded. Review existing agreement/distribution scope before packaging |
| Wine Mono | Optional WineHQ runtime, pinned by upstream scripts. Existing four-byte mscorlib workaround is retained, not validated here; do not confuse IL2CPP failures with Wine Mono |

The tracked PE farms still lack full clean rebuild provenance. The wrapper rebuilds documented components, the default extra Wine modules and i386/FEX WoW64 paths; it does not prove every existing ARM64EC/aarch64 builtin was rebuilt. Completion requires a full module inventory, reproducible build commands, relink evidence and installation tests. Runner labels and Homebrew packages drift; recorded versions aid diagnosis but do not make output bit-reproducible. Pin and validate the entire toolchain after the first clean success.

## CI and packaging

`.github/workflows/baseline.yml` runs diagnostics/provenance tests on Windows, Linux and macOS; a recursive Linux checkout records all pins and runs selected existing source/C graphics checks. Actions are pinned to verified commit SHAs, permissions are read-only, checkout credentials are not persisted, and logs upload even after failure. No game files or credentials are required.

`.github/workflows/host-baseline.yml` attempts all 63 existing host scripts on Linux and macOS using `tools/ci/run_host_checks.py`. Each check has a 180-second limit; the runner preserves every log, nonzero result, timeout and explicit skip, and updates the JSON inventory after each check. Unsupported tests still count as incomplete, never passes. The inventory job returns failure when any check returns nonzero. It is a baseline investigation, not a relaxed pass gate.

`.github/workflows/ios-baseline.yml` runs on `macos-15`, records Xcode/SDK/tools, installs host dependencies, then enforces `audit_inputs.py --require-native`. The engineering branch push runs readiness with packaging off. After this workflow is on the default branch, it can also be manually dispatched against a chosen ref. The build entry point is `build/ci/build-ios.sh`. It uses the official scripts, explicit Debug configuration and generic iOS destination, disables automatic signing and writes an exact MadeiraBuild stamp consumed by existing launch diagnostics. Original JIT entitlements are preserved as an artifact for later signing.

Packaging is opt-in and happens only after successful compilation and distribution-rights review; it creates an unsigned `Payload/Madeira.app` IPA plus SHA-256, input manifest and entitlement reference. It is **not installable until correctly signed**. No provisioning profile, Apple account, certificate or pairing file is committed. A manually signed standalone package must pass JIT, saves and known-working-game checks before comparing LiveContainer. Native compiler/linker errors, result bundles and logs are retained when available. No archive caching hides missing inputs.

The executed macOS readiness run used an arm64 runner, macOS 15.7.9, Xcode 16.4 and iPhoneOS SDK 18.5 (recorded in [ci-macos-host.txt](evidence/ci-macos-host.txt)). This is not an iOS 27 device test or an SDK 27 compilation. Selecting/pinning a suitable Xcode toolchain remains part of completing the native build. Host dependency installation succeeded; readiness then failed on the nine documented missing inputs, before the compile/package step.

## Local commands

From the repository, with Python 3.10+ for the new tools:

```text
python -m unittest discover -s tests/diagnostics -v
python -m unittest discover -s tests/ci -v
python tools/ci/audit_inputs.py --output work/source-inputs.json
python tools/ci/audit_inputs.py --require-native --output work/native-inputs.json
python tests/host/check-config-catalog.py
python tests/host/check-jit-method.py
python tests/host/check-library-sections.py
```

Use `--allow-missing-linux-tests` only for a Windows audit that intentionally omits the three optional FEX Linux binary-test repositories; CI requires them. A normal source audit may exit zero while listing missing native inputs: that means revision inspection completed, not a build. `--require-native` treats those missing inputs and a non-macOS host as errors.

On POSIX hosts also run `bash tests/dxmt/build-bcn-host-test.sh` and existing `tests/host/check-*.py` as their documented dependencies permit. Some tests require clang/Swift, macOS APIs, a configured Wine tree, FFmpeg, Cargo or Python 3.14 (`compression`). Inspect SKIP lines even on exit zero. Native graphics tests require iOS/Wine/Metal and are not replaced by Python source assertions.

## Diagnostic reproduction

1. Copy a stopped per-game log from Madeira's Documents/logs, retaining the original. For a crash/kill, also save the matching iOS Analytics `.ips` or JetsamEvent and build symbols; for hangs, obtain a time-correlated sysdiagnose when possible. Do not assume an absent final line identifies the termination cause.
2. Copy `docs/diagnostics/run-template.json` to a run-specific file and fill known fields. Leave unknowns null. Settings are string-to-string entries. No automatic device collection is implied.
3. Generate a new report directory:

```text
python tools/diagnostics/report.py exported-log.txt --metadata run.json --output work/run-001
```

Default output is bounded pattern/line/hash evidence without raw log excerpts. Optional `--include-excerpts` includes short, best-effort-redacted excerpts; review them and manual metadata for personal data before sharing. No network upload occurs. Unknown log formats and lines over 64 KiB are not diagnosed. Pattern counts count matching lines, not independent faults.

If actual individual frame intervals were captured, add `--frames frames.csv --frames-source "capture mechanism and clock"`. The CSV must contain exactly `frame_time_ms`; no FPS is inferred otherwise. See [PERFORMANCE_BASELINE.md](PERFORMANCE_BASELINE.md). Synthetic fixtures test arithmetic only.

The tool streams logs, keeps at most three examples per pattern, 40 context entries and 20 guest exit events, refuses to overwrite output and never changes the source. It cannot intercept OS termination or recover unwritten data. Existing native log capture, rotation and diagnostic configuration remain unchanged.

## Implementation inventory and validation

| Files | Reason | Validation / limit |
|---|---|---|
| `tools/diagnostics/report.py`, `tests/diagnostics/test_report.py`, metadata template | Structured low-overhead offline evidence and optional explicit frame statistics | 15 behavioral tests; no device crash capture claim |
| `tools/ci/audit_inputs.py`, `tests/ci/test_audit_inputs.py` | Exact nested pins, dirty states, bundled hashes and clear missing-input failure | Three real miniature-repository tests; input presence is not source provenance |
| `build/ntdll-unix/build.sh`, `tests/ci/test_build_safety.py` | Stop failed compilation from archiving/staging stale objects | POSIX injected compiler failure plus negative control removing guard; Windows skips this test |
| `build/fex-arm64ec/build.sh` | Supply toolchain's required `MINGW_TRIPLE` on first configure | Source contract verified; full FEX configure/build pending native inputs |
| `build/tools/gen-config-catalog.py` | Normalize source paths so Windows generates identical catalog and ordering | Existing config catalog test failed before change, passes afterward; generated Swift unchanged |
| `build/ci/build-ios.sh`, three workflows, `tools/ci/run_host_checks.py` | Auditable build/readiness, Debug stamp, complete host-test inventory, error/artifact retention and unsigned packaging | CI results in session report; full native path unvalidated; build entry point passed Bash syntax parsing |
| `.gitignore`, docs/evidence and required reports | Keep generated work/cache out of source; preserve audit/testing evidence | Diff/JSON checks; no existing license or runtime file removed |

Windows result: 15 diagnostics and three provenance unit tests pass; one POSIX build-safety test is skipped. All 63 existing `tests/host/check-*.py` were attempted: after the catalog fix, three complete source checks pass, two return success while skipping required portions, and 58 cannot complete because this host lacks required tools/platform support. Those 58 nonzero executions are not passes and do not establish runtime regressions. Details and sanitized logs are under `docs/evidence/`. Native readiness fails as intended. No native compilation, linking, IPA signing, installation or game test ran locally.

Remote validation at `ba9d950a5b872323db093755fcd8850b9d226ad2`: diagnostics 15/15 and provenance 3/3 passed on all three runner platforms; the additional compiler-failure/negative-control test passed on Linux/macOS and was explicitly skipped on Windows. All four baseline jobs passed. Recursive source audit checked all 24 gitlinks. The BCn decoder ran 47 checks with zero failures; D3D12 tiled-resource host harness and catalog/JIT/library source checks passed. This is host validation, not a rendered iOS graphics or game result. The first fixture run failed because its mock tree lacked a generator prerequisite; the repaired fixture reaches both guarded and unguarded archive paths and passed remotely. Exact runs are in [SESSION_REPORT.md](SESSION_REPORT.md).

The separate full upstream inventory finished with Linux 56 PASS / 2 partial / 5 nonzero and macOS 54 PASS / 9 nonzero, with no timeouts. Both jobs report failure. [HOST_TEST_FINDINGS.md](HOST_TEST_FINDINGS.md) distinguishes actual behavioral assertion failures from platform/harness and prerequisite failures, with durable logs. No upstream test was relaxed to make CI green.

Recommended next engineering task: remove the wineserver seed dependency with an explicit complete source build on macOS, then validate one unchanged standalone game launch before touching engine behavior.
