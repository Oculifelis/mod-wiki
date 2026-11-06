# Config

**Ostentum has no config file of its own.** What you can change:

## Fundamentum's options

These come from Fundamentum and affect Ostentum's items (see [Fundamentum's config](../fundamentum/index.md#config)):

| File | Option | Default | Effect on Ostentum |
|---|---|---|---|
| `fundamentum-client.toml` | `whips.flatHandles` | false | true draws whips in hand as flat icons instead of 3D handles |
| `fundamentum-sky-client.toml` | `sky.fractalSkies`, `sky.melt` | true | Ostentum's moons don't use fractal skies, so these only matter for other mods' moons |

## Datapacks

Almost everything in Ostentum is Fundamentum data under `data/ostentum/fundamentum/`, so a datapack can change it by
putting a file at the same path. Fundamentum merges files field by field, so a file needs only the fields it changes.
For example, to make the pig saddle faster, `data/ostentum/fundamentum/mounts/pig.json`:

```json
{"item": "ostentum:pig_saddle", "speed": 0.2}
```

| What | Folder | Format |
|---|---|---|
| Saddles | `fundamentum/mounts/` | [Mounts](../fundamentum/datapack/mounts.md) |
| Hooks | `fundamentum/hooks/` | [Hooks](../fundamentum/datapack/hooks.md) |
| Summons | `fundamentum/summons/` | [Summons](../fundamentum/datapack/summons.md) |
| Whips | `fundamentum/whips/` (none ship; a file keyed by `item` overrides a whip's tuning) | [Whips](../fundamentum/datapack/whips.md) |
| Moons | `fundamentum/moons/` | [Moons](../fundamentum/datapack/moons.md) |
| Pillager Siege | `fundamentum/night_events/` | [Night events](../fundamentum/datapack/night-events.md) |
| Apple sickness | `fundamentum/sickness/` | [Use sickness](../fundamentum/datapack/sickness.md) |

Recipes, loot and the weaponsmith trade are ordinary vanilla data (`recipe/`, `loot_modifiers/`, `villager_trade/`).
