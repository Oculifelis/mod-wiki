# Config

Two files in `config/netheragriculture/`. Both can also be edited in game from the mods list. Options marked
*restart* take effect when the world is loaded again.

## common.toml

### Overrides.LootModifiers

| Field | Default | Meaning |
|---|---|---|
| `piglinBarteringEnabled` | `true` | adds the mod's seeds, crops and Dead Vines to `minecraft:gameplay/piglin_bartering` |
| `striderEnabled` | `true` | Fabric only: striders drop Raw Strider Leg (`minecraft:entities/strider`) |
| `hoglinEnabled` | `true` | Fabric only: hoglins drop Raw Hoglin Meat in place of porkchops (`minecraft:entities/hoglin`) |
| `netherBridgeEnabled` | `true` | Fabric only: adds seeds and crops to `minecraft:chests/nether_bridge` |
| `bastionHoglinStableEnabled` | `true` | Fabric only: Hoglin Meat in place of porkchops in `minecraft:chests/bastion_hoglin_stable` |

On NeoForge these four loot changes are global loot modifiers in the mod's data, so a datapack can switch them off.

### Overrides.ConfiguredFeatureModifiers

| Field | Default | Meaning |
|---|---|---|
| `crimsonForestVegetationEnabled` | `true` | *restart*: adds the Glowing Fungus to `minecraft:crimson_forest_vegetation` |
| `crimsonNyliumBonemealEnabled` | `true` | *restart*: adds it to `minecraft:crimson_forest_vegetation_bonemeal` |
| `warpedForestVegetationEnabled` | `true` | *restart*: adds it to `minecraft:warped_forest_vegetation` |
| `warpedNyliumBonemealEnabled` | `true` | *restart*: adds it to `minecraft:warped_forest_vegetation_bonemeal` |

### ModCompatibility

| Field | Default | Meaning |
|---|---|---|
| `FarmersDelight.fullRecipeIntegrationEnabled` | `true` | with Farmer's Delight installed, turns off some of the mod's own recipes in favour of Farmer's Delight's cooking |
| `NethersDelight.useOnlyBlackFurnace` | `true` | with My Nether's Delight installed, removes some of its recipes (such as `mynethersdelight:hoglin_loin_cooking`) so the Black Furnace makes them |

## server.toml (per world)

### Entity

| Field | Default | Meaning |
|---|---|---|
| `burningFromItemsEnabled` | `true` | *restart*: foods that set you on fire do so |
| `burningFromBlazeFlightEnabled` | `true` | *restart*: Blaze Flight sets you on fire while flying |
