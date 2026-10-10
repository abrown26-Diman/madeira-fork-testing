#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# Madeira Converter Exception: see LICENSE-EXCEPTION.md
"""Attempt every existing host check; preserve nonzero results and explicit skips."""
import argparse
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--timeout', type=int, default=180)
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error('--timeout must be positive')
    args.output.mkdir(parents=True, exist_ok=False)
    results = []
    for test in sorted((ROOT/'tests/host').glob('check-*.py')):
        start = time.monotonic()
        with (args.output/(test.stem+'.log')).open('wb') as log:
            process = subprocess.Popen([sys.executable, str(test)], cwd=ROOT,
                                       stdout=log, stderr=subprocess.STDOUT,
                                       env=dict(os.environ, PYTHONUTF8='1'),
                                       start_new_session=os.name == 'posix')
            timed_out = False
            try:
                code = process.wait(timeout=args.timeout)
            except subprocess.TimeoutExpired:
                timed_out = True
                if os.name == 'posix':
                    os.killpg(process.pid, signal.SIGKILL)
                else:
                    process.kill()
                process.wait()
                code = 124
        output = (args.output/(test.stem+'.log')).read_text(encoding='utf-8', errors='replace')
        skips = [line for line in output.splitlines() if line.lstrip().startswith('SKIP')]
        row = dict(test=test.name, exit_code=code, timeout=timed_out,
                   seconds=round(time.monotonic()-start, 2), explicit_skips=skips,
                   result='TIMEOUT' if timed_out else 'NONZERO' if code else 'PARTIAL' if skips else 'PASS')
        results.append(row)
        print(f"{row['result']}: {test.name} ({row['seconds']}s)", flush=True)
        # Update after every check so a job cancellation still leaves evidence.
        (args.output/'results.json').write_text(json.dumps(results, indent=2)+'\n', encoding='utf-8')
    if not results:
        print('ERROR: no host checks discovered', file=sys.stderr)
        return 1
    return int(any(row['exit_code'] for row in results))


if __name__ == '__main__':
    raise SystemExit(main())
