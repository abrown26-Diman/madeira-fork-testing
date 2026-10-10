# SPDX-License-Identifier: GPL-3.0-or-later
# Madeira Converter Exception: see LICENSE-EXCEPTION.md
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('sources', ROOT/'build/wineserver/sources.py')
sources = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sources)


class WineserverSourcesTest(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
