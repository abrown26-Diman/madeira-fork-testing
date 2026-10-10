#!/bin/bash
# SPDX-License-Identifier: GPL-3.0-or-later
# Madeira Converter Exception: see LICENSE-EXCEPTION.md
# Full source reconstruction; no prebuilt seed and no incremental object reuse.
set -euo pipefail
BUILD_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$BUILD_DIR/../.." && pwd)"
WINE_SRC="$REPO_ROOT/wine"
SDK=$(xcrun --sdk iphoneos --show-sdk-path)
APP_LIB="$REPO_ROOT/app/Madeira/libwineserver.a"
SHIMS_DIR="$REPO_ROOT/build/ntdll-unix/shims"
case "${1:-all}" in
    all|request|main|mach|unicode) ;;
    *) echo "Usage: $0 [all|request|main|mach|unicode]" >&2; exit 1;;
esac
# Historical partial-build arguments still work, but now rebuild all members.
mkdir -p "$BUILD_DIR/obj"
OBJ_DIR=$(mktemp -d "$BUILD_DIR/obj/build.XXXXXX")
echo "wineserver build evidence: $OBJ_DIR"
python3 "$BUILD_DIR/sources.py" > "$OBJ_DIR/sources.tsv"
OBJCOPY="${OBJCOPY:-$(command -v llvm-objcopy)}"
CC_FLAGS=(
    -arch arm64 -isysroot "$SDK" -miphoneos-version-min=17.0 -O2
    -I"$WINE_SRC/include" -I"$WINE_SRC/include/wine"
    -I"$WINE_SRC/build-macos/include"
    -I"$BUILD_DIR" -I"$WINE_SRC/server"
    -I"$SHIMS_DIR"
    -I"$BUILD_DIR/../madsync" -DHAVE_LINUX_NTSYNC_H=1
    -include "$BUILD_DIR/config_ios.h"
    -include stdarg.h
    -include "$BUILD_DIR/unicode_fix.h"
    -include "$BUILD_DIR/wineserver_ios_kill.h"
    -DBINDIR=\"/usr/local/bin\" -DDATADIR=\"/usr/local/share\"
    -D__WINESRC__ -DWINE_IOS=1
    -Dmain=wineserver_main
    # Symbol collisions with win32u are NOT handled via -D macros — that
    # rewrites macro args (e.g. DECL_HANDLER(name)) and breaks struct
    # name concatenation. Renames done post-compile via objcopy below,
    # applied to EVERY .o in libwineserver.a so cross-file refs (e.g.
    # clipboard.c calling send_notify_message defined in queue.c) stay
    # internal to the archive after the renames.
    -Wno-implicit-function-declaration
)

COLLISIONS=(
    alloc_user_handle free_user_handle get_virtual_screen_rect
    destroy_thread_windows get_window_thread is_desktop_class
    is_message_class is_window_visible mirror_region send_notify_message
    # shared_session: BOTH wineserver and win32u-unix declare it as a
    # common global. Single-process iOS link merges them — last writer
    # wins. win32u's shared_session_init() overwrites with the client-side
    # NtMapViewOfSection result (read-only), making wineserver's writes
    # silently fail since they're going through the client's RO view.
    # Rename wineserver-side to ws_shared_session so each side has its
    # own pointer to its own mapping of the same backing file.
    shared_session
    # user_shared_data: the same defect as shared_session, one layer over.
    # wineserver defines it as a common global and ntdll-unix defines it as
    # initialized data; the single-process link merges them. wineserver's
    # create_user_data_mapping() sets it to a writable alias, then the guest's
    # ntdll init runs virtual_ios.c's `user_shared_data = NULL;
    # NtAllocateVirtualMemory(..., PAGE_READONLY)` over the SAME variable, so
    # the server's pointer starts aiming at the guest's read-only page in the
    # FEX guest band. Unlike shared_session this does not fail silently: the
    # server's next store faults on a PROT_READ page and the main loop wedges
    # forever, which is why the shared clock could never be published and why
    # every process hung in server_init_process() the moment a client
    # connected -- guest ntdll init is exactly when the pointer was stolen.
    user_shared_data
)
RENAME_ARGS=()
for s in "${COLLISIONS[@]}"; do
    RENAME_ARGS+=(--redefine-sym "_${s}=_ws_${s}")
done

OBJECTS=()
while IFS=$'\t' read -r name src; do
    flags=("${CC_FLAGS[@]}")
    if [ "$name" = wineserver_ios_kill ]; then
        # Must not force-include its own kill macro: that would recurse.
        flags=(-arch arm64 -isysroot "$SDK" -miphoneos-version-min=17.0 -O2
               -I"$BUILD_DIR" -DWINE_IOS=1 -Wno-implicit-function-declaration)
    fi
    echo "Compiling $src -> $name.o"
    if ! xcrun -sdk iphoneos clang "${flags[@]}" -c "$REPO_ROOT/$src" \
            -o "$OBJ_DIR/$name.o" 2> "$OBJ_DIR/err-$name.txt"; then
        cat "$OBJ_DIR/err-$name.txt" >&2
        exit 1
    fi
    # Rename definitions AND references, including previously inherited objects.
    "$OBJCOPY" "${RENAME_ARGS[@]}" "$OBJ_DIR/$name.o"
    xcrun lipo "$OBJ_DIR/$name.o" -verify_arch arm64
    OBJECTS+=("$OBJ_DIR/$name.o")
done < "$OBJ_DIR/sources.tsv"
xcrun ar rcs "$OBJ_DIR/libwineserver.a" "${OBJECTS[@]}"
xcrun ar t "$OBJ_DIR/libwineserver.a" > "$OBJ_DIR/members.txt"
python3 "$BUILD_DIR/sources.py" --verify-members "$OBJ_DIR/members.txt"
xcrun nm -g "$OBJ_DIR/libwineserver.a" > "$OBJ_DIR/symbols.txt"
# Archive undefined symbols include cross-member and app/SDK imports. Preserve
# them for the eventual executable link; an archive alone cannot resolve those.
xcrun nm -u "$OBJ_DIR/libwineserver.a" > "$OBJ_DIR/undefined.txt"
for s in "${COLLISIONS[@]}"; do
    if grep -Eq "[[:space:]]_${s}$" "$OBJ_DIR/symbols.txt"; then
        echo "unrenamed wineserver symbol: $s" >&2; exit 1
    fi
done
for s in wineserver_main ws_shared_session ws_user_shared_data; do
    grep -Eq "[[:space:]][BCDST][[:space:]]+_${s}$" "$OBJ_DIR/symbols.txt" || {
        echo "missing required wineserver definition: $s" >&2; exit 1;
    }
done
shasum -a 256 "$OBJ_DIR/libwineserver.a" > "$OBJ_DIR/SHA256SUMS"
# Preserve the old app archive on any compile/rename/validation failure.
cp "$OBJ_DIR/libwineserver.a" "$APP_LIB.tmp"
mv "$APP_LIB.tmp" "$APP_LIB"
echo "Staged $APP_LIB ($(wc -c < "$APP_LIB" | tr -d ' ') bytes)"
