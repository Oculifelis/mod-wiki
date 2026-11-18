# Weight

Weight is off by default and has two parts, each with its own switch in `config/fundamentum/weight.toml`.

- Equipment load (`equipment_load`) weighs worn armour and held items against the `fundamentum:load_capacity`
  attribute. A light, medium or heavy load scales [dodge](dodge.md) distance, the dodge's invulnerable window and its
  hunger cost.
- Inventory weight (`inventory_weight`) weighs everything carried against `fundamentum:carry_capacity`. Each overload
  step slows walking and lowers jumps. Nothing is ever blocked, and walking and jumping always keep at least a tenth.

`count_containers` (on by default) decides whether shulker box, bundle and backpack contents count. The client picks a
bar or a row of weight icons for the meter.

## Item weights

`data/<ns>/fundamentum/item_weights/<name>.json` sets weights by item or tag. An exact item wins over a tag.

```json
{"values": {"minecraft:anvil": 15, "minecraft:obsidian": 2, "#c:ingots": 0.5}}
```

## Rules

Items with no weight of their own fall back to the rules in `data/<ns>/fundamentum/weight_rules/default.json`, which
also hold the load and overload steps. The file with id `fundamentum:default` is used, or the first one by id when that
is missing. A pack replaces the rules by shipping its own `data/fundamentum/fundamentum/weight_rules/default.json`.
This is the shipped file:

```json
{
  "default_item": 0.05,
  "default_block": 0.25,
  "armor": {"per_point": 1.5, "per_toughness": 2.0},
  "load": {
    "steps": [
      {"name": "light", "below": 0.34, "distance": 1.0, "iframes": 1.0, "cost": 1.0},
      {"name": "medium", "below": 0.67, "distance": 0.85, "iframes": 0.85, "cost": 1.3},
      {"name": "heavy", "distance": 0.65, "iframes": 0.65, "cost": 1.75}
    ]
  },
  "inventory": {
    "steps": [
      {"over": 1.0, "speed": -0.1, "jump": -0.1},
      {"over": 1.25, "speed": -0.25, "jump": -0.25},
      {"over": 1.5, "speed": -0.45, "jump": -0.5}
    ]
  }
}
```

| Field | Default | Meaning |
|---|---|---|
| `default_item` | 0.05 | weight of an item with no entry |
| `default_block` | 0.25 | weight of a block item with no entry |
| `armor.per_point` | 1.5 | armour weight per armour point |
| `armor.per_toughness` | 2.0 | armour weight per point of toughness |
| `load.steps` | light, medium, heavy | each step applies below its `below` share of load capacity (no `below` means any load) and multiplies dodge `distance`, `iframes` and `cost` |
| `inventory.steps` | three steps | over its `over` share of carry capacity, walking `speed` and `jump` change by these fractions (clamped to between -0.9 and 0) |

Steps are sorted by `below` or `over`, so their order in the file does not matter. An `inventory` object with no steps
turns the overload penalties off.
