# Other mods

Smaller mods by Oculifelis that don't need a whole section.

## Spartan x Better Combat Unofficial

Gives all 364 [Spartan Weaponry Unofficial](https://www.curseforge.com/projects/1450963) melee weapons their own
[Better Combat](https://www.curseforge.com/projects/639842) attack animation: katanas combo, halberds sweep, warhammers
slam. Without it, they all swing like a sword.

Since 0.2.0 it also animates the 220 dragon bone, dragonsteel and myrmex weapons of
[Spartan Weaponry: Ice and Fire Unofficial](https://www.curseforge.com/projects/1610003), when that addon is installed.
It's optional; nothing changes without it.

It's data only, with no code. Damage, speed and reach stay as Spartan sets them.

**Requires** [Spartan Weaponry Unofficial](https://www.curseforge.com/projects/1450963) and
[Better Combat](https://www.curseforge.com/projects/639842), on client and server.

**Versions:** NeoForge 1.21.1. [On CurseForge](https://www.curseforge.com/projects/1786749).

| Spartan weapon | Better Combat animation | Hands | Combo hits |
|---|---|---|---|
| Dagger, Parrying Dagger | Dagger | One | 3 |
| Longsword | Sword | One | 3 |
| Greatsword | Claymore | Two | 3 |
| Katana | Katana | Two | 4 |
| Saber | Cutlass | One | 2 |
| Rapier | Rapier | One | 2 |
| Battleaxe | Double axe | Two | 2 |
| Warhammer, Battle Hammer | Hammer | Two | 1 |
| Flanged Mace, Club | Mace | One | 3 |
| Cestus | Fist | One | 1 |
| Spear, Pike | Spear | Two | 1 |
| Lance | Lance | One | 2 |
| Halberd | Halberd | Two | 2 |
| Glaive | Glaive | Two | 3 |
| Quarterstaff | Battlestaff | Two | 6 |
| Scythe | Scythe | Two | 2 |
| Longbow | Heavy bow (hold pose) | Two | - |
| Heavy Crossbow | Heavy crossbow (hold pose) | Two | - |

Every material is covered, and Ice and Fire weapons (dragon bone, flamed/iced/lightning dragon bone,
fire/ice/lightning dragonsteel, desert/jungle myrmex chitin and stinger) get the same animation per type. Javelins, throwing knives, tomahawks and boomerangs are left alone so they can still be
thrown.

## Apiflux

An addon for [Complicated Bees](https://modrinth.com/mod/complicated-bees) that lets its FE machines (the
Centrifuge, the Gyrofuge controller and energy cell, and the Mellarium energy cell) run on **Create rotation**.
Its sister mod is [Manacomb](#manacomb), for Botania mana; the two work side by side.

- **Kinetic Dynamo:** put it against the machine and run a shaft into its collar. It gives FE out of its other
  five sides: **0.5 FE per tick for each RPM**, up to 256 FE/t, and draws **2 stress units per RPM**. It stores
  nothing, so a slow dynamo runs the machine part of the time: twice the speed is twice the work, up to the
  machine's full rate. Goggles show its stress and FE output.
- **Recipe:** shaft on top, copper ingot on each side of an andesite casing, redstone below.
- **"Instead of RF" switch:** in `serverconfig/apiflux-server.toml`, `rfInputDisabled = true` makes the four
  machines refuse FE from every other source (Complicated Bees' generators and cables too); only Kinetic Dynamos,
  and Manacomb's mana if installed, get in. Off by default. `kineticEnabled` turns the dynamo on or off.
- Every rate is in a data map, so a datapack can change it.
- Jade shows a line on a machine when outside FE is off; JEI has an info page on the Kinetic Dynamo.

**Requires** Complicated Bees 3.6 or later. **Optional:** Create 6.0.x (the dynamo; without Create, only the RF
switch does anything).

**Versions:** 0.1.0, NeoForge 1.21.1 (21.1.229 or later). [On CurseForge](https://www.curseforge.com/projects/1793756).

## Manacomb

An addon for [Complicated Bees](https://modrinth.com/mod/complicated-bees) that makes the same four FE machines
Botania **mana** receivers. No new block. Its sister mod is [Apiflux](#apiflux), for Create rotation.

- Aim a **Mana Spreader** at the machine, or put a **Mana Spark** on top to draw from pool sparks of the same
  colour, like a Terrestrial Agglomeration Plate.
- **10 FE per mana** by default: a full 160-mana burst is 1600 FE, which runs a Centrifuge (20 FE/t) for 80 ticks.
  Mana turns into FE as it arrives; a spreader stops firing at a full machine.
- **"Instead of RF" switch:** in `serverconfig/manacomb-server.toml`, `rfInputDisabled = true` lets only mana in.
  Off by default. With Apiflux installed, use Apiflux's switch instead; it covers both. `manaEnabled` turns mana
  input on or off.
- The rate, and which machines take mana, are data maps a datapack can change.
- Jade shows "Runs on mana: 1 mana = 10 FE" on a machine; JEI has an info page on the four machines.

**Requires** Complicated Bees 3.6 or later and Botania.

**Versions:** 0.1.0, NeoForge 1.21.1 (21.1.229 or later). [On CurseForge](https://www.curseforge.com/projects/1793766).
