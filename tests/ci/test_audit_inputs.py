# SPDX-License-Identifier: GPL-3.0-or-later
# Madeira Converter Exception: see LICENSE-EXCEPTION.md
"""Exercise provenance inspection on tiny real Git repositories."""
import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[2] / 'tools/ci/audit_inputs.py'
spec = importlib.util.spec_from_file_location('audit_inputs', SCRIPT)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class AuditTests(unittest.TestCase):
    def git(self, root, *args):
        return subprocess.check_output(['git', '-C', str(root), '-c', 'user.name=Test fixture',
                                       '-c', 'user.email=fixture@example.invalid', '-c', 'core.autocrlf=false',
                                       *args], stderr=subprocess.PIPE, text=True).strip()

    def repository(self, root):
        root.mkdir(parents=True, exist_ok=True)
        self.git(root, 'init')
        (root/'marker').write_text('fixture\n')
        self.git(root, 'add', 'marker')
        self.git(root, 'commit', '-m', 'fixture')
        return self.git(root, 'rev-parse', 'HEAD')

    def link(self, root, path, sha):
        self.git(root, 'update-index', '--add', '--cacheinfo', '160000,'+sha+','+path)
        self.git(root, 'commit', '-m', 'pin dependency')

    def test_uninitialized_gitlink_does_not_resolve_parent_head(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            sha = self.repository(root)
            self.link(root, 'child', sha)
            (root/'child').mkdir()
            row, = audit.revisions(root)
            self.assertEqual(row['expected'], sha)
            self.assertIsNone(row['actual'])
            self.assertIsNone(row['dirty'])

    def test_nested_pin_and_dirty_tracking(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.repository(root)
            child = root/'child'
            self.repository(child)
            nested_sha = self.repository(child/'nested')
            self.link(child, 'nested', nested_sha)
            child_sha = self.git(child, 'rev-parse', 'HEAD')
            self.link(root, 'child', child_sha)
            clean = audit.revisions(root)
            self.assertEqual([r['path'] for r in clean], ['child', 'child/nested'])
            self.assertTrue(all(r['actual'] == r['expected'] and not r['dirty'] for r in clean))
            (child/'marker').write_text('changed\n')
            self.assertTrue(audit.revisions(root)[0]['dirty'])

    def test_binary_hashes_identify_changes_without_claiming_build(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.repository(root)
            dll = root/'app/Madeira/arm64ec-windows/test.dll'
            dll.parent.mkdir(parents=True)
            dll.write_bytes(b'fixture one')
            first = audit.inspect(root)
            dll.write_bytes(b'fixture two')
            second = audit.inspect(root)
            self.assertNotEqual(first['bundled_binary_hashes'][0]['sha256'], second['bundled_binary_hashes'][0]['sha256'])
            self.assertFalse(first['native_build_executed'])
            self.assertTrue(all(not row['present'] for row in first['native_inputs']))


if __name__ == '__main__':
    unittest.main()
