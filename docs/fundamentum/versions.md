# Versions

| Minecraft | Loader | Fundamentum | Notes |
|---|---|---|---|
| 26.1.2 | NeoForge | 1.25.1 | the main line: everything on this wiki |
| 1.21.1 | NeoForge 21.1 | 1.25.0 | everything except a few parts that need newer Minecraft (below) |
| 26.2 | NeoForge | 1.14.1 | older: no whips, elements, portal crafting, fractal skies, glow or curves |
| 1.20.1 | Forge 47 | 1.14.1 | older still: also no summons, damage classes, shared damage types, poses or triggers |

## What 1.21.1 leaves out

- Wings drawn from an equipment asset's `wings` layer (wings still work as a slot item; mods draw their own).
- Item model faces with `light_emission`: glowing faces use `neoforge_data` light in the model instead.
- Whip item model conditions are `ItemProperties` overrides instead of item model definitions.
- The `on_shelf` display context.
- A recipe book category for portal crafting (JEI still shows the recipes).
- Mounts saddle through `Saddleable`; mobs that only exist on 26.x (the happy ghast, the nautilus) aren't there.
