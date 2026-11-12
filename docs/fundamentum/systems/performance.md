# Performance

Fundamentum's systems react to game events instead of checking every player or structure every tick. Each one keeps
a slow full check in case something changes in a way no event reports. Those checks are spread over their interval, so
a hundred players are not all checked on the same tick.

## Config

`config/fundamentum/fundamentum/performance.json5` (or per world, see [Config](config.md)). Every value is in
seconds, and 0 turns that check off.

| Key | What it is | Default |
|---|---|---|
| `unlocks_recheck_seconds` | full unlock check per player. Inventory, advancement, stat, unlock and dimension changes recheck only the unlocks they can affect | 60 |
| `multiblocks_recheck_seconds` | full check of each formed structure. A block change inside one rechecks it right away | 60 |
| `stats_recheck_seconds` | full stat check per player. Inventory, equipment, effect and unlock changes recheck the stats they feed | 30 |
| `stats_volatile_seconds` | how often stats nothing announces are read (mana, vanilla stats, scoreboards, other mods). Only runs when such a stat is declared | 2 |
| `music_recheck_seconds` | full music check per player. Biome, structure, combat and boss changes are followed as they happen | 30 |
| `transfer_resync_seconds` | full comparison of tracked tanks. A tank is sent when it changes and when a player loads its chunk | 30 |
| `seasons_recheck_seconds` | how often Serene Seasons is asked for the season, when it is installed | 30 |
| `config_recheck_seconds` | full reread of the config files. Files are reread as soon as the system reports a change in their folder | 60 |
| `survival_step_seconds` | how often survival meters are worked out. A longer step does the same seconds of change at once | 1 |

## Measured

On 26.1.2, `gradlew runServer -Pperftest` (world under `run-perftest`, never build a jar with it) fakes 1, 20 and 100 players
with 10, 100 and 1000 formed multiblocks, times every system's server tick and ends with `PERFTEST RESULT PASS`.
The other versions share the same code. Microseconds per tick, idle players, median / mean / worst:

| Players | Before | After |
|---|---|---|
| 1 | 3.7 / 70.4 / 8615 | 17.3 / 51.6 / 4758 |
| 20 | 2.8 / 223.9 / 14951 | 73.4 / 121.4 / 2046 |
| 100 | 2.7 / 892.3 / 26698 | 172.9 / 194.0 / 4435 |

Before, most ticks did nothing and every second or so one tick did all the work at once, which shows as a low median
and a large worst case. Now the work is spread out. The mean at 100 players is less than a quarter of what it was, and
the worst tick is a sixth.

At 100 players the biggest changes were Unlocks (mean 447.7 to 19.4), Multiblocks (274.9 to 30.3) and Survival (worst
6038 to 406). Survival is most of what is left. It works every meter for every player, so its cost follows the meters
a pack declares and `survival_step_seconds`.

## Left as they were

Hooks, mounts, bosses, armor sets, ammo, effects, moons and night events, and whip tags still run per tick. Each only
touches entities that are already doing something (a hook in flight, a boss alive, an effect running) and costs
nothing measurable when idle.
