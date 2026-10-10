# Captured Windows test output

Sanitized local paths. Nonzero executions are not passes. Partial checks include explicit skips.

## check-audio-downmix.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-audio-downmix.py", line 149, in <module>
    subprocess.run(["cc", "-std=gnu11", "-Wall", "-Wno-unused-function", "-fsanitize=address,undefined",
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-audio-wow64.py

```text
PASS: 37 slots in the same order; shared entries ignore their args or carry no pointers
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-audio-wow64.py", line 81, in <module>
    subprocess.run(["cc", "-std=gnu11", "-Wall", "-Wno-unused-function", "-fsanitize=address,undefined",
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-cfg-early-docs.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-cfg-early-docs.py", line 70, in <module>
    subprocess.run([CC, "-std=gnu11", "-Wall", "-Wextra", "-Werror", "-Wno-unused-function",
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1462, in _execute_child
    args = list2cmdline(args)
           ^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 608, in list2cmdline
    for arg in map(os.fsdecode, seq):
               ^^^^^^^^^^^^^^^^^^^^^
  File "<frozen os>", line 859, in fsdecode
TypeError: expected str, bytes or os.PathLike object, not NoneType

```

## check-cfg-game.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-cfg-game.py", line 54, in <module>
    subprocess.run([CC, "-std=gnu11", "-Wall", "-Wextra", "-Werror", "-Wno-unused-function",
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1462, in _execute_child
    args = list2cmdline(args)
           ^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 608, in list2cmdline
    for arg in map(os.fsdecode, seq):
               ^^^^^^^^^^^^^^^^^^^^^
  File "<frozen os>", line 859, in fsdecode
TypeError: expected str, bytes or os.PathLike object, not NoneType

```

## check-child-desktop.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-child-desktop.py", line 182, in <module>
    if subprocess.run(flags[:1] + sanitize + flags[1:], capture_output=True).returncode == 0:
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-child-ntdll-alias.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-child-ntdll-alias.py", line 197, in <module>
    if subprocess.run(flags[:1] + sanitize + flags[1:], capture_output=True).returncode == 0:
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-config-catalog.py (before normalization fix)

```text
ConfigCatalog.generated.swift is out of date: run build/tools/gen-config-catalog.py
ok   swap sizes include 3072
ok   coverage picker: large-only default, blocks, wide
ok   JIT pool and video memory pickers in Memory & sync
ok   eco mode toggle in Memory & sync, off unless set
ok   catalog lists swap-mb with a 3 GB choice
ok   catalog lists env.MADEIRA_SWAP_COVERAGE
FAILED

```

## check-config-catalog.py

```text
ConfigCatalog.generated.swift is current
ok   swap sizes include 3072
ok   coverage picker: large-only default, blocks, wide
ok   JIT pool and video memory pickers in Memory & sync
ok   eco mode toggle in Memory & sync, off unless set
ok   catalog lists swap-mb with a 3 GB choice
ok   catalog lists env.MADEIRA_SWAP_COVERAGE
PASS

```

## check-control-presets.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-control-presets.py", line 200, in <module>
    subprocess.run([os.environ.get('SWIFTC', 'swiftc'), str(src), '-o', str(exe)], check=True)
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-d3d12-tiled.py

```text
ok   d3d12-tiled-resources defaults to 0
ok   d3d12-reserved-max-mb defaults to 1024
ok   logged once, only when on
ok   device_CreateReservedResource: the stub, unchanged, when the key is off
ok   device_CreateReservedResource1: the stub, unchanged, when the key is off
ok   device_CreateReservedResource2: the stub, unchanged, when the key is off
ok   device_GetResourceTiling: the stub, unchanged, when the key is off
ok   queue_UpdateTileMappings: the stub, unchanged, when the key is off
ok   queue_CopyTileMappings: the stub, unchanged, when the key is off
ok   OPTIONS: Tier 2 and 40 VA bits only behind the key
ok   OPTIONS: the default answer still leaves both at zero (memset)
ok   FORMAT_SUPPORT: R32G32B32 vertex formats only behind the key, nothing but IA_VERTEX_BUFFER
ok   vtable: g_device_vtbl.CreateReservedResource
ok   vtable: g_device_vtbl.CreateReservedResource1
ok   vtable: g_device_vtbl.CreateReservedResource2
ok   vtable: g_device_vtbl.GetResourceTiling
ok   vtable: g_queue_vtbl.UpdateTileMappings
ok   vtable: g_queue_vtbl.CopyTileMappings
ok   reserved resources: refused above the cap with E_OUTOFMEMORY, before anything is allocated
ok   reserved resources: a NULL out is the documented capability test (S_FALSE)
ok   reserved resources: backed as a committed resource in a DEFAULT heap
ok   reserved resources: marked as reserved (GetResourceTiling answers only for them)
ok   GetResourceTiling: packed subresources are D3D12_PACKED_TILE with zero size
ok   GetResourceTiling: slice s starts at s x tiles-per-slice
ok   GetResourceTiling: packed mips start after slice 0's standard mips
ok   GetResourceTiling: a buffer has no mip information
SKIP: no host C compiler for the tiling harness
PASS

```

## check-d3d9-splitlock.py

```text
PASS: device-lock switches present; no split-lock rollback; WOW64 strict split locks default on
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-d3d9-splitlock.py", line 135, in <module>
    subprocess.run(["c++", "-std=c++20", "-O1", "-g", "-pthread", "-fsanitize=address,undefined",
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-d9-upload-commit.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-d9-upload-commit.py", line 93, in <module>
    subprocess.run(["g++", "-std=c++20", "-O1", "-Wall", "-fsanitize=address,undefined", str(src), "-o", str(exe)], check=True)
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-dock-components.py

```text
PASS: pinned client DLL is a build the pinned Dock host supports
PASS: three pinned packages from one HTTPS Valve host; redirects stay on it
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-dock-components.py", line 87, in <module>
    subprocess.run([SWIFTC, '-I', str(tmp), str(source), str(tmp/'main.swift'), '-o', str(exe)], check=True)
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-dock-contract.py

```text
PASS: MadeiraDock.swift: no program-name list (['dockhost.exe'])
PASS: MadeiraDock.swift: no credential or path in "SteamLog.event("[dock-report] \(key)=\(report.fields[key]!)""
PASS: MadeiraDock.swift: no credential or path in "SteamLog.event("[dock-report-file] lines=\(lines.count)")"
PASS: MadeiraDock.swift: no credential or path in "for line in lines.prefix(400) { SteamLog.event("[dock-report"
PASS: MadeiraDock.swift: no credential or path in "SteamLog.event("[dock-handoff] protected-file-ready=1")"
PASS: MadeiraDock.swift: no credential or path in "SteamLog.event("[dock-launch] image-retire=\(retire ? 1 : 0)"
PASS: MadeiraDock.swift: no credential or path in "SteamLog.event("[dock-launch] image-map-guard=\(guardMap ? 1"
PASS: MadeiraDock.swift: no credential or path in "SteamLog.event("[dock-offline] enabled=\(enabled ? 1 : 0) ne"
PASS: MadeiraDock.swift: no credential or path in "SteamLog.event("[dock-offline] Valve's client can log this a"
PASS: MadeiraDockView.swift: no program-name list ([])
PASS: MadeiraDockView.swift: no credential or path in "SteamLog.event("[dock-setup] client components ready")"
PASS: MadeiraDockView.swift: no credential or path in "SteamLog.event("[dock-setup] client components failed")"
PASS: MadeiraDockView.swift: no credential or path in "if let plan { LogStore.shared.log("[dock-installers] " + pla"
PASS: MadeiraDockView.swift: no credential or path in "LogStore.shared.log("[madeira-dock] " + failure, level: .err"
PASS: MadeiraDockView.swift: no credential or path in "LogStore.shared.log("[madeira-dock] host finished (result 0)"
PASS: MadeiraDockView.swift: no credential or path in "LogStore.shared.log("[madeira-dock] session ended without a "
PASS: SteamRuntime.swift: no program-name list (['steam.exe'])
PASS: DockInstallers.swift: no program-name list (['.exe', 'msiexec.exe'])
PASS: DockInstallers.swift: no credential or path in "catch { LogStore.shared.log("[dock-installers] app=\(appID) "
PASS: DockInstallers.swift: no credential or path in "LogStore.shared.log("[dock-installers] app=\(appID) choice=\"
PASS: DockInstallers.swift: no credential or path in "LogStore.shared.log("[dock-installers] app=\(app) off (MADEI"
PASS: DockInstallers.swift: no credential or path in "LogStore.shared.log("[dock-installers] app=\(app) scripts=\("
PASS: DockInstallers.swift: no credential or path in "LogStore.shared.log("[dock-installers] app=\(app) choice=ski"
PASS: DockInstallers.swift: no credential or path in "LogStore.shared.log("[dock-installers] app=\(app) choice=run"
PASS: DockInstallers.swift: no credential or path in "LogStore.shared.log("[dock-installers] app=\(app) batch not "
PASS: DockInstallers.swift: no credential or path in "catch { LogStore.shared.log("[dock-installers] app=\(app) le"
PASS: DockInstallers.swift: no credential or path in "LogStore.shared.log("[dock-installers] app=\(app) program=\("
PASS: DockInstallers.swift: no credential or path in "LogStore.shared.log("[dock-installers] app=\(app) dotnet-fus"
PASS: DockInstallers.swift: no credential or path in "LogStore.shared.log("[dock-installers] app=\(app) scripts=\("
PASS: DockInstallers.swift: no credential or path in "catch { LogStore.shared.log("[dock-installers] app=\(app) re"
PASS: DockInstallers.swift: no credential or path in "LogStore.shared.log("[dock-installers] app=\(app) results re"
PASS: DockInstallers.swift: no credential or path in "LogStore.shared.log("[dock-installers] app=\(app) results re"
PASS: DockInstallers.swift: no credential or path in "LogStore.shared.log("[dock-installers] services=\(services)""
PASS: DockInstallers.swift: no credential or path in "LogStore.shared.log("[dock-installers] start \(index)/\(resu"
PASS: DockInstallers.swift: no credential or path in "LogStore.shared.log("[dock-installers] exit \(index)/\(resul"
PASS: DockInstallers.swift: no credential or path in "LogStore.shared.log("[dock-installers] end succeeded=\(succe"
PASS: compact pool is off unless opted in
PASS: madeira.cfg pool is applied after the Dock policy (explicit wins)
PASS: the standard 896 MB pool is unchanged outside a compact Dock launch
PASS: only the Dock launch requests the Dock pool policy
PASS: the launch uses the sign-in API
PASS: ContentView.swift: does not set the image-retire switch
PASS: MadeiraDockView.swift: does not set the image-retire switch
PASS: SteamRuntime.swift: does not set the image-retire switch
PASS: the image-retire switch is set only in the Dock launch environment
PASS: only the Dock launch configures the host environment
PASS: ContentView.swift: does not set the image-map guard
PASS: MadeiraDockView.swift: does not set the image-map guard
PASS: SteamRuntime.swift: does not set the image-map guard
PASS: the image-map guard is set only in the Dock launch environment
PASS: the bridge clears the fixed Steam identity only for a Dock session (a direct start publishes its game's own)
PASS: only a Dock launch sets MADEIRA_DOCK_SESSION; every other launch clears it
PASS: no built Dock executable or notices are tracked
PASS: madeira-dock matches the revision pinned by Madeira
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-dock-contract.py", line 262, in <module>
    build = subprocess.run([SWIFTC, '-parse-as-library', '-swift-version', '5', '-sanitize=address', '-o', str(exe),
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-dock-gdi-section.py

```text
PASS: startDock asks for the section-backed GDI table once
PASS: before the launch request
PASS: nothing else in ContentView touches it (regular launches unchanged)
PASS: madeira.cfg env.* entries are exported with overwrite when the session starts
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-dock-gdi-section.py", line 74, in <module>
    subprocess.run([CC, '-O1', '-o', str(exe), str(c)], check=True)
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-dock-installers.py

```text
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
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-dock-installers.py", line 422, in <module>
    build = subprocess.run([SWIFTC, '-parse-as-library', '-swift-version', '5', '-sanitize=address', '-o', str(exe),
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-dock-path.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-dock-path.py", line 88, in <module>
    (prefix_dir/'drive_c').mkdir(); (prefix_dir/'dosdevices/c:').symlink_to('../drive_c')
                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\pathlib.py", line 1386, in symlink_to
    os.symlink(target, self, target_is_directory)
OSError: [WinError 123] The filename, directory name, or volume label syntax is incorrect: '../drive_c' -> '<workspace>\\work\\tmp\\madeira-dock-path-33v6kb7m\\wine\\dosdevices\\c:'

```

## check-dock-report.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-dock-report.py", line 71, in <module>
    subprocess.run([SWIFTC, str(source), '-o', str(binary)], check=True)
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-dock-start-screen.py

```text
PASS: DockStartScreen.swift: GPL-3.0-or-later, Copyright 2026 125hz, Converter Exception
PASS: DockStartScreen.swift is built by the Xcode project
PASS: the rules are Foundation-only and pure (switches are passed in)
PASS: no program names in the rules or the census
PASS: no program names in the rules or the census
PASS: no program-name lists: owners are classed by folder
PASS: a Dock start (from Settings or a Steam game's Game details page) tells the library which game it starts
PASS: the library begins and ends the Dock starting screen with the session
PASS: while the hold is on, the desktop's first frame does not end the starting screen
PASS: one row of glyph buttons
PASS: glyph order: close session, live log, show desktop
PASS: close session only once the Dock stopped; show desktop only while the desktop is held back
PASS: the starting screen shows the Dock status, the one-time-install note, and a stop with its words
PASS: the status line reads the installs' end after polling them, and times the host from it (or from the start)
PASS: a Dock start shows the game's cover and backdrop by App ID
PASS: the census runs only while a Dock start holds the desktop back
PASS: driver helpers: restore posted, front by the own thread
PASS: a restored born-minimized window is brought to the front by its own thread's event pump
PASS: a destroyed window leaves the census and any pending front request
PASS: the census is fed by the frame, GDI flush and swapchain hooks
PASS: Winios.m includes the header Swift reads the census struct from
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-dock-start-screen.py", line 313, in <module>
    r = subprocess.run([SWIFTC, '-parse-as-library', '-swift-version', '5', '-o', str(exe),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-ec-conhost.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-ec-conhost.py", line 77, in <module>
    if subprocess.run(flags[:1] + sanitize + flags[1:], capture_output=True).returncode != 0:
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-fastsync.py

```text
FAIL: a C compiler (cc) on PATH
PASS: the client block is iOS-only and uses the shared header
PASS: NtSetEvent: every fastsync call is under #ifdef WINE_IOS
PASS: NtResetEvent: every fastsync call is under #ifdef WINE_IOS
PASS: NtReleaseSemaphore: every fastsync call is under #ifdef WINE_IOS
PASS: NtQuerySemaphore: every fastsync call is under #ifdef WINE_IOS
PASS: NtWaitForSingleObject: every fastsync call is under #ifdef WINE_IOS
PASS: NtWaitForMultipleObjects: every fastsync call is under #ifdef WINE_IOS
PASS: close_inproc_sync() drops the handle from the fastsync cache first (every NtClose/dup/APC close)
PASS: server_init_process_done() flushes a reissued process id
PASS: the server allocates a cell only when fastsync is switched on
PASS: the server keeps madsync and fastsync exclusive
PASS: the timeout re-check runs only while fastsync cells exist
PASS: semaphores allocate through the same switch and are learnt through get_inproc_sync_fd
PASS: sync.c: no allocation in the fastsync lines
PASS: event.c: no allocation in the fastsync lines
PASS: semaphore.c: no allocation in the fastsync lines
PASS: thread.c: no allocation in the fastsync lines
check-fastsync: FAIL

```

## check-filtering-cap.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-filtering-cap.py", line 33, in <module>
    subprocess.run(['g++','-std=c++20','-O1','-fsanitize=address,undefined',str(p),'-o',str(o)],check=True);subprocess.run([str(o)],check=True)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-free-delay.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-free-delay.py", line 151, in <module>
    if subprocess.run(flags[:1] + sanitize + flags[1:], capture_output=True).returncode == 0:
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-frontend.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-frontend.py", line 478, in <module>
    r = subprocess.run(['swift', str(sp)], capture_output=True, text=True)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-gamepad.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-gamepad.py", line 132, in <module>
    subprocess.run([os.environ.get('CC', 'cc'), '-std=c11', '-Wall', '-Wextra', '-Werror',
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-hardware-input.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-hardware-input.py", line 235, in <module>
    subprocess.run([os.environ.get('SWIFTC', 'swiftc'), str(src), '-o', str(exe)], check=True)
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-hidpad.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-hidpad.py", line 644, in <module>
    subprocess.run([cc, *flags, '-Wall', '-Werror', '-Wno-unused-variable', str(reg_source), '-o', str(reg_binary)],
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-hw-registry.py

```text
ok   start_main_thread: init_cpu_info -> ios_hw_registry_publish -> unix_init_startup_info
ok   the call is iOS-only and declared next to it
ok   only start_main_thread (the session's first process) publishes
ok   and inside the WINE_IOS block that ends before server_init_process
ok   build.sh compiles server_ios.c and loader_ios.c (no new translation unit)
ok   MADEIRA_HW_REGISTRY read once, through hwreg_enabled
ok   every HARDWARE key is made by the volatile level-by-level helper
ok   Session Manager\Environment is not touched
ok   ios_hw_key creates each missing level REG_OPTION_VOLATILE (inside the test region)
ok   one [hw-registry] line per session (or the off line)
ok   the CNTFRQ_EL0 read stays outside the test region (the harness supplies its own)
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-hw-registry.py", line 111, in <module>
    out = run_c({"values.c": r'''
          ^^^^^^^^^^^^^^^^^^^^^^^
  File "<workspace>\outputs\Madeira\tests\host\check-hw-registry.py", line 58, in run_c
    r = subprocess.run(cmd, capture_output=True, text=True)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-iat-sync-owner.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-iat-sync-owner.py", line 109, in <module>
    if subprocess.run(flags[:1] + sanitize + flags[1:], capture_output=True).returncode == 0:
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-image-reload.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-image-reload.py", line 222, in <module>
    subprocess.run([os.environ.get('CC', 'cc'), '-std=gnu11', '-Wall', '-Wextra', '-Werror', '-g',
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-image-retire.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-image-retire.py", line 119, in <module>
    subprocess.run([os.environ.get('CC', 'cc'), '-std=gnu11', '-Wall', '-Wextra', '-Werror', '-g',
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-jit-method.py

```text
PASS: StikDebug uses the canonical enable-jit URL
PASS: StikDebug request targets the current PID and carries Madeira's script
PASS: the bundled JavaScript file is the single script source
PASS: StikDebug attach has a finite 90-second readiness timeout
PASS: readiness requires CS_DEBUGGED and a live debugger
PASS: Automatic prefers installed StikDebug, then Built-in StikJIT
PASS: the coordinator routes each selected JIT method once, after the loopback check
PASS: JIT setup is reachable from the main flow and Settings
PASS: pairing import rejects ordinary lockdown plists before invoking StikJIT
PASS: the app starts the helper extension by the helper's own bundle ID in this installation
PASS: no ExtensionKit extension point is declared or looked up (iOS registers none for a renamed install)
PASS: the request (PID, pairing data, script) goes in the extension request, the answer in the item it completes with
PASS: the helper attaches to Madeira and forces its custom script
PASS: built-in JIT is disabled under LiveContainer
PASS: Xcode project contains MadeiraJITHelper.appex in Embed JIT Helper
PASS: Xcode project contains madeira-jit.js in Resources
PASS: Xcode project contains JITBuiltInMessages.swift in Helper Sources
PASS: Xcode project contains Frameworks/StikJIT.xcframework/ios-arm64
PASS: StikJIT links on device only, with a simulator-safe helper stub
PASS: the app may detect the canonical StikDebug URL scheme
PASS: the helper is a classic app extension in PlugIns, as LiveContainer's LiveProcess
PASS: one setting, MADEIRA_BUNDLE_IDENTIFIER, names the app and the helper
PASS: a reset connection reads as a rejected pairing; refused, timed out or unreachable as LocalDevVPN
PASS: Check setup and Enable JIT both explain connection problems
PASS: the library's JIT error offers Pair Again and LocalDevVPN (or the shortcut)
PASS: the library's error alert is on the tab view, shown on the Settings tab as well
PASS: LocalDevVPN opens to connect and returns to Madeira's own URL scheme
PASS: Play without JIT enables it (a second Play while it runs only replaces the game)
PASS: the waiting game starts once, only when JIT came on and nothing else started
PASS: the Play button reads Starting JIT with a spinner meanwhile; the details page stays up for it, and closes for JIT setup
PASS: every way Enable JIT ends settles the waiting game
PASS: Play and Dock starts continue after JIT without repeating the checks already passed
check-jit-method: PASS

```

## check-jit-network.py

```text
PASS: JITNetwork.swift is built by the Xcode project
PASS: the check targets lockdownd through LocalDevVPN's loopback (10.7.0.1:62078, StikDebug's address)
PASS: Enable JIT checks the loopback before any JIT method
PASS: the shortcut runs only when the loopback does not answer and the shortcut is turned on
PASS: a JIT attempt that fails after the shortcut ran puts back what it changed
PASS: "start" asks for the cellular step only without Wi-Fi, and records the "done" it owes before it runs
PASS: "done" disconnects LocalDevVPN when no VPN was on, restores the one the shortcut kept, and leaves VPNs alone when LocalDevVPN was already on or "start" did not report
PASS: the shortcut needs no file (no iCloud Drive or folder to set up)
PASS: Madeira neither logs nor keeps the VPN's name (the shortcut keeps the VPN itself)
PASS: Madeira JIT.shortcut is a signed export (AEA1 with a signing certificate chain)
PASS: Madeira JIT.shortcut is copied into the app
PASS: the file's name is the shortcut's name Madeira runs (Shortcuts names an import after its file)
PASS: the shortcut is offered on iOS 27 or later only (it uses Store Content)
PASS: setup offers it on its own page after any of the three JIT guides, so the guides fit on one screen
PASS: setup's page and Settings › JIT add it from its iCloud link (straight to Add Shortcut), and Madeira's copy through the share sheet with no connection
PASS: the iCloud link and the bundled file are kept as one shortcut
PASS: setup no longer says the pairing file is in Documents
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-jit-network.py", line 121, in <module>
    build = subprocess.run([SWIFTC, '-O', str(src), '-o', str(exe)], capture_output=True, text=True)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-jit-pairing.py

```text
PASS: MadeiraRPPairing.h declares exactly the exported functions (in step)
PASS: the bridging header imports the pairing interface
PASS: the library uses idevice's pairable host and does no mDNS itself
PASS: idevice is pinned to an exact version with a lockfile
SKIP: cargo not on PATH, library tests not run
PASS: the service is published through mDNSResponder (dns_sd) as a pairable host
PASS: on-device pairing is offered from iOS 27
PASS: the session is freed only after its accept returned (or when it never started)
PASS: cancelling signals the running accept
PASS: a pairing is stored through the coordinator
PASS: the stored pairing selects Built-in StikJIT
PASS: the pairing file is kept in the Keychain, this device only, readable while unlocked
PASS: the pairing file is never written to Documents (only the old copy is read there)
PASS: an old Documents copy is deleted only after the Keychain holds it
PASS: imports and on-device pairings share one validation
PASS: an import stops a waiting on-device pairing, so it cannot overwrite the import
PASS: no PIN or device name in "log("advertising failed error=\(error)")"
PASS: the background task uses the permitted .pairing.* identifier
PASS: Info.plist declares the Bonjour service
PASS: Info.plist explains Local Network access
PASS: Info.plist permits the pairing background task
PASS: setup: In-app (iOS 27), In-app with pairing file, StikDebug
PASS: setup: the on-device guide pairs and shows its progress
PASS: Settings › JIT setup can pair on the device
PASS: Xcode project contains JITPairing.swift in Sources
PASS: Xcode project contains libmadeira_rppairing.a in Frameworks
PASS: Xcode project contains MadeiraRPPairing.h */ = {isa = PBXFileReference
PASS: the built library and cargo output are ignored
PASS: crate notices are bundled
PASS: THIRD-PARTY-NOTICES.md lists on-device pairing
PASS: app/Madeira/legal/THIRD-PARTY-NOTICES.md lists on-device pairing
check-jit-pairing: PASS

```

## check-kmt-adapter.py

```text
ok   build.sh compiles d3dkmt_ios.c for upstream d3dkmt.c
ok   the wrapper renames exactly the wrapped entry points
ok   and undefines every rename after the include
ok   NtGdiDdDDIOpenAdapterFromHdc calls upstream_NtGdiDdDDIOpenAdapterFromHdc
ok   NtGdiDdDDIQueryAdapterInfo calls upstream_NtGdiDdDDIQueryAdapterInfo
ok   NtGdiDdDDIQueryStatistics calls upstream_NtGdiDdDDIQueryStatistics
ok   NtGdiDdDDIQueryVideoMemoryInfo calls upstream_NtGdiDdDDIQueryVideoMemoryInfo
ok   QueryAdapterInfo answers only with the switch, for a real adapter handle, else upstream
ok   OpenAdapterFromHdc opens the adapter only with the switch, else the upstream stub
ok   QueryVideoMemoryInfo fills only an empty LOCAL budget, only with the switch
ok   the switch is env MADEIRA_KMT_ADAPTER, read once
ok   madeira_cfg.h comes before Wine's headers (they poison strncpy)
ok   EnumAdapters2 lists the adapter only with the switch and no GPU in `gpus`
ok   OpenAdapterFromDeviceName opens the registry GPU's interface only with the switch
ok   OpenAdapterFromGdiDisplayName's virtual adapter takes the LUID only with the switch
ok   registry GPU: switch LUID, else a fresh one; switch size, else 4096 MB
ok   identity = the registry GPU (ids, name, DriverVersion, path)
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-kmt-adapter.py", line 206, in <module>
    built = cc(harness, exe, ["-fsanitize=address,undefined"])
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<workspace>\outputs\Madeira\tests\host\check-kmt-adapter.py", line 121, in cc
    r = subprocess.run(["cc", "-std=gnu11", "-Wall", "-Wno-unused-function", "-I%s" % u, str(c), "-o", str(exe)]
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-launch-routing.py

```text
PASS: non-i386 targets keep the upstream core choice and exe path; the i386 farm, wbem and winsxs come with the farm
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-launch-routing.py", line 117, in <module>
    subprocess.run(["cc", "-std=gnu11", "-O1", "-g", "-fsanitize=address,undefined", "-fno-omit-frame-pointer",
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-lazy-windows.py

```text
PASS: virtual_init and map_view only reach the window code through the lazy gates
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-lazy-windows.py", line 203, in <module>
    subprocess.run(["cc", "-std=gnu11", "-Wall", "-Wno-unused-function", "-Wno-unused-variable",
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-library-api.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-library-api.py", line 76, in <module>
    subprocess.run(['swift', str(p)], check=True)
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-library-groups.py

```text
PASS: options menu: Group by Last played, Installed, Platform or None
PASS: Group by is remembered; Platform (the sections) by default
PASS: page: the other choices replace the sections, Platform keeps them
PASS: controller focus follows the grouped page's order
PASS: grouped page: the games you added and Steam games together
PASS: grouped page: not installed Steam games only while signed in
PASS: grouped page: installed games open Game details, others their download sheet
PASS: grouped page: group titles collapse with MADEIRA_LIBRARY_COLLAPSE
PASS: docs/LIBRARY.md: Group by
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-library-groups.py", line 138, in <module>
    build = subprocess.run([SWIFTC, '-parse-as-library', '-swift-version', '5', '-o', str(exe),
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-library-sections.py

```text
PASS: page order: Desktop, then Steam, then Other games
PASS: Other games is a section exactly when the Steam section is shown; installed Steam games come first
PASS: Not installed follows Other games; with nothing installed the whole Steam section does
PASS: without the Steam section: one grid of the games you added, or the empty-library message
PASS: pull down on the library refreshes the Steam section
PASS: Other games: count and a collapsible title (MADEIRA_LIBRARY_COLLAPSE)
PASS: Other games: no Add a game button of its own; the + in the navigation bar opens the executable browser
PASS: Other games: empty and no-match texts
PASS: Other games: collapsed, empty, then the games
PASS: Other games: remembered collapsed state
PASS: Other games: the games you added (no Steam game, no desktop), filtered by the search
PASS: Other games: the library's layout
PASS: Steam: installed count and a collapsible title
PASS: Steam: a progress indicator while the library refreshes
PASS: Steam: remembered states (installed shown, Not installed open by default)
PASS: MADEIRA_LIBRARY_COLLAPSE (on by default) makes the titles collapsible
PASS: Steam order: title, sign-in, downloading + installed, empty text, Not installed
PASS: Steam: empty-library text
PASS: Steam: the empty text only when signed in, loaded, nothing owned to install and no search
PASS: Not installed: signed in, folds on its own, not with the Steam title
PASS: Steam: the search, the groups and the library's Sort by apply
PASS: the sign-in card
PASS: Steam cards: the library's list and compact list rows
PASS: log line [library-sections]
PASS: the log line has flags only
PASS: docs/LIBRARY.md: the sections and the switch
PASS: docs/STEAM_LIBRARY.md: pull down to refresh
check-library-sections: PASS

```

## check-nav-keys.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-nav-keys.py", line 117, in <module>
    subprocess.run([os.environ.get('CC', 'cc'), '-Wall', '-Werror', str(csrc), '-o', str(cexe)], check=True)
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-nsi-network.py

```text
PASS: build.sh compiles nsi_network_ios.c
PASS: build.sh archives nsi_network_ios.o into libntdll_unix.a
PASS: build.sh compiles nsi_ndis_ios.c
PASS: build.sh archives nsi_ndis.o into libntdll_unix.a
PASS: build.sh compiles nsi_ip_ios.c
PASS: build.sh archives nsi_ip.o into libntdll_unix.a
PASS: compile_one searches shims/ (for <net/route.h>)
PASS: shims/net/route.h carries Madeira's own notice
PASS: shims/net/route.h has no Apple licence text
PASS: shims/net/route.h declares only the constants ndis.c and ip.c use
PASS: nsi_ndis_ios.c (an include wrapper) carries Madeira's own notice
PASS: nsi_ndis_ios.c compiles ndis.c unchanged
PASS: nsi_ip_ios.c compiles ip.c unchanged
PASS: nsi_network_ios.c keeps Wine's LGPL-2.1-or-later notice
PASS: nsi_network_ios.c's notice is nsi.c's, verbatim
PASS: nsi_ip_ios.c keeps Wine's LGPL-2.1-or-later notice
PASS: nsi_ip_ios.c's notice is tcp.c's, verbatim
PASS: nsi_unixlib_ios.c: a non-TCP enumerate goes to the dispatcher and returns its status
PASS: [nsi-network] prints module, table, status and count only
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-nsi-network.py", line 426, in <module>
    build = subprocess.run([CC, '-std=gnu11', '-Wall', '-Wno-unused-function', '-Wno-missing-braces',
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-onboarding.py

```text
PASS: Onboarding.swift: GPL-3.0-or-later, Copyright 2026 125hz, Converter Exception
PASS: Onboarding.swift is built by the Xcode project
PASS: the rules are Foundation-only (compiled on the host)
PASS: setup is considered once per run, opens only by the rules, and after an update shows only the new pages
PASS: Run setup again shows every page
PASS: setup never opens over a running session, or with nothing to set up
PASS: the pages follow the sign-in and Dock switches, whether LocalDevVPN and Wine Mono are here, and the revision seen
PASS: LocalDevVPN's and Wine Mono's pages are decided once, when setup opens, so installing on the way does not renumber the steps
PASS: only finishing or skipping stores the setup revision; nothing clears it
PASS: the model uses the rules switch
PASS: Library: setup is presented over the library
PASS: Library: setup is considered when the library appears
PASS: Library: controller commands do not act behind setup
PASS: Settings › Steam: Run setup again, hidden with MADEIRA_ONBOARDING=0
PASS: Settings › JIT: Run setup again, hidden with MADEIRA_ONBOARDING=0
PASS: signInPage: Set up later
PASS: dockClientPage: Set up later
PASS: welcome: visible Skip setup
PASS: JIT: each of the three ways in has its own guide
PASS: JIT: In-app (iOS 27), In-app with pairing file, StikDebug
PASS: JIT: the on-device guide pairs and shows its progress
PASS: JIT: the pairing-file guide imports
PASS: JIT: the StikDebug guide selects StikDebug
PASS: JIT: onDeviceGuide goes back
PASS: JIT: pairingFileGuide goes back
PASS: JIT: stikDebugGuide goes back
PASS: JIT: leaving the guide stops a waiting pairing
PASS: JIT: visible defer choice
PASS: JIT: validated import selects Built-in StikJIT through the coordinator
PASS: LocalDevVPN's page sends a missing LocalDevVPN to the App Store, and can be skipped
PASS: LocalDevVPN is checked with canOpenURL (nothing opens), again whenever Madeira comes back to the front
PASS: no hidden gestures
PASS: components through Dock's verified download
PASS: sign-in through #45's sheet
PASS: sign-out through #45's model
PASS: Settings opens Dock's sheet
PASS: Onboarding.swift: no SteamTokenStore (tokens only via the sign-in store)
PASS: Onboarding.swift: no credentialsForDock (tokens only via the sign-in store)
PASS: Onboarding.swift: no refreshToken (tokens only via the sign-in store)
PASS: Onboarding.swift: no SecItem (tokens only via the sign-in store)
PASS: Onboarding.swift: no kSec (tokens only via the sign-in store)
PASS: Onboarding.swift: no accessToken (tokens only via the sign-in store)
PASS: no account, token or path in "LogStore.shared.log("[onboarding] shown reason=\(reason) steps=\(steps"
PASS: no account, token or path in "LogStore.shared.log("[onboarding] step=\(next.rawValue)")"
PASS: no account, token or path in "LogStore.shared.log("[onboarding] skipped")"
PASS: no account, token or path in "LogStore.shared.log("[onboarding] done")"
PASS: no account, token or path in "LogStore.shared.log("[onboarding] JIT method=built-in pairing=imported"
PASS: no account, token or path in "LogStore.shared.log("[onboarding] pairing import failed")"
PASS: no account, token or path in "LogStore.shared.log("[onboarding] LocalDevVPN app-store")"
PASS: no account, token or path in "LogStore.shared.log("[onboarding] JIT method=StikDebug")"
PASS: no account, token or path in "LogStore.shared.log("[onboarding] JIT way=\(way.rawValue)")"
PASS: no account, token or path in "LogStore.shared.log("[onboarding] JIT in-app pairing started")"
PASS: no account, token or path in "LogStore.shared.log("[onboarding] JIT method=built-in")"
PASS: no account, token or path in "LogStore.shared.log("[jit-shortcut] add: iCloud link")"
PASS: no account, token or path in "LogStore.shared.log("[onboarding] JIT shortcut on=\(shortcut.enabled ?"
PASS: no account, token or path in "LogStore.shared.log("[onboarding] sign-in replaced")"
PASS: no account, token or path in "LogStore.shared.log("[onboarding] components download")"
PASS: no account, token or path in "LogStore.shared.log("[onboarding] Wine Mono download")"
PASS: Onboarding.swift: no runWineFullSequence
PASS: Onboarding.swift: no setenv(
PASS: Onboarding.swift: no unsetenv(
PASS: Onboarding.swift: no MADEIRA_EXE
PASS: Onboarding.swift: no MADEIRA_ARGS
PASS: Onboarding.swift: no jit_
PASS: Onboarding.swift: no StikJITHelper
PASS: Onboarding.swift: no poolSize
PASS: Onboarding.swift: no JITPool
PASS: Onboarding.swift: no MADEIRA_POOL
PASS: Onboarding.swift: no FEX_
PASS: Onboarding.swift: no DXMT
PASS: Onboarding.swift: no MADEIRA_JIT
PASS: Onboarding.swift: no steamwebhelper
PASS: Onboarding.swift: no SteamSetup
PASS: Onboarding.swift: no inproc-sync
PASS: Onboarding.swift: no swap-mb
PASS: Onboarding.swift: no MADEIRA_FASTSYNC
PASS: Onboarding.swift: no madsync
PASS: Onboarding.swift: no pool size
PASS: Onboarding.swift: no program-name list (['explorer.exe'])
PASS: rules key nothing on program names
PASS: ContentView hands Dock's start to the library
PASS: a held Dock start writes no sign-in transfer
PASS: a Dock start from Settings is an unsaved library session
PASS: Dock's launch path takes a Steam game's own profile, and only that
PASS: a Steam game's profile leaves Dock's program, arguments and desktop in place
PASS: begin(remember: false) neither adds nor stamps an entry
PASS: the Dock session entry is a desktop session, never saved
PASS: docs/LIBRARY.md documents setup and its switch
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-onboarding.py", line 299, in <module>
    build = subprocess.run([SWIFTC, '-parse-as-library', '-swift-version', '5', '-o', str(exe),
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-pad-output.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-pad-output.py", line 293, in <module>
    subprocess.run([cc, '-std=c11', '-Wall', '-Wextra', '-Werror', '-Wno-unused-function', '-O1', '-pthread',
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-readonly-link.py

```text
PASS: open_fd: the replacement runs only inside the failed-open branch, first
PASS: open_fd: upstream's directory retry and error mapping follow unchanged
PASS: one caller, one unlink
PASS: the log line prints no file name
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-readonly-link.py", line 205, in <module>
    build = subprocess.run([CC, '-std=gnu11', '-Wall', '-Wno-unused-function', '-fsanitize=address,undefined', '-g',
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-runtime-settings.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-runtime-settings.py", line 115, in <module>
    r = subprocess.run(['swift', str(sp)], capture_output=True, text=True, env=env)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-scene-batching.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-scene-batching.py", line 59, in <module>
    o=t/'ml1250-batching';subprocess.run(['g++','-std=c++20','-O1','-fsanitize=address,undefined',str(p),'-o',str(o)],check=True);subprocess.run([str(o)],check=True)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-section-abort.py

```text
PASS: three deferral points: the EPIPE write, the EOF read and the fd read
PASS: ml1183: a dead fd socket inside a section fails the read before abort_thread
PASS: send_request: EPIPE outside a section still exits at once
PASS: read_reply_data: EOF outside a section still exits at once
PASS: server_call_unlocked: a killed thread sends nothing more
PASS: leave: unlock, restore the mask, then exit (where Linux delivers SIGQUIT)
PASS: the four fd_cache_mutex sections themselves are unchanged
PASS: a thread woken as killed in a server wait still exits at once
PASS: the log line prints numbers only
PASS: no thread-local variable (first touch allocates on Darwin)
PASS: the x18 diagnostic read is the only host-specific line replaced
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-section-abort.py", line 308, in <module>
    build = subprocess.run([CC, '-std=gnu11', '-g', '-O1', '-Wall', '-Wno-unused-function', '-Werror=implicit-function-declaration',
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-small-va-band.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-small-va-band.py", line 71, in <module>
    subprocess.run(["cc", "-std=gnu11", "-Wall", "-Wno-unused-function", "-Wno-unused-variable", "-fsanitize=address,undefined", str(c), "-o", str(exe)], check=True)
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-stale-heal-owner.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-stale-heal-owner.py", line 129, in <module>
    if subprocess.run(flags[:1] + sanitize + flags[1:], capture_output=True).returncode == 0:
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-steam-cloud.py

```text
PASS: Steam Cloud is on unless turned off (env.MADEIRA_STEAM_CLOUD = 0)
PASS: Play on a game not checked yet in this app run syncs it first, without asking
PASS: an upload fetches the cloud's copy of every file it replaces before the batch opens
PASS: the cloud's copies go to the backup's cloud/ folder
PASS: backups are in Documents (Files › Madeira › Steam Cloud Backups)
PASS: keeping this device's side leaves a missing save missing instead of uploading nothing
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-steam-cloud.py", line 148, in <module>
    build = subprocess.run([SWIFTC, '-O', str(src), '-o', str(out)], capture_output=True, text=True)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-steam-games.py

```text
PASS: SteamGames.swift: GPL-3.0-or-later, Copyright 2026 125hz, Converter Exception
PASS: SteamGames.swift is built by the Xcode project
PASS: Library: the Steam section is in the library and opens the library's Game details page
PASS: the section lists exactly what Dock's own discovery finds
PASS: an installed Steam game opens its Game details page (its library entry)
PASS: the section never starts Dock itself: Play is on the Game details page
PASS: a finished download's sheet offers Open, which opens the Game details page
PASS: Open presents the Game details page after the download sheet closes
PASS: a finished download (record written) gets its library entry; a failed or paused one does not
PASS: Uninstall removes the game's library entry with its files
PASS: Game details: the Steam section for a Steam game
PASS: Steam section: "Start with"
PASS: Steam section: "Madeira Dock"
PASS: Steam section: "Smaller JIT pool (512 MB) for this launch"
PASS: Steam section: "One-time installs"
PASS: Steam section: "Run at next start"
PASS: Steam section: "Skip"
PASS: Steam section: "Repair installed files"
PASS: Steam section: "Uninstall"
PASS: Steam section: "App ID"
PASS: Steam section: "Free space on this device"
PASS: Steam section: "Pause update"
PASS: Steam section: "Resume update"
PASS: Steam section: "The game"
PASS: Steam section: "Program"
PASS: Steam section: "Choose…"
PASS: Game details: "Library details"
PASS: Game details: "Choose cover image"
PASS: Game details: "Use Steam artwork"
PASS: Game details: "Display"
PASS: Game details: "Resolution"
PASS: Game details: "Aspect & scaling"
PASS: Game details: "Compatibility & performance"
PASS: Game details: "Reduced-precision x87"
PASS: Game details: "CPU cores reported"
PASS: Game details: "D3D9 anisotropic filtering"
PASS: Game details: "On screen"
PASS: Game details: "Performance overlay"
PASS: Game details: "Live logs"
PASS: Game details: "Touch controls"
PASS: Game details: "Control opacity"
PASS: Game details: "Control size"
PASS: Game details: "Executable"
PASS: Game details: "Game details"
PASS: no Launch arguments for a Steam game: Dock starts Steam's own launch option
PASS: Steam games are listed in the Steam section only, not also under Games
PASS: an installed game's card shows the library pills (and Update), any other state its own pill, in all three layouts (dense list, list, grid); no Dock or Steam pill
PASS: the pills in order: bits, graphics API, Update, then the size
PASS: an installed game's card reads its format through its library entry
PASS: the format is read again only for another install folder, build or picked program, once Steam's launch configuration is cached, or a day later while no program is known
PASS: the card reads again when Steam's launch configuration arrives
PASS: the program is the one "The game" starts; bits from its PE header, the API as for any library game
PASS: file reads off the main thread; the size is the install record's; the result is kept on the game's entry
PASS: [steam-games] metadata logs the App ID, bits and API only
PASS: a Steam game keeps one entry, and a details page saved later keeps the card's newer format
PASS: Play on a Steam game's Game details page starts it through Madeira Dock with its own profile
PASS: "The game": no program chosen, no start; otherwise the program is checked inside drive_c and started as a library game
PASS: "The game" hands no sign-in to anything
PASS: a Steam game's session takes its display, overlay and control settings
PASS: a Steam game's profile never replaces what Madeira Dock starts (only "The game" sets what starts)
PASS: the game's own Steam identity and working folder are exported for "The game" only, and cleared for every other launch
PASS: bridge: a direct start publishes its game's own identity once (digits only, a C: folder); every other launch keeps the previous identity
PASS: bridge: Steam's working folder applies to one launch, only as a C: folder of the prefix
PASS: CPU cores and anisotropic filtering are exported when chosen and cleared for the next game otherwise
PASS: SteamGames.swift: no setenv(
PASS: SteamGames.swift: no unsetenv(
PASS: SteamGames.swift: no runWineFullSequence
PASS: SteamGames.swift: no writeHandoff
PASS: SteamGames.swift: no credentialsForDock
PASS: SteamGames.swift: no SteamTokenStore
PASS: SteamGames.swift: no refreshToken
PASS: SteamGames.swift: no SecItem
PASS: SteamGames.swift: no MADEIRA_EXE
PASS: SteamGames.swift: no MADEIRA_ARGS
PASS: SteamGames.swift: no jit_
PASS: SteamGames.swift: no JITPool
PASS: SteamGames.swift: no poolSize
PASS: SteamGames.swift: no steamwebhelper
PASS: SteamGames.swift: no steam.exe
PASS: SteamGames.swift: no SteamSetup
PASS: SteamGames.swift: no FEX_
PASS: SteamGames.swift: no DXMT
PASS: SteamGames.swift: no program names
PASS: no account data, name or path in "LogStore.shared.log("[steam-games] installed=\(found.count) ready=\(fo"
PASS: no account data, name or path in "LogStore.shared.log("[steam-cloud] app=\(appID) quit-upload done files"
PASS: no account data, name or path in "SteamLog.event("[steam-cloud] setting on=\(on ? 1 : 0)")"
PASS: no account data, name or path in "LogStore.shared.log("[steam-start] app=\(entry.steamAppID ?? 0) mode=\"
PASS: no account data, name or path in "LogStore.shared.log("[steam-start] app=\(entry.steamAppID ?? 0) progra"
PASS: no account data, name or path in "LogStore.shared.log("[steam-start] app=\(appID) launch-entries=\(optio"
PASS: the rules are Foundation-only
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-steam-games.py", line 471, in <module>
    build = subprocess.run([SWIFTC, '-parse-as-library', '-swift-version', '5', '-sanitize=address', '-o', str(exe),
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

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
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-steam-library.py", line 366, in <module>
    VEC = {kind: steam_encrypt(KEY_MAIN, container(kind, VEC_PLAIN)).hex() for kind in ['zstd', 'lzma', 'zip']}
                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<workspace>\outputs\Madeira\tests\host\check-steam-library.py", line 244, in container
    from compression import zstd
ModuleNotFoundError: No module named 'compression'

```

## check-steam-signin-native.py

```text
PASS: SwiftSteam holds the sign-in files and, besides them, only the library files (check-steam-library.py lists those)
PASS: the only C sources in SwiftSteam are the content decoders
PASS: SwiftSteam/Auth/SteamAuthAPI.swift is built by the Xcode project
PASS: SwiftSteam/Auth/SteamAuthAPI.swift licence header
PASS: SwiftSteam/Auth/SteamAuthAPI.swift credits Jfishin
PASS: SwiftSteam/Auth/SteamAuthAPI.swift has no DepotDownloader
PASS: SwiftSteam/Auth/SteamAuthAPI.swift has no SteamSession
PASS: SwiftSteam/Auth/SteamAuthAPI.swift has no SteamConnection
PASS: SwiftSteam/Auth/SteamAuthAPI.swift has no CMsgClientLogon
PASS: SwiftSteam/Auth/SteamAuthAPI.swift has no ChannelEncrypt
PASS: SwiftSteam/Auth/SteamAuthAPI.swift has no PICS
PASS: SwiftSteam/Auth/SteamAuthAPI.swift has no appmanifest
PASS: SwiftSteam/Auth/SteamAuthAPI.swift has no steamclient64
PASS: SwiftSteam/Auth/SteamAuthAPI.swift has no steamclient.dll
PASS: SwiftSteam/Auth/SteamAuthAPI.swift has no LaunchApp
PASS: SwiftSteam/Auth/SteamAuthAPI.swift has no emulat
PASS: SwiftSteam/Auth/SteamAuthAPI.swift: no credential interpolated in "SteamLog.trace("\(method) eresult=\(code)")"
PASS: SwiftSteam/Auth/SteamCredentialAuth.swift is built by the Xcode project
PASS: SwiftSteam/Auth/SteamCredentialAuth.swift licence header
PASS: SwiftSteam/Auth/SteamCredentialAuth.swift credits Jfishin
PASS: SwiftSteam/Auth/SteamCredentialAuth.swift has no DepotDownloader
PASS: SwiftSteam/Auth/SteamCredentialAuth.swift has no SteamSession
PASS: SwiftSteam/Auth/SteamCredentialAuth.swift has no SteamConnection
PASS: SwiftSteam/Auth/SteamCredentialAuth.swift has no CMsgClientLogon
PASS: SwiftSteam/Auth/SteamCredentialAuth.swift has no ChannelEncrypt
PASS: SwiftSteam/Auth/SteamCredentialAuth.swift has no PICS
PASS: SwiftSteam/Auth/SteamCredentialAuth.swift has no appmanifest
PASS: SwiftSteam/Auth/SteamCredentialAuth.swift has no steamclient64
PASS: SwiftSteam/Auth/SteamCredentialAuth.swift has no steamclient.dll
PASS: SwiftSteam/Auth/SteamCredentialAuth.swift has no LaunchApp
PASS: SwiftSteam/Auth/SteamCredentialAuth.swift has no emulat
PASS: SwiftSteam/Auth/SteamQRAuth.swift is built by the Xcode project
PASS: SwiftSteam/Auth/SteamQRAuth.swift licence header
PASS: SwiftSteam/Auth/SteamQRAuth.swift credits Jfishin
PASS: SwiftSteam/Auth/SteamQRAuth.swift has no DepotDownloader
PASS: SwiftSteam/Auth/SteamQRAuth.swift has no SteamSession
PASS: SwiftSteam/Auth/SteamQRAuth.swift has no SteamConnection
PASS: SwiftSteam/Auth/SteamQRAuth.swift has no CMsgClientLogon
PASS: SwiftSteam/Auth/SteamQRAuth.swift has no ChannelEncrypt
PASS: SwiftSteam/Auth/SteamQRAuth.swift has no PICS
PASS: SwiftSteam/Auth/SteamQRAuth.swift has no appmanifest
PASS: SwiftSteam/Auth/SteamQRAuth.swift has no steamclient64
PASS: SwiftSteam/Auth/SteamQRAuth.swift has no steamclient.dll
PASS: SwiftSteam/Auth/SteamQRAuth.swift has no LaunchApp
PASS: SwiftSteam/Auth/SteamQRAuth.swift has no emulat
PASS: SwiftSteam/Auth/SteamTokenStore.swift is built by the Xcode project
PASS: SwiftSteam/Auth/SteamTokenStore.swift licence header
PASS: SwiftSteam/Auth/SteamTokenStore.swift credits Jfishin
PASS: SwiftSteam/Auth/SteamTokenStore.swift has no DepotDownloader
PASS: SwiftSteam/Auth/SteamTokenStore.swift has no SteamSession
PASS: SwiftSteam/Auth/SteamTokenStore.swift has no SteamConnection
PASS: SwiftSteam/Auth/SteamTokenStore.swift has no CMsgClientLogon
PASS: SwiftSteam/Auth/SteamTokenStore.swift has no ChannelEncrypt
PASS: SwiftSteam/Auth/SteamTokenStore.swift has no PICS
PASS: SwiftSteam/Auth/SteamTokenStore.swift has no appmanifest
PASS: SwiftSteam/Auth/SteamTokenStore.swift has no steamclient64
PASS: SwiftSteam/Auth/SteamTokenStore.swift has no steamclient.dll
PASS: SwiftSteam/Auth/SteamTokenStore.swift has no LaunchApp
PASS: SwiftSteam/Auth/SteamTokenStore.swift has no emulat
PASS: SwiftSteam/Auth/SteamTokenStore.swift: no credential interpolated in "SteamLog.trace("Failed to encode tokens for storage")"
PASS: SwiftSteam/Auth/SteamTokenStore.swift: no credential interpolated in "SteamLog.trace("Tokens saved to Keychain")"
PASS: SwiftSteam/Auth/SteamTokenStore.swift: no credential interpolated in "SteamLog.trace("Failed to save tokens to Keychain: \(status)"
PASS: SwiftSteam/Auth/SteamTokenStore.swift: no credential interpolated in "SteamLog.trace("Tokens cleared from Keychain")"
PASS: SwiftSteam/Content/ContentDecryptor.swift is built by the Xcode project
PASS: SwiftSteam/Content/ContentDecryptor.swift licence header
PASS: SwiftSteam/Content/ContentDecryptor.swift credits Jfishin
PASS: SwiftSteam/Content/DepotDownloader.swift is built by the Xcode project
PASS: SwiftSteam/Content/DepotDownloader.swift licence header
PASS: SwiftSteam/Content/DepotDownloader.swift credits Jfishin
PASS: SwiftSteam/Content/DepotDownloader.swift: no credential interpolated in "SteamLog.event("[steam-depot] selection app=\(app.appID) bui"
PASS: SwiftSteam/Content/DepotDownloader.swift: no credential interpolated in "SteamLog.event("[steam-depot] license app=\(app.appID) skipp"
PASS: SwiftSteam/Content/DepotDownloader.swift: no credential interpolated in "SteamLog.event("[steam-depot] install begin app=\(app.appID)"
PASS: SwiftSteam/Content/DepotDownloader.swift: no credential interpolated in "if !custom.isEmpty { SteamLog.event("[steam-record] custom-e"
PASS: SwiftSteam/Content/DepotDownloader.swift: no credential interpolated in "SteamLog.event("[steam-shared-record] app=\(app.appID) share"
PASS: SwiftSteam/Content/DepotDownloader.swift: no credential interpolated in "SteamLog.event("[steam-depot] install complete app=\(app.app"
PASS: SwiftSteam/Content/DepotDownloader.swift: no credential interpolated in "if file.flags & 0x200 == 0 { SteamLog.trace("rejected manife"
PASS: SwiftSteam/Content/DepotDownloader.swift: no credential interpolated in "SteamLog.trace("chunk attempt \(attempt + 1) failed: \(failu"
PASS: SwiftSteam/Content/DepotDownloader.swift: no credential interpolated in "SteamLog.trace("manifest from a content server failed: \(err"
PASS: SwiftSteam/Content/DepotDownloader.swift: no credential interpolated in "SteamLog.event("[steam-depot] depot-key refused app=\(appID)"
PASS: SwiftSteam/Content/DepotDownloader.swift: no credential interpolated in "SteamLog.event("[steam-cdn] offered=\(servers.count) usable="
PASS: SwiftSteam/Content/DepotDownloader.swift: no credential interpolated in "SteamLog.trace("content directory failed: \(error.localizedD"
PASS: SwiftSteam/Content/DepotDownloader.swift: no credential interpolated in "SteamLog.trace("content authorization request failed; contin"
PASS: SwiftSteam/Content/DepotDownloader.swift: no credential interpolated in "DispatchQueue.main.async { SteamLog.event("[steam-cdn] host "
PASS: SwiftSteam/Content/DepotManifest.swift is built by the Xcode project
PASS: SwiftSteam/Content/DepotManifest.swift licence header
PASS: SwiftSteam/Content/DepotManifest.swift credits Jfishin
PASS: SwiftSteam/Content/DepotManifest.swift: no credential interpolated in "SteamLog.trace("filename decrypt failed (\(why))")"
PASS: SwiftSteam/Core/CMServerList.swift is built by the Xcode project
PASS: SwiftSteam/Core/CMServerList.swift licence header
PASS: SwiftSteam/Core/CMServerList.swift credits Jfishin
PASS: SwiftSteam/Core/CMServerList.swift: no credential interpolated in "SteamLog.trace("CM directory unavailable, using cached serve"
PASS: SwiftSteam/Core/CMServerList.swift: no credential interpolated in "SteamLog.trace("Fetched \(servers.count) WebSocket CM server"
PASS: SwiftSteam/Core/LicenseListBox.swift is built by the Xcode project
PASS: SwiftSteam/Core/LicenseListBox.swift licence header
PASS: SwiftSteam/Core/LicenseListBox.swift credits Jfishin
PASS: SwiftSteam/Core/SteamCMSession.swift is built by the Xcode project
PASS: SwiftSteam/Core/SteamCMSession.swift licence header
PASS: SwiftSteam/Core/SteamConnection.swift is built by the Xcode project
PASS: SwiftSteam/Core/SteamConnection.swift licence header
PASS: SwiftSteam/Core/SteamConnection.swift credits Jfishin
PASS: SwiftSteam/Core/SteamConnection.swift: no credential interpolated in "SteamLog.trace("WS handshake complete — server protocol: \(`"
PASS: SwiftSteam/Core/SteamConnection.swift: no credential interpolated in "SteamLog.trace("WS server closed — code: \(closeCode.rawValu"
PASS: SwiftSteam/Core/SteamConnection.swift: no credential interpolated in "SteamLog.trace("WS task completed with error: \(error.locali"
PASS: SwiftSteam/Core/SteamConnection.swift: no credential interpolated in "SteamLog.trace("Connecting to CM: \(server.url)")"
PASS: SwiftSteam/Core/SteamConnection.swift: no credential interpolated in "SteamLog.trace("WebSocket connected — ready for protocol mes"
PASS: SwiftSteam/Core/SteamConnection.swift: no credential interpolated in "SteamLog.trace("unexpected text frame (\(text.utf8.count) by"
PASS: SwiftSteam/Core/SteamConnection.swift: no credential interpolated in "SteamLog.trace("WS receive error: \(error.localizedDescripti"
PASS: SwiftSteam/Core/SteamConnection.swift: no credential interpolated in "SteamLog.trace("Connection lost: \(error.localizedDescriptio"
PASS: SwiftSteam/Core/SteamConnection.swift: no credential interpolated in "SteamLog.trace("Connection closed cleanly")"
PASS: SwiftSteam/Core/SteamConnection.swift: no credential interpolated in "SteamLog.trace("Disconnected")"
PASS: SwiftSteam/Core/SteamError.swift is built by the Xcode project
PASS: SwiftSteam/Core/SteamError.swift licence header
PASS: SwiftSteam/Core/SteamError.swift credits Jfishin
PASS: SwiftSteam/Core/SteamMessageCodec.swift is built by the Xcode project
PASS: SwiftSteam/Core/SteamMessageCodec.swift licence header
PASS: SwiftSteam/Core/SteamMessageCodec.swift credits Jfishin
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no credential interpolated in "SteamLog.trace("Message too small (\(data.count) bytes)")"
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no credential interpolated in "SteamLog.trace("Invalid protobuf header length \(headerLengt"
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no credential interpolated in "SteamLog.trace("Unknown protobuf EMsg \(eMsgValue) (\(body.c"
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no credential interpolated in "SteamLog.trace("Non-protobuf message too small: \(data.count"
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no credential interpolated in "SteamLog.trace("Non-protobuf message smaller than header: \("
PASS: SwiftSteam/Core/SteamMessageCodec.swift: no credential interpolated in "SteamLog.trace("Non-protobuf EMsg \(eMsgValue) (header=\(hea"
PASS: SwiftSteam/Core/SteamProtocol.swift is built by the Xcode project
PASS: SwiftSteam/Core/SteamProtocol.swift licence header
PASS: SwiftSteam/Core/SteamProtocol.swift credits Jfishin
PASS: SwiftSteam/Core/SteamSession.swift is built by the Xcode project
PASS: SwiftSteam/Core/SteamSession.swift licence header
PASS: SwiftSteam/Core/SteamSession.swift credits Jfishin
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("ClientLicenseList: parsed \(packageIDs.count"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("ClientLicenseList deserialize FAILED (body \"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("Sent ClientHello (\(helloData.count) bytes)""
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("Logon attempt \(attempt)/2 — reconnecting to"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("Sent ClientHello to new server (attempt \(at"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("TryAnotherCM on attempt \(attempt) — will tr"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("Timeout on attempt \(attempt) — will try dif"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("Idle timeout — disconnecting to release the "
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("ClientLogonResponse: eresult=\(eResultCode)""
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("Server says TryAnotherCM — will reconnect to"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("Logon completed during a game session: logge"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("Authenticated")"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("Got ClientLoggedOff during logon")"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("Sent ClientLogon, waiting for response")"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("ClientLogon timed out after 20s: no response"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("Session disconnected")"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("\(method.rawValue) header eresult=\(response"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("Failed to decode message (\(data.count) byte"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("← \(Self.messageName(message.rawEMsg)) (\(me"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("ServiceMethodResponse not matched: jobTarget"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("Failed to decompress multi message")"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("Failed to parse multi message: \(error)")"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("Received ClientLoggedOff")"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("Late ClientLogOnResponse: eresult=\(eResult)"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("Unhandled EMsg \(message.rawEMsg) (\(message"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("Heartbeat failed: \(error)")"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("Connection lost\(error.map { ": \($0.localiz"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("Reconnecting in \(Int(delay))s (attempt \(re"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("Reconnected successfully")"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("Reconnection failed: \(error)")"
PASS: SwiftSteam/Core/SteamSession.swift: no credential interpolated in "SteamLog.trace("Max reconnection attempts reached")"
PASS: SwiftSteam/Helpers/SteamDevice.swift is built by the Xcode project
PASS: SwiftSteam/Helpers/SteamDevice.swift licence header
PASS: SwiftSteam/Helpers/SteamDevice.swift credits Jfishin
PASS: SwiftSteam/Helpers/SteamDevice.swift has no DepotDownloader
PASS: SwiftSteam/Helpers/SteamDevice.swift has no SteamSession
PASS: SwiftSteam/Helpers/SteamDevice.swift has no SteamConnection
PASS: SwiftSteam/Helpers/SteamDevice.swift has no CMsgClientLogon
PASS: SwiftSteam/Helpers/SteamDevice.swift has no ChannelEncrypt
PASS: SwiftSteam/Helpers/SteamDevice.swift has no PICS
PASS: SwiftSteam/Helpers/SteamDevice.swift has no appmanifest
PASS: SwiftSteam/Helpers/SteamDevice.swift has no steamclient64
PASS: SwiftSteam/Helpers/SteamDevice.swift has no steamclient.dll
PASS: SwiftSteam/Helpers/SteamDevice.swift has no LaunchApp
PASS: SwiftSteam/Helpers/SteamDevice.swift has no emulat
PASS: SwiftSteam/Helpers/SteamLog.swift is built by the Xcode project
PASS: SwiftSteam/Helpers/SteamLog.swift licence header
PASS: SwiftSteam/Helpers/SteamLog.swift has no DepotDownloader
PASS: SwiftSteam/Helpers/SteamLog.swift has no SteamSession
PASS: SwiftSteam/Helpers/SteamLog.swift has no SteamConnection
PASS: SwiftSteam/Helpers/SteamLog.swift has no CMsgClientLogon
PASS: SwiftSteam/Helpers/SteamLog.swift has no ChannelEncrypt
PASS: SwiftSteam/Helpers/SteamLog.swift has no PICS
PASS: SwiftSteam/Helpers/SteamLog.swift has no appmanifest
PASS: SwiftSteam/Helpers/SteamLog.swift has no steamclient64
PASS: SwiftSteam/Helpers/SteamLog.swift has no steamclient.dll
PASS: SwiftSteam/Helpers/SteamLog.swift has no LaunchApp
PASS: SwiftSteam/Helpers/SteamLog.swift has no emulat
PASS: SwiftSteam/Helpers/SteamLog.swift: no credential interpolated in "// LogStore, not stderr: stderr is only captured into the lo"
PASS: SwiftSteam/Helpers/SteamLog.swift: no credential interpolated in "LogStore.shared.log("[steam-trace] " + message())"
PASS: SwiftSteam/Helpers/SteamLog.swift: no credential interpolated in "LogStore.shared.log(message)"
PASS: SwiftSteam/Install/AppManifestWriter.swift is built by the Xcode project
PASS: SwiftSteam/Install/AppManifestWriter.swift licence header
PASS: SwiftSteam/Install/AppManifestWriter.swift credits Jfishin
PASS: SwiftSteam/Library/SteamAppInfo.swift is built by the Xcode project
PASS: SwiftSteam/Library/SteamAppInfo.swift licence header
PASS: SwiftSteam/Library/SteamAppInfo.swift credits Jfishin
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift is built by the Xcode project
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift licence header
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift credits Jfishin
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no credential interpolated in "SteamLog.trace("Fetching license list...")"
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no credential interpolated in "SteamLog.trace("Got \(packageIDs.count) owned packages")"
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no credential interpolated in "SteamLog.trace("Found \(appIDs.count) unique app IDs")"
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no credential interpolated in "SteamLog.trace("Got info for \(appInfos.count) apps")"
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no credential interpolated in "SteamLog.trace("\(games.count) of \(appInfos.count) apps are"
PASS: SwiftSteam/Library/SteamLibraryFetcher.swift: no credential interpolated in "SteamLog.event("[steam-shared] app=\(appID) owners=\(visited"
PASS: SwiftSteam/Proto/SteamProtoMessages.swift is built by the Xcode project
PASS: SwiftSteam/Proto/SteamProtoMessages.swift licence header
PASS: SwiftSteam/Proto/SteamProtoMessages.swift credits Jfishin
PASS: SwiftSteam/SteamSignIn.swift is built by the Xcode project
PASS: SwiftSteam/SteamSignIn.swift licence header
PASS: SwiftSteam/SteamSignIn.swift credits Jfishin
PASS: SwiftSteam/SteamSignIn.swift has no DepotDownloader
PASS: SwiftSteam/SteamSignIn.swift has no SteamSession
PASS: SwiftSteam/SteamSignIn.swift has no SteamConnection
PASS: SwiftSteam/SteamSignIn.swift has no CMsgClientLogon
PASS: SwiftSteam/SteamSignIn.swift has no ChannelEncrypt
PASS: SwiftSteam/SteamSignIn.swift has no PICS
PASS: SwiftSteam/SteamSignIn.swift has no appmanifest
PASS: SwiftSteam/SteamSignIn.swift has no steamclient64
PASS: SwiftSteam/SteamSignIn.swift has no steamclient.dll
PASS: SwiftSteam/SteamSignIn.swift has no LaunchApp
PASS: SwiftSteam/SteamSignIn.swift has no emulat
PASS: SwiftSteam/SteamSignIn.swift: no credential interpolated in "SteamLog.event("[steam-signin] signed out")"
PASS: SwiftSteam/SteamSignIn.swift: no credential interpolated in "SteamLog.event("[steam-signin] sign-in failed method=\(metho"
PASS: SwiftSteam/SteamSignIn.swift: no credential interpolated in "SteamLog.event("[steam-signin] sign-in keychain-store failed"
PASS: SwiftSteam/SteamSignIn.swift: no credential interpolated in "SteamLog.event("[steam-signin] signed in method=\(method)")"
PASS: SwiftSteam/SteamSignInView.swift is built by the Xcode project
PASS: SwiftSteam/SteamSignInView.swift licence header
PASS: SwiftSteam/SteamSignInView.swift has no DepotDownloader
PASS: SwiftSteam/SteamSignInView.swift has no SteamSession
PASS: SwiftSteam/SteamSignInView.swift has no SteamConnection
PASS: SwiftSteam/SteamSignInView.swift has no CMsgClientLogon
PASS: SwiftSteam/SteamSignInView.swift has no ChannelEncrypt
PASS: SwiftSteam/SteamSignInView.swift has no PICS
PASS: SwiftSteam/SteamSignInView.swift has no appmanifest
PASS: SwiftSteam/SteamSignInView.swift has no steamclient64
PASS: SwiftSteam/SteamSignInView.swift has no steamclient.dll
PASS: SwiftSteam/SteamSignInView.swift has no LaunchApp
PASS: SwiftSteam/SteamSignInView.swift has no emulat
PASS: Keychain item stays on this device, available while unlocked
PASS: Keychain item is not synchronised
PASS: the password field is cleared after submitting
PASS: developer interface opens the sheet
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-steam-signin-native.py", line 302, in <module>
    build = subprocess.run([SWIFTC, '-parse-as-library', '-swift-version', '5', '-sanitize=address', '-o', str(exe)] + [str(s) for s in sources])
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-swap-coverage.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-swap-coverage.py", line 469, in <module>
    subprocess.run(['cc', '-O1', '-Wall', '-Wno-unused-function', '-Werror', '-o', str(exe), str(c)], check=True)
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-touch-gamepad.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-touch-gamepad.py", line 113, in <module>
    subprocess.run([os.environ.get('SWIFTC', 'swiftc'), str(src), '-o', str(exe)], check=True)
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-unixlib-binder.py

```text
PASS: every branch keeps upstream's 64-bit table and offers its own 32-bit table (winemetal included); no 64-bit table reaches a 32-bit caller; the mapped-file fallback is 32-bit only
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-unixlib-binder.py", line 161, in <module>
    subprocess.run(["cc", "-std=gnu11", "-Wall", "-Wno-unused-function", "-fsanitize=address,undefined",
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-wg-parser.py

```text
PASS: call tables match enum unix_funcs; wow64 thunks; kill switches (MADEIRA_WG_PARSER, MADEIRA_WG_VIDEO); Apple backend built/archived/linked; FFmpeg has mov and no H.264/HEVC/AAC decoder
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-wg-parser.py", line 1095, in <module>
    subprocess.run(["cc", "-std=gnu11", "-O1", "-g", "-Wall", "-Wno-unused-function", "-fsanitize=address,undefined",
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-win32u-zero-bits.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-win32u-zero-bits.py", line 58, in <module>
    subprocess.run(["cc", "-std=gnu11", "-Wall", "-Wno-unused-function", "-pthread",
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-wine-mono.py

```text
PASS: the version is pin.sh's (11.0.0)
PASS: the tarball hash is pin.sh's
PASS: both mscorlib hashes are pin.sh's
PASS: the URL is the one fetch.sh downloads
PASS: the mscorlib patch is bundle.sh's (offset, context, bytes)
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-wine-mono.py", line 113, in <module>
    built = subprocess.run(['xcrun', 'swiftc', '-O', str(tmp / 'driver.swift'), '-o', str(tmp / 'driver')],
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-wma-decoder.py

```text
SKIP-FAIL: <workspace>\outputs\Madeira\wine\build-macos\include\config.h is missing; point MADEIRA_WINE_BUILD at a configured Wine tree

```

## check-wow-context.py

```text
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-wow-context.py", line 48, in <module>
    subprocess.run(["cc", "-std=gnu11", "-Wall", str(c), "-o", str(Path(t) / "layout")], check=True)
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-wow-cpu-area.py

```text
PASS: both syscall exits flush the CPU area before unlocking; LockJITContext consumes RESET_STATE first
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-wow-cpu-area.py", line 120, in <module>
    subprocess.run(["c++", "-std=c++20", "-DFEX_IOS_HOST", "-O1", "-g", "-fsanitize=address,undefined",
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```

## check-wow-sweep.py

```text
PASS: syscall tail, entry stub, park/unpark placement, registration and sweeper flag invariants
Traceback (most recent call last):
  File "<workspace>\outputs\Madeira\tests\host\check-wow-sweep.py", line 167, in <module>
    subprocess.run(["c++", "-std=c++20", "-O1", "-g", "-fsanitize=address,undefined", "-fno-omit-frame-pointer",
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<user>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified

```
