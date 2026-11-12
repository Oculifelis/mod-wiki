# Survival meters (`com.fundamentum.survival`)

Thirst, body temperature, stamina and the like, as datapack files. A meter is a player stat that drains or fills by
rules, hurts or slows the player past set limits and can show on the HUD. The same code runs on every version.
Fundamentum ships no meters, so nothing happens until a mod or pack adds one.

## A meter

`data/<namespace>/fundamentum/survival/<name>.json`:

    {
      "min": 0, "max": 20,
      "start": 20,
      "respawn": 15,
      "rules": [
        {"amount": -0.05},
        {"amount": -0.1, "when": "sprinting"},
        {"amount": -0.2, "when": [{"type": "climate", "value": "temperature", "min": 1.5}]}
      ],
      "consume": [{"items": ["minecraft:potion", "#c:drinks"], "amount": 6}],
      "drink_blocks": [{"blocks": ["minecraft:water"], "amount": 2}],
      "thresholds": [
        {"below": 6, "effect": "minecraft:slowness", "amplifier": 0},
        {"at_most": 0, "damage": 1, "interval": 4}
      ],
      "hud": {"style": "bar", "color": "#3F76E4", "side": "right"}
    }

| Field | Means | Default |
|---|---|---|
| `stat` | the stat that holds the value | the meter's own id |
| `min`, `max` | the range; values never leave it | 0, 20 |
| `start` | a new player's value | `max` |
| `respawn` | the value after death | `start` |
| `reset_on_death` | false keeps the value through death | true |
| `creative` | true runs it for creative and spectator players too | false |
| `rules` | drain and fill, applied once a second in order | none |
| `consume` | items that change it when eaten or drunk | none |
| `drink_blocks` | blocks a player drinks from with an empty hand | none |
| `thresholds` | effects and damage past a limit | none |
| `hud` | how it shows | not shown |
| `disabled` | a pack turns the meter off by overriding the file | false |

The value is an ordinary stat (see [Stats](stats.md)), so `Stats.get`, stat conditions, the stat tooltip and
`fundamentum:stat_changed` all work on it. Declare the stat too when it should have its own name or number format.
A broken file is left out and the log says why.

## Rules

Every second each rule whose `when` holds adds its `amount`. The server works the meters out in steps of
`survival_step_seconds` (1 by default, see [Performance](performance.md)); a longer step does the same seconds of
change at once. `when` can be:

- an activity name: `sprinting`, `swimming`, `sneaking`, `moving`, `still`, `in_water`, `underwater`, `in_rain`,
  `on_fire`, `in_lava`, `sleeping`
- any condition object (see [Unlocks](unlocks.md) for the condition types)
- a list of these, which must all hold

Two condition types come with meters and work anywhere conditions do:
`{"type": "activity", "is": "sprinting"}` (or a list) and
`{"type": "climate", "value": "temperature", "min": 0.2, "max": 1.0}` (`value` is `temperature` or `humidity`).

A climate rule follows the weather instead of adding a fixed amount:

    {"type": "climate", "value": "temperature", "scale": 50, "offset": 10, "rate": 0.1}

Each second the value moves `rate` of the way toward `reading * scale + offset`, where the reading comes from
[Climate](climate.md) at the player's feet (biome, season, height, heat and cold blocks, rain). That makes a body
temperature that warms near lava and cools in snow without any code.

## Eating, drinking and water

`consume` entries match item ids and `#` item tags. They apply when the player finishes eating or drinking, through
the food hooks ([Food](food.md)), so a cancelled eat changes nothing.

`drink_blocks` lets a player right-click a block or fluid with an empty hand to drink (fluids by their block, like
`minecraft:water`). The client asks only when it is looking at something a meter accepts, and the server checks
again. Every matching meter that isn't full goes up. There is a half-second wait between drinks.

## Thresholds

Each threshold has one of `below`, `above`, `at_most` or `at_least` with a limit. While it holds:

- `effect` (with `amplifier`, and `duration` in ticks, default 60) is kept on the player.
- `damage` hurts the player every `interval` seconds (default 2) with `damage_type`. With no `damage_type` it uses a
  damage type with the meter's own id, then `fundamentum:<the meter's name>`, then `fundamentum:meter`. Fundamentum ships
  `thirst`, `overheating`, `hypothermia`, `exhaustion` and `meter`, each with its own death message. They skip armor,
  effects and knockback, and are in the tag `#fundamentum:meter_damage`.

Crossing into or out of a threshold posts `fundamentum:meter_threshold` ([Events](events.md)).

A file with a threshold missing its limit is refused.

## Death

Meters stand still while a player is dead. On respawn each meter with `reset_on_death` (the default) goes to its
`respawn` value; the others keep theirs.

## HUD

    "hud": {"style": "bar", "color": "#3F76E4", "side": "right", "label": "meter.mymod.thirst", "order": 0}

`style` is `bar`, `text` or `none` (default `bar` once there is a `hud` object). Meters stack upward above the
hotbar, over the hunger bar (`right`, the default) or over the hearts (`left`), by `order` and then id. A text meter
shows its label and value. With no translation for `label` the name comes from the id, so `mymod:body_temperature`
reads "Body Temperature". The layers are `fundamentum:survival` (right) and `fundamentum:survival_left`, so a player can
move, scale or hide them in the HUD editor (see [Hud](hud.md)). The rows are rebuilt only when a meter value or a
declaration changes.
It is hidden in creative and spectator.

## In code

    Meter thirst = Survival.meter(FId.of("mymod", "thirst"));
    double v = Survival.get(player, thirst);
    Survival.add(player, thirst, 4);          // kept inside the range
    Survival.evaluate(serverPlayer);          // one second of rules, for players the server doesn't tick

## Command

`/fundamentum survival` (operators) lists your value for every meter. The result is the number of meters.

## Test

`gradlew runServer -Psurvivaltest` (world under `run-survivaltest`) checks loading with broken and disabled files
left out, start values, rules with activities and conditions, the climate rule, threshold effects and damage,
drinking items and water, death resets, the client sync, the HUD layout and the command. It ends with
`SURVIVALTEST RESULT PASS` or `FAIL`.
