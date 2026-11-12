# Energy and fluid transfer (`com.fundamentum.transfer`)

Small helpers over the loader's own energy and fluid capabilities. There is no new energy unit: a block exposed here
shows up to every other mod as an ordinary energy or fluid handler, and other mods' blocks can be read and filled
through the same calls. One call works on every version; the differences live in `port/FTransfer`.

## Stores

    EnergyBuffer buf = new EnergyBuffer(10_000, 200, 200).onChange(this::setChanged);   // capacity, max in, max out
    buf.insert(500, false);  buf.extract(100, true);    // outside calls, held to the per-call limits
    buf.add(5000);  buf.consume(80);  buf.tryConsume(80);   // the owner's calls, ignore the limits

    FluidTank in = new FluidTank(4000).filter(f -> f == Fluids.WATER).access(true, false).onChange(this::setChanged);
    FluidTank out = new FluidTank(4000).access(false, true);
    FluidTanks both = FluidTanks.of(in, out);
    out.fill(Fluids.LAVA, 1000, false);    // the owner fills a tank outsiders can only drain

Amounts are ints, in energy units and millibuckets. `simulate` changes nothing and runs no listener. A filled
`FluidTanks` puts a fluid into tanks that already hold it before an empty one. Fluids that carry extra data
(components or NBT) are refused. Save a tank with `FluidTank.Contents.CODEC` (`contents()` and `load(...)`); a fluid
missing from the game loads as empty.

## Exposing a block

Call while the mod loads, once per block entity type:

    Transfer.exposeEnergy(MY_BE, (be, side) -> be.energy);
    Transfer.exposeTank(MY_BE, (be, side) -> side == Direction.UP ? null : be.tank);
    Transfer.exposeFluids(FId.of("mymod", "boiler"), (be, side) -> be.tanks);

Return null for a side that has none. On NeoForge 26.x outside calls run in the loader's transactions: an aborted
transaction puts the buffer back, and `onChange` runs once when the outer transaction commits. On 1.21.1 and 1.20.1
the loader simulates with a flag, so the calls go straight through.

## Reading and moving

    EnergyStore e = Transfer.energy(level, pos, Direction.NORTH);    // null when there is none
    FluidStore f = Transfer.fluids(level, pos, null);
    Transfer.moveEnergy(from, to, 1000);  Transfer.moveFluid(from, to, 1000);  Transfer.moveFluid(from, to, Fluids.WATER, 1000);
    Transfer.pushEnergy(level, pos, buf, 200);  Transfer.pullFluid(level, pos, tank, 1000);   // every neighbour in turn

Moves simulate first and only take what the other side accepts. Push and pull go over the six neighbours, each asked
from the side facing this block.

## Tanks in screens

    Transfer.track(this, tank);    // in the block entity's onLoad, server side; removed block entities drop out by themselves

Tracked tanks are sent to players within 64 blocks every half second when they change or a player comes in range.
On the client `Transfer.clientTank(pos, index)` reads them, and `transfer.client.TankWidget` draws one (the fluid's
texture, tinted, from the bottom up) with the usual name and amount tooltip. A menu that keeps its own copy of a
tank can pass the `FluidTank` straight to the widget.

## Item to fluid

"This item holds this much fluid and leaves this item behind": `data/<ns>/fundamentum/item_fluid/<path>.json`

    {"item": "minecraft:water_bucket", "fluid": "minecraft:water", "amount": 1000, "remainder": "minecraft:bucket"}

`amount` defaults to 1000; `remainder` is optional. In code: `ItemFluids.add(id, item, fluid, amount, remainder)`.
A data file with the same id replaces a code entry. Fundamentum does nothing with these by itself; a machine asks
`ItemFluids.find(stack)` or `ItemFluids.forFluid(fluid)`. They are synced to players and shown in recipe viewers as
the `fundamentum:item_to_fluid` category.

## Command

`/fundamentum transfer <pos>` prints the energy and tanks a block exposes. Operators only. Returns 1 when the block has
either.

## Test

`gradlew runServer -Ptransfertest` (world under `run-transfertest`) exposes stores on vanilla barrels and checks
lookups through the loader capability, limits, simulation, sides, push and pull, filters and fill/drain access,
listeners, the save and sync codecs, the client tank map, item-to-fluid data and code entries, the recipe view
category and the command. It ends with `TRANSFERTEST RESULT PASS` or `FAIL`.
