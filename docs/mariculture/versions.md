# Versions

Mariculture 0.5.0 comes in three editions with the same content. What differs is which other mods each can work with.

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
- NeoForge 1.21.1 and 26.1.2: item data lives in named components such as `mariculture:fish`; old items move over on their own.
- Fixed: Mariculture rods now take Lure, Luck of the Sea, Unbreaking and Mending.
