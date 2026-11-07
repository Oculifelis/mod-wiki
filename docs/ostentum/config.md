# Config

Ostentum has one client config file, for the Now Playing HUD. Everything else is set through Fundamentum, a game rule,
tags and datapacks.

## Client config

`config/ostentum-client.toml`, section `nowPlayingHud`, or Mods, Ostentum, Config in game. The HUD shows what the
nearest jukebox you can hear is playing while you wear the [Record Pendant](items.md#records).

| Option | Meaning |
|---|---|
| `enabled` | show the HUD at all |
| `withoutPendant` | show it without wearing the pendant |
| `anchor`, `x`, `y` | which corner or edge it sits against, and the offset from there in GUI pixels (default top left, 4, 4) |
| `scale` | size; 1 is the game's own text |
| `showIcon`, `showTitle`, `showTime`, `showBar` | the playing disc, the song, "1:32 / 3:05" and the progress bar |
| `barWidth`, `maxTitleWidth` | the bar's length and where a long title is cut |
| `background`, `backgroundOpacity` | a faint backdrop like subtitles have, and how dark |
| `textColor`, `textOpacity` | text colour and opacity |

The Engineer's Crossbow's readout is Fundamentum's item HUD, placed and styled in Fundamentum's
`fundamentum-hud-client.toml` (see [Fundamentum's config](../fundamentum/index.md#config)).

## Fundamentum's options

These come from Fundamentum and affect Ostentum's items (see [Fundamentum's config](../fundamentum/index.md#config)):

| File | Option | Default | Effect on Ostentum |
|---|---|---|---|
| `fundamentum-client.toml` | `whips.flatHandles` | false | true draws whips in hand as flat icons instead of 3D handles |
| `fundamentum-sky-client.toml` | `sky.fractalSkies`, `sky.melt` | true | Ostentum's moons don't use fractal skies, so these only matter for other mods' moons |
| `fundamentum-hud-client.toml` | `itemHud.*` | | where and how the Engineer's Crossbow's mode and ammo readout is drawn |

## Game rule

| Rule | Default | Effect |
|---|---|---|
| `ostentum:voidstring_affects_players` (1.21.1: `ostentum:voidstringAffectsPlayers`) | true | false: the Voidstring Bow's swap and pull skip players, who take plain arrow damage. With it on, the server's PvP setting and team friendly fire still apply, and the shooter is never affected. |

Set it with `/gamerule ostentum:voidstring_affects_players false`.

## Tags

| Tag | Default | Effect |
|---|---|---|
| `#ostentum:voidstring_immune` (entity type) | wither, ender dragon, warden, elder guardian | the Voidstring Bow never swaps places with or pulls these; add a mod's bosses here |

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
