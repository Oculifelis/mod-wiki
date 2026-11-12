# Java API

For mod makers building on Fundamentum.

## Depending on it

Fundamentum publishes `com.fundamentum:fundamentum-neoforge:<version>+<minecraft>` (for example
`1.29.0+26.1.2`; `fundamentum-forge` on 1.20.1). Add the Maven repository it's published to, depend on the artifact,
and list `fundamentum` as a required dependency in your `neoforge.mods.toml`. Curios is required, so your dev runs
need Curios too.

```toml
[[dependencies.mymod]]
modId = "fundamentum"
type = "required"
versionRange = "[1.29.0,)"
ordering = "NONE"
side = "BOTH"
```

## Packages

Everything is under `com.fundamentum`. Register things while your mod is constructed.

### Data

| Class | What it's for |
|---|---|
| `data.DataTables` / `DataTable` | your own datapack tables: `DataTables.register(id, "mymod/weapons", WeaponDef::fromJson)` (or a Codec), then `.keyField("item")`, `.merge(DataTable.Merge.SHALLOW)`, `.builtins(...)`, `.synced()`, `.onLoad(...)`. Files merge in file-id order over the built-ins and each other; `DEEP` merge (the default) merges objects field by field and a `null` removes a field. Read with `get`, `entries`, `raw`, `number(key, field, fallback)` |
| `data.StatPatch` | ordered stat patches (tiers, upgrades): a field is a value or steps `{"set", "add", "multiply", "min", "max"}` |
| `item.ItemMatcher` | item id or `#tag` matching (one string or a list) for your data files |

### Combat

| Class | What it's for |
|---|---|
| `attribute.StatAttributes` | shared attributes on every living entity: `crit_chance`, `crit_damage`, `ranged_damage`, `fire_rate`, `reload_speed`, `ammo_conservation`, `armor_pierce`, `blast_radius`, `blast_self_damage`, `projectile_speed`, `spread`, `sickness_duration`, `wing_flight_time`. Fundamentum holds them; the mod that fires or explodes reads and applies them |
| `attribute.HealthCap` | max health up to 1,000,000 |
| `creature.CreatureTypes` | creature type tags and damage rules |
| `damage.Elements` | the elements, `<e>_damage` and `<e>_resistance` attributes; `Elements.add`, `Elements.variant(id, parent, ...)` for a variant that counts as its parent (soul fire is fire; `Element.parent()`, `isA`), `Elements.registerClassifier` for hits no tag can catch. From 1.26.0 datapacks add elements too (`damage.DataElements`, see [new elements](datapack/elements.md#new-elements)): `Element.fromData()`, `nameKey()`, `color()`, `displayName()`; a datapack element's `damage()` and `resistance()` attributes can be null |
| `api.SoulFire` | soul burning: `SoulFire.ignite(entity, ticks)`, `isSoulBurning(entity)`, `clear(entity)`; the tags `SOURCES`, `PROJECTILES`, `WEAPONS`. Call on the server; see [soul fire](datapack/elements.md#soul-fire) |
| `damage.DamageClasses` | melee, ranger, marksman, mage; `<c>_damage` attributes; `DamageClasses.add` |
| `damage.SharedDamage` | shared damage types (`fundamentum:fire`, `soul_fire` ... `arcane`, `fundamentum:bullet`); `SharedDamage.source(level, HOLY, projectile, shooter)` |
| `element.ElementAuras`, `ElementAffinities`, `ElementReactions`, `ElementRef` | auras on a creature, resolved affinities, the loaded reactions, parsing element strings |
| `element.ElementEvents` | events on `NeoForge.EVENT_BUS`: `Reaction` (cancellable, change the damage), `Reacted` (after it fired), `Affinity` (add resistance from code), `AuraApply` (cancellable) |
| `sickness.Sickness` | `isBlocked` and `trigger` for items with their own use logic |
| `trigger.Triggers` | left click as a trigger: implement `Triggers.Handler` (`press`, `hold`, `release`, `interrupted`) or `Triggers.register(...)` |

### Equipment

| Class | What it's for |
|---|---|
| `curios.Slots` | `Slots.equipped(entity, slot)`, `Slots.cosmetic(entity, slot)` |
| `wings.Wings` | wing flight and glide |
| `cosmetic.CosmeticArmor` | `CosmeticArmor.shown(player, slot)` for mods that draw armour themselves |
| `mount.Mounts`, `MountEntity` | mounts; `MountEntity` is a base class for custom mounts that walk, jump and fly |
| `hook.Hooks`, `HookModel` | grappling hooks and their texture layout |
| `summon.Summons` | summons; the `fundamentum:summon_damage` attribute scales minion hits |
| `whip.Whips` | cord whips: register an item with a `WhipDefinition` (tuning, style, slam, summon tag); `WhipHooks`, `WhipFx.beam` / `bolt`, `WhipTags.focus` and `minionHit` for your own minions |
| `arrow.Arrow3DRenderer` | `Arrow3DRenderer.of(ctx, texture)` gives your arrows the 3D look |

### Nights and skies

| Class | What it's for |
|---|---|
| `moon.Moons` | `addListener` (rise, set, while up, kills), `registerFlag`, `registerChance`, `registerSpawner`, `registerNight`, `registerSwitch`; `current`, `isUp`, `raise`, `clear`. Other moon JSON fields are yours through `Moon.json()` |
| `moon.NightEvents` | `addListener` (start, end with an outcome, while up, kills), `registerChance`; `start(level, id, pos)`, `current`, `isUp`, `pos`, `ticksLeft`, `raise`, `end(level, outcome)`, `clear` |
| `moon.MoonsClient` | client: `moon()`, `event()`, `fogMix(pt)`, `skyMix(pt)`, `fogColor()`, `skyColor()` for your own skies |
| `sky.FractalSkies` | the loaded fractal skies |

### Client and drawing

| Class | What it's for |
|---|---|
| `pose.Poses`, `PosePlayer`, `ArmPoses` | player poses and clips; `Poses.cue(entity, "cast")` on the server |
| `pose.FirstPersonHands` | first-person arms; register a `Frame` if you draw the item yourself |
| `glow.Glows` | `Glows.apply(target, rgb, ticks)`: a coloured glowing outline |
| `curve.Curve`, `curve.client.TubeMesh` | smooth curves between two ends, and textured tubes along them |
| `api.ItemHud` | `registerItem(item, (player, stack) -> lines)` or `register(predicate, provider)`: text lines drawn beside the hotbar while the item is held, placed and styled by the player's `fundamentum-hud-client.toml`. Asked once a client tick, never per frame; main hand first, then the off hand (1.25.7) |
| `client.Tooltips` | any item shows its lang lines `<item key>.desc`, `.desc2` and `.desc3` under its name |

`command.Tps` and `command.Showcase` are the [commands](commands.md). Not every package is on every version; see
[Versions](versions.md).
