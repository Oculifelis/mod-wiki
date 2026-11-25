# Factions

Reputation with groups of mobs and villagers. Each faction is one JSON file. Rep is kept on the player through death,
or on the scoreboard team when the faction is team shared.

Each faction is a file at `data/<ns>/fundamentum/factions/<name>.json`. Its id is `<ns>:<name>`. Every field is optional.

```json
{
  "name": "faction.mymod.wardens",
  "color": "#4A7FB0",
  "icon": "minecraft:shield",
  "description": "faction.mymod.wardens.desc",
  "members": ["minecraft:iron_golem", "#mymod:wardens"],
  "professions": ["minecraft:armorer"],
  "relations": {"mymod:raiders": {"type": "enemy", "spill": 0.5}},
  "min": -1000, "max": 1000, "start": 0,
  "ranks": [
    {"id": "outcast", "min": -1000, "attitude": "hostile", "price": 1.5},
    {"id": "stranger", "min": -100, "attitude": "neutral"},
    {"id": "friend", "min": 200, "attitude": "friendly", "price": 0.9,
     "rewards": {"items": [{"id": "minecraft:emerald", "count": 5}]}},
    {"id": "hero", "min": 700, "attitude": "defend", "price": 0.75}
  ],
  "actions": {
    "kill_member": -50,
    "kill_enemy": 10,
    "trade": 2,
    "break_block": {"rep": -5, "blocks": ["#mymod:warden_banners"]},
    "kill_member_alignment": {"mymod:order": -1}
  },
  "drift": {"per_day": 5, "toward": 0},
  "membership": {"joinable": true, "group": "mymod:sides", "min_rank": "friend", "leave_rep": -200},
  "team_shared": false
}
```

| Field | Default | Meaning |
|---|---|---|
| `name`, `description` | the id | lang keys or plain text |
| `color`, `icon` | none | shown in lists and screens |
| `kind` | `faction` | `deity` makes it a [god](gods.md) |
| `members` | none | entity ids or `#tags` that belong to it |
| `professions` | none | villager professions that belong to it |
| `relations` | none | other factions as `enemy`, `ally` or `neutral`, with `spill` as the share of a rep change passed on to them |
| `min`, `max`, `start` | -1000, 1000, 0 | the rep range and the starting rep |
| `ranks` | none | rank bands by `min` rep, each with an `attitude`, a `price` factor and one-time `rewards` |
| `actions` | none | rep for each act, and any key a mod fires with `Factions.act` |
| `drift` | none | rep moves this much per day toward `toward` |
| `membership` | not joinable | `joinable`, a `group` whose factions exclude each other, `min_rank`, `requires` (conditions) and the rep lost on leaving |
| `team_shared` | false | rep belongs to the scoreboard team |
| `enabled` | true | false turns it off |

Hostile members attack on sight, neutral ones act as in vanilla, friendly ones never target the player, and defending
ones also fight whatever attacks the player. Member villagers multiply their prices by the rank's `price`. Mobs of
enemy factions fight each other. An action named `<act>_alignment` moves [alignments](#alignments) when that act
happens.

Reaching a rank grants the unlock `<ns>:rank/<faction>/<rank>` and gives its rewards once. Joining grants
`<ns>:member/<faction>`.

## One faction from several packs

Several mods and datapacks can ship a file with the same faction id. The copies are combined the way tags are:

- `members` and `professions` from every copy are added together.
- `relations` and `actions` combine entry by entry, and a higher pack wins an entry both set.
- `ranks` combine by rank `id`, and a higher pack's rank replaces a lower one with the same id.
- `drift` and `membership` combine field by field. Every other field comes from the highest pack that sets it.
- A copy with `"replace": true` drops every copy below it.

A mod that wants its mobs in another mod's faction ships a file that lists only `members`:

```json
{"members": ["mymod:ghoul", "#mymod:restless"]}
```

## Rewards

Ranks, [quests](quests.md) and [boons](gods.md) share one rewards shape:

```json
{"items": [{"id": "minecraft:emerald", "count": 3}], "loot": "mymod:rewards/small", "xp": 50,
 "effects": [{"id": "minecraft:regeneration", "duration": 200, "amplifier": 0}],
 "unlocks": ["mymod:gate_key"], "rep": {"mymod:wardens": 25}, "alignment": {"mymod:order": 5}, "favour": 10}
```

Mods add their own keys with `Rewards.register`.

## Alignments

Plain numbers on the player, such as order against chaos.

Each axis is a file at `data/<ns>/fundamentum/alignments/<name>.json`.

```json
{"name": "Order", "min": -100, "max": 100, "start": 0}
```

## Commands

For operators:

| Command | What it does |
|---|---|
| `/fundamentum faction list` | every loaded faction |
| `/fundamentum faction info <player>` | rep, rank and memberships |
| `/fundamentum faction rep <player> <faction>` | reads rep |
| `/fundamentum faction rep <player> <faction> set <n>` or `add <n>` | changes rep |
| `/fundamentum faction join <player> <faction>` | adds a membership |
| `/fundamentum faction leave <player> <faction>` | removes one |
| `/fundamentum faction align <player> <axis> [set <n>]` | reads or sets an alignment |

## Known factions

Factions shipped by mods. Packs can add members to any of them by id.

| Faction | Mod |
|---|---|
| `arsmoriendi:dying_god` | Ars Moriendi |
| `arsmoriendi:host` | Ars Moriendi |
| `arsmoriendi:tempters` | Ars Moriendi |
| `arsmoriendi:undead` | Ars Moriendi |
| `ultimaratio:arcanum` | Ultima Ratio |
| `ultimaratio:celestine` | Ultima Ratio |
| `ultimaratio:emberhell` | Ultima Ratio |
| `ultimaratio:fluix` | Ultima Ratio |
| `ultimaratio:narian_fleet` | Ultima Ratio |
| `ultimaratio:raidbanner` | Ultima Ratio |
| `ultimaratio:voidmaw` | Ultima Ratio |
| `ultimaratio:voltforge` | Ultima Ratio |
| `ultimaratio:wildwood` | Ultima Ratio |
