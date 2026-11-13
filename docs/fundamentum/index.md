# Fundamentum

![Fundamentum logo](../assets/fundamentum_logo.png){ width="128" align=right }

A library mod: it doesn't add much on its own. Mods built on it use it for the systems they share, so their items,
stats and events work together instead of each mod rolling its own. Nearly everything is set up through datapacks.

These pages cover **1.30.0**, submitted for all five targets on November 13. See [Versions](versions.md) for the documented builds and the download link. The [shared systems guide](systems.md) covers stats, survival meters, multiblocks and the other additions.

**Requires:** [Curios](https://www.curseforge.com/projects/309927). **Optional:** [JEI](https://modrinth.com/mod/jei), REI and EMI show shared recipe pages where a matching viewer build exists.

JEI and REI are supported on 26.x; EMI support is on 1.21.1 and 1.20.1. [Portal crafting](datapack/portal-crafting.md) uses the shared recipe pages.

## Mods that use Fundamentum

??? note "Mods that require Fundamentum (3)"

    | Mod | What it builds on |
    |---|---|
    | [Ostentum](../ostentum/index.md) | Weapons, relics and summons built on Fundamentum's [wings](datapack/wings.md), [mounts](datapack/mounts.md), [hooks](datapack/hooks.md), [summons](datapack/summons.md) and [whips](datapack/whips.md). |
    | [Flora Ferox](../floraferox/index.md) | Plant monsters, with wings, grappling hooks and whips for each family built on Fundamentum's (see [Built on Fundamentum](../floraferox/index.md#built-on-fundamentum)). |

    | [Fieldframe Transit](../fieldframe-transit/index.md#built-on-fundamentum) | Curved transit tubes built on the shared curve code. |

??? note "Mods with optional Fundamentum support"

    | Mod | What it uses |
    |---|---|
    | [Arcana Varia](../arcanavaria/index.md#built-on-fundamentum) | Four cord whips and four scythe tuning files. |
    | [Fieldframe](../fieldframe/index.md#built-on-fundamentum) | The Graviton Hook and powered whips on NeoForge 26.1.2 and 1.21.1. |

## For players

| Feature | What it does |
|---|---|
| **[Wings](datapack/wings.md)** | In their own Curios slot (with a cosmetic twin). Hold jump to fly, then glide. No fall damage while flying. |
| **[Mounts](datapack/mounts.md)** | A mount item in the `mount` slot plus **V** calls a creature to ride. V again, getting off, unequipping, dying or changing dimension puts it away. |
| **[Grappling hooks](datapack/hooks.md)** | A hook in the `hook` slot plus **H** fires it. It latches onto a block and pulls you there; jump to let go. A latched player takes no fall damage. |
| **[Summons](datapack/summons.md)** | Items in the `summon` slot call minions that follow you and fight what you fight. |
| **[Whips](datapack/whips.md)** | A simulated cord: the whole cord hits, the tip hits hardest, and a crack at the tip is a crit. |
| **Cosmetic armour** | Four slots in their own screen (the button at the top right of the inventory's player preview). |
| **3D arrows** | In place of the flat vanilla ones. |
| **[Special moons](datapack/moons.md) and [night events](datapack/night-events.md)** | Tint the fog and sky, with their own spawns, effects, loot and messages. |
| **[Fractal skies](datapack/fractal-skies.md)** | A moon, event or dimension can draw a fractal sky with an optional melting-vision effect. |
| **[Elements](datapack/elements.md)** | Hits can be fire, ice, water, electric, earth, air, poison, holy, shadow or arcane, leave auras and set off reactions. A datapack can [add new elements](datapack/elements.md#new-elements) with no code. |
| **[Portal crafting](datapack/portal-crafting.md)** | Some items change when thrown through a portal. |
| **[Use sickness](datapack/sickness.md)** | For potions and other consumables. |
| **Tooltips** | For whips and hooks; any item's `.desc` lang lines show under its name. |
| **Max health** | Up to 1,000,000 instead of 1,024. |

## Keys

| Key | Default | Does |
|---|---|---|
| Mount | V | calls or dismisses the [mount](datapack/mounts.md) in the `mount` slot |
| Hook | H | fires a [hook](datapack/hooks.md) from the `hook` slot |

Both are in the Fundamentum key category.

## Config

| File | Option | Default | Meaning |
|---|---|---|---|
| `config/fundamentum-client.toml` | `whips.flatHandles` | false | flat whip handles in hand instead of 3D ones |
| `config/fundamentum-client.toml` | `tooltips.shiftForDetails` | true | item descriptions and stats fold behind "Hold [Shift] for details"; false always shows them |
| `config/fundamentum-sky-client.toml` | `sky.fractalSkies` | true | draw fractal skies |
| `config/fundamentum-sky-client.toml` | `sky.melt` | true | the melting-vision effect |
| `config/fundamentum-sky-client.toml` | `sky.meltIntensity` | 0.5 | 0 to 1 |
| `config/fundamentum-hud-client.toml` | `itemHud.enabled` | true | the item HUD: a few lines beside the hotbar for held items that have one, like [Ostentum](../ostentum/index.md)'s [Engineer's Crossbow](../ostentum/items.md#engineers-crossbow) |
| | `itemHud.anchor`, `itemHud.x`, `itemHud.y` | HOTBAR_RIGHT, 0, 0 | where it sits (beside the hotbar, a corner or an edge) and the offset in GUI pixels |
| | `itemHud.scale` | 1.0 | 0.25 to 4; 1 is the game's own text |
| | `itemHud.textColor`, `itemHud.textOpacity`, `itemHud.shadow` | #FFFFFF, 1.0, true | text that doesn't set its own colour |
| | `itemHud.background`, `itemHud.backgroundOpacity` | false, 0.35 | a dark backdrop, as chat and subtitles have |
| `config/fundamentum-common.toml` | `moons.psychedelicMoon` | false | lets the Psychedelic Moon roll (3% of nights, never a full moon) |

## Compatibility

[Architect's Palette](https://www.curseforge.com/projects/433862) warping recipes keep priority over Fundamentum's portal crafting. Optional.

| Mod | What Fundamentum adds | Needed? |
|---|---|---|
| [Jade](https://modrinth.com/mod/jade) | looking at a playing jukebox shows the disc, a progress bar and "1:12 / 3:05"; works for every disc, modded ones too; toggle it in Jade's plugin settings ("Jukebox song progress") | optional |
| [JEI](https://modrinth.com/mod/jei) | [portal crafting](datapack/portal-crafting.md) recipes | optional |

Item tooltips: other mods' lines added through Fundamentum fold behind Shift too. Tag items `#fundamentum:tooltip_always`
to keep their text open, or `#fundamentum:tooltip_fold` to fold a short one.

## Shaders

With [Iris](https://www.curseforge.com/projects/455508) and a shader pack, moon and night-event sky tints, whip cords and glowing item faces still show (26.1.2,
from 1.25.4). The Psychedelic Moon's fractal sky doesn't show under packs that draw their own sky, such as Complementary.

## Licence

By **Oculifelis**. From 1.25.8, Fundamentum's code and art are open source under the
[GNU LGPL 3.0 or later](https://www.gnu.org/licenses/lgpl-3.0.html): a mod or pack may depend on it, ship it and build on
it. Versions before 1.25.8 were All Rights Reserved. The cord whip system is adapted from
[Better Whips](https://github.com/my2167592261-cell/Better-Whips) (MIT); every texture is Fundamentum's own.

## Pages

| Page | What it covers |
|---|---|
| [Versions](versions.md) | What each Minecraft version has. |
| [Datapacks](datapack/index.md) | Every JSON format, with examples. |
| [KubeJS](kubejs.md) | Scripting Fundamentum's data with KubeJS. |
| [API](api.md) | For mod makers. |
| [Commands](commands.md) | The commands. |
