# Books and themes

Guide books, book styles, guide themes and the bestiary are resource pack files, read from
`assets/<ns>/fundamentum/...`. Each file is the same on every Minecraft version. Every text field is a lang key or plain
text, and a missing key shows as written.

## Guide books

A book is `assets/<ns>/fundamentum/books/<id>.json`, and its entries are
`assets/<ns>/fundamentum/books/<id>/<entry>.json`. The `fundamentum:guide_book` item opens the book named in its
`fundamentum:guide_book` component, and takes the book's title as its name.

```json
{
  "title": "book.mymod.field_guide",
  "subtitle": "book.mymod.field_guide.sub",
  "style": "fundamentum:parchment_tome",
  "icon": "minecraft:spyglass",
  "intro": "book.mymod.field_guide.intro",
  "categories": [
    {"id": "beasts", "title": "book.mymod.cat.beasts", "icon": "minecraft:bone"},
    {"id": "plants", "title": "book.mymod.cat.plants", "icon": "minecraft:fern"}
  ]
}
```

| Field | Default | Meaning |
|---|---|---|
| `title` | the book id | |
| `subtitle` | none | shown in the item tooltip |
| `style` | `fundamentum:parchment_tome` | a [book style](#book-styles) |
| `icon` | none | an item id |
| `intro` | none | the opening text |
| `categories` | none | `{"id", "title", "icon"}` sections, in reading order |

An entry:

```json
{
  "category": "beasts",
  "title": "entity.minecraft.wolf",
  "subtitle": "book.mymod.wolf.sub",
  "entity": "minecraft:wolf",
  "order": 2,
  "facts": ["book.mymod.wolf.fact1", "book.mymod.wolf.fact2"],
  "flavour": "book.mymod.wolf.flavour",
  "cards": [{"icon": "minecraft:bone", "label": "book.mymod.tames", "value": "book.mymod.with_bones"}],
  "health": 8,
  "armor": 0,
  "drops": [{"item": "minecraft:bone", "chance": "50%"}],
  "stamps": [{"kind": "seen"}, {"kind": "kill", "count": 5}]
}
```

| Field | Default | Meaning |
|---|---|---|
| `category` | the first category | an unknown category also falls back to the first |
| `title` | the entry file name | |
| `subtitle`, `flavour`, `caption` | none | text lines on the page |
| `icon` | none | an item id |
| `entity` | none | the mob drawn in the portrait frame |
| `unlock` | none | a Fundamentum unlock id that must be met before the entry opens |
| `order` | 0 | order within the category, then by id |
| `facts` | none | a list of lines |
| `cards` | none | `{"icon", "label", "value", "warn"}` boxes; `warn` draws one as a warning |
| `health`, `armor` | 0 | shown as stats |
| `drops` | none | `{"item", "label", "chance"}`, where `chance` is shown as written |
| `stamps` | none | goals on the entry's progress row |

A stamp has a `kind` of `kill`, `seen`, `obtain` or `unlock`, a `target` (an entity, item or unlock id; `kill` and `seen`
default to the entry's `entity`), an optional `label` and `icon`, and a `count` (1 by default). Kills and pick-ups come
from the game's statistics, and a mob counts as seen once it has been within 24 blocks.

## Book styles

A style is `assets/<ns>/fundamentum/book_styles/<id>.json`, and its textures are
`assets/<ns>/textures/gui/book/<id>/<layer>.png`. Fundamentum ships ten: `parchment_tome`, `bestiary`, `almanac`,
`dig_journal`, `engineers_manual`, `grimoire`, `infernal_grimoire`, `lab_notebook`, `redstone_pad` and `ships_log`.
Copying one of these is the easiest start.

| Field | Default | Meaning |
|---|---|---|
| `name` | the id path | |
| `colors` | none | named colours as hex (`ink`, `dim`, `accent`, `rule`, `card`, `page` and so on) |
| `title_text`, `title_shadow`, `title_upper` | `f8e8c8`, none, true | the title colour, its shadow and whether it is upper case |
| `card_text`, `stamp_text`, `rule_color` | dark brown, dark brown, `d4bf90` | |
| `bullet` | `-` | the mark before each fact |
| `numerals` | plain | `roman` gives page numbers like "- ix -" |
| `frame` | `plain` | the portrait frame |
| `window` | | where the mob is drawn: `x`, `y`, `w`, `h`, `oval` and `ground` (the floor line), relative to the screen centre |
| `caption` | none | `{"x", "y", "color"}` for the portrait caption |
| `layers` | none | each texture layer, by name: `x`, `y`, `w`, `h` and the file size `tw`, `th` |
| `animation` | 16, 12, 16, 11 | `open_ticks`, `turn_ticks`, `close_ticks` and `stamp_ticks` |
| `sounds` | none | sound ids by name, or null for silence |

## Guide themes

A theme is `assets/<ns>/fundamentum/guide_themes/<path>.json`, with the id `<ns>:<path>`. Loose files in
`config/fundamentum/guide_themes/` load too. The theme picker inside a guide lists them all with search and tags, and a
book can name one with `"theme"` in its `chapters.json`. Every field is optional and falls back to the vanilla
container look. A bad colour shows as magenta, and the log names the field.

```json
{
  "name": "Deepslate Tiles",
  "tags": ["dark", "textured", "minecraft"],
  "style": "textured",
  "backdrop": "#99000000",
  "colors": {"fill": "#FF1A1A20", "frame": "#000000", "rule": "#3A3A44", "title": "#E6E6EA", "muted": "#9A9AA6",
             "text": "#E6E6EA", "strong": "#E6E6EA", "soft": "#CBCBD2", "mod": "#CBCBD2", "nav": "#CBCBD2"},
  "shadow": true,
  "accent": {"shift": 0.0, "selection": 70},
  "well": {"fill": "#3A3A44", "light": "#3A3A44", "shadow": "#9A9AA6", "line": "#000000"},
  "page": {"text": "#E6E6EA", "muted": "#9A9AA6", "code": "#E6C07B", "rule": ["#3A3A44", "#3A3A44"], "shadow": true},
  "slot": {"fill": "#3A3A44", "edge": "#9A9AA6"},
  "texture": {
    "background": "minecraft:textures/block/deepslate_tiles.png",
    "border": "minecraft:textures/block/polished_blackstone_bricks.png",
    "tint": "#46000000",
    "border_tint": "#3C000000",
    "border_width": 5,
    "well": "#AF0C0C10"
  }
}
```

| Field | Meaning |
|---|---|
| `name`, `tags` | the name and the tags the picker filters by |
| `style` | `flat` (one fill and a thin frame), `bevel` (container edges and sunken wells) or `textured` (tiled block textures) |
| `backdrop` | the colour behind the panel |
| `colors` | `fill` the panel, `frame` its outline, `rule` the thin lines, `title` the header, `muted` hints and counts, `text` open rows, `strong` the selected row, `soft` closed rows, `mod` closed mod rows, `nav` the page arrows |
| `shadow` | text shadow |
| `accent` | `shift` darkens (below 0) or lightens (above 0) each book's accent colour to read on this panel; `selection` is the highlight strength, 0 to 255 |
| `bevel` | `light` and `shadow` edge colours |
| `well` | the box behind text: `fill`, `light`, `shadow` and `line` |
| `page` | `text`, `title`, `heading`, `link`, `code`, `muted`, `rule` (two colours) and `shadow`; `title`, `heading` and `link` follow the book's accent when left out |
| `slot` | item slot `fill` and `edge` |
| `texture` | for `textured`: `background` (needed), `border`, `size` (16), `tint`, `border_tint`, `border_width` (5, at most 16) and `well` |
| `gradient` | two colours, top and bottom, for a gradient fill |
| `rainbow` | `{"saturation", "speed"}` for an animated rainbow border |
| `beads`, `ribbon` | colours for a beaded edge and a ribbon |

Colours are `#RRGGBB` or `#AARRGGBB`.

### Installing a theme

A theme is one `.json` file. Put it in `config/fundamentum/guide_themes/` inside the game folder (make the folder if
it is missing), then reload resources with F3+T or restart the game. The theme shows in the picker under its `name`, or
under the file name when it has none. A resource pack carries themes at `assets/<ns>/fundamentum/guide_themes/`, and a
pack theme with the same id as a built-in one replaces it.

### Making a theme

The quickest start is a copy of a built-in theme from the Fundamentum jar, at
`assets/fundamentum/fundamentum/guide_themes/`. Copy one into the theme folder, rename the file, then change its `name`
and colours. Anything a theme leaves out comes from the vanilla container look, so a single line is a whole theme:

```json
{"name": "Plum", "style": "flat", "colors": {"fill": "#3A2040"}}
```

A `textured` theme needs `texture.background`, a block texture such as
`minecraft:textures/block/deepslate_tiles.png`. The `rainbow`, `beads`, `ribbon` and `gradient` extras stack on any
style.

## Bestiary

The bestiary is one shared book, `fundamentum:bestiary`, with a stat sheet page for every mob of each mod that turns it
on. A mod turns it on with `assets/<modid>/fundamentum/bestiary/<any>.json`:

```json
{
  "title": "bestiary.mymod",
  "icon": "mymod:bottled_sprite",
  "exclude": ["mymod:puff"],
  "sources": {"mymod:sprite": "mymod:bottled_sprite"},
  "biomes": {"mymod:sprite": ["minecraft:plains"]},
  "drops": {"mymod:sprite": ["minecraft:bone"]},
  "zoom": {"mymod:giant": 0.5}
}
```

| Field | Meaning |
|---|---|
| `title`, `icon` | the mod's section in the contents |
| `entities` | the mobs to list; left out, every living mob of the namespace |
| `exclude` | mobs to leave out |
| `sources` | the item that summons each mob |
| `biomes` | where each mob lives |
| `drops` | what each mob drops |
| `zoom` | portrait size, for a model much bigger or smaller than its hitbox |

Each mob's lore line is the lang key `bestiary.<modid>.<mob>`. A page stays locked, shown as ??? in the contents, until
the mob has been seen. Health, armour and the other stats come from the mob's default attributes.
