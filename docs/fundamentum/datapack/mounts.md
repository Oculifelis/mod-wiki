# Mounts

Mount items go in the Curios `mount` slot (item tag `#curios:mount`). The mount key (default **V**) calls the creature
and seats the player on it. The key again, getting off, unequipping, dying, changing dimension or logging out puts it
away. Summoned mounts are never saved.

**File:** `data/<ns>/fundamentum/mounts/<name>.json`, keyed by `item`. Only `entity` is required.

```json
{
  "item": "mymod:bat_whistle",
  "entity": "mymod:giant_bat",
  "speed": 0.3,
  "jump": 0.9,
  "flying": true,
  "flight_speed": 0.06,
  "step_height": 1.0,
  "health": 30,
  "invulnerable": true,
  "body": "minecraft:white_harness"
}
```

| Field | Default | Meaning |
|---|---|---|
| `item` | the file id | the mount item |
| `entity` | (required) | any rideable creature |
| `speed` | the creature's own | movement speed attribute |
| `jump` | the creature's own | jump strength (horses and the like) |
| `flying` | false | flies where the rider looks |
| `flight_speed` | the creature's own | flying speed |
| `step_height` | the creature's own | blocks it steps up |
| `health` | the creature's own | max health |
| `invulnerable` | true | mounts take no damage unless this is false |
| `body` | none | an item for the body slot (26.1.2: e.g. a harness for a happy ghast) |

Vanilla horses come tamed and saddled. On 26.1.2 every tamable creature is tamed, anything that can wear a saddle is
saddled, and creatures vanilla gives no steering (pig, strider, llama, dolphin) are steered by Fundamentum.
