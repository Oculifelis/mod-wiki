# Versions

These pages document the **1.30.0** builds submitted on November 13. Submission and public release are separate; the [CurseForge files page](https://www.curseforge.com/projects/1765941/files) has the downloads currently available.

| Minecraft | Loader | Documented build |
|---|---|---|
| 26.1.2 | NeoForge | 1.30.0 |
| 26.2 | NeoForge | 1.30.0 |
| 26.3 | NeoForge | 1.30.0 |
| 1.21.1 | NeoForge | 1.30.0 |
| 1.20.1 | Forge | 1.30.0 |

Curios is required. JEI and REI recipe-viewer support is available on 26.x; EMI support is on the older two targets. All three viewers remain optional.

## In 1.30.0

The [shared systems](systems.md) include named stats and startup attribute declarations, stat-change events, configurable survival meters and multiblock patterns. Addons can read pattern cells and world positions by key, with extra data attached to a key.

The stat API supports base values and modifiers on living entities. The existing wing, thrown-weapon, moon, hook and summon systems remain part of the library.

## Wing display and older thrown weapons

The 1.28.0 work added synchronized wing flight phases and the older-version thrown-weapon ports. Those systems are also covered on these pages.

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
