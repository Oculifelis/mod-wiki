# Use sickness

Terraria-style potion sickness: using a matching item gives an effect, and while it lasts every item under rules with
the same effect can't be used (an action-bar message says why). Fundamentum assigns no items itself.

**File:** `data/<ns>/fundamentum/sickness/<name>.json`

```json
{"items": ["#mymod:healing_potions", "mymod:elixir"], "effect": "fundamentum:potion_sickness", "duration": 1200, "trigger": "finish"}
```

| Field | Default | Meaning |
|---|---|---|
| `items` | required | items and `#tags` |
| `duration` | required | ticks; scaled by the user's `fundamentum:sickness_duration` attribute |
| `effect` | `fundamentum:potion_sickness` | any mob effect; a mod may use its own (a mana sickness, say) |
| `trigger` | `finish` | `finish` (after drinking or eating) or `use` (on right click, for instant items) |

Ostentum's apple sickness is one of these: a minute of sickness after an enchanted golden apple.
