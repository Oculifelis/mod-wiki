# Tags and Curios slots

## Tags

| Tag | Kind | Meaning |
|---|---|---|
| `#fundamentum:creature/<type>` | entity type | [creature types](creatures.md) |
| `#fundamentum:showcase/still` | entity type | mobs that stand still in `/fundamentum showcase` |
| `#fundamentum:element/<e>` | damage type, item | damage of that [element](elements.md) / a weapon whose hits are |
| `#fundamentum:class/<c>` | damage type, item | damage class `melee`, `ranger`, `marksman` or `mage` / a bow, gun or staff whose projectiles take that class |
| `#fundamentum:whips` | item | whips (also counted as `#c:tools/whip`) |

## Curios slots

Fundamentum adds four Curios slots to players. An item goes in a slot through the item tag `#curios:<slot>`:

| Slot | Holds |
|---|---|
| `wings` | [wings](wings.md); has a cosmetic twin |
| `mount` | [mount items](mounts.md) |
| `hook` | [grappling hooks](hooks.md) |
| `summon` | [summon items](summons.md); gear can add more with Curios slot modifiers |

For example, `data/curios/tags/item/hook.json`:

```json
{"values": ["mymod:chain_hook"]}
```
