# Summons

*Fundamentum 1.28.0: Forge 1.20.1; NeoForge 1.21.1, 26.1.2, 26.2 and 26.3.*

Summon items go in the Curios `summon` slot (item tag `#curios:summon`). Each calls minions that follow the player,
attack whatever the player hits or is hit by (and hostile mobs near them), and never hurt the player or each other.
Dead minions come back after `respawn` ticks. They drop nothing, are never saved, and go away when the item leaves the
slot or the player dies, logs out or changes dimension.

**File:** `data/<ns>/fundamentum/summons/<name>.json`, keyed by `item`. Only `entity` is required.

```json
{
  "item": "mymod:bone_staff",
  "entity": "minecraft:wolf",
  "count": 1,
  "health": 20,
  "damage": 4,
  "speed": 0.3,
  "respawn": 100,
  "leash": 24,
  "fire_immune": false
}
```

| Field | Default | Meaning |
|---|---|---|
| `item` | the file id | the summon item |
| `entity` | (required) | the creature |
| `count` | 1 | minions per item |
| `health` | the creature's own | max health |
| `damage` | the creature's own | attack damage |
| `speed` | the creature's own | movement speed |
| `respawn` | 100 | ticks before a dead minion comes back |
| `leash` | 24 | blocks it may stray before it's pulled back (at least 4) |
| `fire_immune` | false | takes no fire damage |

More summon slots come from Curios slot modifiers on gear (`curios:summon`). The `fundamentum:summon_damage` attribute
scales every minion's hits. Whips with a summon tag mark targets for minions; see [Whips](whips.md).
