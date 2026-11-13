# For pack makers

Every number is data. Modules, upgrades, tiers, fuels and recipes can be added or changed from a datapack, a KubeJS
script or a Java addon. The mod's own content registers through the same public API, so an addon can do anything the
base mod does.

Precedence: built-in defaults, then datapacks (in pack order), then Java addons, then KubeJS scripts. A broken tuning
batch is rejected as a whole and the old values stay; errors name the file in the server log.

## Config

`config/fieldframe-common.toml`: `[machines] disabled` lists module ids switched off server-wide.

## Datapacks

| To change | Where (`data/<pack>/...`) |
|---|---|
| Machine speed, RF, ranges, intervals | `fieldframe/tuning/*.json`, e.g. `{"module": "fieldframe:fisher", "tunables": {"interval": 300}}` |
| Switch a machine off | `fieldframe/tuning/*.json`, `{"module": "fieldframe:nullifier", "disabled": true}` |
| Engine fuels | `fieldframe/fuels/*.json` |
| Remove recipes | `fieldframe/recipe_filters/*.json`, by id or by whole family |
| Any machine recipe | `recipe/` (`recipes/` on 1.20.1), `"type": "fieldframe:process"` |
| Galvanic Cell electrodes | `fieldframe/electrodes/*.json` |
| Heat sources | `fieldframe/temperatures/*.json` |
| Fluid Armor effects of a single fluid | `fieldframe/fluid_armor_effects/*.json` |
| Fluid Armor pair effects, 0.3.7 and later (which two FLORA fluids give which effect, how strong) | `fieldframe/fluid_armor_pairs/*.json` |
| Aura Chamber effects | `fieldframe/aura/*.json` |
| Tree Tapper logs, Fisher bait, Enchanter fluids | tags `fieldframe:tappable_logs`, `fieldframe:fisher_bait`, `fieldframe:experience_fluids` |

From 0.3.7 the Fluid Armor pair table ships as `fieldframe/fluid_armor_pairs/flora.json`, the 28 original FLORA effects. Your
file can move an effect to another pair, weaken or strengthen it, or turn it off. This one moves Speed to Ender with
Ender at half strength and turns off Redstone with Glowstone:

```json
{"pairs": [
  {"fluids": ["fieldframe:resonant_ender", "fieldframe:resonant_ender"], "effect": "speed", "strength": 0.5},
  {"fluids": ["fieldframe:liquid_redstone", "fieldframe:liquid_glowstone"], "remove": true}
]}
```

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

Other events: `operationStarting`, `operationCompleted`, `moduleInstalled`, `moduleRemoved`, `worldAction` (deny a
world module's break, place or use), `fuels`, `auras`, `electrodes`, `temperatures`, `fluidArmor`. Startup scripts can
also add chassis tiers above Resonant with `event.tier(...)`.
