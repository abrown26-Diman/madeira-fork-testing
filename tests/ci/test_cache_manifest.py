# SPDX-License-Identifier: GPL-3.0-or-later
# Madeira Converter Exception: see LICENSE-EXCEPTION.md
import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('cache_manifest', Path(__file__).resolve().parents[2]/'tools/ci/cache_manifest.py')
cache = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cache)


class CacheIntegrityTest(unittest.TestCase):
    def test_unchanged_cache_and_rejected_mutations(self):
        for mutation in ['none', 'inputs', 'changed', 'missing', 'extra']:
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)/'cache'
                (root/'payload/lib').mkdir(parents=True)
                lib = root/'payload/lib/test.a'
                lib.write_bytes(b'completed library')
                inputs = Path(tmp)/'inputs'
                inputs.write_text('pinned source + compiler + SDK + flags', encoding='utf-8')
                cache.seal(root, inputs)
                if mutation == 'inputs': inputs.write_text('different SDK', encoding='utf-8')
                if mutation == 'changed': lib.write_bytes(b'corrupt or stale')
                if mutation == 'missing': lib.unlink()
                if mutation == 'extra': (root/'payload/lib/stale.a').write_bytes(b'stale')
                if mutation == 'none':
                    cache.verify(root, inputs)
                else:
                    with self.assertRaises(ValueError): cache.verify(root, inputs)


if __name__ == '__main__':
    unittest.main()
