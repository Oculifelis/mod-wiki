# Configs (`com.fundamentum.config`)

One way for every mod to have settings: one file format, one screen, values sent from server to players. Same code
on every version (26.x, 1.21.1, 1.20.1).

## Declaring a config

In code, while the mod is constructed:

    static final FConfig CFG = FConfig.create(FId.of("mymod", "main"));
    static final ConfigValue<Integer> RANGE = CFG.integer("range", 8, 1, 64).category("combat").comment("mymod.config.range");
    static final ConfigValue<Boolean> PARTICLES = CFG.bool("particles", true).side(FConfig.Side.CLIENT);
    ...
    int r = RANGE.get();

Types: `bool`, `integer` and `decimal` (with min and max), `string`, `enumValue`, `id`, `idList`, `colour`.

Or in data only, at `data/<ns>/fundamentum/config/<path>.json` (no code at all):

    { "entries": {
        "enabled": { "type": "bool", "default": true },
        "speed":   { "type": "double", "default": 1.5, "min": 0, "max": 4, "category": "movement" },
        "style":   { "type": "enum", "values": ["plain", "fancy"], "default": "plain", "side": "client" },
        "items":   { "type": "id_list", "default": ["minecraft:apple"] } } }

Another mod reads it with `FConfig.of("mymod:main").decimal("speed").get()`, whoever declared it.

## Sides

- `SERVER` (default): set on the server, sent to every player on join and on every change.
- `CLIENT`: each player's own, never sent.
- `STARTUP`: read once. A change shows "needs restart" and takes effect after the next start; never synced.

## Files and layers, lowest first

1. The default in code (or the declaring data file).
2. Datapacks: `{"defaults": {"range": 12}}` in a higher pack, or a new `"default"` on an entry. A modpack can ship
   different defaults this way without touching anyone's file.
3. `config/fundamentum/<ns>/<path>.json5`: every entry with its comment; entries not set are written commented out
   with their default.
4. `<world>/serverconfig/fundamentum/<ns>/<path>.json5`: per-world values, these win.

Bad values are logged and ignored, never fatal. On a server, edits to the files are picked up on the next tick after the
system reports a change in the config folder, on `/reload`, and by a slow full check (`config_recheck_seconds` in
[Performance](performance.md), 60 by default) for drives that send no change reports.

## Events

`ConfigEvent.listen(e -> ...)` hears `ConfigEvent.Changed(id, keys)` after any change (file, `/reload`, screen, server
sync). It is the ecosystem event `fundamentum:config_changed`, so `FEvents` listeners and advancements see it too
([Events](events.md)). The first load is quiet.

## The screen

The Config button in the mod list opens one screen for every Fundamentum config: search, filter by mod and category,
pages, reset per entry. Players change `CLIENT` entries; only an operator (or the singleplayer owner) can change server
entries, which are sent to the server and checked there. "Classic settings" opens Fundamentum's older config screen.
`ConfigScreenModel` holds the screen's logic without any GUI code, for other front ends.

## Test

`gradlew runServer -Pconfigtest` (world under `run-configtest`, never build a jar with it) checks declaring, files,
layers, datapack defaults, validation, events and the sync messages; it ends with `CONFIGTEST RESULT PASS` or `FAIL`.

## Not covered yet

- No file watcher on the client side; client files are read on start and when the screen saves.
- Fundamentum's older settings (whips, sky, HUD, soul fire, biomes, materials) stay on their own files for now.
