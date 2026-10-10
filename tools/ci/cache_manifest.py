#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# Madeira Converter Exception: see LICENSE-EXCEPTION.md
"""Seal/verify an exact dependency output set against its build-input digest."""
import argparse
import hashlib
import json
from pathlib import Path


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def inventory(root):
    result = {}
    for path in sorted(root.rglob('*')):
        if path.is_symlink():
            raise ValueError(f'cache symlink is not allowed: {path}')
        if path.is_file():
            result[path.relative_to(root).as_posix()] = digest(path)
    if not result:
        raise ValueError('empty cache payload')
    return result


def seal(root, inputs):
    record = dict(schema=1, inputs_sha256=digest(inputs), files=inventory(root/'payload'))
    (root/'manifest.json').write_text(json.dumps(record, indent=2)+'\n', encoding='utf-8')


def verify(root, inputs):
    record = json.loads((root/'manifest.json').read_text(encoding='utf-8'))
    if record.get('schema') != 1 or record.get('inputs_sha256') != digest(inputs):
        raise ValueError('cache build inputs do not match this runner/recipe')
    if record.get('files') != inventory(root/'payload'):
        raise ValueError('cache file set or SHA-256 mismatch')
    print(f"Verified {len(record['files'])} cached dependency files.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['seal', 'verify'])
    parser.add_argument('root', type=Path)
    parser.add_argument('inputs', type=Path)
    args = parser.parse_args()
    try:
        (seal if args.operation == 'seal' else verify)(args.root, args.inputs)
    except (OSError, ValueError) as error:
        parser.exit(1, f'error: {error}\n')


if __name__ == '__main__':
    main()
