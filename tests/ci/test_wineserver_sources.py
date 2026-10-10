# SPDX-License-Identifier: GPL-3.0-or-later
# Madeira Converter Exception: see LICENSE-EXCEPTION.md
import importlib.util
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('sources', ROOT/'build/wineserver/sources.py')
sources = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sources)


class WineserverSourcesTest(unittest.TestCase):
    def test_apple_index_is_metadata_but_all_objects_are_exact(self):
        rows = [('first', 'first.c'), ('second', 'second.c')]
        members = ['__.SYMDEF SORTED', 'first.o', 'second.o']
        sources.verify_members(members, rows)
        for bad in (members[:-1], members + ['stale.o'], members + ['first.o'],
                    members[:1] + members[1:][::-1], members[1:]):
            with self.subTest(members=bad), self.assertRaises(ValueError):
                sources.verify_members(bad, rows)

    def fixture(self, root):
        makefile = root/'wine/server/Makefile.in'
        makefile.parent.mkdir(parents=True)
        makefile.write_text('SOURCES = \\\n' + ''.join(f'\t{x}.c \\\n' for x in sources.STANDARD))
        for name in sources.STANDARD:
            _, path = sources.REPLACEMENTS.get(name, (name, f'wine/server/{name}.c'))
            (root/path).parent.mkdir(parents=True, exist_ok=True)
            (root/path).touch()
        for _, path in sources.EXTRAS:
            (root/path).parent.mkdir(parents=True, exist_ok=True)
            (root/path).touch()
        return makefile

    def test_complete_and_replacements_not_duplicates(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.fixture(root)
            rows = sources.plan(root)
            self.assertEqual(len(rows), 48)
            self.assertEqual(dict(rows)['process_ios'], 'wine/server/process.c')
            self.assertNotIn('main', dict(rows))
            self.assertIn(('main_ios', 'build/wineserver/main_ios.c'), rows)
            self.assertEqual(rows[-1][0], 'wineserver_ios_kill')

    def test_wine_addition_cannot_silently_go_unbuilt(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            makefile = self.fixture(root)
            with makefile.open('a') as f:
                f.write('\tnew_server.c\n')
            with self.assertRaisesRegex(ValueError, 'source list changed'):
                sources.plan(root)

    def test_missing_replacement_cannot_fall_back_to_old_object(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.fixture(root)
            (root/'build/wineserver/main_ios.c').unlink()
            with self.assertRaises(FileNotFoundError):
                sources.plan(root)

    @unittest.skipUnless(os.name == 'posix' and shutil.which('bash'), 'requires POSIX shell')
    def test_compiler_or_objcopy_failure_preserves_existing_archive(self):
        for failure in ('compiler', 'objcopy'):
            with self.subTest(failure=failure), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.fixture(root)
                build = root/'build/wineserver'
                for name in ('build.sh', 'sources.py'):
                    shutil.copyfile(ROOT/'build/wineserver'/name, build/name)
                target = root/'app/Madeira/libwineserver.a'
                target.parent.mkdir(parents=True)
                target.write_bytes(b'known working archive')
                bindir = root/'bin'
                bindir.mkdir()
                marker = root/'archive-called'
                xcrun = '''#!/bin/bash
case "$*" in
    *--show-sdk-path*) echo /mock-sdk; exit 0;;
    *clang*)
        if [ "$FAIL_STAGE" = compiler ]; then echo injected-compiler-error >&2; exit 42; fi
        while [ "$1" != -o ]; do shift; done
        printf mock-object > "$2"; exit 0;;
    *ar*) touch "$ARCHIVE_MARKER"; exit 0;;
esac
exit 0
'''
                for name, content in [('xcrun', xcrun), ('llvm-objcopy', '#!/bin/sh\necho injected-objcopy-error >&2\nexit 43\n')]:
                    (bindir/name).write_text(content)
                    (bindir/name).chmod(0o755)
                env = dict(os.environ, PATH=str(bindir)+os.pathsep+os.environ['PATH'],
                           FAIL_STAGE=failure, ARCHIVE_MARKER=str(marker))
                result = subprocess.run(['bash', str(build/'build.sh')], env=env, capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(f'injected-{failure}-error', result.stderr)
                self.assertEqual(target.read_bytes(), b'known working archive')
                self.assertFalse(marker.exists())


if __name__ == '__main__':
    unittest.main()
