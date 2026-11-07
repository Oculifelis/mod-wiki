# Orbis Novus: Terrain

![Orbis Novus: Terrain](img/terrain_logo.png){ width="128" align=right }

Realistic mountains, eroded valleys and river networks. Valleys are worn down by erosion and rivers run in networks
down to the sea.

The terrain comes from the game's own noise generator, driven by the mod's density functions. That keeps vanilla
caves, aquifers, ore veins, biome features and other mods' structures and features working. The Nether and the End
stay vanilla. Every world is infinite and seeded, so one seed always makes the same world. Chunks generate at close
to vanilla's speed: 28 to 33 ms each in testing, against vanilla's 27.

## Making a world

On the Create World screen, use the **World Type** button to pick **Orbis Novus**. It starts as Patchwork Earth.
**Customize** opens the settings screen, laid out like the old Customized world screen:

![The Customize screen](img/terrain_customize.jpg)

- **Style:** one of the ten below, or **Custom Mix**.
- **Basic:** sea level, base height, height variation and hill size.
- **Mountains & Erosion:** detail, peak sharpness, ridges, twist, erosion, slope limit, terraces and the snow line.
- **Water:** rivers, how many lakes, and islands.
- **Mix:** how much of each style Patchwork Earth or Custom Mix uses, and how big the regions are.
- **Advanced:** basins, craters, spires, and floating islands with their heights.
- **Features:** grass, flowers and trees; ores; lava and water pools; structures. All are on by default.
- **Presets:** every style, plus Sky Teeth, Flatlands, Drowned World, Lake District, Endless Canyons, Shattered
  Shards, Sky Archipelago and Crater Sea.
- **Randomize**, **Copy** and **Paste** (the settings as JSON), **Defaults**, **Done** and **Cancel**.

The settings are saved with the world.

## The styles

<div class="grid cards" markdown>

- ![Green Vale](img/shots/terrain-green_vale.jpg)

    **Green Vale**: rolling green hills with oak woods and rivers.

- ![High Teeth](img/shots/terrain-high_teeth.jpg)

    **High Teeth**: snowy alpine peaks over pine valleys.

- ![Far Spires](img/shots/terrain-far_spires.jpg)

    **Far Spires**: towering amplified spires and gorges.

- ![Skyreach](img/shots/terrain-skyreach.jpg)

    **Skyreach**: grassy islands floating over a shallow sea.

- ![Red Steps](img/shots/terrain-red_steps.jpg)

    **Red Steps**: terraced badlands canyons.

- ![Warm Shoals](img/shots/terrain-warm_shoals.jpg)

    **Warm Shoals**: jungle islands in a warm shallow sea.

- ![Verdigris Reach](img/shots/terrain-verdigris_reach.jpg)

    **Verdigris Reach**: a teal fungal alien world under needle spires.

- ![Grey Silence](img/shots/terrain-grey_silence.jpg)

    **Grey Silence**: a dead grey moon covered in craters.

- ![Painted Stillness](img/shots/terrain-painted_stillness.jpg)

    **Painted Stillness**: flat pastel-banded columns, like a sculpture field.

- ![Patchwork Earth](img/shots/terrain-patchwork_earth.jpg)

    **Patchwork Earth**: rolling hills, alpine peaks, mesa steps and island seas, region by region. The default.

- ![Custom Mix](img/shots/terrain-custom_mix.jpg)

    **Custom Mix**: any of the nine styles above (but Patchwork Earth) region by region, weighed on the Mix page.

</div>

![Patchwork Earth from above, 256 blocks across](img/terrain_patchwork_earth_map.jpg)

### Custom Mix

![The Mix page](img/terrain_custom_mix.jpg)

**Custom Mix** sets the single styles side by side, region by region. The Mix page has a slider from 0 to 5 for each
style, plus one for region size.

Each region keeps its own style's land, biomes and ground. A Grey Silence region is grey moon dust even right next to
Green Vale, and at the border the ground speckles from one to the other. Dry styles keep clear of a neighbour's sea,
and floating islands thin out near the border. The sliders on the other pages apply to every region.

## Natural features (26.1.2, 26.2, 26.3)

On these versions Terrain also adds natural features to the Overworld's biomes, by biome tag, in every world:
procedural trees (redwoods, willows, baobabs, twisted pines, a rare world tree and more), rocks, fallen logs,
standing stones, sea stacks, hot springs, waterfalls and other landforms. If a wood mod such as Biomes O' Plenty is
installed, its logs can stand in for vanilla wood. The 1.21.1 build doesn't have these yet.

## Dedicated servers

On a dedicated server, set these in `server.properties` before the world is first created:

```properties
level-type=orbisnovus_terrain:orbis_novus
generator-settings={"values":{"sea_level":70,"amp":120},"off":["ores"]}
```

`level-type` picks the style. Use `orbis_novus` (Patchwork Earth) or one of these, all prefixed with
`orbisnovus_terrain:`: `green_vale`, `high_teeth`, `far_spires`, `skyreach`, `red_steps`, `warm_shoals`,
`verdigris_reach`, `grey_silence`, `painted_stillness`, `patchwork_earth`, `custom_mix`.

`generator-settings` is optional. It takes the JSON that the Customize screen's **Copy** button gives you:

- `values`: the slider numbers, by key.
- `mix` and `region` (Patchwork Earth and Custom Mix only): each style's weight by style id, and the region size.
- `off`: any of `vegetation`, `ores` and `lakes`.

For example, a Custom Mix of three styles:

```properties
level-type=orbisnovus_terrain:custom_mix
generator-settings={"mix":{"green_vale":2,"verdigris_reach":1,"grey_silence":1,"high_teeth":0,"red_steps":0,"warm_shoals":0,"far_spires":0,"skyreach":0,"painted_stillness":0},"region":1500}
```

Structures follow the usual `generate-structures` setting. Once the world exists, its settings live in its
`level.dat`, and changing `server.properties` no longer affects it.

## Datapacks

The Customize screen covers each world. Beyond that, everything is datapack JSON:

- `data/orbisnovus_terrain/worldgen/noise_settings/<type>.json` sets the shape and the surface blocks. Every field is
  optional: heights, ridges, terraces, islands, rivers, spires and craters.
- `data/orbisnovus_terrain/worldgen/world_preset/<type>.json` holds the biome rules. The first match wins, and each
  rule names a biome or biome tag, with optional ranges of height, depth, temperature, humidity and river.
- To add a world type of your own to the World Type button, add a new `world_preset` and an entry in
  `data/minecraft/tags/worldgen/world_preset/normal.json`.
- Natural features (26.1.2, 26.2, 26.3): `data/orbisnovus_terrain/tags/worldgen/biome/nature/<feature>.json` says
  where each feature goes. To turn a feature off, override its tag with an empty list.

## Compatibility

- **[Orbis Novus: Dungeons](dungeons.md):** its dungeons, settlements, castles and citadels generate in every Orbis
  Novus world type.
- **Structure and feature mods:** their structures and features generate, since the world runs on the vanilla
  generator.
- **Biome mods** (Biomes O' Plenty, Regions Unexplored and others): the Orbis Novus world types use their own biome
  rules, which pick vanilla biomes and a few common biome tags. Normal worlds are unchanged. Modded cave biomes and
  their carvers are handled.
- **Distant Horizons:** works in its normal mode, where it runs the world generator itself for far chunks.
- **Uninstalling:** a world made with an Orbis Novus world type needs the mod to generate new chunks. Normal worlds
  keep working without it.

## Coming in 1.1

Six new styles. Each is a world type of its own and a Custom Mix part, with weight 0 by default so that 1.0 worlds
keep their regions:

- **Folded World:** rock layers folded into S-curves, so cliffs show them as coloured bands.
- **Tidal Continents:** continents joined by tide flats that flood and drain once an in-game hour. The tide moves real
  water, but only near players, and the cost is small: about 0.06 ms a tick on a test server.
- **Shattered Plates:** flat slabs of land, each tilted its own way, with lava in the cracks.
- **Sinkhole Karst:** flat land full of huge round sinkholes, 50 to 200 blocks deep, with jungle or lush caves at the
  bottom.
- **Ribbon Rivers:** rivers raised 30 to 80 blocks on stone walls and arches across the lowland.
- **The Bowl:** a giant valley. Spawn is flat and round, and the land curves up towards the horizon all round.

And three options for every style:

- **Latitude Bands:** biomes run in bands north and south of spawn, hot near spawn and cold further out. You set the
  band width, from 1000 to 16000 blocks.
- **Erosion Age:** from young and jagged to ancient and rolling.
- **Ruins:** broken roads between regions, sunken walls, old foundations and pillars.
