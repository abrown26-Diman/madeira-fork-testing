# Wineserver archive reconstruction — Milestone 0.3

Status: source-complete recipe implemented; native validation is in progress. An archive compilation result is not an application link or a device test.

Baseline: Madeira `497f04430685bec284df536beff1a496cb7ff706`, Wine `257f271cfffed9f22f7987cac53bc00095d092fe` (11.4). No submodule revisions or runtime sources changed.

## Exact membership

The pinned `wine/server/Makefile.in` lists 44 C translation units. `build/wineserver/sources.py` checks that ordered list before compiling. Nine are mapped to Madeira's established replacement/object names; four additional objects bring the archive to 48 members. Every other server source is compiled directly from the pinned fork, including the formerly inherited atom, clipboard, console, registry and synchronization objects. Non-C entries (security.h and manual pages) are not archive members.

| Archive member | Source |
|---|---|
| `async.o` | `wine/server/async.c` |
| `atom.o` | `wine/server/atom.c` |
| `change.o` | `wine/server/change.c` |
| `class.o` | `wine/server/class.c` |
| `clipboard.o` | `wine/server/clipboard.c` |
| `completion.o` | `wine/server/completion.c` |
| `console.o` | `wine/server/console.c` |
| `d3dkmt.o` | `wine/server/d3dkmt.c` |
| `debugger.o` | `wine/server/debugger.c` |
| `device.o` | `wine/server/device.c` |
| `directory.o` | `wine/server/directory.c` |
| `event.o` | `wine/server/event.c` |
| `fd_ios.o` | `build/wineserver/fd_ios.c` |
| `file.o` | `wine/server/file.c` |
| `handle.o` | `wine/server/handle.c` |
| `hook.o` | `wine/server/hook.c` |
| `inproc_sync.o` | `wine/server/inproc_sync.c` |
| `mach_ios.o` | `build/wineserver/mach_ios.c` |
| `mailslot.o` | `wine/server/mailslot.c` |
| `main_ios.o` | `build/wineserver/main_ios.c` |
| `mapping.o` | `build/wineserver/mapping_ios.c` |
| `mutex.o` | `wine/server/mutex.c` |
| `named_pipe.o` | `wine/server/named_pipe.c` |
| `object.o` | `wine/server/object.c` |
| `process_ios.o` | `wine/server/process.c` |
| `procfs.o` | `wine/server/procfs.c` |
| `ptrace.o` | `wine/server/ptrace.c` |
| `queue.o` | `build/wineserver/queue_ios.c` |
| `region.o` | `wine/server/region.c` |
| `registry.o` | `wine/server/registry.c` |
| `request_ios.o` | `build/wineserver/request_ios.c` |
| `semaphore.o` | `wine/server/semaphore.c` |
| `serial.o` | `wine/server/serial.c` |
| `signal.o` | `wine/server/signal.c` |
| `sock.o` | `wine/server/sock.c` |
| `symlink.o` | `wine/server/symlink.c` |
| `thread.o` | `wine/server/thread.c` |
| `timer.o` | `wine/server/timer.c` |
| `token.o` | `wine/server/token.c` |
| `trace.o` | `wine/server/trace.c` |
| `unicode_ios.o` | `build/wineserver/unicode_ios.c` |
| `user.o` | `wine/server/user.c` |
| `window.o` | `build/wineserver/window_ios.c` |
| `winstation.o` | `wine/server/winstation.c` |
| `wine_log_ios.o` | `build/wineserver/wine_log_ios.c` |
| `hidpad_ios.o` | `build/wineserver/hidpad_ios.c` |
| `hidparse_ios.o` | `build/hidpad/hidparse_ios.c` |
| `wineserver_ios_kill.o` | `build/wineserver/wineserver_ios_kill.c` |

The former Jul-10 sock object mentioned by upstream is not needed: the baseline build script already selected `wine/server/sock.c`. There is no substitute empty object or imported seed archive. The first source-list comparison passed locally against all 44 entries.

## Compilation and ABI

Each build uses a fresh `build/wineserver/obj/build.XXXXXX` directory. Sources are compiled as iOS arm64, minimum iOS 17, `-O2`, with the iPhoneOS SDK selected by Xcode. The existing include paths, `__WINESRC__`, `WINE_IOS`, `HAVE_LINUX_NTSYNC_H=1`, `main=wineserver_main`, bindir/datadir defines, implicit-function warning setting, and forced includes are preserved in `build.sh`.

`config_ios.h` includes the macOS configure-generated `config.h` then disables unsupported ptrace/user/TCP headers. `stdarg.h`, `unicode_fix.h` and `wineserver_ios_kill.h` are forced includes. The kill wrapper is compiled without the kill macro, preserving its nonrecursive call to the native implementation. Wine's generated IDL headers come from `make include/all` in clean aarch64 and ARM64EC configure trees. The previous audit's `wine/version.h` prerequisite was incorrect for this revision: no matching include or generation rule exists.

The server runs as a thread inside the app rather than a standalone process. Madeira's main wrapper, Mach/thread handling, socket/request dispatch, Unicode path lookup, window/queue/mapping wrappers, madsync integration and HID support remain in place. In particular, the main wrapper's signal behavior and infinite no-client timeout are unchanged.

After compilation, LLVM objcopy renames both definitions and references for the following Mach-O symbols (each has a leading underscore): `alloc_user_handle`, `free_user_handle`, `get_virtual_screen_rect`, `destroy_thread_windows`, `get_window_thread`, `is_desktop_class`, `is_message_class`, `is_window_visible`, `mirror_region`, `send_notify_message`, `shared_session`, `user_shared_data`. The replacement is `ws_` plus the original name. This preserves separate writable server-side pointers and client-side pointers; preprocessor renaming would damage Wine handler macro expansion.

Objects are archived in the explicit Wine source order followed by the four extras. The ar symbol index supports normal link resolution; there are no initializer ordering changes. The old script sorted inherited objects lexically, but no source-supported dependency on that order has been identified. Final executable linking and device testing remain required.

## Integrity and evidence

The script checks arm64 architecture on every object, exact ordered archive membership, absence of the twelve old global symbol names, and definitions of `wineserver_main`, `ws_shared_session`, and `ws_user_shared_data`. It records source paths, archive members, global symbols, undefined symbols, compiler errors and SHA-256. Undefined references within a static archive are expected (other members, app bridges and SDK functions); they are recorded, not incorrectly treated as proof of a successful link. The Xcode executable link is the final resolution check.

No output is staged until compilation, renaming and validation finish. Old partial-build command arguments request a full build, so an old object cannot silently survive. Failed builds preserve the existing app archive and their diagnostic directory. No build output cache is restored by CI.

Reproduce on the selected macOS runner: install the workflow's host tools, run `bash build/ci/bootstrap-wine.sh`, then `bash build/wineserver/build.sh`. No signing identity or seed archive is required.
