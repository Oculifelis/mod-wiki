# Weapon tuning

These examples come from built jars: Flora Ferox 1.20.0 submitted with Fundamentum 1.28.0, and Arcana Varia 0.8.0 for NeoForge 26.1.2. See [Versions](../versions.md) for public availability.

## Thrown weapons

Flora Ferox ships four definitions under `data/floraferox/fundamentum/thrown/`. A datapack can replace the matching file. For example, `leafrang.json` contains:

```json
{
  "item": "floraferox:leafrang",
  "throw_speed": 1.4,
  "damage": 5,
  "pierce": 1,
  "returns": {
    "range": 14,
    "hits_on_return": true
  },
  "spin": "flat",
  "spin_speed": 40
}
```

`item` identifies the item. This Leafrang has damage 5, throw speed 1.4, pierces one target, returns at range 14 and can hit on the return. The other submitted definitions show a consumable that breaks on impact (`runed_seed` and `spore_flask`) and a recoverable projectile that sticks (`thorn_javelin`).

## Scythes

Arcana Varia 0.8.0 ships four definitions under `data/arcanavaria/fundamentum/scythes/`. For example, `thaumium_scythe.json` contains:

```json
{
  "item": "arcanavaria:thaumium_scythe",
  "damage": 7,
  "reach": 4,
  "moves": {
    "sweet_spot": {},
    "backswing": {}
  }
}
```

The four files set damage and reach and name the available moves. The Void and Exanimator files also set `harvest_souls.heal_per_soul` to 1. The Elemental file maps `crescent_wave` to `sneak_use`. Copy the matching file and change the values you want to retune.
