# Creature types and damage

Creature types are entity type tags, `#fundamentum:creature/<type>`. Fundamentum starts with `undead`, `arthropod`,
`aquatic`, `illager`, `construct` and `boss`; any mod or datapack may add types or members. For example,
`data/fundamentum/tags/entity_type/creature/construct.json`:

```json
{"values": ["minecraft:iron_golem", "minecraft:snow_golem", "mymod:clockwork_knight"]}
```

## Damage rules

Rules scale damage against a type. **File:** `data/<ns>/fundamentum/creature_damage/<name>.json`

```json
{"creature": "undead", "weapon": "#mymod:holy_weapons", "damage": "#minecraft:is_fire", "multiplier": 1.5}
```

| Field | Required | Meaning |
|---|---|---|
| `creature` | yes | the type (`undead`, or a full tag id) |
| `multiplier` | yes | damage multiplier |
| `weapon` | no | an item tag the weapon must be in |
| `damage` | no | a damage type tag the hit must be in |

A rule with neither `weapon` nor `damage` applies to every hit on that type. Matching rules multiply together.
Ostentum uses one to make pickaxes hit constructs for 1.5x.
