# Night events

*Fundamentum 1.28.0: Forge 1.20.1; NeoForge 1.21.1, 26.1.2, 26.2 and 26.3.*

Something that happens on a night, beside (or instead of) its moon: a feast, a raid, a siege. One runs at a time per
world. They're rolled at dusk after the moon, or raised by code or command.

**File:** `data/<ns>/fundamentum/night_events/<name>.json`. The id is `<ns>:<name>`. Every field is optional.

```json
{
  "chance": 0.1,
  "priority": 0,
  "dimension": "minecraft:overworld",
  "requires": ["mymod:dragon_slain"],
  "excludes": ["mymod:peace_treaty"],
  "min_day": 5,
  "cooldown": 3,
  "with_moon": true,
  "moons": ["mymod:harvest"],
  "not_moons": ["mymod:blood"],
  "duration": 0,
  "fog": {"color": "#C08040", "strength": 0.3},
  "sky": {"color": "#C08040", "strength": 0.15},
  "title": {"title": "event.mymod.feast", "subtitle": "event.mymod.feast.sub", "color": "fog"},
  "start_message": "message.mymod.feast",
  "start_sound": "mymod:feast_bell",
  "end_message": "message.mymod.feast_over",
  "end_sound": ""
}
```

| Field | Default | Meaning |
|---|---|---|
| `chance` | 0 | per eligible night; 0 means only when raised by code or command |
| `priority` | 0 | rolled from the highest priority down; the first that happens wins |
| `dimension` | `minecraft:overworld` | |
| `requires` / `excludes` | none | world flags that must all be set / all be unset |
| `min_day` | 0 | not before this day |
| `cooldown` | 0 | nights after it last happened before it can roll again |
| `with_moon` | true | false: never on a night with a special moon |
| `moons` / `not_moons` | any / none | only with these moons / never with these |
| `duration` | 0 | ticks it lasts once started; 0 is dusk to dawn |
| `fog` / `sky` | none | [tints](moons.md#tints), laid over the moon's |
| `title` | none | a title on screen when it starts: a lang key, or `{"title", "subtitle", "color"}` |
| `start_message` / `end_message` | none | as a moon's `rise_message` |
| `start_sound` / `end_sound` | none | as a moon's `rise_sound` |

Ostentum's Pillager Siege is a night event; its waves are code that reads this event. Test with
`/fundamentum event raise <id>`, `clear` and `query` (see [Commands](../commands.md)).
