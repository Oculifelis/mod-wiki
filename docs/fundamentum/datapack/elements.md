# Elements

*NeoForge 26.1.2, 26.2, 26.3 and 1.21.1.*

An element **is a damage type or a damage type tag**. Wherever a field takes elements, it takes one string or a list:

| Written | Means |
|---|---|
| `"minecraft:magic"` | hits of that one damage type |
| `"#minecraft:is_fire"` | hits of any damage type in that tag |
| `"#fundamentum:element/fire"` | the same, and also hits that are fire through their weapon (a weapon in the item tag `#fundamentum:element/fire`) |

Fundamentum's elements are fire, soul fire, ice, water, electric, earth, air, poison, holy, shadow and arcane. Each is a
damage type tag `#fundamentum:element/<e>` and a shared damage type `fundamentum:<e>` that any mod can deal.

| Element | Tags | Shared damage type | Variant of |
|---|---|---|---|
| fire | `#fundamentum:element/fire` | `fundamentum:fire` | |
| soul fire | `#fundamentum:element/soul_fire` | `fundamentum:soul_fire` (burn ticks: `fundamentum:on_soul_fire`) | fire |
| ice, water, electric, earth, air, poison, holy, shadow, arcane | `#fundamentum:element/<e>` | `fundamentum:<e>` | |

Names shown in game come from lang keys `element.<ns>.<path>` with `/` as `.` (`element.fundamentum.element.fire`).

## Variants: soul fire is fire

An element can be a **variant** of another (its *parent*). Every hit of the variant also counts as the parent, so
anything that checks the parent covers it; the variant only adds to it. Soul fire is a variant of fire: fire
resistance, fire-immune mobs, water and frost putting it out, fire auras and every fire reaction apply to soul fire
unchanged. On top of that, soul fire sets what it hits burning with blue soul flames (2 HP a second instead of 1),
and has its own reaction and affinities below.

For damage types the variant's tag sits inside its parent's: the damage type tag `#fundamentum:element/fire` lists
`#fundamentum:element/soul_fire`, and `fundamentum:soul_fire` and `fundamentum:on_soul_fire` are in `#minecraft:is_fire`,
so anything that checks those tags counts soul fire hits too. The item tags are separate: the item tag
`#fundamentum:element/fire` does not list the soul fire one. A weapon in the item tag `#fundamentum:element/soul_fire`
still counts as fire, because Fundamentum's element check (`Element.matches`) covers a parent's variants in code. Code
adds a variant with `Elements.variant(id, parent, damage, resistance)` (see the [API](../api.md)).

### Soul fire

**Burning blue.** An entity set on fire by a soul source burns with vanilla's soul fire sprites (third person and the
first-person screen fire, the same render path as vanilla fire, so shaders treat it the same). It goes back to orange or
out when the fire ends, when it touches ordinary fire or lava, or when something non-soul sets it alight.

**Sources:**

| Source | Tag | What it does |
|---|---|---|
| Blocks | `#fundamentum:soul_fire_sources` | Soul fire and soul campfires. |
| Projectiles | `#fundamentum:soul_fire_projectiles` | Projectiles that set targets on fire (flaming arrows) set them soul-burning. |
| Melee weapons | `#fundamentum:soul_fire_weapons` | Weapons that set targets on fire (Fire Aspect) set them soul-burning; their hits stay as they are. |
| The soul fire element | `#fundamentum:element/soul_fire` | Every hit sets the target soul-burning for 4 s. |

**Damage:** 2 HP a second while soul-burning, the vanilla soul fire block's contact damage. Config
`config/fundamentum-soulfire.toml`:

| Key | Default | What it does |
|---|---|---|
| `soulFireBurnDamage` | 2.0 | Damage a second while soul-burning. |
| `soulFireHitIgniteTicks` | 80 | How long a soul fire hit sets the target soul-burning. |

**A soul weapon, data only:** put the item in `#fundamentum:element/soul_fire` and its hits are soul fire (and so
fire). To keep a weapon's hits as they are and only turn the fire it sets blue, use `#fundamentum:soul_fire_weapons`
instead. For example `data/fundamentum/tags/item/element/soul_fire.json`:

```json
{"values": ["mymod:soul_blade"]}
```

## New elements

*From Fundamentum 1.26.0.*

A datapack can add a whole new element, with no code. Each file `data/<ns>/fundamentum/elements/<name>.json` adds the
element `<ns>:<name>`. It then works everywhere Fundamentum's own elements do: auras, reactions, affinities, weapon
hits, tooltips, `#tag` element strings and `/fundamentum element`. Every field is optional, so `{}` is a valid file.

| Field | Default | Meaning |
|---|---|---|
| `parent` | none | an element id (`fundamentum:fire` or another datapack element); the new one becomes its [variant](#variants-soul-fire-is-fire) |
| `damage_types` | `#<ns>:element/<name>` | the damage type tag whose hits are this element |
| `weapons` | `#<ns>:element/<name>` | the item tag whose hits are this element |
| `name` | `element.<ns>.element.<name>` | the lang key of its name |
| `color` | none | the name's colour, `"#RRGGBB"` or a number |
| `damage_attribute` | none | an attribute that scales the attacker's hits of this element (`1` is normal) |
| `resistance_attribute` | none | an attribute that resists it (`0.5` takes half) |

Attributes come from code, so a datapack can't make new ones. Point the two attribute fields at any attribute that
already exists (Fundamentum's `fundamentum:<e>_damage` and `fundamentum:<e>_resistance` for its elements), or leave them
out. With none, creatures still resist or are weak to the element through [affinities](#affinities).

A file whose id is already an element from code (such as `fundamentum:fire`), whose parent isn't an element, or whose
parents go in a loop, is skipped with a warning in the log. `/fundamentum element list` shows every element loaded,
where it came from and its parent.

### Example: frost

A frost element that counts as nothing else, with a variant, an aura, a reaction, a weapon and a weak creature. The
files, all in one datapack:

`data/mypack/fundamentum/elements/frost.json`, the element, using Fundamentum's ice attributes:

```json
{"color": "#9FE8FF", "damage_attribute": "fundamentum:ice_damage", "resistance_attribute": "fundamentum:ice_resistance"}
```

`data/mypack/fundamentum/elements/hoarfrost.json`, a variant of it:

```json
{"parent": "mypack:frost"}
```

`data/mypack/damage_type/frost.json` and `hoarfrost.json`, damage types to deal it with. `mypack:frost` is the
element's shared damage type: an element `<ns>:<name>` uses the damage type `<ns>:<name>` for its aura when one exists.

```json
{"message_id": "mypack.frost", "exhaustion": 0.1, "scaling": "when_caused_by_living_non_player"}
```

`data/mypack/tags/damage_type/element/frost.json`, the element's damage types (the variant's tag sits inside):

```json
{"values": ["mypack:frost", "#mypack:element/hoarfrost"]}
```

`data/mypack/tags/damage_type/element/hoarfrost.json` lists `mypack:hoarfrost` the same way.

`data/mypack/tags/item/element/frost.json`, weapons whose hits are frost:

```json
{"values": ["minecraft:packed_ice"]}
```

`data/fundamentum/data_maps/damage_type/element_aura.json`, so a frost hit leaves a frost aura:

```json
{"values": {"mypack:frost": {"aura": "#mypack:element/frost", "duration": 200, "max_stacks": 2}}}
```

`data/mypack/fundamentum/element_reaction/flash_freeze.json`, frost on water triples:

```json
{"trigger": "#mypack:element/frost", "aura": "#fundamentum:element/water", "damage": {"multiplier": 3}}
```

`data/fundamentum/data_maps/entity_type/element_affinity.json`, sheep take double frost:

```json
{"values": {"minecraft:sheep": {"resist": {"#mypack:element/frost": -1.0}}}}
```

And the name in `assets/mypack/lang/en_us.json`: `"element.mypack.element.frost": "Frost"`.

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
| soul_rend | soul fire on shadow | x1.5, soul particles |

Soul fire also sets off every fire reaction above (melt, quench, vaporize, overload, detonate, smother), because it is fire.

Its affinities: undead resist shadow and are weak to holy and soul fire (-0.25); vexes and allays resist soul fire
(0.5); the Warden is weak to it (-0.5); blazes take double water; endermen take more water;
guardians take more electric; polar bears resist ice; snow golems are immune to ice and weak to fire.

Test with `/fundamentum element` (see [Commands](../commands.md)).
