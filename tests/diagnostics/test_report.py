# SPDX-License-Identifier: GPL-3.0-or-later
# Madeira Converter Exception: see LICENSE-EXCEPTION.md
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[2] / "tools/diagnostics/report.py"
spec = importlib.util.spec_from_file_location("report", SCRIPT)
report = importlib.util.module_from_spec(spec)
spec.loader.exec_module(report)


class ReportTests(unittest.TestCase):
    def analyze(self, text, **kwargs):
        return report.analyze(io.BytesIO(text.encode()), **kwargs)

    def test_no_false_success_from_empty_or_quiet_log(self):
        for text in ["", "device ready\n", "60 FPS screen; 120 Hz\n"]:
            result = self.analyze(text)
            self.assertEqual(result["application_termination"], "unknown")
            self.assertEqual(result["compatibility_status"], "NOT TESTED")
            self.assertIsNone(result["performance"])

    def test_known_failure_signatures_and_line_numbers(self):
        result = self.analyze('hello\n[dll-missing] wintypes.dll status=c0000135\n[store-undecoded] insn=0xb8e60020\n[mach_exc] UNHANDLED #1\n[redeliv] terminating process\n')
        kinds = {f["kind"]: f for f in result["findings"]}
        self.assertEqual(set(kinds), {"missing_dll", "undecoded_store", "native_exception", "fault_redelivery"})
        self.assertEqual(kinds["missing_dll"]["first_line"], 2)
        self.assertNotIn("excerpt", kinds["missing_dll"]["examples"][0])

    def test_evidence_is_bounded_during_fault_storm(self):
        result = self.analyze('[store-undecoded] x\n' * 10000)
        item = result["findings"][0]
        self.assertEqual(item["count"], 10000)
        self.assertEqual(item["last_line"], 10000)
        self.assertEqual(len(item["examples"]), 3)

    def test_background_gap_not_gameplay_freeze(self):
        result = self.analyze('[freeze] GAP #1 90s BACKGROUNDED(not-a-freeze)\n[freeze] GAP #2 3s unexplained-FREEZE\n')
        self.assertEqual([f["kind"] for f in result["findings"]], ["background_gap", "freeze_gap"])

    def test_guest_exit_not_clean_app_exit(self):
        result = self.analyze('[WineProc] Wine exited with code 0\nMADEIRA-EXIT: child.exe status=0xc0000005\n[WineProc] Wine exited with code -1073741819 (caught by longjmp)\n')
        self.assertEqual(result["guest_exits"]["count"], 3)
        self.assertEqual(result["guest_exits"]["first_events"][1]["status"], 0xc0000005)
        self.assertEqual(result["guest_exits"]["first_events"][2]["status"], -1073741819)
        self.assertEqual(result["application_termination"], "unknown")

    def test_memory_units_not_conflated_or_assumed(self):
        result = self.analyze('phys_footprint=200 MB rss=300MB available=5000MB\nphys_footprint=250MB\nphys_footprint=999 bytes\nphys_footprint=350 MiB\n')
        self.assertEqual(result["memory_observations"]["phys_footprint"]["MB"]["max"], 250)
        self.assertEqual(result["memory_observations"]["rss"]["MB"]["max"], 300)
        self.assertEqual(result["memory_observations"]["phys_footprint"]["MB"]["samples"], 2)
        self.assertEqual(result["memory_observations"]["phys_footprint"]["MiB"]["max"], 350)

    def test_truncation_invalid_utf8_and_hash(self):
        data = b'\xff\n[store-undecoded] final'
        result = report.analyze(io.BytesIO(data))
        self.assertTrue(result["source"]["unterminated_final_line"])
        self.assertEqual(result["source"]["sha256"], hashlib.sha256(data).hexdigest())
        self.assertEqual(result["source"]["bytes"], len(data))

    def test_oversized_line_skipped_and_following_line_kept(self):
        data = b'[store-undecoded]' + b'x' * (report.MAX_LINE * 3) + b'\n[dll-missing] foo\n'
        result = report.analyze(io.BytesIO(data))
        self.assertEqual(result["source"]["lines"], 2)
        self.assertEqual(result["source"]["oversized_lines"], 1)
        self.assertEqual(result["source"]["sha256"], hashlib.sha256(data).hexdigest())
        self.assertEqual([f["kind"] for f in result["findings"]], ["missing_dll"])

    def test_excerpts_opt_in_with_common_credential_redaction(self):
        result = self.analyze('[device] password=secret access_token=token\n', include_excerpts=True)
        text = json.dumps(result)
        self.assertNotIn('secret', text)
        self.assertNotIn('=token', text)

    def test_multiple_sessions_warn_without_guessing_attribution(self):
        result = self.analyze('Running full Wine sequence...\n' * 2)
        self.assertTrue(any('Multiple launch' in s for s in result["limitations"]))

    def test_frame_statistics_and_sample_scope(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'frames.csv'
            path.write_text('frame_time_ms\n10\n20\n30\n40\n', encoding='utf-8')
            result = report.frame_summary(path, 'synthetic unit fixture, no device')
        self.assertEqual(result['average_fps'], 40)
        self.assertEqual(result['p50_ms'], 20)
        self.assertEqual(result['p99_ms'], 40)
        self.assertEqual(result['measured_interval_seconds'], .1)

    def test_invalid_frames_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'frames.csv'
            for text in ['fps\n30\n', 'frame_time_ms\n', 'frame_time_ms\n0\n', 'frame_time_ms\n-1\n', 'frame_time_ms\nnan\n', 'frame_time_ms\ninf\n', 'frame_time_ms\n10,20\n', 'frame_time_ms\n1e308\n1e308\n']:
                path.write_text(text, encoding='utf-8')
                with self.assertRaises(ValueError, msg=text):
                    report.frame_summary(path, 'fixture')

    def test_metadata_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'run.json'
            for value in [[], {'account_token': 'x'}, {'test_duration_seconds': -1}, {'test_duration_seconds': True}, {'test_duration_seconds': 10**400}, {'test_duration_seconds': float('nan')}, {'settings': {'pool': 512}}]:
                path.write_text(json.dumps(value), encoding='utf-8')
                with self.assertRaises(ValueError):
                    report.read_metadata(path)

    def test_cli_exports_and_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            log = Path(tmp) / 'source.txt'
            log.write_text('[store-undecoded] insn=0x123\n', encoding='utf-8')
            output = Path(tmp) / 'report'
            cmd = [sys.executable, str(SCRIPT), str(log), '--output', str(output)]
            first = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(json.loads((output/'report.json').read_text())['findings'][0]['kind'], 'undecoded_store')
            self.assertIn('Interpretation limits', (output/'report.md').read_text())
            self.assertEqual(subprocess.run(cmd, capture_output=True).returncode, 2)
            self.assertEqual(log.read_text(), '[store-undecoded] insn=0x123\n')

    def test_markdown_cannot_escape_json_fence(self):
        result = self.analyze('[device] ```<script>\n', include_excerpts=True)
        result['metadata'] = {'notes': '```'}
        text = report.markdown(result)
        self.assertNotIn('```<script>', text)
        self.assertIn('\\u0060', text)


if __name__ == '__main__':
    unittest.main()
