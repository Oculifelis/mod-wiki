# In-game guide (`com.fundamentum.guide`)

One guide screen for every mod that ships pages: search, a book per mod with chapters, and pages with items, recipes,
multiblock previews, mobs and pictures. Pages are reference pages; there are no quests or progress here. The same code
runs on every version, apart from the screen's drawing.

## Pages

`assets/<namespace>/fundamentum/guide/<path>.md`. The page id is `<namespace>:<path>`, so
`assets/mymod/fundamentum/guide/machines/press.md` is `mymod:machines/press`.

    ---
    title: The Press
    chapter: machines
    icon: mymod:press
    items: mymod:press, mymod:press_plate
    unlock: mymod:pressing
    order: 2
    ---
    # The Press

    Squeezes **ores** into plates. Feed it with a [hopper](mymod:hoppers).

    - Needs *redstone* to run
    - Takes `16` FE per tick

    {{recipe mymod:pressing iron_plate}}
    {{multiblock mymod:big_press}}

| Front matter | Means | Default |
|---|---|---|
| `title` | shown in lists and on the page | the first heading, else the path |
| `chapter` | chapter id; a bare name is in the page's namespace | `<namespace>:main` |
| `icon` | item id | none |
| `items` | comma separated item ids this page explains | none |
| `unlock` | unlock id the player needs to see the page | none |
| `order` | place in the chapter, lowest first, then by title | 0 |

The body takes `#`, `##` and `###` headings, paragraphs (lines run together until a blank line), `-` or `*` bullets,
`---` dividers, `**bold**`, `*italic*`, `` `code` `` and `[text](ns:page)` links. A link to `<ns>:book` opens that
mod's book. Embeds sit on a line of their own:

| Embed | Shows |
|---|---|
| `{{item a:b c:d}}` | items with their names |
| `{{recipe <category> <key>}}` | a recipe from the recipe viewer ([Recipe Viewers](recipe-viewers.md)) |
| `{{multiblock <id>}}` | a multiblock pattern's preview and parts list ([Multiblocks](multiblocks.md)) |
| `{{entity <type> scale=N}}` | a mob facing the mouse, scale 4 to 120, default 30 |
| `{{image ns:textures/x.png WxH}}` | the whole texture drawn at W by H, default 64x64 |

Ids without a namespace use the page's. A broken embed is left out and the log names the page and line.

## Books and chapters

`assets/<namespace>/fundamentum/guide/chapters.json`, one per mod:

    {
      "title": "My Mod",
      "icon": "mymod:guide_book",
      "openers": ["mymod:guide_book"],
      "chapters": [
        {"id": "start", "title": "Getting Started", "icon": "minecraft:crafting_table"},
        {"id": "machines", "title": "Machines", "order": 5, "unlock": "mymod:first_machine"}
      ]
    }

Chapters show by `order` (default: their place in the list), then title. A chapter that pages name but the file leaves
out comes last, titled from its path. A mod without the file gets a book titled from its namespace.

## Unlocks

A page shows only when the player holds its own `unlock` and its chapter's (see [Unlocks](unlocks.md)). Hidden pages
are left out of lists, search and item lookups, and a link to one goes nowhere. Books and chapters with nothing
visible are hidden too.

## Opening it

- Right-click an item from a book's `openers` list. Fundamentum adds no item of its own, so a mod names one of its own
  items (or a vanilla one).
- Press the guide key (G by default). Over an item in an inventory it opens that item's page; anywhere else it opens
  where the guide was last left.
- Items with a page get a tooltip line naming the key. Opener items get one too.
- From code: `Guides.open(FId.of("mymod", "machines/press"))` on the client (does nothing on a server).

## Search

Every word typed has to appear in the title, the text or the page's item ids. Title matches come first, then by title.

## Testing

`gradlew runServer -Pguidetest` builds the guide from test pages and checks front matter, the markup and every embed,
broken pages, chapters and books, links, item lookups, search and unlock gating. It prints `GUIDETEST RESULT PASS` and
stops the server. The screen is only compiled, never opened, in tests.
