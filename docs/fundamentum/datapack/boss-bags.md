# Boss Bags

A boss named in a boss bag file drops none of its own loot. Each player who took part in the fight gets a bag at their
feet instead, theirs alone for a minute, and opening it rolls the loot table for that player and gives the boss's XP.

Files live in `data/<ns>/fundamentum/boss_bags/<name>.json`. A datapack file with the same id is merged over the mod's.
Every field is optional except that a file needs `entity`, `entities` or `tag`.

```json
{
  "entities": ["minecraft:wither"],
  "loot_table": "minecraft:entities/wither",
  "always": [{"item": "minecraft:nether_star", "count": 1}],
  "own_seconds": 60,
  "participation": {"hurt": true, "killer": true, "fighters": true, "radius": 24, "height": 12},
  "puff": ["#3A2A1E", "#D8B45A"],
  "name": "item.mymod.wither_bag",
  "sound": "minecraft:item.bundle.drop_contents"
}
```

A whole tag works too:

```json
{"tag": "#minecraft:skeletons", "participation": {"radius": 0}}
```

| Field | Default | Meaning |
|---|---|---|
| `entity` / `entities` | none | the bosses, one id or a list |
| `tag` | none | an entity type tag, or a list of them |
| `item` | `fundamentum:boss_bag` | the bag item dropped |
| `loot_table` | the boss's own | the table each bag rolls |
| `xp` | true | false lets the boss drop its XP as usual instead of putting it in the bags |
| `own_seconds` | 60 | how long a bag belongs only to its player before anyone can pick it up |
| `always` | none | items every bag holds besides its roll, as ids or `{"item", "count"}` |
| `participation` | see below | who counts as taking part |
| `puff` | umber and gold | colours of the puff when a bag opens, as `#hex` strings or numbers |
| `name` | none | a lang key or text for the bag's name |
| `sound` | bundle emptying | the sound when a bag opens |
| `enabled` | true | false turns the file off, so a pack can switch off a mod's bag |

## Who gets a bag

| Field | Default | Meaning |
|---|---|---|
| `hurt` | true | players who hurt the boss |
| `killer` | true | the player who dealt the killing blow |
| `fighters` | true | players on the boss's Fundamentum boss bar |
| `radius` | 24 | players this many blocks across from the boss when it fell (0 turns this check off) |
| `height` | 12 | how far up or down that check reaches |

Spectators never get a bag.
