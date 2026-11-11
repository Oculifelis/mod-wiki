# Portal crafting

*Fundamentum 1.28.0: Forge 1.20.1; NeoForge 1.21.1, 26.1.2, 26.2 and 26.3.*

An item thrown through a portal (Nether, End, End gateway, or a modded portal that teleports the usual way) that
matches a recipe changes in place instead of travelling, and is pushed back out.

**File:** `data/<ns>/recipe/<name>.json`

```json
{
  "type": "fundamentum:portal_crafting",
  "ingredient": "mymod:ender_whip",
  "result": {"id": "mymod:end_rift_whip", "count": 1},
  "portal": "minecraft:end_portal",
  "dimension": "minecraft:the_end",
  "keep_components": true
}
```

| Field | Default | Meaning |
|---|---|---|
| `ingredient` | required | a normal recipe ingredient |
| `result` | required | an item stack |
| `portal` | any | a block, a list of blocks or a `#tag` |
| `dimension` | any | where the portal leads |
| `keep_components` | false | keep the thrown item's enchantments, damage and name |

A stack makes count x n results, in full stacks. With Architect's Palette installed, items its `warping` recipes take
are left to it. JEI, if installed, shows a Portal Crafting category.
