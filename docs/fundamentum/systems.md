# Shared systems

These systems are in the documented Fundamentum 1.36.0 builds. They let a pack or an addon supply the content while the library handles the shared behavior.

## Stats and survival

| System | What a pack or addon can do |
|---|---|
| Stats | Declare named numbers for players, mobs and item stacks under <code>data/&lt;namespace&gt;/fundamentum/stats/</code>. A value can be stored or read from an attribute, mana, an unlock, a vanilla statistic or a scoreboard score. It can appear in the HUD, the stats screen and item tooltips. |
| Startup attributes | A mod can include declarations at <code>META-INF/fundamentum/stats.json</code>. These are handled at startup, separately from reloadable world stat definitions. The public entry point is <code>attribute.StartupStats</code>. |
| Survival meters | Define thirst, temperature or another meter with rules for filling, draining and effects at its limits. A meter can require a mod, or turn off when one is installed. Meters use the stat system and can have HUD bars. A pack or addon supplies the definitions; the library does not add thirst by itself. |
| Stat changes | Addons can respond to <code>Events.StatChanged</code>. The <code>Stats</code> API reads and changes base values and modifiers. <code>/fundamentum stat</code> provides the player-facing commands. |

## Combat and movement

| System | What a pack or addon can do |
|---|---|
| Dodge | A dash and a roll on the Dodge key (Left Alt). Charges, distance, speed, invulnerability and hunger cost are attributes on worn gear. Styles live under <code>data/&lt;namespace&gt;/fundamentum/dodge_style/</code> and gear values under <code>data/&lt;namespace&gt;/fundamentum/dodge_gear/</code>. Charge bars sit beside the hotbar and move in the HUD editor. [File format](datapack/dodge.md). |
| Weight | Item weights come from <code>data/&lt;namespace&gt;/fundamentum/weight_rules/</code>. Carry capacity and load capacity are attributes. Equipment load and inventory weight each have a config switch and are off by default. The meter shows as a bar or as icons. [File format](datapack/weight.md). |
| Boss Bags | <code>data/&lt;namespace&gt;/fundamentum/boss_bags/</code> sets which bosses drop a bag, what it holds and who counts as a fighter. A right click opens the bag. [File format](datapack/boss-bags.md). |
| Apothic Attributes | When it is installed, crit chance, crit damage, armour pierce, projectile speed and ranged damage use its attributes instead of a second copy. 1.20.1 has no ranged damage there. |

## Guides and books

| System | What it provides |
|---|---|
| Guide books | An item with ten book styles, page turns and stamps. Resource packs define books under <code>assets/&lt;namespace&gt;/fundamentum/books/</code> and styles under <code>fundamentum/book_styles/</code>. |
| Guide themes | 50 built-in themes for guide screens, picked from inside the guide, with tags, search and a separate choice per book. Packs add more under <code>fundamentum/guide_themes/</code>. |
| Bestiary | One shared book for every mob from mods that turn it on, under <code>fundamentum/bestiary/</code>. Each mob gets a stat sheet page, locked until the mob has been seen. [File formats for books, styles, themes and the bestiary](datapack/books.md). |

## Structures and shared content

| System | What it provides |
|---|---|
| Multiblocks | Layered patterns under <code>data/&lt;namespace&gt;/fundamentum/multiblocks/</code>, with block, tag and state keys. A pattern can allow rotation and mirroring. Matching, formed/unformed events, missing-block previews and recipe-viewer pages share one definition. |
| Pattern parts | From 1.30.0, an addon can read cells and world positions by key and attach extra data to a key. That lets a machine find the parts of its formed pattern. |
| Unlocks | Track a player or team’s progress by id, with levels, prerequisites, grant sources and conditions. |
| Shared events | A common event vocabulary for spells, bosses, quests, reputation and the library’s own systems. Listeners can use the code event type or its id. |
| Energy and fluids | Helpers for buffers, tanks, neighboring transfers and screen synchronization over the loader’s handlers. |
| Recipe viewers | A shared declaration for recipe layouts, catalysts, information, item hiding and subtypes. JEI and REI are supported where available; EMI support is for 1.21.1 and 1.20.1. |
| Item unification | Choose a preferred material item and use that choice in recipes, drops and inventories, with separate switches for the affected systems. |
| Shared guides | Searchable books and chapters from resource packs, with item, recipe, multiblock, mob and picture embeds and unlock conditions. |

## Factions, quests and gods

From 2.0.0, on every version.

| System | What a pack or addon can do |
|---|---|
| Factions | Give groups of mobs and villagers a reputation with each player, with ranks that set how members treat the player and what villagers charge. Acts such as kills and trades raise or lower rep. Factions can be allies or enemies, and enemy mobs fight each other. [File format](datapack/factions.md). |
| Quests | Write quests with kill, collect, craft, trade, visit and other objectives, offered by giver mobs or quest NPCs with their own names and skins. A Quest Journal, quest screens styled by resource packs and a HUD tracker show them. [File format](datapack/quests.md). |
| Gods | Make gods as factions whose rep is devotion. Players pray at shrines, make offerings, perform rituals and spend favour on boons such as healing, clear weather or a second life. Pantheons can limit a player to one god. [File format](datapack/gods.md). |

## World and presentation

| System | What it provides |
|---|---|
| Climate and seasons | Temperature and humidity from the world around a position, plus optional seasons. Seasons are off by default. Serene Seasons can supply them on the versions where it is supported. |
| Food hooks | Events and modifiers for eating and drinking, with food groups from data and tags. |
| Mob goals | Data-driven goals for ordinary goal-based mobs, including movement, ranged combat and boss phase gates. Brain-based mobs keep their own behavior. |
| Music rules | Tracks selected by world and combat conditions, with priority, fades and volume controls. |
| HUD layout | Anchors, offsets, scale, opacity and visibility for shared HUD elements, with an editor. |
| Configs | Shared declarations, server synchronization, per-world values and a common configuration screen. |

See the [Java API](api.md) for the public entry points and [Versions](versions.md) for target coverage.
