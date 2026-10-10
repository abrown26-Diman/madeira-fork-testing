# Upstream host nonzero results: macos

See the JSON inventory for passes, partial runs and exact durations.

## check-cfg-early-docs.py

```text
ok: no madeira.cfg: constructor exports MADEIRA_DOCS_DIR, madsync off (fastsync is the default)
ok: log names value, file and directory
ok: madeira.cfg without inproc-sync: madsync off (fastsync is the default)
ok: inproc-sync = 0 honoured
ok: inproc-sync = 1 honoured
ok: no madeira.cfg: legacy madeira-inproc-sync.txt still honoured
ok: old order ignores inproc-sync = 1 (bug reproduced)
ok: CFFIXED_USER_HOME anchor alone finds the file
ok: BOM + CRLF: first key still found
ok: MADEIRA_CFG_EARLY_DOCS=0 restores the old lookup
ok: env.MADEIRA_CFG_EARLY_DOCS = 0 in madeira.cfg also restores it
ok: an exported MADEIRA_DOCS_DIR is left alone
FAIL: Swift reader agrees on the BOM + CRLF file
'SWIFT inproc-sync=unset\n'

```

## check-d3d9-splitlock.py

```text
ld: library 'atomic' not found
clang++: error: linker command failed with exit code 1 (use -v to see invocation)
PASS: device-lock switches present; no split-lock rollback; WOW64 strict split locks default on
Traceback (most recent call last):
  File "/Users/runner/work/madeira-fork-testing/madeira-fork-testing/tests/host/check-d3d9-splitlock.py", line 135, in <module>
    subprocess.run(["c++", "-std=c++20", "-O1", "-g", "-pthread", "-fsanitize=address,undefined",
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    "-o", str(t / "cas"), str(t / "cas.cpp"), "-latomic"], check=True)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/subprocess.py", line 578, in run
    raise CalledProcessError(retcode, process.args,
                             output=stdout, stderr=stderr)
subprocess.CalledProcessError: Command '['c++', '-std=c++20', '-O1', '-g', '-pthread', '-fsanitize=address,undefined', '-o', '/var/folders/nj/vtw8zd2j31d1gdrtntc5y4600000gn/T/tmppgndohgs/cas', '/var/folders/nj/vtw8zd2j31d1gdrtntc5y4600000gn/T/tmppgndohgs/cas.cpp', '-latomic']' returned non-zero exit status 1.

```

## check-dock-components.py

```text
/Applications/Xcode_16.4.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.sdk/usr/include/module.modulemap:15:1: note: in file included from /Applications/Xcode_16.4.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.sdk/usr/include/module.modulemap:15:
 13 | extern module SQLite3 "SQLite3.modulemap"
 14 | extern module xcselect "xcselect.modulemap"
 15 | extern module zlib "zlib.modulemap"
    | `- note: in file included from /Applications/Xcode_16.4.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.sdk/usr/include/module.modulemap:15:
 16 |
 17 | // Interfaces for process management and interprocess communication.

/Applications/Xcode_16.4.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.sdk/usr/include/zlib.modulemap:1:8: error: redefinition of module 'zlib'
1 | module zlib [system] {
  |        `- error: redefinition of module 'zlib'
2 |   header "zconf.h"
3 |   header "zlib.h"

/var/folders/nj/vtw8zd2j31d1gdrtntc5y4600000gn/T/madeira-runtime-yuygkpeg/module.modulemap:1:8: note: previously defined here
1 | module zlib [system] { header "/usr/include/zlib.h" export * link "z" }
  |        `- note: previously defined here

/var/folders/nj/vtw8zd2j31d1gdrtntc5y4600000gn/T/madeira-runtime-yuygkpeg/module.modulemap:1:31: error: header '/usr/include/zlib.h' not found
1 | module zlib [system] { header "/usr/include/zlib.h" export * link "z" }
  |                               `- error: header '/usr/include/zlib.h' not found

/Users/runner/work/madeira-fork-testing/madeira-fork-testing/app/Madeira/SteamRuntime.swift:6:8: error: could not build Objective-C module 'zlib'
  4 |
  5 | import Foundation
  6 | import zlib
    |        `- error: could not build Objective-C module 'zlib'
  7 | #if canImport(CryptoKit)
  8 | import CryptoKit
PASS: pinned client DLL is a build the pinned Dock host supports
PASS: three pinned packages from one HTTPS Valve host; redirects stay on it
Traceback (most recent call last):
  File "/Users/runner/work/madeira-fork-testing/madeira-fork-testing/tests/host/check-dock-components.py", line 87, in <module>
    subprocess.run([SWIFTC, '-I', str(tmp), str(source), str(tmp/'main.swift'), '-o', str(exe)], check=True)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/subprocess.py", line 578, in run
    raise CalledProcessError(retcode, process.args,
                             output=stdout, stderr=stderr)
subprocess.CalledProcessError: Command '['/usr/bin/swiftc', '-I', '/var/folders/nj/vtw8zd2j31d1gdrtntc5y4600000gn/T/madeira-runtime-yuygkpeg', '/Users/runner/work/madeira-fork-testing/madeira-fork-testing/app/Madeira/SteamRuntime.swift', '/var/folders/nj/vtw8zd2j31d1gdrtntc5y4600000gn/T/madeira-runtime-yuygkpeg/main.swift', '-o', '/var/folders/nj/vtw8zd2j31d1gdrtntc5y4600000gn/T/madeira-runtime-yuygkpeg/check']' returned non-zero exit status 1.

```

## check-dock-installers.py

```text
PASS: repeated sections all count; unsafe, escaping and uninstall entries dropped (["runtime a", "tool", "package", "gone"])
PASS: without an app ID only HasRunKey entries count
PASS: no HasRunKey: Steam's per-app key, value 1
PASS: HasRunKey and minimum kept
PASS: program and arguments expanded
PASS: forward slashes become Windows separators
PASS: both registry views
PASS: HKCU: one view
PASS: invalid app IDs add nothing
PASS: a Windows client's own record (32-bit view) counts
PASS: a value below the minimum is not done
PASS: mark raises both views
PASS: marking again changes nothing
PASS: everything pending, whatever the program
PASS: done, missing, unsupported, pending (["pending", "done", "unsupported", "missing"])
PASS: the note names every fate (One-time installs. Runs first: runtime a. Already done: tool. Installer file missing: gone. Cannot run in this build: package (Windows Installer package).)
PASS: all done: no note
PASS: per-start limit
PASS: labels keep only safe characters
PASS: CRLF batch
PASS: begin, services, each program with its exit, end
PASS: every redirection follows a space
PASS: services started once
PASS: services off: recorded, dockhost not run
PASS: the batch records nothing itself; no 'if not errorlevel 1'
PASS: parsed statuses and labels
PASS: running program, not ended
PASS: success statuses
PASS: service outcomes, letters only
PASS: malformed lines ignored
PASS: no file: empty ledger; a fresh game runs its installs
PASS: JSON round trip
PASS: a damaged file reads as empty
FAIL: paths resolve case-insensitively
PASS: parent references, other drives and absent files do not resolve
PASS: a link out of drive_c does not resolve
PASS: PE machine read
PASS: a 32-bit installer needs 32-bit support
PASS: an x64 installer runs
PASS: a package needs msiexec.exe
PASS: game and shared scripts (["runtime a", "tool", "package", "gone", "shared runtime"])
PASS: shared scripts expand %INSTALLDIR% to Steamworks Shared
PASS: MADEIRA_INSTALL_DEFAULT_KEY=0: entries without a key are ignored
PASS: the sheet's program count
PASS: pending program: batch and a per-session madsync request
PASS: the batch runs only the runnable pending program, after the service step
PASS: session recorded; the choice turns to Skip
PASS: the sheet's note (One-time installs. Runs first: tool. Already done: shared runtime. Installer file missing: gone. Cannot run in this build: runtime a (32-bit installer), package (Windows Installer package). This start uses Wine's standard synchronization instead of madsync; the next start uses madsync again.)
PASS: fusion and per-program log lines
PASS: installers first, then the host, in one session, no quoted tokens
PASS: progress before the batch starts
PASS: progress while running
PASS: not finished while a program runs
PASS: progress when finished
PASS: the end is logged once and its time kept (the starting screen times the host from it)
PASS: finished with failures: how many succeeded, which failed
PASS: a program that exited 0 is recorded in both views at the next start
PASS: a backup of system.reg is kept once
PASS: one summary line
PASS: nothing pending: no batch, madsync untouched, no installs' end
PASS: result file and session list cleared
PASS: Skip starts without the pending program
PASS: Run at next start is saved
PASS: with 32-bit support the 32-bit installer runs
PASS: fusion.dll placed before a start that runs installers
PASS: an existing fusion.dll is never replaced
PASS: a batch that never ran records nothing
PASS: MADEIRA_DOCK_INSTALL_CHOICE=0: runs every start, choice untouched
PASS: MADEIRA_DOCK_INSTALL_SERVER_SYNC=0 with madsync: madsync kept, service step left out
PASS: madsync already off in madeira.cfg: the service step runs without a session request
PASS: no inproc-sync (fastsync, the default engine): the service step runs, no madsync note
PASS: MADEIRA_DOCK_INSTALL_SCM=0: services off
PASS: MADEIRA_DOTNET_FUSION=0 leaves the folder alone
PASS: MADEIRA_DOCK_INSTALLERS=0: nothing runs, nothing is shown
PASS: over the limit: 8 run, the rest next start, choice stays Run
FAILURES: 1
PASS: no redistributable names: nothing is decided by program name
PASS: every installer switch defaults on and reads env.NAME
PASS: switch MADEIRA_DOCK_INSTALLERS is read
PASS: switch MADEIRA_INSTALL_DEFAULT_KEY is read
PASS: switch MADEIRA_DOCK_INSTALL_CHOICE is read
PASS: switch MADEIRA_DOCK_INSTALL_SCM is read
PASS: switch MADEIRA_DOCK_INSTALL_SERVER_SYNC is read
PASS: switch MADEIRA_DOTNET_FUSION is read
PASS: the batch never writes the registry (no reg.exe in the bundle)
PASS: madsync is turned off only for a Dock start that runs installers
PASS: MadeiraDock.swift: does not touch the madsync session switch
PASS: MadeiraDockView.swift: does not touch the madsync session switch
PASS: installers are planned after the launch checks, before the session starts
PASS: the planned batch goes into the launch arguments
PASS: the Dock sheet shows the choice and progress
PASS: new file carries the owner copyright
PASS: production installer Swift compiles on the host
FAIL: installer checks pass under AddressSanitizer
PASS: madsync_enabled() compiles with the production madeira_cfg.h
PASS: no madeira.cfg, no session switch: madsync off (fastsync is the default)
PASS: madsync only with inproc-sync = 1
PASS: inproc-sync = 0 still turns it off
PASS: MADEIRA_MADSYNC_SESSION=0: off for this session, logged
PASS: any other session value leaves madsync on
PASS: the session switch never turns madsync on
SKIP: cmd.exe not reachable; batch flow checked textually only
FAILURES: 1

```

## check-lazy-windows.py

```text
/var/folders/nj/vtw8zd2j31d1gdrtntc5y4600000gn/T/tmpe8vbn8x1/lazy.c:16:65: error: typedef redefinition with different types ('int' vs '__darwin_mach_port_t' (aka 'unsigned int'))
   16 | typedef uint64_t mach_vm_address_t, mach_vm_size_t; typedef int mach_port_t; typedef int *vm_region_info_t;
      |                                                                 ^
/Applications/Xcode_16.4.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_mach_port_t.h:50:30: note: previous definition is here
   50 | typedef __darwin_mach_port_t mach_port_t;
      |                              ^
1 error generated.
PASS: virtual_init and map_view only reach the window code through the lazy gates
Traceback (most recent call last):
  File "/Users/runner/work/madeira-fork-testing/madeira-fork-testing/tests/host/check-lazy-windows.py", line 203, in <module>
    subprocess.run(["cc", "-std=gnu11", "-Wall", "-Wno-unused-function", "-Wno-unused-variable",
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    "-Wno-unused-but-set-variable", "-pthread", "-fsanitize=address,undefined",
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    str(c), "-o", str(exe)], check=True)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/subprocess.py", line 578, in run
    raise CalledProcessError(retcode, process.args,
                             output=stdout, stderr=stderr)
subprocess.CalledProcessError: Command '['cc', '-std=gnu11', '-Wall', '-Wno-unused-function', '-Wno-unused-variable', '-Wno-unused-but-set-variable', '-pthread', '-fsanitize=address,undefined', '/var/folders/nj/vtw8zd2j31d1gdrtntc5y4600000gn/T/tmpe8vbn8x1/lazy.c', '-o', '/var/folders/nj/vtw8zd2j31d1gdrtntc5y4600000gn/T/tmpe8vbn8x1/lazy']' returned non-zero exit status 1.

```

## check-steam-library.py

```text
PASS: SteamInstall.swift: licence header
PASS: SteamInstall.swift is built by the Xcode project
PASS: SteamOwnedLibrary.swift: licence header
PASS: SteamOwnedLibrary.swift is built by the Xcode project
PASS: SteamOwnedLibrary.swift credits Jfishin
PASS: SteamDownloadBackground.swift: licence header
PASS: SteamDownloadBackground.swift is built by the Xcode project
PASS: SteamGames.swift: licence header
PASS: SteamGames.swift is built by the Xcode project
PASS: SwiftSteam/Core/CMServerList.swift: licence header
PASS: SwiftSteam/Core/CMServerList.swift is built by the Xcode project
PASS: SwiftSteam/Core/CMServerList.swift credits Jfishin
PASS: SwiftSteam/Core/LicenseListBox.swift: licence header
PASS: SwiftSteam/Core/LicenseListBox.swift is built by the Xcode project
PASS: SwiftSteam/Core/LicenseListBox.swift credits Jfishin
PASS: SwiftSteam/Core/SteamCMSession.swift: licence header
PASS: SwiftSteam/Core/SteamCMSession.swift is built by the Xcode project
PASS: SwiftSteam/Core/SteamConnection.swift: licence header
PASS: SwiftSteam/Core/SteamConnection.swift is built by the Xcode project
PASS: SwiftSteam/Core/SteamConnection.swift credits Jfishin
PASS: SwiftSteam/Core/SteamMessageCodec.swift: licence header
PASS: SwiftSteam/Core/SteamMessageCodec.swift is built by the Xcode project
PASS: SwiftSteam/Core/SteamMessageCodec.swift credits Jfishin
PASS: SwiftSteam/Core/SteamProtocol.swift: licence header
PASS: SwiftSteam/Core/SteamProtocol.swift is built by the Xcode project
PASS: SwiftSteam/Core/SteamProtocol.swift credits Jfishin
PASS: SwiftSteam/Core/SteamSession.swift: licence header
PASS: SwiftSteam/Core/SteamSession.swift is built by the Xcode project
PASS: SwiftSteam/Core/SteamSession.swift credits Jfishin
PASS: SwiftSteam/Content/ContentDecryptor.swift: licence header
PASS: SwiftSteam/Content/ContentDecryptor.swift is built by the Xcode project
PASS: SwiftSteam/Content/ContentDecryptor.swift credits Jfishin
PASS: SwiftSteam/Content/DepotDownloader.swift: licence header
PASS: SwiftSteam/Content/DepotDownloader.swift is built by the Xcode project
PASS: SwiftSteam/Content/DepotDownloader.swift credits Jfishin
PASS: SwiftSteam/Content/DepotManifest.swift: licence header
PASS: SwiftSteam/Content/DepotManifest.swift is built by the Xcode project
PASS: SwiftSteam/Content/DepotManifest.swift credits Jfishin
PASS: SwiftSteam/Library/SteamAppInfo.swift: licence header
PASS: SwiftSteam/Library/SteamAppInfo.swift is built by the Xcode project
PASS: SwiftSteam/Library/SteamAppInfo.swift credits Jfishin
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: licence header
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift is built by the Xcode project
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift credits Jfishin
PASS: SwiftSteam/Install/AppManifestWriter.swift: licence header
PASS: SwiftSteam/Install/AppManifestWriter.swift is built by the Xcode project
PASS: SwiftSteam/Install/AppManifestWriter.swift credits Jfishin
PASS: SwiftSteam/chunk_zip.c is in the Xcode project
PASS: SwiftSteam/chunk_zip.c is built by the Xcode project
PASS: SwiftSteam/chunk_zip.h is in the Xcode project
PASS: SwiftSteam/lzma_shim.c is in the Xcode project
PASS: SwiftSteam/lzma_shim.c is built by the Xcode project
PASS: SwiftSteam/lzma_shim.h is in the Xcode project
PASS: SwiftSteam/zstd_edu.c is in the Xcode project
PASS: SwiftSteam/zstd_edu.c is built by the Xcode project
PASS: SwiftSteam/zstd_edu.h is in the Xcode project
PASS: liblzma is linked (the system library; nothing is bundled)
PASS: the bridging header imports the decoders
PASS: zstd_edu.c keeps Meta's notice
PASS: the BSD licence text of the zstd decoder is in LICENSES/
PASS: THIRD-PARTY-NOTICES.md lists the zstd decoder and its licence text
PASS: SteamOwnedLibrary.swift: no SteamTokenStore (sign-in tokens stay in SteamSignIn)
PASS: SteamOwnedLibrary.swift: no SecItem (sign-in tokens stay in SteamSignIn)
PASS: SteamOwnedLibrary.swift: no kSecClass (sign-in tokens stay in SteamSignIn)
PASS: SteamOwnedLibrary.swift: no saveTokens (sign-in tokens stay in SteamSignIn)
PASS: SteamOwnedLibrary.swift: no clearTokens (sign-in tokens stay in SteamSignIn)
PASS: SteamOwnedLibrary.swift: no loadTokens (sign-in tokens stay in SteamSignIn)
PASS: SteamOwnedLibrary.swift: no UserDefaults (sign-in tokens stay in SteamSignIn)
PASS: SteamOwnedLibrary.swift: no refreshToken (sign-in tokens stay in SteamSignIn)
PASS: SteamGames.swift: no SteamTokenStore (sign-in tokens stay in SteamSignIn)
PASS: SteamGames.swift: no SecItem (sign-in tokens stay in SteamSignIn)
PASS: SteamGames.swift: no kSecClass (sign-in tokens stay in SteamSignIn)
PASS: SteamGames.swift: no saveTokens (sign-in tokens stay in SteamSignIn)
PASS: SteamGames.swift: no clearTokens (sign-in tokens stay in SteamSignIn)
PASS: SteamGames.swift: no loadTokens (sign-in tokens stay in SteamSignIn)
PASS: SteamGames.swift: no refreshToken (sign-in tokens stay in SteamSignIn)
PASS: SteamInstall.swift: no SteamTokenStore (sign-in tokens stay in SteamSignIn)
PASS: SteamInstall.swift: no SecItem (sign-in tokens stay in SteamSignIn)
PASS: SteamInstall.swift: no kSecClass (sign-in tokens stay in SteamSignIn)
PASS: SteamInstall.swift: no saveTokens (sign-in tokens stay in SteamSignIn)
PASS: SteamInstall.swift: no clearTokens (sign-in tokens stay in SteamSignIn)
PASS: SteamInstall.swift: no loadTokens (sign-in tokens stay in SteamSignIn)
PASS: SteamInstall.swift: no UserDefaults (sign-in tokens stay in SteamSignIn)
PASS: SteamInstall.swift: no refreshToken (sign-in tokens stay in SteamSignIn)
PASS: SteamDownloadBackground.swift: no SteamTokenStore (sign-in tokens stay in SteamSignIn)
PASS: SteamDownloadBackground.swift: no SecItem (sign-in tokens stay in SteamSignIn)
PASS: SteamDownloadBackground.swift: no kSecClass (sign-in tokens stay in SteamSignIn)
PASS: SteamDownloadBackground.swift: no saveTokens (sign-in tokens stay in SteamSignIn)
PASS: SteamDownloadBackground.swift: no clearTokens (sign-in tokens stay in SteamSignIn)
PASS: SteamDownloadBackground.swift: no loadTokens (sign-in tokens stay in SteamSignIn)
PASS: SteamDownloadBackground.swift: no UserDefaults (sign-in tokens stay in SteamSignIn)
PASS: SteamDownloadBackground.swift: no refreshToken (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Core/SteamSession.swift: no SteamTokenStore (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Core/SteamSession.swift: no SecItem (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Core/SteamSession.swift: no kSecClass (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Core/SteamSession.swift: no saveTokens (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Core/SteamSession.swift: no clearTokens (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Core/SteamSession.swift: no loadTokens (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Core/SteamSession.swift: no UserDefaults (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Core/SteamConnection.swift: no SteamTokenStore (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Core/SteamConnection.swift: no SecItem (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Core/SteamConnection.swift: no kSecClass (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Core/SteamConnection.swift: no saveTokens (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Core/SteamConnection.swift: no clearTokens (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Core/SteamConnection.swift: no loadTokens (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Core/SteamConnection.swift: no UserDefaults (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Core/SteamConnection.swift: no refreshToken (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Content/DepotDownloader.swift: no SteamTokenStore (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Content/DepotDownloader.swift: no SecItem (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Content/DepotDownloader.swift: no kSecClass (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Content/DepotDownloader.swift: no saveTokens (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Content/DepotDownloader.swift: no clearTokens (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Content/DepotDownloader.swift: no loadTokens (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Content/DepotDownloader.swift: no UserDefaults (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Content/DepotDownloader.swift: no refreshToken (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no SteamTokenStore (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no SecItem (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no kSecClass (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no saveTokens (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no clearTokens (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no loadTokens (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no UserDefaults (sign-in tokens stay in SteamSignIn)
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no refreshToken (sign-in tokens stay in SteamSignIn)
PASS: the connection logs on with SteamSignIn's stored sign-in
PASS: SteamInstall.swift: no program names
PASS: SteamInstall.swift: no helperNames
PASS: SteamInstall.swift: no steamwebhelper
PASS: SteamInstall.swift: no steam.exe
PASS: SteamInstall.swift: no setenv(
PASS: SteamInstall.swift: no unsetenv(
PASS: SteamInstall.swift: no runWineFullSequence
PASS: SteamInstall.swift: no MADEIRA_EXE
PASS: SteamInstall.swift: no MADEIRA_ARGS
PASS: SteamInstall.swift: no jit_
PASS: SteamInstall.swift: no JITPool
PASS: SteamInstall.swift: no poolSize
PASS: SteamInstall.swift: no FEX_
PASS: SteamInstall.swift: no DXMT
PASS: SteamInstall.swift: no BGTaskScheduler
PASS: SteamInstall.swift: no BGContinuedProcessing
PASS: SteamInstall.swift: no UNUserNotificationCenter
PASS: SteamInstall.swift: no SteamKit2
PASS: SteamInstall.swift: no JavaSteam
PASS: SteamInstall.swift: no DepotDownloader's
PASS: SteamInstall.swift: no port of the DepotDownloader
PASS: SteamInstall.swift: no build-round labels
PASS: SteamOwnedLibrary.swift: no program names
PASS: SteamOwnedLibrary.swift: no helperNames
PASS: SteamOwnedLibrary.swift: no steamwebhelper
PASS: SteamOwnedLibrary.swift: no steam.exe
PASS: SteamOwnedLibrary.swift: no setenv(
PASS: SteamOwnedLibrary.swift: no unsetenv(
PASS: SteamOwnedLibrary.swift: no runWineFullSequence
PASS: SteamOwnedLibrary.swift: no MADEIRA_EXE
PASS: SteamOwnedLibrary.swift: no MADEIRA_ARGS
PASS: SteamOwnedLibrary.swift: no jit_
PASS: SteamOwnedLibrary.swift: no JITPool
PASS: SteamOwnedLibrary.swift: no poolSize
PASS: SteamOwnedLibrary.swift: no FEX_
PASS: SteamOwnedLibrary.swift: no DXMT
PASS: SteamOwnedLibrary.swift: no BGTaskScheduler
PASS: SteamOwnedLibrary.swift: no BGContinuedProcessing
PASS: SteamOwnedLibrary.swift: no UNUserNotificationCenter
PASS: SteamOwnedLibrary.swift: no SteamKit2
PASS: SteamOwnedLibrary.swift: no JavaSteam
PASS: SteamOwnedLibrary.swift: no DepotDownloader's
PASS: SteamOwnedLibrary.swift: no port of the DepotDownloader
PASS: SteamOwnedLibrary.swift: no build-round labels
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-library] start signed-in=\(signedIn ? 1 : 0) ca"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-library] signed out: list cleared")"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-library] owned apps=\(apps.count) windows-insta"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-start] launch configuration app=\(appID) entrie"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-account] stored sign-in rejected code=\(code)")"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-\(context)] failed reason=\(Self.reason(error))"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-playtime] apps=\(parsed.count)")"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-playtime] unavailable reason=\(Self.reason(erro"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-cloud] sync games=\(games.count) automatic=\(Se"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-cloud] app=\(appID) \(audit.summary) patterns=\"
PASS: SteamOwnedLibrary.swift: no account data or path in "if let elsewhere = result.1 { SteamLog.event("[steam-cloud] app=\(appI"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-cloud] app=\(appID) failed reason=\(Self.reason"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-cloud] app=\(appID) choice=\(useCloud ? "cloud""
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-cloud] app=\(appID) downloaded files=\(done) ba"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-cloud] app=\(appID) download failed after=\(don"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-cloud] app=\(appID) cloud copies backed up befo"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-cloud] app=\(appID) upload part failed reason=\"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-cloud] app=\(appID) upload file=\(done + 1)/\(w"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-cloud] app=\(appID) uploaded files=\(done) bloc"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-cloud] app=\(appID) upload failed after=\(done)"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-cloud] app=\(appID) before-play sync result=\(h"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-cloud] app=\(appID) quit-upload: connection reo"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-cloud] app=\(appID) quit-upload: check failed")"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-cloud] app=\(appID) quit-upload: held, conflict"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-cloud] app=\(appID) quit-upload: nothing to upl"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-cloud] app=\(appID) quit-upload: uploaded=\(wan"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-depot] paused for a game session count=\(resume"
PASS: SteamOwnedLibrary.swift: no account data or path in "if !resume.isEmpty { SteamLog.event("[steam-depot] resumed after a gam"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-library] connection closed for Madeira Dock")"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-depot] paused for the background count=\(resume"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-depot] resumed after the background count=\(ids"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-depot] cancelled app=\(appID) partial-files-rem"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-repair] app=\(appID) requested=1")"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-depot] uninstalled app=\(id)")"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-depot] library entry app=\(appID)")"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-depot] paused app=\(appID)")"
PASS: SteamOwnedLibrary.swift: no account data or path in "SteamLog.event("[steam-depot] failed app=\(appID) reason=\(Self.reason"
PASS: SteamDownloadBackground.swift: no program names
PASS: SteamDownloadBackground.swift: no helperNames
PASS: SteamDownloadBackground.swift: no steamwebhelper
PASS: SteamDownloadBackground.swift: no steam.exe
PASS: SteamDownloadBackground.swift: no setenv(
PASS: SteamDownloadBackground.swift: no unsetenv(
PASS: SteamDownloadBackground.swift: no runWineFullSequence
PASS: SteamDownloadBackground.swift: no MADEIRA_EXE
PASS: SteamDownloadBackground.swift: no MADEIRA_ARGS
PASS: SteamDownloadBackground.swift: no jit_
PASS: SteamDownloadBackground.swift: no JITPool
PASS: SteamDownloadBackground.swift: no poolSize
PASS: SteamDownloadBackground.swift: no FEX_
PASS: SteamDownloadBackground.swift: no DXMT
PASS: SteamDownloadBackground.swift: no SteamKit2
PASS: SteamDownloadBackground.swift: no JavaSteam
PASS: SteamDownloadBackground.swift: no DepotDownloader's
PASS: SteamDownloadBackground.swift: no port of the DepotDownloader
PASS: SteamDownloadBackground.swift: no build-round labels
PASS: SteamDownloadBackground.swift: no account data or path in "SteamLog.event("[bg-download] " + line)"
PASS: SteamGames.swift: no program names
PASS: SteamGames.swift: no helperNames
PASS: SteamGames.swift: no steamwebhelper
PASS: SteamGames.swift: no steam.exe
PASS: SteamGames.swift: no setenv(
PASS: SteamGames.swift: no unsetenv(
PASS: SteamGames.swift: no runWineFullSequence
PASS: SteamGames.swift: no MADEIRA_EXE
PASS: SteamGames.swift: no MADEIRA_ARGS
PASS: SteamGames.swift: no jit_
PASS: SteamGames.swift: no JITPool
PASS: SteamGames.swift: no poolSize
PASS: SteamGames.swift: no FEX_
PASS: SteamGames.swift: no DXMT
PASS: SteamGames.swift: no BGTaskScheduler
PASS: SteamGames.swift: no BGContinuedProcessing
PASS: SteamGames.swift: no UNUserNotificationCenter
PASS: SteamGames.swift: no SteamKit2
PASS: SteamGames.swift: no JavaSteam
PASS: SteamGames.swift: no DepotDownloader's
PASS: SteamGames.swift: no port of the DepotDownloader
PASS: SteamGames.swift: no build-round labels
PASS: SteamGames.swift: no account data or path in "LogStore.shared.log("[steam-games] installed=\(found.count) ready=\(fo"
PASS: SteamGames.swift: no account data or path in "LogStore.shared.log("[steam-cloud] app=\(appID) quit-upload done files"
PASS: SteamGames.swift: no account data or path in "SteamLog.event("[steam-cloud] setting on=\(on ? 1 : 0)")"
PASS: SteamGames.swift: no account data or path in "LogStore.shared.log("[steam-start] app=\(entry.steamAppID ?? 0) mode=\"
PASS: SteamGames.swift: no account data or path in "LogStore.shared.log("[steam-start] app=\(entry.steamAppID ?? 0) progra"
PASS: SteamGames.swift: no account data or path in "LogStore.shared.log("[steam-start] app=\(appID) launch-entries=\(optio"
PASS: SwiftSteam/Core/CMServerList.swift: no program names
PASS: SwiftSteam/Core/CMServerList.swift: no helperNames
PASS: SwiftSteam/Core/CMServerList.swift: no steamwebhelper
PASS: SwiftSteam/Core/CMServerList.swift: no steam.exe
PASS: SwiftSteam/Core/CMServerList.swift: no setenv(
PASS: SwiftSteam/Core/CMServerList.swift: no unsetenv(
PASS: SwiftSteam/Core/CMServerList.swift: no runWineFullSequence
PASS: SwiftSteam/Core/CMServerList.swift: no MADEIRA_EXE
PASS: SwiftSteam/Core/CMServerList.swift: no MADEIRA_ARGS
PASS: SwiftSteam/Core/CMServerList.swift: no jit_
PASS: SwiftSteam/Core/CMServerList.swift: no JITPool
PASS: SwiftSteam/Core/CMServerList.swift: no poolSize
PASS: SwiftSteam/Core/CMServerList.swift: no FEX_
PASS: SwiftSteam/Core/CMServerList.swift: no DXMT
PASS: SwiftSteam/Core/CMServerList.swift: no BGTaskScheduler
PASS: SwiftSteam/Core/CMServerList.swift: no BGContinuedProcessing
PASS: SwiftSteam/Core/CMServerList.swift: no UNUserNotificationCenter
PASS: SwiftSteam/Core/CMServerList.swift: no SteamKit2
PASS: SwiftSteam/Core/CMServerList.swift: no JavaSteam
PASS: SwiftSteam/Core/CMServerList.swift: no DepotDownloader's
PASS: SwiftSteam/Core/CMServerList.swift: no port of the DepotDownloader
PASS: SwiftSteam/Core/CMServerList.swift: no build-round labels
PASS: SwiftSteam/Core/CMServerList.swift: no account data or path in "SteamLog.trace("CM directory unavailable, using cached servers")"
PASS: SwiftSteam/Core/CMServerList.swift: no account data or path in "SteamLog.trace("Fetched \(servers.count) WebSocket CM servers")"
PASS: SwiftSteam/Core/LicenseListBox.swift: no program names
PASS: SwiftSteam/Core/LicenseListBox.swift: no helperNames
PASS: SwiftSteam/Core/LicenseListBox.swift: no steamwebhelper
PASS: SwiftSteam/Core/LicenseListBox.swift: no steam.exe
PASS: SwiftSteam/Core/LicenseListBox.swift: no setenv(
PASS: SwiftSteam/Core/LicenseListBox.swift: no unsetenv(
PASS: SwiftSteam/Core/LicenseListBox.swift: no runWineFullSequence
PASS: SwiftSteam/Core/LicenseListBox.swift: no MADEIRA_EXE
PASS: SwiftSteam/Core/LicenseListBox.swift: no MADEIRA_ARGS
PASS: SwiftSteam/Core/LicenseListBox.swift: no jit_
PASS: SwiftSteam/Core/LicenseListBox.swift: no JITPool
PASS: SwiftSteam/Core/LicenseListBox.swift: no poolSize
PASS: SwiftSteam/Core/LicenseListBox.swift: no FEX_
PASS: SwiftSteam/Core/LicenseListBox.swift: no DXMT
PASS: SwiftSteam/Core/LicenseListBox.swift: no BGTaskScheduler
PASS: SwiftSteam/Core/LicenseListBox.swift: no BGContinuedProcessing
PASS: SwiftSteam/Core/LicenseListBox.swift: no UNUserNotificationCenter
PASS: SwiftSteam/Core/LicenseListBox.swift: no SteamKit2
PASS: SwiftSteam/Core/LicenseListBox.swift: no JavaSteam
PASS: SwiftSteam/Core/LicenseListBox.swift: no DepotDownloader's
PASS: SwiftSteam/Core/LicenseListBox.swift: no port of the DepotDownloader
PASS: SwiftSteam/Core/LicenseListBox.swift: no build-round labels
PASS: SwiftSteam/Core/SteamCMSession.swift: no program names
PASS: SwiftSteam/Core/SteamCMSession.swift: no helperNames
PASS: SwiftSteam/Core/SteamCMSession.swift: no steamwebhelper
PASS: SwiftSteam/Core/SteamCMSession.swift: no steam.exe
PASS: SwiftSteam/Core/SteamCMSession.swift: no setenv(
PASS: SwiftSteam/Core/SteamCMSession.swift: no unsetenv(
PASS: SwiftSteam/Core/SteamCMSession.swift: no runWineFullSequence
PASS: SwiftSteam/Core/SteamCMSession.swift: no MADEIRA_EXE
PASS: SwiftSteam/Core/SteamCMSession.swift: no MADEIRA_ARGS
PASS: SwiftSteam/Core/SteamCMSession.swift: no jit_
PASS: SwiftSteam/Core/SteamCMSession.swift: no JITPool
PASS: SwiftSteam/Core/SteamCMSession.swift: no poolSize
PASS: SwiftSteam/Core/SteamCMSession.swift: no FEX_
PASS: SwiftSteam/Core/SteamCMSession.swift: no DXMT
PASS: SwiftSteam/Core/SteamCMSession.swift: no BGTaskScheduler
PASS: SwiftSteam/Core/SteamCMSession.swift: no BGContinuedProcessing
PASS: SwiftSteam/Core/SteamCMSession.swift: no UNUserNotificationCenter
PASS: SwiftSteam/Core/SteamCMSession.swift: no SteamKit2
PASS: SwiftSteam/Core/SteamCMSession.swift: no JavaSteam
PASS: SwiftSteam/Core/SteamCMSession.swift: no DepotDownloader's
PASS: SwiftSteam/Core/SteamCMSession.swift: no port of the DepotDownloader
PASS: SwiftSteam/Core/SteamCMSession.swift: no build-round labels
PASS: SwiftSteam/Core/SteamConnection.swift: no program names
PASS: SwiftSteam/Core/SteamConnection.swift: no helperNames
PASS: SwiftSteam/Core/SteamConnection.swift: no steamwebhelper
PASS: SwiftSteam/Core/SteamConnection.swift: no steam.exe
PASS: SwiftSteam/Core/SteamConnection.swift: no setenv(
PASS: SwiftSteam/Core/SteamConnection.swift: no unsetenv(
PASS: SwiftSteam/Core/SteamConnection.swift: no runWineFullSequence
PASS: SwiftSteam/Core/SteamConnection.swift: no MADEIRA_EXE
PASS: SwiftSteam/Core/SteamConnection.swift: no MADEIRA_ARGS
PASS: SwiftSteam/Core/SteamConnection.swift: no jit_
PASS: SwiftSteam/Core/SteamConnection.swift: no JITPool
PASS: SwiftSteam/Core/SteamConnection.swift: no poolSize
PASS: SwiftSteam/Core/SteamConnection.swift: no FEX_
PASS: SwiftSteam/Core/SteamConnection.swift: no DXMT
PASS: SwiftSteam/Core/SteamConnection.swift: no BGTaskScheduler
PASS: SwiftSteam/Core/SteamConnection.swift: no BGContinuedProcessing
PASS: SwiftSteam/Core/SteamConnection.swift: no UNUserNotificationCenter
PASS: SwiftSteam/Core/SteamConnection.swift: no SteamKit2
PASS: SwiftSteam/Core/SteamConnection.swift: no JavaSteam
PASS: SwiftSteam/Core/SteamConnection.swift: no DepotDownloader's
PASS: SwiftSteam/Core/SteamConnection.swift: no port of the DepotDownloader
PASS: SwiftSteam/Core/SteamConnection.swift: no build-round labels
PASS: SwiftSteam/Core/SteamConnection.swift: no account data or path in "SteamLog.trace("WS handshake complete — server protocol: \(`protocol` "
PASS: SwiftSteam/Core/SteamConnection.swift: no account data or path in "SteamLog.trace("WS server closed — code: \(closeCode.rawValue) reason:"
PASS: SwiftSteam/Core/SteamConnection.swift: no account data or path in "SteamLog.trace("WS task completed with error: \(error.localizedDescrip"
PASS: SwiftSteam/Core/SteamConnection.swift: no account data or path in "SteamLog.trace("Connecting to CM: \(server.url)")"
PASS: SwiftSteam/Core/SteamConnection.swift: no account data or path in "SteamLog.trace("WebSocket connected — ready for protocol messages")"
PASS: SwiftSteam/Core/SteamConnection.swift: no account data or path in "SteamLog.trace("unexpected text frame (\(text.utf8.count) bytes)")"
PASS: SwiftSteam/Core/SteamConnection.swift: no account data or path in "SteamLog.trace("WS receive error: \(error.localizedDescription)")"
PASS: SwiftSteam/Core/SteamConnection.swift: no account data or path in "SteamLog.trace("Connection lost: \(error.localizedDescription)")"
PASS: SwiftSteam/Core/SteamConnection.swift: no account data or path in "SteamLog.trace("Connection closed cleanly")"
PASS: SwiftSteam/Core/SteamConnection.swift: no account data or path in "SteamLog.trace("Disconnected")"
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no program names
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no helperNames
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no steamwebhelper
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no steam.exe
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no setenv(
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no unsetenv(
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no runWineFullSequence
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no MADEIRA_EXE
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no MADEIRA_ARGS
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no jit_
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no JITPool
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no poolSize
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no FEX_
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no DXMT
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no BGTaskScheduler
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no BGContinuedProcessing
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no UNUserNotificationCenter
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no SteamKit2
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no JavaSteam
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no DepotDownloader's
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no port of the DepotDownloader
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no build-round labels
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no account data or path in "SteamLog.trace("Message too small (\(data.count) bytes)")"
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no account data or path in "SteamLog.trace("Invalid protobuf header length \(headerLength) for \(d"
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no account data or path in "SteamLog.trace("Unknown protobuf EMsg \(eMsgValue) (\(body.count) byte"
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no account data or path in "SteamLog.trace("Non-protobuf message too small: \(data.count) bytes (E"
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no account data or path in "SteamLog.trace("Non-protobuf message smaller than header: \(data.count"
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no account data or path in "SteamLog.trace("Non-protobuf EMsg \(eMsgValue) (header=\(headerSize)B,"
PASS: SwiftSteam/Core/SteamProtocol.swift: no program names
PASS: SwiftSteam/Core/SteamProtocol.swift: no helperNames
PASS: SwiftSteam/Core/SteamProtocol.swift: no steamwebhelper
PASS: SwiftSteam/Core/SteamProtocol.swift: no steam.exe
PASS: SwiftSteam/Core/SteamProtocol.swift: no setenv(
PASS: SwiftSteam/Core/SteamProtocol.swift: no unsetenv(
PASS: SwiftSteam/Core/SteamProtocol.swift: no runWineFullSequence
PASS: SwiftSteam/Core/SteamProtocol.swift: no MADEIRA_EXE
PASS: SwiftSteam/Core/SteamProtocol.swift: no MADEIRA_ARGS
PASS: SwiftSteam/Core/SteamProtocol.swift: no jit_
PASS: SwiftSteam/Core/SteamProtocol.swift: no JITPool
PASS: SwiftSteam/Core/SteamProtocol.swift: no poolSize
PASS: SwiftSteam/Core/SteamProtocol.swift: no FEX_
PASS: SwiftSteam/Core/SteamProtocol.swift: no DXMT
PASS: SwiftSteam/Core/SteamProtocol.swift: no BGTaskScheduler
PASS: SwiftSteam/Core/SteamProtocol.swift: no BGContinuedProcessing
PASS: SwiftSteam/Core/SteamProtocol.swift: no UNUserNotificationCenter
PASS: SwiftSteam/Core/SteamProtocol.swift: no SteamKit2
PASS: SwiftSteam/Core/SteamProtocol.swift: no JavaSteam
PASS: SwiftSteam/Core/SteamProtocol.swift: no DepotDownloader's
PASS: SwiftSteam/Core/SteamProtocol.swift: no port of the DepotDownloader
PASS: SwiftSteam/Core/SteamProtocol.swift: no build-round labels
PASS: SwiftSteam/Core/SteamSession.swift: no program names
PASS: SwiftSteam/Core/SteamSession.swift: no helperNames
PASS: SwiftSteam/Core/SteamSession.swift: no steamwebhelper
PASS: SwiftSteam/Core/SteamSession.swift: no steam.exe
PASS: SwiftSteam/Core/SteamSession.swift: no setenv(
PASS: SwiftSteam/Core/SteamSession.swift: no unsetenv(
PASS: SwiftSteam/Core/SteamSession.swift: no runWineFullSequence
PASS: SwiftSteam/Core/SteamSession.swift: no MADEIRA_EXE
PASS: SwiftSteam/Core/SteamSession.swift: no MADEIRA_ARGS
PASS: SwiftSteam/Core/SteamSession.swift: no jit_
PASS: SwiftSteam/Core/SteamSession.swift: no JITPool
PASS: SwiftSteam/Core/SteamSession.swift: no poolSize
PASS: SwiftSteam/Core/SteamSession.swift: no FEX_
PASS: SwiftSteam/Core/SteamSession.swift: no DXMT
PASS: SwiftSteam/Core/SteamSession.swift: no BGTaskScheduler
PASS: SwiftSteam/Core/SteamSession.swift: no BGContinuedProcessing
PASS: SwiftSteam/Core/SteamSession.swift: no UNUserNotificationCenter
PASS: SwiftSteam/Core/SteamSession.swift: no SteamKit2
PASS: SwiftSteam/Core/SteamSession.swift: no JavaSteam
PASS: SwiftSteam/Core/SteamSession.swift: no DepotDownloader's
PASS: SwiftSteam/Core/SteamSession.swift: no port of the DepotDownloader
PASS: SwiftSteam/Core/SteamSession.swift: no build-round labels
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("ClientLicenseList: parsed \(packageIDs.count) packages"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("ClientLicenseList deserialize FAILED (body \(message.b"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("Sent ClientHello (\(helloData.count) bytes)")"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("Logon attempt \(attempt)/2 — reconnecting to different"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("Sent ClientHello to new server (attempt \(attempt))")"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("TryAnotherCM on attempt \(attempt) — will try differen"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("Timeout on attempt \(attempt) — will try different ser"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("Idle timeout — disconnecting to release the server-sid"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("ClientLogonResponse: eresult=\(eResultCode)")"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("Server says TryAnotherCM — will reconnect to different"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("Logon completed during a game session: logged off agai"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("Authenticated")"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("Got ClientLoggedOff during logon")"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("Sent ClientLogon, waiting for response")"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("ClientLogon timed out after 20s: no response from the "
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("Session disconnected")"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("\(method.rawValue) header eresult=\(response.header.er"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("Failed to decode message (\(data.count) bytes): \(erro"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("← \(Self.messageName(message.rawEMsg)) (\(message.body"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("ServiceMethodResponse not matched: jobTarget=\(message"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("Failed to decompress multi message")"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("Failed to parse multi message: \(error)")"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("Received ClientLoggedOff")"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("Late ClientLogOnResponse: eresult=\(eResult)\(label)")"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("Unhandled EMsg \(message.rawEMsg) (\(message.body.coun"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("Heartbeat failed: \(error)")"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("Connection lost\(error.map { ": \($0.localizedDescript"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("Reconnecting in \(Int(delay))s (attempt \(reconnectAtt"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("Reconnected successfully")"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("Reconnection failed: \(error)")"
PASS: SwiftSteam/Core/SteamSession.swift: no account data or path in "SteamLog.trace("Max reconnection attempts reached")"
PASS: SwiftSteam/Content/ContentDecryptor.swift: no program names
PASS: SwiftSteam/Content/ContentDecryptor.swift: no helperNames
PASS: SwiftSteam/Content/ContentDecryptor.swift: no steamwebhelper
PASS: SwiftSteam/Content/ContentDecryptor.swift: no steam.exe
PASS: SwiftSteam/Content/ContentDecryptor.swift: no setenv(
PASS: SwiftSteam/Content/ContentDecryptor.swift: no unsetenv(
PASS: SwiftSteam/Content/ContentDecryptor.swift: no runWineFullSequence
PASS: SwiftSteam/Content/ContentDecryptor.swift: no MADEIRA_EXE
PASS: SwiftSteam/Content/ContentDecryptor.swift: no MADEIRA_ARGS
PASS: SwiftSteam/Content/ContentDecryptor.swift: no jit_
PASS: SwiftSteam/Content/ContentDecryptor.swift: no JITPool
PASS: SwiftSteam/Content/ContentDecryptor.swift: no poolSize
PASS: SwiftSteam/Content/ContentDecryptor.swift: no FEX_
PASS: SwiftSteam/Content/ContentDecryptor.swift: no DXMT
PASS: SwiftSteam/Content/ContentDecryptor.swift: no BGTaskScheduler
PASS: SwiftSteam/Content/ContentDecryptor.swift: no BGContinuedProcessing
PASS: SwiftSteam/Content/ContentDecryptor.swift: no UNUserNotificationCenter
PASS: SwiftSteam/Content/ContentDecryptor.swift: no SteamKit2
PASS: SwiftSteam/Content/ContentDecryptor.swift: no JavaSteam
PASS: SwiftSteam/Content/ContentDecryptor.swift: no DepotDownloader's
PASS: SwiftSteam/Content/ContentDecryptor.swift: no port of the DepotDownloader
PASS: SwiftSteam/Content/ContentDecryptor.swift: no build-round labels
PASS: SwiftSteam/Content/DepotDownloader.swift: no program names
PASS: SwiftSteam/Content/DepotDownloader.swift: no helperNames
PASS: SwiftSteam/Content/DepotDownloader.swift: no steamwebhelper
PASS: SwiftSteam/Content/DepotDownloader.swift: no steam.exe
PASS: SwiftSteam/Content/DepotDownloader.swift: no setenv(
PASS: SwiftSteam/Content/DepotDownloader.swift: no unsetenv(
PASS: SwiftSteam/Content/DepotDownloader.swift: no runWineFullSequence
PASS: SwiftSteam/Content/DepotDownloader.swift: no MADEIRA_EXE
PASS: SwiftSteam/Content/DepotDownloader.swift: no MADEIRA_ARGS
PASS: SwiftSteam/Content/DepotDownloader.swift: no jit_
PASS: SwiftSteam/Content/DepotDownloader.swift: no JITPool
PASS: SwiftSteam/Content/DepotDownloader.swift: no poolSize
PASS: SwiftSteam/Content/DepotDownloader.swift: no FEX_
PASS: SwiftSteam/Content/DepotDownloader.swift: no DXMT
PASS: SwiftSteam/Content/DepotDownloader.swift: no BGTaskScheduler
PASS: SwiftSteam/Content/DepotDownloader.swift: no BGContinuedProcessing
PASS: SwiftSteam/Content/DepotDownloader.swift: no UNUserNotificationCenter
PASS: SwiftSteam/Content/DepotDownloader.swift: no SteamKit2
PASS: SwiftSteam/Content/DepotDownloader.swift: no JavaSteam
PASS: SwiftSteam/Content/DepotDownloader.swift: no DepotDownloader's
PASS: SwiftSteam/Content/DepotDownloader.swift: no port of the DepotDownloader
PASS: SwiftSteam/Content/DepotDownloader.swift: no build-round labels
PASS: SwiftSteam/Content/DepotDownloader.swift: no account data or path in "SteamLog.event("[steam-depot] selection app=\(app.appID) build=\(app.b"
PASS: SwiftSteam/Content/DepotDownloader.swift: no account data or path in "SteamLog.event("[steam-depot] license app=\(app.appID) skipped=\(licen"
PASS: SwiftSteam/Content/DepotDownloader.swift: no account data or path in "SteamLog.event("[steam-depot] install begin app=\(app.appID) depots=\("
PASS: SwiftSteam/Content/DepotDownloader.swift: no account data or path in "if !custom.isEmpty { SteamLog.event("[steam-record] custom-executables"
PASS: SwiftSteam/Content/DepotDownloader.swift: no account data or path in "SteamLog.event("[steam-shared-record] app=\(app.appID) shared=\(shared"
PASS: SwiftSteam/Content/DepotDownloader.swift: no account data or path in "SteamLog.event("[steam-depot] install complete app=\(app.appID) bytes="
PASS: SwiftSteam/Content/DepotDownloader.swift: no account data or path in "if file.flags & 0x200 == 0 { SteamLog.trace("rejected manifest path in"
PASS: SwiftSteam/Content/DepotDownloader.swift: no account data or path in "SteamLog.trace("chunk attempt \(attempt + 1) failed: \(failureReason(e"
PASS: SwiftSteam/Content/DepotDownloader.swift: no account data or path in "SteamLog.trace("manifest from a content server failed: \(error.localiz"
PASS: SwiftSteam/Content/DepotDownloader.swift: no account data or path in "SteamLog.event("[steam-depot] depot-key refused app=\(appID) depot=\(d"
PASS: SwiftSteam/Content/DepotDownloader.swift: no account data or path in "SteamLog.event("[steam-cdn] offered=\(servers.count) usable=\(hosts.co"
PASS: SwiftSteam/Content/DepotDownloader.swift: no account data or path in "SteamLog.trace("content directory failed: \(error.localizedDescription"
PASS: SwiftSteam/Content/DepotDownloader.swift: no account data or path in "SteamLog.trace("content authorization request failed; continuing witho"
PASS: SwiftSteam/Content/DepotDownloader.swift: no account data or path in "DispatchQueue.main.async { SteamLog.event("[steam-cdn] host demoted ho"
PASS: SwiftSteam/Content/DepotManifest.swift: no program names
PASS: SwiftSteam/Content/DepotManifest.swift: no helperNames
PASS: SwiftSteam/Content/DepotManifest.swift: no steamwebhelper
PASS: SwiftSteam/Content/DepotManifest.swift: no steam.exe
PASS: SwiftSteam/Content/DepotManifest.swift: no setenv(
PASS: SwiftSteam/Content/DepotManifest.swift: no unsetenv(
PASS: SwiftSteam/Content/DepotManifest.swift: no runWineFullSequence
PASS: SwiftSteam/Content/DepotManifest.swift: no MADEIRA_EXE
PASS: SwiftSteam/Content/DepotManifest.swift: no MADEIRA_ARGS
PASS: SwiftSteam/Content/DepotManifest.swift: no jit_
PASS: SwiftSteam/Content/DepotManifest.swift: no JITPool
PASS: SwiftSteam/Content/DepotManifest.swift: no poolSize
PASS: SwiftSteam/Content/DepotManifest.swift: no FEX_
PASS: SwiftSteam/Content/DepotManifest.swift: no DXMT
PASS: SwiftSteam/Content/DepotManifest.swift: no BGTaskScheduler
PASS: SwiftSteam/Content/DepotManifest.swift: no BGContinuedProcessing
PASS: SwiftSteam/Content/DepotManifest.swift: no UNUserNotificationCenter
PASS: SwiftSteam/Content/DepotManifest.swift: no SteamKit2
PASS: SwiftSteam/Content/DepotManifest.swift: no JavaSteam
PASS: SwiftSteam/Content/DepotManifest.swift: no DepotDownloader's
PASS: SwiftSteam/Content/DepotManifest.swift: no port of the DepotDownloader
PASS: SwiftSteam/Content/DepotManifest.swift: no build-round labels
PASS: SwiftSteam/Content/DepotManifest.swift: no account data or path in "SteamLog.trace("filename decrypt failed (\(why))")"
PASS: SwiftSteam/Library/SteamAppInfo.swift: no program names
PASS: SwiftSteam/Library/SteamAppInfo.swift: no helperNames
PASS: SwiftSteam/Library/SteamAppInfo.swift: no steamwebhelper
PASS: SwiftSteam/Library/SteamAppInfo.swift: no steam.exe
PASS: SwiftSteam/Library/SteamAppInfo.swift: no setenv(
PASS: SwiftSteam/Library/SteamAppInfo.swift: no unsetenv(
PASS: SwiftSteam/Library/SteamAppInfo.swift: no runWineFullSequence
PASS: SwiftSteam/Library/SteamAppInfo.swift: no MADEIRA_EXE
PASS: SwiftSteam/Library/SteamAppInfo.swift: no MADEIRA_ARGS
PASS: SwiftSteam/Library/SteamAppInfo.swift: no jit_
PASS: SwiftSteam/Library/SteamAppInfo.swift: no JITPool
PASS: SwiftSteam/Library/SteamAppInfo.swift: no poolSize
PASS: SwiftSteam/Library/SteamAppInfo.swift: no FEX_
PASS: SwiftSteam/Library/SteamAppInfo.swift: no DXMT
PASS: SwiftSteam/Library/SteamAppInfo.swift: no BGTaskScheduler
PASS: SwiftSteam/Library/SteamAppInfo.swift: no BGContinuedProcessing
PASS: SwiftSteam/Library/SteamAppInfo.swift: no UNUserNotificationCenter
PASS: SwiftSteam/Library/SteamAppInfo.swift: no SteamKit2
PASS: SwiftSteam/Library/SteamAppInfo.swift: no JavaSteam
PASS: SwiftSteam/Library/SteamAppInfo.swift: no DepotDownloader's
PASS: SwiftSteam/Library/SteamAppInfo.swift: no port of the DepotDownloader
PASS: SwiftSteam/Library/SteamAppInfo.swift: no build-round labels
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no program names
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no helperNames
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no steamwebhelper
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no steam.exe
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no setenv(
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no unsetenv(
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no runWineFullSequence
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no MADEIRA_EXE
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no MADEIRA_ARGS
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no jit_
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no JITPool
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no poolSize
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no FEX_
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no DXMT
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no BGTaskScheduler
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no BGContinuedProcessing
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no UNUserNotificationCenter
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no SteamKit2
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no JavaSteam
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no DepotDownloader's
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no port of the DepotDownloader
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no build-round labels
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no account data or path in "SteamLog.trace("Fetching license list...")"
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no account data or path in "SteamLog.trace("Got \(packageIDs.count) owned packages")"
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no account data or path in "SteamLog.trace("Found \(appIDs.count) unique app IDs")"
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no account data or path in "SteamLog.trace("Got info for \(appInfos.count) apps")"
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no account data or path in "SteamLog.trace("\(games.count) of \(appInfos.count) apps are playable "
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no account data or path in "SteamLog.event("[steam-shared] app=\(appID) owners=\(visited.count - 1"
PASS: SwiftSteam/Install/AppManifestWriter.swift: no program names
PASS: SwiftSteam/Install/AppManifestWriter.swift: no helperNames
PASS: SwiftSteam/Install/AppManifestWriter.swift: no steamwebhelper
PASS: SwiftSteam/Install/AppManifestWriter.swift: no steam.exe
PASS: SwiftSteam/Install/AppManifestWriter.swift: no setenv(
PASS: SwiftSteam/Install/AppManifestWriter.swift: no unsetenv(
PASS: SwiftSteam/Install/AppManifestWriter.swift: no runWineFullSequence
PASS: SwiftSteam/Install/AppManifestWriter.swift: no MADEIRA_EXE
PASS: SwiftSteam/Install/AppManifestWriter.swift: no MADEIRA_ARGS
PASS: SwiftSteam/Install/AppManifestWriter.swift: no jit_
PASS: SwiftSteam/Install/AppManifestWriter.swift: no JITPool
PASS: SwiftSteam/Install/AppManifestWriter.swift: no poolSize
PASS: SwiftSteam/Install/AppManifestWriter.swift: no FEX_
PASS: SwiftSteam/Install/AppManifestWriter.swift: no DXMT
PASS: SwiftSteam/Install/AppManifestWriter.swift: no BGTaskScheduler
PASS: SwiftSteam/Install/AppManifestWriter.swift: no BGContinuedProcessing
PASS: SwiftSteam/Install/AppManifestWriter.swift: no UNUserNotificationCenter
PASS: SwiftSteam/Install/AppManifestWriter.swift: no SteamKit2
PASS: SwiftSteam/Install/AppManifestWriter.swift: no JavaSteam
PASS: SwiftSteam/Install/AppManifestWriter.swift: no DepotDownloader's
PASS: SwiftSteam/Install/AppManifestWriter.swift: no port of the DepotDownloader
PASS: SwiftSteam/Install/AppManifestWriter.swift: no build-round labels
PASS: one switch, MADEIRA_STEAM_LIBRARY, on by default
PASS: Info.plist permits only the bundle's own .download.* (background downloads) and .pairing.* (JIT pairing) tasks
PASS: Info.plist asks for no background mode
PASS: the continued-processing task uses the permitted identifier, made concrete
PASS: background downloads and notifications each have a switch, on by default
PASS: iOS 26 continues in the background; otherwise the grace period ends in a clean pause
PASS: every download reports its start, progress and outcome
PASS: a session start pauses downloads and closes the Steam connection (one call, in runWineFullSequence)
PASS: Dock start: the app connection closes, then the sign-in is read and handed over, then the session starts
PASS: the sign-in is read and written once, after the connection closed
PASS: a failed Dock start gives the connection back
PASS: the connection may come back only when the Dock host's report or session is over
PASS: prepareDock pauses downloads, waits for the running one, then waits for the connection to close
PASS: a session ending reopens the connection only through the gate (never while Dock holds the account)
PASS: suspend: no reconnect from here on, log off, then wait for the socket to close
PASS: a logon that completes after suspend() logs straight off again
PASS: downloads go into Madeira Dock's own Steam library folder (SteamRuntimeFiles.relativeRoot + /steamapps)
PASS: the download logs App IDs and depot IDs
PASS: the downloader has no switches of its own
PASS: Dock's validation reads the install record (StateFlags)
FAIL: cc_shim.c compiles on the host
/var/folders/nj/vtw8zd2j31d1gdrtntc5y4600000gn/T/madeira-steam-library-qa5yp0q9/shim/CommonCrypto/cc_shim.c:3:10: fatal error: 'openssl/evp.h' file not found
    3 | #include <openssl/evp.h>
      |          ^~~~~~~~~~~~~~~
1 error generated.
PASS: compression_shim.c compiles on the host
PASS: zstd_edu.c compiles on the host
PASS: lzma_shim.c compiles on the host
PASS: chunk_zip.c compiles on the host
FAIL: the production Steam library, download and decoder code compile on the host
/Applications/Xcode_16.4.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.sdk/usr/include/module.modulemap:4:1: note: in file included from /Applications/Xcode_16.4.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.sdk/usr/include/module.modulemap:4:
  2 | extern module AppleTextureEncoder "AppleTextureEncoder.modulemap"
  3 | extern module asl "asl.modulemap"
  4 | extern module Compression "compression.modulemap"
    | `- note: in file included from /Applications/Xcode_16.4.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.sdk/usr/include/module.modulemap:4:
  5 | extern module CUPS "cups.modulemap"
  6 | extern module dnssd "dnssd.modulemap"

/Applications/Xcode_16.4.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.sdk/usr/include/compression.modulemap:1:8: error: redefinition of module 'Compression'
1 | module Compression [system] {
  |        `- error: redefinition of module 'Compression'
2 |   header "compression.h"
3 |   export *

/var/folders/nj/vtw8zd2j31d1gdrtntc5y4600000gn/T/madeira-steam-library-qa5yp0q9/shim/Compression/module.modulemap:1:8: note: previously defined here
1 | module Compression [system] { header "compression_shim.h" export * }
  |        `- note: previously defined here
2 |

/Applications/Xcode_16.4.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.sdk/usr/include/module.modulemap:15:1: note: in file included from /Applications/Xcode_16.4.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.sdk/usr/include/module.modulemap:15:
 13 | extern module SQLite3 "SQLite3.modulemap"
 14 | extern module xcselect "xcselect.modulemap"
 15 | extern module zlib "zlib.modulemap"
    | `- note: in file included from /Applications/Xcode_16.4.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.sdk/usr/include/module.modulemap:15:
 16 |
 17 | // Interfaces for process management and interprocess communication.

/Applications/Xcode_16.4.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.sdk/usr/include/zlib.modulemap:1:8: error: redefinition of module 'zlib'
1 | module zlib [system] {
  |        `- error: redefinition of module 'zlib'
2 |   header "zconf.h"
3 |   header "zlib.h"

/var/folders/nj/vtw8zd2j31d1gdrtntc5y4600000gn/T/madeira-steam-library-qa5yp0q9/shim/zlib/module.modulemap:1:8: note: previously defined here
1 | module zlib [system] { header "/usr/include/zlib.h" link "z" export * }
  |        `- note: previously defined here
2 |

/Applications/Xcode_16.4.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.sdk/usr/include/CommonCrypto/module.modulemap:1:8: error: redefinition of module 'CommonCrypto'
 1 | module CommonCrypto [system] {
   |        `- error: redefinition of module 'CommonCrypto'
 2 |   umbrella header "CommonCrypto.h"
 3 |   export *

/var/folders/nj/vtw8zd2j31d1gdrtntc5y4600000gn/T/madeira-steam-library-qa5yp0q9/shim/CommonCrypto/module.modulemap:1:8: note: previously defined here
1 | module CommonCrypto [system] { header "cc_shim.h" export * }
  |        `- note: previously defined here
2 |

/var/folders/nj/vtw8zd2j31d1gdrtntc5y4600000gn/T/madeira-steam-library-qa5yp0q9/shim/zlib/module.modulemap:1:31: error: header '/usr/include/zlib.h' not found
1 | module zlib [system] { header "/usr/include/zlib.h" link "z" export * }
  |                               `- error: header '/usr/include/zlib.h' not found
2 |

/var/folders/nj/vtw8zd2j31d1gdrtntc5y4600000gn/T/madeira-steam-library-qa5yp0q9/checks.swift:7:8: error: could not build Objective-C module 'zlib'
  5 | #endif
  6 | import CommonCrypto
  7 | import zlib
    |        `- error: could not build Objective-C module 'zlib'
  8 |
  9 | nonisolated(unsafe) var failures = 0
check-steam-library: 2 FAILED

```

## check-swap-coverage.py

```text
/var/folders/nj/vtw8zd2j31d1gdrtntc5y4600000gn/T/tmpwtt928hx/swap.c:13:10: fatal error: 'linux/falloc.h' file not found
   13 | #include <linux/falloc.h>
      |          ^~~~~~~~~~~~~~~~
1 error generated.
Traceback (most recent call last):
  File "/Users/runner/work/madeira-fork-testing/madeira-fork-testing/tests/host/check-swap-coverage.py", line 469, in <module>
    subprocess.run(['cc', '-O1', '-Wall', '-Wno-unused-function', '-Werror', '-o', str(exe), str(c)], check=True)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/subprocess.py", line 578, in run
    raise CalledProcessError(retcode, process.args,
                             output=stdout, stderr=stderr)
subprocess.CalledProcessError: Command '['cc', '-O1', '-Wall', '-Wno-unused-function', '-Werror', '-o', '/var/folders/nj/vtw8zd2j31d1gdrtntc5y4600000gn/T/tmpwtt928hx/swap', '/var/folders/nj/vtw8zd2j31d1gdrtntc5y4600000gn/T/tmpwtt928hx/swap.c']' returned non-zero exit status 1.

```

## check-wg-parser.py

```text
PASS: call tables match enum unix_funcs; wow64 thunks; kill switches (MADEIRA_WG_PARSER, MADEIRA_WG_VIDEO); Apple backend built/archived/linked; FFmpeg has mov and no H.264/HEVC/AAC decoder
building host FFmpeg into /Users/runner/.cache/madeira-host-ffmpeg/7.1.1-3c7e993eec95
ld: warning: reducing alignment of section __DATA,__common from 0x8000 to 0x4000 because it exceeds segment maximum alignment
Traceback (most recent call last):
  File "/Users/runner/work/madeira-fork-testing/madeira-fork-testing/tests/host/check-wg-parser.py", line 1112, in <module>
    assert out.returncode == 0, out.stdout + out.stderr
           ^^^^^^^^^^^^^^^^^^^
AssertionError: ==17907==AddressSanitizer: detect_leaks is not supported on this platform.


```

## check-wma-decoder.py

```text
SKIP-FAIL: /Users/runner/work/madeira-fork-testing/madeira-fork-testing/wine/build-macos/include/config.h is missing; point MADEIRA_WINE_BUILD at a configured Wine tree

```
