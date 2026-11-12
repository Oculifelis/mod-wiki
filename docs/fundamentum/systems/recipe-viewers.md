# Recipe viewers

`com.fundamentum.recipeview` lets a mod describe a recipe page once and have it show in JEI, REI and EMI, whichever the
player has. Declarations are plain Java made during mod construction (common side, so a server test can read them); the
viewer plugins in `recipeview/jei`, `recipeview/rei` and `recipeview/emi` turn them into each viewer's own pages when
that viewer loads. All three viewers are optional: Fundamentum compiles against them and never ships them.

The package uses nothing else from Fundamentum, so it can later move into its own jar.

## Which viewers each version has

| Version | JEI | REI | EMI |
|---|---|---|---|
| neoforge-26.1.2 | 29.x | 26.1.x | no build for 26.x |
| neoforge-26.2 | 30.x | 26.2.x | no build for 26.x |
| neoforge-26.3 | 31.x | 26.3.x | no build for 26.x |
| neoforge-1.21.1 | 19.x | 16.x | 1.1.x |
| forge-1.20.1 | 15.x | 12.x | 1.1.x |

EMI has no release for any 26.x version, so 26.x has no EMI plugin. When one comes out, copy `recipeview/emi` from
1.21.1 (it only needs the `ResourceLocation` to `Identifier` rename) and add the dependency.

## A category

```java
ViewCategory<MyRecipe> c = RecipeViews.category("mymod:grinding")
        .title(Component.translatable("jei.mymod.grinding"))
        .icon(() -> new ItemStack(MyItems.GRINDER.get()))
        .size(120, 40)                 // the page area in pixels
        .arrow(50, 12, 100)            // a progress arrow; 0 ticks draws it empty
        .catalysts(() -> List.of(new ItemStack(MyItems.GRINDER.get())));
int in = c.input(10, 12);              // slots: x, y of the 18x18 frame's corner
int water = c.fluidInput(30, 12);
int out = c.output(90, 12);
c.recipes(MyRecipes::clientCopy)       // read each time a viewer builds its pages
        .key(r -> r.name())            // the recipe's id becomes mymod:grinding/<key>
        .fill((r, page) -> {
            page.items(in, r.inputs()).fluid(water, new ViewFluid(Fluids.WATER, 250)).item(out, r.result());
            page.text(Component.literal("Takes 5 s"), 30);        // centred at y 30
            page.text(Component.literal("Wet"), 4, 2);            // or at x, y
        });
```

- Ids are `namespace:path`, lower case. A second category with the same id is refused.
- A slot outside the area, an area under 18 pixels, an item in a fluid slot and a fluid amount under 1 are refused when
  declared.
- `slot(ViewSlot.Role.CATALYST, kind, x, y)` adds a slot for a block or tool the recipe needs. JEI and REI show it as an
  input, EMI as a catalyst.
- A `fill` that throws skips only that recipe and logs it once. Empty stacks in a slot are dropped and stacks are copied.

## Hiding, subtypes, information pages

- `RecipeViews.hide(() -> item)` or `RecipeViews.hide(stack -> ...)` keeps items out of every viewer's list. A rule
  that throws counts as no match. Relics use this to hide their base blocks, fillers and
  the blank relic item, and `subtypes` to list each relic apart.
- `RecipeViews.subtypes(() -> item, stack -> key)` makes stacks of one item with different keys separate entries
  (an empty key is the plain item).
- `RecipeViews.info(stacks, lines)` adds an information page; `RecipeViews.infoPages(() -> pages)` adds pages read
  each time, for data-driven content. Pages with no stacks or no lines are dropped.

## Refreshing

`RecipeViews.refresh()` tells listeners (`RecipeViews.onRefresh`) that the recipes changed, for example when a new copy
arrives from the server. JEI picks the change up at once. REI and EMI rebuild their pages on their next reload (joining
a world, `/reload`, or the viewer's own reload key).

## What Fundamentum declares itself

- `fundamentum:portal_crafting` (`portal/PortalViews`): the thrown item, the result, which portal it takes and where it
  leads, with obsidian, flint and steel and an eye of ender as catalysts.
- An information page per relic (`relic/RelicViews`).

## Test

`gradlew runServer -Precipeviewtest` (world in `run-recipeviewtest`) checks the registry: ids, slots, building, text,
arrows, a filler that throws, hiding, subtypes, information pages, refresh listeners, Fundamentum's own categories, and
that every viewer plugin this version compiles is in the jar. The viewers are client mods, so the plugins themselves are
proven by compiling against each viewer. Lines start `RECIPEVIEWTEST`; the result is in `recipeviewtest-result.txt`.
