# For pack makers

The kilns have no recipe list in their code. Everything they make comes from one recipe type, `slowlight:ageing`, so a
datapack or a KubeJS script can add, change or remove any of it.

## The recipe

```json
{
  "type": "slowlight:ageing",
  "ingredient": { "item": "minecraft:honey_bottle" },
  "result": { "id": "slowlight:mead", "count": 1 },
  "days": 2
}
```

Drop it into `data/<your pack>/recipe/` and every kiln can make it. `days` counts on the world's game time (24000
ticks to a day), so a slept night doesn't cheat the wait, and nothing is lost while the chunk is unloaded.

These fields are optional:

| Field | What it does |
|---|---|
| `long_days` | the Long Kiln's own wait for a whole stack. Without it the Long Kiln takes `days` × 3. (The Ember Kiln always takes half of `days`.) |
| `cellar_days` | Faster ageing time in a dark cellar, for recipes that specify it. |
| `condition` | the days count only while it holds. Every part of it is optional, as below. |

The parts of `condition`:

| Field | Values | Notes |
|---|---|---|
| `sky` | `open`, `covered` | open sky above the kiln, or a roof over it |
| `weather` | `clear`, `rain`, `thunder` | rain and thunder count only where rain actually falls on the kiln |
| `time` | `day`, `night` | |
| `moon` | full, new | Only counts at night under the specified phase. |
| `climate` | cold | Requires a cold biome. |
| `light` | dark | Requires a dark kiln location. |
| `dimension` | a dimension id, such as `minecraft:the_nether` | see below |

```json
"condition": { "sky": "open", "time": "night" }
```

`dimension` works differently from the rest: a recipe that names one only exists in that dimension, and there it comes
before a recipe for the same item that names none. That's how cobblestone turns mossy in the Overworld but to
blackstone in the Nether.

To take a recipe away, override its file with your own (Slowlight's are in `data/slowlight/recipe/ageing/`), or remove
it with KubeJS.

## KubeJS

Two ways work, and neither needs anything from Slowlight beyond the mod itself:

```js
// Works because the recipe type has a codec. No schema needed.
ServerEvents.recipes(event => {
  event.custom({
    type: 'slowlight:ageing',
    ingredient: { item: 'minecraft:rotten_flesh' },
    result: { id: 'minecraft:leather' },
    days: 3
  })
  event.remove({ type: 'slowlight:ageing', output: 'slowlight:mead' })
})
```

```js
// Works because a recipe schema ships as a data file
// (data/slowlight/kubejs/recipe_schema/ageing.json).
ServerEvents.recipes(event => {
  event.recipes.slowlight.ageing('4x minecraft:bone_meal', 'minecraft:rotten_flesh', 2)
})
```

The schema is a data file, not a plugin, so Slowlight has no compile-time dependency on KubeJS and nothing goes wrong
when it isn't installed.

## On other versions

| Version | What differs |
|---|---|
| 1.20.1 | recipes go in `data/<your pack>/recipes/` (plural), and results are written `{"item": ..., "count": ...}` (Slowlight's ageing recipes accept `"id"` too). [KubeJS](https://www.curseforge.com/projects/238086) 6 has no recipe schemas, so only `event.custom` and `event.remove` work; `event.recipes.slowlight.ageing` doesn't exist there. |
| 26.1.2, 26.2, 26.3 | ingredients can be a plain item id. There's no KubeJS build for 26.2 or 26.3 yet. |

See [Versions](versions.md) for everything else that differs.

## Tags

| Tag | What it does |
|---|---|
| `#slowlight:pressable` | what the Flower Press takes. It includes `#minecraft:flowers` and `#c:flowers`, so most modded flowers already work; add to it for anything else. |
