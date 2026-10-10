#!/bin/bash
# SPDX-License-Identifier: GPL-3.0-or-later
# Madeira Converter Exception: see LICENSE-EXCEPTION.md
set -euo pipefail
R="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$R"
mkdir -p work/downloads work/ci toolchains research
fetch_source() {
    local url="$1" sha="$2" name="$3" dest="$4"
    curl --fail --location --retry 3 "$url" -o "work/downloads/$name.tar.gz"
    echo "$sha  work/downloads/$name.tar.gz" | shasum -a 256 -c -
    printf '%s\t%s\n' "$sha" "$url" >> work/ci/downloads.tsv
    test ! -e "$dest"
    mkdir -p "$dest"
    tar -xzf "work/downloads/$name.tar.gz" --strip-components=1 -C "$dest"
}
fetch_source https://codeload.github.com/freetype/freetype/tar.gz/42608f77f20749dd6ddc9e0536788eaad70ea4b5 \
    68ce87bb59ea209eb7350f41a94a27519ce16b37011b475a1e62d4abee154b66 freetype-2.13.3 research/freetype
fetch_source https://codeload.github.com/llvm/llvm-project/tar.gz/8dfdcc7b7bf66834a761bd8de445840ef68e4d1a \
    b7f15ee379144b0c26a64ff9a1f27d0ea341a0db0c91b71c66bbfa8b310788ac llvm-15.0.7 toolchains/llvm-project
# The existing DXMT recipe requires Darwin dead stripping on iOS. Make only
# that documented build-system substitution, with an exact context guard.
python3 - <<'PY'
from pathlib import Path
p = Path('toolchains/llvm-project/llvm/cmake/modules/AddLLVM.cmake')
s = p.read_text()
old = 'if(${CMAKE_SYSTEM_NAME} MATCHES "Darwin")\n        # ld64'
assert s.count(old) == 1, 'pinned LLVM dead-strip context changed'
p.write_text(s.replace(old, 'if(${CMAKE_SYSTEM_NAME} MATCHES "Darwin|iOS")\n        # ld64'))
PY
export CC="$(xcrun --sdk macosx --find clang)"
export CXX="$(xcrun --sdk macosx --find clang++)"
export CMAKE_BUILD_PARALLEL_LEVEL="${CMAKE_BUILD_PARALLEL_LEVEL:-3}"
cmake -S toolchains/llvm-project/llvm -B toolchains/llvm-host-build -G Ninja \
    -DCMAKE_OSX_SYSROOT="$(xcrun --sdk macosx --show-sdk-path)" \
    -DCMAKE_BUILD_TYPE=Release -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
    -DLLVM_TARGETS_TO_BUILD= -DLLVM_INCLUDE_TESTS=OFF -DLLVM_INCLUDE_BENCHMARKS=OFF \
    -DLLVM_ENABLE_ZLIB=OFF -DLLVM_ENABLE_ZSTD=OFF -DLLVM_ENABLE_TERMINFO=OFF
cmake --build toolchains/llvm-host-build --target llvm-tblgen
cmake -S toolchains/llvm-project/llvm -B toolchains/llvm-ios-build -G Ninja \
    -DCMAKE_SYSTEM_NAME=iOS -DCMAKE_OSX_ARCHITECTURES=arm64 \
    -DCMAKE_OSX_SYSROOT=iphoneos -DCMAKE_OSX_DEPLOYMENT_TARGET=17.0 \
    -DCMAKE_BUILD_TYPE=Release -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
    -DLLVM_TABLEGEN="$R/toolchains/llvm-host-build/bin/llvm-tblgen" \
    -DLLVM_HOST_TRIPLE=arm64-apple-ios17.0 -DLLVM_DEFAULT_TARGET_TRIPLE=arm64-apple-ios17.0 \
    -DLLVM_TARGET_ARCH=host -DLLVM_TARGETS_TO_BUILD= -DLLVM_ENABLE_PROJECTS= \
    -DLLVM_BUILD_TOOLS=OFF -DLLVM_BUILD_UTILS=OFF -DLLVM_INCLUDE_TESTS=OFF \
    -DLLVM_INCLUDE_BENCHMARKS=OFF -DLLVM_ENABLE_ZLIB=OFF -DLLVM_ENABLE_ZSTD=OFF \
    -DLLVM_ENABLE_TERMINFO=OFF -DLLVM_ENABLE_LIBXML2=OFF
# Same components as dxmt/src/airconv/meson.build: bitwriter + passes and their
# transitive libraries. No unnecessary target backends or executable tools.
cmake --build toolchains/llvm-ios-build --target LLVMBitWriter LLVMPasses
for archive in toolchains/llvm-ios-build/lib/*.a; do
    xcrun lipo -verify_arch arm64 "$archive"
done
shasum -a 256 toolchains/llvm-ios-build/lib/*.a > work/ci/llvm-ios-SHA256SUMS
