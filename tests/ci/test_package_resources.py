# SPDX-License-Identifier: GPL-3.0-or-later
# Madeira Converter Exception: see LICENSE-EXCEPTION.md
import importlib.util
from pathlib import Path
import plistlib
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('verify_app', ROOT/'tools/ci/verify_app.py')
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)


class PackageTest(unittest.TestCase):
    def fixture(self, root):
        app, source = root/'app', root/'source'
        for name in verify.REQUIRED + ['nls/l_intl.nls', 'legal/NOTICE.txt']:
            for base in (app, source):
                p = base/name
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_bytes(b'fixture resource')
        (app/'Info.plist').write_bytes(plistlib.dumps({'CFBundleExecutable': 'Madeira'}))
        return app, source

    def test_complete_resources(self):
        with tempfile.TemporaryDirectory() as tmp:
            app, source = self.fixture(Path(tmp))
            verify.validate_resources(app, source)

    def test_missing_wow64_core_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            app, source = self.fixture(Path(tmp))
            (app/'aarch64-windows/xtajit.dll').unlink()
            with self.assertRaisesRegex(ValueError, 'missing/empty'):
                verify.validate_resources(app, source)

    def test_xcode_copy_of_stale_resource_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            app, source = self.fixture(Path(tmp))
            (app/'nls/l_intl.nls').write_bytes(b'stale')
            with self.assertRaisesRegex(ValueError, 'differs'):
                verify.validate_resources(app, source)

    def test_proprietary_runtime_cannot_be_bundled_accidentally(self):
        with tempfile.TemporaryDirectory() as tmp:
            app, source = self.fixture(Path(tmp))
            (app/'x86_64-vcruntime').mkdir()
            (app/'x86_64-vcruntime/vcruntime140.dll').touch()
            with self.assertRaisesRegex(ValueError, 'Microsoft runtime'):
                verify.validate_resources(app, source)


if __name__ == '__main__':
    unittest.main()
