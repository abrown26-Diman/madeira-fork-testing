# SPDX-License-Identifier: GPL-3.0-or-later
# Madeira Converter Exception: see LICENSE-EXCEPTION.md
"""Exercise the wrapper with a failed existing cache and fail-closed configure."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]


@unittest.skipUnless(os.name == 'posix' and shutil.which('bash'), 'requires POSIX bash; runs in Linux/macOS CI')
class FEXConfigureTest(unittest.TestCase):
    def test_reconfigure_failed_cache_and_propagate_errors(self):
        for fail in [False, True]:
            with self.subTest(fail=fail), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                script = root/'build/fex-ios/build.sh'
                script.parent.mkdir(parents=True)
                shutil.copyfile(ROOT/'build/fex-ios/build.sh', script)
                build = root/'FEX/build-ios'
                build.mkdir(parents=True)
                (build/'CMakeCache.txt').write_text('old failed configure\n')
                bindir = root/'bin'
                bindir.mkdir()
                command = bindir/'cmake'
                command.write_text('''#!/bin/bash
printf '%s\\n' "$*" >> "$CALL_LOG"
[[ " $* " == *" -DCMAKE_SYSTEM_NAME=iOS "* ]] || exit 40
[[ " $* " == *" -DCMAKE_SYSTEM_PROCESSOR=arm64 "* ]] || exit 41
[[ " $* " == *" -DCMAKE_OSX_ARCHITECTURES=arm64 "* ]] || exit 42
exit "$FAIL_CONFIGURE"
''')
                command.chmod(0o755)
                log = root/'calls'
                env = dict(os.environ, PATH=str(bindir)+os.pathsep+os.environ['PATH'], CALL_LOG=str(log), FAIL_CONFIGURE='47' if fail else '0')
                result = subprocess.run(['bash', str(script), '--configure-only'], env=env, capture_output=True, text=True)
                self.assertEqual(result.returncode, 47 if fail else 0, result.stderr)
                self.assertEqual(len(log.read_text().splitlines()), 1)


if __name__ == '__main__':
    unittest.main()
