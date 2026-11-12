# The version-neutral layer (`com.fundamentum.port`)

Fundamentum ships for NeoForge 26.1.2, 26.2, 26.3, NeoForge 1.21.1 and Forge 1.20.1. The classes in
`com.fundamentum.port` have the same names and signatures in all five, so a file written only against them (and
against vanilla names that did not change) can be copied between the five source trees unchanged. The test
`src/porttest/java/com/fundamentum/port/PortSelfTest.java` is such a file: it is byte-identical in every tree.

Run it with `gradlew runServer -Pporttest --no-daemon` (a dedicated server in `run-porttest/`). It prints one
`PORTTEST PASS|FAIL` line per check and ends with `PORTTEST RESULT PASS|FAIL`, then stops the server.

## What is in it

| Class | Use | 26.x | 1.21.1 | 1.20.1 |
|---|---|---|---|---|
| `FId` | ids (`FId.of("ns:path")`, `vanilla()`) | `Identifier` | `ResourceLocation` | `ResourceLocation` |
| `FStreamCodec<T>` | network codecs, `composite` up to 6 fields, `list`, `optional`, `map` | over `FriendlyByteBuf` | same | same |
| `FAttach<T>` | data on entities, chunks, levels, block entities; codec, `copyOnDeath`, sync `NONE/OWNER/TRACKING` | attachment types | attachment types | a capability holding all values, own sync over `FNet` |
| `FLevelData<T>` | data saved per dimension | `SavedDataType` | `SavedData.Factory` | `SavedData` with a load function |
| `FStackData<T>` | a typed value on an item stack | data component | data component | tag `"ns:path"` in the stack NBT |
| `FNet` | `register`, `toPlayer`, `toTracking`, `toTrackingAndSelf`, `toAll`, `toServer`; handlers on the main thread | payloads | payloads | one `SimpleChannel` |
| `FReg` | blocks, items, block items, entity types, effects, sounds, anything else; returns a `Ref` | ids put into properties and builders for you | | |
| `FTags` | tag keys by id, `FTags.is(entityType, tag)` | | | |
| `FVanilla` | renamed vanilla calls: hurt, hurt cooldown, damage sources, attributes, enchantments, custom data, effects, sounds, particles, registry lookups, creating entities by type or id, entity/block entity/stack save and load, fake players, `testPlayer` (a bare player that earns advancements, for tests), saving the world, `isOp`, `configDir`, `playTime`, `statValue` (a vanilla statistic by type and id), `score` and `setScore` (scoreboard) | | | |
| `FCommands` | `listen` (add commands on every command rebuild), `op()` (operator check), `id()` and `getId` (a namespaced id argument) | `IdentifierArgument`, `Commands.hasPermission` | `ResourceLocationArgument`, `hasPermission(2)` | same, on the Forge bus |
| `FLife` | server about to start / started / stopping / stopped, server tick, player logged in, dimension changed, `jsonData` (a datapack folder read on every reload, every pack's copy) | | | |
| `FTransfer` | energy and fluid capabilities behind `com.fundamentum.transfer` (lookups, exposing our buffers and tanks, fluid ids) | `Capabilities.Energy/Fluid.BLOCK`, transactions with snapshot journals | `Capabilities.EnergyStorage/FluidHandler.BLOCK` | `ForgeCapabilities.ENERGY/FLUID_HANDLER` attached to block entities |
| `FMobs` | mobs joining a server level (`joined`), whether a mob runs on a brain (`brainDriven`), a mob's own melee hit (`hurtTarget`), for `com.fundamentum.mobgoal` | `EntityJoinLevelEvent`, `Brain.isBrainDead`, `doHurtTarget(ServerLevel, Entity)` | `EntityJoinLevelEvent`, active brain activities, `doHurtTarget(Entity)` | the same on the Forge bus |
| `FClimate` | crop growth hooks (`cropRule`, `cropGrown`), biome and dimension ids, biome lookup, rainfall, `modLoaded`, for `com.fundamentum.climate`; `FClimateClient.refreshTints` redraws chunks after a tint change | `CropGrowEvent.Pre/Post`, `Identifier`, `levelExtractor.allChanged()` on 26.2 and 26.3 | `CropGrowEvent.Pre/Post`, `ResourceLocation` | `BlockEvent.CropGrowEvent` with `Event.Result` on the Forge bus |

Make every `FAttach`, `FStackData`, `FReg` entry and `FNet` message while the mod is constructed (static fields).
After the loader has taken them, making another throws, with a message that says so.

Where vanilla constants changed type between versions (effects, attributes and sounds became holders in 1.21,
enchantments became data), `FVanilla` has one overload per type, so `FVanilla.addEffect(e, MobEffects.REGENERATION,
100, 0)` and `FVanilla.enchant(level, stack, Enchantments.SHARPNESS, 3)` read the same everywhere. Ids that vanilla
renamed (attribute `generic.max_health` became `max_health` in 1.21.2) are not hidden; use the constant or try both.

## What it cannot hide

These still differ per version, and files that touch them stay per version:

- **Rendering.** Model, renderer and shader APIs change in every release (26.x moved entity rendering to render
  states and submit lists). Client code is not covered at all.
- **Mixins.** They name vanilla methods and fields by their exact signatures, which change between versions.
- **Screens and GUI.** `GuiGraphics`, widget and menu screen APIs differ; so do key mappings and overlays.
- **Data-driven formats.** Worldgen JSON (biomes, features, noise), enchantment definitions, loot tables, recipes,
  advancements and their folder names (`recipes/` vs `recipe/`) differ. Data generators differ too.
- **Loader events and registration timing.** Event classes, their buses and their names differ (Forge
  `AttachCapabilitiesEvent`, NeoForge `RegisterEvent` timing, 26.x events split in two). The layer listens to what it
  needs itself; anything else still subscribes per version.
- **Vanilla constants that moved.** 26.2 moved the entity type constants from `EntityType` to `EntityTypes`, so
  `EntityType.ZOMBIE` is per version from 26.2 on; look types up by id (`FVanilla.entityType(FId.of("zombie"))`,
  `FVanilla.create(FId.of("zombie"), level)`) in shared files.
- **Class and method names in your own code.** Java has no type aliases, so a file that names `ResourceLocation` or
  `Identifier`, `Holder<MobEffect>` or `MobEffect`, `CompoundTag.getInt` or `getIntOr`, is per version. Write against
  `FId` and the wrappers to avoid that; the vanilla escape hatches (`FId.vanilla()`, `FStackData.vanilla()`) return
  version-specific types.
- **Item and block subclasses.** Overridden methods (`use`, `hurtEnemy`, `appendHoverText`, block `useItemOn`)
  changed signatures; subclasses are per version.
- **Attachment sync on 1.20.1** covers entities only (sent to the owner or to trackers on change and on login and
  tracking). Chunk, level and block entity values are saved there but not sent to clients.
- **Level data files** live in different places: `<dimension>/data/ns/path.dat` on 26.x, `<dimension>/data/ns_path.dat`
  on 1.21.1 and 1.20.1. Old saves are not moved between them.
