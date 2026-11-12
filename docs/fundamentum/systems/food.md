# Food hooks (`com.fundamentum.food`)

One event when a player eats or drinks, a pipeline that changes what a food gives before it applies, and food
groups from data. The same code runs on every version; the version differences sit in `com.fundamentum.port.FFood`.
Fundamentum adds no items, blocks or player data for this, and nothing changes until a mod uses it.

## Eating and drinking

A player finishing any food or drink (potions, milk, honey, modded drinks) goes through three steps:

1. `fundamentum:food_eaten` fires (`FoodEaten(player, stack, drink, nutrition, saturation, food)`). It is
   cancellable. A cancelled eat does nothing: the item stays in the hand and no hunger or effects apply.
2. Modifiers change the values (below), lowest priority first.
3. Vanilla applies the food, then Fundamentum moves hunger, saturation and effects to the modified values and fires
   `fundamentum:food_consumed` (`FoodConsumed(...)`, same fields, not cancellable).

    FEvents.listen(FoodEaten.class, (FoodEaten e, FEvents.Call call) -> {
        if (e.drink() && tooHot(e.player())) call.cancel();
    });
    FEvents.listen(FoodConsumed.class, (FoodConsumed e) -> remember(e.player(), e.stack()));

`FoodEaten` carries the values after modifiers, so a listener sees what the player is about to get. Only players on
the server count; mobs that eat are left alone. See [Events](events.md) for listening from data.

## Changing what food gives

    Food.modify((player, stack, food) -> food.withNutrition(food.nutrition() + 1));
    Food.modify(-10, (player, stack, food) -> food.scaled(0.5));   // runs before priority 0
    Food.removeModifier(myModifier);

`FoodValues(nutrition, saturation, drink, effects)` has `withNutrition`, `withSaturation`, `withEffects`,
`withEffect(effect, chance)` and `scaled(factor)`. Saturation is the points added to the player's saturation on
every version (1.20.1 food files store a modifier; Fundamentum converts it). Returning `food` leaves it alone, and
returning null is the same. A modifier can't turn a drink into food or the other way round. One that throws is
skipped and logged.

Hunger is still capped at 20 and saturation at the hunger level. Effects a modifier removes are taken off again
after vanilla applies them, and an effect the player already had before eating is put back the way it was.

    FoodValues base = Food.base(player, stack);     // the item's own values, or null
    FoodValues now = Food.values(player, stack);    // after every modifier
    boolean drink = Food.drink(stack);

## Food groups

`data/<namespace>/fundamentum/food_groups/<name>.json`:

    {
      "name": "food_group.mymod.fruits",
      "icon": "minecraft:apple",
      "color": "#D03030",
      "items": ["minecraft:apple", "#c:foods/berry"],
      "tags": ["diet:fruits"],
      "values": {"minecraft:golden_apple": 0.5},
      "exclude": ["minecraft:enchanted_golden_apple"],
      "guess": true
    }

| Field | Means | Default |
|---|---|---|
| `name` | translation key | `food_group.<ns>.<name>` |
| `icon`, `color` | for mods that show the group | none, white |
| `items` | items and `#` item tags fully in the group | none |
| `tags` | more item tags, with or without `#` | none |
| `values` | a share from 0 to 1 for single items | none |
| `exclude` | items and tags never in the group | none |
| `guess` | foods made from recipes count by their ingredients | true |
| `disabled` | a pack turns the group off by overriding the file | false |

Every group also reads the item tag `#<ns>:food_groups/<name>`. Fundamentum ships fruits, vegetables, proteins,
grains and sugars. Each lists the vanilla foods and reads the matching `diet:` tag and the common `c:` and `forge:`
food tags, so a mod that tags its foods for Diet or the common tags counts with no extra work.

A food named in no group gets a guess from its recipe: each ingredient that is in a group adds its share, averaged
over the ingredients that have any group, and only groups with `guess` on take part. It follows the first recipe it
finds, up to four steps deep. A cookie (wheat and cocoa) comes out as grains. Recipes come from the recipe JSON files,
so recipes made only in code are not seen. An item a group excludes is never guessed into it.

    Map<FId, Double> shares = FoodGroups.groups(stack);   // group id to share, empty when none
    boolean fruit = FoodGroups.in(stack, FId.of("fundamentum", "fruits"));
    double share = FoodGroups.value(stack, FId.of("fundamentum", "grains"));

Groups reload with datapacks. A broken file is left out and the log says why.

## Command

`/fundamentum food` (operators) gives the held item's hunger, saturation and effects after modifiers, and its groups.

## Test

`gradlew runServer -Pfoodtest` (world under `run-foodtest`) checks base values, plain eating, cancelling, modifier
order and errors, effect changes, drinks, the built-in groups, tags, values, excludes and recipe guesses, and the
command. It ends with `FOODTEST RESULT PASS` or `FAIL`.
