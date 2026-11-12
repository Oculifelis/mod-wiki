# Multiblocks

Structures players build out of blocks, with one controller block that checks the rest. Shapes live in datapacks,
matching turns and flips them, formed and unformed events let a mod react, a ghost preview shows players where blocks
go, and a recipe viewer page lists every structure.

Package `com.fundamentum.multiblock`, every version (NeoForge 26.1.2, 26.2, 26.3, 1.21.1; Forge 1.20.1). The same code
on all five; only the client tick hook for the preview is written per version.

## Patterns

One file per structure in `data/<ns>/fundamentum/multiblocks/<name>.json`. The structure's id is `<ns>:<name>`.

```json
{
  "layers": [
    ["ICI", "I.I", "IIG"],
    ["L L", " F ", "LLL"]
  ],
  "key": {
    "I": "minecraft:iron_block",
    "C": "minecraft:crafting_table",
    "G": ["minecraft:gold_block", "minecraft:raw_gold_block"],
    "L": "#minecraft:logs",
    "F": { "block": "minecraft:furnace", "state": { "facing": "north" } }
  },
  "controller": "C",
  "rotate": true,
  "mirror": false,
  "name": "multiblock.mymod.smelter"
}
```

- `layers` go bottom to top. Each layer's rows go north to south and each row's characters west to east. Rows in a
  layer must be the same length.
- A space means any block and `.` means air, unless the key names them. A key value of `"air"` also means air, and
  `"*"` means any block.
- A key value is a block id, a `#tag`, an object with `block` (or `tag`) and `state`, or a list of any of these.
  `state` only checks the properties it names. A block id the game doesn't know drops that choice, so a pattern can
  list blocks from mods that may be missing.
- `controller` is the key character of the controller block. It must appear exactly once.
- The file as written faces north (its first row is the front). With `rotate` (on by default) it also matches turned
  east, south and west. With `mirror` (off by default) it also matches flipped east to west. States in the key turn
  and flip with it, so a furnace facing north in the file faces east in an east-facing build.
- `name` is an optional translation key for the viewer page. Without it the page uses `multiblock.<ns>.<name>`, then
  the file name.

A broken file (no layers, a controller missing or used twice, a character missing from the key, uneven rows) is logged
and left out. Patterns travel to clients with the datapack, so the preview and viewer page work on servers.

## Matching and forming

```java
Multiblocks.Match m = Multiblocks.match(level, pos);        // any pattern with its controller at pos, or null
Multiblocks.Match m = Multiblocks.match(level, pos, id);    // one pattern
m.id(); m.facing(); m.mirrored(); m.positions();

Multiblocks.check(serverLevel, pos);    // match, remember as formed, post the events
Multiblocks.formed(serverLevel, pos);   // the formed structure at that controller, or null
Multiblocks.blockChanged(serverLevel, pos);  // recheck formed structures covering pos now
Multiblocks.forget(serverLevel, pos);   // drop it without an event
Multiblocks.missing(level, id, pos, facing, mirrored);  // cells not built yet
Multiblocks.build(level, id, pos, facing, mirrored);    // place the whole thing (tests, creative tools)
```

`match` only looks. Call `check` when a player uses the controller (or whenever the mod wants it formed). A new
structure posts `fundamentum:multiblock_formed` (`Events.MultiblockFormed(level, controller, structure, facing,
mirrored)`); cancel it and the structure stays unformed. Formed structures are checked again every second and when
`blockChanged` is called, and post `fundamentum:multiblock_unformed` (`Events.MultiblockUnformed(level, controller,
structure)`) once broken. After a datapack reload a formed structure is held to its new shape.

```java
FEvents.listen(Events.MultiblockFormed.class, (e, call) -> {
    if (!e.structure().namespace().equals("mymod")) return;
    // start the machine, or call.cancel() to refuse
});
```

Formed structures are kept in memory while the server runs. A mod that needs them after a restart calls `check` again
when the controller's block entity loads.

## Ghost preview

```java
Multiblocks.preview(player, id, controllerPos, facing, mirrored);
Multiblocks.clearPreview(player);
```

The player sees each missing block as its real block model at about 40% opacity. A wrong block in a cell shows the
wanted block tinted red with a red outline, and a cell that must be air gets a faint red box. It clears itself once
the structure is complete or the player changes dimension. The client checks the structure again only when a block in
its area changes (and on the slow safety timer, see [Hud](hud.md)), not every tick. Client tools can set one directly
with `Multiblocks.project(...)`. The packet is the same as before.

Operators also have `/fundamentum multiblock check <pos>`, `/fundamentum multiblock preview <id> <pos>` (facing the
player) and `/fundamentum multiblock preview clear`.

## Recipe viewer page

`fundamentum:multiblocks` shows every pattern in JEI, REI and EMI (where installed, see
[Recipe Viewers](recipe-viewers.md)): the blocks it takes with counts (up to twelve kinds, tags shown as all
their blocks), the controller, the size and the name. JEI and REI draw the structure itself as real block models at
the top of each entry. Guide pages show the same 3D view with `{{multiblock ...}}`, and it can be
turned by dragging.

## Test

`gradlew runServer -Pmultiblocktest` loads three test patterns and a broken one, builds them in every facing, swaps
blocks in and out (tag members, wrong blocks, a block in an air cell, a wrong furnace facing, a mirrored build),
forms and breaks them through the events, checks the viewer page and the preview packet, then stops the server and
writes `run-multiblocktest/multiblocktest-result.txt`.
