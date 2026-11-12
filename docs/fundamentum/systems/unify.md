# Unify

When several mods add the same ingot, dust, ore or plate, Fundamentum keeps one and points the others at it. Recipes
give the kept item, the others are hidden from recipe viewers and creative tabs, duplicate ores stop generating, and
copies that still turn up (drops, hopper and item handler inserts) are swapped as they appear.

Package `com.fundamentum.unify`, every version (NeoForge 26.1.2, 26.2, 26.3, 1.21.1; Forge 1.20.1).

## Which items count as the same

Members of one item tag are the same material. `data/<ns>/fundamentum/unify/priority.json` says which tags count and
which mod wins:

```json
{
  "mods": ["minecraft", "create", "thermal", "mekanism"],
  "tags": ["c:ingots/*", "c:dusts/*", "c:ores/*"],
  "ignore_tags": ["c:ingots/netherite"],
  "ignore_items": ["somemod:special_ingot"],
  "materials": {
    "gold": { "keep": "minecraft:gold_ingot" },
    "osmium": { "mods": ["mekanism"] },
    "iron": { "unify": false },
    "tin": { "ores": false }
  }
}
```

- `tags` are patterns; `*` matches the rest of a path. A tag with fewer than two members is skipped.
- `mods` is the order of preference. The first mod in the list that has an item in the tag keeps it. With none of them
  present, the tag is left alone.
- The material is the last part of the tag path (`c:ingots/copper` is `copper`). Under `materials`:
  - `keep` names the kept item, or a list of them, tried in order.
  - `mods` puts mods in front of the global order for this material only.
  - `"unify": false` leaves the material alone.
  - `"ores": false` keeps its duplicate ores in worldgen.
- Every pack's copy is read, in id order, lowest pack first. A later file's `mods` go in front of the earlier ones and
  its tags and materials are added. `"replace": true` drops everything read before it.
- Fundamentum's own file puts `minecraft` first and covers the `c:` tags above plus nuggets, plates, gears, rods,
  wires, storage blocks, raw materials and gems. On Forge 1.20.1 it lists the same `forge:` tags too.

An item in two tags keeps the answer from the first tag (in id order). When the kept mod has several items in the tag
(stone and deepslate ores), each replaced item points at the kept item whose name shares the most words with it, so a
deepslate ore becomes the deepslate kept ore.

## Recipes

Recipe outputs are rewritten from JSON as recipes load, before they are decoded. By default the keys `result`,
`results`, `output` and `outputs` are rewritten, whether they hold a string, an object (`item` or `id`, the count is
kept) or a list of either. Forge's `forge:conditional` recipes are rewritten inside.

A mod whose recipe types keep their output somewhere else gets a fix file at
`data/<ns>/fundamentum/unify/fixes/<mod>.json`:

```json
{
  "recipes": [
    { "type": "somemod:crusher", "paths": ["outputs/*/stack"] },
    { "type": "somemod:press", "paths": ["product"], "replace_defaults": true }
  ],
  "skip": ["somemod:special_ingot_from_dust"],
  "skip_types": ["somemod:transmutation"]
}
```

- `paths` are extra places to rewrite, split on `/`. `*` matches every key or list index at that step.
- `"replace_defaults": true` rewrites only the listed paths for that type.
- `skip` lists recipe ids left alone; `skip_types` lists whole recipe types.

Where the hook sits differs by version and changes nothing for datapacks:

- 26.1.2 and 26.2 use NeoForge's recipe JSON event.
- 26.3 loads recipes as a datapack registry, so the hook rewrites each recipe file as it is parsed.
- 1.21.1 and 1.20.1 rewrite the map the recipe manager is handed.

## In the world

- **Dropped items** are swapped when the item entity joins the level.
- **Containers.** What hoppers, hopper minecarts and droppers insert is swapped, and so is what goes into any item
  handler built on the loader's `ItemStackHandler`. A simulated insert is swapped the same way as a real one.
- **Pickup** scans online players' inventories every few seconds. It is off by default.
- **Ores.** The biome modifier `fundamentum:unify_ores` (in `data/fundamentum/neoforge/biome_modifier/` or
  `data/fundamentum/forge/biome_modifier/` on 1.20.1) removes an ore feature when every block it places is a replaced
  ore. Features that also place a kept ore stay.

Every swap at run time posts `material_unified` (`Events.MaterialUnified(tag, from, to)`) through FEvents.

## Config

`config/fundamentum/fundamentum/unify.json5`, all booleans:

| Key | Default | What it does |
| --- | --- | --- |
| `enabled` | true | Master switch |
| `recipes` | true | Rewrite recipe outputs (next `/reload`) |
| `ores` | true | Remove duplicate ores (read when a world starts) |
| `item_entities` | true | Swap dropped items |
| `containers` | true | Swap hopper and item handler inserts |
| `pickup` | false | Swap items in player inventories |
| `hide_viewers` | true | Hide replaced items in JEI, REI and EMI (client) |
| `hide_creative` | true | Hide replaced items on creative tabs (client) |

## Code

```java
Unify.preferred(stack);          // the kept item's stack, count and data kept; the same stack if not replaced
Unify.preferred(item);           // also by Item or by FId
Unify.replaced(stack);           // whether unification points this item elsewhere
Unify.convert(stack);            // preferred plus the material_unified event
Unify.convertAll(container);     // swaps every replaced stack, returns how many
Unify.map().kept();              // the whole map: groups(), kept(), replacements(), tagOf(id), oreRemoved(id)
```

The map is rebuilt on every datapack load and sent to players as they join, so viewers hide the same items the server
replaces.

## Self test

`gradlew runServer -Punifytest` loads test items, tags, recipes and fix files, then checks the map, the recipe
rewrite, drops, hoppers, item handlers, inventories, viewer hiding, the ore modifier and the network copy. It writes
`run-unifytest/unifytest-result.txt` and prints `UNIFYTEST RESULT PASS`.
