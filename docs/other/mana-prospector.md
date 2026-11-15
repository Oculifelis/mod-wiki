# Mana Prospector

![Mana Prospector logo](../assets/manaprospector_logo.png){ width="128" align=right }

Mana Prospector adds two ore prospectors for packs that have both GregTech and Botania. They open GregTech's own prospecting map, the same screen as the GT prospector, but they run on Botania mana instead of EU. There are no batteries to charge, and a full mana tablet holds 250 manasteel scans.

Recipes are datapack JSON, and the scan radius and mana cost of each prospector are in the server config.

![The manasteel and terrasteel prospectors](img/manaprospector_prospectors.png)

## The prospectors

| Prospector | Area | Mana per scan | Modes |
|---|---|---|---|
| Manasteel Prospector | 5x5 chunks, like GT's LV prospector | 2,000 | ores |
| Terrasteel Prospector | 9x9 chunks | 8,000 | ores, underground fluids, bedrock ores (when GregTech has them on) |

Sneak and use the terrasteel one to switch modes. Mana comes out of any mana item in your inventory, the same way Botania's rods draw it. A scan is paid once, when the map opens, so you can keep the map up as long as you like.

You craft the manasteel one from manasteel ingots, a mana pearl, an LV circuit, an LV emitter and an LV sensor. The terrasteel one takes the manasteel prospector, terrasteel ingots, a mana diamond, an HV circuit, an HV emitter and an HV sensor.

## Versions and requirements

| Minecraft | Loader | Version | Needs |
|---|---|---|---|
| 1.20.1 | Forge | 0.1.1 | [GregTech CEu Modern](https://www.curseforge.com/projects/890405) 7.5.2 or newer 7.5 releases, [Botania](https://www.curseforge.com/projects/225643) |
| 1.21.1 | NeoForge | 0.1.0 | [GregTech CEu Modern](https://www.curseforge.com/projects/890405) 7.0.2 or newer, [Botania](https://www.curseforge.com/projects/225643) 1.21.1 |

[CurseForge project](https://www.curseforge.com/projects/1804192)

## For pack makers

The scan radius and mana cost of both prospectors are in the server config, manaprospector-server.toml, and you can change them while the server runs. Recipes are plain crafting recipes at manaprospector:manasteel_prospector and manaprospector:terrasteel_prospector, so a datapack can replace them. KubeJS scripts can edit them too.

| Key | Default | Range | What it changes |
| --- | --- | --- | --- |
| `manasteel.radius` | 2 | 1-8 | Chunks scanned out from the player's chunk (5x5 map). |
| `manasteel.manaPerScan` | 2000 | 0-1,000,000 | Mana drawn each time the map opens. 0 makes it free. |
| `terrasteel.radius` | 4 | 1-8 | Chunks scanned out from the player's chunk (9x9 map). |
| `terrasteel.manaPerScan` | 8000 | 0-1,000,000 | Mana drawn each time the map opens. |

## Credits and license

By Oculifelis, MIT. The item textures are GregTech's portable scanner recolored to Botania's metals (LGPL-3.0, from GregTech CEu Modern).
