# Whips

*NeoForge 26.1.2 and 1.21.1.*

Fundamentum's whips have a simulated cord: hits are tested along its whole moving length, the tip hits hardest, and a
tip hit at crack speed is a crit. Left click swings. A mod registers its whips in code (see [API](../api.md)); a data
file can retune any registered whip, or turn any item into a plain whip.

**File:** `data/<ns>/fundamentum/whips/<name>.json`, keyed by `item`. Every field is optional; a field left out keeps
the whip's registered value (or the default for a plain whip).

```json
{
  "item": "mymod:thorn_whip",
  "length": 5.5,
  "damage": 8,
  "strands": 3,
  "strand_spread": 14,
  "crack_speed": 25,
  "tip_crit_multiplier": 1.75,
  "cooldown_ticks": 13,
  "texture": "mymod:textures/entity/whip/thorn.png",
  "color": "#FF5A8F3C",
  "tip_color": "#FFB8E07A",
  "width": 0.1,
  "tip_width": 0.03,
  "homing_degrees": 0,
  "strand_targets": false
}
```

## Tuning

Any of these, in snake case. Defaults are a plain 4.5-block leather whip.

| Field | Default | Meaning |
|---|---|---|
| `length` | 4.5 | cord length, blocks |
| `segments` | 20 | links in the simulated cord |
| `stiffness` | 0.3 | how stiff the cord is |
| `guide` | 0.85 | how tightly the cord follows the swing (lower is wilder) |
| `lag` | 0.14 | how far the cord trails the hand |
| `retention` | 0.98 | speed kept per physics step |
| `gravity` | 20 | |
| `arc` | 150 | swing arc, degrees |
| `tilt` | 30 | swing tilt, degrees |
| `windup_ticks` / `stroke_ticks` / `recover_ticks` | 4 / 5 / 8 | the swing's phases |
| `hit_ticks_after_stroke` | 3 | how long after the stroke the cord still hits |
| `cooldown_ticks` | 13 | between swings |
| `damage` | 6 | damage at the tip |
| `root_damage` | 0.4 | share of it at the handle |
| `falloff_power` | 1.5 | how damage rises from handle to tip |
| `tip_fraction` | 0.2 | share of the cord that counts as the tip |
| `crack_speed` | 25 | tip speed (blocks/s) for a crack |
| `tip_crit_multiplier` | 1.75 | damage multiplier for a cracking tip hit |
| `hit_radius` | 0.15 | blocks |
| `strands` / `strand_spread` | 1 / 12 | several cords from one handle, spread in degrees |
| `sweep` | true | hit several targets per swing |
| `max_targets` | 8 | |
| `multi_hit_falloff` / `multi_hit_floor` | 0.85 / 0.5 | damage kept per extra target, and the least it falls to |
| `knockback` | 0.4 | |
| `substeps` | 8 | physics steps per tick |

Damage is the tuning's plus the player's attack damage above 1 (Strength, the item's own attack modifiers). It counts
as a player melee attack, so damage classes, elements and enchantments apply.

## Look and aim

| Field | Meaning |
|---|---|
| `texture` | cord texture |
| `color` / `tip_color` | tint from handle to tip, `"#AARRGGBB"` or a number |
| `width` / `tip_width` | cord width at handle and tip |
| `idle_length` | share of the cord that hangs from the hand between swings (default 0.35; 0 for none) |
| `idle_coil` | draw the cord coiled under the handle between swings |
| `hip_coil` | hang the whip coiled at the hip while another item is held (default true) |
| `shockwave` | a ring colour where the tip cracks |
| `cord_fx` | cord shader: `glow`, `energy`, `water`, `wind`, `lightning` or `fire` |
| `glow` | halo colour, or true/false |
| `handle_end` | `[u, v]`: where the cord leaves a 3D handle, in 16x16 handheld pixels (default `[11.5, 4.5]`) |
| `homing_degrees` | turn each swing toward the hostile nearest the crosshair inside this cone |
| `strand_targets` | each strand of a multi-strand whip picks its own target |

## Tags

Put whips in `#fundamentum:whips` (`data/fundamentum/tags/item/whips.json`, `"replace": false`). Fundamentum adds
that tag to `#c:tools/whip`, `#c:tools/melee_weapon` and `#c:tools`, and to vanilla's enchantable tags, so whips take
Sharpness, Smite, Bane of Arthropods, Fire Aspect and Curse of Vanishing on an anvil.

## Flat or 3D handles in hand

The item model condition `fundamentum:whip_flat_handles` is true when the player turns on `whips.flatHandles` in
`config/fundamentum-client.toml`, and `fundamentum:whip_swinging` is true while the cord is out. Use them in
`assets/<ns>/items/<whip>.json` (26.1.2) to pick models, for example:

```json
{"model": {"type": "minecraft:condition", "property": "fundamentum:whip_swinging",
           "on_true": {"type": "minecraft:model", "model": "mymod:item/thorn_whip_handle"},
           "on_false": {"type": "minecraft:model", "model": "mymod:item/thorn_whip"}}}
```

On 1.21.1 the same switches are `ItemProperties` overrides in the item model.
