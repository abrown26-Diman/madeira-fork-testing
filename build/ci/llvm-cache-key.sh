#!/bin/bash
# SPDX-License-Identifier: GPL-3.0-or-later
# Madeira Converter Exception: see LICENSE-EXCEPTION.md
set -euo pipefail
cd "$(dirname "$0")/../.."
mkdir -p work/ci
# Exact key only: source pins, patches and every build flag live in the hashed
# recipe. SDK/compiler identities and host tools distinguish runner updates.
{
    shasum -a 256 build/ci/bootstrap-libraries.sh build/ci/llvm-cache-key.sh tools/ci/cache_manifest.py
    uname -m
    sw_vers
    xcodebuild -version
    xcrun clang --version
    shasum -a 256 "$(xcrun --find clang)" "$(xcrun --find clang++)" "$(xcrun --find ld)"
    for sdk in macosx iphoneos; do
        xcrun --sdk "$sdk" --show-sdk-path
        xcrun --sdk "$sdk" --show-sdk-build-version
        shasum -a 256 "$(xcrun --sdk "$sdk" --show-sdk-path)/SDKSettings.json"
    done
    cmake --version
    ninja --version
} > work/ci/llvm-cache-inputs.txt
key="llvm-ios-$(shasum -a 256 work/ci/llvm-cache-inputs.txt | cut -d' ' -f1)"
printf 'key=%s\n' "$key" | tee -a "${GITHUB_OUTPUT:-/dev/stdout}"
