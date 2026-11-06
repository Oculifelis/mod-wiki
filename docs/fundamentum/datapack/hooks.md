# Grappling hooks

Hook items go in the Curios `hook` slot (item tag `#curios:hook`). The hook key (default **H**) fires a hook where the
player looks. It latches onto the first block it meets, pulls the player there and holds them; jumping lets go.
Firing again adds hooks up to the item's `count` (the oldest goes first). A latched player takes no fall damage.

**File:** `data/<ns>/fundamentum/hooks/<name>.json`, keyed by `item`. Every field is optional.

```json
{
  "item": "mymod:ivy_hook",
  "range": 18,
  "shoot_speed": 1.5,
  "pull_speed": 0.7,
  "count": 1,
  "texture": "mymod:textures/entity/ivy_hook.png",
  "still": false,
  "air_seconds": 0
}
```

| Field | Default | Meaning |
|---|---|---|
| `item` | the file id | the hook item |
| `range` | 18 | blocks |
| `shoot_speed` | 1.5 | blocks per tick |
| `pull_speed` | 0.7 | blocks per tick |
| `count` | 1 | hooks out at once |
| `texture` | Fundamentum's | repaints the hook and chain, in the layout of `fundamentum:textures/entity/hook/hook.png` |
| `still` | false | holds the player exactly between the latched hooks, without the usual give (two hooks on facing walls hang them in the air) |
| `air_seconds` | 0 | above 0, a hook that reaches its range without meeting a block anchors in the air there for that long |
