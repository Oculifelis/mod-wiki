# Apiflux

![Apiflux logo](../assets/apiflux_logo.png){ width="128" align=right }

An addon for [Complicated Bees](https://www.curseforge.com/projects/1100137) that lets its FE machines (the
Centrifuge, the Gyrofuge controller and energy cell, and the Mellarium energy cell) run on **Create rotation**.
Its sister mod is [Manacomb](manacomb.md), for Botania mana; the two work side by side.

## Blocks

| Picture | Name | What it does | How to get it |
|---|---|---|---|
|  | **Kinetic Dynamo**{ #kinetic-dynamo } | Put it against the machine and run a shaft into its collar. It gives FE out of its other five sides: **0.5 FE per tick for each RPM**, up to 256 FE/t, and draws **2 stress units per RPM**. It stores nothing, so a slow dynamo runs the machine part of the time: twice the speed is twice the work, up to the machine's full rate. Goggles show its stress and FE output. | Crafted: shaft on top, copper ingot on each side of an andesite casing, redstone below. |

## Config

`serverconfig/apiflux-server.toml`:

| Key | Default | What it does |
|---|---|---|
| `rfInputDisabled` | `false` | The "Instead of RF" switch: `true` makes the four machines refuse FE from every other source (Complicated Bees' generators and cables too); only [Kinetic Dynamos](#kinetic-dynamo), and [Manacomb](manacomb.md)'s mana if installed, get in. |
| `kineticEnabled` | | Turns the [Kinetic Dynamo](#kinetic-dynamo) on or off. |

Every rate is in a data map, so a datapack can change it.

## Compatibility

| Mod | What it does |
|---|---|
| [Complicated Bees](https://www.curseforge.com/projects/1100137) | Required, 3.6 or later. |
| [Create](https://www.curseforge.com/projects/328085) | Optional, 6.0.x: the [Kinetic Dynamo](#kinetic-dynamo). Without Create, only the RF switch does anything. |
| [Manacomb](manacomb.md) | Works side by side; Apiflux's switch covers both. |
| [Jade](https://www.curseforge.com/projects/324717) | Shows a line on a machine when outside FE is off. |
| [JEI](https://www.curseforge.com/projects/238222) | An info page on the [Kinetic Dynamo](#kinetic-dynamo). |

**Versions:** 0.1.0, NeoForge 1.21.1 (21.1.229 or later). [On CurseForge](https://www.curseforge.com/projects/1793756).

**Licence:** MIT.
