# Fishing

![Rods and bait](img/sheet_fishing.png)

## Rods

Mariculture's rods all catch better than the vanilla rod, and each takes its own baits. Put bait in the rod's
inventory; most bait comes from the Sifter.

| | Rod | Lasts | Baits |
|---|---|---|---|
| ![Reed Fishing Rod](img/reed_fishing_rod.png){ .mc-icon } | Reed Fishing Rod | 96 casts | ant, bread, grasshopper |
| ![Wooden Fishing Rod](img/wooden_fishing_rod.png){ .mc-icon } | Wooden Fishing Rod | 320 casts | grasshopper, maggot, worm |
| ![Titanium Fishing Rod](img/titanium_fishing_rod.png){ .mc-icon } | Titanium Fishing Rod | 640 casts | worm, bee, minnow |
| ![Flux Rod](img/flux_rod.png){ .mc-icon } | Flux Rod | never wears out | every bait; 100 FE a cast, holds 250,000 FE |

Some fish only bite on a good enough rod: [Fish and breeding](fish.md#species) lists the lowest rod for each.

In the Nether a Mariculture hook floats on lava, and fish bite there too.

How fast fish bite is set by `fishing_speed_multiplier` in the [config](config.md#fishery), and per rod by a
[datapack](packs.md#fishing-speed).

## Salt and heat

![Aquatic Environment Analyser](img/aquatic_environment_analyser.png){ .mc-icon .mc-inline } Every fish likes its own
water. Two things matter:

- **Salinity** is fixed by the biome: fresh, brackish or saline.
- **Temperature** starts from the biome and changes with height, weather, the sun and light.

The Aquatic Environment Analyser shows both where you stand.

| Biome | Water | Temperature (°C) |
|---|---|---|
| Beach | brackish | 25 |
| Desert | fresh | 45 |
| Extreme Hills | fresh | 5 |
| Forest | fresh | 10 |
| Frozen Ocean | saline | -1 |
| Frozen River | fresh | -1 |
| Ice Plains | fresh | -1 |
| Jungle | fresh | 25 |
| Mushroom Island | fresh | 15 |
| Nether | fresh | 80 |
| Ocean | saline | 4 |
| Plains | fresh | 10 |
| River | fresh | 10 |
| The End | fresh | 3 |
| Swamp | fresh | 8 |
| Taiga | fresh | 1 |

## Wild fish

These bite in the wild. Every other species has to be [bred](fish.md#breeding).

| Fish | Water | Height | Temperature (°C) |
|---|---|---|---|
| Minnow | fresh | Y 70 and up | -1 to 45 |
| Cod | saline | any | -3 to 20 |
| Sting Ray | brackish | any | 19 to 29 |
| Squid | saline | any | 3 to 20 |
| Damselfish | fresh | any | 22 to 27 |
| Neon Tetra | fresh | any | 20 to 28 |
| Spiderfish | fresh | below Y -48 | -5 to 20 |
| Silver-Stripe Blaasop | saline | below Y -16 | -3 to 5 |
| Netherfish | the Nether | any | 45 to 100 |
| Nightfish | the End, or at night | any | -10 to 66 |

Goldfish, Cod, Walleye and the other wild species in the [species table](fish.md#species) bite wherever their water
suits them.

## Odd catches

- **Zombies** sometimes spawn with a fishing rod or a bucket hat and can drop them.
- **Rockhoppers** are penguins on cold shores. Feed them fish to tame them; it works about one time in three.
