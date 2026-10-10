#!/bin/bash
# SPDX-License-Identifier: GPL-3.0-or-later
# Madeira Converter Exception: see LICENSE-EXCEPTION.md
# Native build recipe; status and actual CI evidence: docs/BUILD_AND_TEST.md.
set -euo pipefail
R="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$R"
mkdir -p work/ci
python3 tools/ci/audit_inputs.py --require-native --output work/ci/native-inputs.json
export PATH="$R/toolchains/llvm-mingw-20260421-ucrt-macos-universal/bin:$PATH"
export SDKROOT="$(xcrun --sdk macosx --show-sdk-path)"
export CC="$(xcrun --sdk macosx --find clang)"
export CXX="$(xcrun --sdk macosx --find clang++)"
export CMAKE_BUILD_PARALLEL_LEVEL="${CMAKE_BUILD_PARALLEL_LEVEL:-3}"
for command in xcodebuild xcrun cmake meson ninja bison cargo rustup; do
    command -v "$command" >/dev/null || { echo "error: missing $command" >&2; exit 1; }
done
xcrun --sdk iphoneos --find clang
xcrun --sdk macosx metal --version
rustup target add aarch64-apple-ios
# Existing scripts and fork pins are retained. This rebuilds the documented
# components, but does not prove all tracked PE binaries were rebuilt.
for component in gnutls-ios ffmpeg freetype-ios fex-ios fex-arm64ec; do
    if [ "$component" = gnutls-ios ]; then
        (cd build/gnutls-ios/src && shasum -a 256 -c SHA256SUMS)
    fi
    bash "build/$component/build.sh"
done
bash build/wine-pe/build-ntdll.sh
bash build/wine-pe/build-modules.sh
# The existing WoW64 core is mandatory for the complete package.
make -C wine/build-macos -j3 dlls/ntdll/aarch64-windows/ntdll.dll \
    dlls/wow64/aarch64-windows/wow64.dll dlls/wow64win/aarch64-windows/wow64win.dll
for module in ntdll wow64 wow64win; do
    cp "wine/build-macos/dlls/$module/aarch64-windows/$module.dll" "app/Madeira/aarch64-windows/$module.dll"
    aarch64-w64-mingw32-strip --strip-debug "app/Madeira/aarch64-windows/$module.dll"
done
for component in ntdll-unix win32u-unix dxmt-ios rppairing-ios; do
    bash "build/$component/build.sh"
done
# Initial merge documented in build/dxmt-ios/README.md. The component script
# itself only refreshes an existing archive; explicitly create and stage it.
xcrun -sdk iphoneos libtool -static -o build/dxmt-ios/libdxmt_combined.a \
    build/dxmt-ios/obj/*.o toolchains/llvm-ios-build/lib/*.a
cp build/dxmt-ios/libdxmt_combined.a app/Madeira/
if [ ! -e dxmt/toolchains ]; then ln -s ../toolchains dxmt/toolchains; fi
meson setup dxmt/build-arm64ec dxmt -Dbuildtype=release \
    -Dwine_build_path=../../wine/build-arm64ec --cross-file=dxmt/build-arm64ec-win.txt --native-file=dxmt/build-osx.txt
ninja -C dxmt/build-arm64ec
for module in d3d11 dxgi winemetal; do
    cp "dxmt/build-arm64ec/src/$module/$module.dll" app/Madeira/arm64ec-windows/
done
cp dxmt/build-arm64ec/src/d3d10/d3d10core.dll app/Madeira/arm64ec-windows/
bash build/madeira-d3d12/build-pe.sh
bash build/madeira-dock/build.sh --check
# Include the i386 farm, not an IPA that silently loses WoW64 support.
bash build/wine-i386/build.sh
bash build/fex-wow64/build.sh
bash build/stage-licenses.sh
# Xcode references the optional VC runtime folder. Keep it empty in CI.
mkdir -p app/Madeira/x86_64-vcruntime
if find app/Madeira/x86_64-vcruntime -iname '*.dll' | grep -q .; then
    echo 'error: CI does not package Microsoft VC runtime DLLs' >&2; exit 1
fi
SHA="$(git rev-parse HEAD)"
# Existing BuildStamp logger consumes this plist entry. No new gameplay timer.
/usr/libexec/PlistBuddy -c 'Delete :MadeiraBuild' app/Madeira/Info.plist 2>/dev/null || true
/usr/libexec/PlistBuddy -c "Add :MadeiraBuild string $SHA Debug" app/Madeira/Info.plist
xcodebuild -project app/Madeira.xcodeproj -scheme Madeira -configuration Debug \
    -destination 'generic/platform=iOS' -derivedDataPath "$R/work/DerivedData" \
    -resultBundlePath "$R/work/ci/Madeira.xcresult" \
    CODE_SIGNING_ALLOWED=NO CODE_SIGNING_REQUIRED=NO DEVELOPMENT_TEAM= \
    LD_GENERATE_MAP_FILE=YES 'LD_MAP_FILE_PATH=$(SRCROOT)/../work/ci/$(TARGET_NAME)-LinkMap.txt' build
APP="$R/work/DerivedData/Build/Products/Debug-iphoneos/Madeira.app"
python3 tools/ci/verify_app.py "$APP" --output work/ci/package-manifest.json
if [ "${PACKAGE_IPA:-0}" = 1 ]; then
    mkdir -p work/package work/staging/Payload
    ditto "$APP" work/staging/Payload/Madeira.app
    (cd work/staging && ditto -c -k --keepParent Payload ../package/Madeira-unsigned.ipa)
    cp work/ci/native-inputs.json work/ci/package-manifest.json work/ci/downloads.tsv work/package/
    cp app/Madeira/Madeira.entitlements work/package/required-entitlements.plist
    shasum -a 256 work/package/Madeira-unsigned.ipa > work/package/SHA256SUMS
fi
