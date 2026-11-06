# KubeJS

**Fundamentum has no KubeJS support.** It adds no KubeJS bindings, events or recipe schemas.

You don't need them for most things:

- **Everything on the [Datapacks](datapack/index.md) pages is plain JSON**, so KubeJS can write it the same way it
  writes any datapack file (with a server data event that adds JSON, or by dropping files in `kubejs/data/`).
- **Portal crafting recipes** are ordinary recipes of type `fundamentum:portal_crafting`, so they can be added as raw
  JSON recipes:

    ```js
    ServerEvents.recipes(event => {
      event.custom({
        type: 'fundamentum:portal_crafting',
        ingredient: {item: 'minecraft:gold_ingot'},
        result: {id: 'minecraft:netherite_scrap', count: 1},
        portal: 'minecraft:nether_portal'
      })
    })
    ```

    The ingredient is written however the Minecraft version's recipes write one.
- **Tags** (creature types, elements, damage classes, Curios slots) are ordinary tags, so KubeJS's tag events work.
- **Attributes** (`fundamentum:crit_chance` and the rest) are ordinary attributes, so item attribute modifiers set from
  KubeJS work.

What needs Java: reacting to a moon rising or a night event ending, custom element reactions in code, new whip
styles, mount and summon behaviour beyond the JSON fields. See the [API](api.md).
