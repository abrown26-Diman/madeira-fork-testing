#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# Madeira Converter Exception: see LICENSE-EXCEPTION.md
"""Validate staged resources and native executable before IPA packaging."""
import argparse
import hashlib
import json
from pathlib import Path
import plistlib
import subprocess

ROOT = Path(__file__).resolve().parents[2]
REQUIRED = [
    'Madeira', 'Info.plist', 'prefix-template.tar.gz', 'madeira-jit.js',
    'cacert.pem', 'Madeira JIT.shortcut', 'Assets.car',
    'Frameworks/StikJIT.framework/StikJIT',
    'PlugIns/MadeiraJITHelper.appex/MadeiraJITHelper',
    'd3d12/libmetalirconverter.dylib',
    'arm64ec-windows/ntdll.dll', 'arm64ec-windows/xtajit64.dll',
    'arm64ec-windows/d3d11.dll', 'arm64ec-windows/dxgi.dll',
    'arm64ec-windows/d3d12.dll', 'arm64ec-windows/madeira_d3d12.dll',
    'arm64ec-windows/dockhost.exe',
    'aarch64-windows/ntdll.dll', 'aarch64-windows/xtajit.dll',
    'aarch64-windows/wow64.dll', 'aarch64-windows/wow64win.dll',
    'i386-windows/ntdll.dll', 'i386-windows/kernel32.dll', 'i386-windows/d3d11.dll',
    'licenses/LICENSE-MADEIRA-GPL-3.0.txt', 'licenses/LICENSE-MADEIRA-EXCEPTION.txt',
]


def validate_resources(app, source):
    for name in REQUIRED:
        p = app/name
        if not p.is_file() or not p.stat().st_size:
            raise ValueError(f'missing/empty package component: {name}')
    if list((app/'x86_64-vcruntime').glob('*.dll')):
        raise ValueError('Microsoft runtime DLLs must not be included by CI')
    # Every staged PE, NLS and licence resource must survive Xcode's copy phases.
    for folder in ('arm64ec-windows', 'aarch64-windows', 'i386-windows', 'nls', 'licenses', 'legal'):
        if not (source/folder).is_dir() or not any((source/folder).iterdir()):
            raise ValueError(f'empty source resource directory: {folder}')
        for p in (source/folder).rglob('*'):
            if p.is_file() and not p.name.startswith('.'):
                rel = p.relative_to(source)
                if not (app/rel).is_file() or p.read_bytes() != (app/rel).read_bytes():
                    raise ValueError(f'package resource differs from staged input: {rel}')
    with (app/'Info.plist').open('rb') as f:
        info = plistlib.load(f)
    if info.get('CFBundleExecutable') != 'Madeira':
        raise ValueError('incorrect CFBundleExecutable')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('app', type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    validate_resources(args.app, ROOT/'app/Madeira')
    native = ['Madeira', 'Frameworks/StikJIT.framework/StikJIT',
              'PlugIns/MadeiraJITHelper.appex/MadeiraJITHelper', 'd3d12/libmetalirconverter.dylib']
    evidence = {}
    for name in native:
        path = args.app/name
        subprocess.run(['xcrun', 'lipo', str(path), '-verify_arch', 'arm64'], check=True)
        evidence[name] = subprocess.check_output(['xcrun', 'otool', '-L', str(path)], text=True)
    files = {p.relative_to(args.app).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
             for p in sorted(args.app.rglob('*')) if p.is_file()}
    args.output.write_text(json.dumps({'schema_version': 1, 'sha256': files, 'native_dependencies': evidence,
                                     'signed_for_installation': False}, indent=2) + '\n')


if __name__ == '__main__':
    main()
