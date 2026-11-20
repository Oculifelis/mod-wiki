# Fieldframe Frameworks

![Fieldframe Frameworks logo](../assets/fieldframe_frameworks_logo.png){ width="128" align=right }

![Fieldframe Frameworks](img/banner.png)

*Big multiblock machines for Fieldframe.*

Frameworks is an addon for [Fieldframe](../fieldframe/index.md) that adds big multiblock machines. A frame built out
of casing blocks, with a core in its wall, runs as one machine. Fieldframe modules go on its walls
and drive it, the same way they drive a single chassis. Still no pipes and no cables.

![Frame Casing, Frame Core, Vault, Tank, Cell, Crucible, Arc Electrode and Cooling Fin; Gantry Controller, Head and Rail, Containment Coil, Field Magnet, Plasma Injector and Plasma Probe](img/blocks.png)

Frameworks requires [Fieldframe](../fieldframe/index.md) 0.3.7 or newer, [Fundamentum](https://www.curseforge.com/projects/1765941) and [Metallurgy: Recast](../metallurgy/index.md). It works with [JEI](https://www.curseforge.com/projects/238222),
[Jade](https://www.curseforge.com/projects/324717), [KubeJS](https://www.curseforge.com/projects/238086) when they are installed.

Frameworks is data-driven. Frame sizes, power costs, alloy recipes and reactor values are datapack files; see the table further down.

Frameworks 0.1.7 runs on NeoForge 26.3, 26.2, 26.1.2 and 1.21.1 and on Forge 1.20.1. See [Versions](../fieldframe/versions.md) and the [CurseForge project](https://www.curseforge.com/projects/1794653).

## The Grand Frame

A hollow box of ![Frame Casing](img/frame_casing.png){ .mc-icon .mc-inline } **Frame Casing**, anywhere from 5 to 9 blocks a side, with a ![Frame Core](img/frame_core.png){ .mc-icon .mc-inline } **Frame Core** in the shell. Every wall
casing can take a Fieldframe module, and all of them share one machine. ![Frame Vaults](img/frame_vault.png){ .mc-icon .mc-inline } **Frame Vaults**, ![Frame Tanks](img/frame_tank.png){ .mc-icon .mc-inline } **Frame Tanks** and ![Frame Cells](img/frame_cell.png){ .mc-icon .mc-inline } **Frame Cells**
inside add room for items, fluids and power. Every frame shows its state on its core, and the Engineering Field
Manual has pages for all of them.

![JEI's Frame Core page](img/04-jei-frame-core.png)

## Foundry

Put ![Frame Crucibles](img/frame_crucible.png){ .mc-icon .mc-inline } **Frame Crucibles** inside a frame and it turns into a Foundry. They melt metals into one pool, mix them into alloys
and pour the result into a tank.

![JEI's Foundry alloys page](img/03-jei-foundry-alloys.png)

## Arc Furnace

![Arc Electrodes](img/arc_electrode.png){ .mc-icon .mc-inline } **Arc Electrodes** make the frame an Arc Furnace instead. Every second each electrode fires a burst of 40,000 RF that
smelts up to 16 items, and it makes steel, damascus steel, hepatizon and tartarite. A Storm Coil on the roof charges it
from lightning: 200,000 RF a strike.

## Cooling Tower

![Cooling Fins](img/cooling_fin.png){ .mc-icon .mc-inline } **Cooling Fins** turn the frame's steam back into water, so the water goes round again and a steam loop closes.

## Gantry

A ![Gantry Controller](img/gantry_controller.png){ .mc-icon .mc-inline } **Gantry Controller** sits in a ring of ![Gantry Rails](img/gantry_rail.png){ .mc-icon .mc-inline } **Gantry Rails**, from 3 up to 64 blocks a side, and moves a ![Gantry Head](img/gantry_head.png){ .mc-icon .mc-inline } **Gantry Head**
over the whole area. The module on the head decides the job: a Block Breaker quarries, a Crop Tender farms, a World
Fluid Pump pumps.

## Starcore

The Starcore is a fusion reactor inside ![Containment Coils](img/starcore_coil.png){ .mc-icon .mc-inline } **Containment Coils**. Its plasma never settles on its own. A control
circuit has to hold it, and if the program lets it drift, it goes out. Lighting it takes 5,000,000 RF.

| Picture | Part | What it does |
|---|---|---|
| ![Field Magnet](img/field_magnet.png){ .mc-icon } | **Field Magnet**{ #field-magnet } | 2 field per signal level, at 40 RF/t per level. A coil holds 60. |
| ![Plasma Injector](img/plasma_injector.png){ .mc-icon } | **Plasma Injector**{ #plasma-injector } | feeds deuterium, up to 1 mB a tick, and one Ender Alloy dust per 250 mB. |
| ![Plasma Probe](img/plasma_probe.png){ .mc-icon } | **Plasma Probe**{ #plasma-probe } | reports pressure (0 to 15) and temperature (20 MK a level) as signals. |

Deuterium comes from Fieldframe's [Centrifuge](../fieldframe/modules.md#centrifuge): 1,000 mB of water makes 100 mB. Reactor explosions are a server setting
in `fieldframe_frameworks-server.toml`, off by default.

## For pack makers

Frameworks is built only on Fieldframe's public API. Every number is data:

| To change | Where (`data/<pack>/...`) |
|---|---|
| Frame tuning | `fieldframe_frameworks/tuning/*.json` |
| Frame components | `fieldframe/frame_components/*.json` |
| Foundry alloys | `fieldframe_frameworks/alloys/*.json` |
| Arc Furnace alloys | `fieldframe_frameworks/arc_alloys/*.json` |
| Starcore fuel (fluids a Plasma Injector burns, default deuterium) | fluid tag `fieldframe_frameworks:starcore_fuel` |
| Starcore dust (used up with the fuel, default Ender Alloy dust) | item tag `fieldframe_frameworks:starcore_fuel_dust` |

KubeJS and Java addons can change the same values ([Fieldframe for pack makers](../fieldframe/pack-makers.md)).

## Credits

By **Oculifelis**.

The licence is LGPL-3.0-or-later.
