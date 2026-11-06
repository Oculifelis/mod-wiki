# Elements

*NeoForge 26.1.2 and 1.21.1.*

An element **is a damage type or a damage type tag**. Wherever a field takes elements, it takes one string or a list:

| Written | Means |
|---|---|
| `"minecraft:magic"` | hits of that one damage type |
| `"#minecraft:is_fire"` | hits of any damage type in that tag |
| `"#fundamentum:element/fire"` | the same, and also hits that are fire through their weapon (a weapon in the item tag `#fundamentum:element/fire`) |

Fundamentum's ten elements are fire, ice, water, electric, earth, air, poison, holy, shadow and arcane. Each is a damage
type tag `#fundamentum:element/<e>` and a shared damage type `fundamentum:<e>` that any mod can deal. Names shown in
game come from lang keys `element.<ns>.<path>` with `/` as `.` (`element.fundamentum.element.fire`).

## Auras

A hit leaves an aura of its element on the creature it hits. Data map on damage types:
`data/<ns>/data_maps/damage_type/element_aura.json`. Keys are damage types or `#tags`.

```json
{
  "values": {
    "#fundamentum:element/fire": {"aura": "#fundamentum:element/fire", "strength": 1, "duration": 120, "decay": 0, "max_stacks": 3, "min_damage": 0},
    "minecraft:drown": {"aura": "#fundamentum:element/water", "duration": 200}
  }
}
```

| Field | Default | Meaning |
|---|---|---|
| `aura` | the damage type itself | which aura the hit leaves; point many damage types at one shared aura |
| `strength` | 1 | strength added per hit (capped at `strength * max_stacks`) |
| `duration` | 100 | ticks the aura lasts; every hit refreshes it |
| `decay` | 0 | strength lost per second; the aura ends at 0 |
| `max_stacks` | 1 | stacks it can build up to (one per hit) |
| `min_damage` | 0 | hits below this leave no aura |

## Reactions

What happens when a hit of one element lands on a creature carrying an aura of another.
**File:** `data/<ns>/fundamentum/element_reaction/<name>.json`. `trigger` and `aura` are required.

```json
{
  "trigger": "#fundamentum:element/fire",
  "aura": "#fundamentum:element/ice",
  "priority": 10,
  "exclusive": false,
  "min_stacks": 1,
  "consume": "all",
  "apply_trigger_aura": false,
  "damage": {"multiplier": 2, "bonus": 0, "per_stack": 0},
  "convert_to": "minecraft:magic",
  "effects": [{"id": "minecraft:slowness", "duration": 60, "amplifier": 1, "on": "target"}],
  "knockback": {"strength": 0.6, "up": 0.2},
  "ignite": 0,
  "extinguish": false,
  "burst": {"radius": 3, "damage": 2, "scale": 0.5, "damage_type": "fundamentum:electric", "include_target": false},
  "fx": {"particle": {"type": "minecraft:cloud"}, "count": 12, "spread": 0.4, "speed": 0.02,
         "sound": "minecraft:block.fire.extinguish", "volume": 1, "pitch": 1},
  "function": "mypack:on_melt"
}
```

| Field | Default | Meaning |
|---|---|---|
| `trigger` | | the element of the incoming hit |
| `aura` | | the aura it must find on the target |
| `priority` | 0 | several reactions can match one hit; they run from the highest down |
| `exclusive` | false | true stops the reactions after it |
| `min_stacks` | 1 | aura stacks needed |
| `consume` | `all` | what it takes from the aura: `all`, `one` or `none` |
| `apply_trigger_aura` | false | whether the hit still leaves its own aura |
| `damage` | x1 | `multiplier`, then `bonus`, plus `per_stack` for each aura stack |
| `convert_to` | none | the hit becomes this damage type (and reacts and resists as that type) |
| `effects` | none | `id`, `duration` (100), `amplifier` (0), `on`: `target` or `attacker` |
| `knockback` | none | `strength` (0.5), `up` (0) |
| `ignite` / `extinguish` | 0 / false | seconds of fire / put the fire out |
| `burst` | none | damage around the target: `radius` (3), `damage` (0) plus `scale` x the hit, `damage_type` (`minecraft:magic`), `include_target` (false) |
| `fx` | none | particles (any particle JSON) and a sound |
| `function` | none | a datapack function to run |

Chains can't loop: a reaction never fires while it is already running, never twice on one creature in one tick, and
chains stop 8 deep.

## Affinities

Resistances, weaknesses and immunities. The same shape is a data map on entity types
(`data/<ns>/data_maps/entity_type/element_affinity.json`) and an item component, counted while the item is worn or
held:

```json
{"values": {"minecraft:blaze": {"resist": {"#fundamentum:element/water": -1.0}, "immune": ["minecraft:drown"]}}}
```

```
/give @s diamond_chestplate[fundamentum:element_affinity={resist:{"#fundamentum:element/fire":0.5}}]
```

`resist` values add up over every matching entry: 0.5 takes half, -1 takes double, 1 or more is immune. `immune`
cancels matching hits outright. Items with the component show it in their tooltip.

## The vanilla set

A built-in datapack, **Fundamentum: vanilla elements**, is on by default. Turn it off with
`/datapack disable "mod/fundamentum:packs/elements_default"`.

| Reaction | Hit on aura | Result |
|---|---|---|
| melt | fire on ice | x2 |
| quench | ice on fire | x1.5, puts the fire out |
| vaporize | fire on water | x1.5 |
| freeze | ice on water | +2, Slowness IV 3 s |
| electrocute | electric on water | 3-block burst of electric damage, the water stays |
| overload | electric on fire | 2.5-block explosion burst, knockback |
| detonate | explosion on fire | x1.5, takes one fire stack |
| shatter | explosion on ice | x1.5, turned into magic damage |
| blight | shadow on arcane | x1.25, Weakness 5 s |
| smother | water or drowning on fire | puts the fire out |

Its affinities: undead resist shadow and are weak to holy; blazes take double water; endermen take more water;
guardians take more electric; polar bears resist ice; snow golems are immune to ice and weak to fire.

Test with `/fundamentum element` (see [Commands](../commands.md)).
