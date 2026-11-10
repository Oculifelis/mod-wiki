# Kiln recipes

Every recipe the [kilns](kilns.md) know, read from the mod's own data. The **Patient Kiln** takes the days shown; the
**Long Kiln** takes three times as long for a whole stack; the **Ember Kiln** takes half, where the world is hot
enough. JEI shows the same list in game.

A recipe with a **condition** only counts its days while the condition holds; otherwise the wait stands still and keeps
the days it has. A recipe with a dimension exists only there, and there it wins over the same item's recipe without one
(so cobblestone turns to blackstone in the Nether and mossy everywhere else).

## Slowlight and vanilla

| In | Out | Days | Long Kiln days | Condition |
|---|---|---|---|---|
| ![Honey Bottle](img/mc/honey_bottle.png){ .mc-icon .mc-inline } Honey Bottle | ![Amber Draught](img/mead.png){ .mc-icon .mc-inline } Amber Draught | 2 | 6 | 1 days in a cellar |
| ![Cobblestone](img/mc/cobblestone.png){ .mc-icon .mc-inline } Cobblestone | ![Blackstone](img/mc/blackstone.png){ .mc-icon .mc-inline } Blackstone | 5 | 15 | in the Nether |
| ![Cornflower](img/mc/cornflower.png){ .mc-icon .mc-inline } Cornflower | 2 × ![Blue Dye](img/mc/blue_dye.png){ .mc-icon .mc-inline } Blue Dye | 3 | 9 |  |
| Packed Ice | Blue Ice | 10 | 30 |  |
| ![Bone](img/mc/bone.png){ .mc-icon .mc-inline } Bone | 6 × ![Bone Meal](img/mc/bone_meal.png){ .mc-icon .mc-inline } Bone Meal | 2 | 6 |  |
| ![Glass Bottle](img/mc/glass_bottle.png){ .mc-icon .mc-inline } Glass Bottle | Bottle o' Enchanting | 1 | 3 | open sky, full moon |
| ![Clay Ball](img/mc/clay_ball.png){ .mc-icon .mc-inline } Clay Ball | ![Brick](img/mc/brick.png){ .mc-icon .mc-inline } Brick | 3 | 9 | open sky, clear weather, by day |
| ![Lanternfruit](img/lanternfruit.png){ .mc-icon .mc-inline } Lanternfruit | ![Candied Lanternfruit](img/candied_lanternfruit.png){ .mc-icon .mc-inline } Candied Lanternfruit | 3 | 9 |  |
| Milk Bucket | Cheese Wheel | 7 | 21 | dark |
| ![Popped Chorus Fruit](img/mc/popped_chorus_fruit.png){ .mc-icon .mc-inline } Popped Chorus Fruit | Chorus Pearl | 3 | 9 | nothing above it, in the End |
| ![Apple](img/mc/apple.png){ .mc-icon .mc-inline } Apple | ![Cider](img/cider.png){ .mc-icon .mc-inline } Cider | 4 | 12 | 3 days in a cellar |
| ![Mud](img/mc/mud.png){ .mc-icon .mc-inline } Mud | 2 × ![Clay Ball](img/mc/clay_ball.png){ .mc-icon .mc-inline } Clay Ball | 2 | 6 |  |
| ![String](img/mc/string.png){ .mc-icon .mc-inline } String | ![Cobweb](img/mc/cobweb.png){ .mc-icon .mc-inline } Cobweb | 3 | 9 |  |
| Red Stained Glass | Crimson Mosaic Glass | 1 | 3 | in the Nether |
| ![Obsidian](img/mc/obsidian.png){ .mc-icon .mc-inline } Obsidian | ![Crying Obsidian](img/mc/crying_obsidian.png){ .mc-icon .mc-inline } Crying Obsidian | 7 | 21 | nothing above it, in the End |
| ![Cooked Cod](img/mc/cooked_cod.png){ .mc-icon .mc-inline } Cooked Cod | ![Cured Cod](img/cured_cod.png){ .mc-icon .mc-inline } Cured Cod | 3 | 9 |  |
| ![Cooked Salmon](img/mc/cooked_salmon.png){ .mc-icon .mc-inline } Cooked Salmon | ![Cured Salmon](img/cured_salmon.png){ .mc-icon .mc-inline } Cured Salmon | 3 | 9 |  |
| ![Oak Sapling](img/mc/oak_sapling.png){ .mc-icon .mc-inline } Oak Sapling | ![Dead Bush](img/mc/dead_bush.png){ .mc-icon .mc-inline } Dead Bush | 7 | 21 | roofed over |
| ![Duskbloom Petals](img/duskbloom_petals.png){ .mc-icon .mc-inline } Duskbloom Petals | ![Dried Duskbloom Petals](img/dried_duskbloom_petals.png){ .mc-icon .mc-inline } Dried Duskbloom Petals | 1 | 3 | open sky, clear weather, by day |
| ![Kelp](img/mc/kelp.png){ .mc-icon .mc-inline } Kelp | ![Dried Kelp](img/mc/dried_kelp.png){ .mc-icon .mc-inline } Dried Kelp | 1 | 3 | open sky, clear weather, by day |
| ![Block of Copper](img/mc/copper_block.png){ .mc-icon .mc-inline } Block of Copper | ![Exposed Copper](img/mc/exposed_copper.png){ .mc-icon .mc-inline } Exposed Copper | 3 | 9 |  |
| ![Spider Eye](img/mc/spider_eye.png){ .mc-icon .mc-inline } Spider Eye | ![Fermented Spider Eye](img/mc/fermented_spider_eye.png){ .mc-icon .mc-inline } Fermented Spider Eye | 3 | 9 |  |
| ![Lanternfruit Seeds](img/lanternfruit_seeds.png){ .mc-icon .mc-inline } Lanternfruit Seeds | ![Gloamwood Seedling](img/gloamwood_sapling.png){ .mc-icon .mc-inline } Gloamwood Seedling | 7 | 21 |  |
| ![Ink Sac](img/mc/ink_sac.png){ .mc-icon .mc-inline } Ink Sac | ![Glow Ink Sac](img/mc/glow_ink_sac.png){ .mc-icon .mc-inline } Glow Ink Sac | 2 | 6 | open sky, by night |
| ![Water Bucket](img/mc/water_bucket.png){ .mc-icon .mc-inline } Water Bucket | Ice | 1 | 3 | open sky, by night, cold biome |
| ![Candied Lanternfruit](img/candied_lanternfruit.png){ .mc-icon .mc-inline } Candied Lanternfruit | ![Lanternfruit Preserve](img/lanternfruit_preserve.png){ .mc-icon .mc-inline } Lanternfruit Preserve | 5 | 15 |  |
| ![Lanternfruit Must](img/lanternfruit_must.png){ .mc-icon .mc-inline } Lanternfruit Must | ![Lanternwine](img/lanternwine.png){ .mc-icon .mc-inline } Lanternwine | 5 | 15 | 3 days in a cellar |
| ![Rotten Flesh](img/mc/rotten_flesh.png){ .mc-icon .mc-inline } Rotten Flesh | ![Leather](img/mc/leather.png){ .mc-icon .mc-inline } Leather | 3 | 9 |  |
| Orange Stained Glass | Magma Mosaic Glass | 1 | 3 | in the Nether |
| ![Cobblestone](img/mc/cobblestone.png){ .mc-icon .mc-inline } Cobblestone | ![Mossy Cobblestone](img/mc/mossy_cobblestone.png){ .mc-icon .mc-inline } Mossy Cobblestone | 4 | 12 |  |
| ![Stone Bricks](img/mc/stone_bricks.png){ .mc-icon .mc-inline } Stone Bricks | ![Mossy Stone Bricks](img/mc/mossy_stone_bricks.png){ .mc-icon .mc-inline } Mossy Stone Bricks | 4 | 12 |  |
| ![Dirt](img/mc/dirt.png){ .mc-icon .mc-inline } Dirt | ![Mud](img/mc/mud.png){ .mc-icon .mc-inline } Mud | 1 | 3 | rain |
| ![far (disc)](img/mc/music_disc_far.png){ .mc-icon .mc-inline } far (disc) | ![music_disc_a_week_in (disc)](img/music_disc_a_week_in.png){ .mc-icon .mc-inline } music_disc_a_week_in (disc) | 7 | 21 |  |
| ![stal (disc)](img/mc/music_disc_stal.png){ .mc-icon .mc-inline } stal (disc) | ![music_disc_lantern_hours (disc)](img/music_disc_lantern_hours.png){ .mc-icon .mc-inline } music_disc_lantern_hours (disc) | 5 | 15 |  |
| ![mellohi (disc)](img/mc/music_disc_mellohi.png){ .mc-icon .mc-inline } mellohi (disc) | ![music_disc_patient_light (disc)](img/music_disc_patient_light.png){ .mc-icon .mc-inline } music_disc_patient_light (disc) | 4 | 12 |  |
| ![Weathered Copper](img/mc/weathered_copper.png){ .mc-icon .mc-inline } Weathered Copper | ![Oxidized Copper](img/mc/oxidized_copper.png){ .mc-icon .mc-inline } Oxidized Copper | 3 | 9 |  |
| ![Sugar Cane](img/mc/sugar_cane.png){ .mc-icon .mc-inline } Sugar Cane | ![Paper](img/mc/paper.png){ .mc-icon .mc-inline } Paper | 2 | 6 | open sky, clear weather, by day |
| ![Slowlight Shard](img/slowlight_shard.png){ .mc-icon .mc-inline } Slowlight Shard | ![Patience Armor Trim](img/patience_armor_trim_smithing_template.png){ .mc-icon .mc-inline } Patience Armor Trim | 14 | 42 |  |
| ![Rotten Flesh](img/mc/rotten_flesh.png){ .mc-icon .mc-inline } Rotten Flesh | Phantom Membrane | 1 | 3 | open sky, full moon |
| ![Pitcher Pod](img/mc/pitcher_pod.png){ .mc-icon .mc-inline } Pitcher Pod | ![Pitcher Plant](img/mc/pitcher_plant.png){ .mc-icon .mc-inline } Pitcher Plant | 3 | 9 |  |
| ![Coarse Dirt](img/mc/coarse_dirt.png){ .mc-icon .mc-inline } Coarse Dirt | ![Podzol](img/mc/podzol.png){ .mc-icon .mc-inline } Podzol | 4 | 12 |  |
| ![Potato](img/mc/potato.png){ .mc-icon .mc-inline } Potato | ![Poisonous Potato](img/mc/poisonous_potato.png){ .mc-icon .mc-inline } Poisonous Potato | 3 | 9 | roofed over |
| ![Chorus Fruit](img/mc/chorus_fruit.png){ .mc-icon .mc-inline } Chorus Fruit | ![Popped Chorus Fruit](img/mc/popped_chorus_fruit.png){ .mc-icon .mc-inline } Popped Chorus Fruit | 2 | 6 | nothing above it, in the End |
| ![Sweet Berries](img/mc/sweet_berries.png){ .mc-icon .mc-inline } Sweet Berries | ![Preserved Berries](img/preserved_berries.png){ .mc-icon .mc-inline } Preserved Berries | 1 | 3 |  |
| Bone Block | Skeleton Skull | 1 | 3 | open sky, new moon |
| ![Amethyst Shard](img/mc/amethyst_shard.png){ .mc-icon .mc-inline } Amethyst Shard | ![Slowlight Shard](img/slowlight_shard.png){ .mc-icon .mc-inline } Slowlight Shard | 7 | 21 |  |
| ![Dried Duskbloom Petals](img/dried_duskbloom_petals.png){ .mc-icon .mc-inline } Dried Duskbloom Petals | ![Slowlight Shard](img/slowlight_shard.png){ .mc-icon .mc-inline } Slowlight Shard | 14 | 42 | open sky, by night |
| Light Blue Stained Glass | Soul Mosaic Glass | 1 | 3 | in the Nether |
| ![Sand](img/mc/sand.png){ .mc-icon .mc-inline } Sand | ![Soul Sand](img/mc/soul_sand.png){ .mc-icon .mc-inline } Soul Sand | 5 | 15 | in the Nether |
| ![Wet Sponge](img/mc/wet_sponge.png){ .mc-icon .mc-inline } Wet Sponge | ![Sponge](img/mc/sponge.png){ .mc-icon .mc-inline } Sponge | 1 | 3 | open sky, clear weather, by day |
| ![Ender Pearl](img/mc/ender_pearl.png){ .mc-icon .mc-inline } Ender Pearl | ![Still Shard](img/still_shard.png){ .mc-icon .mc-inline } Still Shard | 10 | 30 | nothing above it, in the End |
| ![Honey Block](img/mc/honey_block.png){ .mc-icon .mc-inline } Honey Block | 12 × ![Sugar](img/mc/sugar.png){ .mc-icon .mc-inline } Sugar | 5 | 15 |  |
| ![Gravel](img/mc/gravel.png){ .mc-icon .mc-inline } Gravel | ![Suspicious Gravel (kiln finds)](img/mc/suspicious_gravel.png){ .mc-icon .mc-inline } Suspicious Gravel (kiln finds) | 7 | 21 |  |
| ![Sand](img/mc/sand.png){ .mc-icon .mc-inline } Sand | ![Suspicious Sand (kiln finds)](img/mc/suspicious_sand.png){ .mc-icon .mc-inline } Suspicious Sand (kiln finds) | 7 | 21 |  |
| ![Torchflower Seeds](img/mc/torchflower_seeds.png){ .mc-icon .mc-inline } Torchflower Seeds | ![Torchflower](img/mc/torchflower.png){ .mc-icon .mc-inline } Torchflower | 2 | 6 |  |
| Cyan Stained Glass | Warped Mosaic Glass | 1 | 3 | in the Nether |
| ![Glass Bottle](img/mc/glass_bottle.png){ .mc-icon .mc-inline } Glass Bottle | ![Water Bottle](img/mc/potion.png){ .mc-icon .mc-inline } Water Bottle | 1 | 3 | rain |
| ![Bucket](img/mc/bucket.png){ .mc-icon .mc-inline } Bucket | ![Water Bucket](img/mc/water_bucket.png){ .mc-icon .mc-inline } Water Bucket | 2 | 6 | rain |
| ![Exposed Copper](img/mc/exposed_copper.png){ .mc-icon .mc-inline } Exposed Copper | ![Weathered Copper](img/mc/weathered_copper.png){ .mc-icon .mc-inline } Weathered Copper | 3 | 9 |  |
| ![Sponge](img/mc/sponge.png){ .mc-icon .mc-inline } Sponge | ![Wet Sponge](img/mc/wet_sponge.png){ .mc-icon .mc-inline } Wet Sponge | 1 | 3 | rain |

## With other mods

Each of these loads only when its mod is installed.

### Twilight Forest

| In | Out | Days | Long Kiln days | Condition |
|---|---|---|---|---|
| ![Steak](img/mc/cooked_beef.png){ .mc-icon .mc-inline } Steak | ![Beef Jerky](img/twilightforest/beef_jerky.png){ .mc-icon .mc-inline } Beef Jerky | 3 | 9 |  |
| ![Blackberry](img/twilightforest/blackberry.png){ .mc-icon .mc-inline } Blackberry | ![Blackberry Preserve](img/blackberry_preserve.png){ .mc-icon .mc-inline } Blackberry Preserve | 4 | 12 |  |
| ![Blightberry](img/twilightforest/blightberry.png){ .mc-icon .mc-inline } Blightberry | ![Blightberry Preserve](img/blightberry_preserve.png){ .mc-icon .mc-inline } Blightberry Preserve | 4 | 12 |  |
| ![Cooked Chicken](img/mc/cooked_chicken.png){ .mc-icon .mc-inline } Cooked Chicken | ![Chicken Jerky](img/twilightforest/chicken_jerky.png){ .mc-icon .mc-inline } Chicken Jerky | 3 | 9 |  |
| ![Hydra Chop](img/twilightforest/hydra_chop.png){ .mc-icon .mc-inline } Hydra Chop | ![Cured Hydra Chop](img/cured_hydra_chop.png){ .mc-icon .mc-inline } Cured Hydra Chop | 5 | 15 |  |
| ![Duskberry](img/twilightforest/duskberry.png){ .mc-icon .mc-inline } Duskberry | ![Duskberry Preserve](img/duskberry_preserve.png){ .mc-icon .mc-inline } Duskberry Preserve | 4 | 12 |  |
| ![Pufferfish](img/mc/pufferfish.png){ .mc-icon .mc-inline } Pufferfish | ![Fugu Jerky](img/twilightforest/fugu_jerky.png){ .mc-icon .mc-inline } Fugu Jerky | 3 | 9 |  |
| ![Maloberry](img/twilightforest/maloberry.png){ .mc-icon .mc-inline } Maloberry | ![Maloberry Preserve](img/maloberry_preserve.png){ .mc-icon .mc-inline } Maloberry Preserve | 4 | 12 |  |
| ![Cooked Meef](img/twilightforest/cooked_meef.png){ .mc-icon .mc-inline } Cooked Meef | ![Meef Jerky](img/twilightforest/meef_jerky.png){ .mc-icon .mc-inline } Meef Jerky | 3 | 9 |  |
| ![Castle Brick](img/twilightforest/castle_brick.png){ .mc-icon .mc-inline } Castle Brick | ![Mossy Castle Brick](img/twilightforest/mossy_castle_brick.png){ .mc-icon .mc-inline } Mossy Castle Brick | 5 | 15 |  |
| ![Mazestone Brick](img/twilightforest/mazestone_brick.png){ .mc-icon .mc-inline } Mazestone Brick | ![Mossy Mazestone](img/twilightforest/mossy_mazestone.png){ .mc-icon .mc-inline } Mossy Mazestone | 4 | 12 |  |
| ![Underbrick](img/twilightforest/underbrick.png){ .mc-icon .mc-inline } Underbrick | ![Mossy Underbrick](img/twilightforest/mossy_underbrick.png){ .mc-icon .mc-inline } Mossy Underbrick | 4 | 12 |  |
| ![Cooked Mutton](img/mc/cooked_mutton.png){ .mc-icon .mc-inline } Cooked Mutton | ![Mutton Jerky](img/twilightforest/mutton_jerky.png){ .mc-icon .mc-inline } Mutton Jerky | 3 | 9 |  |
| ![Cooked Porkchop](img/mc/cooked_porkchop.png){ .mc-icon .mc-inline } Cooked Porkchop | ![Pork Jerky](img/twilightforest/pork_jerky.png){ .mc-icon .mc-inline } Pork Jerky | 3 | 9 |  |
| ![Cooked Rabbit](img/mc/cooked_rabbit.png){ .mc-icon .mc-inline } Cooked Rabbit | ![Rabbit Jerky](img/twilightforest/rabbit_jerky.png){ .mc-icon .mc-inline } Rabbit Jerky | 3 | 9 |  |
| ![Raspberry](img/twilightforest/raspberry.png){ .mc-icon .mc-inline } Raspberry | ![Raspberry Preserve](img/raspberry_preserve.png){ .mc-icon .mc-inline } Raspberry Preserve | 4 | 12 |  |
| ![Skyberry](img/twilightforest/skyberry.png){ .mc-icon .mc-inline } Skyberry | ![Skyberry Preserve](img/skyberry_preserve.png){ .mc-icon .mc-inline } Skyberry Preserve | 4 | 12 |  |
| ![Stingberry](img/twilightforest/stingberry.png){ .mc-icon .mc-inline } Stingberry | ![Stingberry Preserve](img/stingberry_preserve.png){ .mc-icon .mc-inline } Stingberry Preserve | 4 | 12 |  |
| ![Torchberries](img/twilightforest/torchberries.png){ .mc-icon .mc-inline } Torchberries | ![Torchberry Preserve](img/torchberry_preserve.png){ .mc-icon .mc-inline } Torchberry Preserve | 4 | 12 |  |
| ![Tropical Fish](img/mc/tropical_fish.png){ .mc-icon .mc-inline } Tropical Fish | ![Tropical Fish Jerky](img/twilightforest/tropical_fish_jerky.png){ .mc-icon .mc-inline } Tropical Fish Jerky | 3 | 9 |  |
| ![Blueberry](img/aether_ii/blueberry.png){ .mc-icon .mc-inline } Blueberry | ![Twilight Blueberry Preserve](img/twilight_blueberry_preserve.png){ .mc-icon .mc-inline } Twilight Blueberry Preserve | 4 | 12 |  |
| ![Cooked Venison](img/twilightforest/cooked_venison.png){ .mc-icon .mc-inline } Cooked Venison | ![Venison Jerky](img/twilightforest/venison_jerky.png){ .mc-icon .mc-inline } Venison Jerky | 3 | 9 |  |

### The Undergarden

| In | Out | Days | Long Kiln days | Condition |
|---|---|---|---|---|
| Droopvine Item | ![Candied Droopfruit](img/candied_droopfruit.png){ .mc-icon .mc-inline } Candied Droopfruit | 3 | 9 |  |
| ![Depthrock Bricks](img/undergarden/depthrock_bricks.png){ .mc-icon .mc-inline } Depthrock Bricks | ![Cracked Depthrock Bricks](img/undergarden/cracked_depthrock_bricks.png){ .mc-icon .mc-inline } Cracked Depthrock Bricks | 3 | 9 |  |
| ![Shiverstone Bricks](img/undergarden/shiverstone_bricks.png){ .mc-icon .mc-inline } Shiverstone Bricks | ![Cracked Shiverstone Bricks](img/undergarden/cracked_shiverstone_bricks.png){ .mc-icon .mc-inline } Cracked Shiverstone Bricks | 3 | 9 |  |
| ![Dweller Steak](img/undergarden/dweller_steak.png){ .mc-icon .mc-inline } Dweller Steak | ![Cured Dweller Steak](img/cured_dweller_steak.png){ .mc-icon .mc-inline } Cured Dweller Steak | 4 | 12 |  |
| ![Gloomper Leg](img/undergarden/gloomper_leg.png){ .mc-icon .mc-inline } Gloomper Leg | ![Cured Gloomper Leg](img/cured_gloomper_leg.png){ .mc-icon .mc-inline } Cured Gloomper Leg | 4 | 12 |  |
| ![Cooked Gwibling](img/undergarden/cooked_gwibling.png){ .mc-icon .mc-inline } Cooked Gwibling | ![Cured Gwibling](img/cured_gwibling.png){ .mc-icon .mc-inline } Cured Gwibling | 3 | 9 |  |
| ![Ditchbulb](img/undergarden/ditchbulb.png){ .mc-icon .mc-inline } Ditchbulb | ![Ditchbulb Preserve](img/ditchbulb_preserve.png){ .mc-icon .mc-inline } Ditchbulb Preserve | 4 | 12 |  |
| ![Glitterkelp](img/undergarden/glitterkelp.png){ .mc-icon .mc-inline } Glitterkelp | ![Dried Glitterkelp](img/dried_glitterkelp.png){ .mc-icon .mc-inline } Dried Glitterkelp | 2 | 6 |  |
| ![Blisterberry](img/undergarden/blisterberry.png){ .mc-icon .mc-inline } Blisterberry | ![Rotten Blisterberry](img/undergarden/rotten_blisterberry.png){ .mc-icon .mc-inline } Rotten Blisterberry | 2 | 6 |  |

### The Aether

| In | Out | Days | Long Kiln days | Condition |
|---|---|---|---|---|
| ![Aechor Petal](img/aether_ii/aechor_petal.png){ .mc-icon .mc-inline } Aechor Petal | ![Aechor Petal Tea](img/aechor_petal_tea.png){ .mc-icon .mc-inline } Aechor Petal Tea | 2 | 6 |  |
| ![Blue Berry](img/aether/blue_berry.png){ .mc-icon .mc-inline } Blue Berry | ![Blue Berry Preserve](img/blue_berry_preserve.png){ .mc-icon .mc-inline } Blue Berry Preserve | 4 | 12 |  |
| ![Enchanted Berry](img/aether/enchanted_berry.png){ .mc-icon .mc-inline } Enchanted Berry | ![Enchanted Berry Preserve](img/enchanted_berry_preserve.png){ .mc-icon .mc-inline } Enchanted Berry Preserve | 4 | 12 |  |
| ![White Apple](img/aether/white_apple.png){ .mc-icon .mc-inline } White Apple | ![White Apple Cider](img/white_apple_cider.png){ .mc-icon .mc-inline } White Apple Cider | 4 | 12 |  |

### Aerial Hell

| In | Out | Days | Long Kiln days | Condition |
|---|---|---|---|---|
| ![Aerial Berry](img/aerialhell/aerial_berry.png){ .mc-icon .mc-inline } Aerial Berry | ![Aerial Berry Preserve](img/aerial_berry_preserve.png){ .mc-icon .mc-inline } Aerial Berry Preserve | 4 | 12 |  |
| ![Glowing Stick Fruit](img/aerialhell/glowing_stick_fruit.png){ .mc-icon .mc-inline } Glowing Stick Fruit | ![Candied Glowing Stick Fruit](img/candied_glowing_stick_fruit.png){ .mc-icon .mc-inline } Candied Glowing Stick Fruit | 3 | 9 |  |
| ![Cooked Phantom Meat](img/aerialhell/cooked_phantom_meat.png){ .mc-icon .mc-inline } Cooked Phantom Meat | ![Cured Phantom Meat](img/cured_phantom_meat.png){ .mc-icon .mc-inline } Cured Phantom Meat | 4 | 12 |  |
| ![Cooked Turtle Meat](img/aerialhell/cooked_turtle_meat.png){ .mc-icon .mc-inline } Cooked Turtle Meat | ![Cured Turtle Meat](img/cured_turtle_meat.png){ .mc-icon .mc-inline } Cured Turtle Meat | 4 | 12 |  |
| ![Rotten Leather](img/aerialhell/rotten_leather.png){ .mc-icon .mc-inline } Rotten Leather | ![Leather](img/mc/leather.png){ .mc-icon .mc-inline } Leather | 4 | 12 |  |
| ![Venomous Snake Skin](img/aerialhell/venomous_snake_skin.png){ .mc-icon .mc-inline } Venomous Snake Skin | ![Leather](img/mc/leather.png){ .mc-icon .mc-inline } Leather | 3 | 9 |  |
| ![Mud Bricks](img/aerialhell/mud_bricks.png){ .mc-icon .mc-inline } Mud Bricks | Mossy Mud Bricks | 4 | 12 |  |
| ![Shadow Catacombs Bricks](img/aerialhell/shadow_catacombs_bricks.png){ .mc-icon .mc-inline } Shadow Catacombs Bricks | Mossy Shadow Catacombs Bricks | 5 | 15 |  |
| ![Stellar Cobblestone](img/aerialhell/stellar_cobblestone.png){ .mc-icon .mc-inline } Stellar Cobblestone | Mossy Stellar Cobblestone | 4 | 12 |  |
| ![Ruby Aerial Berry](img/aerialhell/ruby_aerial_berry.png){ .mc-icon .mc-inline } Ruby Aerial Berry | ![Ruby Aerial Berry Preserve](img/ruby_aerial_berry_preserve.png){ .mc-icon .mc-inline } Ruby Aerial Berry Preserve | 4 | 12 |  |
| ![Purple Shadow Fruit](img/aerialhell/purple_shadow_fruit.png){ .mc-icon .mc-inline } Purple Shadow Fruit | ![Shadow Fruit Preserve](img/shadow_fruit_preserve.png){ .mc-icon .mc-inline } Shadow Fruit Preserve | 4 | 12 |  |
| ![Dark Shadow Fruit](img/aerialhell/dark_shadow_fruit.png){ .mc-icon .mc-inline } Dark Shadow Fruit | ![Shadow Fruit Preserve](img/shadow_fruit_preserve.png){ .mc-icon .mc-inline } Shadow Fruit Preserve | 4 | 12 |  |
| ![Stellar Sugar Cane](img/aerialhell/stellar_sugar_cane.png){ .mc-icon .mc-inline } Stellar Sugar Cane | ![Stellar Rock Sugar](img/stellar_rock_sugar.png){ .mc-icon .mc-inline } Stellar Rock Sugar | 3 | 9 |  |
| ![Stellar Bread](img/aerialhell/stellar_bread.png){ .mc-icon .mc-inline } Stellar Bread | ![Stellar Rusk](img/stellar_rusk.png){ .mc-icon .mc-inline } Stellar Rusk | 2 | 6 |  |
| ![Vibrant Aerial Berry](img/aerialhell/vibrant_aerial_berry.png){ .mc-icon .mc-inline } Vibrant Aerial Berry | ![Vibrant Aerial Berry Preserve](img/vibrant_aerial_berry_preserve.png){ .mc-icon .mc-inline } Vibrant Aerial Berry Preserve | 4 | 12 |  |
| ![Volucite Aerial Berry](img/aerialhell/volucite_aerial_berry.png){ .mc-icon .mc-inline } Volucite Aerial Berry | ![Volucite Aerial Berry Preserve](img/volucite_aerial_berry_preserve.png){ .mc-icon .mc-inline } Volucite Aerial Berry Preserve | 4 | 12 |  |
