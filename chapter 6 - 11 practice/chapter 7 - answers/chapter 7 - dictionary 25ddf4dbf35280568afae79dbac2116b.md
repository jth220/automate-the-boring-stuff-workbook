# chapter 7 - dictionary

1.

```python
this_dict = {}
this_dict2 = dict()
```

2.

```python
this_dict = {’foo’:42}
```

3.

```python
#Dictionary - unordered and unsequential, data is collected as a key-value pair, accessed via keys (so order does not matter)
#List - ordered and sequential, elements are accessed via indexes (order is preserved)
```

4.

```python
#Trying to acess spamp['foo'] where it is not defined will give you a KeyError
```

5.

```python
#spam.keys() is used to view objects in the dictionary, because it returns an iterable object (list) cat is indeed found in keys and therefore returns True
```

6.

```python
#On the other hand, cat is a key, and is not found in values and therefore is False
```

7.

```python
setdefault() #used to insert key, value if they are not found in the dictionary, otherwise they return the value
```

8.

```python
pprint()
```

# 1) Chess Dictionary Validator

## Goal

Write `isValidChessBoard(board: dict[str, str]) -> bool` that validates a chessboard represented as a dict:

- **keys**: squares `'a1'..'h8'` (file `a–h`, rank `1–8`)
- **values**: piece codes `'wP','wN','wB','wR','wQ','wK','bP','bN','bB','bR','bQ','bK'`

## Rules

- Exactly **one** white king (`wK`) and **one** black king (`bK`).
- Each color: **≤ 16** pieces total.
- Each color: **≤ 8 pawns** (`wP`/`bP`).
- All squares valid (`a1..h8`), all piece codes valid.
- No other constraints (don’t enforce move legality or side to move).

## Starter

```python
def isValidChessBoard(board: dict[str, str]) -> bool:
    # 1) validate keys (squares)
    # 2) validate values (piece codes)
    # 3) count per color, pawns per color, kings per color
    # 4) enforce limits / exactly-one-king rule
    return False

```

## Minimal Test Cases

### Valid

```python
valid_start = {
  'a8':'bR','b8':'bN','c8':'bB','d8':'bQ','e8':'bK','f8':'bB','g8':'bN','h8':'bR',
  'a7':'bP','b7':'bP','c7':'bP','d7':'bP','e7':'bP','f7':'bP','g7':'bP','h7':'bP',
  'a1':'wR','b1':'wN','c1':'wB','d1':'wQ','e1':'wK','f1':'wB','g1':'wN','h1':'wR',
  'a2':'wP','b2':'wP','c2':'wP','d2':'wP','e2':'wP','f2':'wP','g2':'wP','h2':'wP'
}

```

### Invalid & Why

- **Bad square key**: `{'z9': 'wQ', 'e1':'wK', 'e8':'bK'}` → invalid square.
- **Bad piece code**: `{'e1':'wK', 'e8':'bKing'}` → invalid piece code.
- **Two white kings**: `{'e1':'wK','d1':'wK','e8':'bK'}` → >1 `wK`.
- **No black king**: `{'e1':'wK'}` → missing `bK`.
- **Too many pawns**: 9 `wP`s → pawn limit exceeded.
- **Too many pieces**: 17 white pieces → color total exceeded.

### Edge cases

- Empty dict `{}` → invalid (kings missing).
- Mixed case: `'Wp'` or `'WK'` → invalid (must match exact `'wP'` etc.).
- Extra unknown keys should fail even if kings/pawns are fine.

---

# 2) Fantasy Game Inventory + Loot Conversion

## Goal

- `display_inventory(inventory: dict[str,int]) -> None`
- `add_to_inventory(inventory: dict[str,int], added_items: list[str]) -> dict[str,int]`

### Data Model

Inventory is a dict like:

```python
{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

```

## Requirements

### `display_inventory`

- Print exactly:
    
    ```
    Inventory:
    12 arrow
    42 gold coin
    1 rope
    6 torch
    1 dagger
    Total number of items: 62
    
    ```
    
- Order doesn’t need to match above unless you choose to (you may keep insertion order).
- Sum the total and print at the end.

### `add_to_inventory`

- For each item string in `added_items`, increment its count in `inventory` (create if missing).
- Return the updated `inventory` object (mutating in place is fine if documented).

## Starters

```python
def display_inventory(inventory: dict[str, int]) -> None:
    # print header
    # iterate items and print "<count> <item>"
    # compute and print total
    ...

def add_to_inventory(inventory: dict[str, int], added_items: list[str]) -> dict[str, int]:
    # for each name in added_items: inventory[name] = inventory.get(name, 0) + 1
    # return inventory
    ...

```

## Test Data

```python
inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# After update:
# {'gold coin': 45, 'rope': 1, 'dagger': 1, 'ruby': 1}

```

**Expected `display_inventory(inv)` output after update:**

```
Inventory:
45 gold coin
1 rope
1 dagger
1 ruby
Total number of items: 48

```