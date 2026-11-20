# For pack makers

Every number is data. Modules, upgrades, tiers, fuels and recipes can be added or changed from a datapack, a KubeJS
script or a Java addon. The mod's own content registers through the same public API, so an addon can do anything the
base mod does.

Built-in defaults apply first, then datapacks (in pack order), then Java addons, then KubeJS scripts. A broken tuning
batch is rejected as a whole and the old values stay; errors name the file in the server log.

## Config

`config/fieldframe-common.toml`: `[machines] disabled` lists module ids switched off server-wide.

## Datapacks

| To change | Where (`data/<pack>/...`) |
|---|---|
| Machine speed, RF, ranges, intervals | `fieldframe/tuning/*.json`, e.g. `{"module": "fieldframe:fisher", "tunables": {"interval": 300}}`; every key is listed on [Tuning keys](tuning.md) |
| Switch a machine off | `fieldframe/tuning/*.json`, `{"module": "fieldframe:nullifier", "disabled": true}` |
| Engine fuels | `fieldframe/fuels/*.json` |
| Remove recipes | `fieldframe/recipe_filters/*.json`, by id or by whole family |
| Any machine recipe | `recipe/` (`recipes/` on 1.20.1), `"type": "fieldframe:process"` |
| Galvanic Cell electrodes | `fieldframe/electrodes/*.json` |
| Heat sources, and the waste heat a working Heater, Magma Crucible, Pyrolyzer, Alloy Smelter or Boiler gives a Hot Junction | `fieldframe/temperatures/*.json` |
| How cold a Condenser or Steam Turbine water face must be to return most of the steam | `fieldframe/tuning/*.json`, module `fieldframe:steam_turbine`, tunable `cold_kelvin` |
| Field Coil power and field width, and how much a Field Receiver takes, 0.4.0 and later | `fieldframe/tuning/*.json`, modules `fieldframe:field_coil` (tunables `rf_per_tick`, `radius_per_coil`) and `fieldframe:field_receiver` (`rf_per_tick`) |
| Fluid Armor effects of a single fluid | `fieldframe/fluid_armor_effects/*.json` |
| Fluid Armor pair effects, 0.3.7 and later (which two FLORA fluids give which effect, how strong) | `fieldframe/fluid_armor_pairs/*.json` |
| Exchanger ring speed, Fuzzy defaults, and each tier's largest size, starting size and modes, 0.3.9 and later | `fieldframe/exchanger/*.json` |
| Tag Unifier mod order (whose ingots, nuggets, dusts, plates and gears win), 0.3.9 and later | `fieldframe/unification/*.json` |
| Aura Chamber effects | `fieldframe/aura/*.json` |
| Treadmill animals, their food and RF | `fieldframe/treadmill/*.json` |
| Blocks a frame accepts inside its walls, and the storage each adds | `fieldframe/frame_components/*.json` |
| Graviton Hook range, shot and pull speed, hook count; where the Arc and Tesla Whip lash leaves the handle | `fundamentum/hooks/*.json`, `fundamentum/whips/*.json` (read by Fundamentum) |
| Tree Tapper logs, Fisher bait, Enchanter fluids | tags `fieldframe:tappable_logs`, `fieldframe:fisher_bait`, `fieldframe:experience_fluids` |
| Latex logs, lightning rods, electrolytes, turbine and excavator fluids, explosives | tags `fieldframe:latex_logs`, `fieldframe:lightning_rods`, `fieldframe:electrolytes`, `fieldframe:turbine_fluids`, `fieldframe:excavator_fluids`, `fieldframe:explosives` |

From 0.3.7 the Fluid Armor pair table ships as `fieldframe/fluid_armor_pairs/flora.json`, the 28 original FLORA effects. A
pack's file can move an effect to another pair, weaken or strengthen it, or turn it off. This one moves Speed to Ender with
Ender at half strength and turns off Redstone with Glowstone:

```json
{"pairs": [
  {"fluids": ["fieldframe:resonant_ender", "fieldframe:resonant_ender"], "effect": "speed", "strength": 0.5},
  {"fluids": ["fieldframe:liquid_redstone", "fieldframe:liquid_glowstone"], "remove": true}
]}
```

The Tag Unifier ships `fieldframe/unification/default.json`, `{"replace": true, "prefer": ["metallurgy", "minecraft", "fieldframe"]}`.
A file with `{"prefer": ["create"]}` puts Create first and keeps the rest in order. `"replace": true` sets the whole list.

Metallurgy's alloyer and crusher recipes come in as `fieldframe:alloying/metallurgy/<name>` and
`fieldframe:crushing/metallurgy/<name>`; ship a recipe with that id to replace one.

## KubeJS

The script surface is the same on all three editions.

```js
// startup script: a new module
FieldframeEvents.registerModules(event => {
  event.processor('kubejs:smasher', 'kubejs:smashing').stage('automation').displayName('Smasher')
    .faceTexture('fieldframe:block/module/crusher').tunable('speed', 0.5, 4, 1.5, 'x')
})

// server script: recipes and tuning
ServerEvents.recipes(event => {
  event.custom(Fieldframe.recipes.process('kubejs:smashing').input('minecraft:cobblestone', 1)
    .result('minecraft:sand', 1).result('minecraft:flint', 1, 0.25).duration(40).energy(10).json())
})
FieldframeEvents.tuning(e => e.tune('fieldframe:fuel_engine', 'rf_per_tick', 60))
```

The other events are `operationStarting`, `operationCompleted`, `moduleInstalled`, `moduleRemoved`, `worldAction` (deny a
world module's break, place or use), `fuels`, `auras`, `electrodes`, `temperatures`, `fluidArmor`, `treadmill`,
`frameComponents` and `recipeFilter`, plus the client event `manual`. Startup scripts can
also add chassis tiers above Resonant with `event.tier(...)`.
