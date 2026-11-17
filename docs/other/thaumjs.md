# ThaumJS

ThaumJS is an addon for [Thaumaturge](https://www.curseforge.com/projects/1628024) that adds [KubeJS](https://www.curseforge.com/projects/238086) support. Server scripts can add recipes, set aspects, add Infernal Furnace bonuses and write research, so a pack can tune Thaumaturge without writing JSON by hand.

It requires Thaumaturge 1.1.0 or newer and KubeJS 8. It adds no items or blocks, so it is only needed where scripts use it.

| Minecraft | Loader | ThaumJS |
|---|---|---|
| 26.1.2 | NeoForge 26.1.2.122 or newer | 0.1.0 |

[CurseForge project](https://www.curseforge.com/projects/1811724)

## What scripts can do

- Add crucible, infusion, infusion enchantment, arcane workbench and salis mundus recipes, each with the research that unlocks it.
- Set or remove the aspects of items, tags and mobs.
- Add or clear Infernal Furnace bonus drops.
- Write new Thaumonomicon entries and tabs.

Everything reloads with `/reload`. The recipe schemas are JSON files that KubeJS reads, so a datapack can change them.

```js
ServerEvents.recipes(function (e) {
  e.recipes.thaumaturge.crucible('minecraft:diamond', 'minecraft:coal', { ordo: 5, terra: 3 })
})
ThaumJSEvents.aspects(function (e) { e.item('minecraft:stick', { herba: 7 }) })
```

The [readme](https://github.com/Oculifelis/ThaumJS#readme) has an example for each event.

## Limits

Changing a single field of an existing research entry is not supported yet. Scripts replace the whole entry instead.

## Credits and licence

By Oculifelis. KubeJS is by LatvianModder and contributors, and Thaumaturge is by Leclowndu93150 and contributors. The licence is MIT.
