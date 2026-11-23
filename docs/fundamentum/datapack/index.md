# Datapacks

Almost everything in Fundamentum is data. Every format here is read from `data/<namespace>/fundamentum/<folder>/`,
where `<namespace>` is any namespace (usually the pack's or mod's own), and loads on world load and on `/reload`.

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
| `fundamentum/dodge_style/` | [dodge styles](dodge.md) | file id |
| `fundamentum/dodge_gear/` | [dodge gear](dodge.md#dodge-gear) | `item` |
| `fundamentum/item_weights/`, `fundamentum/weight_rules/` | [weight](weight.md) | file id |
| `fundamentum/boss_bags/` | [boss bags](boss-bags.md) | file id |
| `fundamentum/factions/`, `fundamentum/alignments/` | [factions and gods](factions.md) | file id |
| `fundamentum/quests/`, `fundamentum/npcs/` | [quests and quest NPCs](quests.md) | file id |
| `fundamentum/pantheons/`, `fundamentum/shrines/`, `fundamentum/rituals/` | [pantheons, shrines and rituals](gods.md) | file id |
| `recipe/` | [portal crafting recipes](portal-crafting.md) | recipe id |

Data maps (`data/<ns>/data_maps/...`) hold [element auras and affinities](elements.md); tags hold
[creature types, elements, damage classes and slot items](tags.md). Resource packs hold [quest screens](quests.md#quest-screens), [player poses](poses.md) and
[guide books, book styles, guide themes and the bestiary](books.md).

## How files merge

Files are read in file-id order and merged over each other, field by field: a later file only needs the fields it
changes, and a field set to `null` is removed. For the formats keyed by `item`, the file's `item` field says which item
it is for; without one, the file's id is used (so `data/mymod/fundamentum/wings/angel_wings.json` is for
`mymod:angel_wings`).

So a pack retunes something another mod ships with a file of the same key that holds only the changed fields. For
example, Ostentum's pig saddle is `data/ostentum/fundamentum/mounts/pig.json`. This file slows it further:

```json
{"item": "ostentum:pig_saddle", "speed": 0.1}
```

Dodge styles, dodge gear and weight rules are the exception. A later file with the same id replaces the earlier one
whole, so it holds every field it keeps.
