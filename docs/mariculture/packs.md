# For pack makers

## Three ways to change the machines

All three make the same changes to the same machine tables, and all three reload with `/reload`.

| Way | Editions |
|---|---|
| Datapacks: `data/<namespace>/mariculture/tweaks/*.json` | all three |
| KubeJS server scripts: `Mariculture.add(...)` | all three |
| CraftTweaker: `mods.mariculture.*` | 1.20.1 and 1.21.1 (CraftTweaker has no 26.1 release) |

Where two of them add the same thing, CraftTweaker wins over KubeJS and KubeJS wins over datapacks. Additions win over
Mariculture's own recipes; removals hide them. Changes apply on the server, so JEI on a client joined to a remote
server shows the built-in tables.

## The change format

A file, or a `Mariculture.add` call, holds one change, or `{"changes": [...]}` with several. Ids are registry ids,
fluids are full fluid ids and amounts are in mB.

| `type` | Fields |
|---|---|
| `vat_add` | `fluid1` `{fluid, amount}`; optional `fluid2`, `item` + `count`, `output_fluid`, `output_item` `{item, count}`; `time` (in vat steps of 30 ticks); `id` |
| `vat_remove` | `output_item` and/or `output_fluid` |
| `melting_add` | `input`, `temperature`, `fluid`, `amount`; optional `bonus` + `bonus_chance` (1 in n) |
| `melting_remove` | `input` |
| `fuel_add` | one of `item`, `tag`, `fluid`; `max_temperature`, `temperature_per_tick`, `ticks_per_step` |
| `fuel_remove` | one of `item`, `tag`, `fluid` |
| `anvil_add` | `input`, `output`, `count` (default 1), `hits` |
| `anvil_remove` | `input` |
| `casting_add` | `caster` (`ingot`, `nugget` or `block`), `fluid`, `result`, `amount` (the caster's default) |
| `casting_remove` | `caster`, `result` |
| `loot_add` | `item`, `chance` (percent), `rarity` (`junk`, `good`, `rare`), `dimension` (`any`, `overworld_like`, `nether`, `end`), `rod` (`dire`, a rod tier, or `any`), `exact` (only that rod) |
| `loot_remove` | `item` (from every rarity and dimension) |

```json
{"changes": [
  {"type": "vat_add", "fluid1": {"fluid": "minecraft:water", "amount": 500}, "fluid2": {"fluid": "minecraft:lava", "amount": 500},
   "output_item": {"item": "minecraft:stone", "count": 2}, "time": 3},
  {"type": "loot_add", "item": "minecraft:diamond", "chance": 5, "rarity": "rare", "dimension": "end", "rod": "super"},
  {"type": "loot_remove", "item": "minecraft:nether_star"}
]}
```

A broken file is skipped, with a log line naming the file and the field.

## KubeJS

In `kubejs/server_scripts/*.js`, pass a change as an object, as `{changes: [...]}`, or as a JSON string:

```js
Mariculture.add({type: 'anvil_add', input: 'minecraft:cobblestone', output: 'minecraft:gravel', hits: 2})
Mariculture.add({changes: [{type: 'melting_remove', input: 'minecraft:iron_ingot'}]})
Mariculture.add('{"type": "fuel_add", "tag": "c:rods/blaze", "max_temperature": 2000, "temperature_per_tick": 200, "ticks_per_step": 4}')
```

The changes are cleared before every server script load. KubeJS also loads `kubejs/data/` as a datapack, so the JSON
files above work there too.

## CraftTweaker

```zenscript
mods.mariculture.Vat.addRecipe(<fluid:minecraft:water> * 500, <fluid:minecraft:lava> * 500, <item:minecraft:stone>, 2);
mods.mariculture.Crucible.addRecipe(900, <item:minecraft:diamond>, <fluid:mariculture:molten_iron> * 144);
mods.mariculture.Crucible.addFuel(<item:minecraft:blaze_rod>, 2000, 200, 2400);
mods.mariculture.Casting.addIngotRecipe(<fluid:minecraft:lava> * 250, <item:minecraft:magma_block>);
mods.mariculture.Anvil.addRecipe(<item:minecraft:cobblestone>, <item:minecraft:gravel>, 10);
```

Each has a matching `removeRecipe` (or `removeFuel`). Vat times are in vat steps of 30 ticks.

## Fishing speed

`fishing_speed_multiplier` in the [config](config.md#fishery) (default 50) is how many ticks a Mariculture hook takes
off its wait for a bite every tick, in water and in Nether lava. A datapack can override it and speed up single rods:

```json
// data/<namespace>/mariculture/fishing_speed/<name>.json
{"speed_multiplier": 20, "rods": {"mariculture:titanium_fishing_rod": 10}}
```

Files are read in id order: the last `speed_multiplier` wins, rod bonuses add up, and the result never goes below 0.

## Other mods

Each of these can be turned off under `plugins` in the [config](config.md#plugins).

| Mod | What Mariculture does with it |
|---|---|
| Aquaculture 2 | its worms are bait; Mariculture fish and salt make its fillets; its fish melt into fish oil |
| Biomes O' Plenty | salinity and temperature for its biomes; its flowers crush into dye on the anvil |
| Railcraft Reborn | its steel tools and armour melt in the crucible |
| Thermal Series | redstone and glowstone melt into Thermal's fluids in the crucible |
| Tinkers' Construct (1.20.1) | natural gas fuels the smeltery; titanium, rutile and magnesium melt, cast and alloy in it; every smeltery melting and casting also works in Mariculture's crucible and casters |
| Hephaestus (26.1.2) | titanium, rutile and magnesium melt, cast and alloy in its smeltery; titanium makes tool parts; its meltings and castings work in Mariculture's machines |
| Forestry (1.20.1, 1.21.1) | its bioethanol works as Mariculture's; fish squeeze into fish oil; its bees craft into bee bait |
| Complicated Bees | its drones, princesses and queens craft into bee bait |
| Botania | the living rod, petal bait, the Manafish, Botania loot on the living rod, and mana pearls from oysters |
| Blood Magic (1.20.1) / Neo Vitae (1.21.1, 26.1.2) | the bound fishing rod, its bait and loot, and blood-shard mass fishing |
| Redstone Arsenal | its flux-infused fishing rod catches Mariculture fish and loot; flux dust is bait |
| Thaumaturge (26.1.2) | aspects on Mariculture's items |

Which mod versions each edition supports is on [Versions](versions.md).
