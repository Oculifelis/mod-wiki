# Biome slices

Fundamentum places biomes from data files into the overworld's and the Nether's climate map, with or without
TerraBlender. A slice either shares part of an existing biome's climate space (the host is split, not replaced) or
claims a climate box of its own. Mods ship slices in their jar; datapacks can add, override or switch them off.

## Files

`data/<namespace>/fundamentum/biome_slices/<name>.json`. The slice id is `<namespace>:<name>`. A datapack that ships a
file with the same id replaces it; `"enabled": false` in that file switches it off.

The biome itself is a normal datapack biome (`data/<namespace>/worldgen/biome/<name>.json`) with its tags
(`#minecraft:is_overworld`, `#minecraft:is_jungle`, `#c:is_cave` and so on); the slice only says where it goes.

```json
{
  "biome": "examplemod:jungle_ruins",
  "dimension": "minecraft:overworld",
  "share": { "with": ["minecraft:jungle", "#c:is_jungle"], "axis": "weirdness", "side": "high" },
  "weight": 0.25,
  "climate": { "temperature": [0.55, 1.0] },
  "requires": ["examplemod"],
  "toggle": "examplemod:jungle_ruins"
}
```

| Key | Default | Meaning |
|---|---|---|
| `biome` | required | The biome to place. A biome that isn't registered skips the slice. |
| `dimension` | `minecraft:overworld` | Any dimension whose generator uses a multi-noise biome source; `minecraft:the_nether` works. |
| `share.with` | | A biome id, a `#tag`, or a list of them: the hosts whose climate cells are split. |
| `share.axis` | `weirdness` (Nether: `humidity`) | The climate axis the host cell is cut along: `temperature`, `humidity`, `continentalness`, `erosion` or `weirdness` (not `depth`). |
| `share.side` | `high` | Which end of the host cell the slice takes: `high`, `low` or `middle`. |
| `share.band` | | `[min, max]` on that axis instead of `weight`: the slice takes exactly that band of each host cell. |
| `share.shift` | `0.15` (`0.2` is a good Nether value) | For hosts that are a single value on that axis (all Nether biomes are points): the slice becomes a neighbour point this far up or down the axis. |
| `climate` | | Axis to number or `[min, max]`, in vanilla's -2..2 units, any of the six axes including `depth`. With `share`, it narrows which part of the hosts is split. Without `share`, it is the slice's own box. |
| `placement` | `split` for `share`, and for a `climate` box without `depth` in the overworld; `add` otherwise | `split`: cut every biome cell inside the box and give the slice its share. `add`: put the box in as a new cell; overlapping cells that span it are carved around it, single-value cells (vanilla's surface and Nether points) are kept. Use `add` for caves (`depth` 0.2..0.9). |
| `weight` | `0.5` with `share`, else `1.0` | The fraction (above 0, at most 1) of each matched cell the slice takes along the axis. |
| `offset` | `0` | The climate point offset for `add` boxes, as in vanilla's parameter points. |
| `requires` | | Mod id or list of mod ids; if any is missing the slice is skipped. |
| `toggle` | | An id a mod can switch with `BiomeSlices.registerToggle(id, () -> config value)`. |
| `enabled` | `true` | `false` skips it (for datapacks overriding a mod's slice). |

Rules of thumb:

- A surface variant of a biome: `share` with the biome, `weirdness` high or low, weight 0.2 to 0.5. Vanilla surface cells
  are depth 0 and 1 only, so a share split never touches caves.
- A cave biome: a `climate` box with `depth` [0.2, 0.9] and `placement` `add` (the default for a box with depth).
- A Nether biome: `share` with a Nether biome on `humidity` or `temperature`; the slice becomes a neighbour point, so it
  takes part of that biome's area.
- Slices apply in id order; a later slice can share with an earlier slice's biome.

Surface rules (optional): `data/<namespace>/fundamentum/surface_rules/<name>.json`:

```json
{ "dimension": "minecraft:overworld", "requires": ["examplemod"], "rule": { "type": "minecraft:condition", "...": "..." } }
```

`rule` is a vanilla surface rule. All files for a dimension run, in id order, before the dimension's own rules. Guard
each with a `minecraft:biome` condition so it only touches your biome.

## In game

- `/fundamentum biomes slices` (operators): each slice with `+` (placed) or `-` (skipped) and why, then each dimension's
  path and climate point count, then the surface rule files.
- `config/fundamentum-biomes.toml`: `enabled` (all slices), `disabled_slices` (ids to leave out),
  `terrablender_region_weight` (10).
- The log has one `Biome slices:` line per skipped slice and per dimension.

## How it is placed

The merged list is built once per world load, at server start, before the levels exist. Nothing runs per biome lookup
except vanilla's own search over a longer list.

- **TerraBlender installed**: for the overworld and the Nether, the slices go into one region per dimension
  (`fundamentum:overworld`, `fundamentum:nether`, weight from the config): the vanilla preset's list with the slices
  merged in. TerraBlender blends it with its other regions (BOP, Regions Unexplored and so on), so the slices appear
  wherever our region is picked. TerraBlender picks surface rules by the namespace of the biome being surfaced, so the
  rule files go to it under the namespace of each active slice biome (and of each rule file). A namespace that already
  has TerraBlender rules from its own mod is left alone, with one log line, because TerraBlender keeps one rule set per
  namespace; such a mod adds its rules itself. Everything is
  called by reflection; Fundamentum doesn't depend on TerraBlender.
- **No TerraBlender**, or another dimension: the dimension's own parameter list (whatever the world preset or a
  datapack gave it) is merged with the slices and swapped in for vanilla's `parameters()` by a mixin; the source's
  possible biomes and the generator's feature steps are rebuilt. Surface rules are put in front of the dimension's
  noise settings' rule.
- **A non multi-noise biome source** (a custom terrain mod's own source, a flat or single-biome world): one log line,
  its slices are skipped and reported. Nothing crashes.

## Other worldgen mods

| Mod | What happens |
|---|---|
| Terralith (datapack overworld list) | No TerraBlender: the slices split Terralith's own list (its biomes can be hosts by id or tag). With TerraBlender: our region is vanilla plus slices, beside Terralith's. |
| Tectonic | Changes the noise router and terrain shape only; the source stays multi-noise, slices apply. |
| Biomes O' Plenty, Regions Unexplored | Need TerraBlender, so the TerraBlender path is used; our region is one more region among theirs. |
| Oh The Biomes We've Gone (1.20.1 only) | Uses TerraBlender there; same path. |
| Orbis Novus / Worldforge | Its overworld uses its own biome source: one log line, overworld slices skipped. Its Nether is vanilla multi-noise, so Nether slices apply. |

## Performance

Measured in the headless test world (see below). Vanilla searches its climate list with an R-tree; the merged list
has a few more points, so a lookup costs about the same. The list is built once per world load; lookups allocate
nothing new.

### Measured

Test world, seed 20261109, 250,000 random climate points x 4 passes (1M lookups) after a warm-up pass, two rounds,
on a desktop that was also running other builds, so a few percent either way is noise. The second round:

| What | Vanilla | With slices |
|---|---|---|
| Climate list lookup (`findValue`), own injector: 7593 points vs 8277 | 4510 ns | 4873 ns (+8%, from 9% more points) |
| Full biome sample (`getNoiseBiome`, noise + lookup), own injector | 14889 ns | 15789 ns (+6%) |
| Full biome sample, TerraBlender with our region beside vanilla's | 19957 ns | 19883 ns (same) |

An earlier run on a busier machine gave 5005 / 5722 ns for the lookup and had the full sample swing both ways by
about 20%, so treat the full-sample difference as within noise. Biomes are sampled once per 4x4x4 cell while a chunk
generates, so the extra lookup cost does not show in chunk generation time.

## Tests

- Unit tests: `gradlew test --tests com.fundamentum.biome.*` (box arithmetic and file parsing).
- World test: `gradlew runServer -Pbiometest` (own injector) and `-Pbiometest=tb` (with the held TerraBlender jar,
  `-Ptbjar=<path>` for another). Each makes a fresh world in `run-biometest*/`, loads the test slices in
  `src/biometest/resources`, finds each test biome with the game's biome search, generates the chunk and reads the
  biome back, checks the surface rule, runs the benchmark, writes `biometest-result.txt` and stops. Never build a jar
  with `-Pbiometest`.
