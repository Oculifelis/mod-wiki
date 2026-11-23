# Gods

Gods are [factions](factions.md) with `"kind": "deity"`. Devotion is their rep, so ranks, liked and hated acts
(`actions`), rival gods (`relations`) and drift all work as they do for factions. Favour is a separate pool that boons
spend.

A god is a file in `data/<ns>/fundamentum/factions/` with the faction fields plus these, all optional:

```json
{
  "kind": "deity",
  "name": "god.mymod.solenne",
  "domain": "sun",
  "symbol": "minecraft:sunflower",
  "pantheon": "mymod:dawn",
  "ranks": [{"id": "lapsed", "min": -1000, "attitude": "neutral"}, {"id": "devout", "min": 100}],
  "actions": {"kill_member": -100, "kill_enemy": 5},
  "favour": {"max": 100, "regen": 1},
  "prayer": {"devotion": 1, "favour": 2, "cooldown": 1200},
  "offerings": [{"item": "minecraft:gold_ingot", "devotion": 10, "favour": 5}, {"item": "#minecraft:flowers", "devotion": 1}],
  "follow": {"min_rank": "devout", "forsake": -100},
  "boons": {
    "mend": {"cost": 30, "min_rank": "devout", "cooldown": 6000, "rewards": {"heal": 10}},
    "second_life": {"cost": 100, "min_rank": "devout", "cooldown": 24000, "revive": true}
  },
  "wrath": {"enabled": true, "below": -200, "chance": 0.1, "cooldown": 6000, "rewards": {"lightning": true}}
}
```

| Field | Meaning |
|---|---|
| `domain`, `symbol`, `pantheon` | shown with the god, and `pantheon` places it in a pantheon |
| `favour` | the pool size and how much favour followers regain per minute |
| `prayer` | devotion and favour gained by praying, and the cooldown in ticks |
| `offerings` | items (ids or tags) and what each one gives |
| `follow` | what following needs (`min_rank`, `requires`) and the devotion lost by forsaking |
| `boons` | favour cost, rank, cooldown and [rewards](factions.md#rewards), and `revive: true` saves a follower from death |
| `wrath` | off unless enabled, and below this devotion the god may strike with its rewards |

## Miracles

Boons, rituals and wrath use the shared rewards plus these keys:

| Key | Value | Effect |
|---|---|---|
| `heal` | a number | heals the player |
| `weather` | `clear`, `rain`, `thunder` or `{"type", "duration"}` | changes the weather |
| `smite` | `{"damage", "radius"}` | lightning hits the nearest monster |
| `lightning` | `true` or `{"damage", "visual"}` | lightning hits the player |
| `spawn` | `{"entity", "count"}` | spawns mobs |
| `favour` | a number or `{"<god>": n}` | adds favour |

## Pantheons

Each pantheon is a file at `data/<ns>/fundamentum/pantheons/<name>.json`.

```json
{"name": "pantheon.mymod.dawn", "gods": ["mymod:solenne", "mymod:veyr"], "exclusive": true}
```

In an exclusive pantheon a player follows one god at a time.

## Shrines

Each shrine is a file at `data/<ns>/fundamentum/shrines/<name>.json`.

```json
{"deity": "mymod:solenne", "blocks": ["mymod:sun_altar"], "power": 1.0,
 "nearby": {"blocks": ["#minecraft:candles"], "radius": 4, "per": 0.1, "max": 1.0}, "desecrate": 50}
```

A built shrine uses `"multiblock": "<pattern id>"` in place of `blocks`, and players pray at its controller. Using a
shrine with an empty hand prays. Using it with an item offers that item. Each matching block nearby adds `per` to the
shrine's `power`, up to `max`. `desecrate` is the devotion lost for breaking it.

## Rituals

Each ritual is a file at `data/<ns>/fundamentum/rituals/<name>.json`.

```json
{"deity": "mymod:solenne", "shrine": "mymod:sun_shrine",
 "items": [{"item": "minecraft:gold_block", "count": 1}], "time": "night", "moon": [0],
 "min_rank": "devout", "cooldown": 24000, "devotion": 25, "favour": 20, "rewards": {"weather": "clear"}}
```

Praying at the shrine while carrying the items performs the first ritual that fits, and the items are used up.

## Favour

Favour is the mana pool `fundamentum:favour` at priority -1000, so a mana mod's own pool takes over where one exists.
It holds the favour of the player's first patron god.

## Commands

| Command | Who | What it does |
|---|---|---|
| `/gods` | anyone | lists gods, devotion and favour |
| `/gods follow <god>` | anyone | takes a patron |
| `/gods forsake <god>` | anyone | drops a patron |
| `/gods boon <god> <boon>` | anyone | asks for a boon |
| `/fundamentum god list` | operators | every loaded god |
| `/fundamentum god info <player>` | operators | a player's devotion and favour |
| `/fundamentum god devotion <player> <god> <value>` | operators | sets devotion |
| `/fundamentum god favour <player> <god> <value>` | operators | sets favour |
| `/fundamentum god wrath <player> <god>` | operators | calls down wrath |
