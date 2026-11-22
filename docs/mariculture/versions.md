# Versions

Mariculture 0.7.0.2 comes in three editions with the same content. What differs is which other mods each can work with.

| Minecraft | Loader | Patchouli | CraftTweaker | KubeJS | Datapack tweaks |
|---|---|---|---|---|---|
| 1.20.1 | Forge 47.4 | yes | yes | yes | yes |
| 1.21.1 | NeoForge 21.1 | yes | yes | yes | yes |
| 26.1.2 | NeoForge 26.1.2 | yes | no (no CraftTweaker for 26.1) | yes | yes |

## Other mods by edition

| Mod | 1.20.1 | 1.21.1 | 26.1.2 |
|---|---|---|---|
| Tinkers' Construct / Hephaestus | Tinkers' Construct 3 | none | Hephaestus |
| Blood Magic / Neo Vitae | Blood Magic 3 | Neo Vitae | Neo Vitae |
| Forestry | Forestry Community Edition 2.x | Forestry Community Edition 3.0 | none |
| Bee bait | Forestry and Complicated Bees 3.4 | Forestry and Complicated Bees 3.6 | Complicated Bees |
| Thaumaturge aspects | no | no | yes |

## Changes

**0.7.0.2**: Fundamentum 1.37.0 or newer is required.

**0.7.0.1**: machine menus, the Compendium and fishing rods.

- Wooden and Titanium fishing rods have recipes.
- Machine menus have colored slot borders, faint item hints and tooltips. Shift-click puts items in the slot made for them.
- The Compendium has a page on how Mariculture differs from the original. It shows in the creative tab and is given once on first join.
- Keybinds are in their own Controls category.
- Fixed the bobber never dipping on Mariculture rods and rod catches sinking in water.
- Fixed the Metal Fish page in the Compendium, DNA machines losing progress without power or when a new battery goes in, water flowing into machines, and rods from other mods showing up when that mod is missing.

**0.7.0**: Alex's Caves fish, Metallurgy: Recast metals and metal fish, and species files.

- 14 fish bite in Alex's Caves' cave biomes, some of them in acid and purple soda.
- Each fish is a species file in `mariculture/fish_species` that sets its biomes, the fluid it bites in, what it makes and its breeding needs.
- Metallurgy metals melt in the Crucible Furnace and cast back into nuggets, ingots and blocks.
- Each Metallurgy ore has a metal fish with an effect that matches its metal and odd breeding needs like certain foods, light, depth or tank size.
- Datapack tweak files can name the mods they need with `requires`.
- Fundamentum is now required.
- The limestone sea bed also forms under dirt and mud floors, set by the `mariculture:seabed_floor` block tag.

**0.6.0**: compatibility with other fishing and ocean mods, all of it in data files.

- Raw fish from any mod in the `mariculture:foreign_fish` tag make fish meal and sushi. The tag holds the fish from Aquaculture 2, Upgrade Aquatic, Alex's Caves, Starcatcher and Tide.
- Biome salinity and temperature come from datapack files in `mariculture/biome_environment`. Modded oceans count as salt water and modded beaches as brackish water. Alex's Caves' Abyssal Chasm is cold salt water.
- Rods from other mods can fish Mariculture's catch at a set tier, listed in `mariculture/rod_tiers`. Aquaculture's iron, gold, diamond and neptunium rods are in the list.
- Mariculture fish show up in Starcatcher's pools and guide.
- On 1.20.1 and 1.21.1, Mariculture fish bite on Tide rods and fill pages in Tide's journal. Mariculture rods keep Mariculture fishing.
- The Stardew Fishing minigame plays for the Mariculture fish on the hook.
- Upgrade Aquatic kelps work in kelp wraps, and Alex's Caves pearls count as pearls.
- Fixed a crash when reeling in a Tide rod with Mariculture installed.

**0.4.1**: the first public release, with all 340 textures redrawn.

**0.4.0**: datapack tweaks and KubeJS; the fishing speed setting and its datapack override; JEI pages for fishing
loot; Hephaestus and Neo Vitae support (1.21.1 and 26.1.2), Forestry (1.20.1 and 1.21.1) and Complicated Bees (all
three); a Jade fix.

**0.3.0**: CraftTweaker; JEI pages for jewelry; Tinkers' Construct (1.20.1); fishing in lava.

**0.2.0**: Thaumaturge aspects (26.1.2).

## 0.5.0

- Now requires Curios. Rings, bracelets and necklaces go in Curios' ring, bracelet and necklace slots; the [Mirror](jewelry.md#mirror) shows the first of each.
- With extra slots from other mods, the strongest piece of each kind counts; the config `jewelry.extra_slots_stack` makes every slot count.
- Jewelry worn in the old built-in slots of a 0.4.1 world is not carried over: take it off with the Mirror before updating.
- New Mariculture advancement tab (16 goals), a grouped creative tab, and fluid tags `c:molten_<name>`, `c:fish_oil` and `c:experience`.
- On NeoForge 1.21.1 and 26.1.2, item data lives in named components such as `mariculture:fish`, and old items move over on their own.
- Mariculture rods now take Lure, Luck of the Sea, Unbreaking and Mending.
