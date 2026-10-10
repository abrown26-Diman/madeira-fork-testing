#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# Madeira Converter Exception: see LICENSE-EXCEPTION.md
"""Complete server object plan. Refuse unreviewed Wine source-list changes."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
STANDARD = """async atom change class clipboard completion console d3dkmt debugger
device directory event fd file handle hook inproc_sync mach mailslot main mapping
mutex named_pipe object process procfs ptrace queue region registry request semaphore
serial signal sock symlink thread timer token trace unicode user window winstation""".split()
REPLACEMENTS = {
    name: (name + "_ios", f"build/wineserver/{name}_ios.c")
    for name in ("request", "main", "mach", "unicode", "fd")
}
REPLACEMENTS.update({name: (name, f"build/wineserver/{name}_ios.c")
                     for name in ("window", "mapping", "queue")})
REPLACEMENTS["process"] = ("process_ios", "wine/server/process.c")
EXTRAS = [
    ("wine_log_ios", "build/wineserver/wine_log_ios.c"),
    ("hidpad_ios", "build/wineserver/hidpad_ios.c"),
    ("hidparse_ios", "build/hidpad/hidparse_ios.c"),
    ("wineserver_ios_kill", "build/wineserver/wineserver_ios_kill.c"),
]


def plan(root=ROOT):
    makefile = (root / "wine/server/Makefile.in").read_text()
    actual = re.findall(r"^\s+(\w+)\.c\b", makefile, re.MULTILINE)
    if actual != STANDARD:
        raise ValueError(f"Wine server source list changed: expected {STANDARD}, got {actual}")
    rows = [REPLACEMENTS.get(name, (name, f"wine/server/{name}.c")) for name in STANDARD] + EXTRAS
    if len({name for name, _ in rows}) != len(rows):
        raise ValueError("duplicate archive member")
    for _, source in rows:
        if not (root / source).is_file():
            raise FileNotFoundError(source)
    return rows


if __name__ == "__main__":
    for name, source in plan():
        print(f"{name}\t{source}")
