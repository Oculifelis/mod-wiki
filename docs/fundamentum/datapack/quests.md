# Quests

Quests from data, offered by giver mobs and quest NPCs, tracked per player and kept through death.

Each quest is a file at `data/<ns>/fundamentum/quests/<name>.json`. Only `objectives` is needed.

```json
{
  "name": "quest.mymod.clear_the_road",
  "description": "quest.mymod.clear_the_road.desc",
  "faction": "mymod:wardens",
  "min_rank": "stranger",
  "givers": ["minecraft:iron_golem"],
  "npcs": ["mymod:captain"],
  "objectives": [
    {"type": "kill", "target": "#minecraft:raiders", "count": 5},
    {"type": "collect", "item": "minecraft:emerald", "count": 3}
  ],
  "time_limit": 24000,
  "repeatable": true,
  "cooldown": 72000,
  "turn_in": true,
  "group": "road",
  "rewards": {"rep": {"mymod:wardens": 50}, "xp": 100},
  "fail": {"rep": {"mymod:wardens": -10}}
}
```

| Field | Default | Meaning |
|---|---|---|
| `name`, `description` | the id | lang keys or plain text |
| `faction`, `min_rank` | none | the quest is offered only at this rank or higher |
| `requires` | none | conditions that must all pass |
| `givers` | none | mob ids or `#tags` that offer it on shift and use |
| `npcs` | none | quest NPC types that offer it |
| `objectives` | | the list below, all needed |
| `time_limit` | none | ticks before it fails |
| `repeatable`, `cooldown` | false, 0 | it can be taken again after this many ticks |
| `turn_in` | false | finished objectives still need handing in at a giver or NPC |
| `group` | none | the tab of the quest screen that lists it |
| `screen` | `fundamentum:journal` | the [quest screen](#quest-screens) its offers open in |
| `rewards` | none | the [rewards shape](factions.md#rewards) |
| `fail` | none | rewards given on failing or abandoning, usually lost rep |
| `enabled` | true | false turns it off |

## Objectives

Each objective takes a `count` (1 if left out).

| Type | Fields | Counts when the player |
|---|---|---|
| `kill` | `target` (ids or tags) and `faction` | kills a match |
| `break`, `place` | `block` | breaks or places a match |
| `collect` | `item`, `consume` | holds the items, which are taken unless `consume` is false |
| `craft` | `item` | crafts a match |
| `trade` | `target` | trades with a match |
| `visit` | `biome`, `structure`, `dimension`, `condition` | stands there |
| `survive_night` | | lives through a night |
| `act` | `act` | does a [faction act](factions.md) |
| `unlock` | `unlock` | has the unlock |
| `condition` | `condition` | passes the condition |

Mods add types with `Quests.register` and report progress with `Quests.signal`. The conditions `quest_done`,
`quest_active` and `location` work anywhere conditions do.

## Quest NPCs

The entity `fundamentum:quest_giver` takes its type from a file.

Each NPC type is a file at `data/<ns>/fundamentum/npcs/<name>.json`.

```json
{"name": "npc.mymod.captain", "texture": "mymod:textures/entity/captain.png", "slim": false,
 "wander": false, "invulnerable": true, "held": "minecraft:iron_sword", "screen": "mymod:wardens"}
```

The name shows over its head. The texture is a 64x64 skin in the player layout. Without one, the NPC wears one of the
nine vanilla player skins.

## Quest screens

Resource packs style the journal and the NPC screens. The same file works on every version.

Each screen is a file at `assets/<ns>/fundamentum/quest_screens/<name>.json`.

```json
{"layout": "book", "title": "screen.mymod.ledger", "book_style": "fundamentum:parchment_tome",
 "groups": [{"id": "road", "title": "group.mymod.road", "icon": "minecraft:compass"}],
 "colors": {"ink": "3a2414"}}
```

`layout` is `book`, `tabbed` or `list`. Screens have Accept and Abandon buttons. The Quest Journal key has no binding
at first. The HUD tracker is the `fundamentum:quest_tracker` layer and moves or hides in the HUD editor.

## Commands

| Command | Who | What it does |
|---|---|---|
| `/quests` | anyone | lists taken quests and their progress |
| `/quests accept <quest>` | anyone | takes a quest on offer |
| `/quests abandon <quest>` | anyone | drops a quest |
| `/fundamentum quest list` | operators | every loaded quest |
| `/fundamentum quest info <player>` | operators | a player's quests |
| `/fundamentum quest give <player> <quest>` | operators | gives a quest |
| `/fundamentum quest complete <player> <quest>` | operators | finishes it with rewards |
| `/fundamentum quest fail <player> <quest>` | operators | fails it |
| `/fundamentum quest reset <player> <quest>` | operators | clears it and its cooldown |
| `/fundamentum npc list` | operators | every quest NPC type |
| `/fundamentum npc spawn <npc>` | operators | places a quest NPC |
