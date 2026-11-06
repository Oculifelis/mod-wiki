# Commands

All under `/fundamentum`, for operators (level 2), except `/fundamentum_sky`, which is a client command anyone can use.

| Command | What it does |
|---|---|
| `/fundamentum moon start <id>` | starts any loaded moon or night event (tab-completes them all), making it night first |
| `/fundamentum moon stop` | ends tonight's moon and night event |
| `/fundamentum moon list` | every moon and night event, marked `[up]` or `[off]` |
| `/fundamentum moon query` | names tonight's moon |
| `/fundamentum moon raise <id>` / `clear` | raise or clear a moon without changing the time |
| `/fundamentum event raise <id> [ticks]` / `clear` / `query` | the same for night events |
| `/fundamentum element help` | the elements manual in chat |
| `/fundamentum element reactions` | every loaded reaction, in order |
| `/fundamentum element auras <targets>` | the auras on creatures |
| `/fundamentum element clear <targets>` | removes them |
| `/fundamentum element affinity <targets> <damage type>` | how much they resist that damage type |
| `/fundamentum element hit <targets> <damage type> <amount> [attacker]` | a test hit (resets the hurt cooldown, so several in a row all land); prints the health taken and the auras left |
| `/fundamentum tps [dimension]` | TPS and ms per tick, per dimension with entity and chunk counts; one dimension lists its ten most common entity types |
| `/fundamentum showcase <mod>` | builds a gallery in the sky: a lit glass case per mob from that mod (or `minecraft`) |
| `/fundamentum showcase return` / `clear` | takes you back / removes the gallery |
| `/fundamentum_sky preview <id>` / `off` | shows a [fractal sky](datapack/fractal-skies.md) now, on your client only |

Elements, `tps`, night events and the fractal sky command are NeoForge 26.1.2 and 1.21.1 (`tps` and night events are
also on 26.2).
