# Versions

**1.21.1 NeoForge** is the main version: every feature is made there first. The others are ports: 1.20.1 and 26.1.2 at 0.8.2, 26.2 and 26.3 at 0.8.3. A few
things are cut or work differently on some of them, and everything that is is listed here.

| Minecraft | Loader | KubeJS | Almanac (Patchouli) | Aerial Hell compat | What differs |
|---|---|---|---|---|---|
| **1.21.1** | NeoForge 21.1 | yes | yes | yes | nothing: the main version |
| 1.20.1 | Forge 47.4 | `event.custom` only | yes | yes | [a few small cuts](#1201-forge) |
| 26.1.2 | NeoForge 26.1.2 | yes | yes | yes | [the Ember Kiln's heat](#2612-neoforge) |
| 26.2 | NeoForge 26.2 | no build exists | no | no Aerial Hell build | [no Patchouli](#262-and-263-neoforge) |
| 26.3 | NeoForge 26.3 | no build exists | no | no Aerial Hell build | [no Patchouli](#262-and-263-neoforge) |

## 1.20.1 (Forge)

Everything is in except these, which 1.20.1 itself can't do:

- **The Scrape pottery sherd** isn't among the kiln gravel's finds (the sherd came in 1.21). The other finds are the
  same.
- **The flow and bolt armour trims** don't exist on 1.20.1, so they can't take the Slowlight Shard as a material. Every
  other trim pattern can.
- **The Keepsake Urn** plays the pot's place sound where 1.21 has a sound for putting something into a pot.
- **Gloamwood boats:** a dispenser drops them as items instead of placing them, and a boat smashed by a fall drops oak
  planks and sticks, as every modded boat does on 1.20.1.
- **KubeJS 6** has no recipe schemas, so `event.recipes.slowlight.ageing` doesn't exist; `event.custom` and
  `event.remove` work. Datapack recipes use 1.20.1's format: see [For pack makers](packs.md#on-other-versions).
- **Aerial Hell:** the Vine Blossom is pressable only if the installed Aerial Hell has it.

## 26.1.2 (NeoForge)

Nothing is cut. One thing behaves differently: the **Ember Kiln** works where water would evaporate (26.1 decides that
per biome, not per dimension). In vanilla that still means the Nether; a mod that adds a scorching biome elsewhere may
let it work there too.

## 26.2 and 26.3 (NeoForge)

Everything under 26.1.2 applies, and:

- **No Patchouli** exists for these versions, so there's no *A Slow Almanac* (its recipe doesn't show).
- **No KubeJS** build exists yet.
- **Aerial Hell** has no build for these versions, so its compat has nothing to load with (it's in the jar, ready for when it does).
- **Sulfur cube types** (0.8.3): these versions have the sulfur cube, and a cube that swallows a Slowlight Shard block
  drifts while one holding a Still Shard block hangs still. See [To build with](items.md#to-build-with).

## Testing

Every version's jar passes Slowlight's in-game self-test (a scripted week in a test world that checks every block,
recipe and wait), and KubeJS was tested for real on 1.20.1, 1.21.1 and 26.1.2.
