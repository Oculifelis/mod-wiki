# Datapacks

Almost everything in Fundamentum is data. Every format here is read from `data/<namespace>/fundamentum/<folder>/`,
where `<namespace>` is any namespace (your pack's or mod's own), and loads on world load and on `/reload`.

| Folder | What it defines | Keyed by |
|---|---|---|
| `fundamentum/wings/` | [wing stats](wings.md) | `item` |
| `fundamentum/mounts/` | [mount items](mounts.md) | `item` |
| `fundamentum/hooks/` | [grappling hooks](hooks.md) | `item` |
| `fundamentum/summons/` | [summon items](summons.md) | `item` |
| `fundamentum/whips/` | [whip tuning](whips.md) | `item` |
| `fundamentum/moons/` | [special moons](moons.md) | file id |
| `fundamentum/night_events/` | [night events](night-events.md) | file id |
| `fundamentum/fractal_skies/` | [fractal skies](fractal-skies.md) | file id |
| `fundamentum/element_reaction/` | [element reactions](elements.md) | file id |
| `fundamentum/creature_damage/` | [creature damage rules](creatures.md) | file id |
| `fundamentum/sickness/` | [use sickness rules](sickness.md) | file id |
| `recipe/` | [portal crafting recipes](portal-crafting.md) | recipe id |

Data maps (`data/<ns>/data_maps/...`) hold [element auras and affinities](elements.md); tags hold
[creature types, elements, damage classes and slot items](tags.md). [Player poses](poses.md) are resource pack files.

## How files merge

Files are read in file-id order and merged over each other, field by field: a later file only needs the fields it
changes, and a field set to `null` is removed. For the formats keyed by `item`, the file's `item` field says which item
it is for; without one, the file's id is used (so `data/mymod/fundamentum/wings/angel_wings.json` is for
`mymod:angel_wings`).

So to retune something another mod ships, write a file with the same key and only the fields you change. For example,
Ostentum's pig saddle is `data/ostentum/fundamentum/mounts/pig.json`; a pack can slow it further with:

```json
{"item": "ostentum:pig_saddle", "speed": 0.1}
```
