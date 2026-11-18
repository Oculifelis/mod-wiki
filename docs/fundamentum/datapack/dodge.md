# Dodge

The Dodge key (Left Alt by default) sends a player a short way in the direction the movement keys point, with a window
of invulnerability. How far, how fast and how often all come from a dodge style. Gear can swap the style while worn or
held.

Dodge styles live in `data/<ns>/fundamentum/dodge_style/<name>.json`, and the style's id is `<ns>:<name>`. Fundamentum
ships `fundamentum:dash` (the default) and `fundamentum:roll`. Every field is optional. A file with the same id as
another replaces it whole, so a pack that retunes `fundamentum:dash` writes every field it wants to keep.

```json
{
  "distance": 5,
  "ticks": 8,
  "iframe_start": 2,
  "iframe_end": 8,
  "chain_delay": 4,
  "recharge_ticks": 50,
  "lock_ticks": 6,
  "pose": "low",
  "ground": true,
  "air": false,
  "directions": "eight",
  "cost": 0.3,
  "neutral": "back",
  "sound": "minecraft:entity.player.attack.nodamage",
  "volume": 0.6,
  "pitch": 0.9,
  "particle": "minecraft:poof",
  "particle_count": 4,
  "exit_speed": 0.1
}
```

That is the shipped roll.

| Field | Default | Meaning |
|---|---|---|
| `distance` | 4 | blocks covered |
| `ticks` | 4 | how long the move lasts |
| `iframe_start` / `iframe_end` | 0 / `ticks` | the ticks of the move that take no damage |
| `chain_delay` | 6 | ticks before the next dodge can start |
| `recharge_ticks` | 40 | ticks for one spent charge to come back |
| `lock_ticks` | 0 | ticks after the move with no attacking or using items |
| `pose` | `none` | `low` shrinks the player to a crawl while the dodge moves |
| `ground` / `air` | true / true | whether the style works on the ground and in the air |
| `air_dodges` | 1 | dodges allowed before landing again |
| `directions` | `eight` | `eight` goes any way the keys point, `four` snaps to forward, back, left or right |
| `allow_up` | false | a dodge with jump held rises straight up |
| `gravity` | true | false keeps the dodge level in the air |
| `cost` | 0.2 | hunger exhaustion per dodge |
| `neutral` | `back` | where a dodge with no movement key goes: `back`, `forward` or `none` (no dodge) |
| `sound`, `volume`, `pitch` | none, 0.6, 1.4 | the sound on each dodge |
| `particle`, `particle_count`, `particle_spread`, `particle_speed` | none, 6, 0.3, 0.02 | the puff on each dodge |
| `exit_speed` | 0.2 | share of the dodge speed kept when the move ends |
| `impact_reach` | 0.4 | how far past the player's box a dodge finds mobs it passes through |
| `impact_knockback` | 0.5 | scales the knockback attribute against those mobs |

The player's dodge attributes scale these numbers, and the [weight](weight.md) load scales distance, the invulnerable
window and the cost.

## Dodge gear

`data/<ns>/fundamentum/dodge_gear/<name>.json` gives an item its own dodge style. The style applies while the item is
worn or held. When two files name the same item, the higher `priority` wins.

```json
{"item": "minecraft:leather_boots", "style": "fundamentum:roll", "priority": 1}
```

| Field | Default | Meaning |
|---|---|---|
| `item` | needed | the item |
| `style` | needed | a dodge style id |
| `priority` | 0 | which file wins for the same item, and which item wins when a player has several |

## Config

`config/fundamentum/dodge.toml` sets `base_charges` (dodges before a recharge, 0 to 20), `default_style`
(`fundamentum:dash`) and `air_dodges`. Client entries pick the input (the key, a double tap of a movement key, or both),
the double tap window and the charge bar.
