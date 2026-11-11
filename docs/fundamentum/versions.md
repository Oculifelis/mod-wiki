# Versions

| Minecraft | Loader | Latest built | Notes |
|---|---|---|---|
| 26.1.2 | NeoForge | 1.28.0 | the main line: everything on this wiki; works under Iris shader packs |
| 1.21.1 | NeoForge 21.1 | 1.28.0 | everything except a few parts that need newer Minecraft (below) |
| 26.2 | NeoForge 26.2 | 1.28.0 | the same as 26.1.2 |
| 26.3 | NeoForge 26.3 | 1.28.0 | biome slices include surface rules |
| 1.20.1 | Forge 47 | 1.28.0 | the same as 1.21.1, with the same parts left out |

## What 1.21.1 leaves out

- The newer equipment-asset `wings` layer is unavailable. Wings can use an explicit texture path instead.
- Item model faces with `light_emission`: glowing faces use `neoforge_data` light in the model instead.
- Whip item model conditions are `ItemProperties` overrides instead of item model definitions.
- The `on_shelf` display context.
- A recipe book category for portal crafting (JEI still shows the recipes).
- Mounts saddle through `Saddleable`; mobs that only exist on 26.x (the happy ghast, the nautilus) aren't there.

## New in 1.28.0

Wing textures can use an explicit path, and other players see the wearer's flight phase. Thrown weapons and both boss-relic display modes work on 1.20.1 and 1.21.1 too. Biome slices supply surface rules on 26.3.

## New in 1.27.2

Whirl and Backswing can share a scythe. Backswing waits until Whirl ends.

## New in 1.27.1

Biome slices work on all five targets. On 26.3 they place biomes without supplying surface rules.

## New in 1.27.0

Weapon systems for content mods to use; Fundamentum itself still adds no items.

| System | What it does |
|---|---|
| Shields | parry at the right moment to stop the hit, knock back and reflect arrows; shield bash; on NeoForge 26.x some shields can be thrown and come back |
| Flails | a real swinging chain: spin up, ground slam, rope-dart launch; set up in datapacks with materials and kinds |
| Scythes | sweet spot at the end of reach, backswing, whirl, reaping pull, crescent wave, souls that heal and power up hits |
| Gauntlets | combo punches with a finisher |
| Sentries | placed turrets that aim at the nearest enemy, limited by sentry slots |
| Spears | reach and charge damage attributes; on 26.x thrown and picked up again |
| Thrown weapons (NeoForge 26.x) | knives, javelins, shuriken, bursting bottles, returning boomerangs; thrower damage class; Hurling, Farflight and Ricochet enchantments |
| Boss relics | trophy blocks with a floating gold likeness; a redstone signal makes it face forward |
| Biome slices (26.1.2 in 1.27.0) | add a biome to the Overworld or Nether from data, with or without TerraBlender |
| Better Combat support | when installed it handles left-click swings; each weapon type keeps its own moves. Not required |
