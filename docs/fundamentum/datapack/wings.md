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
| `flight_ticks` | 40 | how long you can rise, in ticks; scaled by the `fundamentum:wing_flight_time` attribute and capped at 75 (a dedicated server kicks "flying" players after 80) |
| `rise_speed` | 0.4 | top rising speed, blocks per tick |
| `rise_acceleration` | 0.1 | how fast you reach it |
| `horizontal_speed` | 1.0 | multiplier on air movement |
| `glide_fall_speed` | 0.15 | fall speed while gliding, at least 0.04 |

A wing item that isn't in any file uses the defaults.

!!! note "Drawing the wings"
    On 26.1.2, a wing item with an `equippable` component naming an equipment asset is drawn on the player from that
    asset's `wings` layer, like an elytra. Otherwise (and always on 1.21.1) the mod that adds the wings draws them.
