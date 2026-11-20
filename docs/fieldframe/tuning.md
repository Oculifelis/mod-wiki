# Tuning keys

Every machine number below can be changed from a datapack (`data/<pack>/fieldframe/tuning/*.json`) or a KubeJS
`FieldframeEvents.tuning` script. Values outside the range are rejected with the rest of that batch.

```json
{"module": "fieldframe:fisher", "tunables": {"interval": 300}}
```

Most processing machines take `speed` (a multiplier on how fast an operation runs) and `energy_multiplier`
(a multiplier on the RF it costs).

## Processing

| Module | Key | Default | Range |
|---|---|---|---|
| Alloy Smelter (`fieldframe:alloy_smelter`) | `speed` | 1x | 0.1 to 16 |
|  | `energy_multiplier` | 1x | 0 to 16 |
| Armor Infuser (`fieldframe:armor_infuser`) | `mb_per_tick` | 100mB/t | 1 to 10000 |
|  | `rf_per_mb` | 2RF/mB | 0 to 1000 |
| Bio-Digester (`fieldframe:bio_digester`) | `speed` | 1x | 0.1 to 16 |
|  | `energy_multiplier` | 1x | 0 to 16 |
| Blast Chiller (`fieldframe:blast_chiller`) | `speed` | 1x | 0.1 to 16 |
|  | `energy_multiplier` | 1x | 0 to 16 |
| Brewer (`fieldframe:brewer`) | `rf_per_brew` | 400RF | 0 to 100000 |
|  | `interval` | 100ticks | 1 to 1200 |
| Centrifuge (`fieldframe:centrifuge`) | `speed` | 1x | 0.1 to 16 |
|  | `energy_multiplier` | 1x | 0 to 16 |
| Crusher (`fieldframe:crusher`) | `speed` | 1x | 0.1 to 16 |
|  | `energy_multiplier` | 1x | 0 to 16 |
| Enchanter (`fieldframe:enchanter`) | `level` | 30 | 1 to 30 |
|  | `mb_per_level` | 100mB | 0 to 10000 |
|  | `rf_per_enchant` | 4000RF | 0 to 1000000 |
|  | `interval` | 100ticks | 1 to 1200 |
| Fluid Transposer (`fieldframe:fluid_transposer`) | `speed` | 1x | 0.1 to 16 |
|  | `energy_multiplier` | 1x | 0 to 16 |
| Glacial Precipitator (`fieldframe:glacial_precipitator`) | `speed` | 1x | 0.1 to 16 |
|  | `energy_multiplier` | 1x | 0 to 16 |
| Heater (`fieldframe:heater`) | `speed` | 1x | 0.1 to 16 |
|  | `energy_multiplier` | 1x | 0 to 16 |
| Insolator (`fieldframe:insolator`) | `speed` | 1x | 0.1 to 16 |
|  | `energy_multiplier` | 1x | 0 to 16 |
| Item Charger (`fieldframe:item_charger`) | `rf_per_tick` | 1000RF/t | 1 to 1000000 |
| Magma Crucible (`fieldframe:magma_crucible`) | `speed` | 1x | 0.1 to 16 |
|  | `energy_multiplier` | 1x | 0 to 16 |
| Mixer (`fieldframe:mixer`) | `speed` | 1x | 0.1 to 16 |
|  | `energy_multiplier` | 1x | 0 to 16 |
| Press (`fieldframe:press`) | `speed` | 1x | 0.1 to 16 |
|  | `energy_multiplier` | 1x | 0 to 16 |
| Pyrolyzer (`fieldframe:pyrolyzer`) | `speed` | 1x | 0.1 to 16 |
|  | `energy_multiplier` | 1x | 0 to 16 |
| Recipe Assembler (`fieldframe:recipe_assembler`) | `rf_per_craft` | 20RF | 0 to 10000 |
|  | `interval` | 10ticks | 1 to 200 |
| Refinery (`fieldframe:refinery`) | `speed` | 1x | 0.1 to 16 |
|  | `energy_multiplier` | 1x | 0 to 16 |
| Sawmill (`fieldframe:sawmill`) | `speed` | 1x | 0.1 to 16 |
|  | `energy_multiplier` | 1x | 0 to 16 |
| Stone Extruder (`fieldframe:stone_extruder`) | `min_mb` | 1000mB | 1 to 64000 |
|  | `obsidian_lava_mb` | 1000mB | 1 to 64000 |
|  | `rf_per_block` | 0RF | 0 to 100000 |
|  | `rf_stone` | 40RF | 0 to 100000 |
|  | `interval` | 20ticks | 1 to 1200 |
| Tag Unifier (`fieldframe:tag_unifier`) | `rf_per_item` | 20RF | 0 to 10000 |
|  | `items_per_tick` | 4items | 1 to 64 |
| Tool Repairer (`fieldframe:tool_repairer`) | `points_per_tick` | 2XP | 1 to 100 |
|  | `durability_per_point` | 2uses | 1 to 20 |
|  | `mb_per_point` | 20mB | 1 to 1000 |
| Washer (`fieldframe:washer`) | `speed` | 1x | 0.1 to 16 |
|  | `energy_multiplier` | 1x | 0 to 16 |

## Generation

| Module | Key | Default | Range |
|---|---|---|---|
| Arcane Engine (`fieldframe:arcane_engine`) | `rf_per_tick` | 80RF/t | 1 to 100000 |
|  | `rf_per_level` | 4000RF | 0 to 1000000 |
| Blast Damper (`fieldframe:blast_damper`) | `capture_radius` | 6blocks | 1 to 16 |
|  | `rf_per_power2` | 3500RF | 0 to 1000000 |
|  | `capacity` | 500000RF | 1000 to 100000000 |
|  | `release_per_tick` | 512RF/t | 1 to 100000 |
|  | `chamber_tier` | 2tier | 0 to 10 |
|  | `chamber_interval` | 100ticks | 20 to 12000 |
| Boiler (`fieldframe:boiler`) | `steam_per_tick` | 20mB/t | 1 to 1000 |
|  | `burn_divisor` | 4x | 0.25 to 64 |
|  | `heat_kelvin` | 600K | 300 to 10000 |
|  | `heat_factor` | 0.25x | 0 to 1 |
| Field Receiver (`fieldframe:field_receiver`) | `rf_per_tick` | 1024RF/t | 0 to 1000000 |
| Fluid Engine (`fieldframe:fluid_engine`) | `rf_per_tick` | 80RF/t | 1 to 100000 |
|  | `mb_per_batch` | 10mB | 1 to 1000 |
| Food Engine (`fieldframe:food_engine`) | `rf_per_tick` | 40RF/t | 1 to 100000 |
|  | `rf_per_point` | 1600RF | 0 to 1000000 |
| Fuel Engine (`fieldframe:fuel_engine`) | `rf_per_tick` | 40RF/t | 1 to 10000 |
|  | `burn_divisor` | 4x | 0.25 to 64 |
|  | `bucket_max_ticks` | 1250ticks | 1 to 100000 |
| Galvanic Cell (`fieldframe:galvanic_cell`) | `rf_per_volt` | 25RF/t per V | 0 to 10000 |
|  | `max_rf_per_tick` | 128RF/t | 0 to 100000 |
|  | `anode_ticks` | 1200ticks | 1 to 1000000 |
|  | `electrolyte_per_tick` | 1mB/t | 1 to 1000 |
| Gem Engine (`fieldframe:gem_engine`) | `rf_per_tick` | 80RF/t | 1 to 100000 |
| Geothermal Probe (`fieldframe:geothermal_probe`) | `max_rf_per_tick` | 60RF/t | 0 to 10000 |
|  | `full_depth_y` | 0y | -64 to 320 |
|  | `half_depth_y` | 40y | -64 to 320 |
|  | `nether_factor` | 1x | 0 to 8 |
|  | `share_radius` | 24blocks | 0 to 64 |
|  | `check_interval` | 100ticks | 20 to 1200 |
| Hand Crank (`fieldframe:hand_crank`) | `rf_per_tick` | 20RF/t | 0 to 1000 |
|  | `ticks_per_turn` | 10ticks | 1 to 200 |
|  | `max_queue` | 20ticks | 1 to 1200 |
| Hot Junction (`fieldframe:hot_junction`) | `rf_per_kelvin` | 0.02RF/t per K | 0 to 10 |
|  | `max_rf_per_tick` | 32RF/t | 0 to 10000 |
|  | `waste_max` | 5RF/t | 0 to 10000 |
|  | `check_interval` | 40ticks | 20 to 1200 |
| Lunar Prism (`fieldframe:lunar_prism`) | `rf_per_tick` | 16RF/t | 0 to 1000 |
|  | `rain_factor` | 0.5x | 0 to 1 |
|  | `check_interval` | 100ticks | 20 to 1200 |
| Motion Harvester (`fieldframe:motion_harvester`) | `enabled` | 1 | 0 to 1 |
|  | `rf_per_speed` | 40RF | 0 to 1000 |
|  | `max_rf_per_tick` | 10RF/t | 0 to 1000 |
|  | `max_entities` | 4 | 1 to 16 |
| Redstone Engine (`fieldframe:redstone_engine`) | `rf_per_tick` | 60RF/t | 1 to 100000 |
| Solar Collector (`fieldframe:solar_collector`) | `rf_per_tick` | 8RF/t | 0 to 1000 |
|  | `rain_factor` | 0.25x | 0 to 1 |
|  | `check_interval` | 100ticks | 20 to 1200 |
| Steam Turbine (`fieldframe:steam_turbine`) | `max_steam` | 40mB/t | 1 to 10000 |
|  | `rf_per_mb` | 4RF/mB | 0 to 1000 |
|  | `spin_up_ticks` | 300ticks | 1 to 6000 |
|  | `coast_ticks` | 600ticks | 1 to 12000 |
|  | `cold_return` | 0.9x | 0 to 1 |
|  | `air_return` | 0.5x | 0 to 1 |
|  | `cold_kelvin` | 300K | 1 to 10000 |
| Storm Coil (`fieldframe:storm_coil`) | `strike_rf` | 200000RF | 0 to 100000000 |
|  | `capacity` | 400000RF | 1000 to 100000000 |
|  | `release_per_tick` | 512RF/t | 1 to 100000 |
| Treadmill (`fieldframe:treadmill`) | `feed_ticks` | 1200ticks | 20 to 72000 |
|  | `coast_ticks` | 2400ticks | 1 to 72000 |
|  | `hold_interval` | 5ticks | 1 to 100 |
| Waterwheel/Turbine Interface (`fieldframe:waterwheel_interface`) | `rf_per_flow` | 3RF/t | 0 to 1000 |
|  | `check_interval` | 100ticks | 20 to 1200 |
|  | `mb_per_tick` | 5mB/t | 1 to 1000 |
|  | `rf_per_mb` | 12RF/mB | 0 to 1000 |
| Wind Rotor (`fieldframe:wind_rotor`) | `max_rf_per_tick` | 32RF/t | 0 to 10000 |
|  | `min_height` | 64y | -64 to 512 |
|  | `full_height` | 192y | -64 to 512 |
|  | `clear_factor` | 0.6x | 0 to 4 |
|  | `rain_factor` | 1x | 0 to 4 |
|  | `thunder_factor` | 1.4x | 0 to 4 |
|  | `nether_factor` | 0x | 0 to 4 |
|  | `end_factor` | 0.5x | 0 to 4 |
|  | `share_radius` | 4blocks | 0 to 32 |
|  | `check_interval` | 100ticks | 20 to 1200 |

## World

| Module | Key | Default | Range |
|---|---|---|---|
| Aura Chamber (`fieldframe:aura_chamber`) | `rf_per_tick` | 20RF/t | 0 to 10000 |
|  | `range` | 6blocks | 1 to 16 |
|  | `interval` | 20ticks | 1 to 200 |
|  | `use_amplifier` | 0 | 0 to 1 |
| Block Breaker (`fieldframe:block_breaker`) | `rf_per_block` | 60RF | 0 to 10000 |
|  | `interval` | 10ticks | 1 to 200 |
| Block Placer (`fieldframe:block_placer`) | `rf_per_block` | 20RF | 0 to 10000 |
|  | `interval` | 10ticks | 1 to 200 |
| Crop Tender (`fieldframe:crop_tender`) | `rf_per_action` | 20RF | 0 to 10000 |
|  | `interval` | 10ticks | 1 to 200 |
| Entity Mover (`fieldframe:entity_mover`) | `allow_players` | 1 | 0 to 1 |
|  | `max_strength` | 1b/t | 0.1 to 2 |
|  | `max_entities` | 8 | 1 to 32 |
|  | `rf_per_entity` | 4RF | 0 to 1000 |
|  | `interval` | 4ticks | 1 to 200 |
| Experience Collector (`fieldframe:xp_collector`) | `range` | 4blocks | 1 to 8 |
|  | `mb_per_point` | 20mB | 1 to 1000 |
|  | `interval` | 10ticks | 1 to 200 |
| Fisher (`fieldframe:fisher`) | `min_water` | 6 | 1 to 9 |
|  | `rf_per_catch` | 200RF | 0 to 100000 |
|  | `interval` | 600ticks | 20 to 12000 |
| Hydraulic Excavator (`fieldframe:hydraulic_excavator`) | `rf_per_block` | 240RF | 0 to 100000 |
|  | `fluid_per_block` | 100mB | 0 to 4000 |
|  | `interval` | 8ticks | 1 to 200 |
| Interaction Head (`fieldframe:interaction_head`) | `rf_per_use` | 30RF | 0 to 10000 |
|  | `interval` | 20ticks | 1 to 200 |
| Mob Grinder (`fieldframe:mob_grinder`) | `range` | 2blocks | 1 to 3 |
|  | `interval` | 20ticks | 5 to 200 |
|  | `max_targets` | 3mobs | 1 to 8 |
|  | `rf_per_attack` | 60RF | 0 to 10000 |
|  | `mb_per_point` | 20mB | 1 to 1000 |
| Tree Tapper (`fieldframe:tree_tapper`) | `mb_per_tap` | 10mB | 1 to 1000 |
|  | `interval` | 40ticks | 1 to 1200 |
| Water Collector (`fieldframe:water_collector`) | `min_sources` | 2 | 1 to 9 |
|  | `mb_per_source` | 25mB | 1 to 1000 |
|  | `interval` | 20ticks | 1 to 1200 |

## Handling

| Module | Key | Default | Range |
|---|---|---|---|
| Drop Collector (`fieldframe:drop_collector`) | `items_per_pickup` | 16items | 1 to 256 |
|  | `interval` | 5ticks | 1 to 200 |
| Field Coil (`fieldframe:field_coil`) | `rf_per_tick` | 4096RF/t | 0 to 1000000 |
|  | `radius_per_coil` | 4blocks | 1 to 16 |
| Nullifier (`fieldframe:nullifier`) | `items_per_tick` | 16 | 1 to 4096 |
|  | `mb_per_tick` | 1000mB | 1 to 64000 |
| Power Terminal (`fieldframe:power_terminal`) | `push_rf_per_tick` | 256RF/t | 1 to 100000 |
| Storage Sorter (`fieldframe:storage_sorter`) | `items_per_tick` | 8items | 1 to 64 |
| World Fluid Pump (`fieldframe:world_fluid_pump`) | `rf_per_block` | 40RF | 0 to 10000 |
|  | `interval` | 10ticks | 1 to 200 |
