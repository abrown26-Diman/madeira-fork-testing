#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# Madeira Converter Exception: see LICENSE-EXCEPTION.md
"""Offline, bounded evidence extraction from Madeira logs. Python 3.10+; no deps.

Findings are observations, never proof of a root cause or gameplay compatibility.
Default output contains no raw log text. --include-excerpts is for local triage.
"""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import re
import sys

MAX_LINE = 64 * 1024
MAX_FRAMES = 2_000_000
RULES = [
    ("missing_dll", r"\[dll-missing\]|import_dll Library .+ not found", "Check the named module and its transitive imports in the correct architecture farm."),
    ("undecoded_store", r"\[store-undecoded\]", "Correlate the instruction, alias and Mach exception; do not disable the redelivery guard."),
    ("fault_redelivery", r"\[redeliv\].*(?:terminating|storm|redeliveries)", "Retest the first fault on the pinned source; later repetitions are not independent failures."),
    ("native_exception", r"\[mach_exc\].*UNHANDLED|\*\*\* Terminating app due to uncaught exception|SWIFT TASK CONTINUATION MISUSE", "Pair with the matching iOS .ips report and symbols from this build."),
    ("guest_exception", r"\[exc\].*code=|err:seh:|Unhandled exception", "Guest exceptions can be handled or expected; inspect surrounding lines and the guest exit."),
    ("jit_protection", r"Failed to mprotect|(?:mprotect|mach_vm_protect).*(?:failed|failure)|JIT not enabled", "Check JIT attachment, signing and the first protection failure; a warning alone does not prove a crash."),
    ("allocation_failure", r"(?:mmap|malloc|allocation|jit.pool).*(?:failed|failure|EXHAUST)|out of memory", "Correlate allocation size, address-map/pool limits and memory samples; do not assume jetsam."),
    ("graphics_failure", r"Failed to create (?:internal command library|.*pipeline|.*device)|MTLLibraryErrorDomain|(?:shader|pipeline).*(?:compilation failed|compile failed)|\[d3d12[^\]]*\].*E_NOTIMPL", "Identify the graphics backend and first failing shader, pipeline or capability."),
    ("freeze_gap", r"\[freeze\] GAP.*unexplained-FREEZE", "A detector scheduling gap is an observation, not a CPU/GPU attribution."),
    ("background_gap", r"\[freeze\] GAP.*BACKGROUNDED", "Background suspension is not classified as a gameplay freeze."),
    ("detector_failure", r"\[freeze\].*(?:DETECTOR DEAD|FAILED to start|respawn FAILED)", "Missing GAP events cannot establish a freeze-free run when the detector failed."),
]
RULES = [(name, re.compile(pattern, re.I), advice) for name, pattern, advice in RULES]
CONTEXT = re.compile(r"\[(?:build|device|launch-route|steam-start|fex-config)\]|madeira\.cfg|Target exe:|DXMT_CONFIG|WINEDEBUG")
EXIT = re.compile(r"(?:MADEIRA-EXIT:.*?status=|Wine exited with code\s+)(0x[0-9a-fA-F]+|-?[0-9]+)")
MEMORY = re.compile(r"\b(phys_footprint|resident_size|rss|available|limit_remaining)\s*=\s*([0-9]+)\s*(MB|MiB)\b", re.I)
METADATA_KEYS = {
    "game", "executable", "launch_route", "device_model", "ios_version", "runtime_version",
    "build_commit", "settings", "resolution", "test_scene", "test_duration_seconds",
    "thermal_start", "thermal_end", "jit_method", "container", "notes",
}


def read_metadata(path):
    if path is None:
        return {}
    if path.stat().st_size > 64 * 1024:
        raise ValueError("metadata exceeds 64 KiB")
    value = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(value, dict) or value.keys() - METADATA_KEYS:
        raise ValueError("metadata must be an object with only the documented keys")
    for key, item in value.items():
        if item is None:
            continue
        if key == "settings":
            if not isinstance(item, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in item.items()):
                raise ValueError("settings must map strings to strings")
        elif key == "test_duration_seconds":
            if isinstance(item, bool) or not isinstance(item, (int, float)) or not (0 < item <= sys.float_info.max):
                raise ValueError("test_duration_seconds must be finite and positive")
        elif not isinstance(item, str):
            raise ValueError(f"{key} must be a string or null")
    return value


def bounded_lines(stream, stats):
    """Hash every byte, but discard oversized line tails without allocating them."""
    digest = hashlib.sha256()
    while True:
        part = stream.readline(MAX_LINE + 1)
        if not part:
            break
        digest.update(part)
        stats["bytes"] += len(part)
        oversized = len(part) > MAX_LINE
        head = part[:MAX_LINE]
        while not part.endswith(b"\n") and len(part) == MAX_LINE + 1:
            part = stream.readline(MAX_LINE + 1)
            digest.update(part)
            stats["bytes"] += len(part)
        stats["lines"] += 1
        if oversized:
            stats["oversized_lines"] += 1
        if not part.endswith(b"\n"):
            stats["unterminated_final_line"] = True
        # Never classify truncated text: it may hide a negation or a suffix.
        yield stats["lines"], None if oversized else head.decode("utf-8", errors="replace").rstrip("\r\n")
    stats["sha256"] = digest.hexdigest()


def excerpt(text):
    # Best effort only. Raw logs may contain personal data in arbitrary formats.
    text = re.sub(r"(?i)\b(?:access_token|refresh_token|password|authorization|cookie)\b\s*[:=]\s*\S+", "[credential redacted]", text)
    text = re.sub(r"[\x00-\x08\x0b-\x1f\x7f]", "?", text)
    return text[:600]


def analyze(stream, include_excerpts=False):
    stats = dict(bytes=0, lines=0, oversized_lines=0, unterminated_final_line=False)
    findings = {}
    context = []
    context_count = 0
    exit_count = 0
    exits = []
    memory = {}
    launches = 0
    for number, line in bounded_lines(stream, stats):
        if line is None:
            continue
        if "Running full Wine sequence..." in line:
            launches += 1
        if CONTEXT.search(line):
            context_count += 1
            if len(context) < 40:
                item = {"line": number}
                if include_excerpts:
                    item["excerpt"] = excerpt(line)
                context.append(item)
        for name, pattern, advice in RULES:
            if not pattern.search(line):
                continue
            item = findings.setdefault(name, {"kind": name, "count": 0, "first_line": number, "last_line": number, "next_step": advice, "examples": []})
            item["count"] += 1
            item["last_line"] = number
            if len(item["examples"]) < 3:
                example = {"line": number}
                if include_excerpts:
                    example["excerpt"] = excerpt(line)
                item["examples"].append(example)
        match = EXIT.search(line)
        if match:
            exit_count += 1
            if len(exits) < 20:
                value = match[1]
                exits.append({"line": number, "status": int(value, 16 if value.lower().startswith("0x") else 10), "scope": "guest; may be a helper process"})
        for match in MEMORY.finditer(line):
            key = match[1].lower()
            unit = "MiB" if match[3].lower() == "mib" else "MB"
            item = memory.setdefault(key, {}).setdefault(unit, {"samples": 0, "min": int(match[2]), "max": 0})
            item["samples"] += 1
            item["min"] = min(item["min"], int(match[2]))
            item["max"] = max(item["max"], int(match[2]))
    return {
        "schema_version": 1,
        "source": stats,
        "findings": list(findings.values()),
        "context": {"matched_lines": context_count, "first_lines": context},
        "guest_exits": {"count": exit_count, "first_events": exits},
        "launch_markers": launches,
        "application_termination": "unknown",
        "compatibility_status": "NOT TESTED",
        "memory_observations": memory,
        "performance": None,
        "limitations": [
            "Pattern matches are evidence to inspect, not root-cause diagnoses. Counts are matching log lines, not unique faults.",
            "No clean application-exit marker exists in this format. A missing final line cannot distinguish crash, jetsam, suspension, force-quit, or an incomplete export.",
            "A guest/helper exit does not establish application exit or gameplay status. Compatibility requires a separate reviewed test record.",
            "Memory figures retain their logged MB or MiB labels in separate groups; footprint, RSS and available memory are different metrics. No device-wide jetsam threshold is assumed.",
            "No CPU utilization, GPU timing, FPS or frame-time values are inferred from text chatter or the display refresh rate.",
            "Export a stopped log. For abrupt termination, retain the original log, matching iOS Analytics .ips/JetsamEvent and, for hangs, a time-correlated sysdiagnose.",
        ] + (["Multiple launch markers: observations span sessions; split the log before attributing a failure to one game."] if launches > 1 else [])
          + (["Oversized lines were hashed but not classified."] if stats["oversized_lines"] else []),
    }


def frame_summary(path, source):
    """Explicitly supplied frame intervals only; never sample the UI FPS counter."""
    if not source or not source.strip():
        raise ValueError("--frames-source must describe the capture method and clock")
    values = []
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        # csv uses text mode below; compute identity in bounded chunks first.
        for block in iter(lambda: handle.read(64 * 1024), b""):
            digest.update(block)
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != ["frame_time_ms"]:
            raise ValueError("frames CSV must have exactly one column: frame_time_ms")
        for row in reader:
            if len(values) >= MAX_FRAMES:
                raise ValueError("frame sample limit exceeded")
            if None in row:
                raise ValueError(f"extra CSV field at row {reader.line_num}")
            value = float(row["frame_time_ms"])
            if not math.isfinite(value) or value <= 0:
                raise ValueError(f"invalid frame interval at row {reader.line_num}")
            values.append(value)
    if not values:
        raise ValueError("no frame intervals supplied")
    values.sort()
    try:
        total = math.fsum(values)
    except OverflowError as error:
        raise ValueError("frame interval sum overflowed") from error
    if not math.isfinite(total):
        raise ValueError("frame interval sum overflowed")
    average_fps = 1000 * len(values) / total
    if not math.isfinite(average_fps):
        raise ValueError("frame intervals are too small to summarize")
    percentile = lambda p: values[math.ceil(p * len(values)) - 1]
    return dict(source=source, sha256=digest.hexdigest(), samples=len(values),
                measured_interval_seconds=total / 1000,
                average_fps=average_fps,
                mean_frame_time_ms=total / len(values), p50_ms=percentile(.50),
                p95_ms=percentile(.95), p99_ms=percentile(.99),
                max_frame_time_ms=values[-1], percentile_method="nearest rank",
                scope="supplied intervals only; capture correctness is not independently verified")


def markdown(report):
    lines = ["# Madeira diagnostic evidence", "", "Application termination: **unknown**. Compatibility: **NOT TESTED**.", "",
             f"Log SHA-256: `{report['source']['sha256']}`", "",
             "## Observed patterns", "", "| Pattern | Lines matched | First line | Last line |", "|---|---:|---:|---:|"]
    for item in report["findings"]:
        lines.append(f"| {item['kind']} | {item['count']} | {item['first_line']} | {item['last_line']} |")
    if not report["findings"]:
        lines += ["", "No recognized patterns. This is not evidence of a successful run."]
    for item in report["findings"]:
        lines += ["", f"**{item['kind']}**: {item['next_step']}"]
    # JSON indentation inside a fence is unambiguous for arbitrary caller metadata.
    # Escape backticks to keep log contents from ending the fence.
    for title, key in [("Supplied test metadata (not independently verified)", "metadata"),
                       ("Memory observations", "memory_observations"), ("Performance", "performance"),
                       ("Guest exits", "guest_exits"), ("Context and excerpts", "context")]:
        content = json.dumps(report.get(key), indent=2, ensure_ascii=True).replace("`", "\\u0060")
        lines += ["", f"## {title}", "", "```json", content, "```"]
    if any("excerpt" in example for item in report["findings"] for example in item["examples"]):
        content = json.dumps(report["findings"], indent=2, ensure_ascii=True).replace("`", "\\u0060")
        lines += ["", "## Pattern excerpts", "", "```json", content, "```"]
    lines += ["", "## Interpretation limits", ""] + [f"- {value}" for value in report["limitations"]]
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("log", type=Path)
    parser.add_argument("--output", type=Path, required=True, help="new report directory; must not already exist")
    parser.add_argument("--metadata", type=Path)
    parser.add_argument("--include-excerpts", action="store_true", help="include bounded raw text; review for personal data before sharing")
    parser.add_argument("--frames", type=Path)
    parser.add_argument("--frames-source")
    args = parser.parse_args(argv)
    try:
        metadata = read_metadata(args.metadata)
        if bool(args.frames) != bool(args.frames_source):
            raise ValueError("--frames and --frames-source must be supplied together")
        perf = frame_summary(args.frames, args.frames_source) if args.frames else None
        with args.log.open("rb") as handle:
            report = analyze(handle, args.include_excerpts)
        report["metadata"] = metadata
        report["performance"] = perf
        args.output.mkdir(parents=True, exist_ok=False)
        (args.output / "report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
        (args.output / "report.md").write_text(markdown(report), encoding="utf-8")
    except (OSError, ValueError, csv.Error) as error:
        parser.exit(2, f"report: {error}\n")
    print(f"Wrote {args.output / 'report.json'} and report.md; no compatibility verdict inferred.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
