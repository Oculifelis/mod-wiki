# Wings

Wing items go in the Curios `wings` slot (put the item in the item tag `#curios:wings`). Holding jump in the air rises
for the flight time, then glides; landing refills it. No fall damage while flying or gliding.

**File:** `data/<ns>/fundamentum/wings/<name>.json`, keyed by `item`. Every field is optional.

```json
{
  "item": "mymod:angel_wings",
  "flight_ticks": 50,
  "rise_speed": 0.45,
  "rise_acceleration": 0.12,
  "horizontal_speed": 1.25,
  "glide_fall_speed": 0.12
}
```

| Field | Default | Meaning |
|---|---|---|
| `item` | the file id | the wing item |
| `texture` | absent | explicit wing texture, such as `mymod:textures/entity/wings/angel.png`; supported on all five targets from 1.28.0 |
| `flight_ticks` | 40 | how long you can rise, in ticks; scaled by the `fundamentum:wing_flight_time` attribute and capped at 75 (a dedicated server kicks "flying" players after 80) |
| `rise_speed` | 0.4 | top rising speed, blocks per tick |
| `rise_acceleration` | 0.1 | how fast you reach it |
| `horizontal_speed` | 1.0 | multiplier on air movement |
| `glide_fall_speed` | 0.15 | fall speed while gliding, at least 0.04 |

A wing item that isn't in any file uses the defaults.

!!! note "Drawing the wings"
    An explicit `texture` path works on all five targets. On newer versions a wing item can also use an equipment asset's `wings` layer. From 1.28.0, nearby players see the wearer's folded, rising or gliding phase.
