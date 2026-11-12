# Ecosystem events (`com.fundamentum.event`)

Shared events so mods can react to each other without depending on each other: spells, bosses, rituals, quests,
reputation, machines and more. Same code on every version.

## Events are records

Each event is a Java record with a fixed id `fundamentum:<name>` (see `Events` for the 47 in this release: `spell_cast`,
`boss_killed`, `quest_completed`, `rep_changed`, `ritual_started`, `first_join`, `dimension_entered`, `effect_applied` ...).
The climate, food, unlock and config packages add a few more of their own (below).
Some can be cancelled (`spell_cast`, `ritual_started`, `entity_tamed`, ...), most only announce.

    // a mod that does the thing posts it; true means a listener cancelled it
    if (FEvents.post(new Events.SpellCast(caster, FId.of("mymod", "fireball"), 20))) return;

    // anyone listens, by class or by id
    FEvents.listen(Events.BossKilled.class, e -> ...);
    FEvents.listen(Events.SpellCast.class, (e, call) -> { if (silenced(e.caster())) call.cancel(); });
    FEvents.listen(FId.of("fundamentum", "quest_completed"), (e, call) -> ...);

Listeners run in the order they were added. A cancel stops the later ones; cancelling an event that cannot be cancelled
does nothing. New types: `FEvents.register(FId.of("mymod", "thing"), Thing.class, cancellable)`, ids are never reused.

## Who posts what

Fundamentum's own systems post the events that belong to them. The rest (spells, machines, quests, rituals, taming,
reputation, devotion, structures) are for the mods that own those things to post.

| System | Events | Cancel does |
|---|---|---|
| Players | `first_join` (once per player; someone already playing for over 10 seconds when Fundamentum was added is skipped), `dimension_entered` | |
| Config | `config_changed` | |
| Bosses | `boss_spawned` (first start only, not chunk reloads), `boss_phase_changed` (phases count from 1, 0 is the base phase), `boss_killed` (`killer` is null when no player landed the blow) | |
| Boss loot | `boss_loot_dropped` (per player, or once with a null player for a shared drop) | |
| Loot additions | `loot_added` (table, addition, stacks) | leaves those stacks out |
| Shields | `shield_blocked` (after a real block, with the damage stopped) | |
| Status effects | `effect_applied`, `effect_tick` (each tick of each custom effect), `effect_ended` (`expired`, `cured` or `removed`) | refuses the effect, skips that tick |
| Armour sets | `set_bonus_on` (per tier gained), `set_bonus_off` (last tier lost), players only | |
| Ammo | `ammo_drawn` | keeps the ammo; the shot still goes off |
| Thrown weapons | `thrown_weapon_hit` | the hit does no damage |
| Wings | `wings_take_off` | the server keeps the wings folded (the client still glides until it lands) |
| Mana | `mana_spent` | keeps the mana; the spend fails |
| Summons and sentries | `summon_created` | the summon never appears |
| Relics | `relic_placed`, `relic_broken` | stops the placing |
| Slots | `slot_equipped`, `slot_unequipped` (entity, slot, index, cosmetic, stack), through Curios ([Slots](slots.md)) | |
| Stats | `stat_changed` | |
| Unlocks | `unlock_granted`, plus `unlock/pre`, `unlock/granted`, `unlock/revoked` ([Unlocks](unlocks.md)) | `unlock_granted` and `unlock/pre` stop the unlock |
| Unify | `material_unified` | |
| Multiblocks | `multiblock_formed`, `multiblock_unformed` | stops the forming |
| Climate | `season_changed` (`SeasonChanged(from, to, day)`; `from` or `to` is null when seasons turn on or off) ([Climate](climate.md)) | |
| Food | `food_eaten`, `food_consumed` ([Food](food.md)) | `food_eaten` stops the eating |
| Survival meters | `meter_threshold` (a threshold starts or stops holding: where a meter starts or stops hurting) | |
| Music | `music_changed` (the track the server expects, worked out when the music state changes) | |
| Moons and night events | `moon_rose`, `moon_set`, `night_event_started`, `night_event_ended` | |
| Elements | `element_reacted` | |

Item transfer (pipes and machine IO) posts nothing: it moves items every tick, and an event per move would flood every
listener. Machines built on it post `machine_processed` instead.

## On the loader's bus

Every event that was not cancelled is also posted on the loader's event bus as `FundamentumEvent` (and
`FundamentumEvent.Cancellable` for the cancellable ones), so `@SubscribeEvent` code works: `e.id()`, `e.as(SpellCast.class)`,
`setCanceled(true)`.

## Fields and conditions

`FEvents.describe(event)` gives the fields as plain JSON (entities as their type, ids as text). `FEvents.matches(event,
where)` checks a JSON condition: exact values, `{"min": .., "max": ..}`, a list of allowed values, `null` for an empty
field; a field the event lacks never matches, and `minecraft:` may be left out.

## Advancements

The trigger `fundamentum:event` completes when an event about the player fires and was not cancelled:

    "criteria": { "done": { "trigger": "fundamentum:event", "conditions": {
        "event": "fundamentum:quest_completed", "where": { "quest": "mymod:first_steps" } } } }

The player is the event's first player field, and `player` takes the usual entity conditions (they are checked
against that player). Fake players never earn these (the loader keeps advancements from them).

## Test

`gradlew runServer -Peventtest` (world under `run-eventtest`) checks the types, listening, cancelling, the loader bus,
conditions, config events, first join, the trigger (player conditions included) and that every event above is
registered, with a small test datapack; it ends with `EVENTTEST RESULT PASS` or `FAIL`. The systems tests
(`-Psystemstest`, `-Psystems2test`) and the system's own tests check that each system really posts its events.
