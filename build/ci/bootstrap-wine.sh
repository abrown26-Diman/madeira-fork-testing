#!/bin/bash
# SPDX-License-Identifier: GPL-3.0-or-later
# Madeira Converter Exception: see LICENSE-EXCEPTION.md
set -euo pipefail
R="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$R"
mkdir -p toolchains work/ci work/downloads
TC=llvm-mingw-20260421-ucrt-macos-universal
SHA=bd85a3975723815cef28dbbd2ca2cb0c926f6b348a12a0453f39f7af273cb3f7
URL="https://github.com/mstorsjo/llvm-mingw/releases/download/20260421/$TC.tar.xz"
curl --fail --location --retry 3 "$URL" -o "work/downloads/$TC.tar.xz"
echo "$SHA  work/downloads/$TC.tar.xz" | shasum -a 256 -c -
printf '%s\t%s\n' "$SHA" "$URL" > work/ci/downloads.tsv
# Do not overlay an older toolchain installation.
test ! -e "toolchains/$TC"
tar -xJf "work/downloads/$TC.tar.xz" -C toolchains
export PATH="$R/toolchains/$TC/bin:$PATH"
export CC="$(xcrun --sdk macosx --find clang)"
export CXX="$(xcrun --sdk macosx --find clang++)"
for arch in aarch64 arm64ec; do
    B="$R/wine/build-$arch"
    [ "$arch" != aarch64 ] || B="$R/wine/build-macos"
    test ! -e "$B"
    mkdir -p "$B"
    (
        cd "$B"
        ../configure --enable-archs="$arch" --without-x --disable-tests --enable-winegstreamer
        make -j3 include
    ) 2>&1 | tee "work/ci/wine-configure-$arch.txt"
done
