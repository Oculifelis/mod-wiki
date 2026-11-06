# Moons

Special moons, like Terraria's Blood Moon: a night that tints the fog and sky and can bring its own spawns, effects
and loot. Tonight's moon is rolled at dusk and kept with the world.

**File:** `data/<ns>/fundamentum/moons/<name>.json`. The moon's id is `<ns>:<name>`. Every field is optional.

```json
{
  "chance": 0.05,
  "priority": 0,
  "dimension": "minecraft:overworld",
  "requires": ["mymod:dragon_slain"],
  "full_moon": "any",
  "fog": {"color": "#2E5BCC", "strength": 0.45, "fade": {"in": 2.25, "out": 2.25, "curve": "linear"}},
  "sky": {"color": "#2E5BCC", "strength": 0.2, "shift": {"color": "#CC2E9B", "seconds": 8}},
  "effects": [{"effect": "minecraft:luck", "amplifier": 0}],
  "spawns": [{"entity": "mymod:moth", "chance": 0.45, "cap": 4, "interval": 160}],
  "bonus_loot": "mymod:moons/harvest",
  "summon": {
    "item": "mymod:harvest_lantern",
    "consume": 1,
    "cooldown": 40,
    "sound": {"id": "minecraft:block.beacon.activate", "volume": 1.2, "pitch": 1.4},
    "refusals": {"elsewhere": "message.mymod.lantern.elsewhere", "daylight": "message.mymod.lantern.daylight",
                 "already": "message.mymod.lantern.already"}
  },
  "rise_message": {"key": "message.mymod.harvest_moon", "color": "fog", "bold": true},
  "rise_sound": "mymod:moonrise",
  "set_message": "message.mymod.harvest_set"
}
```

| Field | Default | Meaning |
|---|---|---|
| `chance` | 0 | chance per eligible night; 0 means it only comes when called by an item, command or code |
| `priority` | 0 | moons roll from the highest priority down; the first that rises wins |
| `dimension` | `minecraft:overworld` | |
| `requires` | none | world flags that must all be set before it rises by chance (mods set flags in code) |
| `full_moon` | `any` | `any`, `never` or `only` |
| `moon_phases` | any | only on these phases (0 full, 1-3 waning, 4 new, 5-7 waxing) |
| `fog` | none | a [tint](#tints) on the night air of its dimension |
| `sky` | none | a [tint](#tints) on its sky and the sunset glow (the colour defaults to the fog's) |
| `effects` | none | mob effects kept on players in its dimension while it's up |
| `spawns` | none | extra creatures: `chance` per try, `cap` alive at once, a try every `interval` ticks |
| `bonus_loot` | none | a loot table rolled when a player kills a hostile creature under it |
| `summon` | none | an item that calls the moon at night: how many it uses up, a cooldown in ticks, a sound (`""` for silent) and lang keys for when it refuses |
| `rise_message` / `set_message` | none | a lang key, or `{"key", "color": "#hex" or "fog", "bold", "italic", "overlay"}` |
| `rise_sound` | none | a sound id, or `{"id", "volume", "pitch"}`; played to everyone it rises over |

Any other field belongs to the mod that owns the moon, which reads it in code.

## Tints

Fog and sky tints share one shape, also used by [night events](night-events.md):

```json
{"color": "#hex", "strength": 0.3, "fade": {"in": 5, "out": 5, "curve": "linear"}, "shift": {"color": "#hex", "seconds": 8}}
```

| Field | Meaning |
|---|---|
| `color` | the tint colour |
| `strength` | 0 to 1 |
| `fade.in` / `fade.out` | seconds to fade in and out |
| `fade.curve` | `linear` is steady; `ease_out` is fast at first and slows |
| `shift` | the colour drifts to `shift.color` and back over `shift.seconds` |

## Testing

`/fundamentum moon start <id>` starts any moon (making it night first), `stop` ends it, `list` shows them all, and
`query` names tonight's moon. See [Commands](../commands.md).
