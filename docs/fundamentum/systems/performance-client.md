# Client HUD cost

Fundamentum's HUD elements (item HUD, stats, survival meters, boss bar placement) used to rebuild their rows every
frame, and some client code polled on a timer. They now rebuild only when something changes (a synced value, a
declaration, the layout, a block near the ghost preview, a resource reload). A slow safety recheck stays as a net:
`refresh.safetyRecheck` in `config/fundamentum-hud-client.toml`, in seconds, default 5, 0 turns it off. See
[Hud](hud.md).

## Numbers

Time spent inside Fundamentum's HUD layers per frame, in microseconds, timed with `System.nanoTime()` around every
`fundamentum:` layer. Each run is about 440 frames in a flat creative world with the stats test and survival test
meters showing. Each column is median / 99th percentile / worst.

| Version | Before (cd5b812) | After |
|---|---|---|
| 26.1.2 | 172.3 / 503.2 / 966.0 | 50.0 / 434.6 / 621.8 |
| 26.2 | 136.6 / 376.5 / 450.3 | 36.5 / 307.2 / 545.0 |
| 26.3 | 135.1 / 454.6 / 610.2 | 37.8 / 345.3 / 489.7 |
| 1.21.1 | 205.0 / 724.5 / 1555.4 | 117.6 / 715.9 / 936.7 |
| 1.20.1 | 186.0 / 502.6 / 661.5 | 138.0 / 611.8 / 950.6 |

- The median is the number to read. It drops by about 70% on 26.x and by 25-40% on 1.21.1 and 1.20.1.
- The worst frame is noisy. Three 26.1.2 runs after the change gave 622, 1037 and 490 µs, with medians of 50, 51 and 41.
- 1.21.1 and 1.20.1 draw immediately, so their time includes the GPU calls themselves. 26.x only records what to
  draw, so most of what was left to save there was the per-frame rebuilding.

## How to measure

Build with `-Phudshot=perf` and run the client: `gradlew runClient -Phudshot=perf --no-daemon`. It makes a flat world,
times 450 frames, prints a `HUDSHOT PERF` line and closes. `-Phudshot` alone goes on to the full check (HUD editor,
guide, reload, ghost blocks) with screenshots in `run-hudshot/screenshots/`.

The client is hidden, muted and never takes the mouse. It needs `run-hudshot/options.txt` with
`soundCategory_master:0.0` and `pauseOnLostFocus:false`, and `run-hudshot/config/fml.toml` with
`earlyWindowControl = false`. The harness and its mouse mixin load only with `-Phudshot` and never ship.
