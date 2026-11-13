# Ostentum

![Ostentum logo](../assets/ostentum_logo.png){ width="140" align=right }

A vanilla expansion built on [Fundamentum](../fundamentum/index.md): summoning saddles for vanilla mounts, grappling
hooks, summon charms, whips, special weapons with a trick each, three special moons, a Pillager Siege night and boss
relics.

Most of Ostentum is Fundamentum data. The mounts, hooks, summons, whips, moons, siege, elemental damage and portal
crafting all run on Fundamentum; Ostentum adds the items, creatures, art, music and recipes that use them.

**Requires** [Fundamentum](../fundamentum/index.md) and [Curios](https://www.curseforge.com/projects/309927). **Optional:** [Patchouli](https://www.curseforge.com/projects/306770), for a guide book (crafted from a book and a saddle), and
[JEI](https://www.curseforge.com/projects/238222) to see the recipes.

| Minecraft | Loader | Latest built |
|---|---|---|
| 26.1.2 | NeoForge | 1.9.10 |
| 26.2 | NeoForge | 1.9.10 |
| 26.3 | NeoForge | 1.9.10 |
| 1.21.1 | NeoForge | 1.9.10 |
| 1.20.1 | Forge | 1.9.10 |

The happy ghast harness and the nautilus saddle are on 26.x. The Forge 1.20.1 build needs Fundamentum 1.25.8 or newer and Curios 5.14.1 or newer. The [Pathfinder's Glaive](items.md#pathfinders-glaive) waypoint uses a gold and orange light column in 1.9.9.

In 1.9.10, the [Echo Blade](items.md#echo-blade) has an animated blade, the [Duelist’s Saber](items.md#duelists-saber) has its guard pose, and the Delver’s Shovel crafting recipes are included.

[CurseForge project](https://www.curseforge.com/projects/1786639)

## Built on Fundamentum

The [items guide](items.md) has the stats for Ostentum's saddles, hooks, summons, whips and special weapons.

| Override | Path under <code>data/ostentum/</code> | Format |
|---|---|---|
| Mounts | <code>fundamentum/mounts/</code> | [Mounts](../fundamentum/datapack/mounts.md) |
| Hooks | <code>fundamentum/hooks/</code> | [Hooks](../fundamentum/datapack/hooks.md) |
| Summons | <code>fundamentum/summons/</code> | [Summons](../fundamentum/datapack/summons.md) |
| Whips | <code>fundamentum/whips/&lt;name&gt;.json</code> keyed by item ID | [Whips](../fundamentum/datapack/whips.md) |
| Moons | <code>fundamentum/moons/</code> | [Moons](../fundamentum/datapack/moons.md) |
| Pillager Siege | <code>fundamentum/night_events/</code> | [Night events](../fundamentum/datapack/night-events.md) |
| Portal crafting | <code>recipe/</code> (<code>recipes/</code> on Forge 1.20.1) with type <code>fundamentum:portal_crafting</code> | [Portal crafting](../fundamentum/datapack/portal-crafting.md) |

## What's in it

| Picture | Section | What's in it |
|---|---|---|
| ![Summoning saddle](img/horse_saddle.png){ .mc-icon } | **[Summoning saddles](items.md#summoning-saddles)** | saddles for twelve vanilla mounts, in the Curios mount slot |
| ![Stillwind Hook](img/stillwind_hook.png){ .mc-icon } | **[Grappling hooks](items.md#grappling-hooks)** | from amethyst to the [Stillwind Hook](items.md#stillwind-hook) |
| ![Bottled Dragonling](img/bottled_dragonling.png){ .mc-icon } | **[Summons](items.md#summons)** | wolves, a baby iron golem, a chibi ender dragon, a flying pink dolphin and more |
| ![Leather Whip](img/leather_whip.png){ .mc-icon } | **[Whips](items.md#whips)** | real cord whips, from the [Leather Whip](items.md#leather-whip) to the [Destruction Whip](items.md#destruction-whip) |
| ![Echo Blade](img/echo_blade.png){ .mc-icon } | **[Special weapons](items.md#special-weapons)** | each with one trick of its own |
| ![Harvest Moon disc](img/music_disc_harvest_moon.png){ .mc-icon } | **[Moons and the siege](items.md#moons-and-the-siege)** | the Harvest, Enchanted and Glimmer Moons, and the Pillager Siege, each with its own music track and disc |
| ![Record Pendant](img/record_pendant.png){ .mc-icon } | **[Records](items.md#records)** | [record shelves](items.md#record-shelf), and the Record Pendant, which shows what the nearest jukebox is playing |
| ![Wither relic](img/wither_relic.png){ .mc-icon } | **[Boss relics](items.md#boss-relics)** | a gold likeness of each boss on a pedestal |

### Small changes

| Change | What it does |
|---|---|
| Pickaxes on golems | pickaxes hit iron, snow and copper golems for 1.5x |
| Enchanted golden apple | gives a minute of use sickness |
| Elemental hits | Fire Aspect weapons hit as fire, snowballs as ice and tridents as water |
| Netherite armour | resists a little fire per piece |

## Credits

By Oculifelis: code, design, music and the hand-drawn art.

| By | Work | Licence | Used for |
|---|---|---|---|
| Malcolm Riley | [Unused Textures](https://github.com/malcolmriley/unused-textures) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | the base of the [Duelist's Saber](items.md#duelists-saber), the Hearthblades, the [Echo Blade](items.md#echo-blade) and the Resonant Hilt (recoloured and redrawn) |
| Rhodox | Painterly | used with permission | the [Delver's Pick](items.md#delvers-pick) head |
| Mojang | Minecraft | Mojang keeps its rights | many item and creature textures, recoloured or reworked |

From 1.9.8, Ostentum's code and Oculifelis's own art and music are open source under the
[GNU LGPL 3.0 or later](https://www.gnu.org/licenses/lgpl-3.0.html). Art from others keeps its own licence: the
Unused Textures art stays CC BY 4.0, the Painterly art is used by permission and isn't covered, and Mojang keeps its
rights to art reworked from Minecraft. Versions before 1.9.8 were All Rights Reserved.

## Compatibility

Works with [Better Combat](https://www.curseforge.com/projects/639842) (optional) on 1.20.1, 1.21.1, 26.1.2, 26.2 and 26.3.

Works with [Jade](https://www.curseforge.com/projects/324717) (optional) on 1.20.1, 1.21.1, 26.1.2, 26.2 and 26.3.
