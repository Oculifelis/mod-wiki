# Manaflux

![Manaflux logo](../assets/manaflux_logo.png){ width="128" align=right }

Run any FE machine on [Botania](https://www.curseforge.com/projects/225643) mana. Aim a spreader at the machine, or put a spark on it, and the mana arrives as FE. There is no separate converter block. This 0.2.0 release was previously called Manacomb.

Real Botania blocks keep their own behavior. Blocks that only produce FE are left alone.

## Getting mana into a machine

| Method | What to do |
|---|---|
| Mana Spreader | Bind it to the machine with the Wand of the Forest. It stops firing when the machine is full. |
| Mana Spark | Put a spark on the machine to draw from pool sparks of the same color in range. |

The default rate is **10 FE per mana**. A full 160-mana spreader burst supplies 1,600 FE. Mana converts as it arrives; the machine does not store mana. A burst larger than the remaining FE space loses its excess.

## Config

The per-world file is <code>serverconfig/manaflux-server.toml</code>.

| Key | Default | Meaning |
|---|---|---|
| <code>manaEnabled</code> | <code>true</code> | Enable mana receivers. |
| <code>anyFeBlock</code> | <code>true</code> | Let any FE input block receive mana. When false, only blocks listed in the data map do. |
| <code>defaultFePerMana</code> | <code>10.0</code> | FE per mana for blocks without an individual rate. |
| <code>rfInputDisabled</code> | <code>false</code> | With Complicated Bees installed, refuse outside FE for its four powered machines. |

A datapack can set per-block rates with the <code>manaflux:mana_input</code> data map. The <code>manaflux:no_mana</code> tag excludes blocks from mana input.

## Compatibility

| Mod | What it does |
|---|---|
| [Botania](https://www.curseforge.com/projects/225643) | Required. It supplies mana, spreaders and sparks. |
| [Complicated Bees](https://www.curseforge.com/projects/1100137) | Optional. Its powered machines receive mana like other FE inputs, with the extra outside-FE switch above. |
| [Rotaflux](rotaflux.md) | Its outside-FE switch takes precedence when both mods are installed. Mana and kinetic input remain available. |
| [Jade](https://www.curseforge.com/projects/324717) | Optional. Shows the mana input rate and whether outside FE is disabled. |
| [JEI](https://www.curseforge.com/projects/238222) | Optional. Adds information for the Complicated Bees machines when that mod is installed. |

**Documented build:** 0.2.0 on NeoForge 1.21.1, requiring NeoForge 21.1.229 or newer. The mod id is <code>manaflux</code>. [CurseForge project](https://www.curseforge.com/projects/1793766).

By Oculifelis, under MIT.
