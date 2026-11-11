# Player poses

*Fundamentum 1.28.0: Forge 1.20.1; NeoForge 1.21.1, 26.1.2, 26.2 and 26.3.* These are client resources, so they go in a resource pack, not a datapack.

## Item bindings

How players hold an item. **File:** `assets/<item ns>/player_pose/<item path>.json`. Every field is optional.

```json
{
  "arms": "support",
  "when": "always",
  "main": [-45, -25, 0],
  "support": [0, 0, 3],
  "hold": "mymod:greatsword_idle",
  "fire": "mymod:greatsword_slam",
  "cues": {"cast": "mymod:cast", "swing": ["mymod:swing_a", "mymod:swing_b"]},
  "first_person": {"arm": "grip", "grip": [0.4, -0.6, -1.2], "angles": [18, 30, 0], "swing": true}
}
```

| Field | Meaning |
|---|---|
| `arms` | third-person hold: `two_handed`, `bow`, `pistol`, `staff`, `support` (off hand on a point of the item), `spear`, `block` or `item`; no binding means vanilla's |
| `main` / `support` | the main arm's angles and the support hand's point on the item |
| `hold`, `fire`, `reload`, `charge` | clips to play in those states |
| `cues` | named clips the server starts with `Poses.cue(entity, "cast")` |
| `rest` | the clip between actions |
| `first_person` | the player's own arms in first person (below) |

### First-person arms

| Field | Meaning |
|---|---|
| `arm` | `grip` (fist on a handle), `palm` (open hand under a floating item), `gun` / `wand` (fist on a grip frame) or `none` |
| `grip` | pixels in the held item's frame |
| `angles` | degrees: pitch up, yaw inward, roll |
| `fist_in`, `swing` | fine-tuning |
| `support` | the other hand, drawn while the off hand is empty (same fields) |

## Clips

Blockbench or GeckoLib animations at `assets/<ns>/player_anim/<name>.json`, with bones `right_arm`, `left_arm` and
`first_person` (which moves the item and arms together).
