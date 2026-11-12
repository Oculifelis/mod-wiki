# Stats (`com.fundamentum.stat`)

Named numbers on players, mobs and item stacks: strength, crit chance, play time, a sword's sharpness. Each one is
stored, or read from somewhere else (an attribute, mana, an unlock, a vanilla statistic, a score). Same code on every
version.

## Reading and writing

    Stats.get(player, FId.of("mymod", "strength"));
    Stats.set(entity, id, 12);  Stats.add(entity, id, 1);
    Stats.get(stack, id);  Stats.set(stack, id, 40);           // item stats live on the stack
    Stats.format(id, value);                                   // "50%", "1:05", "2.5"

An undeclared id is a stored number with no limits, on any living entity. Item stats read through an entity use the
stack in its main hand. Writes are clamped to the stat's `min` and `max`; computed stats cannot be written (`set`
returns false), except scoreboard ones.

## Declaring one

`data/<ns>/fundamentum/stats/<path>.json`, every field optional:

    {
      "name": "stat.mymod.strength",     translation key (default stat.<ns>.<path>)
      "icon": "minecraft:iron_sword",
      "type": "number",                  number, percent (0..1 shown as %), time (ticks shown as m:ss) or count
      "scope": "player",                 player, entity (any living entity) or item (on the stack)
      "default": 0, "min": 0, "max": 100,
      "format": "%.1fx",                 optional Java format for the number
      "hud": true,                       shown on the stats HUD layer
      "tooltip": true,                   shown in item tooltips (item scope; on by default there)
      "source": {"type": "stored"}
    }

## Sources

    {"type": "stored"}                                       saved on the entity or stack (the default)
    {"type": "attribute", "id": "minecraft:max_health"}      the attribute's current value
    {"type": "mana", "pool": "mymod:mana", "value": "max"}   pool optional; value current or max
    {"type": "unlock", "id": "mymod:smelting"}               the unlock level
    {"type": "vanilla_stat", "stat": "minecraft:custom", "value": "minecraft:jump"}
    {"type": "scoreboard", "objective": "kills"}             the entity's score; can be set

`"source": "attribute"` works as a short form when the source needs no fields. An unknown source type reads as stored.
Mods add their own:

    Stats.registerSource("mymod:level_power", (def, entity, stack) -> entity == null ? 0 : power(entity));

## Events

`Events.StatChanged(entity, stat, from, to)` is posted on every entity write that changes the value. Computed player
stats post it from a check once a second. Item stack writes post nothing.

## Client

Players get the declarations and their values synced. The `fundamentum:stats` HUD layer (see HudLayers) lists stats
marked `hud`; the Stats Screen key (unbound by default, under Fundamentum in Controls) opens a page of all of them;
item stats with `tooltip` show on the item's tooltip.

## Condition

    {"type": "stat", "id": "mymod:strength", "min": 5, "max": 20}

Either end is optional. Works anywhere Fundamentum conditions are used (unlock grant sources, for one).

## Command

`/fundamentum stat get <target> <id>`, `set <targets> <id> <value>`, `add <targets> <id> <amount>`. Operators only.
`get` returns the value rounded down, for `execute store`.

## Test

`gradlew runServer -Pstattest` (world under `run-stattest`) checks stored stats, clamping, every source, formats, item
and mob stats, tooltips, the condition, the command, the change event and the codecs; it ends with
`STATTEST RESULT PASS` or `FAIL`.
