# Fractal skies

*NeoForge 26.1.2 and 1.21.1.*

A sky drawn per pixel by Fundamentum's fractal shader in place of the vanilla one, while a moon, a night event or a
dimension calls for it. Players can turn fractal skies and the melt effect off in `config/fundamentum-sky-client.toml`.

**File:** `data/<ns>/fundamentum/fractal_skies/<name>.json`. At least one of `moon`, `event` and `dimension` must be
given, and all that are given must match. Everything else is optional.

```json
{
  "moon": "fundamentum:psychedelic",
  "priority": 0,
  "fractal": "mandelbrot",
  "iterations": 160,
  "palette": "rainbow",
  "tint": "#FFFFFF",
  "mapping": "zenith",
  "center": [-0.7436, 0.1318],
  "scale": 2.5,
  "zoom": {"speed": 0.01, "depth": 4},
  "tour": false,
  "palette_speed": 0.02,
  "morph_speed": 0.005,
  "rotation_speed": 0.002,
  "brightness": 0.8,
  "horizon": 0.25,
  "fade_seconds": 4,
  "melt": 0
}
```

| Field | Default | Meaning |
|---|---|---|
| `moon` | | while this moon is up |
| `event` | | while this night event runs |
| `dimension` | | in this dimension (alone: always there) |
| `priority` | 0 | the highest of the skies that match is drawn |
| `fractal` | `mandelbrot` | `mandelbrot`, `julia` or `burning_ship` |
| `iterations` | 160 | 16 to 500 |
| `palette` | `rainbow` | `rainbow`, `fire`, `ice`, `acid`, `neon` or `void` |
| `tint` | `#FFFFFF` | multiplies the colours |
| `mapping` | `zenith` | `zenith` (centred overhead) or `axes` (seen along each axis and blended, with no seams) |
| `center` | `[-0.7436, 0.1318]` | where the zoom heads |
| `scale` | 2.5 | how much of the plane the sky spans at its widest |
| `zoom.speed` / `zoom.depth` | 0.01 / 4 | zoom cycles per second, and how deep |
| `tour` | false | Mandelbrot only: the whole set spans the sky and each zoom dives into a different spot, then back out |
| `palette_speed` / `morph_speed` / `rotation_speed` | 0.02 / 0.005 / 0.002 | cycles per second |
| `brightness` | 0.8 | |
| `horizon` | 0.25 | elevation where the sky is fully shown; it fades out below |
| `fade_seconds` | 4 | in and out |
| `melt` | 0 | 0 to 1: the melting-vision effect over the world while it shows (the client config scales it) |

To preview a sky without waiting for its moon, use the client command `/fundamentum_sky preview <id>`, and
`/fundamentum_sky off` to stop.
