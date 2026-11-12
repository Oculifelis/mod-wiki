# Unlocks (`com.fundamentum.unlock`)

"This player (or their team) has unlocked X": a level and the time it happened, for research trees, skill trees,
recipe gates, codex entries and the like. Same code on every version.

## Granting and checking

Any id works, declared or not:

    Unlocks.grant(player, FId.of("mymod", "smelting"));          // level 1, parents checked
    Unlocks.grant(player, FId.of("mymod", "smelting"), 3);       // raise to level 3
    Unlocks.has(player, id); Unlocks.level(player, id);           // player and team together
    Unlocks.revoke(player, id);
    Unlocks.all(player);                                          // id -> Entry(level, time)

A grant at or below the held level does nothing and returns false. Calls that take a player look at the player and
their team together; calls that take an `UnlockHolder` (`UnlockHolder.of(player)`, `Unlocks.team(player)`) look at that
holder alone. On the client, `Unlocks.client()` and `Unlocks.clientHas(id)` give the local player's view as the server
last sent it.

Player unlocks are saved on the player and kept through death; team unlocks are saved with the world.

## Declaring one

`data/<ns>/fundamentum/unlocks/<path>.json`, every field optional:

    {
      "name": "unlock.mymod.smelting",            translation key (default unlock.<ns>.<path>)
      "description": "unlock.mymod.smelting.desc",
      "icon": "minecraft:furnace",
      "hidden": false,                            hide from lists until held
      "team_shared": false,                       goes to the player's team when they have one
      "max_level": 1,                             0 for no cap
      "parents": ["mymod:fire"],                  needed first
      "grant": [ {"type": "advancement", "id": "minecraft:story/smelt_iron"},
                 {"type": "item", "id": "minecraft:furnace"} ]
    }

`grant` lists Fundamentum conditions (below); any one of them grants the unlock. They are checked for online players
once a second and at login, and again in the same check when one unlock grants another. `Unlocks.checkSources(player)`
runs the check by hand.

## Events

`UnlockEvent.Pre` (cancellable) and `Events.UnlockGranted` (cancellable) come before a grant is stored;
`UnlockEvent.Granted` after it, `UnlockEvent.Revoked` after a revoke. Each carries the player, the holder, the unlock and
the level. Ids: `fundamentum:unlock/pre`, `unlock/granted`, `unlock/revoked`.

## Teams

Scoreboard teams are built in (team key `vanilla/<team name>`). A team mod adds its own with
`Unlocks.registerTeams(provider)`; the one added last is asked first. A teammate sees the team's unlocks; leaving the
team drops them from the player's view.

## Conditions

`com.fundamentum.condition.Conditions` is a small JSON condition registry used by grant sources, stats and anything
else that wants it:

    {"type": "unlocked", "id": "mymod:smelting", "min": 2}
    {"type": "advancement", "id": "minecraft:story/mine_stone"}
    {"type": "item", "id": "minecraft:diamond", "count": 3}        carried in the inventory
    {"type": "vanilla_stat", "stat": "minecraft:custom", "value": "minecraft:jump", "min": 10}
    {"type": "all", "of": [...]}, {"type": "any", "of": [...]}, {"type": "not", "of": {...}}

A plain list means all of them. An unknown type is false. `Conditions.register(type, test)` adds more.

## Advancements

    "criteria": { "got": { "trigger": "fundamentum:unlocked", "conditions": { "id": "mymod:smelting", "min_level": 2 } } }

Without `id` any unlock counts. The trigger fires on every grant and again at login.

## Command

`/fundamentum unlock grant <players> <id> [level]`, `revoke <players> <id>`, `has <player> <id>`, `list <player>`.
Operators only. Commands skip the parent check.

## Test

`gradlew runServer -Punlocktest` (world under `run-unlocktest`) checks declarations, levels, parents, cancelling,
revoking, teams, conditions, grant sources, the trigger, the command and the save and sync codecs; it ends with
`UNLOCKTEST RESULT PASS` or `FAIL`.

## Not covered yet

FTB Teams and Argonauts guilds are not wired in; they can be added with `registerTeams`. There is no unlock screen yet.
