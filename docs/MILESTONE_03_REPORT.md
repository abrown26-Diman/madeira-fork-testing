# Milestone 0.3 execution report (in progress)

Objective: native iOS compilation and a validated unsigned IPA. **Not complete.** No native application link, package, installation, gameplay or performance result is claimed yet.

Baseline: `497f04430685bec284df536beff1a496cb7ff706`. Dedicated branch: `engineering/native-ios-build`. All FEX, Wine, DXMT and nested gitlinks remain unchanged. Steam, saves, game configuration, UI and JIT runtime code are untouched.

## Executed Actions attempts

| Commit | Run | Actual result |
|---|---|---|
| d928bc4 | [38032706137](https://github.com/abrown26-Diman/madeira-fork-testing/actions/runs/38032706137) | Recursive checkout, host tools, Xcode selection and toolchain hash verification passed. Wine host configure failed with `ld: library 'System' not found`. Fixed by explicit macOS sysroot. |
| 1c275bd | [38032991109](https://github.com/abrown26-Diman/madeira-fork-testing/actions/runs/38032991109) | Both Wine configurations completed. `async.c` compiled to iOS Mach-O and objcopy completed. Archive validation stopped because the lipo argument order was wrong; corrected before retry. The then-used `make include` was also found to be a no-op and replaced with Wine's actual `include/all` target. |
| e04ea3a | [38033345354](https://github.com/abrown26-Diman/madeira-fork-testing/actions/runs/38033345354) | Xcode 27 StikJIT import and both generated-header builds passed. All 48 iOS server objects compiled and passed arm64 validation and objcopy. Apple ar created the archive; the exact-member comparison stopped on its legitimate `__.SYMDEF SORTED` index. The corrected checker passes against this actual saved member list; native retry follows. |

Run 4351c1e / [38033705916](https://github.com/abrown26-Diman/madeira-fork-testing/actions/runs/38033705916): **wineserver native build and validation PASS**. Archive: 1,310,968 bytes, SHA-256 `b981908ab710935f755bc42166e8d54c3e09b138ac2558d535160a6cf3fcd882`. Overall run deliberately cancelled after that successful step to incorporate source-verified missing FEX build options/targets. Evidence upload completed. LLVM and FreeType source downloads verified their pinned hashes before cancellation.

Full build at `8ff5753`: [38034106394](https://github.com/abrown26-Diman/madeira-fork-testing/actions/runs/38034106394) **failed during native FEX configuration**, after successful LLVM iOS, wineserver, GMP, Nettle, GnuTLS, FFmpeg and FreeType compilation. Errors: `string no output variable specified` (FEX/CMakeLists.txt:89), then `Unsupported processor type .` (line 115). The iOS wrapper set Apple's compiler architecture but omitted the separate `CMAKE_SYSTEM_PROCESSOR`; the fix supplies `arm64` only for the native iOS build. The Windows ARM64EC toolchain already supplies its correct processor triple. FEX source and validation remain unchanged.

Retry at `ed68f99`: [38068957841](https://github.com/abrown26-Diman/madeira-fork-testing/actions/runs/38068957841), pending native validation. It adds an early FEX configure check and exact, manifest-verified caching of completed LLVM outputs. The old run uploaded LLVM hashes/logs, not the libraries, so the first cache population still requires one fresh LLVM build.

The first three runs never reached LLVM or the application build. Raw decisive logs are retained in [evidence/milestone-03](evidence/milestone-03); full failure artifacts remain attached to the Actions runs.

## Tests

[Cross-platform checks at e04ea3a](https://github.com/abrown26-Diman/madeira-fork-testing/actions/runs/38033345366): **PASS** on Windows, Linux and macOS, plus recursive Linux source audit/selected existing graphics checks. The 15 diagnostic tests pass. All 12 CI unit tests pass on POSIX at e04ea3a; the two POSIX-only fault-injection tests are explicitly skipped on Windows. The new tests cover complete archive source membership, unexpected Wine additions, missing replacement sources, failed compiler/objcopy preserving an existing archive, complete package resources, missing WoW64 support, stale copied resources and accidental proprietary runtime inclusion. These tests do not substitute for native compilation.

Local Windows at 4351c1e: 15 diagnostics pass, 11 CI tests pass, 2 POSIX-only tests skip. The added membership test accepts Apple index metadata and rejects missing/duplicate/stale/reordered objects. All cross-platform checks also pass at [4351c1e](https://github.com/abrown26-Diman/madeira-fork-testing/actions/runs/38033705899). Bash syntax checks pass for the four changed build scripts using Git Bash in the normal Windows process context. Optional local YAML parsing was unavailable because PyYAML is not installed; GitHub accepted and executed the workflow. The current 8ff5753 adds the provisioning-profile test: 14 CI tests total (12 pass locally, 2 POSIX skips), and [cross-platform CI passes](https://github.com/abrown26-Diman/madeira-fork-testing/actions/runs/38034106406). Existing unrelated 63-script host inventory failures remain documented in [HOST_TEST_FINDINGS.md](HOST_TEST_FINDINGS.md).

## Changes and rationale

- `build/wineserver/{build.sh,sources.py}`: complete 48-member source reconstruction, unchanged iOS replacements and symbol renames, fresh object directory and validation before atomic staging. Removes undocumented binary seed dependency.
- `build/ci/bootstrap-wine.sh`: checksum-verified pinned LLVM-MinGW, correct host SDK and actual Wine-generated headers.
- `build/ci/bootstrap-libraries.sh`: exact LLVM 15.0.7/FreeType 2.13.3 sources, recorded hashes, guarded documented LLVM CMake patch, host tablegen and iOS static components.
- `build/fex-ios/build.sh` explicitly requests the existing `JemallocLibs` and `softfloat_3e` archives referenced by Xcode. `build/fex-arm64ec/build.sh` selects the existing fork's `FEX_IOS_HOST_BUILD` and `FEX_IOS_HOST` paths so its iOS entry/alias code and CRT are built. No FEX source changes.
- `build/ci/build-ios.sh` and workflow: staged bootstrap, recorded versions, matching Swift generation, actual native component/app build, initial DXMT archive merge, complete WoW64 core, failure logs and gated package.
- `tools/ci/audit_inputs.py`: removes the seed archive as an input and the nonexistent Wine version-header check.
- `tools/ci/verify_app.py`, `tests/ci/test_{wineserver_sources,package_resources}.py`: resource/native architecture checks and failure tests.
- FreeType notices are copied from the pinned hash-verified source into the bundled licence folder. Package validation rejects provisioning profiles.
- Architecture/build/backlog documentation: exact construction, dependency provenance, instructions and remaining limitations. See [WINESERVER_BUILD.md](WINESERVER_BUILD.md) and [BUILD_AND_TEST.md](BUILD_AND_TEST.md).

## Remaining gates

Wineserver, LLVM iOS and the libraries listed above passed. Remaining gates are FEX, the remaining native/PE dependency scripts, final Xcode compilation/link, package validation and SHA-256, then independent signing and physical-device regression tests. Existing tracked PE modules and StikJIT retain their prior source-rebuild provenance limitations; this milestone does not silently relabel them as rebuilt. Signing requirements are separate from compilation. No IPA is currently available.

Next engineering action: inspect the active run's first compiler/linker failure and fix the smallest source-supported build issue without changing runtime behavior.
