# Slots

Fundamentum's accessory slots: `wings` (with a cosmetic twin), `mount`, `hook`, `summon` and `quiver`, on players. They
are Curios slots, read and written through one API, `com.fundamentum.slots.Slots`.

Package `com.fundamentum.slots`, every version (NeoForge 26.1.2, 26.2, 26.3, 1.21.1; Forge 1.20.1).

## Curios

- Fundamentum requires Curios on every version (`type="required"` on NeoForge, `mandatory=true` on Forge).
- The slots are defined as data in `data/fundamentum/curios/` (slot `wings` has `add_cosmetic`). Every `Slots` call goes
  to Curios, so slots other mods add through Curios are readable too.
- They show in Curios' own screen. The cosmetic armour screen holds only the cosmetic armour.
- Older versions kept the slots themselves when Curios was missing (`fundamentum:slots` on the player). That store is
  gone, and whatever was in it is not moved into Curios.

## Which items go in a slot

An item may go in a slot when it is in the item tag `#curios:<slot>` (`#curios:wings`, `#curios:quiver` ...), the same tag
Curios reads, or when a validator added for that slot accepts it:

```java
Slots.validator(Slots.QUIVER, stack -> stack.getItem() instanceof MyQuiverItem);
Slots.allows(Slots.QUIVER, stack);   // what the screen and tryEquip check
```

Curios' screen checks its own rules (the tag, plus whatever the item says through Curios). Validators only feed
`allows` and `tryEquip`.

## Reading

```java
Slots.equipped(player, Slots.WINGS);        // first worn item in a slot type, or empty
Slots.allEquipped(player, Slots.SUMMON);    // every worn item of a type
Slots.get(player, Slots.HOOK, 0);           // one slot; getCosmetic(...) for a cosmetic twin
Slots.size(player, Slots.SUMMON);           // how many (Curios slot modifiers can raise it); cosmeticSize(...)
Slots.firstMatching(player, s -> s.is(MyItems.CHARM));            // Optional<Worn>: slot, index, stack
Slots.firstMatching(player, Slots.QUIVER, s -> s.is(ItemTags.ARROWS));
Slots.allWorn(player);                      // every worn item in any slot (cosmetic twins excluded)
```

`firstMatching` and `allWorn` never look at cosmetic twins: a cosmetic item has no effect.

## Writing (server side)

```java
Slots.set(player, Slots.HOOK, 0, stack);         // replaces; no validity check; false if there is no such slot
Slots.setCosmetic(player, Slots.WINGS, 0, stack);
Slots.tryEquip(player, Slots.QUIVER, stack);     // first empty slot that allows it, as a right-click equip would
Slots.unequip(player, Slots.HOOK, 0);            // empties it and returns what was there
```

## Events

`fundamentum:slot_equipped` and `fundamentum:slot_unequipped` (`Events.SlotEquipped` / `SlotUnequipped`: entity, slot,
index, cosmetic, stack), posted on the server after the change, through `FEvents` like every Fundamentum event
([Events](events.md)). Replacing one item with another posts both.

- They are posted for every Curios slot, other mods' slots included, from Curios' own change check. That check runs as
  the entity ticks, so the events arrive on the next tick.
- Curios reports main slots only. A cosmetic change made with `Slots.set`, `setCosmetic` or `equip` posts the events
  itself (`cosmetic` true). One made by hand in Curios' screen posts nothing.

`Slots.onChange(entity -> ...)` is the plain listener for code that only needs to know something changed (both sides).

## Rendering

Renderers draw `Slots.shown(entity, slot)`: the cosmetic twin when it holds something, else the worn item, else empty.
Fundamentum's wings use it.

## More slot types

Add the slot as Curios data (`data/<ns>/curios/slots/<id>.json` and an `entities` file). `Slots` reads it with no
code. `Slots.define` is gone.

## Older API

`com.fundamentum.curios.Slots` still works and passes every call to `com.fundamentum.slots.Slots`; it is deprecated.

## Test

`gradlew runServer -Pslottest` (world under `run-slottest`) checks sizes and the cosmetic twin, validity by tag and
validator, set, get, tryEquip, firstMatching, shown, unequip, both events (a cosmetic twin's included) and that the
cosmetic armour screen adds no accessory slots. It ends with `SLOTTEST RESULT PASS` or `FAIL`.
