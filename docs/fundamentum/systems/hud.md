# HUD layout and editor (`com.fundamentum.hud`)

Every HUD element drawn through Fundamentum can be moved, scaled, faded and switched off by the player, the way Jade
does it for its tooltip. One file holds all of it, and an in-game editor writes that file. A mod that adds its HUD
element through the library gets all of this with no extra code. Same code on every version.

## For players

- Open the editor from the Fundamentum settings screen (the HUD layout button at the top right), or bind the
  HUD Editor key (unbound by default, under Fundamentum in Controls).
- Each element shows as a box over the live HUD. Drag a box to move it. It snaps to the nearest of nine screen
  points (corners, edge middles and the center), so it stays in place when the window or GUI scale changes.
- Scroll over a box to scale it. Shift and scroll to fade it. Right click to switch it off or on.
- Reset puts the selected element back. Reset all puts every element back. Done saves.
- The vanilla boss bars are an element too, so boss bars from any mod move with them.
- F1 still hides everything.

## The file

`config/fundamentum-hud-layout.json`, in the game folder:

    {"hide_all": false, "layers": {
      "mymod:mana_bar": {"enabled": false},
      "othermod:heat": {"order": 50, "anchor": "top_right", "x": -4, "y": 4, "scale": 1.5, "opacity": 0.8}}}

`anchor` is one of `top_left`, `top_center`, `top_right`, `middle_left`, `center`, `middle_right`, `bottom_left`,
`bottom_center`, `bottom_right` or `hotbar_right` (beside the hotbar). `x` and `y` are GUI pixels from that point.
`scale` runs from 0.25 to 4 and `opacity` from 0.1 to 1. Anything left out keeps the element's default. Settings for an
element that isn't registered yet are kept and apply once it is.

The older `config/fundamentum-hud.json` (order and on/off only) is read once when the new file is missing, then
renamed to `fundamentum-hud.json.old`.

## For mods

Register the element on the client with its size, and draw it from 0, 0 inside its own box:

    HudLayerRenderer.register(Identifier.fromNamespaceAndPath("mymod", "mana_bar"), 100, true,
        new HudLayout.Placement(HudBox.Anchor.BOTTOM_LEFT, 4, -4), () -> 82, () -> 7,
        (g, delta) -> drawBar(g));

- The width and height suppliers are asked every frame, so return a stored number. A size of 0 draws nothing.
- Pass colors through `HudLayerRenderer.fade(argb)` so the player's opacity applies.
- The `Placement` is the default, and the target of Reset.
- `register(id, order, drawer)` without a size still works. That layer draws in screen space, and the editor can switch
  it off and move or scale it as a whole.
- `HudLayers.setEnabled`, `setOrder` and `setHideAll` change things from code. `HudLayout.version()` goes up on every
  change, so a drawer can keep its layout cached until it moves.

On 1.21.1 the id is a `ResourceLocation` and the drawer takes `(GuiGraphics, DeltaTracker)`. On 1.20.1 it is
`new ResourceLocation(ns, path)` and the drawer takes `(GuiGraphics, float partialTick)`.

Fundamentum's own elements are `fundamentum:item_hud`, `fundamentum:stats`, `fundamentum:survival` (meters over the
hunger bar), `fundamentum:survival_left` (meters over the hearts) and `fundamentum:boss_bars`.

## Redrawing only on change

The HUD, the stats and survival meters and the multiblock ghost preview rebuild what they draw only when something
changes: a synced value, a declaration, the layout, a block in the preview area or a resource reload. Each keeps its
last result and a version number to compare against. As a safety net they also recheck on a slow timer, set by
`refresh.safetyRecheck` in `config/fundamentum-hud-client.toml` (seconds, default 5, 0 turns it off). See
[Performance Client](performance-client.md) for the numbers.
