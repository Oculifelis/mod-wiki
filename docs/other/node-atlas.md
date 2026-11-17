# Node Atlas

Node Atlas keeps a log of found aura nodes and points an arrow back to the one that is needed. Logged nodes also show on JourneyMap, Xaero's maps and FTB Chunks. This is a client addon for [Thaumaturge](https://www.curseforge.com/projects/1628024), based on Thaumcraft Node Tracker by Dyonovan and GTNewHorizons.

**Requires** Thaumaturge 1.1.0 or newer. It goes on the client and adds nothing to a dedicated server.

| Minecraft | Loader | Node Atlas |
|---|---|---|
| 26.1.2 | NeoForge 26.1.2.122 or newer | 0.2.0 |
| 1.21.1 | NeoForge 21.1.259 or newer | 0.2.0 |

[Public downloads](https://www.curseforge.com/projects/1796713)

## Using the log

Right-clicking a node with a Thaumometer, or while wearing Goggles of Revealing, saves its position, type, modifier and aspects. Scanning it again updates the entry. Each world or server has its own log.

The list opens with the `I` key. It filters by primal aspect, sorts by distance or by an aspect, and marks a node. While revealing goggles are worn, an arrow points toward the marked node and shows its distance and whether it is above or below. **Del** forgets an entry.

The config sets the arrow's position and size, or switches it to a plain red arrow.

## Maps

Logged nodes show as markers on [JourneyMap](https://www.curseforge.com/projects/32274), as temporary waypoints on [Xaero's Minimap](https://www.curseforge.com/projects/263420) and as icons on [FTB Chunks](https://www.curseforge.com/projects/314906). [Xaero's World Map](https://www.curseforge.com/projects/317780) shows the same waypoints when Xaero's Minimap is installed too. All of these maps are optional.

Each node type has its own marker colour and shape, and the marked node shows in cyan. Temporary waypoints are never written to Xaero's waypoint files. The client config turns each map off and can add type labels under JourneyMap markers.

## Resource packs

Marker colours, outlines, shapes and sizes, plus the Xaero waypoint colour, come from `assets/nodeatlas/map_markers.json`. The file has one entry per node type and one for the marked node. A resource pack can replace it. Shapes are a diamond, a circle or a square.

## Licence

Node Atlas is licensed under CC BY-NC-SA 4.0, like the original Thaumcraft Node Tracker by Dyonovan and GTNewHorizons. Port by Oculifelis. The arrow and map markers are drawn in code, and aspect icons come from Thaumaturge by Leclowndu93150 and contributors. The original's Navigator is not part of the port.

## Compatibility

Works with [Better Combat](https://www.curseforge.com/projects/639842) (optional) on 1.21.1.

Works with [Jade](https://www.curseforge.com/projects/324717) (optional) on 1.21.1.

Works with JourneyMap, Xaero's Minimap, Xaero's World Map and FTB Chunks (all optional) on 1.21.1 and 26.1.2.
