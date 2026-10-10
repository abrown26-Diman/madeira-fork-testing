# Compatibility matrix

No device/game run was performed for this milestone. Public issue reports are leads, not evidence from this build. Performance belongs in separate run records and never determines launch status by itself.

| Target | Exact edition/build | Status | Evidence/run ID | Performance |
|---|---|---|---|---|
| ULTRAKILL | Awaiting supplied game build | NOT TESTED | None | Not measured |
| TCG Card Shop Simulator | Awaiting supplied game build | NOT TESTED | None | Not measured |
| Kingdom Hearts titles | Record each title/edition separately before testing | NOT TESTED | None | Not measured |
| Disney Dreamlight Valley | Awaiting supplied game build | NOT TESTED | None | Not measured |
| Persona 3 Reload | Awaiting supplied game build | NOT TESTED | None | Not measured |

## Evidence rules

Use exactly: `NOT TESTED`, `FAILS TO LAUNCH`, `STARTS PROCESS`, `REACHES MAIN MENU`, `REACHES GAMEPLAY`, `PLAYABLE`, `STABLE`.

- NOT TESTED: no reviewed run for this game/build/runtime combination.
- FAILS TO LAUNCH: reproducible launch failure before an identifiable guest process starts.
- STARTS PROCESS: guest process evidence, without a confirmed menu.
- REACHES MAIN MENU: reproducible interactive menu with supporting capture/log.
- REACHES GAMEPLAY: player-controlled gameplay, not an intro/video alone.
- PLAYABLE: two repeat runs of a documented representative 15-minute scene, usable controls/audio, no blocking rendering issue; performance is separately reported.
- STABLE: at least three repeat 30-minute representative runs plus save/reload and relaunch checks, without blocking failure. State the tested scope; this is not a whole-game guarantee.

Attach exact game/store/build and executable, device model/RAM, iOS version, standalone/container route and version, JIT method, runtime build commit and dependency manifest, settings, backend, resolution, scene/save identifier, test duration, start/end thermal state, observed result, original log hash and reviewer/date. Do not include account credentials or distribute game files. A regression is a new row/run for the new runtime; retain older evidence instead of overwriting it.

For a failure: repeat with identical settings, preserve the first fault and original log, then reduce to an engine/API test where possible. For status promotion: require reproducible evidence and manually review it. The report tool always emits NOT TESTED as a placeholder and never updates this matrix.

## Baseline preservation checklist

Before runtime changes, establish device evidence for Steam sign-in and a small owned-game download; library persistence; save copy/hash and reload; controller and touch input; audio and a video sample; Wine desktop; JIT attachment/relaunch; one previously functioning x64 game and one WoW64 program. Existing host tests are useful but do not substitute for these checks. All are currently pending device access. Prefer a standalone sideload before repeating with LiveContainer. Never experiment on the only copy of a save.
