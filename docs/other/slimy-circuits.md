# Slimy Circuits

This mod puts redstone wiring on the surface of any solid block. Paste, sticky repeaters, sticky comparators and a set of logic parts go on floors, walls and ceilings, with no collision box and no room taken up in the block space.

Recipes, recipe advancements and the guide book are datapack JSON, so packs and scripts can change them.

## Paste

Redstone Paste is made from redstone and a slime ball. Each surface has four arms and a centre dot, and the spot clicked picks the arm. Every new arm costs one paste. Sneaking while clicking adds an arm and the one opposite it. Left click takes paste off again.

Paste carries a signal from 0 to 15 and loses one strength per space. Trails join where their arms meet, around inside corners and around outside corners. A floor trail joins vanilla dust only where an arm points at the dust.

## Sticky repeaters and comparators

A sticky repeater is a repeater and a slime ball. It sits on any face, and right click cycles the delay from 1 to 4. A repeater or comparator pointing into its side locks it.

A sticky comparator reads a container, an item frame or a plain signal behind it. Right click switches between compare and subtract.

## Logic parts

All parts sit on any face and switch after 2 game ticks unless noted.

| Part | Behaviour |
|---|---|
| AND, OR, XOR, NAND, NOR, XNOR | Two side inputs, output at the front |
| NOT | Reads the back |
| R-S Flip-Flop | Left side sets, right side resets, reset wins |
| Rain Detector, Thunder Detector | On during that weather with open sky above |
| Redstone Clock | Pulses with a period of 10, 20, 30 or 40 ticks per half |
| Advanced Redstone Clock | 2 tick pulse every 1, 2, 3 or 4 seconds |
| Fast Repeater | Passes the back signal after 1 tick |
| Slow Repeater | Waits 1 to 4 seconds |
| Rotary Switch | Sends the back signal to the front, left or right |
| Wireless Transmitter, Wireless Receiver | 16 frequencies, same dimension |
| Timer | Fires a 2 tick pulse after the back input has been off for 1, 2, 5, 10, 20, 30 or 60 seconds, then repeats. An input resets it |
| Pulse Former | Gives a 2 tick pulse when the back input turns on, or when it turns off, depending on the setting |
| Toggle Latch | Flips its output each time the back input turns on. Either side input forces it off |
| Counter | Left side counts up, right side counts down, from 0 to 15. Output is on when the count reaches the target set from 1 to 15. Small studs show the count |
| Multiplexer | The back input picks the left or right side input for the output |
| Synchronizer | Gives a 2 tick pulse when the left, right and back inputs are all on |
| Randomizer | Each time the back input turns on, the output goes on or off at random |

## Slab covers

Right clicking a circuit that holds one surface with a slab covers that surface. Left click takes the cover off.

## Versions and requirements

| Minecraft | Loader | Version | Needs |
|---|---|---|---|
| 1.20.1 | Forge | 1.2.0 | [Patchouli](https://www.curseforge.com/projects/306770) |
| 1.21.1 | NeoForge | 1.2.0 | [Patchouli](https://www.curseforge.com/projects/306770) |
| 26.1.2 | NeoForge | 1.2.0 | [Patchouli](https://www.curseforge.com/projects/306770) |
| 26.2 | NeoForge | 1.2.0 | [Patchouli](https://www.curseforge.com/projects/306770) |
| 26.3 | NeoForge | 1.2.0 | Patchouli optional |

[CurseForge project](https://www.curseforge.com/projects/1812033)

The gate faces are based on the Gates content by se7kn8 (MIT).
