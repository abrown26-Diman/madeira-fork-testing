# SPDX-License-Identifier: GPL-3.0-or-later
# Madeira Converter Exception: see LICENSE-EXCEPTION.md
"""Fault injection: a failed compile must never archive yesterday's objects."""
from pathlib import Path
import os
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]


@unittest.skipUnless(os.name == 'posix' and shutil.which('bash'), 'requires POSIX bash; runs in Linux/macOS CI')
class BuildFailureTest(unittest.TestCase):
    def test_compile_failure_preserves_archive_and_negative_control_detects_old_bug(self):
        script = (ROOT/'build/ntdll-unix/build.sh').read_text()
        start = script.index('if [ "$FAILED" -gt 0 ]; then')
        end = script.index('\nfi', start) + len('\nfi')
        for guarded, source in [(True, script), (False, script[:start] + script[end:])]:
            with self.subTest(guarded=guarded), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                build = root/'build/ntdll-unix'
                build.mkdir(parents=True)
                (build/'build.sh').write_text(source)
                # Satisfy the unrelated code-generation prerequisite so both
                # controls reach the compiler/archive behavior under test.
                generator = root/'build/crypto-unix/gen_gnutls_symtab.sh'
                generator.parent.mkdir(parents=True)
                generator.write_text('#!/bin/sh\nexit 0\n')
                generator.chmod(0o755)
                wine_source = root/'wine/dlls/ntdll/unix/file.c'
                wine_source.parent.mkdir(parents=True)
                wine_source.write_text('/* fake compiler input */\n')
                (root/'app/Madeira').mkdir(parents=True)
                target = root/'app/Madeira/libntdll_unix.a'
                target.write_bytes(b'known baseline')
                bindir = root/'bin'
                bindir.mkdir()
                commands = {
                    'xcrun': '#!/bin/sh\ncase "$*" in *--show-sdk-path*) echo /mock-sdk; exit 0;; esac\necho "injected compiler failure" >&2\nexit 42\n',
                    'ar': '#!/bin/sh\necho archived >> "$MOCK_ARCHIVE_LOG"\nprintf stale > "$2"\n',
                }
                for name, text in commands.items():
                    tool = bindir/name
                    tool.write_text(text)
                    tool.chmod(0o755)
                marker = root/'archive-called'
                env = dict(os.environ, PATH=str(bindir)+os.pathsep+os.environ['PATH'], MOCK_ARCHIVE_LOG=str(marker))
                result = subprocess.run(['bash', str(build/'build.sh')], env=env, capture_output=True, text=True)
                if guarded:
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn('existing archives were not updated', result.stderr)
                    self.assertFalse(marker.exists())
                    self.assertEqual(target.read_bytes(), b'known baseline')
                else:
                    # The test must catch the old behavior, not just any failed build.
                    self.assertTrue(marker.exists(), result.stdout + result.stderr)
                    self.assertEqual(target.read_bytes(), b'stale')


if __name__ == '__main__':
    unittest.main()
