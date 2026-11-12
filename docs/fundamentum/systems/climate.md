# Climate and seasons (`com.fundamentum.climate`)

Temperature and humidity at any spot, and an optional year of seasons that shifts them, slows or speeds crops and
tints grass and leaves. The same code runs on every version. Seasons are off until a server turns them on.

## Reading the climate

    double t = Climate.temperature(level, pos);   // vanilla scale: plains 0.8, snow below 0.15, desert 2.0
    double h = Climate.humidity(level, pos);      // 0 to 1
    Climate.Reading parts = Climate.temperatureParts(level, pos);  // biome, season, height, blocks, weather

The parts add up to the total:

- **biome**: the biome's own temperature (after loader biome changes and vanilla's frozen-ocean noise) or rainfall.
- **season**: the current season's offset for that biome, 0 while seasons are off.
- **height**: -0.00125 per block above sea level + 17, the same cooling vanilla uses. Humidity has none.
- **blocks**: heat and cold blocks nearby (below).
- **weather**: rain on a spot open to the sky gives -0.1 temperature and +0.2 humidity.

Temperature is not clamped. Humidity is clamped to 0..1 in `humidity()`, but the parts are left raw.
On a client level only the season's flat offsets count, because per-biome season rules stay on the server.

## Heat and cold blocks

`data/<namespace>/fundamentum/climate_blocks/<name>.json`:

    {"blocks": ["minecraft:lava", "#minecraft:campfires"], "temperature": 0.6, "humidity": -0.1, "radius": 4}

`blocks` is one id or a list, `#` for a block tag. The effect is full on the spot and fades to nothing just past
`radius` (default 4, capped at 8). Only the nearest matching block of each file counts, so a lava lake is no hotter
than one lava block at the same distance. Different files add up. Fundamentum ships `heat` (lava, fire, soul fire,
campfires, magma) and `cold` (ice, packed and blue ice, snow blocks, powder snow). A file that can't be read is
skipped and the log says why.

## Seasons

`data/<namespace>/fundamentum/seasons/<name>.json`, one file per season:

    {
      "order": 3,
      "length": 8,
      "temperature": -0.35,
      "rainfall": 0,
      "biomes": [
        {"biomes": ["#minecraft:is_jungle", "minecraft:desert"], "temperature": -0.1}
      ],
      "crop_growth": 0.25,
      "crops": {"minecraft:wheat": 0.5, "#mymod:hardy_crops": 1},
      "grass": "#8E9A84",
      "foliage": "#8C8270",
      "tint": 0.35
    }

| Field | Means | Default |
|---|---|---|
| `order` | place in the year, lowest first (ties go by id) | 0 |
| `length` | days, at least 1 | 8 |
| `temperature`, `rainfall` | offsets for every biome no rule names | 0 |
| `biomes` | per-biome offsets, first match wins; a rule leaves out a value to use the season's | none |
| `crop_growth` | growth multiplier, 1 is normal, 0 stops crops | 1 |
| `crops` | per-crop multipliers by block id or `#` tag, first match wins | none |
| `grass`, `foliage` | colour clients blend toward, `#RRGGBB` | none |
| `tint` | how far the blend goes, 0 to 1 | 0.25 |

Fundamentum ships spring, summer, autumn and winter, 8 days each (a 32-day year). A pack can replace any of them by
id or add more. A broken file is left out of the year and the log says why. The config can change the lengths and pick which seasons run
without a datapack (see Config below).

The calendar runs on the overworld's day count, so `/time set` moves it and every dimension shares one season.
Seasons only apply in the dimensions the config lists (the overworld by default); elsewhere the season part is 0
and crops grow normally.

When the season changes, `fundamentum:season_changed` fires (`SeasonChanged(from, to, day)`, either side null when
seasons turn on or off). See [Events](events.md).

    FEvents.listen(SeasonChanged.class, (SeasonChanged e) -> ...);
    Season now = Seasons.current(level);   // null while seasons are off or this dimension has none

## Crops

The season's multiplier applies to every crop growth step the loader reports (vanilla crops, saplings, stems,
cactus, cane and the like, and modded crops that fire the loader's event). Below 1, each step only goes through
with that chance, so 0.25 means a quarter of the steps. Above 1, a grown step may add more age right away: 1.25
gives a 25% chance of one extra age step. Blocks without an `age` property only ever get slowed.
Turn this off with `crop_growth` in the config.

## Grass and leaf tint

Clients blend biome grass and foliage colours toward the season's colours by its `tint` share. The server sends the
season to each player on login and on every change, and the client redraws loaded chunks. Blocks that use fixed
colours (birch and spruce leaves) are not tinted. Turn it off with `tint` in the server's config.

## Serene Seasons

On 1.21.1 and 1.20.1, if Serene Seasons is installed it takes over: Fundamentum reads its season by name
(spring, summer, autumn, winter; its early, mid and late sub-seasons count as the plain one) and our own calendar,
crop changes and tint stand down, since Serene Seasons does those itself. Season offsets in `Climate` still apply from
the matching file. Set `serene_seasons` to false in the config to ignore it. Serene Seasons has no 26.x build, so the
bridge does nothing there.

## Config

`config/fundamentum/fundamentum/climate.json5` (see [Config](config.md)):

| Key | Does | Default |
|---|---|---|
| `seasons` | runs the year | false |
| `crop_growth` | seasons change crop growth | true |
| `tint` | seasons tint grass and leaves | true |
| `serene_seasons` | let Serene Seasons supply the season when installed | true |
| `dimensions` | dimensions the season applies in | `["minecraft:overworld"]` |
| `season_length` | days for every season, over the files' own `length`; 0 keeps the files' | 0 |
| `season_lengths` | days per season, `"fundamentum:summer=12, fundamentum:winter=4"`; wins over `season_length` | `""` |
| `season_list` | which seasons make up the year, in their usual order; empty means all of them | `[]` |

So a server that wants a long summer and no autumn sets `season_lengths` to `"fundamentum:summer=16"` and
`season_list` to spring, summer and winter. Seasons are still off until `seasons` is true.

## Commands

Operators only.

- `/fundamentum climate` gives the temperature and humidity where you stand, part by part.
- `/fundamentum season` gives the season and day (the result is the season's place in the year, 1 for the first).
- `/fundamentum season set <season>` starts that season today. It moves the calendar, not the clock. A season id with
  no namespace means `fundamentum:`.

## Test

`gradlew runServer -Pclimatetest` (world under `run-climatetest`) checks that seasons start off, the year loads in
order with a broken file left out, the calendar, setting a season and the event, biome rules, height, heat and cold
blocks, rain, crop slowing and speeding, the client sync and tint blend, and the commands. It ends with
`CLIMATETEST RESULT PASS` or `FAIL`.
