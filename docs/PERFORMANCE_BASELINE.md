# Performance baseline

There is no measured device baseline yet. No FPS, frame-time, CPU, GPU, memory reduction or compatibility improvement is claimed. The approximately 30 FPS target is an objective where hardware and requirements permit it, not a result.

## Controlled run protocol

1. Record the fields in [COMPATIBILITY_MATRIX.md](COMPATIBILITY_MATRIX.md) and `diagnostics/run-template.json`. Use a legally obtained, unchanged game and a fixed scene/save/route. Record power/charging state, brightness, background activity and ambient conditions in notes.
2. Install the unchanged baseline and verify its commit/configuration. Prefer standalone; treat LiveContainer as a separate experiment. Use the same resolution, graphics settings, input route and JIT method.
3. Let the device return to a comparable initial thermal state. Record warm-up duration, then capture at least three identical measured intervals. Separate cold shader/cache runs from warm runs; record cache state. For sustained performance, add a 15–30 minute run with thermal transitions.
4. Change one significant variable. State the mechanism/hypothesis, expected evidence and regression risk before running. Alternate baseline/change order where practical and keep both raw datasets.
5. Report individual runs plus variation, measured interval and instrumentation overhead. Investigate a repeatable difference rather than cherry-picking the best run. Revert a regression or a change that cannot demonstrate its intended benefit.

## Measurements and limits

The existing overlay estimates FPS from present counters. It is not an export of individual frame intervals and it does not measure GPU execution time. Display Hz, log frequency and detector liveness cannot be substituted for game FPS or CPU/GPU utilization.

The offline tool accepts a CSV with exactly `frame_time_ms` and one finite positive interval per row, together with a required capture-method/clock description. It computes total interval duration, average FPS as `1000*N/sum(intervals)`, mean, nearest-rank p50/p95/p99 and maximum interval. These statistics describe only the supplied intervals. Include whether capture counts submitted presents, displayed frames or another event; those are different observations. Use a stopped, immutable capture file. No "1% low" or GPU time is inferred.

Memory reports separate footprint, RSS, available and limit-remaining values, retaining MB and MiB labels separately. Peaks in sampled logs are observed sample maxima, not guaranteed process peaks or a device jetsam threshold. An iOS JetsamEvent may be required to explain an OS kill. Thermal state is a coarse OS indicator; no device frequency or throttling percentage is invented.

## Planned experiments, not optimization claims

| Hypothesis | Required evidence | Acceptance gate |
|---|---|---|
| Shader compilation causes early stutter | Correlated compile events and valid per-frame intervals, cold/warm cache comparison | Reduced repeatable compile stalls without rendering/cache invalidation regression |
| JIT code-cache work causes CPU stalls | Safe FEX counters/profiling plus frame intervals, bounded overhead measurement | Reduced measured work and frame tails with same correctness suite |
| Wine synchronization stalls GC/engine workers | Thread ownership/wait evidence and minimal concurrency reproducer | Correct forward progress before performance tuning; no global unsafe suspend toggle |
| Resource uploads or peak footprint cause stalls/termination | Allocation/upload evidence, observed footprint and pressure/OS report | Reduced sampled peaks with correct rendering and no increased transfer stalls |

These tests require a native/device baseline. Synthetic unit-test intervals validate arithmetic only and must never be entered as game results.
