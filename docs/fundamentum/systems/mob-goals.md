# Mob goals (`com.fundamentum.mobgoal`)

Ready-made goals for vanilla-style mobs, handed out by datapack. A pack names a mob (or an entity tag), a goal and a
priority, and every matching mob gets that goal when it joins the world. The same code runs on every version.

Mobs that run on a brain (villagers, piglins, hoglins, axolotls, wardens and the like) are left alone: their goal
selectors don't drive them, so adding goals there would do nothing or fight the brain. `MobGoals.brainDriven(mob)`
tells you which is which.

## Data

`data/<namespace>/fundamentum/mob_goals/<name>.json`, one entry or a list:

    {"entity": "minecraft:zombie", "goal": "fundamentum:kite", "priority": 2, "params": {"min": 5, "max": 9}}

    {
      "entity": "#minecraft:skeletons",
      "goals": [
        {"goal": "fundamentum:ranged_ammo", "priority": 2, "params": {"ammo": "#minecraft:arrows"}},
        {"goal": "fundamentum:call_allies", "priority": 3}
      ]
    }

`entity` is an entity id, or `#` and an entity tag. An entry in `goals` may carry its own `entity`. `priority`
defaults to 3 (lower runs first, as in vanilla). A file with an unknown goal or a bad entry is skipped whole and the
log says why. Reloading (`/reload`) swaps the goals on every loaded mob.

`"phases": ["enraged", "two"]` makes the goal run only while the mob is a boss (see Bosses) in one of those phases.
It stops when the phase changes.

## Goals

| Id | Does | Params (defaults) |
|---|---|---|
| `fundamentum:kite` | backs away from a target that comes too close | `min` 6, `max` 10, `speed` 1.2 |
| `fundamentum:strafe` | circles the target, switching direction now and then | `radius` 6, `speed` 0.6, `switch_ticks` 60 |
| `fundamentum:leap` | jumps at the target from the ground | `min` 2, `max` 6, `cooldown` 40, `horizontal` 0.5, `vertical` 0.4, `chance` 0.2 |
| `fundamentum:charge` | runs straight at the target and hits once on contact | `min` 4, `range` 12, `speed` 0.6, `duration` 30, `cooldown` 100 |
| `fundamentum:flee_low_health` | runs from its target or attacker when hurt badly | `health` 0.25 (share of max), `speed` 1.4, `distance` 16 |
| `fundamentum:call_allies` | when hurt, allies nearby with no target turn on the attacker | `radius` 16, `max` 8 |
| `fundamentum:guard` | stays near a point and walks back when it strays; drops targets past its leash | `pos` [x, y, z] (where it spawned), `radius` 8, `leash` radius x 2, `speed` 1 |
| `fundamentum:follow_leader` | follows the oldest allied mob nearby, so groups move as a pack | `min` 3, `max` 8, `range` 16, `speed` 1 |
| `fundamentum:ranged_ammo` | shoots its target, using up ammo it carries (hands, then quiver) | `ammo` "#minecraft:arrows" (tag or item), `interval` 40, `range` 15, `power` 1, `speed` 1 |
| `fundamentum:faction_target` | a target goal: picks the nearest mob the faction hook calls hostile | `range` 16, `interval` 10, `sight` true |

`kite`, `flee_low_health`, `guard` and `follow_leader` need a mob that can path (a `PathfinderMob`); other mobs skip
them. `ranged_ammo` finds ammo with `Ammo.find` and takes it with `Ammo.consume`, so a mob with no arrows stops
shooting. Mobs that already shoot (skeletons, pillagers) fire through their own ranged attack; for others, add a
shooter (below).

## From code

    MobGoals.register(FId.of("mymod", "burrow"), false, (mob, params) -> new BurrowGoal(mob, params.d("depth", 2)));
    MobGoals.addShooter((mob, target, ammo, power) -> ammo.is(MyItems.SPEAR.get()) && throwSpear(mob, target, power));
    MobGoals.setFactions(new FactionHook() {
        @Override public boolean hostile(Mob self, LivingEntity other) { return MyFactions.atWar(self, other); }
        @Override public boolean allied(Mob self, LivingEntity other) { return MyFactions.same(self, other); }
    });

A factory may return null to skip a mob. `true` as the second argument puts the goal in the target selector.
Shooters are tried newest first; one that returns true has fired and the ammo is used up.

Fundamentum has no factions. The default hook calls nothing hostile and calls mobs of the same type allies, so
`faction_target` does nothing until a faction mod sets a hook, and `call_allies` and `follow_leader` work within
one mob type. `setFactions(null)` puts the default back.

`MobGoals.added(mob)` lists what was added to a mob, `apply(mob)` adds the goals again (it takes the old ones off
first) and `remove(mob)` takes them off.

## Command

`/fundamentum mobgoals` counts the loaded entries per mob; `/fundamentum mobgoals <mob>` lists what one mob got.

## Test

`gradlew runServer -Pgoaltest --no-daemon` runs `src/goaltest/java/com/fundamentum/mobgoal/MobGoalSelfTest.java` (the same
file on every version) in `run-goaltest/`. It prints `GOALTEST PASS|FAIL` lines and `GOALTEST RESULT PASS|FAIL`.
