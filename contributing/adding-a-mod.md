# Adding a mod

Each mod has its own folder under `docs/` and its own tab in `mkdocs.yml`. To add one:

1. Make `docs/<mod>/index.md`: what the mod is, what it needs, the versions, and a short feature list.
2. Add more pages beside it as the mod needs them. The usual set is:
    - `items.md`: every item, block and mob, with how to get it.
    - `config.md`: every config option, with its file and default.
    - `datapack/`: one page per JSON format, with a full example and a field table.
    - `api.md`: public classes and events, for addon makers.
3. Put the logo in `docs/assets/<mod>_logo.png`, and add a card for the mod to `docs/index.md`.
4. Add a tab to `nav` in `mkdocs.yml`, in the same shape as the others:

    ```yaml
    - MyMod:
        - mymod/index.md
        - Items: mymod/items.md
        - Config: mymod/config.md
    ```

5. Build it with `python -m mkdocs build --strict` and fix every warning before you commit.

Every item, block and mob on a page gets a picture beside it. Items are their flat inventory sprite from the mod's own
texture, scaled up nearest-neighbour; blocks and mobs are real in-game cut-outs made with the shared `mobshots` kit.
Never use angled or isometric renders made outside the game. `python tools/entry_icons.py <mod> docs/<mod>/items.md --prose`
adds the pictures to tables and bold names; picture whatever it reports as missing by hand.

Field tables use the columns **Field | Default | Meaning**. Every JSON example should be one that loads; check it against
the mod's code, not against memory.
