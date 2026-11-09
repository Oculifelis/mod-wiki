# Config

Settings are in `config/mariculture-common.toml`.

## general

| Field | Default | Meaning |
|---|---|---|
| `zombie_fishing_gear_chance` | 0.0125 | chance (0 to 1) that a naturally spawned zombie carries a fishing rod and a bucket hat |
| `zombie_hat_drop_chance` | 0.1 | chance that such a zombie drops its bucket hat |
| `zombie_rod_drop_chance` | 0.05 | chance that such a zombie drops its fishing rod |
| `dragon_spawn_egg_enabled` | true | whether the Dragon Spawn Egg can summon an Ender Dragon |
| `natural_gas_catches_fire` | true | whether natural gas next to fire, torches or lava catches fire |
| `hardcore_diving` | 0 | 0 to 100: makes your air run out faster under water; higher is faster, 0 turns it off |
| `speedboat_vertical_percent` | 200 | how fast a Speed Boat at least 90% under water rises, in percent of the normal rate |

## fishery

| Field | Default | Meaning |
|---|---|---|
| `fishing_speed_multiplier` | 50 | 0 to 1000: ticks taken off the wait for a bite every tick while a Mariculture hook is in water or lava; 0 is vanilla speed. A datapack can override it ([For pack makers](packs.md#fishing-speed)) |
| `stargazer_prevents_spawns` | true | whether a Fish Feeder with a living Whitemargin Stargazer stops hostile mobs spawning within 16 blocks (8 up and down) of its tank |

## machines

Higher "work" numbers make a machine slower.

| Field | Default | Meaning |
|---|---|---|
| `sawmill_speed` | 650 | work per Sawmill batch, in hundredths of a tick (650 is 6 ticks) |
| `sawmill_output_multiplier` | 2 | multiplies how many blocks the Sawmill makes from one set of six |
| `fish_feeder_speed` | 200 | life a fish loses each feeder cycle (higher ages fish faster) |
| `fishing_net_speed` | 300 | a Fishing Net catches on one random tick in this many |
| `crucible_furnace_speed` | 40000 | work the Crucible Furnace needs per melted item |
| `hatchery_speed` | 100 | work a Hatchery needs per egg |
| `incubator_speed` | 400 | work an Incubator needs per batch |
| `dna_machine_speed` | 1000 | work the DNA Extractor needs per try (the DNA Injector needs five times this) |
| `autofisher_speed` | 2500 | work an Automatic Fisher needs per cast |
| `item_eject_ticks` | 20 | ticks between a machine pushing items out |
| `crucible_bonus_dusts` | true | whether melting ores can give bonus dusts |

## jewelry

| Field | Default | Meaning |
|---|---|---|
| `drops_on_death` | false | whether worn jewelry drops when its wearer dies (unless keepInventory or Reaper keeps it) |
| `leapfrog_jumps_per_damage` | 10 | jumps per point of wear on Leapfrog jewelry |
| `sonic_ticks_per_damage` | 1200 | ticks of sprinting per point of wear on Sonic the Hedgehog jewelry |
| `restoration_ticks_between_repairs` | 100 | ticks between Restoration repairs |
| `blink_milliseconds_between_blinks` | 0 | how long a player waits between blinks |
| `blink_ray_trace_distance` | 2000 | the furthest a blink reaches, in blocks (Blink also allows 16 per level) |

## factory

| Field | Default | Meaning |
|---|---|---|
| `dictionary_tag_groups` | ores, ingots, storage_blocks, nuggets, dusts, gems, raw_materials, dyes | groups of material tags (`c:<group>/<material>`, `forge:` on 1.20.1) whose items the Automatic Dictionary Converter treats as the same |
| `dictionary_blacklist` | lapis lazuli, ink sac, cocoa beans, bone meal, green dye | items the converter never converts from or to |
| `fluid_dictionary` | water, XP and ender fluids (below) | fluids the Fluid Auto-Dictionary converts between, as `family=fluid=ratio` |

The default `fluid_dictionary` converts water (`minecraft:water`, ratio 2000); XP between Mariculture's, Ender IO's, Mob
Grinding Utils', Industrial Foregoing's and CoFH Core's (200 each); and ender between Mariculture's and Thermal's
(25 each). Fluids of mods that aren't installed are skipped.

## plugins

Each turns one mod's support on or off; all default to `true`. See [Other mods](packs.md#other-mods) for what each does.

`aquaculture`, `biomesoplenty`, `railcraft`, `thermal`, `tconstruct`, `tconstruct_recipe_import`, `hephaestus`,
`hephaestus_recipe_import`, `forestry`, `complicated_bees`, `botania`, `bloodmagic`, `neovitae`, `redstone_arsenal`.

| Field | Default | Meaning |
|---|---|---|
| `bound_rod_weak_shard_fish` | 8 | fish an activated bound fishing rod catches for one weak blood shard |
