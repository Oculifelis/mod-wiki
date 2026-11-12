# Rotaflux

![Rotaflux logo](../assets/rotaflux_logo.png){ width="128" align=right }

One [Create](https://www.curseforge.com/projects/328085) block that turns shaft rotation into FE for any block that
takes FE: machines, batteries, cables, from any mod. The public **0.1.0** download is named **Apiflux** and requires
[Complicated Bees](https://www.curseforge.com/projects/1100137). Its switch can make those machines accept only rotation and mana.
Its sister mod is [Manacomb](manacomb.md), for Botania mana; the two work side by side.

## Blocks

| Picture | Name | What it does | How to get it |
|---|---|---|---|
|  | **Kinetic Dynamo**{ #kinetic-dynamo } | Run a shaft into its collar on top. It gives FE out of its other five sides, shared between them: **0.5 FE per tick for each RPM**, up to 256 FE/t, and draws **2 stress units per RPM**. It stores nothing, so a slow dynamo runs a machine part of the time. Goggles show its stress and FE output. | Crafted: shaft on top, copper ingot on each side of an andesite casing, redstone below. |

## Config

`serverconfig/apiflux-server.toml`:

| Key | Default | What it does |
|---|---|---|
| `kineticEnabled` | `true` | Turns the [Kinetic Dynamo](#kinetic-dynamo)'s output on or off. |
| `rfInputDisabled` | `false` | `true` makes its Centrifuge, Gyrofuge and Mellarium refuse FE from every other source (Complicated Bees' generators and cables too); only [Kinetic Dynamos](#kinetic-dynamo), and [Manacomb](manacomb.md)'s mana if installed, get in. |

Every rate is in the data map `data/apiflux/data_maps/block/kinetic_dynamo.json` (`fe_per_rpm`, `max_fe_per_tick`,
`stress_impact`, `min_rpm`), so a datapack can change it.

## Compatibility

| Mod | What it does |
|---|---|
| [Create](https://www.curseforge.com/projects/328085) | Optional, 6.0.6 or later (not 6.1): adds the Kinetic Dynamo. Without Create, the RF switch is still available. |
| [Complicated Bees](https://www.curseforge.com/projects/1100137) | Required by the public 0.1.0 jar. |
| [Manacomb](manacomb.md) | Works side by side; Rotaflux's switch covers both. |
| [Jade](https://www.curseforge.com/projects/324717) | Shows a line on a Complicated Bees machine when outside FE is off. |
| [JEI](https://www.curseforge.com/projects/238222) | An info page on the [Kinetic Dynamo](#kinetic-dynamo). |

**Versions:** 0.1.0 (Apiflux), NeoForge 1.21.1 (21.1.229 or later). The released mod id is `apiflux`. [On CurseForge](https://www.curseforge.com/projects/1793756).

**Licence:** MIT.
