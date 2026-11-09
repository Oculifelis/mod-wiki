# Modules

A module goes on one side of a chassis. All the modules on a chassis share its item stores, tanks, RF buffer and signal
channels. Names and descriptions are the in-game ones; the manual has each module's live numbers and recipes.

![All 77 modules](img/modules.png)

## Processing

Turn one thing into another, using items, fluids and RF from the chassis. 24 modules.

| Module | What it does |
|---|---|
| **Alloy Smelter** | Melts metals together into alloys: bronze, invar, electrum and more (Induction Smelter). |
| **Armor Infuser** | Fills fluid armor in a lane with effect fluid from a reservoir (FLORA's Fluidic Armor Infuser). |
| **Bio-Digester** | Turns seeds, saplings, leaves and other farm waste with water into biogas (for a Fluid Engine) and compost (bone meal for the Crop Tender). |
| **Blast Chiller** | Freezes fluids into solids: water into ice, lava into obsidian. |
| **Brewer** | Brews potions like a brewing stand, paid in RF (Alchemical Imbuer). |
| **Centrifuge** | Spins items (and fluids) apart into their parts (Centrifugal Separator). |
| **Crusher** | Breaks items down; some recipes yield byproducts. |
| **Enchanter** | Enchants items like an enchanting table, paid in liquid experience and RF (Arcane Ensorcellator). |
| **Fluid Transposer** | Fills containers from a reservoir or empties them into one. |
| **Glacial Precipitator** | Turns water into snow and ice with RF. |
| **Heater** | Smelts using furnace recipes, paid for in RF. |
| **Insolator** | Grows crops and saplings from a catalyst seed with water and RF (Phytogenic Insolator). |
| **Item Charger** | Charges RF-holding items; full items move to the output lane (Energetic Infuser). |
| **Magma Crucible** | Melts items into fluids: stone into lava, redstone into redstone flux. |
| **Mixer** | Combines items with a fluid. |
| **Press** | Compacts and presses items. |
| **Pyrolyzer** | Bakes coal and wood into coke and charcoal, releasing creosote (Pyrolytic Converter). |
| **Recipe Assembler** | Crafts from a ghost pattern using items in the input lane. |
| **Refinery** | Refines one fluid into another plus a solid byproduct (Fractionating Still). |
| **Sawmill** | Saws logs into planks with sawdust as a byproduct (Thermal's Sawmill). |
| **Stone Extruder** | Makes cobblestone, stone or obsidian from lava and water (Igneous Extruder). |
| **Tag Unifier** | Turns ingots, nuggets, dusts, plates and gears from any mod into the one your pack prefers (Metallurgy's, then vanilla's), for a little RF. |
| **Tool Repairer** | Mends damaged tools and armour from Orange storage with liquid experience from the Orange tank, at the Mending rate; finished items go to Green. |
| **Washer** | Washes items with water to separate useful byproducts. |

## Power

Make RF into the chassis buffer. 22 modules.

| Module | What it does |
|---|---|
| **Arcane Engine** | Consumes enchanted items for RF by their enchantment levels (Disenchantment Dynamo). |
| **Blast Damper** | Cancels explosions within 6 blocks and stores their energy (a creeper: 31,500 RF). On a Reinforced chassis it also detonates TNT from Purple storage. |
| **Boiler** | Turns water from a tank into steam. Burns furnace fuel, or runs on heat alone when lava or magma touches it. |
| **Cold Junction** | The cold side for a Hot Junction on the same machine: put it against water, ice or snow. |
| **Condenser** | Lets a Steam Turbine on the same machine return its steam as water: most of it when this side touches water, ice or snow, half in open air. |
| **Fluid Engine** | Burns fluid fuels listed in the fuels data into RF (Magmatic/Compression Dynamo). |
| **Food Engine** | Turns food into RF by its hunger value (Gourmand Dynamo). |
| **Fuel Engine** | Burns furnace fuel into the RF buffer. |
| **Galvanic Cell** | A battery from two metals: the less noble one in Orange storage is used up, the nobler one in Purple stays. Needs water in the Orange tank. |
| **Gem Engine** | Turns gems listed in the fuels data into RF (Lapidary/Numismatic Dynamo). |
| **Geothermal Probe** | Bottom side only: taps the ground's heat. Works deep down (best below height 0), much better over lava or magma, at any height in the Nether. Probes close together share the heat. |
| **Hand Crank** | Right-click it with an empty hand to turn it: 20 RF/t while it turns, for a little hunger. Hold the button to keep it going. Your first power before any fuel. |
| **Hot Junction** | Makes RF from the temperature difference between the block in front of it and the block in front of a Cold Junction on the same machine. A working Heater counts as warm. Two different metals in Purple storage (zinc and gold, say) make it up to twice as strong. |
| **Lunar Prism** | Top side only: the Solar Collector's night twin. Makes up to 16 RF/t under a full moon, less as the moon wanes, nothing at new moon. |
| **Motion Harvester** | Turns the movement of nearby creatures into a trickle of RF. |
| **Redstone Engine** | Turns redstone into RF (Enervation Dynamo). |
| **Solar Collector** | Generates RF in daylight with open sky. Top face only. |
| **Steam Turbine** | Burns steam for RF. The rotor takes about 15 seconds to reach full speed; a Condenser on the same machine turns the spent steam back into water. |
| **Storm Coil** | Top side only, under a Lightning Rod: each strike stores 200,000 RF and feeds it to the machine. Signals each strike and how full it is. |
| **Treadmill** | Lead an adult animal into the block in front: it walks in place for RF while it eats its food from Purple storage (a cow 6 RF/t, a fast horse up to 13). |
| **Waterwheel/Turbine Interface** | Flowing water makes RF; turbine mode burns a stored fluid. |
| **Wind Rotor** | Turns in the wind: better high up, in open air and in storms. Rotors close together share the wind. |

## World

Work on the blocks and mobs in front of them. 12 modules.

| Module | What it does |
|---|---|
| **Aura Chamber** | Takes a batch of metal blocks and surrounds nearby players with that metal's effect while it runs on RF (Metallurgy's chamber). |
| **Block Breaker** | Breaks the block in front with a real tool and collects the real drops. |
| **Block Placer** | Places blocks from a lane in front of the face. |
| **Crop Tender** | Harvests ripe crops in a small area and replants them. |
| **Entity Mover** | Pushes or pulls creatures in front of the face. |
| **Experience Collector** | Absorbs experience orbs in front into liquid experience. |
| **Fisher** | Fishes from open water in front; bait speeds it up. |
| **Hydraulic Excavator** | Works a bounded area layer by layer with a tool, water and RF. |
| **Interaction Head** | Right-clicks the block in front with the held stack, as the chassis owner. |
| **Mob Grinder** | Attacks mobs in front with the weapon in Purple storage (its enchantments count, and it wears); drops go to Green, experience to a tank. Never players; named mobs only if you allow it. |
| **Tree Tapper** | Draws tree sap (or latex) from the log in front without harming it (Tree Extractor). |
| **Water Collector** | Collects water from two or more source blocks in front (Aqueous Accumulator). |

## Handling

Move items, fluids and power in and out of the chassis. 11 modules.

| Module | What it does |
|---|---|
| **Combined Service Port** | Item, fluid and RF access through one face, each with its own per-tick limit. |
| **Drop Collector** | Picks up dropped items from a small area in front of the face. |
| **Fluid Port** | Connects one fluid reservoir to the neighbouring tank; never mixes fluids. |
| **Inventory Access Panel** | Lets players open the item lanes this panel permits. |
| **Item Ejector** | Drops items into the world in front of the face, with delay and quantity limits. |
| **Item Port** | Connects one item lane to the neighbouring inventory: passive access or active import/export. |
| **Nullifier** | Destroys matching items (and a bound fluid) once armed. Deletion is permanent. |
| **Power Terminal** | Exchanges RF with neighbours through the standard energy interface. |
| **Storage Sorter** | Moves items matching its filter from one of the machine's storages to another (Green to Purple unless you change it), never out of the machine. |
| **Tank Access Panel** | Lets players fill and empty permitted reservoirs with containers. |
| **World Fluid Pump** | Collects source blocks from a small area, or places fluid back into it. |

## Control

Read and write the eight signal channels. 7 modules.

| Module | What it does |
|---|---|
| **Controller Plate** | Runs a small rule program over lanes, RF, channels, registers and states. |
| **Environment Sensor** | Signals daylight, rain or open sky. |
| **Logic Plate** | AND / OR / XOR / NAND / NOR / XNOR / NOT / BUFFER over two channels. |
| **Memory Plate** | Set / reset / toggle latch. Reset beats set beats toggle. |
| **Resource Sensor** | Signals when a lane, reservoir or the RF buffer crosses thresholds. |
| **Signal Terminal** | Bridges world redstone and an internal control channel. |
| **Timer/Counter Plate** | Emits timed pulses or counts rising edges. |

## Display

Show what is going on. 1 modules.

| Module | What it does |
|---|---|
| **Indicator Panel** | Shows a channel on its face: the green lamp lights when it is on, amber from 8, red at 15, and the bar fills with the level. |
