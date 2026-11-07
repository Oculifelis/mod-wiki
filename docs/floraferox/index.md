# Flora Ferox

![Flora Ferox logo](../assets/floraferox_logo.png){ width="140" align=right }

29 plant creatures across the Overworld, the Nether and the End. You grow and splice herbs and brew from them, then
fight what they wake with seed guns, whips, sceptres and cleavers.

**Requires** [Fundamentum](../fundamentum/index.md) and Curios. **Optional:** JEI, for the Grafting Bench splices, the
brews and info pages.

**Versions:** NeoForge 26.1.2.

## The four families

Every creature, herb, weapon and charm belongs to one of four herb families. Each family takes full damage from one
kind of damage, and half from every other kind. Untyped damage, such as fire and falling, is not scaled.

| Family | Herb | Weak to | Weapon line |
|---|---|---|---|
| **Pulse** | Pulseroot | ranged | seed guns |
| **Dusk** | Duskpetal | magic | sceptres |
| **Moon** | Moonwisp | summons | whips |
| **Mire** | Mirecap | melee | cleavers |

The [bestiary](bestiary.md) lists every creature with its family, stats, moves and drops.

## How it plays

1. **Pick a flower.** Picking a sunflower (Pulse), a rose, poppy, peony or pink tulip (Dusk), a blue orchid or
   cornflower (Moon), or a lily pad, moss or mangrove propagule (Mire) has a 1 in 6 chance of waking that family's
   first monster.
2. **Splice a herb.** At the **Grafting Bench**, splice wheat seeds with that flower to get the family's herb seeds.
   Splice those with an **Ember Graft** for the burning strain, then with a **Rime Graft** for the frozen strain.
3. **Grow and pick it.** Herbs grow on farmland like any crop. Picking a grown herb always wakes a monster: the common
   herb wakes its family's first monster, and the burning and frozen strains wake the [hunters](bestiary.md#the-hunters).
4. **Spend the drops.** Tokens, trophies and grafts buy and craft better gear.

The **Weedwarden** is a villager who works at the Grafting Bench. She trades seeds, grafts, pellets, charms and weapons
for tokens and trophies. The three **Grower's Almanac** books explain each step: the first is crafted, and the
Weedwarden sells the other two.

## Brewing

Each herb brewed into an Awkward Potion gives its family's drink: twelve in all, with splash, lingering and arrow
versions. Each boosts its family's damage type and adds a vanilla effect to go with it. The burning strains add fire
resistance, and the frozen strains add one more effect.

## Gear

Every weapon line has three tiers: a plain one, a burning one that sets targets alight, and a frozen one that slows
and chills them. Each later tier is crafted from the one before, with herbs, a graft and the family's trophy.

- **Cleavers (melee):** right click sends a slash flying a few blocks.
- **Sceptres (magic):** left click casts petal bolts. Right click is the tier's support: Dusk Bloom heals you and allies
  within 4 blocks, Ember Ward rings you in fire and makes you fireproof, Rime Shell gives Resistance and Absorption and
  freezes hostiles near you.
- **Seed guns (ranged):** one-handed pistols that fire heart-shaped seed pellets, on left or right click. They have
  their own enchantments: Heartsight, Seed Hopper, Weedkiller, Quickdraw, Bloom Shot, Heartmend and Infinity.
- **Whips (summon):** Fundamentum cord whips. Your pets attack whatever the whip hits.
- **Grappling hooks:** one for every weapon, worn in the hook slot and fired with H. Mire grapples pull hardest, Dusk
  tendrils hang in the air on a miss, Pulse hooks reach furthest, Moon grapnels hold you still.
- **Wings:** Leafwing, Emberwing and Rimewing, each flying further than the last.
- **Armour:** Leafguard, Emberbark and Rimebark. Each set has four helmets, one per damage type. A full set boosts that
  damage type, and the helmet decides the set effect (twelve in all, each on its helmet's tooltip).
- **Charms:** a charm for each family, and one for each hunter's trophy. Each adds to its family's damage; the trophy
  charms add a small effect too. Worn in a Curios charm slot or carried.
- **Peace Lily Charm:** every Flora Ferox creature leaves you alone until you strike it.

## For pack makers

Creature spawns are standard NeoForge biome modifiers (`data/floraferox/neoforge/biome_modifier/`), so a datapack can
move or remove them. The chance of a picked flower waking a monster is the config value `verdureHarvestChance`.

## Credits

By Oculifelis: code, design and art. Inspired by Violent Verdure, the Terraria mod by Violytta Ran.

- Rhodox, Painterly Pack, used with permission.
- Malcolm Riley, [Unused Textures](https://github.com/malcolmriley/unused-textures),
  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), recoloured.
- TriQue06, Mythic Upgrades (MIT): the base of the armour.
