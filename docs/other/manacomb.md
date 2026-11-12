# Manacomb

![Manacomb logo](../assets/manacomb_logo.png){ width="128" align=right }

An addon for [Complicated Bees](https://www.curseforge.com/projects/1100137) that makes the same four FE machines
[Botania](https://www.curseforge.com/projects/225643) **mana** receivers. No new block. Its sister mod is
[Rotaflux](rotaflux.md), for Create rotation.

## How mana gets in

| Way | What it does |
|---|---|
| **Mana Spreader** | Aim it at the machine. A spreader stops firing at a full machine. |
| **Mana Spark** | Put it on top to draw from pool sparks of the same colour, like a Terrestrial Agglomeration Plate. |

**10 FE per mana** by default: a full 160-mana burst is 1600 FE, which runs a Centrifuge (20 FE/t) for 80 ticks.
Mana turns into FE as it arrives.

## Config

`serverconfig/manacomb-server.toml`:

| Key | Default | What it does |
|---|---|---|
| `rfInputDisabled` | `false` | The "Instead of RF" switch: `true` lets only mana in. With [Apiflux (now called Rotaflux)](rotaflux.md) installed, use its `apiflux-server.toml` switch instead; it covers both. |
| `manaEnabled` | `true` | Turns mana input on or off. |

The rate, and which machines take mana, are data maps a datapack can change.

## Compatibility

| Mod | What it does |
|---|---|
| [Complicated Bees](https://www.curseforge.com/projects/1100137) | Required, 3.6 or later. |
| [Botania](https://www.curseforge.com/projects/225643) | Required. |
| [Rotaflux](rotaflux.md) | Works side by side. |
| [Jade](https://www.curseforge.com/projects/324717) | Shows "Runs on mana: 1 mana = 10 FE" on a machine. |
| [JEI](https://www.curseforge.com/projects/238222) | An info page on the four machines. |

**Versions:** 0.1.0, NeoForge 1.21.1 (21.1.229 or later). [On CurseForge](https://www.curseforge.com/projects/1793766).

**Licence:** MIT.
