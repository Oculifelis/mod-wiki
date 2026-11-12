# Music rules (`com.fundamentum.music`)

Datapack rules that pick the music by biome, structure, dimension, time of day, weather, season, boss fight and
combat. The client crossfades between tracks and keeps vanilla music quiet while one plays. Boss music runs through
the same system. The same code runs on every version.

## Rules

`data/<namespace>/fundamentum/music/<name>.json`, one rule per file:

    {
      "sound": "mymod:music.ruins",
      "priority": 10,
      "fade_in": 60,
      "fade_out": 40,
      "dimension": "minecraft:overworld",
      "biomes": ["#minecraft:is_jungle", "minecraft:swamp"],
      "structures": ["#minecraft:village", "mymod:ruins"],
      "time": "night",
      "weather": ["clear", "rain"],
      "season": "winter",
      "boss": false,
      "combat": false
    }

| Field | Means | Default |
|---|---|---|
| `sound` | sound event id to loop (from a `sounds.json`), required | none |
| `priority` | higher wins | 0 |
| `fade_in`, `fade_out` | ticks, at least 1 | 40 |
| `dimension` / `dimensions` | one id or a list | any |
| `biome` / `biomes` | ids or `#` tags | any |
| `structure` / `structures` | ids or `#` tags; the player must stand inside a piece | any |
| `time` | `day` (1000-12000), `dusk` (12000-13000), `night` (13000-23000), `dawn` (23000-1000), or `{"from": 6000, "to": 9000}` | any |
| `weather` | `clear`, `rain`, `thunder`, one or a list | any |
| `season` / `seasons` | season ids; a bare name like `winter` means `fundamentum:winter` | any |
| `boss` | `true` (any boss fight), `false` (no boss fight), or boss type ids | any |
| `combat` | `true` or `false` | any |

Every field a rule names has to match. Out of the rules that match, the highest priority plays; ties go to the lowest
rule id. A rule with no fields but `sound` matches everywhere. A season rule never matches while seasons are off (see
[Climate](climate.md)). A file that can't be read is skipped and the log says why.

When nothing matches, vanilla music plays as usual.

## Boss music

The boss package sends its track through `BossMusic`, and anything else may too:

    BossMusic.play(player, FId.of("mymod", "music.boss").vanilla(), 40, bossEntity);
    BossMusic.stop(player, 40);

The boss track joins the rules at priority 1000 (`MusicDirector.BOSS_PRIORITY`) and wins ties. A rule above 1000
still plays over it, so a pack can give one boss its own track with `"boss": "mymod:lich", "priority": 2000`.

## Combat

A player is fighting when a mob hurt them or they hurt a mob within the last `combat_ticks`, or when a hostile mob
within `combat_range` blocks targets them.

## Server and client

The server works out what only it knows (the structures a rule watches, the boss fight and combat) and sends that
state to each player when it changes. It also sends the rules on login. The client checks everything else (biome,
time, weather, season) and picks the track.

On 1.20.1 vanilla music is dropped as it starts while a rule's track plays. Newer versions swap it out through the
loader's music event.

## Config

`fundamentum:music` (see [Config](config.md)):

| Key | Means | Default |
|---|---|---|
| `enabled` | client: play rule music at all | true |
| `volume` | client: 0 to 1, on top of the game's music slider | 1 |
| `stop_vanilla` | client: keep vanilla music quiet while a rule's track plays | true |
| `combat_ticks` | server: how long a hit keeps a player fighting, 20 to 2400 | 200 |
| `combat_range` | server: hostile mob range for combat, 0 to 64, 0 turns it off | 16 |

## Command

`/fundamentum music` (operators) says which track plays for you and why, how many rules loaded, whether you count as
fighting and which watched structures you stand in.

## Testing

`gradlew runServer -Pmusictest` loads test rules and checks parsing, broken files, priority, every condition, the
structure lookup, the boss track and boss rules, combat from a hit and from a hunting mob, the network sync, the config
and the command. It prints `MUSICTEST RESULT PASS` and stops the server.
