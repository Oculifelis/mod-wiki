# Relics

A relic is a trophy for a boss: the boss's gold likeness floating over a stand. Relics are data only. One
file, `data/<ns>/fundamentum/relics/<name>.json`, makes the relic `<ns>:<name>`: its item, its stand, its drop and its
recipe viewer page. No code, no blocks, no items, no models are needed in the mod (or datapack) that adds it.

Package `com.fundamentum.relic`, every version (NeoForge 26.1.2, 26.2, 26.3, 1.21.1; Forge 1.20.1).

## How it works

- **One item for every relic**, `fundamentum:relic`. Which relic it is lives in the stack's data component
  `fundamentum:relic` (on Forge 1.20.1, the stack's NBT under the same name). The item takes the relic's name, rarity
  and tooltip and draws as a small copy of the relic.
- **Bases**. The relic stands on a base block. A base is registered once with the sizes it comes in (1 to 5 blocks
  across): one anchor block per size, `<base>_<size>`, plus one filler block, `<base>_filler`, for the other cells of a
  wide stand. Fundamentum registers `fundamentum:relic_stand` (sizes 1 to 5), the default for every relic. Which relic
  stands on it is block entity data (`fundamentum:relic`), so one base serves every relic.
- **The base never exists for the player.** Bases have no item, recipe, loot table or tag; the relic item is the only
  thing a player holds. There is no blank relic in any creative tab, a blank `/give @s fundamentum:relic` is refused
  with a message (use `/fundamentum relic give <id> [players]`), and the blank item, the bases and fillers are hidden in
  JEI, EMI and REI. A blank stack that turns up anyway is called "Unknown relic" and places nothing.
- **A relic whose file is gone** (a datapack removed, a mod uninstalled): the stand keeps the id, draws its base alone,
  and drops nothing when broken. Put the file back and the relic comes back. Each missing id is logged once.

### Placing

- Odd sizes (1, 3, 5) centre on the block the player placed.
- Even sizes (2, 4): the placed block is one cell of the middle 2x2, and the stand grows away from the player and to
  their right. The figure stands at the stand's true centre either way.
- Every cell of the footprint must be free and the layer above all of them clear; otherwise nothing is placed and the
  player is told the size it needs.
- Breaking any cell breaks the whole stand, and the relic drops once. In creative it drops nothing.

### Turning, bobbing, redstone

The likeness always floats and bobs. With no redstone signal it turns slowly, one full turn every `turn_ticks`. With a
signal (into any cell of the stand) it eases round to face the way the stand was placed and holds there, still bobbing;
when the signal goes it starts turning again from where it stood. The turn is kept by the block entity on both sides,
so every player sees the same angle.

## Making a relic

    data/mymod/fundamentum/relics/my_boss.json

    { "boss": "mymod:my_boss", "size": 3, "name": "My Boss Relic", "drop": "killer" }

That is a whole relic: the boss's own model in gold, on Fundamentum's gold stand, 3x3, handed to the player who landed
the killing blow. `/fundamentum relic give mymod:my_boss` gives one. In code: `Relics.stack(FId.of("mymod", "my_boss"))`.

### Fields

Lengths are in pixels (sixteenths of a block). Only `boss` is required. Ids are `namespace:path`; texture ids are full
paths (`mymod:textures/entity/relic/x.png`).

| Field | Default | Meaning |
|---|---|---|
| `boss` | required | Entity type id of the boss that gives the relic. |
| `size` | `1` | Blocks across, 1 to 5 (`"single"` = 1 and `"grand"` = 3 still read). |
| `name` | from the id | Shown name when the lang has neither `relic.<ns>.<name>` nor `block.<ns>.<name>`. With none, the id's path in words (`small_thing` is "Small Thing"). |
| `base` | `"fundamentum:relic_stand"` | The base it stands on: a base id, or an object (below). A base that lacks the size falls back to Fundamentum's stand. |
| `base.id` | `"fundamentum:relic_stand"` | The base id, inside the object form. |
| `base.tint` | none (gold as drawn) | Recolours the base: one colour or a ramp, dark to light. |
| `base.layer`, `base.texture`, `base.glow` | the base's own | A model layer to draw as the base instead, its texture and unlit glow texture. |
| `base.top` | the base's own | Where the figure's float starts, over the stand's floor. |
| `rarity` | `"rare"` (`"epic"` from size 3) | Item rarity: `common`, `uncommon`, `rare`, `epic`. |
| `stack` | `16` | Item stack size (1 to 99). |
| `light` | `9` | Light level of the stand. |
| `drop` | `"none"` | `"drops"`: falls with the boss's drops. `"killer"`: straight into the inventory of the player who landed the killing blow (or where the boss died). `"none"`: the mod hands it out (`Relics.hand`). |
| `description` | none | Translation key of one grey tooltip line. |
| `jei` | `jei.<ns>.info.<name>` if the lang has it | Translation key of extra text on the recipe viewer page. |
| `figure.layer`, `figure.texture`, `figure.glow` | none | Model mode: a ready-made model layer, its gold texture and unlit glow. Absent: entity mode (the boss's own renderer, gilded). |
| `figure.offset`, `figure.scale` | `[0,0,0]`, fit | Model mode: root offset in model pixels (y down) and scale. Entity mode: `scale` overrides the fit. |
| `figure.entity` | `boss` | Entity mode: the entity drawn. |
| `figure.phases` | `[1]` | Entity mode: phases shown, one figure each, standing round the middle. Posed by `RelicFigure` or `RelicClient.poser`. |
| `figure.wide`, `figure.tall` | `18`, `21` (grown with size) | Entity mode: the circle the figure sweeps and its height; it is scaled to fit both. |
| `figure.float` | `2.5` | How far the figure's lowest point floats over the base's top. |
| `figure.radius` | `0.92` | Several phases: how far from the middle each figure stands, in blocks. |
| `figure.bounds` | measured | Entity mode: the figure's box at scale 1, in blocks, when measuring gives a poor fit. |
| `tint` (or `figure.tint`) | gold ramp | The figure's colour ramp, dark to light (`#RRGGBB`, `RRGGBB` or `0xRRGGBB`). Blank means gold. A model-mode figure is only recoloured when this is set. |
| `tint_floor` | `0.7` | How far up the ramp the darkest texel starts (0 to 1). |
| `bob.height`, `bob.period`, `bob.phase`, `bob.centred` | `1`, `100`, `0`, `false` | The bob. |
| `turn_ticks` | `900` | Ticks per full turn when unpowered (at least 20). |

Still read but no longer used (the stand's block properties are the base's now): `part`, `part_light`, `shape`,
`part_shape`, `strength`, `resistance`, `fire_resistant` (relics never burn).

The files are a synced data table (`Relics.TABLE`). A datapack file of the same id is merged over the mod's and
changes everything live on world load and `/reload`, size and base included (stands already placed keep their
footprint until broken). The creative tab and the recipe viewers refresh with it.

Lang keys: `relic.<ns>.<name>` (name), `jei.<ns>.info.<name>` (recipe viewer text), and any key a file names in `description`.

## Bases

A mod with its own look registers a base while it is constructed:

    RelicBases.register(FId.of("mymod", "altar"), new int[] {1, 3},
        n -> new RelicBases.Look("mymod:altar_" + n, "mymod:textures/entity/altar_" + n + ".png", null, n == 1 ? 10F : 28F, 1F));

This registers `mymod:altar_1`, `mymod:altar_3` and `mymod:altar_filler`. A `Look` with a null layer draws the anchor's
own block model instead (the mod supplies blockstates and models for it). A factory overload makes anchors of a
`RelicBlock` subclass. Relic files pick it with `"base": "mymod:altar"`. The mod supplies the layer definitions (or
block models) and textures; it adds no items, loot or tags for them.

Fundamentum's stand is Ars Moriendi's gold pedestal with a diamond: its 1x1 and 3x3 models, with 2 scaled from the 1x1
and 4 and 5 from the 3x3.

## API

- `Relics.stack(FId)`: a stack of the relic. `Relics.def(String id)`: its declaration as it stands now, or null.
- `Relics.name(FId)`: its shown name. `Relics.give(...)`, `Relics.hand(id, players)`: give to players, dropping at their
  feet when the inventory is full.
- `Relics.RELIC`: the stack data. `Relics.ITEM`, `Relics.STAND`, `Relics.ENTITY`, `Relics.TABLE`, `Relics.TAB`.
- `RelicBases.register`, `get`, `all`, `anchorFor(def)`, `look(anchor, def)`.
- Events (`FEvents`): `RelicPlaced` (cancellable), `RelicBroken`. See `EVENTS.md`.
- Client: `RelicClient.poser(entityType, (entity, phase) -> ...)` poses an entity-mode stand-in; an entity class may
  instead implement `RelicFigure.relicPose(phase)`.

### Deprecated: `Relics.register`

`Relics.register(owner, modid, blocks, items, [blockEntities, entityName,] names...)` still compiles and works, so a
mod written for the old system keeps loading. It no longer registers anything: the `RelicSet` it returns hands out
holders of the shared blocks and item (`block(name)` is the stand at that relic's size, `part(name)` the stand's filler,
`item(name)` is `fundamentum:relic`, `entity()` is `fundamentum:relic`, `stack(name)` a stack of that relic). Blocks and
items the mod used to own under its own ids are gone, so worlds that held them need the remap below.

## Moving Ostentum over (to do in Ostentum, not done here)

Ostentum registers its four relics through `Relics.register` (`wither_relic`, `elder_guardian_relic`, `warden_relic`,
`dragon_relic`, plus the frame `dragon_relic_frame` and its own block entity `ostentum:relic`). With this Fundamentum it
compiles and runs, but its own ids no longer exist. What Ostentum must change:

1. **Drop its relic registrations.** Remove the `SET` fields that hand out blocks and items, its `BLOCK_ENTITIES`
   register and the `ostentum:relic` block entity. Keep the four files in `data/ostentum/fundamentum/relics/`; they now
   make `ostentum:wither_relic` and the rest by themselves.
2. **Files.** Replace `"size": "grand"` with `"size": 3` (both read). Remove the `base` layer objects that point at
   `ostentum:relic_base_1x1` / `_3x3`: Fundamentum's stand is the same model (moved here). Keep `figure` as is.
3. **Code that hands out relics** (`DRAGON_RELIC_ITEM`, `new ItemStack(...)` of a relic): use
   `Relics.stack(FId.of("ostentum", "dragon_relic"))`.
4. **Old worlds.** Placed relic blocks and held relic items under `ostentum:*_relic` ids would be lost. Ostentum keeps,
   for one or two versions, hidden legacy blocks and items under the old ids (no creative entry, hidden in viewers):
   a legacy block's block entity ticks once, puts `fundamentum:relic_stand_<n>` with the relic id in its place (and the
   fillers, replacing `dragon_relic_frame`), and a legacy item turns itself into `Relics.stack(...)` on its first
   inventory tick. Then the legacy ids are removed.
5. **Lang.** `block.ostentum.<name>` keeps working (it is the second name looked up); `relic.ostentum.<name>` is the
   new key. Tooltips: name the key in each file's `description`.
6. **Models and textures** for the pedestal (`client.RelicModels` base layers, `textures/entity/relic/base_*`) can go;
   the figure layers stay.
7. Ostentum's page and dependency: relics now need the Fundamentum release that carries this system.

## Testing

`gradlew runServer -Prelictest` (world under `run-relictest/`) loads three relic files from a test datapack (3x3, 2x2
with a base tint, 1x1 with a figure tint) and checks: no blank relic or base in any creative tab, the relic tab lists the
files, a blank `/give` is refused, footprints and fillers of the 3x3 and 2x2, blocked placements fail, breaking a filler
breaks the stand, an unknown relic keeps its id and drops nothing, names, recipe viewer hiding and subtypes, and the
deprecated `Relics.register` mapping. It writes `relictest-result.txt` and stops the server.
